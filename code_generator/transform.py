import re
from collections import defaultdict

import yaml
from bs4 import BeautifulSoup


def parse_input_fields(input_fields, enabler_fields):
    """
    Parses input fields with array-like notation (e.g., 'taxes[0][tax_id]') into nested dictionaries and lists.
    Marks fields as non-required if they have an associated enabler.

    :param input_fields: A dictionary where the keys are input field names and the values are the corresponding values.
    :param enabler_fields: A set of fields that are marked as having enablers.
    :return: A structured dictionary representing the nested data and a list of required fields.
    """
    result = defaultdict(lambda: defaultdict(dict))
    required_fields = []

    array_pattern = re.compile(r"(\w+)\[(\d+)\]\[(\w+)\]")

    for key, value in input_fields.items():
        match = array_pattern.match(key)
        if match:
            array_name, index, sub_key = match.groups()
            result[array_name][int(index)][sub_key] = value
            if key not in enabler_fields:
                required_fields.append(key)
        else:
            result[key] = value
            if key not in enabler_fields:
                required_fields.append(key)

    # Convert defaultdict to regular dict and handle lists
    final_result = {}
    for key, val in result.items():
        if isinstance(val, defaultdict):
            final_result[key] = [val[idx] for idx in sorted(val)]
        else:
            final_result[key] = val

    # Remove array indices from required fields
    required_fields = [re.sub(r"\[\d+\]", "", key) for key in required_fields]

    return final_result, list(set(required_fields))


def generate_schema_definitions(parsed_fields, required_fields):
    """
    Generate schema definitions for complex objects (arrays of dictionaries).
    """
    definitions = {}
    properties = {}

    for key, val in parsed_fields.items():
        if isinstance(val, list):
            # Assume all items in the list have the same structure
            item_schema = {sub_key: {"type": "string"} for sub_key in val[0].keys()}
            definitions[key] = {"type": "object", "properties": item_schema}
            properties[key] = {
                "type": "array",
                "items": {"$ref": f"#/components/schemas/{key}"},
            }
        else:
            properties[key] = {"type": "string"}

    return properties, definitions, required_fields


def extract_api_data(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    paths = {}
    schemas = {}

    # Find all action holders
    for action_holder in soup.find_all("div", class_="action_holder"):
        # Extract the action title
        action_title = action_holder.find("div", class_="action_title").text.strip()

        # Extract the URL
        action_url_div = action_holder.find("div", class_="action_url")
        if not action_url_div:
            continue
        action_url = action_url_div.text.strip()

        # Extract the method from the form
        form = action_holder.find("form")
        if form:
            http_method = form.get("method", "get").lower()
        else:
            http_method = "get" if "?" in action_url else "post"

        # Default assumptions
        summary = action_title

        # Extract path and query parameters
        query_params = []
        if "?" in action_url:
            path, query_string = action_url.split("?", 1)
            parameters = query_string.split("&")
            for param in parameters:
                param_name = param.split("=")[0]
                query_params.append(
                    {
                        "in": "query",
                        "name": param_name,
                        "required": True,
                        "schema": {"type": "string"},
                    }
                )
        else:
            path = action_url

        # Collect body parameters
        body_parameters = {}
        input_fields = {}
        enabler_fields = set()

        if form and http_method == "post":
            # Extract input fields directly in the form
            for input_tag in form.find_all("input"):
                if "name" not in input_tag.attrs:
                    continue
                if input_tag["type"] == "hidden":
                    continue  # Skip hidden inputs as they are not user parameters
                param_name = input_tag["name"]

                # Check if this input has an enabler (checkbox) and add to the set
                if param_name.endswith("_enablee"):
                    checkbox_id = param_name.replace("_enablee", "_enabler")
                    if form.find("input", {"id": checkbox_id, "type": "checkbox"}):
                        enabler_fields.add(param_name)

                input_fields[param_name] = (
                    "string"  # Assume all form inputs are strings for simplicity
                )

            # Extract additional fields within <ul>
            for li_tag in form.find_all("li"):
                label = li_tag.find("label")
                input_tag = li_tag.find("input")
                if label and input_tag and "name" in input_tag.attrs:
                    param_name = input_tag["name"]
                    id_name = input_tag["id"]
                    # Check for enabler here as well
                    if id_name.endswith("_enablee"):
                        checkbox_id = id_name.replace("_enablee", "_enabler")
                        if form.find("input", {"id": checkbox_id, "type": "checkbox"}):
                            enabler_fields.add(param_name)

                    input_fields[param_name] = (
                        "string"  # Assume all inputs are strings for simplicity
                    )

            # Parse input fields to handle array-like notation
            parsed_fields, required_fields = parse_input_fields(
                input_fields, enabler_fields
            )

            # Generate the schema definitions and update the body parameters
            properties, definitions, required_fields = generate_schema_definitions(
                parsed_fields, required_fields
            )
            body_parameters.update(properties)
            schemas.update(definitions)

        # Constructing the path item for OpenAPI
        if body_parameters:
            request_body = {
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": body_parameters,
                            "required": required_fields,
                        }
                    }
                }
            }
        else:
            request_body = None

        # Prepare the path_info for this method
        path_item = {
            http_method: {
                "summary": summary,
                "responses": {
                    "200": {
                        "description": "Successful response",
                        "content": {"application/json": {"schema": {"type": "object"}}},
                    },
                    "400": {"description": "Bad request"},
                    "401": {"description": "Unauthorized"},
                    "500": {"description": "Internal server error"},
                },
            }
        }

        if request_body:
            path_item[http_method]["requestBody"] = request_body

        # Add to paths dictionary, ensuring we don't overwrite existing paths
        path = path.replace("https://api.moloni.pt/sandbox", "")
        if path in paths:
            paths[path].update(path_item)
        else:
            paths[path] = path_item

    return paths, schemas


def create_openapi_spec(paths, schemas):
    openapi_spec = {
        "openapi": "3.0.0",
        "info": {"title": "Moloni API", "version": "1.0.0"},
        "paths": paths,
        "components": {"schemas": schemas},
    }

    return openapi_spec


def main():
    for i in range(1, 7):
        # Load the HTML file
        with open(f"./{i}.html", "r") as file:
            html_content = file.read()

        # Extract API data from HTML
        paths, schemas = extract_api_data(html_content)

        if not paths:
            print("No paths were found. Please check the HTML structure.")
            return

        # Create OpenAPI specification
        openapi_spec = create_openapi_spec(paths, schemas)

        # Write the OpenAPI specification to a YAML file
        with open(f"./{i}.yaml", "w") as yaml_file:
            yaml.dump(openapi_spec, yaml_file, default_flow_style=False)

        print("OpenAPI specification generated successfully!")


if __name__ == "__main__":
    main()

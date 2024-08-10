import re
import subprocess

import inflection
import yaml
from jinja2 import Template


class OpenAPIClientGenerator:
    class_template = Template(
        '''
from pydantic import BaseModel, ValidationError
from typing import Union, Optional

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data


{% for model_name, model_code in models.items() %}
{{ model_code }}
{% endfor %}

class {{ class_name }}(MoloniBaseClient):        
    {% for method_name, details in methods.items() %}
    @endpoint('/<version>{{ details['path'] }}', method='{{ details['method'] }}')
    def {{ method_name }}(self{% if details['model_name'] != 'dict' %}, data: Union[{{ details['model_name'] }}, dict], {% else %}, {% endif %}**kwargs):
        """
        {{ method_name }}(self{% if details['model_name'] != 'dict' %}, data: Union[{{ details['model_name'] }}, dict], {% else %}, {% endif %}**kwargs)
        
        Args:
            {% if details['model_name'] != 'dict' %}
            data (Union[{{ details['model_name'] }}, dict]): A model instance or dictionary containing the following fields:
            {% for param_name, param_type in details['params'].items() %}
                - {{ param_name }} ({{ param_type }}): {{ param_name }} of the {{ details['model_name'] }}.
            {% endfor %}
            {% endif %}

        Returns:
            ApiResponse: The response from the API.
        """
        {% if details['model_name'] != 'dict' %}
        data = validate_data(data, self.validate, {{ details['model_name'] }})

        return self._request(fill_query_params(kwargs.pop('path'), self.version), data={**data, **kwargs})
        {% else %}
        return self._request(fill_query_params(kwargs.pop('path'), self.version), data={**kwargs})
        {% endif %}
    {% endfor %}
'''
    )

    def __init__(self, openapi_spec_path):
        with open(openapi_spec_path, "r") as file:
            self.openapi_spec = yaml.safe_load(file)
        self.client_classes = {}

    def generate_class_name(self, path):
        return "".join(word.capitalize() for word in path.split("/")[1:2]) + "Client"

    def sanitize_method_name(self, summary):
        summary = summary.strip()
        summary = re.sub(r"[^\w\s]", "", summary)
        method_name = re.sub(r"\s+", "_", summary)
        return inflection.underscore(method_name).lstrip("_")

    def generate_pydantic_model(self, model_name, properties, required_fields):
        fields = {}
        for prop_name, prop_details in properties.items():
            field_type = (
                "Union[str, int]"
                if prop_name.endswith("_id") or prop_name in ("qty", "offset")
                else "str"
            )  # Default type is string for simplicity
            field_type = "bool" if prop_name.startswith("is_") else field_type
            field_type = (
                f"Optional[{field_type}]"
                if prop_name not in required_fields
                else field_type
            )

            if prop_name in required_fields:
                fields[prop_name] = (field_type, ...)  # Required fields
            elif prop_name in ("qty", "offset"):
                fields[prop_name] = (field_type, 25 if prop_name == "qty" else 0)
            else:
                fields[prop_name] = (field_type, None)  # Optional fields

        model_code = f"class {model_name}(BaseModel):\n"
        for field_name, (field_type, default_value) in sorted(
            fields.items(), key=lambda x: x[0] in required_fields, reverse=True
        ):
            model_code += f"    {field_name}: {field_type}"
            if field_name not in required_fields and field_name not in (
                "qty",
                "offset",
            ):
                model_code += f" = {default_value}"
            if field_name in ("qty", "offset"):
                model_code += f" = {25 if field_name == 'qty' else 0}"
            model_code += "\n"

        return model_code.strip()

    def parse_paths(self):
        for path, path_details in self.openapi_spec["paths"].items():
            class_name = self.generate_class_name(path)
            if class_name not in self.client_classes:
                self.client_classes[class_name] = {"methods": {}, "models": {}}

            for method, method_details in path_details.items():
                method_name = self.sanitize_method_name(method_details["summary"])
                body_params = (
                    method_details.get("requestBody", {})
                    .get("content", {})
                    .get("application/json", {})
                    .get("schema", {})
                    .get("properties", {})
                )
                required_fields = (
                    method_details.get("requestBody", {})
                    .get("content", {})
                    .get("application/json", {})
                    .get("schema", {})
                    .get("required", [])
                )

                if body_params:
                    model_name = f"{re.sub('Client$', '', class_name)}{inflection.camelize(method_name)}Model"
                    model_code = self.generate_pydantic_model(
                        model_name, body_params, required_fields
                    )
                    params = {
                        param: (
                            "Union[str, int]"
                            if param.endswith("_id")
                            else "bool" if param.startswith("is_") else "str"
                        )
                        for param in body_params.keys()
                    }
                else:
                    model_name = "dict"  # Fallback if no model is generated
                    model_code = None
                    params = {}

                self.client_classes[class_name]["methods"][method_name] = {
                    "method": method,
                    "path": path,
                    "params": params,
                    "summary": method_details.get("summary", ""),
                    "model_name": model_name,
                }

                if model_code:
                    self.client_classes[class_name]["models"][model_name] = model_code

    def generate_code(self):
        self.parse_paths()
        generated_files = []

        for class_name, details in self.client_classes.items():
            rendered_class = self.class_template.render(
                class_name=class_name,
                methods=details["methods"],
                models=details["models"],
            )
            file_name = f"../moloni/api/{inflection.underscore(class_name)}.py"
            with open(file_name, "w") as f:
                f.write(rendered_class.strip())
                print(f"Generated {class_name}.py")
            generated_files.append(file_name)

        return generated_files

    def format_code_with_black(self, files):
        try:
            subprocess.run(["black"] + files, check=True)
            print("Code formatted with Black successfully!")
        except subprocess.CalledProcessError as e:
            print(f"Error formatting code with Black: {e}")

    def update_init_file(self, files):
        new_imports = []
        new_exports = []

        # Collect imports and names to export from the generated classes
        for class_name, details in self.client_classes.items():
            class_import = (
                f"from .{inflection.underscore(class_name)} import {class_name}"
            )
            new_imports.append(class_import)
            new_exports.append(class_name)

            for model_name in details["models"].keys():
                model_import = (
                    f"from .{inflection.underscore(class_name)} import {model_name}"
                )
                new_imports.append(model_import)
                new_exports.append(model_name)

        # Read the existing __init__.py file if it exists
        try:
            with open("../moloni/api/__init__.py", "r") as init_file:
                init_lines = init_file.readlines()
        except FileNotFoundError:
            init_lines = []

        # Prepare lists for existing imports and the __all__ list
        existing_imports = []
        existing_all = []
        in_all_section = False

        # Parse the existing __init__.py content
        for line in init_lines:
            stripped_line = line.strip()

            # Identify existing imports
            if stripped_line.startswith("from .") and "import" in stripped_line:
                existing_imports.append(stripped_line)

            # Identify and parse the __all__ list
            if stripped_line.startswith("__all__"):
                in_all_section = True
                all_items = re.findall(r'"(.*?)"', stripped_line)
                existing_all.extend(all_items)
            elif in_all_section:
                all_items = re.findall(r'"(.*?)"', stripped_line)
                if all_items:
                    existing_all.extend(all_items)
                if stripped_line.endswith("]"):
                    in_all_section = False

        # Combine and deduplicate imports and exports
        all_imports = list(set(existing_imports + new_imports))
        all_exports = list(set(existing_all + new_exports))

        # Sort imports and exports for consistency
        all_imports.sort()
        all_exports.sort()

        # Create the updated __init__.py content
        new_init_content = "\n".join(all_imports) + "\n\n__all__ = [\n"
        new_init_content += ",\n".join([f'"{name}"' for name in all_exports])
        new_init_content += "\n]\n"

        # Write back the updated __init__.py
        with open("../moloni/api/__init__.py", "w") as init_file:
            init_file.write(new_init_content)
        print("__init__.py has been updated with the generated classes and models.")


if __name__ == "__main__":
    for i in range(1, 7):
        generator = OpenAPIClientGenerator(f"{i}.yaml")
        files = generator.generate_code()
        generator.format_code_with_black(files)
        generator.update_init_file(files)
    generator.format_code_with_black(["../moloni/api/__init__.py"])

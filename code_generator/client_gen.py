import os
import re
import subprocess

import inflection
import yaml
from jinja2 import Template


class OpenAPIClientGenerator:
    class_template = Template(
        '''
from pydantic import BaseModel, ValidationError
from typing import Union, Optional, List, Any

from moloni.base.client import MoloniBaseClient
from moloni.base.helpers import endpoint, fill_query_params, validate_data 
from moloni.base import ApiResponse


class ApiRequestModel(BaseModel):
    _api_client: Any = None

    def connect(self, *args, **kwargs):
        self._api_client = {{ class_name }}(*args, **kwargs)
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


{% for model_name, model_code in components.items() %}
{{ model_code }}
{% endfor %}


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
    test_template = Template(
        """
import unittest
from unittest.mock import patch, Mock
from requests import Response
from moloni.api.{{ module_name|lower }} import {{ class_name }}{% if model_imports %}, {{ model_imports }}{% endif %}
from moloni.base import ApiResponse, NoMoreRecords


class Test{{ class_name }}(unittest.TestCase):
    def setUp(self):
        self.client = {{ class_name }}()

    {% for method_name, details in methods.items() %}
    @patch.object(
        {{ class_name }},
        "_request"
    )
    def test_{{ method_name }}(self, mock_request):
        # Mock the Response object
        mock_response = Mock(spec=Response)
        mock_response.json.return_value = {"some_key": "some_value"}
        mock_response.status_code = 200
        mock_response.headers = {"Content-Type": "application/json"}

        # Create the ApiResponse object with the mocked Response
        mock_request.return_value = ApiResponse(
            response=mock_response,
            request_data={"qty": 10, "offset": 0}
        )

        {% if details['model_name'] != 'dict' %}
        model_data = {{ details['model_name'] }}(
            {% for param_name, param_type in details['params'].items() %}
            {% if param_name in ['products', 'warehouse', 'taxes', 'associated_documents', 'payments', 'suppliers', 'warehouses'] %}
            {{ param_name }}=[],
            {% else %} {{ param_name }}={% if param_type == 'str' %}"{{ param_name }}"{% elif param_type.startswith('Optional[List') %}[]{% elif param_type == 'int' %}1{% elif param_type == 'float' %}1.0{% elif param_type == 'bool' %}True{% else %}"sample_value"{% endif %},
            {% endif %}
            {% endfor %}
        )
        response = self.client.{{ method_name }}(data=model_data)
        {% else %}
        response = self.client.{{ method_name }}()
        {% endif %}
        
        # Assertions
        self.assertIsInstance(response, ApiResponse)
        self.assertEqual(response.payload, {"some_key": "some_value"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        mock_request.assert_called_once()

        # Test pagination functionality
        try:
            next_params = response.next(qty=5)
            self.assertEqual(next_params["offset"], 10)
            self.assertEqual(next_params["qty"], 5)
        except NoMoreRecords:
            pass
        
    {% endfor %}
"""
    )

    def __init__(self, openapi_spec_path):
        with open(openapi_spec_path, "r") as file:
            self.openapi_spec = yaml.safe_load(file)
        self.client_classes = {}

    def generate_test_code(self, module_name, class_name, methods, models):
        model_imports = ", ".join(models.keys())

        test_code = self.test_template.render(
            module_name=module_name,
            class_name=class_name,
            methods=methods,
            models=models,
            model_imports=model_imports,
        )
        return test_code

    def generate_class_name(self, path):
        return "".join(word.capitalize() for word in path.split("/")[1:2]) + "Client"

    def sanitize_method_name(self, summary):
        summary = summary.strip()
        summary = re.sub(r"[^\w\s]", "", summary)
        method_name = re.sub(r"\s+", "_", summary)
        return inflection.underscore(method_name).lstrip("_")

    def generate_pydantic_model(
        self, model_name, properties, required_fields, method_name
    ):
        required_fields = ["company_id"]
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

            if prop_details.get("type") == "array":
                field_type = f"Optional[List[{prop_details.get('items').get('$ref').split('/')[-1].capitalize()}]]"

            if prop_name in required_fields:
                fields[prop_name] = (field_type, ...)  # Required fields
            elif prop_name in ("qty", "offset"):
                fields[prop_name] = (field_type, 25 if prop_name == "qty" else 0)
            else:
                fields[prop_name] = (field_type, None)  # Optional fields

        model_code = f"class {model_name}(ApiRequestModel):\n"
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

        model_code += "\n"
        model_code += f'''
    def request(self) -> ApiResponse:
        """
        request(self) -> ApiResponse
        
        Make an API request using the initialized client.
    
        This method checks if the `_api_client` attribute is set (i.e., if the client has been initialized via the `connect` method). 
        If the client is initialized, it will make an API request using the provided method name and the model's data, 
        excluding the `_api_client` attribute itself from the request payload. If the client is not initialized, it will raise a `ValueError`.
    
        Returns:
            The response from the API.
    
        Raises:
            ValueError: If the client is not initialized via the `connect` method.
    
        Example:
            # Assuming you have a model instance `request_model` and an API client `api_client`
            with request_model.connect(auth_config=auth_config) as api:
                response = api.request()
    
            # The above example assumes that the `connect` method has been used to initialize the client.
            # The request method then sends the model's data to the API and returns the API's response.
        """
        if hasattr(self, "_api_client"):
            response = self._api_client.{method_name}(
                self.model_dump(exclude={{"_api_client"}}, exclude_unset=True)
            )
            return response
        else:
            raise ValueError("Client not initialized. Use the 'connect' method.")
'''

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
                        model_name, body_params, required_fields, method_name
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
            module_name = inflection.underscore(class_name)
            rendered_class = self.class_template.render(
                class_name=class_name,
                methods=details["methods"],
                models=details["models"],
                components=self.generate_components(),
            )

            file_name = f"../moloni/api/{inflection.underscore(class_name)}.py"
            with open(file_name, "w") as f:
                f.write(rendered_class.strip())
                print(f"Generated {class_name}.py")
            generated_files.append(file_name)

            test_code = self.generate_test_code(
                module_name, class_name, details["methods"], details["models"]
            )
            test_file_name = f"../tests/{module_name}_test.py"
            with open(test_file_name, "w") as f:
                f.write(test_code.strip())
                print(f"Generated {module_name}_test.py")
            generated_files.append(test_file_name)

        return generated_files

    def generate_components(self):
        components = self.openapi_spec["components"]["schemas"]

        # Dictionary to store generated model classes
        models = {}

        # Function to convert OpenAPI type to Python type
        def get_python_type(openapi_type):
            # if openapi_type == "string":
            #     return "str"
            # if openapi_type == "integer":
            #     return "int"
            # if openapi_type == "boolean":
            #     return "bool"
            # if openapi_type == "number":
            #     return "float"
            return "Optional[Any]"

        # Generate Pydantic models from OpenAPI components
        for model_name, model_info in components.items():
            properties = model_info.get("properties", {})
            fields = []

            for field_name, field_info in properties.items():
                python_type = get_python_type(field_info["type"])
                fields.append(f"    {field_name}: {python_type} = None")

            model_str = (
                f"class {model_name.capitalize()}(BaseModel):\n"
                + "\n".join(fields)
                + "\n"
            )
            models[model_name] = model_str

        # Output the generated models
        for model_name, model_code in models.items():
            print(model_code)
        return models

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

            for model_name, code in self.generate_components().items():
                model_import = f"from .{inflection.underscore(class_name)} import {model_name.capitalize()} as {class_name}{model_name.capitalize()}Model"
                new_imports.append(model_import)
                new_exports.append(f"{class_name}{model_name.capitalize()}Model")

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
            init_file.write(
                "\n".join(
                    "/n".join(
                        new_init_content.split(
                            "from .users_client import UsersUpdateMeModel"
                        )
                    ).split('"UsersUpdateMeModel",')
                )
            )
        print("__init__.py has been updated with the generated classes and models.")


if __name__ == "__main__":
    os.unlink("../moloni/api/__init__.py")
    for i in range(1, 7):
        generator = OpenAPIClientGenerator(f"{i}.yaml")
        files = generator.generate_code()
        generator.format_code_with_black(files)
        generator.update_init_file(files)
    generator.format_code_with_black(["../moloni/api/__init__.py"])

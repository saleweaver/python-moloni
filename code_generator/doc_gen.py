import os
import re
from pathlib import Path


def extract_class_names(file_content):
    """
    Extract class names from the file content.
    This includes both BaseModel (Pydantic models) and Client classes.
    """
    # Regular expression to match class definitions
    class_pattern = re.compile(r"class (\w+)\(.*\):")

    # Extract class names
    classes = class_pattern.findall(file_content)

    # Identify which classes are models (BaseModel) and which is the client
    base_models = []
    client_name = None

    for class_name in classes:
        if "Client" in class_name:
            client_name = class_name
        else:
            base_models.append(class_name)

    return base_models, client_name


def generate_documentation_file(base_models, client_name, module_name, output_dir):
    """
    Generate the documentation content based on the extracted class names.
    """
    if not client_name:
        return

    doc_content = f"{client_name}\n{'=' * len(client_name)}\n\n"

    doc_content += f".. autoclass:: moloni.api.{client_name}\n\n"

    doc_content += f"Models:\n{'-' * len('Models:')}\n\n"
    for model in base_models:
        doc_content += f".. autoclass:: moloni.api.{model}\n\n"

    # Write to the documentation file
    output_path = Path(output_dir) / f"{module_name}.rst"
    with open(output_path, "w") as f:
        f.write(doc_content)
    print(f"Documentation file created: {output_path}")


def main(api_dir, output_dir):
    """
    Main function to process all Python files in the api/ directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(api_dir):
        if file_name == "__init__.py":
            continue
        if file_name.endswith(".py"):
            file_path = os.path.join(api_dir, file_name)
            module_name = file_name[:-3]  # Remove the .py extension

            with open(file_path, "r") as file:
                file_content = file.read()

            base_models, client_name = extract_class_names(file_content)
            generate_documentation_file(
                base_models, client_name, module_name, output_dir
            )


if __name__ == "__main__":
    api_dir = "../moloni/api/"  # Directory containing the Python files
    output_dir = "../docs/endpoints"  # Output directory for the documentation files
    main(api_dir, output_dir)

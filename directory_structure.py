import os
import json
import yaml


def read_gitignore(start_path):
    gitignore_path = os.path.join(start_path, ".gitignore")
    to_ignore = [
        ".env",
        "__pycache__",
        ".pytest_cache",
        ".vscode",
        ".git",
    ]

    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as gitignore_file:
            lines = gitignore_file.readlines()
            for line in lines:
                line = line.strip()
                if line and not line.startswith("#"):
                    to_ignore.append(line)

    return to_ignore


def generate_directory_structure(start_path, output_format="json"):
    if not os.path.exists(start_path):
        print(f"Error: The specified directory '{start_path}' does not exist.")
        return None

    structure = {}
    to_ignore = read_gitignore(start_path)

    for dirpath, dirnames, filenames in os.walk(start_path):
        for r in to_ignore:
            if r in dirnames:
                dirnames.remove(r)

        current_dir = structure
        path_components = os.path.relpath(dirpath, start_path).split(os.path.sep)

        for component in path_components:
            if component not in current_dir:
                current_dir[component] = {}
            current_dir = current_dir[component]

        for filename in filenames:
            current_dir[filename] = None

    if output_format == "json":
        return json.dumps(structure, indent=4)
    elif output_format == "yaml":
        return yaml.dump(structure, default_flow_style=False)
    elif output_format == "txt":
        return generate_txt_structure(structure, "")


def generate_txt_structure(structure, indentation):
    result = ""
    for key, value in structure.items():
        if value is None:
            result += indentation + f"- {key}\n"
        else:
            result += indentation + f"- {key}:\n"
            result += generate_txt_structure(value, indentation + "  ")
    return result


def save_structure_to_file(output_file, structure):
    with open(output_file, 'w') as file:
        file.write(structure)

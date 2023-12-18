import os
import json
import argparse
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


def generate_directory_structure(start_path, output_file, output_format):
    if not os.path.exists(start_path):
        print(f"Error: The specified directory '{start_path}' does not exist.")
        return

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
        with open(output_file, 'w') as json_file:
            json.dump(structure, json_file, indent=4)
    elif output_format == "yaml":
        with open(output_file, 'w') as yaml_file:
            yaml.dump(structure, yaml_file, default_flow_style=False)
    elif output_format == "txt":
        with open(output_file, 'w') as txt_file:
            generate_txt_structure(txt_file, structure, "")

def generate_txt_structure(file, structure, indentation):
    for key, value in structure.items():
        if value is None:
            file.write(indentation + f"- {key}\n")
        else:
            file.write(indentation + f"- {key}:\n")
            generate_txt_structure(file, value, indentation + "  ")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a directory structure in different formats.")
    parser.add_argument("directory", nargs="?", default=os.getcwd(), help="The directory to inspect.")
    parser.add_argument("-o", "--output", help="The output file name.")
    parser.add_argument("-f", "--format", choices=["json", "yaml", "txt"], default="json", help="The output file format.")

    args = parser.parse_args()

    start_path = args.directory
    output_file = args.output
    output_format = args.format

    if output_file is None:
        # Use the directory name as the default output file name
        output_file = os.path.basename(start_path)

    # Convert relative path to absolute path if necessary
    start_path = os.path.abspath(start_path)

    if output_format == "json":
        output_file += '.json'
    elif output_format == "yaml":
        output_file += '.yaml'
    elif output_format == "txt":
        output_file += '.txt'

    generate_directory_structure(start_path, output_file, output_format)

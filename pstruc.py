import os
import json
import argparse
import sys


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


def generate_directory_structure(start_path, output_file):
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

    with open(output_file, 'w') as json_file:
        json.dump(structure, json_file, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a directory structure in JSON format.")
    parser.add_argument("directory", nargs="?", default=os.getcwd(), help="The directory to inspect.")
    parser.add_argument("-o", "--output", help="The output JSON file name.")

    args = parser.parse_args()

    start_path = args.directory
    output_file = args.output


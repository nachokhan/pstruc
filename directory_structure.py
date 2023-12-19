import os
import json
import yaml


def generate_directory_structure(start_path, output_format="json"):
    """
    Generate a directory structure for the specified directory.

    Args:
        start_path (str): The directory to inspect.
        output_format (str): The desired output format ('json', 'yaml', or 'txt').

    Returns:
        str: The directory structure in the specified format.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
    """
    try:
        if not os.path.exists(start_path):
            raise FileNotFoundError(f"The specified directory '{start_path}' does not exist.")

        structure = {}
        to_ignore = _read_gitignore(start_path)

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
            return _generate_txt_structure(structure, "")

    except Exception as e:
        return f"Error: {str(e)}"


def save_structure_to_file(output_file, structure):
    """
    Save the directory structure to a file.

    Args:
        output_file (str): The name of the output file.
        structure (str): The directory structure content to be saved.

    Returns:
        str: An error message if an error occurs during file saving; otherwise, None.
    """
    try:
        with open(output_file, 'w') as file:
            file.write(structure)
        return None  # No error occurred
    except Exception as e:
        return f"Error: {str(e)}"


def _read_gitignore(start_path):
    """
    Read patterns from a .gitignore file in the specified directory.

    Args:
        start_path (str): The directory to read .gitignore from.

    Returns:
        list: List of patterns to be ignored.
    """
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


def _generate_txt_structure(structure, indentation):
    """
    Generate a plain text representation of the directory structure.

    Args:
        structure (dict): The directory structure.
        indentation (str): The current indentation level.

    Returns:
        str: The plain text representation of the directory structure.
    """
    result = ""
    for key, value in structure.items():
        if value is None:
            result += indentation + f"- {key}\n"
        else:
            result += indentation + f"- {key}:\n"
            result += _generate_txt_structure(value, indentation + "  ")
    return result

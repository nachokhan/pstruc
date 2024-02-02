import os
import json
import yaml
import fnmatch
from pstruc._file_structure import read_file


def generate_directory_structure(start_path, output_format="json", to_ignore=[], to_add_content=[]):
    """
    Generate a directory structure for the specified directory.

    Args:
        start_path (str): The directory to inspect.
        output_format (str): The desired output format ('json', 'yaml', 'txt', 'dict').
        to_ignore (list): List of patterns to ignore.
        file_content (list): List of patterns to determine which file content to include in the structure.

    Returns:
        str: The directory structure in the specified format.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
    """
    formatted_structure = None
    try:
        if not os.path.exists(start_path):
            raise FileNotFoundError(f"The specified directory '{start_path}' does not exist.")

        structure = {}

        for dirpath, dirnames, filenames in os.walk(start_path):
            # Exclude files and folders that match ignore patterns
            dirnames[:] = [d for d in dirnames if not any(fnmatch.fnmatchcase(d, pattern) for pattern in to_ignore)]
            filenames[:] = [f for f in filenames if not any(fnmatch.fnmatchcase(f, pattern) for pattern in to_ignore)]

            current_dir = structure
            path_components = os.path.relpath(dirpath, start_path).split(os.path.sep)

            for component in path_components:
                if component not in current_dir:
                    current_dir[component] = {}
                current_dir = current_dir[component]

            for filename in filenames:
                if to_add_content and any(fnmatch.fnmatchcase(filename, pattern) for pattern in to_add_content):
                    content = read_file(os.path.join(dirpath, filename))
                    current_dir[filename] = content
                else:
                    current_dir[filename] = None

        formatted_structure = _format_structure(structure, output_format)

        return formatted_structure

    except Exception as e:
        raise e


def _format_structure(structure, format):
    formatted_structure = structure
    if format == "json":
        formatted_structure = json.dumps(structure, indent=4)
    elif format == "yaml":
        formatted_structure = yaml.dump(structure, default_flow_style=False)
    elif format == "txt":
        formatted_structure = _generate_txt_structure(structure, "")

    return formatted_structure


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
        if isinstance(structure, dict):
            structure = _format_structure(structure, "json")

        with open(output_file, 'w') as file:
            file.write(structure)
    except Exception as e:
        raise e


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

import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from _directory_structure import generate_directory_structure
from _pretty_structure import pretty_print


if __name__ == "__main__":
    # Get the root directory of the project
    root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    structure = generate_directory_structure(root_directory, "json")

    if structure is not None:
        # Pretty print the structure with colors
        pretty_print(structure)
    else:
        print("Failed to parse the directory structure string.")

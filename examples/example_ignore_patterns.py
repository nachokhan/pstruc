import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from pstruc import get_project_structure, save_structure_to_file
from pstruc.file_tools import get_all_ignore_patterns


if __name__ == "__main__":
    # Specify the directory path and output format
    start_path = os.getcwd()
    output_format = "dict"

    # Optional: Specify additional files/folders to ignore
    ignore_patterns = get_all_ignore_patterns(
        start_path,
        [".gitignore", "/var/lalala/jeje.json"],
        [".git"]
    )

    try:
        # Generate the directory structure
        structure = get_project_structure(
            ".",
            output_format,
            ignore_patterns,
            to_add_content=["*.py", "README.md"],
        )

        # Specify the output file name (optional)
        output_file = "output_structure.json"

        # Save the directory structure to a file (optional)
        save_structure_to_file(output_file, structure)
        print(f"Directory structure has been generated and saved to '{output_file}'.")
    except Exception as e:
        print(e)  # Handle any errors

import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from pstruc import get_project_structure, save_structure_to_file


if __name__ == "__main__":
    # Specify the directory path and output format
    start_path = "/Users/nacho/dev/proyectos/project-structure"
    output_format = "json"

    # Optional: Specify additional files/folders to ignore
    ignore_patterns = ["*.png", "*.md", "*req*", "pstruc.egg-info", ".git", "LICENSE", "dist", "test", "examples", ".github", "*ignore*"]

    # Generate the directory structure
    structure = get_project_structure(
        ".",
        output_format,
        ignore_patterns,
        file_content=["*.py"],
    )

    if "Error" in structure:
        print(structure)  # Handle any errors
    else:
        # Specify the output file name (optional)
        output_file = "output_structure.json"

        # Save the directory structure to a file (optional)
        error = save_structure_to_file(output_file, structure)
        if error:
            print(error)  # Handle any errors
        else:
            print(f"Directory structure has been generated and saved to '{output_file}'.")

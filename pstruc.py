import argparse
import os
from directory_structure import generate_directory_structure
from directory_structure import save_structure_to_file


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
        directory_name = os.path.basename(os.path.normpath(start_path))
        output_file = directory_name

    # Convert relative path to absolute path if necessary
    start_path = os.path.abspath(start_path)

    if output_format == "json":
        output_file += '.json'
    elif output_format == "yaml":
        output_file += '.yaml'
    elif output_format == "txt":
        output_file += '.txt'

    structure = generate_directory_structure(start_path, output_format)

    if structure is not None:
        # If called from the command line, create the output file
        save_structure_to_file(output_file, structure)
        print(f"Directory structure has been generated and saved to '{output_file}'.")

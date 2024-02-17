import argparse
import os
import sys
from pstruc._directory_structure import generate_directory_structure as get_project_structure
from pstruc._directory_structure import save_structure_to_file
from pstruc._pretty_structure import pretty_print
from pstruc.file_tools import get_all_ignore_patterns


def main():
    parser = argparse.ArgumentParser(description="Generate a directory structure in different formats.")
    parser.add_argument("directory", nargs="?", default=os.getcwd(), help="The directory to inspect.")
    parser.add_argument("-o", "--output", help="The output file name.")
    parser.add_argument("-f", "--format", choices=["json", "yaml", "txt"], default="yaml", help="The output file format.")
    parser.add_argument("-p", "--print", action="store_true", help="Print the directory structure without saving it.")
    parser.add_argument("-ns", "--not-save", action="store_true", help="Structure won't be saved in output file.")
    parser.add_argument("-ip", "--add-ignore-patterns", help="A comma-separated list of patterns to ignore (in addition to .gitignore).")
    parser.add_argument("-iff", "--ignore-from-files", help="A comma-separated list of file names to get the ignore patterns from")
    parser.add_argument("-igi", "--ignore-git-ignore", action="store_true", help="Ignore the patterns inside .gitignore file (if present)")
    parser.add_argument("-fc", "--add-content-file-patterns", help="A comma-separated list of patterns for files to add its content.")

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

    patterns_to_ignore = None
    if args.add_ignore_patterns:
        patterns_to_ignore = args.add_ignore_patterns.split(",")

    file_content = False
    if args.add_content_file_patterns:
        file_content = args.add_content_file_patterns.split(",")

    files_with_ignore_patterns = []
    if args.ignore_from_files:
        files_with_ignore_patterns.extend(args.ignore_from_files.split(","))

    if args.ignore_git_ignore:
        files_with_ignore_patterns.append(".gitignore")
        fwip_set = set(files_with_ignore_patterns)
        files_with_ignore_patterns = list(fwip_set)

    print(f"FILES: {files_with_ignore_patterns}")

    try:

        to_ignore = get_all_ignore_patterns(
            start_path,
            files_with_ignore_patterns,
            patterns_to_ignore)

        print(f"PATTERNS: {to_ignore}")

        structure = get_project_structure(
            start_path,
            output_format,
            to_ignore,
            file_content,
            args
        )

        if structure is not None:
            if args.print:
                print_strcuture = get_project_structure(
                    start_path,
                    "json",
                    to_ignore,
                    file_content
                )
                pretty_print(print_strcuture)

            if not args.not_save:
                save_structure_to_file(output_file, structure)
                print(f"Directory structure has been generated and saved to '{output_file}'.")
    except Exception as e:
        print(f"Error: {e}")
        raise e
        sys.exit(1)


if __name__ == "__main__":
    main()
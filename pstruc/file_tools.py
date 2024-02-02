import os


def get_all_ignore_patterns(
        start_path,
        files_with_ignore_patterns=[],
        extra_ignore_patterns=[]
):
    """
    Retrieves a combined list of ignore patterns from specified files and additional user-provided patterns.

    Args:
        start_path (str): The root directory path from where the search for ignore files begins.
        files_with_ignore_patterns (list of str): Filenames from which to read ignore patterns 
                                                  (e.g., '.gitignore').
        extra_ignore_patterns (list of str): Additional patterns provided by the user.

    Returns:
        list: A list of unique ignore patterns.
    """
    to_ignore = []

    for file in files_with_ignore_patterns:
        to_ignore.extend(_read_ignore_patterns_from_file(start_path, file))

    if extra_ignore_patterns:
        to_ignore.extend(extra_ignore_patterns)

    to_ignore = set(to_ignore)
    to_ignore = list(to_ignore)

    return to_ignore


def _read_ignore_patterns_from_file(start_path, file_with_ignore_patterns):
    """
    Reads and parses ignore patterns from a specified file.

    This method is used for extracting patterns from files like '.gitignore'.

    Args:
        start_path (str): The base directory path to look for the ignore file.
        file_with_ignore_patterns (str): The filename from which to read ignore patterns.

    Returns:
        list: A list of ignore patterns found in the specified file.
    """
    to_ignore = []

    # Check if file_with_ignore_patterns contains a path
    if os.path.dirname(file_with_ignore_patterns):
        result_path_file = file_with_ignore_patterns
    else:
        result_path_file = os.path.join(start_path, file_with_ignore_patterns)

    if os.path.exists(result_path_file):
        with open(result_path_file, "r") as path_file:
            lines = path_file.readlines()
            for line in lines:
                line = line.strip()
                if line and not line.startswith("#"):
                    to_ignore.append(line)
    return to_ignore

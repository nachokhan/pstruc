import os


def get_all_ignore_patterns(
        start_path=None,
        files_with_ignore_patterns=[],
        extra_ignore_patterns=[]
):
    to_ignore = []

    for file in files_with_ignore_patterns:
        to_ignore.extend(read_ignore_patterns_from_file(start_path, file))

    if extra_ignore_patterns:
        to_ignore.extend(extra_ignore_patterns)

    to_ignore = set(to_ignore)
    to_ignore = list(to_ignore)

    return to_ignore


def read_ignore_patterns_from_file(start_path, file_with_ignore_patterns):
    to_ignore = []

    # Read patterns from a file (e.g., .gitignore)
    result_path_file = os.path.join(start_path, file_with_ignore_patterns)
    print("A ver:" + result_path_file)
    if os.path.exists(result_path_file):
        with open(result_path_file, "r") as path_file:
            lines = path_file.readlines()
            for line in lines:
                line = line.strip()
                if line and not line.startswith("#"):
                    to_ignore.append(line)
    return to_ignore

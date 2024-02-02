
# Project Structure Generator

## Overview
Project Structure Generator is a versatile tool available both as a command-line interface and as a library. It enables users to generate directory structures in JSON, YAML, or plain text formats and offers the ability to pretty-print the structure with color.

## Features
- Generate directory structures in JSON, YAML, Dictionary or plain text.
- Exclude patterns specified in `.gitignore`.
- Pretty-print the directory structure with colorful output.
- Command-line interface for ease of use.
- Ability to include content of specified files.
- Customizable patterns for more precise control over the directory structure output.

## Installation
To install the package, use the following command:
```
pip install pstruc
```

## CLI Usage
The `pstruc` tool supports various arguments for generating and customizing the directory structure.

### Arguments
- `directory`: Specify the directory to inspect (_not specified: current directory_)
- `-f`, `--format`: Choose the output format (json, yaml, txt, dict).
- `-o`, `--output`: Specify the output file name.
- `-p`, `--print`: Print the directory structure without saving it.
- `-ns`, `--not-save`: Do not save the generated structure to an output file.
- `-ip`, `--add-ignore-patterns`: Add custom patterns to ignore.
- `-iff`, `--ignore-from-files`: List of files to get the ignore patterns from.
- `-igi`, `--ignore-git-ignore`: Ignore the patterns inside .gitignore file.
- `-fc`, `--add-content-file-patterns`: Include content of specified files.

### Example
```
python pstruc.py /path/to/directory -f json -o output_structure -ip "*.log","__pycache__" -fc "*.md","*.txt"
```
This command will generate a JSON file `output_structure.json` representing the directory structure of `/path/to/directory`, ignoring files matching `*.log` and `__pycache__`, and including content of markdown and text files.

## Library Usage
As a library, `pstruc` provides a straightforward API for generating and manipulating directory structures. The core functionality is based on generating the structure, saving it, and pretty-printing.

### Example
```python
from pstruc import get_project_structure, save_structure_to_file, pretty_print

# Generate directory structure
structure = get_project_structure('/path/to/directory', 'json', ignore_patterns=["*.log", "__pycache__"], file_content=["*.md", "*.txt"])

# Save to a file
save_structure_to_file('output_structure.json', structure)

# Pretty-print the structure
pretty_print(structure)
```

## Library Available Methods
- `get_project_structure(start_path, output_format, ignore_patterns, file_content)`: Generates the directory structure.
  - `start_path (str)`: The directory to inspect.
  - `output_format (str)`: The desired output format ('json', 'yaml', 'txt', 'dict').
  - `ignore_patterns (list)`: List of patterns to ignore.
  - `file_content (list)`: List of patterns to determine which file content to include in the structure.

- `save_structure_to_file(output_file, structure)`: Saves the directory structure to a file.
  - `output_file (str)`: The name of the output file.
  - `structure (str)`: The directory structure content to be saved.

- `pretty_print(structure)`: Pretty-prints the directory structure.
  - `structure (str or dict)`: The directory structure to print.
  - `indentation (str)`: The current indentation level.

- `get_all_ignore_patterns(start_path, files_with_ignore_patterns, extra_ignore_patterns)`: Retrieves a combined list of ignore patterns from specified files and additional user-provided patterns.
  - `start_path (str)`: The root directory path from where the search for ignore files begins.
  - `files_with_ignore_patterns (list of str)`: Filenames from which to read ignore patterns (e.g., '.gitignore').
  - `extra_ignore_patterns (list of str)`: Additional patterns provided by the user.



## Contributing
Contributions are welcome! Please follow our [Contributing Guidelines](CONTRIBUTING.md).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [colorama](https://pypi.org/project/colorama/) - For colorful output.

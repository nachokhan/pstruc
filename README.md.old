# 📒 Project Structure Generator

## Overview

A library and command-line tool for getting directory structures in different formats. This tool allows you to inspect a directory and create a structured representation of its contents in JSON, YAML, or plain text. You can also pretty-print the structure with colorful output.

## Features

✅ Generate directory structures in JSON, YAML, or plain text formats.

📝 Read patterns from a `.gitignore` file to exclude specific files or directories.

🎨 Pretty-print the directory structure with colorful output.

📦 Easily configurable and customizable.

## Installation
(still not installable 🛠) 
To install the package, you can use `pip`:

```
pip install pstruc
```

## CLI Usage

### Basic Usage

Generate a directory structure and save it to a YAML file:

```
python pstruc.py /path/to/directory -f yaml -o output_structure
```

Pretty-print the directory structure:

```
python pstruc.py /path/to/directory -p
```

### Advanced Usage

Use the `.gitignore` file to specify patterns to exclude:

```
# .gitignore
# Exclude virtual environment, cache, and log files
.env
__pycache__
*.log
```

Exclude patterns specified in `.gitignore` when generating the structure:

```
python pstruc.py /path/to/directory -f json
```

Include content of specified files (code, readmes, etc):

```
python pstruc.py /path/to/directory -f [format] -fc [content file patterns]
```

Do not save the generated structure to an output file:

```
python pstruc.py /path/to/directory -ns
```

Add custom patterns to ignore in addition to .gitignore:

```
python pstruc.py /path/to/directory -ip "pattern1,pattern2"
```

For more options and details, run:

```
python pstruc.py --help
```

## Example

Suppose you have the following directory structure:

```
my_project/
├── documents/
│   ├── report.txt
│   ├── proposal.docx
│   └── presentation.pptx
├── source_code/
│   ├── main.py
│   ├── utils/
│   │   ├── helper.py
│   │   └── constants.py
│   └── tests/
│       ├── test_main.py
│       └── test_utils.py
└── README.md
```

Running the following command:

```
python pstruc.py my_project -f json
```

Will generate a JSON representation of the directory structure.

```json
{
  "my_project": {
    "documents": {
      "report.txt": null,
      "proposal.docx": null,
      "presentation.pptx": null
    },
    "source_code": {
      "main.py": null,
      "utils": {
        "helper.py": null,
        "constants.py": null
      },
      "tests": {
        "test_main.py": null,
        "test_utils.py": null
      }
    },
    "README.md": null
  }
}
```

## 📚 Library Usage

In addition to being a command-line tool, `pstruc` can also be used as a library in your own Python projects. This allows you to integrate directory structure generation and manipulation directly into your scripts or applications.

### 🔧 Available Functions

The `pstruc` library offers the following key functions for use in your projects:

#### 🔍 `get_project_structure`
Generates a directory structure for a specified directory.

**Parameters:**
- `start_path (str)`: The directory to inspect.
- `output_format (str)`: The desired output format ('json', 'yaml', or 'txt').
- `ignore_patterns (list)`: List of additional patterns to ignore.
- `file_content (list)`: List of patterns to determine which file content to include in the structure.

**Returns:** 
- `str`: The directory structure in the specified format.

**Example:**

```python
from pstruc import get_project_structure

structure = get_project_structure('/path/to/directory', 'json')
print(structure)
```

#### 💾 `save_structure_to_file`
Saves the directory structure to a file.

**Parameters:**
- `output_file (str)`: The name of the output file.
- `structure (str)`: The directory structure content to be saved.

**Returns:**
- `None` or `str`: An error message if an error occurs; otherwise, `None`.

**Example:**

```python
from pstruc import save_structure_to_file

error = save_structure_to_file('output.json', structure)
if error:
    print(f"Error saving file: {error}")
```

#### 🎨 `pretty_print`
Pretty-prints a directory structure.

**Parameters:**
- `structure (str or dict)`: The directory structure to print.
- `indentation (str)`: The current indentation level.

**Example:**

```python
from pstruc import pretty_print

pretty_print(structure)
```

### ⚙️ Advanced Integration

You can integrate these functions into your Python applications to dynamically generate, save, and display directory structures. This is particularly useful for building tools that require a clear understanding of project layouts or for automating documentation tasks.


## Documentation

For detailed documentation and examples, please refer to the [Wiki](https://github.com/nachokhan/pstruc/wiki).

## Contributing

Contributions are welcome! If you want to contribute to this project, please follow the [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [colorama](https://pypi.org/project/colorama/) - For colorful output.

## Contact

👤 Ignacio Rigoni

- GitHub: [https://github.com/nachokhan](https://github.com/nachokhan)
- Email: ignacio.rigoni@gmail.com

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/nachokhan/pstruc/issues).

## Roadmap

See the [open issues](https://github.com/nachokhan/pstruc/issues) for a list of proposed features and known issues.

## Changelog

See the [CHANGELOG](CHANGELOG.md) for a list of changes in each version of the project.

## Credits

- Icons by [FontAwesome](https://fontawesome.com/)
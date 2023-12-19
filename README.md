# Project Name

📂 Directory Structure Generator

## Overview

A command-line tool for generating directory structures in different formats. This tool allows you to inspect a directory and create a structured representation of its contents in JSON, YAML, or plain text. You can also pretty-print the structure with colorful output.

## Features

✅ Generate directory structures in JSON, YAML, or plain text formats.

📝 Read patterns from a `.gitignore` file to exclude specific files or directories.

🎨 Pretty-print the directory structure with colorful output.

📦 Easily configurable and customizable.

## Installation
(still not installable 🫠) 
To install the Directory Structure Generator, you can use `pip`:

```
pip install directory-structure-generator
```

## Usage

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

For more options and details, run:

```
python pstruc.py --help
```

## Example

Suppose you have the following directory structure:

```
my_project/
├── documents/
│ ├── report.txt
│ ├── proposal.docx
│ └── presentation.pptx
├── source_code/
│ ├── main.py
│ ├── utils/
│ │ ├── helper.py
│ │ └── constants.py
│ └── tests/
│ ├── test_main.py
│ └── test_utils.py
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


## Documentation

For detailed documentation and examples, please refer to the [Wiki](https://github.com/nachokhan/project-structure/wiki).

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

If you encounter any issues or have questions, please [open an issue](https://github.com/nachokhan/project-structure/issues).

## Roadmap

See the [open issues](https://github.com/nachokhan/project-structure/issues) for a list of proposed features and known issues.

## Changelog

See the [CHANGELOG](CHANGELOG.md) for a list of changes in each version of the project.

## Credits

- Icons by [FontAwesome](https://fontawesome.com/)

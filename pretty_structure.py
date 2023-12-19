import json
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)


def pretty_print(structure, indentation=""):
    """
    Pretty-print a directory structure.

    Args:
        structure (str or dict): The directory structure to print.
        indentation (str): The current indentation level.
    """

    if isinstance(structure, str):
        structure = _parse_structure(structure)

    if isinstance(structure, dict):
        for key, value in structure.items():
            if value is None:
                print(indentation + f"- {Fore.GREEN}{key}{Style.RESET_ALL}")
            else:
                print(indentation + f"- {Fore.BLUE}{key}{Style.RESET_ALL}:")
                pretty_print(value, indentation + "  ")


def _parse_structure(structure_str):
    """
    Parse a directory structure from a JSON-formatted string.

    Args:
        structure_str (str): The JSON-formatted structure string.

    Returns:
        dict: The parsed directory structure.
    """
    try:
        return json.loads(structure_str)
    except json.JSONDecodeError:
        return None

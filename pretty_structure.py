import json
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)


def _parse_structure(structure_str):
    try:
        return json.loads(structure_str)
    except json.JSONDecodeError:
        return None


def pretty_print(structure, indentation=""):

    if isinstance(structure, str):
        structure = _parse_structure(structure)

    if isinstance(structure, dict):
        for key, value in structure.items():
            if value is None:
                print(indentation + f"- {Fore.GREEN}{key}{Style.RESET_ALL}")
            else:
                print(indentation + f"- {Fore.BLUE}{key}{Style.RESET_ALL}:")
                pretty_print(value, indentation + "  ")

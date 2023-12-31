import subprocess
import os

def is_text_file(file_name):
    """
    Check if a file is a text file based on its MIME type.

    Args:
        file_name (str): The path to the file to be checked.

    Returns:
        bool: True if the file is a text file, False if it's binary.
    """
    try:
        with open(file_name, 'rb') as file:
            # Read the first 1024 bytes from the file and check for binary characters
            data = file.read(1024)
            if b'\x00' in data:
                return False
            return True
    except Exception as e:
        return False


def read_file(file_name):
    """
    Read and return the content of a text file or indicate that it's a binary file.

    Args:
        file_name (str): The path to the file to be read.

    Returns:
        str: The file's content if it's a text file, or "(binary file)" if it's binary.
    """
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"The file '{file_name}' does not exist.")

    if is_text_file(file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        except Exception as e:
            return str(e)
    else:
        return "(binary file)"

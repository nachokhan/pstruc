import os
import pytest
from pstrucsrc._directory_structure import generate_directory_structure


def test_generate_directory_structure_valid_directory():
    # Test with a valid directory
    start_path = os.path.abspath(os.path.dirname(__file__))  # Use the current directory for testing
    structure = generate_directory_structure(start_path)
    assert structure is not None
    assert "Error" not in structure  # No error should occur
    assert isinstance(structure, str)  # The result should be a string


def test_generate_directory_structure_invalid_directory():
    # Test with an invalid directory
    invalid_path = "/invalid_directory_path"
    structure = generate_directory_structure(invalid_path)
    assert structure is not None
    assert "Error" in structure  # An error should occur
    assert isinstance(structure, str)  # The result should be a string


def test_generate_directory_structure_yaml_format():
    # Test generating directory structure in YAML format
    start_path = os.path.abspath(os.path.dirname(__file__))  # Use the current directory for testing
    structure = generate_directory_structure(start_path, output_format="yaml")
    assert structure is not None
    assert "Error" not in structure  # No error should occur
    assert isinstance(structure, str)  # The result should be a string


def test_generate_directory_structure_txt_format():
    # Test generating directory structure in TXT format
    start_path = os.path.abspath(os.path.dirname(__file__))  # Use the current directory for testing
    structure = generate_directory_structure(start_path, output_format="txt")
    assert structure is not None
    assert "Error" not in structure  # No error should occur
    assert isinstance(structure, str)  # The result should be a string


def test_generate_directory_structure_json_format():
    # Test generating directory structure in JSON format
    start_path = os.path.abspath(os.path.dirname(__file__))  # Use the current directory for testing
    structure = generate_directory_structure(start_path, output_format="json")
    assert structure is not None
    assert "Error" not in structure  # No error should occur
    assert isinstance(structure, str)  # The result should be a string
    assert structure.startswith("{")
    assert structure.endswith("}")


if __name__ == "__main__":
    pytest.main()

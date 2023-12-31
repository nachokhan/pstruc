import tempfile
import pytest
from pstruc._file_structure import is_text_file, read_file


@pytest.fixture
def text_file():
    # Create a temporary text file for testing
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as file:
        file.write("This is a text file.")
        return file.name


@pytest.fixture
def binary_file():
    # Create a temporary binary file for testing
    with tempfile.NamedTemporaryFile(mode='wb', delete=False) as file:
        file.write(b'\x00\x01\x02\x03')
        return file.name


def test_is_text_file_with_text_file(text_file):
    assert is_text_file(text_file) is True


def test_is_text_file_with_binary_file(binary_file):
    assert is_text_file(binary_file) is False


def test_read_text_file_content(text_file):
    content = read_file(text_file)
    assert content == "This is a text file."


def test_read_binary_file_content(binary_file):
    content = read_file(binary_file)
    assert content == "(binary file)"


def test_read_nonexistent_file():
    with pytest.raises(Exception):
        read_file("nonexistent_file.txt")

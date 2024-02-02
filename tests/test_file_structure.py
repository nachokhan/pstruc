import pytest
import os
from pstruc._file_structure import is_text_file, read_file


def test_is_text_file_with_text_file(tmp_path):
    file_path = tmp_path / "file.txt"
    file_path.write_text("This is a text file.")
    assert is_text_file(str(file_path)) is True


def test_is_text_file_with_binary_file(tmp_path):
    file_path = tmp_path / "file.bin"
    file_path.write_bytes(b'\x00\x01\x02')
    assert is_text_file(str(file_path)) is False


def test_read_text_file_content(tmp_path):
    file_path = tmp_path / "file.txt"
    file_path.write_text("This is a text file.")
    assert read_file(str(file_path)) == "This is a text file."

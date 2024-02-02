import pytest
from unittest.mock import patch, MagicMock
import sys
from pstruc import pstruc

# Adjusting the paths to mock functions according to their actual locations

@pytest.fixture
def mock_generate_directory_structure():
    with patch("pstruc._directory_structure.generate_directory_structure") as mock:
        yield mock

@pytest.fixture
def mock_save_structure_to_file():
    with patch("pstruc._directory_structure.save_structure_to_file") as mock:
        yield mock

@pytest.fixture
def mock_pretty_print():
    with patch("pstruc._pretty_structure.pretty_print") as mock:
        yield mock

@pytest.fixture
def mock_get_all_ignore_patterns():
    with patch("pstruc.file_tools.get_all_ignore_patterns") as mock:
        yield mock

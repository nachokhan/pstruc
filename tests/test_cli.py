import os
import pytest
import subprocess


def test_cli_with_valid_directory(tmpdir):
    # Test CLI with a valid directory
    test_directory = os.path.join(tmpdir, "test_dir")
    os.mkdir(test_directory)

    result = subprocess.run(["python3", "pstruc.py", test_directory], stdout=subprocess.PIPE, text=True)
    assert result.returncode == 0  # Exit code should be 0 for success


def test_cli_with_invalid_directory():
    # Test CLI with an invalid directory
    invalid_path = "/invalid_directory_path"
    result = subprocess.run(["python3", "pstruc.py", invalid_path], stderr=subprocess.PIPE, text=True)
    assert result.returncode != 0  # Exit code should not be 0 for error


def test_cli_with_yaml_format(tmpdir):
    # Test CLI with YAML format
    test_directory = os.path.join(tmpdir, "test_dir")
    os.mkdir(test_directory)

    result = subprocess.run(["python3", "pstruc.py", test_directory, "-f", "yaml"], stdout=subprocess.PIPE, text=True)
    assert result.returncode == 0  # Exit code should be 0 for success
    assert "Directory structure has been generated" in result.stdout


if __name__ == "__main__":
    pytest.main()

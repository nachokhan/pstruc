from setuptools import setup
from pstruc.version import __version__

# Leer la descripción larga desde README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    version=__version__,
    long_description=long_description,
)

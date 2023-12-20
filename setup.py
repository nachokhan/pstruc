from setuptools import setup

# Leer la descripción larga desde README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    long_description=long_description,
)

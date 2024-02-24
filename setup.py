from setuptools import setup, find_packages
# from pstruc.version import __version__

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='pstruc',
    version="1.0.1",
    author='Ignacio Rigoni',
    description='Get a project file structure to analyze it',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nachokhan/pstruc',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    packages=find_packages(),
    install_requires=[
        'colorama==0.4.6',
        'iniconfig==2.0.0',
        'packaging==23.2',
        'pluggy==1.3.0',
        'pytest==7.4.3',
        'PyYAML==6.0.1',
        'setuptools>=40.8.0',
    ],
    python_requires='>=3.11.0',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pstruc = pstruc.pstruc:main'
        ]
    },
    extras_require={
        'dev': ['pytest']
    }
)

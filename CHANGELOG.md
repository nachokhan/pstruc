
# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

- Planned features or upcoming changes will be listed here.

## [1.0.0] - 2024-02-17
### Added
- Metadata field at the same level as the project structure, including information on ignored patterns, prompt options used, and the `pstruc` version.
### Changed
- Restructured to include two main fields: `metadata` and `structure`, enhancing the clarity and utility of the project structure output.

## [0.5.0] - 2024-02-02
### Added
- New output format `"dict"`, offering a Python dictionary representation of the structure for improved integration with Python-based projects.
### Changed
- Updated docstrings for clarity.
- The `"to_ignore_files"` option now defaults to the project's path if no path is specified.

## [0.4.0] - 2024-01-22
### Added
- New CLI arguments `"ignore-git-ignore"` and `"ignore-from-files"`.
### Changed
- Modified internal code to enhance file access responsibilities.
- Improved `README.md` documentation for better user guidance.

## [0.3.1] - 2024-01-17
### Fixed
- A minor bug in the main method.

## [0.3.0] - 2024-01-17
### Added
- Command-line interface functionality for `pstruc`, allowing direct execution in the terminal.

## [0.2.1] - 2024-01-01
### Fixed
- File saving error handling.
- Issue with how add-file-content patterns were processed in the CLI.

## [0.2.0] - 2023-12-31
### Changed
- Added options to include additional ignore-patterns and file-patterns for enhanced customization.

## [0.1.6] - 2023-12-21
### Changed
- Enabled release on push to production.
### Fixed
- Main methods now directly importable from the package.

## [0.1.5] - 2023-12-20
### Changed
- Updated release notes.

## [0.1.4] - 2023-12-20
### Changed
- Updated information in `Readme`.

## [0.1.3] - 2023-12-20
### Changed
- Relocated the main file for better project structure.

## [0.1.2] - 2023-12-19
### Added
- Initial release of the project.
- `pretty_print` method for more colorful and informative output.





### SCHEMA

### Changed
- List any changes to existing features here.

### Fixed
- List any bug fixes here.

### Deprecated
- List any features that are now deprecated.

### Removed
- List any features or functionalities that have been removed.

### Security
- List any security improvements here.

(Replace YYYY-MM-DD with the actual date of the release)

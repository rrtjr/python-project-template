"""
This module provides functions to change placeholders into actual project information.
"""

import os
import re
from typing import List


def replace_in_file(file_path: str, old_string: str, new_string: str) -> None:
    """
    Replaces occurrences of a string in a file with a new string.

    Args:
        file_path (str): The path to the file.
        old_string (str): The string to be replaced.
        new_string (str): The string to replace with.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content: str = file.read()
    content = re.sub(old_string, new_string, content)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def to_snake_case(string: str) -> str:
    """
    Converts a given string to snake_case.

    Args:
        string (str): The input string to be converted.

    Returns:
        str: The snake_case version of the input string.
    """
    string = re.sub(r"[\s-]+", "_", string)
    string = re.sub(r"([a-z])([A-Z])", r"\1_\2", string)
    string = string.lower()
    return string


def rename_project_directory(old_name: str, new_name: str) -> None:
    """
    Renames a project directory from an old name to a new name.

    Args:
        old_name (str): The current name of the project directory.
        new_name (str): The new name for the project directory.
    """
    os.rename(f"src/{old_name.replace('-', '_')}", f"src/{new_name}")


def update_python_version(file_path: str, old_version: str, new_version: str) -> None:
    """
    Updates the Python version in the specified file.

    Args:
        file_path (str): The path to the file.
        old_version (str): The old Python version string to be replaced.
        new_version (str): The new Python version string to replace with.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content: str = file.read()
    content = re.sub(rf"{re.escape(old_version)}", new_version, content)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def update_pre_commit_python_version(file_path: str, old_version: str, new_version: str) -> None:
    """
    Updates the Python version in the pre-commit-config.yaml file.

    Args:
        file_path (str): The path to the file.
        old_version (str): The old Python version string to be replaced.
        new_version (str): The new Python version string to replace with.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content: str = file.read()
    content = re.sub(rf"python: {re.escape(old_version)}", f"python: {new_version}", content)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def update_project_version(file_path: str, new_version: str) -> None:
    """
    Updates the project version in the specified file.

    Args:
        file_path (str): The path to the file.
        new_version (str): The new project version string to replace with.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content: str = file.read()
    content = re.sub(r'version\s*=\s*".*"', f'version = "{new_version}"', content)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def get_current_project_name(file_path: str) -> str:
    """
    Retrieves the current project name from the specified file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The current project name.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content: str = file.read()
    match = re.search(r'name\s*=\s*"(.*?)"', content)
    return match.group(1) if match else ""


def get_current_python_version(file_path: str) -> str:
    """
    Retrieves the current Python version from the specified file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The current Python version.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content: str = file.read()
    match = re.search(r"python\s*=\s*\"(.*?)\"", content)
    return match.group(1) if match else ""


def main() -> None:
    """
    Main function to update the project name in files and rename the project directory.
    """
    pyproject_file = "pyproject.toml"
    old_name: str = get_current_project_name(pyproject_file)
    print(f"Old project name {old_name} found.")

    new_name: str = input("Enter the new project name: ")
    new_name = to_snake_case(new_name)

    files_to_update: List[str] = [
        "pyproject.toml",
    ]

    for file_path in files_to_update:
        replace_in_file(file_path, old_name, new_name)

    rename_project_directory(old_name, new_name)

    old_python_version: str = get_current_python_version(pyproject_file)
    new_python_version: str = input("Enter the exact target Python version: ")

    python_version_files: List[str] = [
        "pyproject.toml",
        ".github/workflows/ci.yml",
        ".python-version",
        ".pre-commit-config.yaml",
    ]

    for file_path in python_version_files:
        if file_path == ".pre-commit-config.yaml":
            update_pre_commit_python_version(file_path, old_python_version, new_python_version)
        else:
            update_python_version(file_path, old_python_version, new_python_version)

    new_project_version = "0.0.1"
    version_files: List[str] = [
        "pyproject.toml",
        ".bumpversion.cfg",
    ]

    for file_path in version_files:
        update_project_version(file_path, new_project_version)

    print(f"Project name has been updated to {new_name}")
    print(f"Python version has been updated to {new_python_version}")
    print(f"Project version has been updated to {new_project_version}")


if __name__ == "__main__":
    main()

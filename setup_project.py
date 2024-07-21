"""
This module provides functions to change placeholders into actual project information.
"""

import os
import re


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


def main() -> None:
    """
    Main function to update the project name in files and rename the project directory.
    """
    old_name = "python-project-template-by-rtj"
    new_name: str = input("Enter the new project name: ")
    new_name = to_snake_case(new_name)

    files_to_update = [
        "pyproject.toml",
    ]

    for file_path in files_to_update:
        replace_in_file(file_path, old_name, new_name)

    rename_project_directory(old_name, new_name)

    print(f"Project name has been updated to {new_name}")


if __name__ == "__main__":
    main()

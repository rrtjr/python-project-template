# Just Another Python Project Template

[![CI Pipeline](https://github.com/rrtjr/python-project-template/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/rrtjr/python-project-template/actions/workflows/ci.yml)

## Description

Welcome to my Python Starter Kit! As someone who often finds myself recreating project setups from scratch, I created this template to streamline the process and ensure consistency across my projects. This template provides a solid foundation for rapid development, saving time and effort in the initial setup phase. This template will be handy for me and anyone looking to kickstart their Python projects efficiently.

## Features

1. **Setup Script**: Includes a `setup_project.py` script to simplify the initial setup process for new projects, allowing you to easily rename the project and configure initial settings.

2. **Dependency Management**: Utilizes `pyproject.toml` and Poetry for efficient dependency management and project configuration, ensuring a modern and streamlined development workflow.

3. **GitHub Workflows**: Integrated GitHub Actions workflows for seamless CI/CD, release automation, and package updates:
    - **CI Workflow**: Automatically runs tests and checks code coverage with each commit to maintain code quality and reliability.
    - **Release Workflow**: Automates version bumping and publishing releases to streamline the release process.
    - **Package Update Workflow**: Automatically checks and updates Python package dependencies on a regular schedule to keep your project up-to-date.

4. **Code Coverage**: Incorporates `pytest-cov` to measure and report code coverage, integrated with the CI workflow to ensure comprehensive test coverage.

5. **Pre-commit Hooks**: Configured pre-commit hooks to maintain code quality and prevent common issues before they are pushed to remote.

6. **VSCode Configuration**: Provides `.vscode/settings.json` for a consistent development environment setup in Visual Studio Code, enhancing the developer experience.

7. **Documentation**: Includes a `README.md` template to guide the documentation of the project, ensuring clear and comprehensive project information from the start.

8. **Tests Directory**: Set up a `tests` directory with sample unit tests using `unittest` or `pytest`, facilitating test-driven development and ensuring code reliability.

9. **Python Version**: Specifies the Python version used by the project in a `.python-version` file, ensuring consistency across different development environments.

Certainly! Here’s a detailed section on how to use the project template:

## How to Use This Project Template

### 1. Clone the Template Repository

First, clone the project template repository to your local machine:

```sh
git clone https://github.com/rrtjr/python-project-template new_project
cd new_project
```

### 2. Run the Setup Script

Run the setup script to configure your project with a new name and initial settings:

```sh
python setup_project.py
```

The script will prompt you to enter the new project name and will update all relevant files and directories accordingly.

### 3. Initialize a New Git Repository

After the setup script runs, remove the old `.git` directory and initialize a new Git repository:

```sh
rm -rf .git
git init
git checkout -b main
git add .
git commit -m "Initial commit with updated project name"
git remote add origin https://github.com/your-username/new_project_name.git
git config branch.main.remote origin
git config branch.main.merge refs/heads/main
git config branch.main.vscode-merge-base origin/main
git pull origin main --allow-unrelated-histories # Then follow instructions to resolve conflicts
git push -u origin main
```

This assumes you have an empty git repository. Should you have an existing and wanting to merge you can combine histories by:

```sh
git merge origin/main --allow-unrelated-histories
```

You can then proceed ub resolving the conflicts (e.g. pyproject.toml, workflows, .pre-commit-config)

### 4. Install Dependencies

Use Poetry to install the project dependencies defined in `pyproject.toml`:

```sh
poetry env use $(pyenv which python)
poetry install
```

### 5. Setup Pre-commit Hooks

Install pre-commit hooks to maintain code quality and prevent common issues:

```sh
pre-commit install
```

### 6. Running Tests (TODO)

Run the tests using `pytest` to ensure everything is working correctly:

```sh
poetry run pytest
```

### 7. Using the CI/CD Workflows

The template comes with pre-configured GitHub Actions workflows for CI/CD, release automation, and package updates. These workflows are automatically triggered based on your GitHub repository's activity:

- **CI Workflow**: Runs tests and checks code coverage with each commit.
- **Release Workflow**: Automates version bumping and publishing releases.
- **Package Update Workflow**: Checks and updates Python package dependencies on a regular schedule.

Ensure your repository on GitHub is set up with the necessary permissions and tokens for these workflows to function correctly.

### 8. VSCode Configuration

The template includes a `.vscode/settings.json` file for a consistent development environment setup in Visual Studio Code. Open the project in VSCode to take advantage of the predefined settings.

#### 9. Documentation

Update the `README.md` file to include relevant information about your new project. Use the provided template as a guide to ensure clear and comprehensive documentation.

#### 10. Python Version

The `.python-version` file specifies the Python version used by the project. Ensure your development environment uses the same Python version to maintain consistency.


## Contribution Guidelines

I welcome contributions to improve this project template! To ensure a smooth and effective collaboration, please follow these guidelines:

### 1. Fork the Repository

First, fork the repository to your GitHub account:

1. Navigate to the [repository on GitHub](https://github.com/rrtjr/python-project-template).
2. Click the "Fork" button in the upper-right corner.

### 2. Clone Your Fork

Clone your forked repository to your local machine:

```sh
git clone https://github.com/your-username/python-project-template.git
cd project_name
```

### 3. Create a Branch

Create a new branch for your feature or bugfix:

```sh
git checkout -b feature-or-bugfix-description
```

### 4. Make Your Changes

Make your changes to the codebase. Ensure that your changes adhere to the coding standards and that you update or add tests as needed.

#### 5. Install Dependencies

If you haven't already, install the project dependencies using Poetry:

```sh
poetry install
```

### 6. Run Tests

Before committing your changes, run the tests to ensure everything is working correctly:

```sh
poetry run pytest
```

### 7. Commit Your Changes

Commit your changes with a clear and concise commit message:

```sh
git add .
git commit -m "Brief description of your changes"
```

### 8. Push to Your Fork

Push your branch to your forked repository on GitHub:

```sh
git push origin feature-or-bugfix-description
```

### 9. Open a Pull Request

Open a pull request to the original repository:

1. Navigate to the original [repository on GitHub](https://github.com/rrtjr/python-project-template).
2. Click the "Pull requests" tab.
3. Click the "New pull request" button.
4. Select the branch you pushed to and the branch you want to merge into (usually `main`).
5. Provide a clear and detailed description of your changes and click "Create pull request".

#### 10. Review Process

Your pull request will be reviewed by the project maintainers. They may request changes or provide feedback. Please be responsive and address any comments or requests.

## Code of Conduct

Please adhere to the [Code of Conduct](CODE_OF_CONDUCT.md) in all your interactions with the project.

## Summary

Thanks for considering to contribute to this small project. By following these guidelines, we can maintain the quality better for everyone. If you have any questions, feel free to open an issue. Happy coding!

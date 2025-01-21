# Data Engineering Challenge

## Description
This project is a coding challenge to test basic data engineering skills using Python and SQLite.

## Requirements
- Python 3
- SQLite
- Poetry

## Project Structure
de_challenge/
├── de/
│ ├── init.py
│ ├── main.py
| ├── queries.yaml
| └── utils.py
├── tests/
│ ├── init.py
│ └── test_main.py
├── .gitignore
├── pyproject.toml
└── README.md

## Installation

### Prerequisites

- Python 3.11
- Poetry for dependency management

## Setup
1. Clone the repository.
2. Install the dependencies using Poetry:
    poetry install
3. Running the Project
    poetry run python de/main.py
4. Running Tests
    poetry run pytest

## Project Files

1. main.py
- Contains the main functionality for generating ratings, computing monthly aggregates, and finding top products.
2. queries.yaml
- This file contains the SQL queries used in the project.
3. utils.py
- Contains utility for main file.
4. test_main.py
- Contains tests for the main functionality using pytest.
5. pyproject.toml
- Defines the project dependencies and configuration for Poetry.


## GitHub Actions 
1. Used it to create a simple workflow, defined as follows.
2. Configured action_test.yml through github interface of github actions.
3. It allows to check build pass/fail on merge/push of code to main branch from feature branch.
4. Workflow consists of a single job called "build" that executes on an ubuntu-latest runner. The job includes steps to check out the repository, set up Python 3.11, install project dependencies using Poetry, and run tests using pytest.
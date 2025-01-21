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

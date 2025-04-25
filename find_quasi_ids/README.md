# Find Quasi-Identifiers

Python CLI tool designed to identify quasi-identifiers in tabular datasets.

Quasi-identifiers are combinations of data attributes that, while not uniquely identifying on their own, can be used in conjunction with other data to re-identify individuals. This tool is useful for privacy-preserving data analysis, anonymization, and compliance with data protection regulations.

## Features

- Automatically detects potential quasi-identifiers in CSV
- Supports customizable thresholds and parameters
- Simple command-line interface
- Easily extensible and configurable

## Installation

1. Clone the repository.
2. In your virtual environment of choice run
    ```bash
    uv add <path/to/cloned/repo>/find_quasi_ids
    ```
    or if you're still using pip
    ```bash
    pip install <path/to/cloned/repo>/find_quasi_ids
    ```

## Usage

You can either:

- activate your venv where you installed `find-quasi-ids` and run it as
    ```bash
    find-quasi-ids 
    ```
- run it with uv and let uv handle the venv as
    ```bash
    uv run find-quasi-ids
    ```


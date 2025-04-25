# Find Quasi-Identifiers

A Python CLI tool to identify quasi-identifiers in tabular datasets (CSV files).

Quasi-identifiers are combinations of data attributes that, while not uniquely identifying on their own, can be used together to re-identify individuals. This tool helps analyze data for quasi-identifiers that could potentially lead to privacy risks or data leaks.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Algorithm Options](#algorithm-options)
  - [Examples](#examples)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Automatic detection** of potential quasi-identifiers in CSV files
- **Supports multiple algorithms**: brute-force and greedy
- **Customizable thresholds and parameters**
- **Simple command-line interface**
- **Easily extensible and configurable**

## Installation

> [!NOTE]
> `find-quasi-ids` is not available on PyPI or any other Python package index. You must clone the repository and install it locally in a Python virtual environment.

1. **Clone the repository containing the tool:**

2. **Create and activate a Python virtual environment (Python 3.8+ recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3. **Install the tool and its dependencies into your virtual environment:**

    - **Standard install:**
        ```bash
        pip install /path/to/cloned/tool/repo/find_quasi_ids/
        ```
        Or, if you use [uv](https://github.com/astral-sh/uv):
        ```bash
        uv pip install /path/to/cloned/tool/repo/find_quasi_ids/
        ```

    - **Editable (development) install:**  
      If you want to extend or modify the tool and have changes reflected without reinstalling, install in editable mode:
        ```bash
        pip install -e /path/to/cloned/tool/repo/find_quasi_ids/
        ```
        Or with uv:
        ```bash
        uv add -e /path/to/cloned/tool/repo/find_quasi_ids/
        ```

4. **Verify the installation:**
    ```bash
    find-quasi-ids --help
    ```

> [!TIP]
> Installing in editable mode (`-e`) is recommended if you plan to modify or extend the codebase.

## Usage

### Basic Usage

```
find-quasi-ids -f  {brute,greedy} [algorithm options]
```

**Options:**
- `-f, --input-file `: Path to input CSV datafile (**required**)
- `--out-dir `: Directory to write output CSV file(s) (default: `output/` in current directory)
- `-h, --help`: Show help message and exit

### Algorithm Options

You must specify one of the following algorithms:

- `brute`: Run the brute-force algorithm
- `greedy`: Run the greedy algorithm

Each algorithm may have its own additional options (see help for details).

### Examples

**Show help:**
```
find-quasi-ids -h
```

**Run brute-force on a dataset:**
```
find-quasi-ids -f data.csv brute
```

**Run greedy algorithm and specify output directory:**
```
find-quasi-ids -f data.csv --out-dir results/ greedy
```

**Using uv to run (if installed with uv):**
```
uv run find-quasi-ids -f data.csv brute
```

## Output

- The tool will write one or more CSV files to the specified output directory (or the default directory).
- Each output file contains the detected quasi-identifiers with a distinct ratio score.


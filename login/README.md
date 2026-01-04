# Python Desktop App

A minimal README template for a Python desktop application.

## Overview

Short description: what the app does and its primary purpose.

## Features

- Feature 1
- Feature 2

## Requirements

- Python 3.10+
- Optional: `pip`, `virtualenv` or `venv`

## Installation

1. Clone the repo:

```bash
git clone <repo-url> && cd python_desktop
```

2. Create and activate a virtual environment:

On Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On Windows (cmd):

```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
```

On macOS / Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

If this project uses `pyproject.toml` / Poetry:

```bash
poetry install
```

## Running

Run the application (replace `main.py` with your entrypoint):

```bash
python main.py
```

## Packaging (optional)

A quick example using `PyInstaller` to create a single-file executable:

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

The executable will be in `dist/`.

### Windows helper scripts

Two helper scripts are provided to build a Windows executable from the project root:

- `build_exe.bat` — run from Explorer or CMD (will try to use `.venv` python if present).
- `build_exe.ps1` — PowerShell script (run from PowerShell, may need `Unblock-File`).

Usage (from project root):

```powershell
.\build_exe.ps1
```

or

```cmd
build_exe.bat
```

Notes:
- The scripts call `pyinstaller --onefile --windowed` and use `main.py` as the entrypoint by default.
- To build the app using `first-desktop.py` instead, edit the scripts and replace `main.py` with `first-desktop.py`.

## Continuous integration (optional)

A GitHub Actions workflow is included to produce a Windows build using PyInstaller and upload the built `.exe` as an artifact.

- Workflow file: [.github/workflows/windows-pyinstaller-build.yml](.github/workflows/windows-pyinstaller-build.yml)

The workflow runs on `windows-latest`, installs dependencies (from `requirements.txt` if present), runs the project's `build_exe.ps1` if available, and uploads `dist/*.exe` as an artifact.

If you want the CI to include a custom icon, add your `.ico` at `assets/app.ico` in the repository.

## Development

- Testing: describe test runner, e.g., `pytest`
- Linting: e.g., `flake8` or `ruff`
- Formatting: e.g., `black`

Example commands:

```bash
pip install -r dev-requirements.txt
pytest
ruff check .
black .
```

## Contributing

- Fork the repo and create a feature branch.
- Open a PR with a clear description and tests.

## License

Add your chosen license here (e.g., MIT).

## Contact

Maintainer: Your Name — replace with real contact details.

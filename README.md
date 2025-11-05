# langchain-learning

This project demonstrates a simple setup for experimenting with LangChain and related libraries.

## Requirements
- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) (fast Python package manager)

## Installation

1. (Recommended) Create and activate a virtual environment:
	```sh
	python3 -m venv .venv
	source .venv/bin/activate
	```

2. Install dependencies using [uv](https://github.com/astral-sh/uv):
	```sh
	uv pip install -r requirements.txt
	# or, to install from pyproject.toml:
	uv pip install .
	```

If you don't have `uv` installed, you can install it with:
```sh
pip install uv
```

## Running


To run the example script with uv:

```sh
uv pip run python hello.py
```

Or, if you prefer the standard way:

```sh
python hello.py
```

You should see:

```
Hello from langchain-learning!
```

## Notes
- Edit `hello.py` or add new scripts to experiment with LangChain.
- Update `pyproject.toml` to manage dependencies.

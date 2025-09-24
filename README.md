# fastapis

A boilerplate project for building application programming interfaces

## Install

This project uses `uv` for dependency management.

1.  Create a virtual environment:

    ```bash
    uv venv
    ```

2.  Activate the virtual environment:

    ```bash
    source .venv/bin/activate
    ```

3.  Install the project in editable mode with development dependencies:

    ```bash
    uv pip install -e .[dev]
    ```

## Run

After installation, you can run the server with the following command:

```bash
run-server
```

This will start the FastAPI application on `http://0.0.0.0:8000`.

## Build

This project uses [Hatch](https://hatch.pypa.io/latest/) for project management.

If you don't have `hatch` installed, you can install it with `uv`:

```bash
uv tool install hatch
```

To build the source distribution (`sdist`) and wheel, run the following command:

```bash
hatch build
```

The distributions will be created in the `dist/` directory.

## Pre-commit

This project uses [pre-commit](https://pre-commit.com/) to enforce code style and quality.

Install the pre-commit hooks with:

```bash
pre-commit install && pre-commit install -t pre-push
```

The hooks will run automatically on every commit. You can also run them manually:

```bash
pre-commit run --all-files
```

To skip checks:

```bash
git commit --no-verify
```

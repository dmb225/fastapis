# Default task - run the server
default:
    just run

# Create a virtual environment
venv-create:
    uv venv

# Activate the virtual environment
venv-activate:
    source .venv/bin/activate

# Install the project in editable mode with development dependencies
install:
    uv pip install -e .[dev]

# Run the server
run:
    run-server

# Build the source distribution (`sdist`) and wheel
build:
    hatch build

# Install the pre-commit hooks
pre-commit-install:
    pre-commit install && pre-commit install -t pre-push

# Run linters
lint:
    pre-commit run --all-files

# To commit while skipping checks:
commit-no-verify:
    git commit --no-verify

# Run tests
test:
    pytest -v tests/

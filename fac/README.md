# FAC CLI Tool

A command-line tool for business-specific actions.

## Installation

For development:

```bash
# Clone the repository
cd fac
pip install -e .
```

## Usage

After installation, the tool can be run by typing:

```bash
fac
```

Currently, this prints "hello" as a proof of concept.

## Development

This project uses standard Python development practices.

### Testing

To run the tests, first install the development dependencies:

```bash
# Activate the virtual environment
source venv/bin/activate

# Install development dependencies
pip install -r requirements-dev.txt
```

Then run the tests using pytest:

```bash
pytest
```

For test coverage information:

```bash
pytest --cov=fac
```
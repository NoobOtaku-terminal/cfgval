# cfgval - Config Validator

A powerful CLI tool to validate YAML, JSON, and TOML configuration files against JSON schemas.

## Features

- ✅ Validates YAML, JSON, and TOML files
- 📋 JSON Schema support (Draft 7)
- 🎨 Beautiful, human-readable output with Rich
- 📊 JSON output mode for CI/CD integration
- 🐳 Docker support for containerized validation
- 🔍 Auto-discovery of schemas in the same directory
- 📁 Recursive directory validation

## Installation

### From source

```bash
pip install -r requirements.txt
python -m cfgval.cli validate <path> --schema <schema.json>
```

### As a package

```bash
pip install -e .
cfgval validate <path> --schema <schema.json>
```

### With Docker

```bash
docker build -t cfgval:latest .
docker run --rm -v "$(pwd)/examples:/data" cfgval:latest validate /data --schema /app/cfgval/schemas/example_schema.json
```

## Usage

### Basic validation

```bash
# Validate a single file
python -m cfgval.cli validate examples/example_config.yaml --schema cfgval/schemas/example_schema.json

# Validate a directory (all YAML, JSON, TOML files)
python -m cfgval.cli validate examples --schema cfgval/schemas/example_schema.json

# JSON output for CI/CD
python -m cfgval.cli validate examples --schema cfgval/schemas/example_schema.json --json
```

### Auto-discovery mode

If you place a `schema.json` file in the same directory as your config files, cfgval will automatically use it:

```bash
python -m cfgval.cli validate examples/
```

## Testing

Run the test suite:

```bash
pytest -q
```

## CI/CD Integration

A GitHub Actions workflow is included in `.github/workflows/ci.yml` that:

- Runs tests on every push and pull request
- Validates example configs
- Uses Python 3.11

## Project Structure

```
cfgval/
├── cfgval/
│   ├── __init__.py
│   ├── cli.py           # CLI interface with Typer
│   ├── loader.py        # Multi-format file loader
│   ├── validator.py     # JSON Schema validation
│   ├── reporters.py     # Human & JSON output
│   ├── schemas/
│   │   └── example_schema.json
│   └── tests/
│       ├── test_loader.py
│       └── test_validator.py
├── examples/
│   ├── example_config.yaml
│   └── example_config_bad.yaml
├── Dockerfile
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Dependencies

- `typer[all]` - CLI framework
- `jsonschema` - JSON Schema validation
- `pyyaml` - YAML parsing
- `tomli` - TOML parsing
- `rich` - Beautiful terminal output

##IMPORTANT
Before using this tool at time of commit make a file name .pre-commit-config.yaml
and then copy paste below code

# repos:

# - repo: local

# hooks:

# - id: cfgval-validate

# name: cfgval-validate

# entry: python -m cfgval.cli validate --schema cfgval/schemas/example_schema.json

# language: system

# files: \.(yml|yaml|json|toml)$ uncoomment it when you are using it

## License

MIT

from pathlib import Path
import typer
from typing import Optional, List
from .loader import load_file
from .validator import load_schema, validate_instance
from .reporters import report_human, report_json

app = typer.Typer(help="Config Validator")

@app.command()
def validate(
    paths: List[Path] = typer.Argument(..., help="Files or directories to validate"),
    schema: Optional[Path] = typer.Option(None, "--schema", "-s", help="Path to JSON schema to use"),
    json_output: bool = typer.Option(False, "--json", help="Print machine-readable JSON results")
):
    files = []
    for p in paths:
        if not p.exists():
            typer.echo(f"[yellow]Warning:[/yellow] path does not exist — skipping: {p}", err=True)
            continue

        if p.is_dir():
            for ext in ("*.yaml", "*.yml", "*.json", "*.toml"):
                files.extend(p.rglob(ext))
        else:
            files.append(p)

    if not files:
        typer.echo("No files to validate.", err=True)
        raise typer.Exit(code=1)

    # load schema once if provided
    schema_obj = None
    if schema:
        schema_obj = load_schema(schema)

    results = []
    exit_with_error = False
    for f in files:
        try:
            data = load_file(f)
        except Exception as exc:
            results.append({"file": str(f), "errors": [{"message": f"Parse error: {exc}"}]})
            exit_with_error = True
            continue

        # determine schema: passed-in or look for sibling schema.json
        target_schema = schema_obj
        if target_schema is None:
            candidate = f.parent / "schema.json"
            if candidate.exists():
                target_schema = load_schema(candidate)
            else:
                results.append({"file": str(f), "errors": [{"message": "No schema provided or found (schema.json in same dir)"}]})
                exit_with_error = True
                continue

        errors = validate_instance(data, target_schema)
        results.append({"file": str(f), "errors": errors})
        if errors:
            exit_with_error = True

    # reporting
    if json_output:
        report_json(results)
    else:
        for r in results:
            report_human(r["file"], r["errors"])

    raise typer.Exit(code=(2 if exit_with_error else 0))

if __name__ == "__main__":
    app()

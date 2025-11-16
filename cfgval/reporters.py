from rich.console import Console
from rich.table import Table
import json

console = Console()

def report_human(path, errors):
    if not errors:
        console.print(f"[green]OK[/green] — {path}")
        return
    console.print(f"[red]INVALID[/red] — {path}")
    t = Table("Path", "Validator", "Message")
    for e in errors:
        p = ".".join(map(str, e.get("path", []))) or "<root>"
        t.add_row(p, str(e.get("validator")), e.get("message"))
    console.print(t)

def report_json(results):
    # results: list of {"file": path, "errors": [...]}
    print(json.dumps(results, indent=2))

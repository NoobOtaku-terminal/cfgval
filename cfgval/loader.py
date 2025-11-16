from pathlib import Path
import json
import tomli
import yaml

def load_file(path: Path):
    text = path.read_bytes()
    suffix = path.suffix.lower()
    try:
        if suffix in (".yaml", ".yml"):
            return yaml.safe_load(text)
        elif suffix == ".json":
            return json.loads(text)
        elif suffix == ".toml":
            # tomli loads from bytes
            return tomli.loads(text.decode())
        else:
            # try JSON -> YAML -> TOML (best-effort)
            try:
                return json.loads(text)
            except Exception:
                try:
                    return yaml.safe_load(text)
                except Exception:
                    return tomli.loads(text.decode())
    except Exception as exc:
        raise ValueError(f"Failed to parse {path}: {exc}") from exc

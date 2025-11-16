from jsonschema import Draft7Validator, ValidationError, exceptions
from typing import Any, Dict, List
from pathlib import Path
import json

def load_schema(schema_path: Path) -> Dict[str, Any]:
    return json.loads(schema_path.read_text())

def validate_instance(instance: Dict[str, Any], schema: Dict[str, Any]) -> List[Dict]:
    """
    Return list of error dicts (empty if valid).
    Each dict: { "message": ..., "path": [...], "validator": ... }
    """
    validator = Draft7Validator(schema)
    errors = []
    for err in validator.iter_errors(instance):
        errors.append({
            "message": err.message,
            "path": list(err.absolute_path),
            "validator": err.validator,
            "validator_value": err.validator_value
        })
    return errors

from cfgval.validator import validate_instance
import json

schema = {
  "type": "object",
  "required": ["a"],
  "properties": { "a": {"type": "integer"} }
}

def test_validate_ok():
    errors = validate_instance({"a": 1}, schema)
    assert errors == []

def test_validate_bad():
    errors = validate_instance({"a": "x"}, schema)
    assert len(errors) > 0

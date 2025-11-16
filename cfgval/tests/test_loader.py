from pathlib import Path
from cfgval.loader import load_file
import pytest

def test_load_yaml(tmp_path):
    p = tmp_path / "c.yaml"
    p.write_text("a: 1\nb: hi")
    data = load_file(p)
    assert data["a"] == 1

def test_load_toml(tmp_path):
    p = tmp_path / "c.toml"
    p.write_text("x = 3")
    data = load_file(p)
    assert data["x"] == 3

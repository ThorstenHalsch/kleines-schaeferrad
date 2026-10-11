"""Resolve original evidence by current path, historical path, or unique filename."""
import json
from pathlib import Path

def evidence_path(root, name):
    root = Path(root)
    name = str(name)
    assets = json.loads((root / "evidence/component-index.json").read_text())["assets"]
    for asset in assets:
        if name in (asset["path"], asset["previous_path"]):
            return root / asset["path"]
    direct = root / name
    if direct.is_file():
        return direct
    direct = root / "evidence/raw" / name
    if direct.is_file():
        return direct
    matches = [asset for asset in assets if asset["filename"] == name]
    if len(matches) == 1:
        return root / matches[0]["path"]
    if len(matches) > 1:
        raise ValueError(f"Ambiguous evidence filename: {name}")
    raise FileNotFoundError(f"Unknown evidence source: {name}")

from __future__ import annotations

import random
from pathlib import Path
from typing import Any

from .util import atomic_write_json, read_json


def generate_system_key(cells: list[tuple[str, str, int]], seed: int) -> dict[str, Any]:
    rng = random.Random(seed)
    mapping: dict[str, Any] = {}
    for cell_id, condition, replicate in cells:
        key = f"{cell_id}__{condition}__r{replicate}"
        if rng.random() < 0.5:
            mapping[key] = {"A": "operator", "B": "legacy", "presentation_order": ["A", "B"] if rng.random() < 0.5 else ["B", "A"]}
        else:
            mapping[key] = {"A": "legacy", "B": "operator", "presentation_order": ["A", "B"] if rng.random() < 0.5 else ["B", "A"]}
    return {"seed": seed, "cells": mapping}


def load_or_create_key(path: Path, cells: list[tuple[str, str, int]], seed: int) -> dict[str, Any]:
    if path.exists():
        return read_json(path)
    key = generate_system_key(cells, seed)
    atomic_write_json(path, key)
    try:
        path.chmod(0o600)
    except OSError:
        pass
    return key

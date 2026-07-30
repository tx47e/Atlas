#!/usr/bin/env python3
"""Verifica intervalele grafice ale Pinaclurilor pentru Destinul compus 12."""

import importlib.util
from pathlib import Path
import sys


SCRIPT = Path(__file__).with_name("generate_harta_suprapusa.py")
spec = importlib.util.spec_from_file_location("harta_pinacluri_skill", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Nu se poate incarca {SCRIPT}")
harta = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = harta
spec.loader.exec_module(harta)

result = harta.harta_data("Birsan Daniel Robert", "19.02.1998")
assert [(start, end) for start, end, *_ in result["pinacles"]] == [
    (0, 24),
    (25, 34),
    (35, 44),
    (45, 108),
]
print("OK: Harta Pinacluri Daniel -> 0-24, 25-34, 35-44, 45-108")

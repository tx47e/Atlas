#!/usr/bin/env python3
"""Verifica intervalele Pinaclurilor pentru Destinul compus 12."""

from datetime import date
import importlib.util
from pathlib import Path
import sys


SCRIPT = Path(__file__).with_name("calculator_numerologic_examen.py")
spec = importlib.util.spec_from_file_location("calculator_pinacluri_skill", SCRIPT)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Nu se poate incarca {SCRIPT}")
calculator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = calculator
spec.loader.exec_module(calculator)

result = calculator.pinacluri(date(1998, 2, 19))
assert result["baza"]["destin_compus"] == 12
assert [row["interval_varsta"] for row in result["randuri"]] == [
    "0-24",
    "25-34",
    "35-44",
    "45+",
]
print("OK: Pinacluri Daniel -> 0-24, 25-34, 35-44, 45+")

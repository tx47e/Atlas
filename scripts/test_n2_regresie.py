#!/usr/bin/env python3
"""Regression check for the one-step N2 and N4 rules."""

from __future__ import annotations

from datetime import date
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
CALCULATORS = (
    ROOT / "scripts" / "calculator_numerologic_examen.py",
    ROOT
    / "skills"
    / "numerologie-lucrare-redactare"
    / "scripts"
    / "calculator_numerologic_examen.py",
)


def load_calculator(path: Path, index: int):
    spec = importlib.util.spec_from_file_location(f"calculator_n2_{index}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Nu se poate incarca {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    for index, path in enumerate(CALCULATORS):
        calculator = load_calculator(path, index)
        result = calculator.matrice_data_nasterii(date(1998, 2, 19))
        numbers = result["meta"]["numere_de_lucru"]
        assert numbers["n1"] == 39
        assert numbers["n2"] == 12
        assert numbers["n3"] == 37
        assert numbers["n4"] == 10
        assert result["meta"]["sir_complet"] == "1902199839123710"
        vibratii = calculator.vibratii(date(1998, 2, 19))
        assert vibratii["solutia_aspectelor_de_indreptat"]["calcul"]["rezultat"] == 10
        print(f"OK: {path} -> N1=39, N2=12, N3=37, N4=10")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

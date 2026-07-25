#!/usr/bin/env python3
"""Regression check for Destin one-step reduction and interpretation digit."""

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
    spec = importlib.util.spec_from_file_location(f"calculator_destin_{index}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Nu se poate incarca {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    for index, path in enumerate(CALCULATORS):
        calculator = load_calculator(path, index)
        result = calculator.vibratii(date(1998, 2, 19))
        assert result["calea_destinului"]["rezultat"] == 39
        destin = result["destinul_vibratia_destinului"]
        assert destin["calcul"]["intrare"] == 39
        assert destin["calcul"]["pasi"] == ["3 + 9 = 12"]
        assert destin["calcul"]["rezultat"] == 12
        assert destin["cifra_interpretare"]["intrare"] == 12
        assert destin["cifra_interpretare"]["pasi"] == ["1 + 2 = 3"]
        assert destin["cifra_interpretare"]["rezultat"] == 3
        assert result["puntea_interior_destin"]["calcul"] == "|1 - 3| = 2"
        print(f"OK: {path} -> Calea 39, Destin 12, interpretare 3")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

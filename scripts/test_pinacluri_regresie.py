#!/usr/bin/env python3
"""Regresie pentru intervalele Pinaclurilor bazate pe Destinul compus."""

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
HARTA_GENERATOR = (
    ROOT
    / "skills"
    / "numerologie-SVG-harta-suprapusa"
    / "scripts"
    / "generate_harta_suprapusa.py"
)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Nu se poate incarca {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    expected = ["0-24", "25-34", "35-44", "45+"]
    for index, path in enumerate(CALCULATORS):
        calculator = load_module(path, f"calculator_pinacluri_{index}")
        result = calculator.pinacluri(date(1998, 2, 19))
        assert result["baza"]["calea_destinului"] == 39
        assert result["baza"]["destin_compus"] == 12
        assert [row["interval_varsta"] for row in result["randuri"]] == expected
        print(f"OK: {path} -> Destin 12, intervale {expected}")

    harta = load_module(HARTA_GENERATOR, "harta_pinacluri")
    result = harta.harta_data("Birsan Daniel Robert", "19.02.1998")
    assert [(start, end) for start, end, *_ in result["pinacles"]] == [
        (0, 24),
        (25, 34),
        (35, 44),
        (45, 108),
    ]
    print(f"OK: {HARTA_GENERATOR} -> intervale grafice corecte")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

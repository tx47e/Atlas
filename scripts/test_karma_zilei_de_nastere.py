from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CALCULATORS = (
    ROOT / "scripts" / "calculator_numerologic_examen.py",
    ROOT / "skills" / "numerologie-lucrare-redactare" / "scripts" / "calculator_numerologic_examen.py",
)
CASES = {
    1: (1, "spre 100%"),
    9: (9, "spre 100%"),
    10: (10, "spre 80%"),
    19: (19, "spre 80%"),
    20: (20, "spre 60%"),
    22: (0, "spre 60%"),
    23: (1, "spre 60%"),
    29: (7, "spre 60%"),
    30: (8, "spre 40%"),
    31: (9, "spre 40%"),
}


def load(path: Path, index: int):
    spec = importlib.util.spec_from_file_location(f"karma_calculator_{index}", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    for index, path in enumerate(CALCULATORS):
        module = load(path, index)
        for day, (arcana, percentage) in CASES.items():
            assert module.karma_zilei_de_nastere(day) == {
                "zi": day,
                "arcana": arcana,
                "procent": percentage,
            }
        for invalid in (0, 32):
            try:
                module.karma_zilei_de_nastere(invalid)
            except ValueError:
                pass
            else:
                raise AssertionError(f"Zi invalida acceptata: {invalid}")
    print("Karma zilei de nastere: OK")


if __name__ == "__main__":
    main()

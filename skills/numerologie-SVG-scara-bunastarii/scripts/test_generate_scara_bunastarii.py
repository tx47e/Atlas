#!/usr/bin/env python3
"""Test reprezentativ pentru modelul Daniel."""

from __future__ import annotations

from datetime import datetime
import importlib.util
from pathlib import Path
import sys
import xml.etree.ElementTree as ET


SCRIPT = Path(__file__).with_name("generate_scara_bunastarii.py")
SPEC = importlib.util.spec_from_file_location("generate_scara_bunastarii", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Nu se poate incarca {SCRIPT}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def main() -> int:
    birth_date = datetime.strptime("19.02.1998", "%d.%m.%Y")
    data = MODULE.calculate(birth_date)
    expected = [51, 42, 40, 36, 14, 13, 12, 11, 8, 7, 6, 4, 4, 0, 0, 0, 0]
    assert [row["value"] for row in data["rows"]] == expected
    assert [row["label"] for row in data["rows"][-4:]] == [
        "Vector 456 - Vointa",
        "Casuta 4",
        "Casuta 5",
        "Casuta 6",
    ]
    assert data["n1"] == 39
    assert data["n2"] == 12
    assert data["full_code"] == "190219983912371"
    svg = MODULE.render_svg("Birsan Daniel Robert", birth_date, data)
    ET.fromstring(svg)
    assert svg.count('class="wellbeing-row"') == 17
    assert "Vector 789 - Creativitate" in svg
    assert "Atlas Numerologie" in svg
    print("OK: model Daniel, 17 trepte, N2=12, SVG valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

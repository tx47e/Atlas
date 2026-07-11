#!/usr/bin/env python3
"""Generate a self-contained Numerologie SVG Triunghiul Financiar."""

from __future__ import annotations

import argparse
import html
import re
import sys
from dataclasses import dataclass
from pathlib import Path


WIDTH = 1000
HEIGHT = 760
TRIANGLE_POINTS = "500,82 299,700 701,700"
TRIANGLE_FILL = "#ff1017"
TRIANGLE_STROKE = "#1f1f1f"
WATERMARK = "Atlas Numerologie"


@dataclass(frozen=True)
class FinancialTriangle:
    name: str
    day_raw: str
    month_raw: str
    year_raw: str
    day_value: int
    month_value: int
    year_value: int
    destiny_sum: int
    destiny_value: int

    @property
    def code(self) -> str:
        return f"{self.day_value}{self.month_value}{self.year_value}{self.destiny_value}"

    @property
    def formula(self) -> str:
        return (
            f"{self.day_raw} -> {self.day_value} | "
            f"{self.month_raw} -> {self.month_value} | "
            f"{self.year_raw} -> {self.year_value} | "
            f"{self.day_value} + {self.month_value} + {self.year_value} = "
            f"{self.destiny_sum} -> {self.destiny_value}"
        )


def reduce_to_digit(value: int) -> int:
    """Reduce a positive integer to one digit using standard digit sums."""
    if value < 0:
        raise ValueError("Value must be positive.")
    while value > 9:
        value = sum(int(char) for char in str(value))
    return value


def parse_birth_date(birth_date: str) -> tuple[str, str, str]:
    match = re.fullmatch(r"\s*(\d{1,2})[./-](\d{1,2})[./-](\d{4})\s*", birth_date)
    if not match:
        raise ValueError("Birth date must use dd.mm.yyyy, dd/mm/yyyy, or dd-mm-yyyy.")

    day_raw, month_raw, year_raw = match.groups()
    day = int(day_raw)
    month = int(month_raw)
    year = int(year_raw)

    if not 1 <= day <= 31:
        raise ValueError("Birth day must be between 1 and 31.")
    if not 1 <= month <= 12:
        raise ValueError("Birth month must be between 1 and 12.")
    if year < 1:
        raise ValueError("Birth year must be positive.")

    return day_raw.zfill(2), month_raw.zfill(2), year_raw


def calculate(name: str, birth_date: str) -> FinancialTriangle:
    day_raw, month_raw, year_raw = parse_birth_date(birth_date)
    day_value = reduce_to_digit(int(day_raw))
    month_value = reduce_to_digit(int(month_raw))
    year_value = reduce_to_digit(int(year_raw))
    destiny_sum = day_value + month_value + year_value
    destiny_value = reduce_to_digit(destiny_sum)

    return FinancialTriangle(
        name=name.strip(),
        day_raw=day_raw,
        month_raw=month_raw,
        year_raw=year_raw,
        day_value=day_value,
        month_value=month_value,
        year_value=year_value,
        destiny_sum=destiny_sum,
        destiny_value=destiny_value,
    )


def svg_text(data: FinancialTriangle) -> str:
    title = html.escape(f"Triunghiul financiar - {data.name}", quote=False)
    formula = html.escape(data.formula, quote=False)
    code = html.escape(data.code, quote=False)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <rect width="{WIDTH}" height="{HEIGHT}" fill="#ffffff"/>
  <text x="500" y="38" text-anchor="middle" font-family="Georgia, serif" font-size="28" fill="#242424">{title}</text>
  <text x="500" y="66" text-anchor="middle" font-family="Arial, sans-serif" font-size="15" fill="#444444">{formula}</text>

  <!-- Isosceles triangle with apex angle 36 degrees and base angles 72 degrees. -->
  <polygon points="{TRIANGLE_POINTS}" fill="{TRIANGLE_FILL}" stroke="{TRIANGLE_STROKE}" stroke-width="4" stroke-linejoin="round"/>

  <text x="500" y="678" text-anchor="middle" font-family="Arial Black, Arial, sans-serif" font-size="116" font-weight="900" fill="#2b2b2b">{code}</text>

  <text x="500" y="728" text-anchor="middle" font-family="Arial, sans-serif" font-size="15" fill="#444444">apex 36 grade | unghiuri baza 72 si 72 grade</text>
  <text x="980" y="745" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#aaa" font-weight="800">{WATERMARK}</text>
</svg>
'''


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate Triunghiul Financiar SVG from a name and birth date."
    )
    parser.add_argument("--name", required=True, help="Full person name.")
    parser.add_argument(
        "--birth-date",
        required=True,
        help="Birth date in dd.mm.yyyy, dd/mm/yyyy, or dd-mm-yyyy format.",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Destination SVG path.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        data = calculate(args.name, args.birth_date)
        svg = svg_text(data)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(svg, encoding="utf-8", newline="\n")
    except Exception as exc:  # noqa: BLE001 - CLI should print concise errors.
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Generated: {args.output}")
    print(f"Triunghiul financiar: {data.code}")
    print(f"Calcul: {data.formula}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Genereaza SVG-ul autonom Scara Bunastarii din data nasterii."""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import html
from pathlib import Path


VECTORI = {
    "123": "Energie",
    "456": "Vointa",
    "789": "Creativitate",
    "147": "Spiritualitate",
    "258": "Social",
    "369": "Bunastare materiala",
    "159": "Cariera",
    "357": "Scopuri",
}
ELEMENTE = {
    1: ("Foc", "#e45745", "#a7332a"),
    2: ("Apa", "#2878c7", "#18528f"),
    3: ("Aer", "#a9bdcc", "#6f8798"),
    4: ("Pamant", "#9a6a43", "#684226"),
    5: ("Foc", "#e45745", "#a7332a"),
    6: ("Apa", "#2878c7", "#18528f"),
    7: ("Aer", "#a9bdcc", "#6f8798"),
    8: ("Pamant", "#9a6a43", "#684226"),
    9: ("Foc", "#e45745", "#a7332a"),
}


def parse_birth_date(value: str) -> datetime:
    for pattern in ("%d.%m.%Y", "%d-%m-%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(value.strip(), pattern)
        except ValueError:
            pass
    raise ValueError("Data trebuie sa fie in formatul ZZ.LL.AAAA.")


def digits(value: int | str) -> list[int]:
    return [int(char) for char in str(value) if char.isdigit()]


def reduce_fully(value: int) -> int:
    current = abs(value)
    while current > 9:
        current = sum(digits(current))
    return current


def first_nonzero_digit(value: int) -> int:
    for char in str(abs(value)):
        if char != "0":
            return int(char)
    raise ValueError("Ziua nasterii trebuie sa contina o cifra nenula.")


def calculate(birth_date: datetime) -> dict:
    compact = birth_date.strftime("%d%m%Y")
    n1 = sum(digits(compact))
    n2 = sum(digits(n1))
    n3 = n1 - 2 * first_nonzero_digit(birth_date.day)
    n4 = reduce_fully(n3)
    full_code = f"{compact}{n1}{n2}{n3}{n4}"
    occurrences = Counter(int(char) for char in full_code if char != "0")

    cells = {
        str(number): {
            "count": occurrences[number],
            "value": number * occurrences[number],
        }
        for number in range(1, 10)
    }

    rows = []
    for code, label in VECTORI.items():
        value = sum(cells[char]["value"] for char in code)
        rows.append(
            {
                "type": "vector",
                "key": code,
                "label": f"Vector {code} - {label}",
                "value": value,
            }
        )
    for number in range(1, 10):
        rows.append(
            {
                "type": "cell",
                "key": str(number),
                "label": f"Casuta {number}",
                "value": cells[str(number)]["value"],
            }
        )

    rows.sort(
        key=lambda row: (
            -row["value"],
            0 if row["type"] == "vector" else 1,
            row["key"],
        )
    )
    return {
        "compact": compact,
        "n1": n1,
        "n2": n2,
        "n3": n3,
        "n4": n4,
        "full_code": full_code,
        "rows": rows,
    }


def text(value: str) -> str:
    return html.escape(value, quote=True)


def render_svg(name: str, birth_date: datetime, data: dict) -> str:
    width = 1400
    height = 1120
    left = 70
    label_width = 330
    track_x = 425
    track_width = 800
    value_x = 1290
    row_start = 190
    row_height = 46
    maximum = max(row["value"] for row in data["rows"]) or 1
    rows_svg = []

    for index, row in enumerate(data["rows"]):
        y = row_start + index * row_height
        bar_width = round(track_width * row["value"] / maximum, 2)
        if row["type"] == "vector":
            label_color = "#0f6f73"
            label_weight = "700"
            dot = ""
        else:
            number = int(row["key"])
            _, fill, stroke = ELEMENTE[number]
            label_color = "#3d2c22"
            label_weight = "600"
            dot = (
                f'<circle cx="{left + 7}" cy="{y - 5}" r="7" '
                f'fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
            )
        label_x = left + (24 if dot else 0)
        rows_svg.append(
            f'<g class="wellbeing-row">{dot}'
            f'<text x="{label_x}" y="{y}" fill="{label_color}" '
            f'font-family="Arial,Helvetica,sans-serif" font-size="19" '
            f'font-weight="{label_weight}">{text(row["label"])}</text>'
            f'<rect x="{track_x}" y="{y - 18}" width="{track_width}" height="18" '
            f'rx="9" fill="#eee3d2"/>'
            f'<rect x="{track_x}" y="{y - 18}" width="{bar_width}" height="18" '
            f'rx="9" fill="url(#bar-gradient)"/>'
            f'<text x="{value_x}" y="{y}" text-anchor="end" fill="#173b3d" '
            f'font-family="Arial,Helvetica,sans-serif" font-size="20" '
            f'font-weight="800">{row["value"]}</text></g>'
        )

    legend_items = []
    legend_x = 435
    for label, fill, stroke in (
        ("Foc", "#e45745", "#a7332a"),
        ("Pamant", "#9a6a43", "#684226"),
        ("Apa", "#2878c7", "#18528f"),
        ("Aer", "#a9bdcc", "#6f8798"),
    ):
        legend_items.append(
            f'<circle cx="{legend_x}" cy="1015" r="7" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
            f'<text x="{legend_x + 14}" y="1021" fill="#a4772b" font-family="Arial,Helvetica,sans-serif" '
            f'font-size="16" font-weight="700">{label}</text>'
        )
        legend_x += 145

    subtitle = (
        f'{birth_date.strftime("%d.%m.%Y")} | N1={data["n1"]} | N2={data["n2"]} | '
        f'N3={data["n3"]} | N4={data["n4"]} | Sir: {data["full_code"]}'
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<defs><linearGradient id="bar-gradient" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0f6f73"/><stop offset="1" stop-color="#c6953f"/></linearGradient></defs>
<rect width="{width}" height="{height}" fill="#fbf7ef"/>
<rect x="38" y="32" width="1324" height="1032" rx="18" fill="#fffdf8" stroke="#d9c7aa" stroke-width="2"/>
<text x="700" y="83" text-anchor="middle" fill="#173b3d" font-family="Georgia,serif" font-size="35" font-weight="700">Scara Bunastarii</text>
<text x="700" y="121" text-anchor="middle" fill="#8c6423" font-family="Georgia,serif" font-size="24">{text(name)}</text>
<text x="700" y="151" text-anchor="middle" fill="#6d5b50" font-family="Arial,Helvetica,sans-serif" font-size="16">{text(subtitle)}</text>
{''.join(rows_svg)}
<g aria-label="Legenda elemente">{''.join(legend_items)}</g>
<text x="1340" y="1090" text-anchor="end" font-family="Arial,Helvetica,sans-serif" font-size="14" fill="#aaa" font-weight="800">Atlas Numerologie</text>
</svg>'''


def main() -> int:
    parser = argparse.ArgumentParser(description="Genereaza SVG-ul Scara Bunastarii.")
    parser.add_argument("--name", required=True, help="Numele complet al persoanei")
    parser.add_argument("--birth-date", required=True, help="Data nasterii ZZ.LL.AAAA")
    parser.add_argument("--output", required=True, type=Path, help="Calea SVG de iesire")
    args = parser.parse_args()

    birth_date = parse_birth_date(args.birth_date)
    data = calculate(birth_date)
    svg = render_svg(args.name, birth_date, data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(svg, encoding="utf-8", newline="\n")
    top = ", ".join(f'{row["label"]}={row["value"]}' for row in data["rows"][:3])
    zero = ", ".join(row["label"] for row in data["rows"] if row["value"] == 0)
    print(f"Generated: {args.output}")
    print(f"Top 3: {top}")
    print(f"Zero: {zero or '-'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Generate a self-contained Numerologie SVG Soarta si Destin."""

from __future__ import annotations

import argparse
import html
import re
import sys
from dataclasses import dataclass
from pathlib import Path


WIDTH, HEIGHT = 1200, 720
CHART_X, CHART_Y, CHART_W, CHART_H = 95, 130, 735, 400
PAPER, FATE, DESTINY = "#f4e5d4", "#bf6b2c", "#116466"


@dataclass(frozen=True)
class ChartData:
    name: str
    short_name: str
    date: str
    fate_left: int
    fate_right: int
    destiny_left: int
    destiny_right: int
    fate: str
    destiny: str
    fate_comfort: float
    destiny_comfort: float
    ages: list[int]
    interval: int
    tendency: str


def parse_birth_date(value: str) -> tuple[str, str, str]:
    match = re.fullmatch(r"\s*(\d{1,2})[./-](\d{1,2})[./-](\d{4})\s*", value)
    if not match:
        raise ValueError("Birth date must use dd.mm.yyyy, dd/mm/yyyy, or dd-mm-yyyy.")
    day, month, year = match.groups()
    if not 1 <= int(day) <= 31 or not 1 <= int(month) <= 12 or int(year) < 1:
        raise ValueError("Birth date contains an invalid day, month, or year.")
    return day.zfill(2), month.zfill(2), year


def fmt(value: float) -> str:
    return f"{value:.2f}".replace(".", ",")


def calculate(name: str, birth_date: str) -> ChartData:
    day, month, year = parse_birth_date(birth_date)
    date_code = f"{day}{month}{year}"
    raw_left, raw_right = int(f"{day}{month}"), int(year)
    adjusted = "".join("1" if digit == "0" else digit for digit in date_code)
    adjusted_left, adjusted_right = int(adjusted[:4]), int(adjusted[4:])
    fate = f"{raw_left * raw_right:07d}"
    destiny = f"{adjusted_left * adjusted_right:07d}"
    odd = sum(int(digit) % 2 for digit in date_code)
    even = len(date_code) - odd
    interval = 12 if even > odd else 10
    tendency = "para / feminina" if interval == 12 else "impara / masculina"
    return ChartData(
        name=name.strip(),
        short_name=name.strip().split()[1] if len(name.strip().split()) > 1 else name.strip(),
        date=f"{day}.{month}.{year}",
        fate_left=raw_left,
        fate_right=raw_right,
        destiny_left=adjusted_left,
        destiny_right=adjusted_right,
        fate=fate,
        destiny=destiny,
        fate_comfort=sum(map(int, fate)) / 7,
        destiny_comfort=sum(map(int, destiny)) / 7,
        ages=[index * interval for index in range(7)],
        interval=interval,
        tendency=tendency,
    )


def point(index: int, value: int) -> tuple[float, float]:
    return CHART_W * index / 6, CHART_H * (9 - value) / 9


def text(x: float, y: float, content: str, css: str, anchor: str | None = None) -> str:
    suffix = f' text-anchor="{anchor}"' if anchor else ""
    return f'<text class="{css}" x="{x:.1f}" y="{y:.1f}"{suffix}>{html.escape(content)}</text>'


def join_ro(values: list[str]) -> str:
    if not values:
        return "niciuna"
    if len(values) == 1:
        return values[0]
    return ", ".join(values[:-1]) + " si " + values[-1]


def svg_text(data: ChartData) -> str:
    fate_values = [int(value) for value in data.fate]
    destiny_values = [int(value) for value in data.destiny]
    fate_points = " ".join(f"{x:.1f},{y:.1f}" for x, y in (point(i, value) for i, value in enumerate(fate_values)))
    destiny_points = " ".join(f"{x:.1f},{y:.1f}" for x, y in (point(i, value) for i, value in enumerate(destiny_values)))
    fate_y = CHART_H * (9 - data.fate_comfort) / 9
    destiny_y = CHART_H * (9 - data.destiny_comfort) / 9
    meeting = [index + 1 for index, (left, right) in enumerate(zip(fate_values, destiny_values)) if left == right]
    crossing = [index + 1 for index, (left, right) in enumerate(zip(fate_values, destiny_values)) if left != right]
    crossing_ages = []
    crossing_actions = []
    for index in crossing:
        fate, destiny = fate_values[index - 1], destiny_values[index - 1]
        direction = "ridica" if destiny > fate else "coboara"
        crossing_ages.append(str(data.ages[index - 1]))
        prefix = "destinul " if not crossing_actions else ""
        crossing_actions.append(f"{prefix}{direction} {fate} la {destiny}")

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
        f'  <title>Soarta si destin - {html.escape(data.name)}</title>',
        '  <defs><style>',
        f'.paper{{fill:{PAPER}}}.axis{{stroke:#2d2d2d;stroke-width:2}}.grid{{stroke:#cdbda7;stroke-width:1;opacity:.75}}',
        f'.comfort-fate{{stroke:{FATE};stroke-width:2.5;stroke-dasharray:9 7}}.comfort-destiny{{stroke:{DESTINY};stroke-width:2.5;stroke-dasharray:4 6}}',
        f'.fate{{fill:none;stroke:{FATE};stroke-width:5;stroke-linejoin:round;stroke-linecap:round}}.destiny{{fill:none;stroke:{DESTINY};stroke-width:5;stroke-linejoin:round;stroke-linecap:round}}',
        f'.fate-dot{{fill:{FATE};stroke:{PAPER};stroke-width:3}}.destiny-dot{{fill:{DESTINY};stroke:{PAPER};stroke-width:3}}.meet-dot{{fill:#2d2d2d;stroke:{PAPER};stroke-width:3}}',
        '.title{font-family:Arial,Helvetica,sans-serif;font-size:30px;font-weight:800;fill:#242424}.subtitle{font-family:Arial,Helvetica,sans-serif;font-size:17px;font-weight:700;fill:#555}.label{font-family:Arial,Helvetica,sans-serif;font-size:15px;fill:#333}.small{font-family:Arial,Helvetica,sans-serif;font-size:13px;fill:#555}.value{font-family:Arial,Helvetica,sans-serif;font-size:16px;font-weight:800;fill:#111;text-anchor:middle}.legend{font-family:Arial,Helvetica,sans-serif;font-size:16px;font-weight:800;fill:#222}',
        '  </style></defs>',
        f'  <rect class="paper" width="{WIDTH}" height="{HEIGHT}"/>',
        text(60, 54, f"Soarta si destin - {data.name}", "title"),
        text(60, 82, f"Data nasterii: {data.date} | Soarta: {data.fate_left} x {data.fate_right} = {data.fate} | Destin: {data.destiny_left} x {data.destiny_right} = {data.destiny}", "subtitle"),
        f'  <g id="chart" transform="translate({CHART_X},{CHART_Y})">',
        f'    <line class="axis" x1="0" y1="{CHART_H}" x2="{CHART_W}" y2="{CHART_H}"/><line class="axis" x1="0" y1="0" x2="0" y2="{CHART_H}"/>',
        '    <g class="grid">',
    ]
    lines.extend(f'      <line x1="0" y1="{CHART_H * (9 - value) / 9:.1f}" x2="{CHART_W}" y2="{CHART_H * (9 - value) / 9:.1f}"/>' for value in range(10))
    lines.extend(f'      <line x1="{CHART_W * index / 6:.1f}" y1="0" x2="{CHART_W * index / 6:.1f}" y2="{CHART_H}"/>' for index in range(7))
    lines += [
        '    </g>',
        f'    <line class="comfort-fate" x1="0" y1="{fate_y:.1f}" x2="{CHART_W}" y2="{fate_y:.1f}"/>',
        f'    <line class="comfort-destiny" x1="0" y1="{destiny_y:.1f}" x2="{CHART_W}" y2="{destiny_y:.1f}"/>',
        f'    <polyline class="fate" points="{fate_points}"/><polyline class="destiny" points="{destiny_points}"/>',
    ]
    for index, (fate, destiny) in enumerate(zip(fate_values, destiny_values)):
        x, fate_point_y = point(index, fate)
        _, destiny_point_y = point(index, destiny)
        if fate == destiny:
            lines.append(f'    <circle class="meet-dot" cx="{x:.1f}" cy="{fate_point_y:.1f}" r="10"/>' + text(x, max(fate_point_y - 19, 12), str(fate), "value", "middle"))
        else:
            lines.append(f'    <circle class="fate-dot" cx="{x:.1f}" cy="{fate_point_y:.1f}" r="9"/>' + text(x, max(fate_point_y - 18, 12), str(fate), "value", "middle"))
            lines.append(f'    <circle class="destiny-dot" cx="{x:.1f}" cy="{destiny_point_y:.1f}" r="9"/>' + text(x, max(destiny_point_y - 18, 12), str(destiny), "value", "middle"))
    lines.append('    <g class="label">')
    lines.extend(text(-24, CHART_H * (9 - value) / 9 + 5, str(value), "label") for value in range(10))
    lines.extend(text(CHART_W * index / 6, 430, str(age), "label", "middle") for index, age in enumerate(data.ages))
    lines += [
        text(CHART_W / 2, 462, f"Varsta / etape de {data.interval} ani", "label", "middle"),
        '      <text class="label" x="-72" y="214" transform="rotate(-90 -72 214)">Valoare cifra</text>',
        '    </g>',
        '  </g>',
    ]
    lines += [
        '  <g transform="translate(900,150)">', text(0, 0, "Legenda", "legend"),
        f'    <line class="fate" x1="0" y1="34" x2="70" y2="34"/>{text(88, 39, f"Soarta {data.fate}", "label")}',
        f'    <line class="destiny" x1="0" y1="70" x2="70" y2="70"/>{text(88, 75, f"Destin {data.destiny}", "label")}',
        f'    <line class="comfort-fate" x1="0" y1="108" x2="70" y2="108"/>{text(88, 113, f"Confort Soarta {fmt(data.fate_comfort)}", "label")}',
        f'    <line class="comfort-destiny" x1="0" y1="136" x2="70" y2="136"/>{text(88, 141, f"Confort Destin {fmt(data.destiny_comfort)}", "label")}',
        f'    <circle class="meet-dot" cx="12" cy="174" r="8"/>{text(34, 179, "Punct de intalnire", "label")}',
        text(0, 210, "Intalniri: pozitiile " + (", ".join(map(str, meeting)) or "niciuna"), "small"),
        text(0, 233, "Rascruci: pozitiile " + join_ro([str(value) for value in crossing]), "small"),
        '  </g>',
        f'  <g transform="translate(60,640)">{text(0, 0, f"Sinteza: pentru {data.short_name} folosim intervale de {data.interval} ani, deoarece data are predominanta {data.tendency}.", "subtitle")}{text(0, 24, f"Liniile sunt apropiate; rascrucile apar la {join_ro(crossing_ages)} de ani, unde {join_ro(crossing_actions)}.", "subtitle")}</g>',
        f'  <text x="1180" y="705" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#aaa" font-weight="800">Atlas Numerologie</text>',
        '</svg>',
    ]
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate Soarta si Destin SVG from a name and birth date.")
    parser.add_argument("--name", required=True, help="Full person name.")
    parser.add_argument("--birth-date", required=True, help="Birth date in dd.mm.yyyy, dd/mm/yyyy, or dd-mm-yyyy format.")
    parser.add_argument("--output", required=True, type=Path, help="Destination SVG path.")
    args = parser.parse_args(argv)
    try:
        data = calculate(args.name, args.birth_date)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(svg_text(data), encoding="utf-8", newline="\n")
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Generated: {args.output}")
    print(f"Soarta: {data.fate} | Destin: {data.destiny}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

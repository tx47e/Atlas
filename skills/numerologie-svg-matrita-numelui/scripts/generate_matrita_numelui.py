from __future__ import annotations

import argparse
import html
import math
import re
import unicodedata
from collections import Counter
from datetime import datetime
from pathlib import Path

ALPHABET = {**dict.fromkeys("AJS", 1), **dict.fromkeys("BKT", 2), **dict.fromkeys("CLU", 3), **dict.fromkeys("DMV", 4), **dict.fromkeys("ENW", 5), **dict.fromkeys("FOX", 6), **dict.fromkeys("GPY", 7), **dict.fromkeys("HQZ", 8), **dict.fromkeys("IR", 9)}
ORDER = ((1, 4, 7), (2, 5, 8), (3, 6, 9))
OPTIMUM = {1: "111", 2: "222", 3: "333", 4: "44", 5: "55", 6: "66", 7: "7", 8: "8", 9: "9"}
COLORS = {1: "#e6b4a9", 2: "#b8d9e7", 3: "#fffaf3", 4: "#d8c1a2", 5: "#e6b4a9", 6: "#b8d9e7", 7: "#fffaf3", 8: "#d8c1a2", 9: "#e6b4a9"}


def reduce_full(value: int) -> int:
    while value > 9:
        value = sum(map(int, str(value)))
    return value


def parse_date(value: str):
    for fmt in ("%d.%m.%Y", "%d-%m-%Y", "%d/%m/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            pass
    raise ValueError("Data trebuie sa fie ZZ.LL.AAAA, ZZ-LL-AAAA, ZZ/LL/AAAA sau AAAA-LL-ZZ.")


def normalize(value: str) -> str:
    decomposed = unicodedata.normalize("NFD", value.upper())
    return re.sub(r"[^A-Z]", "", "".join(c for c in decomposed if unicodedata.category(c) != "Mn"))


def name_values(name: str) -> list[int]:
    return [ALPHABET[c] for c in normalize(name) if c in ALPHABET]


def expression_number(name: str) -> int:
    component_reductions = []
    for component in re.split(r"\s+", name.strip()):
        values = name_values(component)
        if values:
            component_reductions.append(reduce_full(sum(values)))
    return reduce_full(sum(component_reductions)) if component_reductions else 0


def date_counts(birth_date: str) -> Counter[int]:
    born = parse_date(birth_date)
    compact = born.strftime("%d%m%Y")
    n1 = sum(map(int, compact))
    n2 = sum(map(int, str(n1)))
    first_day_digit = next(int(c) for c in f"{born.day:02d}" if c != "0")
    n3 = n1 - 2 * first_day_digit
    n4 = sum(map(int, str(abs(n3))))
    return Counter(int(c) for c in f"{compact}{n1}{n2}{n3}{n4}" if c != "0")


def compare_counts(name: Counter[int], date: Counter[int]) -> dict[str, object]:
    supported = [digit for digit in range(1, 10) if name[digit] and date[digit]]
    excess = {digit: name[digit] - date[digit] for digit in range(1, 10) if name[digit] - date[digit] >= 2}
    missing = [digit for digit in range(1, 10) if date[digit] and not name[digit]]
    potential = [digit for digit in range(1, 10) if name[digit] and not date[digit]]
    vectors = {"123": "Energie", "456": "Vointa", "789": "Creativitate", "147": "Spiritualitate", "258": "Social", "369": "Bunastare materiala", "159": "Cariera", "357": "Scopuri"}
    active_name = [f"{code}, {label}" for code, label in vectors.items() if all(name[int(d)] for d in code)]
    active_date = [f"{code}, {label}" for code, label in vectors.items() if all(date[int(d)] for d in code)]
    max_name = max(name.values(), default=0)
    max_date = max(date.values(), default=0)
    return {
        "dominant_name": [digit for digit in range(1, 10) if name[digit] == max_name and max_name],
        "dominant_date": [digit for digit in range(1, 10) if date[digit] == max_date and max_date],
        "supported": supported,
        "excess_name": excess,
        "missing_name": missing,
        "name_potential": potential,
        "active_vectors_name": active_name,
        "active_vectors_date": active_date,
    }


def points(n: int, cx: float, cy: float, radius: float, step: int = 1, rotation: float = -math.pi / 2) -> str:
    base = [(cx + radius * math.cos(rotation + 2 * math.pi * i / n), cy + radius * math.sin(rotation + 2 * math.pi * i / n)) for i in range(n)]
    ordered, current = [], 0
    for _ in range(n):
        ordered.append(base[current])
        current = (current + step) % n
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in ordered)


def geometry(count: int, cx: float, cy: float) -> tuple[str, str]:
    style = 'fill="none" stroke="#0b2b2c" stroke-width="2.4" stroke-linejoin="round"'
    if count == 0:
        return "", "absent"
    if count == 1:
        return f'<circle cx="{cx}" cy="{cy}" r="11" {style}/>', "cerc"
    if count == 2:
        return (f'<line x1="{cx-8}" y1="{cy}" x2="{cx+8}" y2="{cy}" {style}/><circle cx="{cx-19}" cy="{cy}" r="10" {style}/><circle cx="{cx+19}" cy="{cy}" r="10" {style}/>', "doua cercuri legate")
    if count == 3:
        return f'<polygon points="{points(3, cx, cy, 20)}" {style}/>', "triunghi"
    if count == 4:
        return f'<rect x="{cx-16}" y="{cy-16}" width="32" height="32" {style}/>', "patrat"
    if count == 5:
        return f'<polygon points="{points(5, cx, cy, 21, 2)}" {style}/>', "pentagrama"
    if count == 6:
        return f'<polygon points="{points(3, cx, cy, 21)}" {style}/><polygon points="{points(3, cx, cy, 21, rotation=math.pi/2)}" {style}/>', "hexagrama"
    if count == 7:
        return f'<polygon points="{points(7, cx, cy, 22, 3)}" {style}/>', "septagrama"
    if count == 8:
        return f'<polygon points="{points(8, cx, cy, 22)}" {style}/>', "octogon"
    return f'<polygon points="{points(count, cx, cy, 22)}" {style}/>', f"poligon regulat cu {count} laturi"


def build_svg(name: str, birth_date: str) -> tuple[str, dict[str, object]]:
    values = name_values(name)
    expression = expression_number(name)
    matrix_values = values + ([expression] if expression else [])
    counts = Counter(matrix_values)
    baseline = date_counts(birth_date)
    comparison = compare_counts(counts, baseline)
    code = "".join(map(str, values))
    cells = []
    for row, digits in enumerate(ORDER):
        for col, digit in enumerate(digits):
            x, y, w, h = 75 + col * 250, 245 + row * 180, 235, 165
            shown = str(digit) * counts[digit] if counts[digit] else "—"
            date_shown = str(digit) * baseline[digit] if baseline[digit] else "—"
            shape, label = geometry(counts[digit], x + 194, y + 127)
            cells.append(f'<g aria-label="Casuta {digit}: data {html.escape(date_shown)}; nume {html.escape(shown)}; {html.escape(label)}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{COLORS[digit]}" stroke="#0b2b2c" stroke-opacity=".25"/><text x="{x+12}" y="{y+22}" class="small">data {html.escape(date_shown)}</text><text x="{x+w/2}" y="{y+86}" class="value" text-anchor="middle">{html.escape(shown)}</text><text x="{x+12}" y="{y+h-13}" class="small">optim {OPTIMUM[digit]}</text>{shape}</g>')
    title_name = html.escape(name.strip())
    subtitle = html.escape(f"cod {code} · exprimare {expression} · exprimarea este introdusa in matrice")
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="850" viewBox="0 0 900 850" role="img" aria-labelledby="title desc"><title id="title">Matrita numelui pentru {title_name}</title><desc id="desc">Matrice numerologica 3 pe 3 comparata cu data si optimul.</desc><style>.title{{font:700 31px Georgia,serif;fill:#0b2b2c}}.name{{font:700 22px Arial,sans-serif;fill:#0b2b2c}}.sub{{font:14px Arial,sans-serif;fill:#365455}}.value{{font:800 30px Georgia,serif;fill:#0b2b2c}}.small{{font:13px Arial,sans-serif;fill:#284748}}</style><rect width="900" height="850" fill="#f7efe3"/><text x="450" y="68" text-anchor="middle" class="title">Matrita numelui</text><text x="450" y="108" text-anchor="middle" class="name">{title_name}</text><text x="450" y="145" text-anchor="middle" class="sub">{subtitle}</text>{''.join(cells)}<text x="825" y="820" text-anchor="end" class="sub">Atlas Numerologie</text></svg>'''
    return svg, {"code": code, "expression": expression, "counts": dict(counts), "date_counts": dict(baseline), "comparison": comparison}


def main() -> None:
    parser = argparse.ArgumentParser(description="Genereaza Matrita numelui in SVG.")
    parser.add_argument("--name", required=True)
    parser.add_argument("--birth-date", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    svg, _ = build_svg(args.name, args.birth_date)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(svg, encoding="utf-8")
    print(output.resolve())


if __name__ == "__main__":
    main()

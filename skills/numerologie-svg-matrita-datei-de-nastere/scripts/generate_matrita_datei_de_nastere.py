from __future__ import annotations

import argparse
import html
import math
from collections import Counter
from datetime import datetime
from pathlib import Path

ORDER = ((1, 4, 7), (2, 5, 8), (3, 6, 9))
OPTIMUM = {1: "111", 2: "222", 3: "333", 4: "44", 5: "55", 6: "66", 7: "7", 8: "8", 9: "9"}
COLORS = {1: "#e6b4a9", 2: "#b8d9e7", 3: "#fffaf3", 4: "#d8c1a2", 5: "#e6b4a9", 6: "#b8d9e7", 7: "#fffaf3", 8: "#d8c1a2", 9: "#e6b4a9"}


def reduce_once(value: int) -> int:
    return sum(int(c) for c in str(abs(value)))


def parse_date(value: str):
    for fmt in ("%d.%m.%Y", "%d-%m-%Y", "%d/%m/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            pass
    raise ValueError("Data trebuie sa fie ZZ.LL.AAAA, ZZ-LL-AAAA, ZZ/LL/AAAA sau AAAA-LL-ZZ.")


def points(n: int, cx: float, cy: float, radius: float, step: int = 1, rotation: float = -math.pi / 2) -> str:
    base = [(cx + radius * math.cos(rotation + 2 * math.pi * i / n), cy + radius * math.sin(rotation + 2 * math.pi * i / n)) for i in range(n)]
    order, current = [], 0
    for _ in range(n):
        order.append(base[current])
        current = (current + step) % n
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in order)


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
    born = parse_date(birth_date)
    compact = born.strftime("%d%m%Y")
    n1 = sum(map(int, compact))
    n2 = reduce_once(n1)
    first_day_digit = next(int(c) for c in f"{born.day:02d}" if c != "0")
    n3 = n1 - 2 * first_day_digit
    n4 = reduce_once(n3)
    sequence = f"{compact}{n1}{n2}{n3}{n4}"
    counts = Counter(int(c) for c in sequence if c != "0")
    cells = []
    for row, digits in enumerate(ORDER):
        for col, digit in enumerate(digits):
            x, y, w, h = 75 + col * 250, 245 + row * 180, 235, 165
            shown = str(digit) * counts[digit] if counts[digit] else "—"
            shape, label = geometry(counts[digit], x + 194, y + 127)
            cells.append(f'<g aria-label="Casuta {digit}: {html.escape(shown)}; {html.escape(label)}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{COLORS[digit]}" stroke="#0b2b2c" stroke-opacity=".25"/><text x="{x+12}" y="{y+22}" class="small">{digit}</text><text x="{x+w/2}" y="{y+86}" class="value" text-anchor="middle">{html.escape(shown)}</text><text x="{x+12}" y="{y+h-13}" class="small">optim {OPTIMUM[digit]}</text>{shape}</g>')
    title_name = html.escape(name.strip() or "Persoana")
    subtitle = html.escape(f"{born.strftime('%d.%m.%Y')} · N1={n1} · N2={n2} · N3={n3} · N4={n4} · sir {sequence}")
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="850" viewBox="0 0 900 850" role="img" aria-labelledby="title desc"><title id="title">Matrita datei de nastere pentru {title_name}</title><desc id="desc">Matrice numerologica 3 pe 3 cu aparitii, optim si geometrie.</desc><style>.title{{font:700 31px Georgia,serif;fill:#0b2b2c}}.name{{font:700 22px Arial,sans-serif;fill:#0b2b2c}}.sub{{font:14px Arial,sans-serif;fill:#365455}}.value{{font:800 30px Georgia,serif;fill:#0b2b2c}}.small{{font:13px Arial,sans-serif;fill:#284748}}</style><rect width="900" height="850" fill="#f7efe3"/><text x="450" y="68" text-anchor="middle" class="title">Matrita datei de nastere</text><text x="450" y="108" text-anchor="middle" class="name">{title_name}</text><text x="450" y="145" text-anchor="middle" class="sub">{subtitle}</text>{''.join(cells)}<text x="825" y="820" text-anchor="end" class="sub">Atlas Numerologie</text></svg>'''
    return svg, {"n1": n1, "n2": n2, "n3": n3, "n4": n4, "sequence": sequence, "counts": dict(counts)}


def main() -> None:
    parser = argparse.ArgumentParser(description="Genereaza Matrita datei de nastere in SVG.")
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

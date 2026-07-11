#!/usr/bin/env python3
"""Generate Omuletul Relatiilor on the validated Vitruvian reference layout."""
from __future__ import annotations
import argparse
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSITIONS = {0:(318,328),1:(442,180),2:(592,328),3:(700,405),4:(610,498),5:(650,680),6:(450,625),7:(250,680),8:(285,498),9:(151,380)}
LABEL_FONT_WEIGHT = "800"

def digits(value: str) -> list[int]:
    return [int(char) for char in value if char.isdigit()]

def reduce_day(value: str) -> int:
    number = int(value.replace("/", ".").replace("-", ".").split(".")[0])
    while number > 9:
        number = sum(int(char) for char in str(number))
    return number

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name-a", required=True); parser.add_argument("--birth-date-a", required=True)
    parser.add_argument("--name-b", required=True); parser.add_argument("--birth-date-b", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    left, right = Counter(digits(args.birth_date_a)), Counter(digits(args.birth_date_b))
    va, vb = reduce_day(args.birth_date_a), reduce_day(args.birth_date_b)
    together = va + vb
    while together > 9: together = sum(int(char) for char in str(together))

    boxes = []
    for number, (x, y) in POSITIONS.items():
        if not (left[number] or right[number]):
            continue
        a = str(number) * left[number] if left[number] else "-"
        b = str(number) * right[number] if right[number] else "-"
        value = f"{a} / {b}"; width = max(82, len(value) * 14 + 28)
        left_x = x - len(value) * 7 + len(a) * 7
        right_x = x + len(value) * 7 - len(b) * 7
        boxes.append(f'<rect x="{x-width/2:.1f}" y="{y-22:.1f}" width="{width:.1f}" height="44" rx="5" fill="#ffffff" stroke="#d5d5d5" stroke-width="1.5" opacity=".98"/><text x="{left_x:.1f}" y="{y+7:.1f}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="{LABEL_FONT_WEIGHT}" fill="#0070c9">{a}</text><text x="{x:.1f}" y="{y+7:.1f}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="{LABEL_FONT_WEIGHT}" fill="#333333"> / </text><text x="{right_x:.1f}" y="{y+7:.1f}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="{LABEL_FONT_WEIGHT}" fill="#ff00b8">{b}</text>')
    fire = sum(left[n] + right[n] for n in (1,5,9)); water = sum(left[n] + right[n] for n in (2,6)); air = sum(left[n] + right[n] for n in (3,7)); earth = sum(left[n] + right[n] for n in (4,8)); potential = left[0] + right[0]
    header = f'''<style>.value,.soft{{display:none}}</style><g id="generated-overlay"><rect x="0" y="0" width="900" height="116" fill="#f4dcb6" opacity=".96"/><text x="24" y="32" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="800" fill="#0070c9">{args.name_a} - {args.birth_date_a}</text><text x="24" y="58" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="800" fill="#ff00b8">{args.name_b} - {args.birth_date_b}</text><text x="560" y="32" font-family="Arial, Helvetica, sans-serif" font-size="17" font-weight="800" fill="#4f4f4f">Realizare impreuna: {va} + {vb} = {va+vb} -&gt; {together}</text><text x="560" y="58" font-family="Arial, Helvetica, sans-serif" font-size="17" font-weight="800" fill="#4f4f4f">De rezolvat impreuna: |{va} - {vb}| = {abs(va-vb)}</text>{''.join(boxes)}<rect x="0" y="770" width="900" height="70" fill="#f4dcb6" opacity=".96"/><text x="24" y="790" font-family="Arial, Helvetica, sans-serif" font-size="15" font-weight="800" fill="#333333">Sinteza elemente</text><text x="24" y="814" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="700" fill="#555555">Foc: {fire}   Apa: {water}   Aer: {air}   Pamant: {earth}   Potential/0: {potential}</text></g>'''
    svg = (ROOT / "assets" / "reference.svg").read_text(encoding="utf-8")
    svg = svg.replace("</svg>", header + "</svg>")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(svg, encoding="utf-8", newline="\n")
    print(f"Generated: {args.output}")

if __name__ == "__main__": main()

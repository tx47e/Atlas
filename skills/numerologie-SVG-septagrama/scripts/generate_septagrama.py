#!/usr/bin/env python3
"""Generate a Septagrama SVG without consulting external numerology notes."""
from __future__ import annotations
import argparse, re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def parse(value: str) -> tuple[int, int, int]:
    m = re.fullmatch(r"(\d{1,2})[./-](\d{1,2})[./-](\d{4})", value.strip())
    if not m: raise ValueError("Data trebuie sa fie dd.mm.yyyy.")
    d, mo, y = map(int, m.groups())
    if not 1 <= d <= 31 or not 1 <= mo <= 12: raise ValueError("Data nasterii nu este valida.")
    return d, mo, y

def cycle_text(number: int, year: int) -> tuple[str, int]:
    start_age = (number - 1) * 7
    return f"C{number}:{year + start_age} - {year + start_age + 6}", year + start_age + 3

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--name", required=True); p.add_argument("--birth-date", required=True)
    p.add_argument("--output", required=True, type=Path); p.add_argument("--reference-date", default=date.today().isoformat())
    args = p.parse_args(); day, month, birth_year = parse(args.birth_date)
    reference = date.fromisoformat(args.reference_date)
    age = reference.year - birth_year - ((reference.month, reference.day) < (month, day))
    active = min(14, max(1, age // 7 + 1))
    svg = (ROOT / "assets" / "reference.svg").read_text(encoding="utf-8")
    svg = re.sub(r"<title>.*?</title>", f"<title>Septagrama - {args.name} - {day:02d}.{month:02d}.{birth_year}</title>", svg)
    svg = re.sub(r"C(\d+):\d{4} - \d{4}", lambda m: cycle_text(int(m.group(1)), birth_year)[0], svg)
    svg = re.sub(r'(C8:\d{4} - \d{4}) \(\d{2}\.\d{2}\.\d{4}\)', r'\1', svg)
    svg = re.sub(r'(49-56 ani\. 52,5 ani )\d{4}', lambda m: m.group(1) + str(cycle_text(8, birth_year)[1]), svg)
    order = [1,2,9,3,10,4,11,5,12,6,13,7,14]
    years = iter([cycle_text(n, birth_year)[1] for n in order])
    svg = re.sub(r'(<tspan class="bold">)\d{4}(</tspan>)', lambda m: m.group(1) + str(next(years)) + m.group(2), svg)
    svg = svg.replace(' class="green"', '')
    svg = re.sub(r'(<text x="900" y="96")>(C8:)', r'\1 class="bold">\2', svg)
    label = cycle_text(active, birth_year)[0]
    svg = re.sub(r'(<text[^>]*?) class="bold"(>\s*' + re.escape(label) + r'</text>)', r'\1 class="green"\2', svg)
    svg = re.sub(
        r'(class="green">\s*' + re.escape(label) + r'</text>\s*<text)([^>]*>)',
        r'\1 class="green"\2',
        svg,
    )
    c8_crisis = cycle_text(8, birth_year)[1]
    svg = re.sub(
        r'<text x="900" y="126"[^>]*>.*?</text>',
        f'<text x="900" y="126">49-56 ani. <tspan class="orange">52,5 ani</tspan> <tspan class="bold">{c8_crisis}</tspan> (al 53-lea an de viata)</text>',
        svg,
    )
    if active == 5:
        c5_crisis = cycle_text(5, birth_year)[1]
        svg = re.sub(
            r'<text[^>]*x="40"[^>]*y="832"[^>]*>.*?</text>',
            f'<text class="green" x="40" y="832">28-35 ani. 31,5 ani {c5_crisis} (al 32-lea an de viata)</text>',
            svg,
        )
    args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(svg, encoding="utf-8", newline="\n")
    print(f"Generated: {args.output} | active cycle: C{active}")
    return 0
if __name__ == "__main__": raise SystemExit(main())

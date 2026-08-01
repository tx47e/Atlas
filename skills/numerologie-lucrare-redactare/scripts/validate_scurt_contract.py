from __future__ import annotations

import argparse
import re
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Validează contractul vizual și editorial al template-ului scurt.")
    parser.add_argument("--md", type=Path, required=True)
    parser.add_argument("--html", type=Path, required=True)
    parser.add_argument("--spirit-code", type=int)
    parser.add_argument("--spirit-substage", type=int)
    args = parser.parse_args()

    md = args.md.read_text(encoding="utf-8")
    html = args.html.read_text(encoding="utf-8")
    prefixes = set(re.findall(r"^Index: ([A-Z]+-\d{8}-v\d+\.\d+r)-", md, re.M))
    errors: list[str] = []

    if len(prefixes) != 1:
        errors.append(f"Prefixuri de index detectate: {sorted(prefixes)}")
    prefix = next(iter(prefixes), "")
    if prefix and re.search(rf"(?m)^Index: {re.escape(prefix)}-[^\n]+\n(?!\n)", md):
        errors.append("Există un index fără linie goală înaintea elementului indexat")
    if re.search(r"<p>Index:\s*", html):
        errors.append("Un index HTML a fost absorbit într-un paragraf")
    if len(re.findall(r"<div\b", html)) != len(re.findall(r"</div>", html)):
        errors.append("Elementele div nu sunt echilibrate")
    if re.search(r"Ã|Ä|È|�|â€”|â†’", md + html):
        errors.append("Au fost detectate secvențe de mojibake")

    for suffix in ("G-002", "G-002a"):
        pattern = rf"Index: {re.escape(prefix)}-{suffix}</div>\s*<div class=\"matrix-grid matrix-grid-outlined\"[^>]*>.*?<svg"
        if prefix and not re.search(pattern, html, re.S):
            errors.append(f"{suffix} nu folosește matricea grafică Daniel cu geometrii SVG")
    if html.count('<div class="matrix-cell element-') < 18:
        errors.append("G-002 și G-002a nu au câte nouă celule grafice")

    if "Codul Spiritului" in html:
        for needle in (
            'class="table-wrap spirit-code-wrap"><table class="spirit-code-table"',
            '<table class="spirit-zones-table"',
            '<table class="stage-table"',
        ):
            if needle not in html:
                errors.append(f"Lipsește componenta Spirit: {needle}")
        current_rows = re.findall(r'<tr class="[^"]*\bcurrent-row\b[^"]*">(.*?)</tr>', html, re.S)
        if len(current_rows) != 1:
            errors.append(f"T-019 trebuie să aibă exact un current-row, nu {len(current_rows)}")
        if args.spirit_substage is not None and current_rows:
            first_cell = re.search(r"<td[^>]*>(\d+)</td>", current_rows[0])
            actual = int(first_cell.group(1)) if first_cell else None
            if actual != args.spirit_substage:
                errors.append(f"T-019 evidențiază subetapa {actual}, nu {args.spirit_substage}")
        if args.spirit_code is not None and f'<span class="spirit-cell-highlight">{args.spirit_code}</span>' not in html:
            errors.append(f"T-017 nu evidențiază Codul Spiritului {args.spirit_code}")

    if errors:
        print("SHORT_CONTRACT=FAILED")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print("SHORT_CONTRACT=OK")


if __name__ == "__main__":
    main()

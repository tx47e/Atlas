from __future__ import annotations

import argparse
import html as html_std
import re
from pathlib import Path


def clean_cell(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = html_std.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Validează contractul vizual și editorial al template-ului scurt.")
    parser.add_argument("--md", type=Path, required=True)
    parser.add_argument("--html", type=Path, required=True)
    parser.add_argument("--spirit-code", type=int)
    parser.add_argument("--spirit-substage", type=int)
    parser.add_argument("--life-lessons-product", type=int)
    parser.add_argument("--birth-year", type=int)
    parser.add_argument("--current-year", type=int)
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
    if re.search(r"(?:apar|apare)\s+(?:numai|doar)\s+în\s+matricea\s+numelui", md + html, re.I):
        errors.append("Sunt interpretate cifre prezente exclusiv în Matricea numelui")

    forbidden_tarot_patterns = (
        (r"1\.7\. Tarot", "1.7. Tarot"),
        (rf"{re.escape(prefix)}-SUB-007(?![A-Za-z0-9])", "SUB-007"),
        (rf"{re.escape(prefix)}-P-010a(?![A-Za-z0-9])", "P-010a"),
        (rf"{re.escape(prefix)}-P-010b(?![A-Za-z0-9])", "P-010b"),
        (rf"{re.escape(prefix)}-T-010(?![A-Za-z0-9])", "T-010"),
    )
    for pattern, label in forbidden_tarot_patterns:
        if prefix and re.search(pattern, md + html):
            errors.append(f"Template-ul scurt conține vechiul bloc Tarot interzis: {label}")

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
        elif len(re.findall(r'class="current-substage"', current_rows[0])) != 3:
            errors.append("T-019 trebuie să marcheze exact cele trei celule de la Subetapă încolo")
        elif re.search(r'<td[^>]*rowspan="[^"]+"[^>]*class="current-substage"', current_rows[0]):
            errors.append("T-019 marchează greșit o celulă a etapei principale")
        stage_header = "<th>Etapă</th><th>Descriere etapă</th><th>Subetapă</th><th>Lecție</th><th>Descriere subetapă</th>"
        if stage_header not in html:
            errors.append("T-019 nu păstrează cele 5 coloane validate din BDR-19980219-v1.00r-T-019")
        if '<td rowspan="4">1</td><td rowspan="4">Înțelegere și stabilizare</td>' not in html:
            errors.append("T-019 nu păstrează structura cu rowspan pentru etapa 1")
        if args.spirit_substage is not None and current_rows:
            first_cell = re.search(r"<td[^>]*>(\d+)</td>", current_rows[0])
            actual = int(first_cell.group(1)) if first_cell else None
            if actual != args.spirit_substage:
                errors.append(f"T-019 evidențiază subetapa {actual}, nu {args.spirit_substage}")
        if args.spirit_code is not None and f'<span class="spirit-cell-highlight">{args.spirit_code}</span>' not in html:
            errors.append(f"T-017 nu evidențiază Codul Spiritului {args.spirit_code} exact ca modelul Daniel")

        t017 = re.search(
            rf"Index: {re.escape(prefix)}-T-017</div>\s*<div class=\"table-wrap spirit-code-wrap\"><table class=\"spirit-code-table\"[^>]*>(.*?)</table>",
            html,
            re.S,
        )
        if not t017:
            errors.append("T-017 nu a fost găsit ca tabel HTML valid")
        else:
            table_html = t017.group(1)
            highlights = re.findall(r'<span class="([^"]*\bspirit-cell-highlight\b[^"]*)">(\d+)</span>', table_html)
            if len(highlights) != 1:
                errors.append(f"T-017 trebuie să aibă exact un marcaj personal, nu {len(highlights)}")
            elif highlights[0][0] != "spirit-cell-highlight":
                errors.append("Marcajul personal din T-017 combină spirit-cell-highlight cu o clasă de zonă")

            for zone_class in ("spirit-zone-love", "spirit-zone-reason", "spirit-zone-material", "spirit-zone-gifts"):
                if zone_class not in table_html:
                    errors.append(f"T-017 nu colorează zona {zone_class}")
            if '<span class="spirit-zone-love">0</span>' not in table_html:
                errors.append("T-017 nu colorează codul 0 în albastrul zonei Iubire")

            month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            rows = [row for row in re.findall(r"<tr[^>]*>(.*?)</tr>", table_html, re.S) if "<td" in row]
            if len(rows) != 31:
                errors.append(f"T-017 trebuie să aibă 31 de rânduri pentru zile, nu {len(rows)}")
            else:
                for day, row in enumerate(rows, start=1):
                    cells = re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)
                    if len(cells) != 13:
                        errors.append(f"T-017 are {len(cells)} celule pe rândul zilei {day}, nu 13")
                        continue
                    for month, max_day in enumerate(month_lengths, start=1):
                        value = clean_cell(cells[month])
                        if day > max_day and value:
                            errors.append(f"T-017 completează data inexistentă {day:02d}.{month:02d}")
                        elif day <= max_day and not value:
                            errors.append(f"T-017 lasă goală data validă {day:02d}.{month:02d}")

    if prefix and "T-015" in html:
        t015 = re.search(
            rf"Index: {re.escape(prefix)}-T-015</div>\s*(?:<!--.*?-->\s*)*<div class=\"table-wrap\"><table[^>]*>(.*?)</table>",
            html,
            re.S,
        )
        if not t015:
            errors.append("T-015 nu a fost gasit ca tabel HTML valid")
        else:
            row_matches = re.findall(r"<tr([^>]*)>(.*?)</tr>", t015.group(1), re.S)
            body_rows = [(attrs, row) for attrs, row in row_matches if "<td" in row]
            readings: list[str] = []
            for _, row in body_rows:
                cells = re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)
                if len(cells) >= 4:
                    readings.append(clean_cell(cells[-1]))
            repeated = sorted({item for item in readings if item and readings.count(item) > 1})
            if repeated:
                errors.append("T-015 repeta aceeasi citire pentru cicluri diferite")
            active_count = sum(1 for attrs, _ in body_rows if "active-cycle" in attrs)
            if active_count != 1:
                errors.append(f"T-015 trebuie sa aiba exact un rand active-cycle, nu {active_count}")

    if prefix and args.life_lessons_product is not None:
        expected_lessons = [int(digit) for digit in str(args.life_lessons_product)]
        t008 = re.search(
            rf"Index: {re.escape(prefix)}-T-008</div>\s*(?:<!--.*?-->\s*)*<div class=\"table-wrap\"><table[^>]*>(.*?)</table>",
            html,
            re.S,
        )
        if not t008:
            errors.append("T-008 nu a fost gasit ca tabel HTML valid")
        else:
            headers = [clean_cell(cell) for cell in re.findall(r"<th[^>]*>(.*?)</th>", t008.group(1), re.S)]
            actual_lessons: list[int] = []
            for header in headers[1:]:
                match = re.search(r"Lecția\s+\d+\s+[—-]\s+(\d)$", header)
                if match:
                    actual_lessons.append(int(match.group(1)))
            if actual_lessons != expected_lessons:
                errors.append(f"T-008 are sirul {actual_lessons}, nu cifrele complete ale produsului {expected_lessons}")

            body_rows = re.findall(r"<tr[^>]*>(.*?)</tr>", t008.group(1), re.S)
            body_rows = [row for row in body_rows if "<td" in row]
            expected_cells = len(expected_lessons) + 1
            for row in body_rows:
                if len(re.findall(r"<td[^>]*>", row)) != expected_cells:
                    errors.append("T-008 nu distribuie fiecare grup de ani pe toate pozitiile sirului")
                    break

            if args.birth_year is not None and args.current_year is not None and body_rows:
                life_year = args.current_year - args.birth_year + 1
                expected_column = (life_year - 1) % len(expected_lessons) + 1
                current_position = None
                for row in body_rows:
                    cells = re.findall(r"<td[^>]*>(.*?)</td>", row, re.S)
                    for index, cell in enumerate(cells[1:], start=1):
                        if re.search(rf">?{args.current_year}<?", cell):
                            current_position = index
                            break
                    if current_position is not None:
                        break
                if current_position != expected_column:
                    errors.append(
                        f"T-008 plaseaza anul {args.current_year} pe coloana {current_position}, nu pe coloana {expected_column}"
                    )

    if errors:
        print("SHORT_CONTRACT=FAILED")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print("SHORT_CONTRACT=OK")


if __name__ == "__main__":
    main()

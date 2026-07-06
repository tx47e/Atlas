import html
import pathlib
import re

MD_PATH = pathlib.Path(
    r"output\lucrari\1998-02-19-BIRSAN-DANIEL-ROBERT\1998-02-19-BIRSAN-DANIEL-ROBERT-v1r.md"
)
HTML_PATH = pathlib.Path(
    r"output\lucrari\1998-02-19-BIRSAN-DANIEL-ROBERT\1998-02-19-BIRSAN-DANIEL-ROBERT-v1r.html"
)


def slug(text: str) -> str:
    replacements = str.maketrans(
        {
            "ă": "a",
            "â": "a",
            "î": "i",
            "ș": "s",
            "ş": "s",
            "ț": "t",
            "ţ": "t",
            "Ă": "a",
            "Â": "a",
            "Î": "i",
            "Ș": "s",
            "Ş": "s",
            "Ț": "t",
            "Ţ": "t",
        }
    )
    text = text.translate(replacements).lower()
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def md_inline(text: str) -> str:
    text = html.escape(text, quote=False)
    return re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def convert_table(lines: list[str]) -> str:
    header = split_table_row(lines[0])
    body = [split_table_row(line) for line in lines[2:]]
    head_html = "".join(f"<th>{md_inline(cell)}</th>" for cell in header)
    rows = []
    for row in body:
        rows.append("<tr>" + "".join(f"<td>{md_inline(cell)}</td>" for cell in row) + "</tr>")
    return (
        '<div class="table-wrap"><table><thead><tr>'
        + head_html
        + "</tr></thead><tbody>\n"
        + "\n".join(rows)
        + "\n</tbody></table></div>"
    )


def convert_section(md: str) -> str:
    lines = md.strip().splitlines()
    out: list[str] = []
    paragraph: list[str] = []
    i = 0

    def flush_paragraph() -> None:
        if not paragraph:
            return
        text = " ".join(part.strip() for part in paragraph).strip()
        paragraph.clear()
        calc_prefix = "<strong>Calcul:</strong> "
        if text.startswith(calc_prefix):
            out.append(f'<div class="calc-box">{text[len(calc_prefix):]}</div>')
        else:
            out.append(f"<p>{text}</p>")

    while i < len(lines):
        line = lines[i].rstrip()
        if not line:
            flush_paragraph()
            i += 1
            continue
        if line.startswith("| "):
            flush_paragraph()
            table_lines = []
            while i < len(lines) and lines[i].startswith("| "):
                table_lines.append(lines[i])
                i += 1
            out.append(convert_table(table_lines))
            continue
        if line.startswith("## "):
            flush_paragraph()
            title = line[3:].strip()
            out.append(f'<h2 id="{slug(title)}">{html.escape(title)}</h2>')
        elif line.startswith("### "):
            flush_paragraph()
            title = line[4:].strip()
            out.append(f'<h3 id="{slug(title)}">{html.escape(title)}</h3>')
        else:
            paragraph.append(md_inline(line))
        i += 1

    flush_paragraph()
    return "\n\n".join(out) + "\n"


md = MD_PATH.read_text(encoding="utf-8")
section_match = re.search(
    r"## Capitolul 2\. Caracterul\n.*?(?=## Capitolul 6\. Ajutoare\n)",
    md,
    flags=re.S,
)
if not section_match:
    raise SystemExit("Could not locate MD chapters 2-5")

replacement = convert_section(section_match.group(0))

page = HTML_PATH.read_text(encoding="utf-8")
page = re.sub(r'\s*<div class="index(?: index-heading)?">Index: [^<]+</div>\s*', "\n", page)

html_pattern = re.compile(
    r'<h2 id="capitolul-2-caracterul">.*?(?=<h2 id="capitolul-6-ajutoare">)',
    flags=re.S,
)
if not html_pattern.search(page):
    raise SystemExit("Could not locate HTML chapters 2-5")

page = html_pattern.sub(replacement, page, count=1)
HTML_PATH.write_text(page, encoding="utf-8")
print("synced chapters 2-5")

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
    replacements = {
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
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def md_inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
    return text


def convert_section(md: str) -> str:
    lines = md.strip().splitlines()
    out: list[str] = []
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        if not paragraph:
            return
        text = " ".join(part.strip() for part in paragraph).strip()
        paragraph.clear()
        calc_prefix = "<strong>Calcul:</strong> "
        if text.startswith(calc_prefix):
            calc = text[len(calc_prefix) :]
            out.append(f'<div class="calc-box">{calc}</div>')
        else:
            out.append(f"<p>{text}</p>")

    for raw in lines:
        line = raw.rstrip()
        if not line:
            flush_paragraph()
            continue
        if line.startswith("### "):
            flush_paragraph()
            title = line[4:].strip()
            out.append(f'<h3 id="{slug(title)}">{html.escape(title)}</h3>')
        elif line.startswith("#### "):
            flush_paragraph()
            title = line[5:].strip()
            out.append(f'<h4 id="{slug(title)}">{html.escape(title)}</h4>')
        else:
            paragraph.append(md_inline(line))

    flush_paragraph()
    return "\n\n".join(out) + "\n"


md = MD_PATH.read_text(encoding="utf-8")
section_match = re.search(
    r"### 1\.2\. Calea destinului, destinul si puntile\n.*?(?=### 1\.4\. Structura matriciala\n)",
    md,
    flags=re.S,
)
if not section_match:
    raise SystemExit("Could not locate MD section 1.2 through 1.3")

replacement = convert_section(section_match.group(0))

page = HTML_PATH.read_text(encoding="utf-8")
page = re.sub(r'\s*<div class="index(?: index-heading)?">Index: [^<]+</div>\s*', "\n", page)

html_pattern = re.compile(
    r'<h3 id="1-2-calea-destinului-destinul-si-puntile">.*?(?=<h3 id="1-4-structura-matriciala">)',
    flags=re.S,
)
if not html_pattern.search(page):
    raise SystemExit("Could not locate HTML section 1.2 through 1.3")

page = html_pattern.sub(replacement, page, count=1)
HTML_PATH.write_text(page, encoding="utf-8")
print("synced sections 1.2 and 1.3")

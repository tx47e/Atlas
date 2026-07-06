import pathlib
import re

HTML_PATH = pathlib.Path(
    r"output\lucrari\1998-02-19-BIRSAN-DANIEL-ROBERT\1998-02-19-BIRSAN-DANIEL-ROBERT-v1r.html"
)
PREFIX = "BDR-19980219-v1r"


def next_index(counters: dict[str, int], kind: str) -> str:
    counters[kind] = counters.get(kind, 0) + 1
    return f"{PREFIX}-{kind}-{counters[kind]:03d}"


def add_style(html: str) -> str:
    html = re.sub(
        r"\n\.index \{\n  color: var\(--gold\);\n  font-size: 12px;\n  font-weight: 700;\n  margin-top: 18px;\n\}\n",
        "\n",
        html,
    )
    if ".index-heading + h1" in html and ".index {" in html:
        return html
    css = """
.index {
  color: var(--gold);
  font-size: 12px;
  font-weight: 700;
  line-height: 1.2;
  margin: 14px 0 6px;
}
.index-heading {
  display: block;
  margin: 30px 0 8px;
}
.index-heading + h1,
.index-heading + h2,
.index-heading + h3,
.index-heading + h4 {
  margin-top: 0;
}
"""
    return html.replace(".topbar span { color: #f7ead8; font-size: 14px; }\n", ".topbar span { color: #f7ead8; font-size: 14px; }\n" + css, 1)


def strip_existing_indexes(content: str) -> str:
    content = re.sub(r'\s*<div class="index(?: index-heading)?">Index: [^<]+</div>\s*', "\n", content)
    content = re.sub(
        r'<h([1-4])([^>]*)><span class="heading-index">Index: [^<]+</span><span>(.*?)</span></h\1>',
        r"<h\1\2>\3</h\1>",
        content,
        flags=re.S,
    )
    return content


def index_headings(content: str, counters: dict[str, int]) -> str:
    def repl(match: re.Match[str]) -> str:
        level, attrs, inner = match.group(1), match.group(2), match.group(3).strip()
        kind = "CAP" if level in {"1", "2"} else "SUB"
        idx = next_index(counters, kind)
        return f'<div class="index index-heading">Index: {idx}</div>\n<h{level}{attrs}>{inner}</h{level}>'

    return re.sub(r"<h([1-4])([^>]*)>(.*?)</h\1>", repl, content, flags=re.S)


def index_blocks(content: str, counters: dict[str, int]) -> str:
    indexed_lines: list[str] = []
    for line in content.splitlines():
        stripped = line.lstrip()
        kind = None
        if stripped.startswith("<p"):
            kind = "P"
        elif stripped.startswith("<ul"):
            kind = "L"
        elif stripped.startswith('<div class="note"'):
            kind = "P"
        elif stripped.startswith('<div class="table-wrap"') or stripped.startswith('<div class="matrix-grid"'):
            kind = "T"
        elif stripped.startswith('<div class="calc-box"') or stripped.startswith("<pre") or stripped.startswith("<figure"):
            kind = "C"

        if kind:
            idx = next_index(counters, kind)
            indexed_lines.append(f'<div class="index">Index: {idx}</div>')
        indexed_lines.append(line)
    return "\n".join(indexed_lines)


html = HTML_PATH.read_text(encoding="utf-8")
html = add_style(html)

nav_end = html.find("</nav>")
main_end = html.rfind("</main>")
if nav_end == -1 or main_end == -1 or nav_end > main_end:
    raise SystemExit("Could not locate main content after nav")

before = html[: nav_end + len("</nav>")]
content = html[nav_end + len("</nav>") : main_end]
after = html[main_end:]

content = strip_existing_indexes(content)
counters: dict[str, int] = {}
content = index_headings(content, counters)
content = index_blocks(content, counters)

HTML_PATH.write_text(before + content + after, encoding="utf-8")
print(counters)


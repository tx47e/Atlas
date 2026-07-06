import html
import pathlib
import re

base = pathlib.Path(r"output\lucrari\1998-02-19-BIRSAN-DANIEL-ROBERT")
md_path = base / "1998-02-19-BIRSAN-DANIEL-ROBERT-v1r.md"
html_path = base / "1998-02-19-BIRSAN-DANIEL-ROBERT-v1r.html"

md_text = md_path.read_text(encoding="utf-8")
section = re.search(
    r"### 1\.1\. Vibratiile fundamentale\n(?P<body>.*?)\n### 1\.2\. Calea destinului, destinul si puntile",
    md_text,
    re.S,
).group("body")

out = ['<h3 id="1-1-vibratiile-fundamentale">1.1. Vibratiile fundamentale</h3>']
paragraph: list[str] = []


def flush_paragraph() -> None:
    if paragraph:
        out.append("<p>" + html.escape(" ".join(paragraph), quote=False) + "</p>")
        paragraph.clear()


for line in section.strip().splitlines():
    stripped = line.strip()
    if not stripped:
        flush_paragraph()
        continue
    if stripped.startswith("#### "):
        flush_paragraph()
        title = stripped[5:]
        slug = title.lower().replace(" - ", "-").replace(" ", "-")
        out.append(f'<h4 id="{html.escape(slug)}">{html.escape(title, quote=False)}</h4>')
    elif stripped.startswith('<div class="calc-box">'):
        flush_paragraph()
        out.append(stripped)
    else:
        paragraph.append(stripped)

flush_paragraph()
new_section = "\n".join(out)

html_text = html_path.read_text(encoding="utf-8")
html_text = re.sub(
    r'(?s)<h3 id="1-1-vibratiile-fundamentale">.*?(?=<h3 id="1-2-calea-destinului-destinul-si-puntile">)',
    new_section + "\n",
    html_text,
    count=1,
)
html_path.write_text(html_text, encoding="utf-8")
print("updated html section", len(new_section))


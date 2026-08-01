from __future__ import annotations

import re
from pathlib import Path

import render_andreea_short_html as renderer


ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "output/lucrari/1998-02-19-BIRSAN-DANIEL-ROBERT"
MD_PATH = DIR / "1998-02-19-BIRSAN-DANIEL-ROBERT-scurt-v1.00r.md"
HTML_PATH = DIR / "1998-02-19-BIRSAN-DANIEL-ROBERT-scurt-v1.00r.html"
PREFIX = "BDR-19980219-v1.00r"


def main() -> None:
    model = HTML_PATH.read_text(encoding="utf-8")
    style = re.search(r"<style>(.*?)</style>", model, re.S)
    if not style:
        raise RuntimeError("CSS-ul lucrării Daniel nu a fost găsit")

    renderer.DIR = DIR
    source = MD_PATH.read_text(encoding="utf-8")
    source = re.sub(r"\A---\n.*?\n---\n", "", source, count=1, flags=re.S)
    source = re.sub(rf"(?m)^(Index: {re.escape(PREFIX)}-[^\n]+)\n(?!\n)", r"\1\n\n", source)
    source = renderer.embed_markdown_images(source)
    body = renderer.add_heading_ids(renderer.render_markdown(source))
    body = re.sub(r'<p>Index: ([^<]+)</p>', r'<div class="idx">Index: \1</div>', body)
    body = renderer.convert_callouts(body)
    body = renderer.build_toc(body)
    body = re.sub(
        r'(?<!<div class="table-wrap">)(<table\b.*?</table>)',
        r'<div class="table-wrap">\1</div>',
        body,
        flags=re.S,
    )
    body = renderer.apply_daniel_component_classes(body, PREFIX)
    body = renderer.wrap_tarot_figures(body)
    body = renderer.embed_sources(body)

    css = style.group(1) + "\nblockquote{padding:14px 18px;margin:16px 0;background:linear-gradient(100deg,rgba(239,224,189,.72),rgba(255,248,232,.84));border:1px solid var(--line);border-left:5px solid var(--gold);border-radius:0 5px 5px 0} figure{margin:18px 0} figcaption{text-align:center;color:var(--muted);font-style:italic}"
    document = f'''<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Bîrsan Daniel Robert — 19.02.1998</title>
<style>{css}</style>
</head>
<body>
<header><div class="title">Bîrsan Daniel Robert · lucrare numerologică scurtă</div><div class="meta">Revizie V1.00R · 18.07.2026 · The Scribe</div></header>
<main>{body}</main>
</body>
</html>
'''
    HTML_PATH.write_text(document, encoding="utf-8", newline="\n")
    print(HTML_PATH)


if __name__ == "__main__":
    main()

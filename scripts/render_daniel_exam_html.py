from __future__ import annotations

import re
from pathlib import Path

import render_andreea_short_html as renderer


ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "output/lucrari/1998-02-19-BIRSAN-DANIEL-ROBERT"
MD_PATH = DIR / "1998-02-19-BIRSAN-DANIEL-ROBERT-v1.07r.md"
HTML_PATH = DIR / "1998-02-19-BIRSAN-DANIEL-ROBERT-v1.07r.html"
PREFIX = "BDR-19980219-v1.07r"


MATRIX_GRID = '''<div class="matrix-grid">
<div class="matrix-cell element-foc"><div class="matrix-number">1</div><div class="matrix-main">1111</div><div class="matrix-opt">optim 111</div><div class="matrix-geom" aria-label="pătrat"><svg viewBox="0 0 40 32" role="img"><rect x="8" y="4" width="24" height="24"/></svg></div></div>
<div class="matrix-cell element-pamant"><div class="matrix-number">4</div><div class="matrix-main">-</div><div class="matrix-opt">optim 44</div><div class="matrix-geom matrix-geom-empty" aria-hidden="true"></div></div>
<div class="matrix-cell element-aer"><div class="matrix-number">7</div><div class="matrix-main">7</div><div class="matrix-opt">optim 7</div><div class="matrix-geom" aria-label="cerc"><svg viewBox="0 0 40 32" role="img"><circle cx="20" cy="16" r="6"/></svg></div></div>
<div class="matrix-cell element-apa"><div class="matrix-number">2</div><div class="matrix-main">22</div><div class="matrix-opt">optim 222</div><div class="matrix-geom" aria-label="două cercuri legate"><svg viewBox="0 0 40 32" role="img"><line x1="17.1" y1="16" x2="22.9" y2="16" style="stroke-linecap:butt"/><circle cx="10" cy="16" r="6"/><circle cx="30" cy="16" r="6"/></svg></div></div>
<div class="matrix-cell element-foc"><div class="matrix-number">5</div><div class="matrix-main">-</div><div class="matrix-opt">optim 55</div><div class="matrix-geom matrix-geom-empty" aria-hidden="true"></div></div>
<div class="matrix-cell element-pamant"><div class="matrix-number">8</div><div class="matrix-main">8</div><div class="matrix-opt">optim 8</div><div class="matrix-geom" aria-label="cerc"><svg viewBox="0 0 40 32" role="img"><circle cx="20" cy="16" r="6"/></svg></div></div>
<div class="matrix-cell element-aer"><div class="matrix-number">3</div><div class="matrix-main">33</div><div class="matrix-opt">optim 333</div><div class="matrix-geom" aria-label="două cercuri legate"><svg viewBox="0 0 40 32" role="img"><line x1="17.1" y1="16" x2="22.9" y2="16" style="stroke-linecap:butt"/><circle cx="10" cy="16" r="6"/><circle cx="30" cy="16" r="6"/></svg></div></div>
<div class="matrix-cell element-apa"><div class="matrix-number">6</div><div class="matrix-main">-</div><div class="matrix-opt">optim 66</div><div class="matrix-geom matrix-geom-empty" aria-hidden="true"></div></div>
<div class="matrix-cell element-foc"><div class="matrix-number">9</div><div class="matrix-main">9999</div><div class="matrix-opt">optim 9</div><div class="matrix-geom" aria-label="pătrat"><svg viewBox="0 0 40 32" role="img"><rect x="8" y="4" width="24" height="24"/></svg></div></div>
</div>'''


def build_toc(body: str) -> str:
    chapters = re.findall(r'<h2 id="([^"]+)">(Capitolul [^<]+)</h2>', body)
    items = "".join(f'<li><a href="#{target}">{label}</a></li>' for target, label in chapters)
    heading = re.search(r'<h2 id="cuprins">.*?</h2>', body, flags=re.S)
    if not heading:
        raise RuntimeError("Cuprinsul nu a fost găsit")
    next_chapter = body.find(f'<div class="index">Index: {PREFIX}-CAP-003a</div>', heading.end())
    if next_chapter < 0:
        raise RuntimeError("Sfârșitul Cuprinsului nu a fost găsit")
    toc_index = f'<div class="index">Index: {PREFIX}-L-004</div>'
    return body[:heading.end()] + f"\n{toc_index}\n<ol>{items}</ol>\n" + body[next_chapter:]


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
    body = re.sub(r'<p>Index: ([^<]+)</p>', r'<div class="index">Index: \1</div>', body)
    body = re.sub(
        rf'(<div class="index">Index: {re.escape(PREFIX)}-G-001</div>)\s*<pre><code class="language-text">.*?</code></pre>',
        rf'\1\n{MATRIX_GRID}',
        body,
        count=1,
        flags=re.S,
    )
    body = renderer.convert_callouts(body)
    body = build_toc(body)
    body = re.sub(
        r'(?<!<div class="table-wrap">)(<table\b.*?</table>)',
        r'<div class="table-wrap">\1</div>',
        body,
        flags=re.S,
    )
    body = renderer.wrap_tarot_figures(body)
    body = renderer.embed_sources(body)
    body = re.sub(
        r'<p>(<img\b[^>]+alt="([^"]+)"[^>]*>)</p>',
        r'<figure>\1<figcaption>\2</figcaption></figure>',
        body,
    )

    css = style.group(1)
    document = f'''<!doctype html>
<html lang="ro">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Lucrare numerologică - Bîrsan Daniel Robert - V1.07R</title>
  <style>{css}</style>
</head>
<body>
  <header class="topbar"><strong>Bîrsan Daniel Robert</strong><span>Lucrare numerologică · Revizie V1.07R · 19.02.1998</span></header>
  <main>{body}</main>
</body>
</html>
'''
    HTML_PATH.write_text(document, encoding="utf-8", newline="\n")
    print(HTML_PATH)


if __name__ == "__main__":
    main()

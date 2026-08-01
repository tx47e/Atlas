from __future__ import annotations

import base64
import html
import mimetypes
import re
import subprocess
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "output/lucrari/1998-01-12-ROMAN-ANDREEA-MARIA"
MD_PATH = DIR / "1998-01-12-ROMAN-ANDREEA-MARIA-scurt-v1.00r.md"
HTML_PATH = DIR / "1998-01-12-ROMAN-ANDREEA-MARIA-scurt-v1.00r.html"
MODEL_HTML = ROOT / "output/lucrari/1998-02-19-BIRSAN-DANIEL-ROBERT/1998-02-19-BIRSAN-DANIEL-ROBERT-scurt-v1.00r.html"
NODE = Path(r"C:\Users\Mihai\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe")
MARKED = Path(r"C:\Users\Mihai\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\node_modules\marked")


def embed_markdown_images(text: str) -> str:
    pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
    return pattern.sub(lambda m: f'<img src="{html.escape(m.group(2), quote=True)}" alt="{html.escape(m.group(1), quote=True)}">', text)


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode('ascii')}"


def embed_sources(body: str) -> str:
    def repl(match: re.Match[str]) -> str:
        src = html.unescape(match.group(1))
        if src.startswith("data:"):
            return match.group(0)
        path = DIR / src
        if not path.is_file():
            raise FileNotFoundError(f"Imagine lipsă: {path}")
        return f'src="{data_uri(path)}" data-source="{html.escape(src, quote=True)}"'
    return re.sub(r'src="([^"]+)"', repl, body)


def build_toc(body: str) -> str:
    chapters = re.findall(r'<h2 id="([^"]+)">(Capitolul [^<]+)</h2>', body)
    items = "".join(f'<li><a href="#{target}">{label}</a></li>' for target, label in chapters)
    anchor = body.find('<h2 id="cuprins">')
    if anchor < 0:
        raise RuntimeError("Cuprinsul nu a fost găsit")
    start = body.find("<ol>", anchor)
    end = body.find("</ol>", start)
    if start < 0 or end < 0:
        raise RuntimeError("Lista Cuprinsului nu a fost găsită")
    return body[:start] + f"<ol>{items}</ol>" + body[end + 5:]


def add_heading_ids(body: str) -> str:
    used: dict[str, int] = {}
    def repl(match: re.Match[str]) -> str:
        level, label = match.group(1), match.group(2)
        plain = re.sub(r"<[^>]+>", "", label)
        slug = unicodedata.normalize("NFKD", plain).encode("ascii", "ignore").decode("ascii").lower()
        slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-") or "sectiune"
        used[slug] = used.get(slug, 0) + 1
        target = slug if used[slug] == 1 else f"{slug}-{used[slug]}"
        return f'<h{level} id="{target}">{label}</h{level}>'
    return re.sub(r"<h([1-4])>(.*?)</h\1>", repl, body, flags=re.S)


def render_markdown(source: str) -> str:
    script = "const fs=require('fs');const {marked}=require(process.argv[1]);const s=fs.readFileSync(0,'utf8');process.stdout.write(marked.parse(s,{gfm:true,breaks:false}));"
    result = subprocess.run(
        [str(NODE), "-e", script, str(MARKED)],
        input=source,
        text=True,
        capture_output=True,
        check=True,
        encoding="utf-8",
    )
    return result.stdout


def convert_callouts(body: str) -> str:
    def repl(match: re.Match[str]) -> str:
        inner = match.group(1)
        inner = re.sub(
            r"<p>\[!example\]\s*([^\n<]+)\n",
            r"<p><strong>\1</strong><br>",
            inner,
            count=1,
        )
        return f'<aside class="callout example">{inner}</aside>'
    return re.sub(r"<blockquote>(.*?)</blockquote>", repl, body, flags=re.S)


def apply_daniel_component_classes(body: str, prefix: str = "RAM-19980112-v1.00r") -> str:
    escaped_prefix = re.escape(prefix)
    body = re.sub(
        rf'(<div class="idx">Index: {escaped_prefix}-T-017</div>\s*)<div class="table-wrap"><table>',
        r'\1<div class="table-wrap spirit-code-wrap"><table class="spirit-code-table">',
        body,
        count=1,
    )
    body = re.sub(
        rf'(<div class="idx">Index: {escaped_prefix}-T-018</div>\s*)<div class="table-wrap"><table>',
        r'\1<div class="table-wrap"><table class="spirit-zones-table">',
        body,
        count=1,
    )
    for css, label in (("love", "Iubire"), ("reason", "Rațiune"), ("material", "Material"), ("gifts", "Haruri")):
        body = body.replace(
            f'<td><span class="zone-badge zone-{css}">{label}</span></td>',
            f'<td class="zone-cell zone-{css}"><span class="zone-badge">{label}</span></td>',
            1,
        )
    return body


def wrap_tarot_figures(body: str) -> str:
    return re.sub(
        r'<p>(<img\b[^>]+>)</p>\s*<p><em>(.*?)</em></p>',
        r'<figure>\1<figcaption>\2</figcaption></figure>',
        body,
        flags=re.S,
    )


def main() -> None:
    model = MODEL_HTML.read_text(encoding="utf-8")
    style = re.search(r"<style>(.*?)</style>", model, re.S)
    if not style:
        raise RuntimeError("CSS-ul modelului Daniel nu a fost găsit")

    source = MD_PATH.read_text(encoding="utf-8")
    source = re.sub(r"\A---\n.*?\n---\n", "", source, count=1, flags=re.S)
    source = re.sub(r"(?m)^(Index: RAM-19980112-v1\.00r-[^\n]+)\n(?!\n)", r"\1\n\n", source)
    source = embed_markdown_images(source)
    body = add_heading_ids(render_markdown(source))
    body = re.sub(r'<p>Index: ([^<]+)</p>', r'<div class="idx">Index: \1</div>', body)
    body = convert_callouts(body)
    body = build_toc(body)
    body = re.sub(r'(?<!<div class="table-wrap">)(<table\b.*?</table>)', r'<div class="table-wrap">\1</div>', body, flags=re.S)
    body = apply_daniel_component_classes(body)
    body = wrap_tarot_figures(body)
    body = embed_sources(body)

    css = style.group(1) + "\nblockquote{padding:14px 18px;margin:16px 0;background:linear-gradient(100deg,rgba(239,224,189,.72),rgba(255,248,232,.84));border:1px solid var(--line);border-left:5px solid var(--gold);border-radius:0 5px 5px 0} figure{margin:18px 0} figcaption{text-align:center;color:var(--muted);font-style:italic}"
    document = f'''<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Roman Andreea Maria — 12.01.1998</title>
<style>{css}</style>
</head>
<body>
<header><div class="title">Roman Andreea Maria · lucrare numerologică scurtă</div><div class="meta">Revizie V1.00R · 31.07.2026 · The Scribe</div></header>
<main>{body}</main>
</body>
</html>
'''
    HTML_PATH.write_text(document, encoding="utf-8", newline="\n")
    print(HTML_PATH)


if __name__ == "__main__":
    main()

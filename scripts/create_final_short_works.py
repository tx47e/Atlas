from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FINAL_WORK_DATE = "02.08.2026"
FINAL_PAPER_CSS = r"""
/* final-paper-texture: patina organica, fara pattern liniar repetitiv */
body {
  background-image:
    radial-gradient(ellipse at 16% 10%, rgba(35, 137, 143, .24), transparent 31%),
    radial-gradient(ellipse at 82% 78%, rgba(4, 43, 49, .52), transparent 42%),
    radial-gradient(ellipse at 55% 28%, rgba(255, 255, 255, .035), transparent 36%);
}
main {
  background-color: #f6ead0;
  background-image:
    radial-gradient(ellipse at 7% 6%, rgba(122, 78, 24, .105), transparent 24%),
    radial-gradient(ellipse at 94% 11%, rgba(151, 104, 34, .085), transparent 22%),
    radial-gradient(ellipse at 12% 86%, rgba(111, 73, 27, .075), transparent 28%),
    radial-gradient(ellipse at 91% 93%, rgba(139, 92, 28, .095), transparent 25%),
    radial-gradient(ellipse at 46% 31%, rgba(255, 252, 235, .34), transparent 35%),
    radial-gradient(ellipse at 62% 69%, rgba(121, 83, 34, .045), transparent 29%),
    linear-gradient(117deg, rgba(255, 250, 231, .24), rgba(188, 144, 72, .045) 48%, rgba(255, 248, 224, .18));
  box-shadow:
    inset 0 0 92px rgba(103, 67, 22, .12),
    inset 0 0 24px rgba(139, 94, 32, .055),
    0 12px 36px #001f2478,
    0 0 0 1px rgba(248, 231, 189, .52);
}
@media print {
  main {
    background: #f8eed6 !important;
    box-shadow: none !important;
  }
}
""".strip()


@dataclass(frozen=True)
class Work:
    folder: str
    stem: str
    full_name: str
    birth_date: str

    @property
    def directory(self) -> Path:
        return ROOT / "output" / "lucrari" / self.folder

    @property
    def revision_md(self) -> Path:
        return self.directory / f"{self.stem}-scurt-v1.00r.md"

    @property
    def revision_html(self) -> Path:
        return self.directory / f"{self.stem}-scurt-v1.00r.html"

    @property
    def final_md(self) -> Path:
        return self.directory / f"{self.stem}-scurt-v1.00f.md"

    @property
    def final_html(self) -> Path:
        return self.directory / f"{self.stem}-scurt-v1.00f.html"


WORKS = (
    Work(
        folder="1998-01-12-ROMAN-ANDREEA-MARIA",
        stem="1998-01-12-ROMAN-ANDREEA-MARIA",
        full_name="Roman Andreea Maria",
        birth_date="12.01.1998",
    ),
    Work(
        folder="1998-02-19-BIRSAN-DANIEL-ROBERT",
        stem="1998-02-19-BIRSAN-DANIEL-ROBERT",
        full_name="Bîrsan Daniel Robert",
        birth_date="19.02.1998",
    ),
)


EDITORIAL_BULLET = re.compile(
    r"(?mi)^- (?:Template selectat|Stil de redactare|Nivel de detaliere|Versiune):[^\n]*\n?"
)
EMPTY_PREVIOUS_NAME_BULLET = re.compile(
    r"(?mi)^- Nume anterior:\s*(?:nu există|nu exista)\s*\n?"
)
ANALYSIS_INTERVAL_BULLET = re.compile(r"(?mi)^- Interval analizat:[^\n]*\n?")
WORK_DATE_BULLET = re.compile(r"(?mi)^- Data lucrării:[^\n]*")
INDEX_LINE = re.compile(r"(?mi)^Index:[^\n]*\n(?:[ \t]*\n)?")
DOCUMENTATION_MD = re.compile(
    r"(?ms)\n## Documentația și trasabilitatea lucrării\s*\n.*\Z"
)
INDEX_HTML = re.compile(
    r"(?is)<div class=\"(?:idx|index)(?: [^\"]*)?\">\s*Index:.*?</div>\s*"
)
EDITORIAL_LI = re.compile(
    r"(?is)<li>(?:Template selectat|Stil de redactare|Nivel de detaliere|Versiune):.*?</li>\s*"
)
EMPTY_PREVIOUS_NAME_LI = re.compile(
    r"(?is)<li>Nume anterior:\s*(?:nu există|nu exista)\s*</li>\s*"
)
ANALYSIS_INTERVAL_LI = re.compile(r"(?is)<li>Interval analizat:.*?</li>\s*")
WORK_DATE_LI = re.compile(r"(?is)<li>Data lucrării:.*?</li>")
DOCUMENTATION_HTML = re.compile(
    r"(?is)<h2 id=\"documentatia-si-trasabilitatea-lucrarii\">.*?</main>"
)
ELEMENT_INDEXES = re.compile(
    r"(?is)<div class=\"element-indexes\">.*?</div>"
)
INLINE_INDEX = re.compile(
    r"(?i)(?:\*\*|<strong>)?Index:\s*[A-Z]{2,4}-\d{8}-v\d+\.\d+[rf]-[A-Za-z0-9-]+"
    r"(?:\*\*|</strong>)?(?:<br>)?"
)


def final_toc_md(text: str) -> str:
    pattern = re.compile(r"(?ms)(^## Cuprins\s*\n\n)(.*?)(?=\n## Capitolul 1\.)")

    def repl(match: re.Match[str]) -> str:
        entries: list[str] = []
        for line in match.group(2).splitlines():
            item = re.fullmatch(r"\s*(\d+)\.\s+(.+?)\s*", line)
            if item:
                entries.append(f"Capitolul {item.group(1)}. {item.group(2)}  ")
        if len(entries) != 11:
            raise RuntimeError(f"Cuprins Markdown incomplet: {len(entries)} intrări")
        return match.group(1) + "\n".join(entries) + "\n"

    text, replaced = pattern.subn(repl, text, count=1)
    if replaced != 1:
        raise RuntimeError("Cuprinsul Markdown nu a putut fi transformat")
    return text


def final_toc_html(text: str) -> str:
    pattern = re.compile(r'(?is)(<h2 id="cuprins">Cuprins</h2>)\s*<ol>(.*?)</ol>')

    def repl(match: re.Match[str]) -> str:
        entries = re.findall(r"(?is)<li>(.*?)</li>", match.group(2))
        if len(entries) != 11:
            raise RuntimeError(f"Cuprins HTML incomplet: {len(entries)} intrări")
        nav = "".join(f'<div class="toc-entry">{entry}</div>' for entry in entries)
        return match.group(1) + f'<nav class="toc-final">{nav}</nav>'

    text, replaced = pattern.subn(repl, text, count=1)
    if replaced != 1:
        raise RuntimeError("Cuprinsul HTML nu a putut fi transformat")
    return text


def final_frontmatter(source: str, work: Work) -> str:
    match = re.match(r"\A---\n(.*?)\n---\n", source, re.S)
    if not match:
        raise RuntimeError(f"Frontmatter lipsă: {work.revision_md}")

    kept: list[str] = []
    for line in match.group(1).splitlines():
        key = line.split(":", 1)[0].strip().lower()
        if key in {"template", "versiune", "agent", "tags"}:
            continue
        if key == "titlu":
            kept.append(f"titlu: {work.full_name} — {work.birth_date}")
        elif key == "status":
            kept.append("status: final")
        else:
            kept.append(line)

    return "---\n" + "\n".join(kept) + "\n---\n" + source[match.end() :]


def build_final_md(source: str, work: Work) -> str:
    text = final_frontmatter(source.replace("\r\n", "\n"), work)
    text = INDEX_LINE.sub("", text)
    text = ELEMENT_INDEXES.sub("", text)
    text = INLINE_INDEX.sub("", text)
    text = EDITORIAL_BULLET.sub("", text)
    text = EMPTY_PREVIOUS_NAME_BULLET.sub("", text)
    text = ANALYSIS_INTERVAL_BULLET.sub("", text)
    text = WORK_DATE_BULLET.sub(f"- Data lucrării: {FINAL_WORK_DATE}", text)
    text = final_toc_md(text)
    text = DOCUMENTATION_MD.sub("\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"
    return text


def build_final_html(source: str, work: Work) -> str:
    text = source.replace("\r\n", "\n")
    text = INDEX_HTML.sub("", text)
    text = ELEMENT_INDEXES.sub("", text)
    text = INLINE_INDEX.sub("", text)
    text = EDITORIAL_LI.sub("", text)
    text = EMPTY_PREVIOUS_NAME_LI.sub("", text)
    text = ANALYSIS_INTERVAL_LI.sub("", text)
    text = WORK_DATE_LI.sub(f"<li>Data lucrării: {FINAL_WORK_DATE}</li>", text)
    text = final_toc_html(text)
    text = DOCUMENTATION_HTML.sub("</main>", text)
    text, style_replaced = re.subn(
        r"</style>",
        "\n" + FINAL_PAPER_CSS + "\n</style>",
        text,
        count=1,
    )
    if style_replaced != 1:
        raise RuntimeError(f"Stilul HTML negăsit: {work.revision_html}")
    header = (
        f'<header><div class="title">{work.full_name}</div>'
        f'<div class="meta">{work.birth_date}</div></header>'
    )
    text, replaced = re.subn(r"(?is)<header>.*?</header>", header, text, count=1)
    if replaced != 1:
        raise RuntimeError(f"Header HTML negăsit: {work.revision_html}")
    return text.rstrip() + "\n"


def validate_final(work: Work, revision_html: str, md: str, html: str) -> None:
    failures: list[str] = []
    if "Index:" in md or "Index:" in html:
        failures.append("au rămas indexuri")
    if "## Documentația și trasabilitatea lucrării" in md:
        failures.append("capitolul de documentație a rămas în Markdown")
    if 'id="documentatia-si-trasabilitatea-lucrarii"' in html:
        failures.append("capitolul de documentație a rămas în HTML")
    if re.search(r"(?mi)^- (?:Template selectat|Stil de redactare|Nivel de detaliere|Versiune):", md):
        failures.append("metadatele editoriale au rămas în Date generale")
    if re.search(r"(?i)<li>(?:Template selectat|Stil de redactare|Nivel de detaliere|Versiune):", html):
        failures.append("metadatele editoriale au rămas în Date generale HTML")
    if re.search(r"(?mi)^- Nume anterior:\s*(?:nu există|nu exista)|^- Interval analizat:", md):
        failures.append("câmpurile fără valoare au rămas în Date generale")
    if re.search(r"(?is)<li>Nume anterior:\s*(?:nu există|nu exista)|<li>Interval analizat:", html):
        failures.append("câmpurile fără valoare au rămas în Date generale HTML")
    if f"- Data lucrării: {FINAL_WORK_DATE}" not in md or f"<li>Data lucrării: {FINAL_WORK_DATE}</li>" not in html:
        failures.append("data ultimei modificări nu este actualizată")
    toc_md = re.search(r"(?ms)^## Cuprins\s*\n\n(.*?)(?=\n## Capitolul 1\.)", md)
    if not toc_md or re.search(r"(?m)^\d+\.\s", toc_md.group(1)) or toc_md.group(1).count("Capitolul ") != 11:
        failures.append("Cuprinsul Markdown păstrează numerotarea automată")
    toc_html = re.search(r'(?is)<h2 id="cuprins">Cuprins</h2>(.*?)(?=<h2 id="capitolul-1-)', html)
    if not toc_html or "<ol>" in toc_html.group(1) or toc_html.group(1).count('class="toc-entry"') != 11:
        failures.append("Cuprinsul HTML păstrează numerotarea automată")
    expected_header = (
        f'<header><div class="title">{work.full_name}</div>'
        f'<div class="meta">{work.birth_date}</div></header>'
    )
    if expected_header not in html:
        failures.append("headerul final nu conține exclusiv numele și data nașterii")
    if "final-paper-texture" not in html or "repeating-linear-gradient(0deg" in html.split("final-paper-texture", 1)[1]:
        failures.append("textura finală de hârtie nu este aplicată corect")
    if "status: final" not in md or re.search(r"(?mi)^versiune:", md):
        failures.append("frontmatterul final este incorect")
    if html.count("data:image/") != revision_html.count("data:image/"):
        failures.append("numărul imaginilor integrate diferă față de revizie")
    relative_images = re.findall(r'<img\b[^>]*\bsrc="(?!data:)[^"]+"', html, re.I)
    if relative_images:
        failures.append("HTML-ul final conține imagini relative")
    for broken in ("Ã", "Ä", "È", "Â", "â€”", "â†’", "�"):
        if broken in md or broken in html:
            failures.append(f"posibil mojibake: {broken}")
    if failures:
        raise AssertionError(f"{work.full_name}: " + "; ".join(failures))


def main() -> None:
    for work in WORKS:
        revision_md = work.revision_md.read_text(encoding="utf-8")
        revision_html = work.revision_html.read_text(encoding="utf-8")
        final_md = build_final_md(revision_md, work)
        final_html = build_final_html(revision_html, work)
        validate_final(work, revision_html, final_md, final_html)
        work.final_md.write_text(final_md, encoding="utf-8", newline="\n")
        work.final_html.write_text(final_html, encoding="utf-8", newline="\n")
        print(work.final_md)
        print(work.final_html)


if __name__ == "__main__":
    main()

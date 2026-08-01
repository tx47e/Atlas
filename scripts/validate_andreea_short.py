from __future__ import annotations

import base64
import hashlib
import re
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "output/lucrari/1998-01-12-ROMAN-ANDREEA-MARIA"
MD = DIR / "1998-01-12-ROMAN-ANDREEA-MARIA-scurt-v1.00r.md"
HTML = DIR / "1998-01-12-ROMAN-ANDREEA-MARIA-scurt-v1.00r.html"
DANIEL_MD = ROOT / "output/lucrari/1998-02-19-BIRSAN-DANIEL-ROBERT/1998-02-19-BIRSAN-DANIEL-ROBERT-scurt-v1.00r.md"


def main() -> None:
    md = MD.read_text(encoding="utf-8")
    html = HTML.read_text(encoding="utf-8")
    daniel_md = DANIEL_MD.read_text(encoding="utf-8")
    ids = re.findall(r'\bid="([^"]+)"', html)
    hrefs = re.findall(r'href="#([^"]+)"', html)
    images = re.findall(r'<img\b[^>]*\bsrc="([^"]+)"[^>]*>', html)
    source_pairs = re.findall(r'<img\b[^>]*\bsrc="([^"]+)"[^>]*\bdata-source="([^"]+)"[^>]*>', html)
    md_refs = re.findall(r'!\[[^]]*\]\(([^)]+)\)', md) + re.findall(r'<img\b[^>]*\bsrc="([^"]+)"', md)

    errors: list[str] = []
    duplicates = sorted({x for x in ids if ids.count(x) > 1})
    missing_anchors = sorted(set(hrefs) - set(ids))
    missing_files = [x for x in md_refs if not (DIR / x).is_file()]
    if duplicates:
        errors.append(f"ID-uri duplicate: {duplicates}")
    if missing_anchors:
        errors.append(f"Ancore lipsă: {missing_anchors}")
    if any(not x.startswith("data:") for x in images):
        errors.append("HTML-ul conține imagini neîncorporate")
    if missing_files:
        errors.append(f"Fișiere grafice lipsă: {missing_files}")
    if re.search(r"\{\{|PLACEHOLDER", md + html):
        errors.append("Au rămas placeholder-e")
    if re.search(r"Ã|Ä|È|�|â€”|â†’", md + html):
        errors.append("Au fost detectate secvențe de mojibake")
    if re.search(r"^Index: (?!RAM-19980112-v1\.00r-)", md, re.M):
        errors.append("Există index străin")
    if re.search(r"(?m)^Index: RAM-19980112-v1\.00r-[^\n]+\n(?!\n)", md):
        errors.append("Un index Markdown nu este separat prin linie goală de elementul următor")
    if "<p>Index: RAM-19980112-v1.00r-" in html:
        errors.append("Un index HTML a fost absorbit într-un paragraf")
    if len(re.findall(r"<div\b", html)) != len(re.findall(r"</div>", html)):
        errors.append("Elementele div nu sunt echilibrate")
    if not re.search(r'\| 12 \| <span class="spirit-cell-highlight">41</span>', md):
        errors.append("Poziția Codului Spiritului 41 nu este evidențiată corect")
    if not re.search(r'Index: RAM-19980112-v1\.00r-G-002</div>\s*<div class="matrix-grid matrix-grid-outlined"[^>]*>.*?<svg', html, re.S):
        errors.append("G-002 nu este redat conform modelului grafic cu geometrii SVG")
    if not re.search(r'Index: RAM-19980112-v1\.00r-G-002a</div>\s*<div class="matrix-grid matrix-grid-outlined"[^>]*>.*?<svg', html, re.S):
        errors.append("G-002a nu este redat ca matrice comparativă cu geometrii SVG")
    if html.count('<div class="matrix-cell element-') < 18:
        errors.append("Matricele G-002 și G-002a nu conțin câte nouă celule")
    compact_hexagram = '<polygon points="20,5 30,22 10,22"/><polygon points="20,27 10,10 30,10"/>'
    if compact_hexagram not in md or compact_hexagram not in html:
        errors.append("Hexagrama compactă nu păstrează cele șase vârfuri complet vizibile")
    if any(old in md + html for old in [
        '20,3 35,27 5,27',
        '20,6 32,25 8,25',
    ]):
        errors.append("A rămas o geometrie veche, aplatizată sau prea mare, pentru hexagramă")

    # Audit independent pentru Spirit, conform formulelor și tabelului din Vault.
    spirit_code = 55 - 12 - (2 * 1)
    spirit_substage = ((spirit_code - 1) % 13) + 1
    spirit_birth_age = (spirit_code - 1) * 189
    spirit_current_age = spirit_birth_age + 28
    if (spirit_code, spirit_substage, spirit_birth_age, spirit_current_age) != (41, 2, 7560, 7588):
        errors.append("Calculul independent al Codului Spiritului a eșuat")
    required_spirit = [
        'class="table-wrap spirit-code-wrap"><table class="spirit-code-table"',
        '<td>12</td>\n<td align="right"><span class="spirit-cell-highlight">41</span></td>',
        '<table class="spirit-zones-table"',
        'class="zone-cell zone-gifts"><span class="zone-badge">Haruri</span>',
        '<tr class="stage-love current-row"><td>2</td><td>Interacțiune</td>',
        'Vârsta actuală = 7.560 + 28 = <strong>7.588 ani</strong>',
    ]
    for needle in required_spirit:
        if needle not in html:
            errors.append(f"Spirit incomplet sau formatat greșit: {needle}")
    if 'stage-reason current-row' in html:
        errors.append("T-019 evidențiază greșit subetapa 6 rămasă din modelul Daniel")

    required_karma = [
        'Arcana karmică = <strong>12 — Spânzuratul</strong>',
        'Intervalul 10–19 = karma împlinită <strong>spre 80%</strong>',
        'Karma lunii = <strong>karma față de frate sau soră</strong>',
        'Karma din Calea Destinului = <strong>31</strong>',
        'categoria karmică <strong>3</strong>',
        'Arcana <strong>9</strong> — Eremitul. Karma din Calea Destinului <strong>31</strong>',
    ]
    for needle in required_karma:
        if needle not in html:
            errors.append(f"Karma incompletă sau calculată greșit: {needle}")
    if not all(x in md for x in ["0–32 ani", "33–42 ani", "43–52 ani", "53 ani–sfârșit"]):
        errors.append("Intervalele pinaclurilor nu sunt complete")
    if not all(x in md for x in ["vibrația anuală **5**", "Lecția **9**", "Soarta și Destinul sunt la **2 / 2**"]):
        errors.append("Sinteza perioadei curente este incompletă")

    # Contract 1:1 cu modelul Daniel: aceeași schemă, valori și texte personale.
    index_pattern = r"^Index: [A-Z]+-\d+-v1\.00r-([^\s]+)"
    daniel_indexes = re.findall(index_pattern, daniel_md, re.M)
    andreea_indexes = re.findall(index_pattern, md, re.M)
    if daniel_indexes != andreea_indexes:
        errors.append("Secvența tipurilor și sufixelor de index nu coincide cu modelul Daniel")
    heading_pattern = r"^(#{2,3})\s+(.+)$"
    if re.findall(heading_pattern, daniel_md, re.M) != re.findall(heading_pattern, md, re.M):
        errors.append("Structura capitolelor și subcapitolelor nu coincide cu modelul Daniel")
    if re.findall(r"^### 11\.[^\n]+", md, re.M) != [
        "### 11.1. Carieră și bani",
        "### 11.2. Iubire și relație",
    ]:
        errors.append("Concluziile Andreei nu au exact cele două subcapitole aprobate")
    personal_conclusion_values = [
        "Destinul tău **31/4**",
        "Numărul tău ereditar karmic este **3**",
        "Arcana **6 — Îndrăgostiții**",
        "Arcanei **9 — Eremitul**",
        "Soarta și Destinul sunt la **2 / 2**",
    ]
    for needle in personal_conclusion_values:
        if needle not in md:
            errors.append(f"Concluzia personală a Andreei nu conține: {needle}")
    shared_relationship_values = [
        "potențialul maxim al relației este **4**",
        "podul de trecut este **2**",
        "**111**, **2**, **8** și **99**",
        "**11**, **2**, **8** și **999**",
    ]
    for needle in shared_relationship_values:
        if needle not in md or needle not in daniel_md:
            errors.append(f"Faptul relațional comun diferă între lucrări: {needle}")
    if any(old in md for old in ["T-020", "T-021", "G-008", "### 11.3."]):
        errors.append("Au reapărut elemente eliminate din vechiul capitol Concluzii")

    for name in [
        "matrita-datei-roman-andreea-maria.svg",
        "soarta-si-destin-roman-andreea-maria.svg",
    ]:
        ET.parse(DIR / name)
    matrix_svg = (DIR / "matrita-datei-roman-andreea-maria.svg").read_text(encoding="utf-8")
    for needle in ["N1=31", "N2=4", "N3=29", "N4=11", "120119983142911", "Atlas Numerologie"]:
        if needle not in matrix_svg:
            errors.append(f"SVG-ul matricei nu conține valoarea validată: {needle}")
    if 'data-source-svg="matrita-datei-roman-andreea-maria.svg"' not in html:
        errors.append("G-002 nu declară SVG-ul autonom folosit ca sursă tehnică")

    embedded = {name: uri for uri, name in source_pairs}
    for name in [
        "soarta-si-destin-roman-andreea-maria.svg",
        "omulet-relatii-roman-andreea-maria-birsan-daniel-robert.png",
    ]:
        uri = embedded.get(name)
        if not uri:
            errors.append(f"Resursa nu este încorporată: {name}")
            continue
        decoded = base64.b64decode(uri.split(",", 1)[1])
        if hashlib.sha256(decoded).digest() != hashlib.sha256((DIR / name).read_bytes()).digest():
            errors.append(f"Hash diferit pentru resursa încorporată: {name}")

    heading_md_count = len(re.findall(r"^#{1,4} ", md, re.M))
    heading_html_count = len(re.findall(r"<h[1-4]\b", html))
    index_count = len(re.findall(r"^Index: RAM-19980112-v1\.00r-", md, re.M))
    if heading_md_count != heading_html_count:
        errors.append(f"Număr diferit de titluri MD/HTML: {heading_md_count}/{heading_html_count}")
    if index_count == 0:
        errors.append("Nu au fost detectate indexurile reviziei")
    print(f"HEADINGS_MD={heading_md_count}")
    print(f"HEADINGS_HTML={heading_html_count}")
    print(f"INDEXES={index_count}")
    print(f"HTML_IMAGES={len(images)}")
    print(f"MD_IMAGE_REFS={len(md_refs)}")
    print("SVG_XML=valid")
    if errors:
        print("VALIDATION=FAILED")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print("VALIDATION=OK")


if __name__ == "__main__":
    main()

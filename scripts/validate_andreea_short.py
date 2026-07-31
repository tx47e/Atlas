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


def main() -> None:
    md = MD.read_text(encoding="utf-8")
    html = HTML.read_text(encoding="utf-8")
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
    if len(re.findall(r"<div\b", html)) != len(re.findall(r"</div>", html)):
        errors.append("Elementele div nu sunt echilibrate")
    if not re.search(r'\| 12 \| <span class="spirit-cell-highlight">41</span>', md):
        errors.append("Poziția Codului Spiritului 41 nu este evidențiată corect")
    if not all(x in md for x in ["0–32 ani", "33–42 ani", "43–52 ani", "53 ani–sfârșit"]):
        errors.append("Intervalele pinaclurilor nu sunt complete")
    if not all(x in md for x in ["vibrația anuală **5**", "Lecția **9**", "Soarta și Destinul sunt la **2 / 2**"]):
        errors.append("Sinteza perioadei curente este incompletă")

    for name in [
        "soarta-si-destin-roman-andreea-maria.svg",
        "harta-suprapusa-soarta-destin-roman-andreea-maria-v1.00r.svg",
    ]:
        ET.parse(DIR / name)

    embedded = {name: uri for uri, name in source_pairs}
    for name in [
        "soarta-si-destin-roman-andreea-maria.svg",
        "harta-suprapusa-soarta-destin-roman-andreea-maria-v1.00r.svg",
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

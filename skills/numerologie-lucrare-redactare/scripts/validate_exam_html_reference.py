from __future__ import annotations

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class ReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.hrefs: list[str] = []
        self.image_sources: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if data.get("id"):
            self.ids.append(data["id"] or "")
        if tag == "a" and (data.get("href") or "").startswith("#"):
            self.hrefs.append((data.get("href") or "")[1:])
        if tag == "img":
            self.image_sources.append(data.get("src") or "")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validează referința HTML pentru lucrarea de examen.")
    parser.add_argument("html", type=Path)
    parser.add_argument("--md", type=Path, help="Sursa Markdown Daniel, pentru verificarea parității indexurilor")
    args = parser.parse_args()

    document = args.html.read_text(encoding="utf-8")
    searchable = re.sub(r'(?<=src=")[^"]*;base64,[^"]+', "[DATA-URI]", document)
    errors: list[str] = []

    required = (
        "Destin compus: <strong>3 + 9 = 12</strong>",
        "Cifră de interpretare: <strong>1 + 2 = 3</strong>",
        "N1: <strong>1 + 9 + 0 + 2 + 1 + 9 + 9 + 8 = 39</strong>",
        "N2: <strong>3 + 9 = 12</strong>",
        "N3: <strong>39 - (2 × 1) = 37</strong>",
        "N4: <strong>3 + 7 = 10</strong>",
        "Limita Pinaclului 1: <strong>36 - 12 = 24</strong>",
        "0–24 ani",
        "25–34 ani",
        "35–44 ani",
        "45+ ani",
        "Numărul ereditar karmic",
        "matrix-grid",
    )
    for token in required:
        if token not in searchable:
            errors.append(f"Lipsește reperul obligatoriu: {token}")

    forbidden = ("0-33", "34-42", "43-51", "52+", "Destinul 3", "Rezultatul este 3. Destin")
    for token in forbidden:
        if token in searchable:
            errors.append(f"A rămas un reper vechi: {token}")

    for token in ("Ãƒ", "Ã„", "Ãˆ", "Ã‚", "â€œ", "â€", "ï¿½"):
        if token in searchable:
            errors.append(f"Posibil mojibake detectat: {token}")

    parsed = ReferenceParser()
    parsed.feed(document)
    duplicate_ids = sorted({value for value in parsed.ids if parsed.ids.count(value) > 1})
    if duplicate_ids:
        errors.append("ID-uri HTML duplicate: " + ", ".join(duplicate_ids))
    missing_targets = sorted({target for target in parsed.hrefs if target not in parsed.ids})
    if missing_targets:
        errors.append("Ancore fără destinație: " + ", ".join(missing_targets))
    relative_images = [src for src in parsed.image_sources if not src.startswith("data:")]
    if relative_images:
        errors.append("Imagini neîncorporate: " + ", ".join(relative_images[:5]))

    index_count = len(re.findall(r"Index: BDR-19980219-v1\.07r-", document))
    if index_count < 250:
        errors.append("Număr suspect de mic de indexuri editoriale")

    if args.md:
        markdown = args.md.read_text(encoding="utf-8")
        index_pattern = r"Index: (BDR-19980219-v1\.07r-[A-Za-z0-9-]+)"
        md_indexes = re.findall(index_pattern, markdown)
        html_indexes = re.findall(index_pattern, document)
        if md_indexes != html_indexes:
            errors.append("Ordinea sau setul indexurilor diferă între Markdown și HTML")
        if len(md_indexes) != len(set(md_indexes)):
            errors.append("Markdown-ul conține indexuri duplicate")

    if errors:
        print("VALIDARE ESUATA")
        for error in errors:
            print(f"- {error}")
        return 1

    print("VALIDARE REUSITA")
    print(f"- indexuri: {index_count}")
    print(f"- imagini incorporate: {len(parsed.image_sources)}")
    print(f"- ancore interne: {len(parsed.hrefs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

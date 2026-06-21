from pathlib import Path
import re
import sys

import pdfplumber

try:
    import pypdfium2 as pdfium
except Exception:  # pragma: no cover
    pdfium = None


BASE = Path(__file__).resolve().parent
PDF = BASE / "Chibulcutean Tamara_Lucrare Examen.pdf"
OUT_MD = BASE / "Chibulcutean Tamara_Lucrare Examen - extractie.md"
TEMPLATE_MD = BASE / "Template lucrare numerologica - din PDF.md"
PAGE_IMAGES = BASE / "pagini_pdf"


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def md_escape_cell(value: str) -> str:
    value = clean_text(value or "")
    value = value.replace("|", "\\|")
    value = value.replace("\n", "<br>")
    return value


def table_to_md(table) -> str:
    rows = [[md_escape_cell(cell or "") for cell in row] for row in table if row]
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    header = rows[0]
    sep = ["---"] * width
    body = rows[1:]
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(sep) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in body)
    return "\n".join(lines)


def render_pages() -> None:
    if pdfium is None:
        return
    PAGE_IMAGES.mkdir(exist_ok=True)
    doc = pdfium.PdfDocument(PDF)
    for page_number, page in enumerate(doc, start=1):
        target = PAGE_IMAGES / f"pagina-{page_number:03}.png"
        if target.exists():
            page.close()
            continue
        bitmap = page.render(scale=1.6)
        image = bitmap.to_pil()
        image.save(target)
        page.close()
    doc.close()


def extract_markdown() -> None:
    render_pages()
    lines = [
        "---",
        "titlu: Chibulcutean Tamara - Lucrare Examen",
        "sursa: Chibulcutean Tamara_Lucrare Examen.pdf",
        "tip: extractie markdown din PDF",
        "status: draft pentru verificare",
        "---",
        "",
        "# Chibulcutean Tamara - Lucrare Examen",
        "",
        "> Extractie realizata din PDF, pastrand ordinea paginilor. Pentru fiecare pagina este inclus textul extras automat si, unde este disponibil, captura paginii pentru verificarea graficelor, tabelelor si elementelor vizuale.",
        "",
    ]

    with pdfplumber.open(PDF) as pdf:
        total = len(pdf.pages)
        for idx, page in enumerate(pdf.pages, start=1):
            lines.append(f"## Pagina {idx}")
            lines.append("")
            image_path = PAGE_IMAGES / f"pagina-{idx:03}.png"
            if image_path.exists():
                lines.append(f"![Pagina {idx}](pagini_pdf/pagina-{idx:03}.png)")
                lines.append("")

            text = clean_text(page.extract_text(x_tolerance=1, y_tolerance=3) or "")
            if text:
                lines.append("### Text extras")
                lines.append("")
                lines.append(text)
                lines.append("")
            else:
                lines.append("_Nu s-a putut extrage text automat din aceasta pagina._")
                lines.append("")

            tables = page.extract_tables()
            if tables:
                lines.append("### Tabele detectate automat")
                lines.append("")
                for table_idx, table in enumerate(tables, start=1):
                    md_table = table_to_md(table)
                    if md_table:
                        lines.append(f"#### Tabel {table_idx}")
                        lines.append("")
                        lines.append(md_table)
                        lines.append("")

            lines.append("---")
            lines.append("")
            print(f"extras {idx}/{total}", flush=True)

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def create_template() -> None:
    template = """---
titlu: Template lucrare numerologica
tip: template derivat din lucrare PDF
sursa: Chibulcutean Tamara_Lucrare Examen.pdf
status: draft pentru standardizare
---

# Template lucrare numerologica

> Template derivat din ordinea lucrarii PDF. Completeaza campurile marcate cu `{{...}}` si pastreaza ordinea sectiunilor pentru lucrari similare.

## Coperta

- Titlu lucrare: {{titlu_lucrare}}
- Nume persoana analizata: {{nume_complet}}
- Data nasterii: {{data_nasterii}}
- Autor / consultant: {{autor}}
- Data lucrarii: {{data_lucrarii}}

## Date de intrare

| Camp | Valoare |
| --- | --- |
| Nume complet | {{nume_complet}} |
| Nume activ | {{nume_activ}} |
| Nume anterior / schimbat | {{nume_anterior}} |
| Data nasterii | {{data_nasterii}} |
| Tema / intrebare principala | {{tema_principala}} |
| Stil de adresare | {{stil_adresare}} |
| Nivel de detaliere | {{nivel_detaliere}} |

## Sinteza initiala

{{sinteza_initiala}}

## Vibratii fundamentale

### Vibratie interioara

- Calcul: {{calcul_vibratie_interioara}}
- Traseu de reducere: {{traseu_vibratie_interioara}}
- Rezultat: {{rezultat_vibratie_interioara}}

{{interpretare_vibratie_interioara}}

### Vibratie exterioara

- Calcul: {{calcul_vibratie_exterioara}}
- Traseu de reducere: {{traseu_vibratie_exterioara}}
- Rezultat: {{rezultat_vibratie_exterioara}}

{{interpretare_vibratie_exterioara}}

### Vibratie cosmica fixa

- Calcul: {{calcul_vibratie_cosmica_fixa}}
- Traseu de reducere: {{traseu_vibratie_cosmica_fixa}}
- Rezultat: {{rezultat_vibratie_cosmica_fixa}}

{{interpretare_vibratie_cosmica_fixa}}

### Vibratie cosmica variabila

- Calcul: {{calcul_vibratie_cosmica_variabila}}
- Traseu de reducere: {{traseu_vibratie_cosmica_variabila}}
- Rezultat: {{rezultat_vibratie_cosmica_variabila}}

{{interpretare_vibratie_cosmica_variabila}}

### Vibratie cosmica totala

- Calcul: {{calcul_vibratie_cosmica_totala}}
- Traseu de reducere: {{traseu_vibratie_cosmica_totala}}
- Rezultat: {{rezultat_vibratie_cosmica_totala}}

{{interpretare_vibratie_cosmica_totala}}

### Vibratie globala

- Calcul: {{calcul_vibratie_globala}}
- Traseu de reducere: {{traseu_vibratie_globala}}
- Rezultat: {{rezultat_vibratie_globala}}

{{interpretare_vibratie_globala}}

## Destin si evolutie

### Vibratia destinului

- Calcul: {{calcul_vibratia_destinului}}
- Traseu de reducere: {{traseu_vibratia_destinului}}
- Rezultat: {{rezultat_vibratia_destinului}}

{{interpretare_vibratia_destinului}}

### Calea destinului

{{calea_destinului}}

### Aspecte de indreptat

{{aspecte_de_indreptat}}

### Soarta si destin

| Element | Valoare |
| --- | --- |
| Soarta | {{soarta}} |
| Zona de confort a sortii | {{zona_confort_soarta}} |
| Destin | {{destin}} |
| Zona de confort a destinului | {{zona_confort_destin}} |

![Grafic soarta si destin]({{grafic_soarta_destin}})

{{interpretare_soarta_destin}}

### Punti

| Punte | Calcul | Rezultat | Interpretare |
| --- | --- | --- | --- |
| Interior - exterior | {{calcul_punte_interior_exterior}} | {{rezultat_punte_interior_exterior}} | {{interpretare_punte_interior_exterior}} |
| Interior - destin | {{calcul_punte_interior_destin}} | {{rezultat_punte_interior_destin}} | {{interpretare_punte_interior_destin}} |
| Exterior - destin | {{calcul_punte_exterior_destin}} | {{rezultat_punte_exterior_destin}} | {{interpretare_punte_exterior_destin}} |
| Cosmic - destin | {{calcul_punte_cosmic_destin}} | {{rezultat_punte_cosmic_destin}} | {{interpretare_punte_cosmic_destin}} |

## Karma

### Karma din ziua nasterii

{{karma_ziua_nasterii}}

### Karma din luna nasterii

{{karma_luna_nasterii}}

### Karma din calea destinului

{{karma_calea_destinului}}

## Numere personale

### Numarul de exprimare

{{numarul_de_exprimare}}

### Numarul intim

{{numarul_intim}}

### Numarul de realizare

{{numarul_de_realizare}}

### Numarul activ

{{numarul_activ}}

### Numarul ereditar

{{numarul_ereditar}}

### Numarul neamului

{{numarul_neamului}}

### Cod numerologic personal

{{cod_numerologic_personal}}

## Matrici si analize

### Matricea datei de nastere

```text
1 | 4 | 7
2 | 5 | 8
3 | 6 | 9
```

{{matricea_datei_de_nastere}}

### Matricea numelui

```text
1 | 4 | 7
2 | 5 | 8
3 | 6 | 9
```

{{matricea_numelui}}

### Matricea numelui vs matricea datei de nastere

{{comparatie_matrici}}

### Scara bunastarii

| Pozitie | Denumire | Cantitate | Formula | Valoare | Interpretare |
| --- | --- | --- | --- | --- | --- |
| {{pozitie}} | {{denumire}} | {{cantitate}} | {{formula}} | {{valoare}} | {{interpretare}} |

{{interpretare_scara_bunastarii}}

## Cicluri si etape de viata

### Pinacluri - oportunitati si provocari

| Etapa | Varsta | Oportunitate | Provocare | Interpretare |
| --- | --- | --- | --- | --- |
| Pinaclul 1 | {{varsta_p1}} | {{oportunitate_p1}} | {{provocare_p1}} | {{interpretare_p1}} |
| Pinaclul 2 | {{varsta_p2}} | {{oportunitate_p2}} | {{provocare_p2}} | {{interpretare_p2}} |
| Pinaclul 3 | {{varsta_p3}} | {{oportunitate_p3}} | {{provocare_p3}} | {{interpretare_p3}} |
| Pinaclul 4 | {{varsta_p4}} | {{oportunitate_p4}} | {{provocare_p4}} | {{interpretare_p4}} |

### Ciclul de 7 ani

{{ciclul_de_7_ani}}

### Lectii de viata

{{lectii_de_viata}}

### Ciclul de 9 ani

{{ciclul_de_9_ani}}

### Ciclul de 12 ani

{{ciclul_de_12_ani}}

### Ani importanti interiori si exteriori

| An | Important interior | Important exterior | Interpretare |
| --- | --- | --- | --- |
| {{an}} | {{important_interior}} | {{important_exterior}} | {{interpretare_an}} |

## Ezoterism si aplicabilitate

### Deschidere spre ezoterism

{{deschidere_spre_ezoterism}}

### Aplicabilitate profesionala

{{aplicabilitate_profesionala}}

## Concluzie finala

### Directia principala

{{directia_principala}}

### Resurse dominante

{{resurse_dominante}}

### Provocari principale

{{provocari_principale}}

### Recomandari practice

{{recomandari_practice}}

### Inchidere

{{concluzie_finala}}
"""
    TEMPLATE_MD.write_text(template, encoding="utf-8")


if __name__ == "__main__":
    if not PDF.exists():
        print(f"PDF lipsa: {PDF}", file=sys.stderr)
        sys.exit(1)
    extract_markdown()
    create_template()
    print(OUT_MD)
    print(TEMPLATE_MD)

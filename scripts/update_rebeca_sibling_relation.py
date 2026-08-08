from __future__ import annotations

import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "output/lucrari/2020-03-15-VULCU-REBECA-ANDREEA"
MD = DIR / "2020-03-15-VULCU-REBECA-ANDREEA-scurt-v1.00r.md"
PAIR_DIR = ROOT / "output/lucrari/2025-07-14-VULCU-MARC-IOAN"
PREFIX = "VRA-20200315-v1.00r"


def main() -> None:
    source_stem = "omulet-relatii-vulcu-marc-ioan-vulcu-rebeca-andreea"
    target_stem = "omulet-relatii-vulcu-rebeca-andreea-vulcu-marc-ioan"
    for extension in (".svg", ".png"):
        shutil.copyfile(PAIR_DIR / f"{source_stem}{extension}", DIR / f"{target_stem}{extension}")

    text = MD.read_text(encoding="utf-8")
    text = text.replace("Vulcu Rebeca Rebeca", "Vulcu Rebeca Andreea")
    if "- Relație analizată:" not in text:
        text = text.replace(
            "- Gen: feminin\n",
            "- Gen: feminin\n- Relație analizată: Vulcu Marc Ioan, frate, născut la 14.07.2025\n",
            1,
        )
    text = text.replace(
        "8. Ciclicități\n9. Concluzii",
        "8. Ciclicități\n9. Relații\n10. Aplicabilitate profesională\n11. Concluzii",
        1,
    )
    text = text.replace("## Capitolul 9. Concluzii", "## Capitolul 11. Concluzii", 1)
    text = text.replace("### 9.1. Carieră și bani", "### 11.1. Carieră și bani", 1)

    relation_and_professional = f'''Index: {PREFIX}-CAP-013

## Capitolul 9. Relații

Index: {PREFIX}-L-003

- Nume: Vulcu Marc Ioan
- Data nașterii: 14.07.2025
- Gen: masculin
- Tipul relației: frate

Index: {PREFIX}-SUB-028

### 9.1. Omulețul relațiilor

Index: {PREFIX}-G-006

![Omulețul relațiilor pentru Vulcu Rebeca Andreea și Vulcu Marc Ioan]({target_stem}.png)

Index: {PREFIX}-C-007

> [!example] Calcul relațional
> Realizare împreună: 6 + 5 = 11 → **2**  
> De rezolvat împreună: |6 − 5| = **1**

Index: {PREFIX}-P-029

Rebeca, tu vii în relația cu fratele tău prin ziua redusă **6**, iar Marc prin **5**. Tu aduci grijă, armonie și tendința de a proteja; el aduce curiozitate, mișcare și dorință de explorare. Potențialul comun **2** cere cooperare, apropiere și atenție la ritmul emoțional al fiecăruia.

Index: {PREFIX}-P-030

Tema de rezolvat **1** este identitatea. Faptul că ești sora mai mare nu înseamnă că trebuie să porți responsabilitatea pentru toate reacțiile lui Marc. Ai voie să ai propriile obiecte, prietenii și momente de liniște, iar el are nevoie să descopere singur ce poate face. Legătura devine sănătoasă când ajutorul nu se transformă în control.

Index: {PREFIX}-P-031

Împreună aveți Foc **4**, Apă **4**, Aer **2**, Pământ **1** și potențialul lui **0** de **4** ori. Inițiativa și emoția sunt puternice, dar partea practică are nevoie de reguli simple, ritualuri de familie și responsabilități potrivite vârstei. Activitățile comune scurte, urmate de timp separat, vă ajută să păstrați și apropierea, și autonomia.

Index: {PREFIX}-CAP-014

## Capitolul 10. Aplicabilitate profesională

Index: {PREFIX}-SUB-029

### 10.1. Aplicabilitate profesională

Index: {PREFIX}-C-014

> [!example] Calcul
> DA: luna 3 + suma cifrelor anului 4 = **7**  
> NU: suma tuturor cifrelor datei = **13**

Index: {PREFIX}-T-016

| Aplicabilitate profesională DA | Aplicabilitate profesională NU |
| --- | --- |
| **7 — Carul:** direcție, mobilizare și capacitatea de a conduce energia către o țintă. | **13 — Moartea:** obstacolul poate fi teama de schimbare sau dificultatea de a încheia o etapă. |

Index: {PREFIX}-P-046

Pentru Rebeca, această secțiune descrie un potențial aflat încă în formare. Energia **7** susține concentrarea, învățarea și orientarea către un scop, iar **13** cere acceptarea transformării. Un mediu stabil, dar flexibil, îi permite să învețe că schimbarea nu distruge siguranța, ci poate crea o formă mai potrivită.

'''
    if f"Index: {PREFIX}-CAP-013" not in text:
        text = text.replace(f"Index: {PREFIX}-CAP-015\n", relation_and_professional + f"Index: {PREFIX}-CAP-015\n", 1)

    relation_conclusion = f'''Index: {PREFIX}-SUB-031

### 11.2. Iubire și relație

Index: {PREFIX}-P-032r

Rebeca, relația cu Marc are potențialul **2**, deci crește prin cooperare, blândețe și sentimentul că sunteți de aceeași parte. Tu poți aduce grijă și continuitate, iar el poate aduce joc, mișcare și noutate.

Index: {PREFIX}-P-032s

Podul **1** vă cere să rămâneți două persoane distincte. Nu trebuie să fii permanent „cea responsabilă”, iar Marc nu trebuie fixat în rolul „celui mic”. Când adulții evită comparațiile, vă oferă timp individual și împart responsabilitățile potrivit vârstei, apropierea nu devine competiție.

Index: {PREFIX}-SUB-040

### 11.3. Momentul prezent

Index: {PREFIX}-P-032t

Rebeca, în 2026 te afli în primul Pinaclu, cu Oportunitatea **9** și Provocarea **3**, în primul ciclu de 9 ani și în primul ciclu de 12 ani. Anul personal **1** deschide inițiativa, iar Lecția **0** cere timp de acumulare și integrare. Pentru etapa ta actuală, direcția potrivită este să primești experiențe noi în pași mici, cu rutină stabilă, exprimare prin joc și libertatea de a observa înainte de a răspunde.

'''
    if f"Index: {PREFIX}-SUB-031" not in text:
        text = text.replace(f"Index: {PREFIX}-CAP-016\n", relation_conclusion + f"Index: {PREFIX}-CAP-016\n", 1)

    text = re.sub(
        r"\| SVG-uri integrate \| Matrice, Scara bunăstării și Soartă–Destin \|",
        "| SVG-uri integrate | Matrice, Scara bunăstării, Soartă–Destin și Omulețul relațiilor |",
        text,
    )
    MD.write_text(text, encoding="utf-8", newline="\n")
    print(MD)


if __name__ == "__main__":
    main()

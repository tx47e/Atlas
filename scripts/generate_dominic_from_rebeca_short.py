from __future__ import annotations

import importlib.util
import json
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_MD = ROOT / "output/lucrari/2020-03-15-VULCU-REBECA-ANDREEA/2020-03-15-VULCU-REBECA-ANDREEA-scurt-v1.00r.md"
OUT_DIR = ROOT / "output/lucrari/2021-05-08-VULCU-DOMINIC-IOAN"
OUT = OUT_DIR / ".2021-05-08-VULCU-DOMINIC-IOAN-scurt-v1.00r.tmp.md"
REPORT = OUT_DIR / "2021-05-08-VULCU-DOMINIC-IOAN-scurt-v1.00r-calculator.json"
CALCULATOR = ROOT / "skills/numerologie-lucrare-redactare/scripts/calculator_numerologic_examen.py"
MATRIX_GENERATOR = ROOT / "skills/numerologie-SVG-matrita-datei-de-nastere/scripts/generate_matrita_datei_de_nastere.py"
NAME_MATRIX_GENERATOR = ROOT / "skills/numerologie-SVG-matrita-numelui/scripts/generate_matrita_numelui.py"
SOARTA_GENERATOR = ROOT / "skills/numerologie-SVG-soarta-si-destin/scripts/generate_soarta_si_destin.py"
RELATION_GENERATOR = ROOT / "skills/numerologie-SVG-omuletul-relatiilor/scripts/generate_omulet_relatiilor.py"
PREFIX = "VDI-20210508-v1.00r"


ARCANA = {
    8: ("Puterea", "08-Strenght.jpg", "tarot-08-puterea-karma-zilei.jpg"),
    16: ("Turnul", "16-The Tower.jpg", "tarot-16-turnul-numarul-ereditar-karmic.jpg"),
    18: ("Luna", "18-The Moon.jpg", "tarot-18-luna-karma-calea-destinului.jpg"),
}


def run_report() -> dict:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [
            sys.executable,
            str(CALCULATOR),
            "--data-nasterii", "08.05.2021",
            "--nume-complet", "Vulcu Dominic Ioan",
            "--nume-familie", "Vulcu",
            "--prenume", "Dominic Ioan",
            "--prenume-activ", "Domi",
            "--gen", "masculin",
            "--an-start", "2021",
            "--an-final", "2129",
            "--pretty",
        ],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    report = json.loads(result.stdout)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    return report


def run_partner_report() -> dict:
    result = subprocess.run(
        [
            sys.executable,
            str(CALCULATOR),
            "--data-nasterii", "17.03.2023",
            "--nume-complet", "Vulcu Victor Daniel",
            "--nume-familie", "Vulcu",
            "--prenume", "Victor Daniel",
            "--prenume-activ", "Vic",
            "--gen", "masculin",
            "--an-start", "2023",
            "--an-final", "2131",
            "--pretty",
        ],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return json.loads(result.stdout)


def load_generator(path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if not spec or not spec.loader:
        raise RuntimeError(f"Nu pot încărca generatorul: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def replace_block(text: str, suffix: str, body: str) -> str:
    marker = f"Index: {PREFIX}-{suffix}"
    pattern = rf"({re.escape(marker)}\n)(.*?)(?=\nIndex: {re.escape(PREFIX)}-|\Z)"
    updated, count = re.subn(pattern, lambda m: m.group(1) + "\n" + body.rstrip() + "\n", text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"Blocul {suffix} nu a fost găsit o singură dată: {count}")
    return updated


def wellbeing(rows: list[dict]) -> str:
    max_value = max(x["valoare"] for x in rows) or 1
    classes = {1: "foc", 2: "apa", 3: "aer", 4: "pamant", 5: "foc", 6: "apa", 7: "aer", 8: "pamant", 9: "foc"}
    out = ['<div class="wellbeing-chart" aria-label="Scara bunăstării">']
    for item in rows:
        value = item["valoare"]
        width = round(value / max_value * 100, 2)
        if item["tip"] == "vector":
            code, name = item["denumire"].split(" - ", 1)
            label = f'<span class="wellbeing-label vector-label">Vector {code} — {name}</span>'
        else:
            n = int(item["denumire"])
            label = f'<span class="wellbeing-label"><i class="element-dot element-{classes[n]}"></i>Căsuța {n}</span>'
        out.append(f'<div class="wellbeing-row">{label}<span class="wellbeing-track"><span class="wellbeing-fill" style="width:{width}%"></span></span><span class="wellbeing-value">{value}</span></div>')
    out.append('<div class="wellbeing-legend"><span><i class="element-dot element-foc"></i>Foc</span><span><i class="element-dot element-pamant"></i>Pământ</span><span><i class="element-dot element-apa"></i>Apă</span><span><i class="element-dot element-aer"></i>Aer</span></div>')
    out.append("</div>")
    return "\n".join(out)


def lesson_table(lessons: list[int], start_year: int = 2020, end_age: int = 60) -> str:
    headers = " | ".join(f'Lecția {i + 1} — <strong style="font-size: 1.15em; font-weight: 700;">{v}</strong>' for i, v in enumerate(lessons))
    aligns = " | ".join(["---:"] * len(lessons))
    lines = [f"| Vârstă | {headers} |", f"| --- | {aligns} |"]
    step = len(lessons)
    for start_age in range(1, end_age + 1, step):
        vals = []
        for offset in range(step):
            age = start_age + offset
            year = start_year + age - 1
            val = str(year)
            if year == 2026:
                val = f'<span style="color: #b3261e; font-weight: 700;">{year}</span>'
            vals.append(val)
        lines.append(f"| {start_age}–{start_age + step - 1} | " + " | ".join(vals) + " |")
    return "\n".join(lines)


def cycle9_table(start_year: int = 2020) -> str:
    lines = [
        "| Ciclu (vârstă) | Anul 1 — început | Anul 2 | Anul 3 | Anul 4 | Anul 5 | Anul 6 | Anul 7 | Anul 8 | Anul 9 — încheiere |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for cycle in range(1, 10):
        first = start_year + (cycle - 1) * 9
        vals = []
        for pos in range(9):
            year = first + pos
            val = f"**{year}**" if pos in (0, 8) else str(year)
            if year == 2026:
                val = f'<span style="color: #b3261e; font-weight: 700;">{year}</span>'
            vals.append(val)
        a0 = (cycle - 1) * 9
        lines.append(f"| C{cycle} ({a0}–{a0 + 8}) | " + " | ".join(vals) + " |")
    return "\n".join(lines)


def cycle12_table(start_year: int = 2021) -> str:
    readings = {
        1: "Formarea primelor repere: corp, familie, ritm, limbaj emoțional și primele reguli ale siguranței.",
        2: "Explorare, desprindere treptată și definirea unei direcții proprii în raport cu familia și lumea.",
        3: "Extindere prin alegeri, experiențe, studiu, relații și responsabilități asumate conștient.",
        4: "Consolidarea unei forme de viață mai ample: profesie, familie, structură, statut și stabilitate.",
        5: "Recalibrarea sensului și valorificarea experienței acumulate prin libertate matură și selecție.",
        6: "Transmitere, maturitate și influență exercitată cu discernământ în familie, comunitate sau proiecte.",
        7: "Sinteză spirituală, simplificare și întoarcere la ceea ce rămâne esențial după multe experiențe.",
        8: "Moștenire, ghidare și administrarea responsabilă a puterii, resurselor și înțelepciunii acumulate.",
        9: "Integrare târzie, împăcare cu etapele parcurse și închiderea ciclurilor lungi cu luciditate.",
    }
    lines = ["| Ciclu | Interval calendaristic | Vârste | Citire |", "| --- | --- | ---: | --- |"]
    for i in range(1, 10):
        start_age = (i - 1) * 12
        end_age = start_age + 11
        cycle_start = start_year + start_age
        cycle_end = start_year + end_age
        if i == 1:
            style = '<span class="active-cycle-cell" style="color: #b3261e; font-weight: 700;">'
            close = "</span>"
            lines.append(f"| {style}**Ciclul {i} — activ**{close} | {style}**{cycle_start}–{cycle_end}**{close} | {style}**{start_age}–{end_age}**{close} | {style}{readings[i]}{close} |")
        else:
            lines.append(f"| Ciclul {i} | {cycle_start}–{cycle_end} | {start_age}–{end_age} | {readings[i]} |")
    return "\n".join(lines)


def spirit_code_table(day: int, month: int) -> str:
    def zone_class(code: int) -> str:
        if 0 <= code <= 13:
            return "spirit-zone-love"
        if 14 <= code <= 26:
            return "spirit-zone-reason"
        if 27 <= code <= 39:
            return "spirit-zone-material"
        return "spirit-zone-gifts"

    romans = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    lines = ["| Ziua | " + " | ".join(romans) + " |", "| --- | " + " | ".join(["---:"] * 12) + " |"]
    for d in range(1, 32):
        vals = []
        for m in range(1, 13):
            if d > month_lengths[m - 1]:
                vals.append("")
                continue
            code = 55 - d - 2 * m
            if d == day and m == month:
                cell = f'<span class="spirit-cell-highlight">{code}</span>'
            else:
                cell = f'<span class="{zone_class(code)}">{code}</span>'
            vals.append(cell)
        lines.append(f"| {d} | " + " | ".join(vals) + " |")
    return "\n".join(lines)


def spirit_stage_table(substage: int) -> str:
    rows = [
        '<table class="stage-table">',
        '<colgroup><col style="width:7%"><col style="width:22%"><col style="width:8%"><col style="width:18%"><col style="width:45%"></colgroup>',
        '<thead><tr><th>Etapă</th><th>Descriere etapă</th><th>Subetapă</th><th>Lecție</th><th>Descriere subetapă</th></tr></thead>',
        '<tbody>',
    ]
    data = [
        ("stage-love", "1", "Înțelegere și stabilizare", 4, [
            (1, "Început de cale", "Înțeleg cine sunt și ce am de făcut pe pământ."),
            (2, "Interacțiune", "Înțeleg cine sunt și ce am de făcut în raport cu alte persoane."),
            (3, "Căutarea echilibrului", "Înțeleg echilibrul dintre centru și margini, dintre apropiere și mișcare."),
            (4, "Stabilitate", "Stabilizez tot ce am înțeles până acum."),
        ]),
        ("stage-reason", "2", "Experimentare și manifestare", 4, [
            (5, "Schimbare", "Experimentez și învăț ce a rămas de lucrat, dar altfel decât până acum."),
            (6, "Prelucrarea karmei", "Balansez, prelucrez ce am acumulat și creez teren stabil pentru o nouă etapă."),
            (7, "Depășirea obstacolelor", "Sunt pregătit pentru experiențe mai intense și învăț să nu fug de ele."),
            (8, "Succesul", "Culeg roadele a ceea ce am învățat și mă manifest responsabil."),
        ]),
        ("stage-material", "3", "Finalizare și orientare către ceilalți", 4, [
            (9, "Finalizarea", "Închei ce ține de mine, ca să pot privi dincolo de mine."),
            (10, "Norocul", "Învăț să primesc, să colaborez și să las viața să mă așeze în contexte potrivite."),
            (11, "Slujirea", "Îi slujesc pe alții prin experiența și maturitatea acumulată."),
            (12, "Sacrificiul", "Învăț diferența dintre dăruire conștientă și pierdere de sine."),
        ]),
        ("stage-gifts", "4", "Examen", 1, [
            (13, "Examenul", "Integrez lecția și trec spre un nivel nou de înțelegere."),
        ]),
    ]
    for stage_class, stage, description, span, items in data:
        for index, (number, lesson, subdescription) in enumerate(items):
            classes = stage_class + (" current-row" if number == substage else "")
            first_cells = f'<td rowspan="{span}">{stage}</td><td rowspan="{span}">{description}</td>' if index == 0 and span > 1 else ""
            if span == 1:
                first_cells = f"<td>{stage}</td><td>{description}</td>"
            current_cell = ' class="current-substage"' if number == substage else ""
            rows.append(f'<tr class="{classes}">{first_cells}<td{current_cell}>{number}</td><td{current_cell}>{lesson}</td><td{current_cell}>{subdescription}</td></tr>')
    rows.append("</tbody>")
    rows.append("</table>")
    return "\n".join(rows)


def copy_tarot() -> None:
    src_dir = ROOT / "vault/tarot/imagini"
    for _, src, dest in ARCANA.values():
        shutil.copyfile(src_dir / src, OUT_DIR / dest)
    shutil.copyfile(src_dir / "10-Wheel of Fortune.jpg", OUT_DIR / "tarot-10-roata-norocului-aplicabilitate-profesionala.jpg")
    shutil.copyfile(src_dir / "18-The Moon.jpg", OUT_DIR / "tarot-18-luna-obstacol-profesional.jpg")


def main() -> None:
    report = run_report()
    partner_report = run_partner_report()
    partner_path = partner_report["capitolul_2_formule_calcule_tabele_grafice"]["2.1_codul_numerologic_personal_data_nasterii"]
    if partner_path["vibratia_interioara"]["calcul"]["rezultat"] != 8:
        raise RuntimeError("Vibrația interioară a lui Victor nu corespunde calculului relațional așteptat.")
    copy_tarot()
    date_mod = load_generator(MATRIX_GENERATOR, "matrix_date_skill")
    name_mod = load_generator(NAME_MATRIX_GENERATOR, "matrix_name_skill")
    subprocess.run([sys.executable, str(MATRIX_GENERATOR), "--name", "Vulcu Dominic Ioan", "--birth-date", "08.05.2021", "--output", str(OUT_DIR / "matrita-datei-vulcu-dominic-ioan.svg")], check=True)
    subprocess.run([sys.executable, str(NAME_MATRIX_GENERATOR), "--name", "Vulcu Dominic Ioan", "--birth-date", "08.05.2021", "--output", str(OUT_DIR / "matrita-numelui-vulcu-dominic-ioan.svg")], check=True)
    subprocess.run([sys.executable, str(SOARTA_GENERATOR), "--name", "Vulcu Dominic Ioan", "--birth-date", "08.05.2021", "--output", str(OUT_DIR / "soarta-si-destin-vulcu-dominic-ioan.svg")], check=True)
    relation_svg = OUT_DIR / "omulet-relatii-vulcu-dominic-ioan-vulcu-victor-daniel.svg"
    relation_png = relation_svg.with_suffix(".png")
    if not relation_svg.is_file() or not relation_png.is_file():
        subprocess.run([
            sys.executable, str(RELATION_GENERATOR),
            "--name-a", "Vulcu Dominic Ioan", "--birth-date-a", "08.05.2021",
            "--name-b", "Vulcu Victor Daniel", "--birth-date-b", "17.03.2023",
            "--output", str(relation_svg), "--png-output", str(relation_png),
        ], check=True)

    calc = report["capitolul_2_formule_calcule_tabele_grafice"]
    base = calc["2.1_codul_numerologic_personal_data_nasterii"]
    matrix = calc["2.2_structura_matriciala"]
    name = calc["2.3_codul_numerologic_personal_al_numelui"]
    cycles = calc["2.4_ciclicitati"]
    prof = calc["2.6_spiritul"]["inclinatii_profesionale"]
    life_lessons = cycles["lectii_de_viata"]["sir_lectii"]
    life_lessons_text = "–".join(map(str, life_lessons))
    life_lessons_calc = f'8 × 5 × 2021 = {cycles["lectii_de_viata"]["produs"]} → ' + ", ".join(map(str, life_lessons))

    text = BASE_MD.read_text(encoding="utf-8")
    replacements = {
        "Vulcu Rebeca Andreea": "Vulcu Dominic Ioan",
        "Rebeca": "Domi",
        "VRA-20200315-v1.00r": PREFIX,
        "VRA-20200315": "VDI-20210508",
        "2020-03-15-VULCU-REBECA-ANDREEA": "2021-05-08-VULCU-DOMINIC-IOAN",
        "15.03.2020": "08.05.2021",
        "2020-03-15": "2021-05-08",
        "08.08.2026": "10.08.2026",
        "matrita-datei-vulcu-rebeca-andreea.svg": "matrita-datei-vulcu-dominic-ioan.svg",
        "matrita-numelui-vulcu-rebeca-andreea.svg": "matrita-numelui-vulcu-dominic-ioan.svg",
        "soarta-si-destin-vulcu-rebeca-andreea.svg": "soarta-si-destin-vulcu-dominic-ioan.svg",
        "tarot-15-diavolul-karma-zilei.jpg": "tarot-08-puterea-karma-zilei.jpg",
        "tarot-13-moartea-karma-calea-destinului.jpg": "tarot-18-luna-karma-calea-destinului.jpg",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    # Înlocuirea prenumelui activ nu trebuie să modifice al doilea prenume.
    text = text.replace("Vulcu Domi Ioan", "Vulcu Dominic Ioan")
    text = re.sub(
        r"\n- Relație analizată:.*",
        "\n- Relație analizată: Vulcu Victor Daniel (Vic), 17.03.2023, masculin, frate",
        text,
    )

    blocks = {
        "P-007": "Rebeca, tu ai vibrația interioară **6**: grijă, responsabilitate, frumusețe, familie și nevoia de armonie. Traseul zilei tale pornește din **15**, unde **1** inițiază, iar **5** caută libertate; împreună ajung la **6**, energia care învață să transforme dorința în ocrotire matură. Arhetipal, această vibrație te apropie de Protector, Vindecător și Creator de spațiu cald. Maturizarea apare când nu confunzi iubirea cu salvarea tuturor, ci înveți să ajuți cu limite clare.",
        "P-008": "Îți dorești apropiere, siguranță afectivă și un mediu în care oamenii se poartă frumos unii cu alții. Ai nevoie de ordine emoțională, de gesturi concrete de grijă și de sentimentul că ceea ce construiești aduce bine cuiva.",
        "P-009": "Te motivează proiectele în care poți îngriji, organiza, înfrumuseța sau repara ceva. O rutină potrivită este să alegi zilnic un gest concret de responsabilitate: să termini, să așezi, să clarifici sau să faci un lucru util pentru spațiul tău.",
        "P-010": "Umbra lui **6** este suprasolicitarea prin grijă, perfecționismul afectiv și tendința de a lua asupra ta emoțiile celorlalți. Când simți că trebuie să repari tot, întreabă-te: «Ce îmi aparține mie și ce trebuie să las celuilalt?»",
        "T-009": '<table class="polarities-table"><tbody><tr><th scope="row">Polarități pozitive</th><td><ul><li>grijă și responsabilitate;</li><li>simț estetic și capacitate de armonizare;</li><li>loialitate față de cei apropiați;</li><li>talent de a crea spații calde și sigure;</li><li>capacitate de a susține și vindeca prin prezență.</li></ul></td></tr><tr><th scope="row">Polarități negative</th><td><ul><li>supraprotecție și control prin grijă;</li><li>vinovăție când alegi pentru tine;</li><li>perfecționism în familie sau relații;</li><li>asumarea problemelor altora;</li><li>nevoie de aprobare afectivă.</li></ul></td></tr><tr><th scope="row">Direcții de dezvoltare</th><td><ul><li>ajută fără să te pierzi;</li><li>pune limite blânde și clare;</li><li>transformă grija în acțiuni concrete;</li><li>acceptă imperfecțiunea oamenilor;</li><li>hrănește și propriile tale nevoi.</li></ul></td></tr></tbody></table>',
        "C-001": "> [!example] Calcul\n> Ziua din data de naștere = **15** → 1 + 5 = **6**",
        "C-002": "> [!example] Calcul\n> Luna din data de naștere = **3**",
        "P-012": "Fiind născută în luna martie, ai rolul social al Comunicatorului, specific vibrației exterioare **3**. Oamenii te pot percepe expresivă, curioasă, jucăușă și capabilă să aduci viață într-un grup. Succesul social vine când mesajul tău rămâne limpede și nu se risipește în prea multe direcții.",
        "P-013": "Rebeca, dacă în interior ești **6**, la exterior oamenii te pot percepe ca pe un **3**. Înăuntru cauți armonie și grijă; în exterior poți apărea veselă, expresivă și spontană. **6** spune «vreau să fie bine», iar **3** spune «hai să vorbim și să ne bucurăm». Împreună pot face din tine o prezență caldă și luminoasă.",
        "P-013a": "Puntea dintre interior și exterior arată ajustarea dintre responsabilitatea interioară și expresivitatea vizibilă. Ea te ajută să observi când gluma, povestea sau joaca exprimă autentic grija ta și când pot ascunde o nevoie mai profundă de siguranță.",
        "C-002a": "> [!example] Calculul punții interior–exterior\n> |**6** − **3**| = **3**",
        "P-013b": "Rezultatul **3** cere autenticitate prin comunicare. Când spui ce simți simplu și viu, oamenii te pot primi fără ezitare în rolul tău: nu doar ca persoană care are grijă, ci ca om care aduce bucurie, cuvânt și coerență între intenție și gest.",
        "C-003": "> [!example] Calcul\n> Toate cifrele adunate din data de naștere = 1 + 5 + 0 + 3 + 2 + 0 + 2 + 0 = **13** → 1 + 3 = **4**\n>\n> Cifra de interpretare = **4**",
        "P-015": "Rebeca, Destinul compus **4** vine din **13**, o sumă care vorbește despre transformare, efort și reorganizare. Muntele tău de urcat este să construiești ordine, răbdare și rezultate concrete. Vibrația ta interioară **6** vrea armonie, iar Destinul **4** cere structură: când cele două lucrează împreună, poți deveni un om de încredere, capabil să așeze lucrurile frumos și temeinic.",
        "C-004": "> [!example] Calcul\n> Data nașterii: 15.03.2020 → data compactă = **15032020**  \n> N1 = 1 + 5 + 0 + 3 + 2 + 0 + 2 + 0 = **13**  \n> N2 = 1 + 3 = **4**  \n> N3 = 13 − (2 × 1) = **11**  \n> N4 = 1 + 1 = **2**  \n> Șir complet = 15032020 + 13 + 4 + 11 + 2 = **15032020134112**",
        "G-002": date_mod.build_html_component("Vulcu Rebeca Andreea", "15.03.2020")[0],
        "P-035": "**Căsuța 1.** Ai **4** apariții. Psihicul și inițiativa sunt puternice: poți porni lucruri, poți insista și poți apăra ceea ce simți că este important. Umbra este încăpățânarea; maturizarea apare când fermitatea ta rămâne deschisă la dialog.",
        "P-036": "**Căsuța 2.** Ai **3** apariții. Emoțiile, comunicarea și colaborarea sunt foarte active. Simți repede atmosfera și poți răspunde intuitiv oamenilor. Ai grijă să nu absorbi prea mult din starea celorlalți; numește ce simți și respiră înainte să reacționezi.",
        "P-037": "**Căsuța 3.** Ai **2** apariții. Relațiile și prelucrarea informației circulă bine, cu schimb în ambele sensuri. Poți învăța prin dialog și poveste. Când apar prea multe idei, alege firul central și du-l până la capăt.",
        "P-038": "**Căsuța 4.** Ai **1** apariție. Corpul, organizarea și rezultatele concrete sunt disponibile ca bază. Sprijină-le prin program, somn, mișcare și reguli simple, fără să transformi ordinea în presiune.",
        "P-039": "**Căsuța 5.** Ai **1** apariție. Libertatea, curajul și stima de sine sunt prezente într-o formă accesibilă. Energia se maturizează când alegi experiențe noi cu măsură și nu confunzi libertatea cu fuga de responsabilitate.",
        "P-040": "**Căsuța 6.** Nu ai apariții. Iubirea ca ocrotire, pragmatismul și administrarea concretă sunt energii conservate. Ele se construiesc prin exemple bune, ritualuri de familie, buget, responsabilități împărțite și exercițiul de a transforma grija în gesturi vizibile.",
        "P-041": "**Căsuța 7.** Nu ai apariții. Observația profundă, răbdarea și înțelepciunea sunt energii conservate. Ele se activează prin studiu, liniște, natură, rugăciune, întrebări bune și oameni care te ajută să nu răspunzi doar din impuls.",
        "P-042": "**Căsuța 8.** Nu ai apariții. Puterea, responsabilitatea socială și performanța sunt energii conservate. Ele se construiesc prin limite, asumare, relație sănătoasă cu banii și contexte în care înveți să folosești autoritatea fără teamă.",
        "P-043": "**Căsuța 9.** Nu ai apariții. Inteligența mentală, compasiunea largă și transformarea sunt conservate. Nu înseamnă lipsă, ci o zonă care are nevoie de hrană: lectură, modele bune, experiențe de sens și timp pentru a înțelege imaginea de ansamblu.",
        "G-004": wellbeing(matrix["scara_bunastarii"]),
        "P-018": "Darurile și nevoile se citesc din căsuțele cu cel puțin **2** cifre: la tine sunt **1**, **2** și **3**. Darul lui **1** este inițiativa, dar nevoia lui este să fie ascultată fără să devină încăpățânare. Darul lui **2** este sensibilitatea, iar nevoia lui este siguranța emoțională. Darul lui **3** este comunicarea, iar nevoia lui este să primească spațiu de exprimare și finalizare.",
        "P-019": "Scara bunăstării arată că treapta dominantă este vectorul **123, Energie**, cu **16**. El este susținut de vectorul **258, Social** și de vectorul **357, Scopuri**, ambele cu **11**. Pentru tine, împlinirea pornește din energie, emoție și comunicare, apoi are nevoie să fie orientată spre oameni și scopuri clare. Bunăstarea materială apare când energia de început primește disciplină și direcție.",
        "C-009": "> [!example] Calcul\n> Rebeca = 25 → 2 + 5 = **7**",
        "P-021": "Numărul activ **7** aduce în comportamentul tău curent observație, profunzime și nevoie de înțelegere. Poți părea uneori retrasă sau selectivă, dar în interior cauți sens. Resursa este discernământul; umbra este izolarea.",
        "C-009a": "> [!example] Calcul\n> Vocalele numelui = 3 + 3 + 5 + 5 + 1 + 1 + 5 + 5 + 1 = **29** → 2 + 9 = **11** → 1 + 1 = **2**",
        "P-021c": "Numărul intim **2** caută apropiere, blândețe și siguranță afectivă. Te hrănesc relațiile în care poți simți că ești ascultată. Umbra este sensibilitatea la respingere; maturizarea apare când spui ce ai nevoie fără să aștepți ca ceilalți să ghicească.",
        "C-008": "> [!example] Calcul\n> Vulcu = 16 → 1 + 6 = **7**",
        "P-020": "Numărul ereditar **7** aduce o memorie de neam legată de discreție, observație, credință, studiu și căutarea adevărului. Poți moșteni nevoia de a înțelege lucrurile în profunzime și de a nu te mulțumi cu aparențele.",
        "P-022b": "Numărul ereditar karmic citește numele de familie în intervalul simbolic **1–22** și evidențiază o lecție arhetipală a neamului. El arată ce tipar cere înțelegere și maturizare, astfel încât resursele moștenite să fie folosite fără repetarea automată a limitelor trecutului.",
        "C-005": "> [!example] Calcul în intervalul 1–22\n> Vulcu = **16**\n>\n> Arcana neamului = **16 — Turnul**",
        "T-013": f'<table class="tarot-profile-table"><tbody><tr><td>Index: {PREFIX}-G-003<br>![Arcana 16 — Turnul](tarot-16-turnul-numarul-ereditar-karmic.jpg)<div class="tarot-image-caption"><em>Arcana <strong>16</strong> — Turnul</em></div></td><td><ul><li><strong>Resursă moștenită:</strong> capacitatea de a vedea rapid ce nu mai este stabil, ce este construit pe frică, aparență sau compromis și ce are nevoie să fie reclădit pe baze reale.</li><li><strong>Manifestare:</strong> curajul de a schimba structuri vechi, reguli, obiceiuri sau tipare de familie atunci când ele nu mai susțin viața, adevărul și dezvoltarea.</li><li><strong>Umbră:</strong> teamă de pierdere, reacții bruște, rezistență la schimbare sau tendința de a păstra o formă cunoscută până când presiunea devine prea mare și lucrurile se rup singure.</li><li><strong>Maturizare:</strong> construirea unei siguranțe interioare care nu depinde doar de forme vechi, ci de adevăr, responsabilitate, ordine nouă și capacitatea de a reconstrui pas cu pas după o clarificare.</li></ul></td></tr></tbody></table>',
        "P-022c": "Numărul ereditar karmic **16**, asociat Turnului, vorbește despre o moștenire în care adevărul cere uneori restructurare. Domi, poți duce mai departe resursa de a vedea unde o construcție nu mai este sinceră, unde regulile vechi nu mai ajută și unde este nevoie de o bază mai curată. Turnul nu înseamnă distrugere de dragul distrugerii, ci momentul în care ceea ce era fragil, fals sau prea rigid trebuie dat jos pentru ca viața să poată fi așezată mai drept. În linia de neam, această arcană poate arăta familii care au trecut prin schimbări bruște, rupturi, mutări, pierderi de siguranță sau situații în care a fost nevoie să se reconstruiască de la zero.",
        "P-022d": "Umbra lui **16** este să te agăți de forme care par sigure, dar nu mai susțin viața, sau să reacționezi prea brusc atunci când ceva se clatină. Maturizarea apare când accepți schimbarea ca pe o șansă de curățare, nu ca pe o pedeapsă, și când înveți să reconstruiești cu răbdare: spui adevărul, pui limite, alegi ce merită păstrat și renunți la ceea ce nu mai are temelie. Astfel, Turnul devine o forță de eliberare: nu mai lasă neamul să trăiască în structuri vechi doar pentru că sunt cunoscute, ci deschide drumul spre o siguranță mai sinceră, construită conștient.",
        "C-010": "> [!example] Calcul\n> Consoanele numelui = **42** → 4 + 2 = **6**",
        "P-022": "Numărul de realizare **6** te face vizibilă ca persoană caldă, atentă și responsabilă. Ceilalți pot simți la tine dorința de armonie și capacitatea de a ține împreună oamenii sau lucrurile.",
        "P-022a": "Vibrația exterioară **3** și Numărul de realizare **6** formează o combinație afectivă: **3** exprimă, iar **6** ocrotește. Imaginea ta devine matură când comunicarea nu rămâne doar joacă, ci devine grijă concretă.",
        "C-012": "> [!example] Calcul\n> Vulcu = 7, Rebeca = 7, Andreea = 3 → 7 + 7 + 3 = **17** → 1 + 7 = **8**",
        "P-024": "Numărul de exprimare **8** susține responsabilitatea, administrarea resurselor și curajul de a ocupa un loc vizibil. Poți crește în roluri în care înveți să folosești puterea cu maturitate.",
        "P-024a": "Armonizarea dintre Numărul de exprimare **8** și Destinul **4** cere structură, disciplină și rezultate verificabile. **8** vrea impact, iar **4** cere fundație; împreună pot construi autoritate sănătoasă.",
        "C-011": "> [!example] Calcul\n> Vulcu: 4 + 3 + 3 + 3 + 3 = **16** → **7**\n>\n> Rebeca: 9 + 5 + 2 + 5 + 3 + 1 = **25** → **7**\n>\n> Andreea: 1 + 5 + 4 + 9 + 5 + 5 + 1 = **30** → **3**\n>\n> Codul literelor numelui = **43333952531149551**\n>\n> Codul numerologic personal al numelui = **8**",
        "G-002a": name_mod.build_html_component("Vulcu Rebeca Andreea", "15.03.2020")[0],
        "P-023": "Comparând pătratul datei cu pătratul numelui, energiile comune valide sunt **1**, **2**, **3**, **4** și **5**. Numele susține inițiativa, sensibilitatea, comunicarea, ordinea și curajul de a experimenta.",
        "P-023b": "Prin **1**, numele îți întărește pornirea; prin **2**, îți susține relaționarea; prin **3**, îți amplifică expresia; prin **4**, adaugă formă; prin **5**, deschide libertatea. Aceste energii există și în matricea nativă, deci pot fi interpretate ca sprijin real.",
        "P-023c": "Energiile **6**, **7**, **8** și **9** nu apar în matricea datei. Chiar dacă numele poate conține unele dintre ele, lectura personală se păstrează pe ceea ce are suport nativ și pe ceea ce se construiește conștient prin experiență.",
        "P-185": "În tabel, poziția ta este la ziua **15** și luna **III**, unde apare codul **34**.",
        "T-017": spirit_code_table(15, 3),
        "P-186": "Rebeca, codul **34** te așază în zona **Materială**. Spiritul tău învață prin construcție, responsabilitate, rezultate, administrarea resurselor și transformarea potențialului interior în ceva concret și folositor.",
        "T-018": "| Zona | Interval cod | Nivel simbolic | Teme principale |\n| --- | --- | --- | --- |\n| <span class=\"zone-badge zone-love\">Iubire</span> | 1-13 | 0-2.500 ani | relații, emoții, atașamente, compasiune, vulnerabilitate |\n| <span class=\"zone-badge zone-reason\">Rațiune</span> | 14-26 | 2.500-5.000 ani | logică, discernământ, structură, analiză, minte |\n| <span class=\"zone-badge zone-material\">Material</span> | 27-39 | 5.000-7.500 ani | bani, construcție, putere, manifestare, responsabilitate |\n| <span class=\"zone-badge zone-gifts\">Haruri</span> | 40-52 | 7.500-10.000 ani | înțelepciune, haruri spirituale, ghidare, serviciu, intuiție |",
        "T-019": spirit_stage_table(8),
        "P-192": "Subetapa ta este **8 — Succesul**. Lecția este să culegi roadele a ceea ce ai învățat și să transformi manifestarea în responsabilitate, nu în presiune.",
        "C-003d": "> [!example] Calcul\n> Vârsta la naștere = (34 × 189) - 189 = **6237**\n>\n> Vârsta actuală = 6237 + 6 = **6243**",
        "P-197": "Ghidarea practică este să înveți să construiești încet, cu răbdare. Când ai o idee sau o dorință, întreabă-te ce formă concretă îi dai: timp, spațiu, regulă, obiect, economie, responsabilitate.",
        "P-009a": "În lectura numerologică, ziua de naștere arată o încărcătură karmică simbolică. Fiind născută în ziua de **15**, te afli în zona de aproximativ **80%** și lucrezi cu Arcana **15 — Diavolul**.",
        "C-001a": "> [!example] Calcul\n> Ziua nașterii = **15**\n>\n> Arcana karmică = **15 — Diavolul**\n>\n> Intervalul 10–19 = karma împlinită **spre 80%**",
        "G-001a": "![Arcana 15 — Diavolul, karma din ziua de naștere](tarot-15-diavolul-karma-zilei.jpg)\n\n_Arcana **15** — Diavolul. Karma din ziua de naștere_",
        "P-009b": "Diavolul vorbește simbolic despre atașamente, dorință, magnetism și felul în care puterea instinctivă poate fi folosită matur. Resursa este vitalitatea; umbra este dependența de plăcere, control sau validare.",
        "P-009b1": "Umbra karmei **15** poate apărea ca încăpățânare, posesivitate ori legare de lucruri care oferă confort rapid. Nu este un verdict, ci o imagine despre locul unde libertatea interioară cere atenție.",
        "P-009b2": "Cheia este să alegi conștient: ce te hrănește cu adevărat și ce doar te ține prinsă. Când dorința primește limită și discernământ, devine energie de creație.",
        "C-002b": "> [!example] Calcul\n> Luna nașterii = **3**\n>\n> Karma lunii = **responsabilitate în comunicare și relaționare**",
        "P-013d": "Luna **3** îți cere să lucrezi cu expresia, cuvântul și felul în care creezi legături. Umbra este risipirea sau folosirea cuvântului ca evitare; maturizarea apare când spui adevărul cu blândețe.",
        "P-015a": "Karma din Calea Destinului păstrează suma compusă a tuturor cifrelor datei. Pentru tine citim amprenta **13**, nu doar Destinul redus la **4**.",
        "C-003a": "> [!example] Calcul\n> 1 + 5 + 0 + 3 + 2 + 0 + 2 + 0 = **13**\n>\n> Karma din Calea Destinului = **13**\n>\n> Intervalul 10–19 = categoria karmică **spre 80%**",
        "P-015b": "Rebeca, Calea karmică **13** este asociată simbolic cu Arcana **13 — Moartea**. Ea vorbește despre transformare, încheierea formelor vechi și capacitatea de a renaște mai matur. Nu indică un eveniment fatal, ci o lecție de curățare și reorganizare.",
        "G-001b": "![Arcana 13 — Moartea. Karma din Calea Destinului 13](tarot-13-moartea-karma-calea-destinului.jpg)\n\n_Arcana **13** — Moartea. Karma din Calea Destinului_",
        "P-015c": "Codul Spiritului **34**, zona Materială și subetapa **8 — Putere** arată că direcția ta de maturizare trece prin folosirea responsabilă a resurselor. Karma zilei **15**, Karma lunii **3** și Calea karmică **13** te învață să transformi dorința, cuvântul și schimbarea în construcție concretă.",
        "C-013": "> [!example] Calcul\n> Calea Destinului: **13**\n> Destin compus: **4**\n> Limita Pinaclului 1: 36 - **4** = **32**\n> Pinacluri: **0–32** -> **33–42** -> **43–52** -> **53+**",
        "T-003": "| Pinaclu | Interval | Oportunitate | Provocare | Interpretare |\n| --- | --- | ---: | ---: | --- |\n| Pinaclul 1 | 0–32 | 9 | 3 | Învățare prin compasiune, finalizări și comunicare matură. |\n| Pinaclul 2 | 33–42 | 1 | 2 | Inițiativă nouă, cu lecția cooperării. |\n| Pinaclul 3 | 43–52 | 1 | 1 | Autonomie puternică, cu atenție la ego și încăpățânare. |\n| Pinaclul 4 | 53+ | 7 | 1 | Înțelepciune, cercetare și autonomie interioară. |",
        "P-024c": "**Pinaclul 1: până la 32 de ani**, Oportunitatea **9** îți deschide compasiunea, imaginația și înțelegerea largă, iar Provocarea **3** cere să comunici limpede, fără risipire.",
        "P-024d": "**Pinaclul 2: între 33 și 42 de ani**, Oportunitatea **1** aduce inițiativă și autonomie. Provocarea **2** cere cooperare, ascultare și răbdare în relații.",
        "P-024e": "**Pinaclul 3: între 43 și 52 de ani**, Oportunitatea **1** se repetă și cere curaj. Provocarea **1** te învață să conduci fără orgoliu și să începi fără să forțezi.",
        "P-024f": "**Pinaclul 4: de la 53 de ani până la sfârșitul vieții**, Oportunitatea **7** favorizează studiul, credința, înțelepciunea și profunzimea. Provocarea **1** cere autonomie matură.",
        "P-024g": "Rebeca, la 6 ani te afli în Pinaclul **1**, cu Oportunitatea **9** și Provocarea **3**. Pentru etapa copilăriei, asta se traduce prin imaginație, sensibilitate și nevoia de a învăța să exprimi ce simți în cuvinte simple.",
        "P-025": "Zona ta de confort este între oportunitățile **4.5** și provocările **1.75**: te simți bine când există structură, dar ai nevoie și de libertate controlată pentru inițiativă și explorare.",
        "C-006": "> [!example] Sinteză\n> Soartă: **1503 × 2020 = 3036060**  \n> Destin: **1513 × 2121 = 3209073**",
        "P-025a": "Pe linia **Sorții**, traseul **3–0–3–6–0–6–0** aduce comunicare, pauze de acumulare și responsabilitate afectivă. Pe linia **Destinului**, traseul **3–2–0–9–0–7–3** adaugă cooperare, transformare, introspecție și expresie. Pentru tine, Rebeca, citirea aceasta arată că bucuria de a vorbi și de a crea are nevoie de răbdare, înțelegere și timp interior.",
        "P-025b": "La **6 ani**, graficul se citește încă în zona de formare: familia, ritmul zilnic și oamenii apropiați sunt mai importante decât interpretarea unor decizii personale majore. Energia perioadei susține învățarea prin cuvânt, joacă, reguli simple și siguranță emoțională.",
        "P-025c": "Când apar valori precum **0** în șiruri, le citim prudent: ele nu adaugă o direcție numerologică separată, ci pot amplifica sau deschide potențialul cifrei de lângă ele. Pentru tine, pauzele dintre cifre arată că lucrurile au nevoie de timp de așezare.",
        "P-025d": "Sfatul pentru etapa actuală este blând și concret: ritm stabil, somn, activități creative, povești, reguli explicate și mult spațiu pentru a spune ce simți. Astfel, energia lui **3** devine comunicare, iar Destinul **4** începe să se formeze ca siguranță.",
        "P-026b": "**Șirul anilor importanți interiori:** " + " → ".join(map(str, cycles["ani_importanti_interiori_exteriori"]["interiori"])) + ".",
        "P-026d": "**Șirul anilor importanți exteriori:** " + " → ".join(map(str, cycles["ani_importanti_interiori_exteriori"]["exteriori"])) + ".",
        "P-026e": "Rebeca, prima suprapunere importantă este în **2024**, când schimbarea interioară și cea exterioară apar împreună. Următorul nod mare este **2032**. În astfel de ani, familia și mediul pot observa mai clar ce se maturizează în tine.",
        "P-028": f"Rebeca, lecțiile de viață se recalculează din produsul zilei, lunii și anului nașterii: **{life_lessons_calc}**. Șirul **{life_lessons_text}** se repetă de-a lungul vieții. Fiecare revenire îți oferă ocazia să trăiești mai matur cele două teme ale sale:\n\n- **9** — compasiune, imaginație, încheierea etapelor, desprindere și capacitatea de a privi experiențele dintr-o perspectivă mai largă;\n- **0** — un spațiu de acumulare și deschidere care nu adaugă o direcție numerologică separată, ci amplifică lecția din jur și cere răbdare, receptivitate și timp pentru integrare.\n\nRepetarea lui **9** întărește tema sensibilității și a înțelegerii, iar cele trei poziții de **0** arată că ritmul tău include pauze importante de așezare. Lecția nu este să grăbești sensul, ci să lași experiența să se clarifice înainte de a merge mai departe.",
        "T-008": lesson_table(life_lessons),
        "P-028a": "În **2026**, Rebeca, lecția ta este **0**. Ea nu aduce o temă numerică separată, ci deschide un timp de acumulare, receptivitate și integrare, în care ceea ce înveți are nevoie să se așeze înainte de a deveni acțiune. Lecția **0** se întâlnește cu anul personal **1**, care deschide începuturi: familia te poate ajuta cel mai bine oferindu-ți experiențe noi în pași simpli, un ritm stabil și libertatea de a observa înainte de a răspunde. Astfel, începutul nu devine grabă, ci curiozitate susținută de siguranță.",
        "T-007": cycle9_table(),
        "P-027": "Rebeca, în 2026 ești în primul ciclu de 9 ani, în **Anul 7** ca vârstă și cu an personal **1** în raportul calculatorului. Este o etapă de începuturi, învățare și formare a încrederii prin experiențe simple, repetate și sigure.",
        "T-015": cycle12_table(),
        "P-027a": "În 2026 ești în Ciclul de 12 ani **1**, intervalul 2020–2031. Este o etapă de bază: corp, familie, ritm, prime reguli, limbaj emoțional și sentimentul că lumea poate fi un loc sigur.",
    }
    blocks.update({
        "P-007": "Domi, tu ai vibrația interioară **8**: forță, responsabilitate, putere de organizare și nevoie de rezultate concrete. Fiind născut în ziua **8**, această energie apare direct, concentrată, fără trepte intermediare: simți repede unde există autoritate, regulă, limită sau miză și ai tendința să verifici prin faptă ce funcționează. Arhetipal, vibrația te apropie de Administrator, Strateg și Constructor de rezultate. În manifestarea luminoasă poți fi hotărât, protector, rezistent și atent la dreptate; în umbră poți răspunde prin control, încăpățânare, competiție sau presiune. Maturizarea lui **8** nu înseamnă să renunți la putere, ci să înveți să o folosești calm, proporțional și responsabil, astfel încât fermitatea ta să ofere siguranță, nu teamă.\n\nOptul simbolizează forțele materiale și este numărul reacției și al justiției echilibrante. Este vibrația cea mai puternică, căreia cu greu te poți sustrage. Este cifra puterii și a bogăției, dar și a aprecierii lumești. Este caracterizată de Saturn, cel responsabil nu doar cu problemele, ci mai ales cu probele. Aceasta este cifra succesului și a insuccesului material. Optul este puternic, dur și practic, cu profil de om de afaceri sau politician norocos, dar drumul vieții lui nu este niciodată simplu. Nu este capabil să acumuleze bani la fel de ușor și fără griji precum o face Treiul. Cariera lui ține de luptă, eforturi, pericole și muncă grea. Este foarte calculat și planificat. Câteodată lasă impresia că nu face niciun pas fără a urmări ceva, vreun câștig oarecare. Este capabil să atingă un succes uimitor, dar, pentru că iubește viața periculoasă și plină de tot felul de peripeții, se poate lovi și de posibilitatea eșecului ca o consecință a alegerilor sale.",
        "P-008": "Îți dorești să simți că poți influența concret lucrurile, că efortul produce un rezultat și că regulile au sens. Ai nevoie de respect, de repere clare și de libertatea de a încerca singur, dar și de adulți care îți arată că adevărata putere include răbdare, grijă și capacitatea de a repara.",
        "P-009": "Te motivează provocările vizibile, jocurile cu scop, sarcinile în care poți construi, ordona, conduce sau măsura progresul. O rutină potrivită este să primești responsabilități mici și reale, cu început și sfârșit clar, astfel încât energia lui **8** să asocieze autoritatea cu consecvența și rezultatul cu munca bine așezată.",
        "P-010": "Teama din umbra lui **8** este pierderea controlului, neputința sau situația în care altcineva decide fără să explice. Atunci poți deveni rigid, provocator ori foarte competitiv. Întrebarea de maturizare este: «Cum pot rămâne puternic fără să forțez?»; răspunsul se construiește prin alegere, negociere, reguli constante și acceptarea faptului că vulnerabilitatea nu anulează puterea.",
        "T-009": '<table class="polarities-table"><tbody><tr><th scope="row">Polarități pozitive</th><td><ul><li>forță și rezistență;</li><li>simț al responsabilității;</li><li>capacitate de organizare și administrare;</li><li>curaj în fața provocărilor;</li><li>orientare spre rezultate concrete.</li></ul></td></tr><tr><th scope="row">Polarități negative</th><td><ul><li>control și rigiditate;</li><li>competiție excesivă;</li><li>nerăbdare față de ritmul celorlalți;</li><li>teamă de slăbiciune;</li><li>presiune pusă pe sine sau pe ceilalți.</li></ul></td></tr><tr><th scope="row">Direcții de dezvoltare</th><td><ul><li>folosește puterea pentru a proteja;</li><li>leagă autoritatea de responsabilitate;</li><li>învață să negociezi, nu doar să impui;</li><li>măsoară progresul fără comparație permanentă;</li><li>acceptă ajutorul și ritmul construcției.</li></ul></td></tr></tbody></table>',
        "C-001": "> [!example] Calcul\n> Ziua din data de naștere = **8**",
        "C-002": "> [!example] Calcul\n> Luna din data de naștere = **5**",
        "P-012": "Fiind născut în luna mai, ai rolul social al Exploratorului, specific vibrației exterioare **5**. Oamenii te pot percepe curios, mobil, spontan și dornic să încerci. Ai nevoie de varietate și libertate de mișcare, iar succesul social apare când această energie primește repere suficient de clare încât curiozitatea să nu devină risipire.",
        "P-013": "Domi, dacă în interior ești **8**, la exterior oamenii te pot percepe ca pe un **5**. Înăuntru cauți control, eficiență și rezultat; în exterior poți apărea liber, jucăuș, schimbător și atras de noutate. **8** spune «vreau să stăpânesc situația», iar **5** spune «vreau să explorez». Împreună pot forma un om curajos și adaptabil, capabil să transforme experiența în competență.",
        "P-013a": "Puntea dintre interior și exterior arată ajustarea dintre forța interioară și imaginea mobilă pe care o văd ceilalți. Ea te ajută să observi când libertatea exprimă autentic curajul tău și când schimbarea devine o metodă de a evita o limită, o regulă sau un rezultat care cere răbdare.",
        "C-002a": "> [!example] Calculul punții interior–exterior\n> |**8** − **5**| = **3**",
        "P-013b": "Rezultatul **3** cere autenticitate prin comunicare. Când spui limpede ce vrei, ce te deranjează și ce soluție propui, forța lui **8** și libertatea lui **5** devin mai ușor de înțeles și de acceptat. Maturizarea punții înseamnă coerență între intenție, cuvânt și faptă, astfel încât să poți ocupa un rol fără să îl impui.",
        "C-003": "> [!example] Calcul\n> Toate cifrele adunate din data de naștere = 0 + 8 + 0 + 5 + 2 + 0 + 2 + 1 = **18** → 1 + 8 = **9**\n>\n> Cifra de interpretare = **9**",
        "P-015": "Domi, Calea Destinului **18** reunește inițiativa lui **1** cu forța, responsabilitatea și raportarea la putere a lui **8**; suma lor conduce la cifra de interpretare **9**, care cere perspectivă largă, compasiune, finalizare și capacitatea de a transforma experiența în înțelegere. Cantitativ, traseul este complet: toate cifrele datei formează **18**, Destinul se reduce o singură dată la **9**, iar cifra de interpretare rămâne **9**. Calitativ, muntele tău de urcat este să treci de la puterea concentrată asupra rezultatului imediat la o putere care vede ansamblul și efectul asupra oamenilor. Vibrația interioară **8** vrea eficiență și control, în timp ce Destinul **9** cere generozitate, desprindere și încheiere matură. Când lucrează împreună, poți deveni un om capabil să organizeze resurse pentru un scop mai mare decât interesul de moment; în umbră, poți oscila între control și dezamăgire, iar maturizarea apare când termini ceea ce începi, accepți imperfecțiunea și folosești forța pentru a construi ceva util și altora.\n\nPentru ca energia lui **9** să se exprime la nivel înalt, ai nevoie de un ideal care depășește interesul personal și de sentimentul că ceea ce faci contribuie la binele altora. Egoismul, vanitatea, orgoliul, preocupările mărunte sau atașamentul excesiv față de bani pot îngusta această perspectivă și pot transforma forța ta într-o sursă de nemulțumire ori suferință. În schimb, studiul, reflecția, cultivarea vieții interioare și participarea la proiecte cu sens îți oferă spațiul potrivit pentru o minte activă, idei originale, idealism și o imaginație bogată. Lecția independenței nu înseamnă izolare, ci capacitatea de a te adapta singur și apoi de a intra deschis în lume, comunicând și dând mai departe ceea ce ai înțeles. **7** și **9** au în comun căutarea sensului, însă o trăiesc în direcții diferite: **7** se retrage pentru a cerceta și a aprofunda, în timp ce **9** se întoarce către oameni pentru a încheia, a împărtăși și a transforma cunoașterea în faptă. De aceea, Destinul tău **9** cere ca experiența acumulată să nu rămână doar în interior, ci să capete o formă folositoare în exterior.",
        "C-004": "> [!example] Calcul\n> Data nașterii: 08.05.2021 → data compactă = **08052021**  \n> N1 = 0 + 8 + 0 + 5 + 2 + 0 + 2 + 1 = **18**  \n> N2 = 1 + 8 = **9**  \n> N3 = 18 − (2 × 8) = **2**  \n> N4 = **2**  \n> Șir complet = 08052021 + 18 + 9 + 2 + 2 = **0805202118922**",
        "G-002": date_mod.build_html_component("Vulcu Dominic Ioan", "08.05.2021")[0],
        "P-035": "**Căsuța 1.** Reprezintă psihicul, voința, inițiativa și felul în care îți afirmi propria direcție. Ai **2** apariții în căsuța cifrei **1**, configurație care poate fi înțeleasă simbolic drept un sistem psihic cu două sensuri de circulație: poți primi și acumula energie din mediul apropiat, dar o poți și transmite mai departe către ceilalți. Tendința de a pune propriul interes pe primul loc există într-o formă moderată și destul de ușor de recunoscut. De multe ori poți observa singur acest lucru și îl poți admite fără să îl trăiești ca pe o acuzație. În relații funcționezi puternic după principiul reciprocității: răspunzi la respect prin respect, la ajutor prin disponibilitate și la ostilitate prin opoziție, chiar dacă răspunsul tău poate lua o altă formă decât gestul primit.\n\nCele două apariții ale lui **1** pot crea și un dialog interior intens. O parte din tine poate susține o alegere, în timp ce alta îi vede imediat limitele sau riscurile. Din exterior, această negociere lăuntrică nu este întotdeauna vizibilă, de aceea ceilalți pot înțelege greu ce hotărâre pregătești. Când cele două impulsuri nu ajung repede la un acord, poți rămâne în îndoială și poți avea nevoie de o încurajare, de un termen clar sau de un reper venit din afară. Într-un context familiar poți fi foarte sigur și îndrăzneț, iar într-o situație asemănătoare, dar percepută ca mai complicată, poți deveni prudent, rezervat ori nehotărât. Această alternanță nu arată lipsă de forță, ci consumul produs de confruntarea dintre două răspunsuri posibile. Maturizarea căsuței înseamnă să îți acorzi o pauză înainte de decizie, să numești cele două variante și să alegi conștient criteriul după care vei acționa. Astfel, energia psihică rămâne suficient de puternică pentru curaj și inițiativă, fără să fie risipită în conflict interior.",
        "P-036": "**Căsuța 2.** Reprezintă emoțiile, sensibilitatea, comunicarea, bioenergia și capacitatea de colaborare. Ai **4** apariții în căsuța cifrei **2**, configurația **2222**, ceea ce indică simbolic un sistem energetic foarte intens, orientat în cele din urmă spre exterior. Simți repede atmosfera unui loc și poți observa din ton, gesturi sau schimbări subtile când o persoană este liniștită, tensionată ori are nevoie de sprijin. Empatia ta poate influența puternic climatul relațional: prin prezență, cuvinte și atitudine poți amplifica neliniștea, dar poți aduce și calm, încredere și speranță. Această lectură nu descrie o putere medicală sau o modificare fizică a materiei, ci responsabilitatea de a înțelege cât de mult pot conta mesajele și starea pe care le transmiți celorlalți.\n\nFelul în care folosești această sensibilitate depinde de maturitatea ta afectivă și de valorile pe care le cultivi. Cuvintele calde, blânde, motivante și sincere îți așază energia într-o direcție constructivă, în timp ce gândurile ostile, critica repetată sau reacțiile încărcate pot obosi atât persoanele din jur, cât și propriul tău sistem emoțional. Ai nevoie să înveți că empatia nu înseamnă să preiei tot ce simt ceilalți: poți recunoaște o stare fără să devină a ta și poți oferi sprijin fără să porți întreaga povară. Configurația **2222** poate aduce o dorință profundă de plenitudine sufletească și de armonie emoțională. Uneori te poți concentra atât de mult asupra unei stări ideale, încât să nu mai observi bucuria simplă care există deja. Maturizarea acestei căsuțe înseamnă să rămâi receptiv, dar bine delimitat, să folosești cuvântul pentru a încuraja și să primești viața reală cu nuanțele ei, fără să amâni bucuria până când totul devine perfect.",
        "P-037": "**Căsuța 3.** Reprezintă relaționarea, curiozitatea și capacitatea de a primi, organiza și transmite informația. În matricea ta nu există nicio apariție a cifrei **3**, ceea ce descrie simbolic o energie conservată în zona prelucrării logice și a exprimării spontane. Nu înseamnă că îți lipsește inteligența, ci că raționamentul abstract nu este întotdeauna prima cale pe care o alegi. Te simți mai sigur atunci când o activitate este explicată limpede, desfăcută în pași și repetată suficient pentru a deveni familiară. În loc să improvizezi imediat, ai tendința să compari situația nouă cu ceea ce ai trăit deja și să folosești soluții care și-au dovedit utilitatea.\n\nInteresul tău pentru cercetare poate fi selectiv. Nu vei simți nevoia să aprofundezi orice subiect doar de dragul acumulării de informații, însă poți investi multă atenție într-un domeniu care are sens pentru tine și contribuie la dezvoltarea ta. La început poți părea rezervat, lent sau dependent de explicațiile primite din exterior. După o perioadă suficientă de acomodare, exersare și înțelegere a regulilor, această aparentă încetineală se poate transforma într-o capacitate mentală foarte bine organizată. Poți ajunge să impresionezi prin precizie și competență, mai ales într-un domeniu ales cu adevărat din plăcere și aprofundat în timp. Pentru familie și educatori, cheia este să nu grăbească răspunsul și să nu confunde ritmul de pregătire cu lipsa potențialului. Explicațiile concrete, exemplele, repetiția fără critică, întrebările simple și legarea informației de experiențe reale te ajută să construiești această căsuță treptat și temeinic.",
        "P-038": "**Căsuța 4.** Reprezintă corpul fizic, sănătatea, spiritul practic, orientarea spre rezultate concrete, organizarea, cadrul, trăinicia, statornicia și temeinicia. În matricea ta nu ai nicio apariție în căsuța cifrei **4**, ceea ce arată că această energie este conservată: nu o poți accesa întotdeauna când dorești și în aceeași măsură. Pot exista perioade în care te simți foarte sănătos și rezistent, dar și momente în care chiar o răceală ușoară te poate solicita mai mult decât te-ai aștepta. Energia poate oscila între «foarte mult» și «foarte puțin», iar aceeași alternanță se poate vedea în organizare, disciplină și consecvență. Pentru a echilibra această căsuță, te ajută un program stabil și obiceiuri simple, respectate chiar și atunci când nu există presiunea imediată a rezultatului. În etapa copilăriei, sănătatea, somnul, alimentația și mișcarea au nevoie de atenție constantă și de un ritm potrivit corpului tău.",
        "P-039": "**Căsuța 5.** Reprezintă libertatea, stima de sine, curajul, adaptarea, nonconformismul și capacitatea de a ieși din tipare. Ai **1** apariție în căsuța cifrei **5**, ceea ce îți oferă impulsul de a explora și de a încerca o cale proprie. Resursa este flexibilitatea: poți descoperi soluții noi atunci când ai voie să experimentezi și să înveți direct din consecințe. Umbra poate fi confundarea libertății cu lipsa limitelor, schimbarea direcției din impuls sau căutarea permanentă a stimulului nou. Energia se maturizează când alegi singur între câteva opțiuni clare, îți asumi rezultatul și revii la un punct stabil după fiecare explorare.",
        "P-040": "**Căsuța 6.** Reprezintă iubirea ca ocrotire, instinctele, arta, realismul și pragmatismul. Nu ai nicio apariție în căsuța cifrei **6**, de aceea această energie este conservată: nu este disponibilă constant la cerere și se poate manifesta alternativ, foarte intens într-un context și foarte puțin în altul. Poți avea nevoie de exemple concrete pentru a transforma afecțiunea în grijă practică, inspirația în lucru terminat și dorința într-o alegere realistă. Aportul extern vine prin familie, educatori, activități artistice, sarcini potrivite vârstei și contexte în care vezi legătura dintre efort și rezultat. Construiești conștient această energie prin responsabilități mici, rutine repetabile, participare la viața familiei și învățarea diferenței dintre a ocroti și a prelua totul asupra ta.",
        "P-041": "**Căsuța 7.** Nu ai apariții. Observația profundă, răbdarea și înțelepciunea sunt energii conservate. Ele se activează prin studiu, liniște, natură, rugăciune, întrebări bune și oameni care te ajută să nu răspunzi doar din impuls. În copilărie, jocurile de strategie, experimentele simple și timpul oferit pentru a gândi înainte de răspuns pot construi treptat această zonă.",
        "P-042": "**Căsuța 8.** Ai **2** apariții. Puterea, responsabilitatea și performanța sunt active și se potrivesc vibrației tale interioare **8**. Poți înțelege devreme regula și miza; umbra este presiunea, iar direcția practică este să legi privilegiul de responsabilitate și rezultatul de cooperare.",
        "P-043": "**Căsuța 9.** Reprezintă inteligența mentală, memoria, compasiunea, învățarea, finalizarea și capacitatea de transformare. Ai **1** apariție în căsuța cifrei **9**, ceea ce îți oferă acces la înțelegerea de ansamblu și la legarea experiențelor într-o concluzie. Poți învăța bine atunci când informația are sens, este asociată unei povești și poate fi folosită într-o situație reală. Umbra apare când imaginea mare te face să treci prea repede peste detalii sau când o concluzie intuită nu este verificată. Îți dezvolți această energie prin lectură, conversație, recapitulare, proiecte duse până la capăt și exercițiul de a spune nu doar ce ai înțeles, ci și pe ce observații se bazează.",
        "G-004": wellbeing(matrix["scara_bunastarii"]),
        "P-018": "Darurile și nevoile se citesc din căsuțele cu cel puțin **2** cifre: la tine sunt **1**, **2** și **8**. Darul lui **1** este inițiativa, cu nevoia de a fi ascultat; darul lui **2** este sensibilitatea și colaborarea, cu nevoia de siguranță emoțională; darul lui **8** este puterea de organizare, cu nevoia de reguli drepte și responsabilități reale.",
        "P-019": "Scara bunăstării arată că treapta dominantă este vectorul **258, Social**, cu **29**, urmat de vectorul **789, Creativitate**, cu **25**, și de diagonala **159, Cariera**, cu **16**. Bunăstarea ta pornește din relația dintre emoție, libertate și putere socială, apoi are nevoie de creativitate și de un scop vizibil. Vectorul **369, Bunăstare materială**, cu **9**, arată că rezultatul concret se construiește conștient prin organizare, pragmatism și finalizare.",
        "P-017": '<div class="parity-chart framed-panel" style="width:100%;max-width:none" role="img" aria-label="Din totalul de 10 cifre, 4 sunt impare și 6 sunt pare."><div class="parity-chart-total">Total: <strong>10</strong> cifre</div><div class="parity-chart-bar"><span class="parity-odd" style="width:40%"><strong>Impare · 4</strong></span><span class="parity-even" style="width:60%"><strong>Pare · 6</strong></span></div></div>\n\nÎn șirul complet ai **6** cifre pare și **4** cifre impare. Cifrele pare susțin capacitatea de a primi, de a procesa și de a da mai departe, iar ponderea lor mai mare accentuează receptivitatea și relația cu mediul. Când această receptivitate este suprasolicitată, poate apărea ezitarea; la tine, cele **4** cifre impare păstrează suficient impuls pentru inițiativă, iar echilibrul se construiește când alegerea este urmată de un pas concret.',
        "C-009": "> [!example] Calcul\n> Domi = 23 → 2 + 3 = **5**",
        "P-021": "Numărul activ **5** aduce în comportamentul tău curiozitate, mobilitate, adaptare și nevoie de libertate. Poți intra repede în experiențe noi și înveți bine prin încercare; resursa este flexibilitatea, iar umbra este risipirea sau refuzul rutinei.",
        "C-009a": "> [!example] Calcul\n> Vocalele numelui = 3 + 3 + 6 + 9 + 9 + 9 + 6 + 1 = **46** → 4 + 6 = **10** → 1 + 0 = **1**",
        "P-021c": "Numărul intim **1** caută autonomie, inițiativă și sentimentul că poți începe din propria voință. Te hrănesc alegerile reale și încurajarea efortului; umbra este izolarea prin «fac singur», iar maturizarea apare când independența știe și să ceară ajutor.",
        "C-008": "> [!example] Calcul\n> Vulcu = 16 → 1 + 6 = **7**",
        "P-020": "Numărul ereditar **7** aduce o memorie de neam legată de discreție, observație, credință, studiu și căutarea adevărului. Poți moșteni nevoia de a înțelege lucrurile în profunzime și de a nu te mulțumi cu aparențele.",
        "C-005": "> [!example] Calcul în intervalul 1–22\n> Vulcu = **16**\n>\n> Arcana neamului = **16 — Turnul**",
        "P-022c": "Numărul ereditar karmic **16**, asociat Turnului, vorbește despre o moștenire în care adevărul cere uneori restructurare. Domi, poți duce mai departe resursa de a vedea unde o construcție nu mai este sinceră, unde regulile vechi nu mai ajută și unde este nevoie de o bază mai curată. Turnul nu înseamnă distrugere de dragul distrugerii, ci momentul în care ceea ce era fragil, fals sau prea rigid trebuie dat jos pentru ca viața să poată fi așezată mai drept. În linia de neam, această arcană poate arăta familii care au trecut prin schimbări bruște, rupturi, mutări, pierderi de siguranță sau situații în care a fost nevoie să se reconstruiască de la zero.",
        "P-022d": "Umbra lui **16** este să te agăți de forme care par sigure, dar nu mai susțin viața, sau să reacționezi prea brusc atunci când ceva se clatină. Maturizarea apare când accepți schimbarea ca pe o șansă de curățare, nu ca pe o pedeapsă, și când înveți să reconstruiești cu răbdare: spui adevărul, pui limite, alegi ce merită păstrat și renunți la ceea ce nu mai are temelie. Astfel, Turnul devine o forță de eliberare: nu mai lasă neamul să trăiască în structuri vechi doar pentru că sunt cunoscute, ci deschide drumul spre o siguranță mai sinceră, construită conștient.",
        "C-010": "> [!example] Calcul\n> Consoanele numelui = **31** → 3 + 1 = **4**",
        "P-022": "Numărul de realizare **4** te face vizibil ca persoană practică, ordonată și capabilă să transforme o intenție în structură. Ceilalți pot vedea seriozitate și perseverență; umbra este rigiditatea, iar maturizarea cere reguli simple, utile și adaptabile.",
        "P-022a": "Vibrația exterioară **5** și Numărul de realizare **4** creează un dialog între libertate și ordine: **5** explorează, iar **4** fixează. Imaginea ta devine matură când noutatea primește un pas concret de finalizare.",
        "C-012": "> [!example] Calcul\n> Vulcu = 7, Dominic = 4, Ioan = 3 → 7 + 4 + 3 = **14** → 1 + 4 = **5**",
        "P-024": "Numărul de exprimare **5** susține adaptarea, comunicarea, mișcarea și învățarea prin experiență. Poți crește în roluri în care există varietate și contact cu lumea, cu condiția să construiești continuitate și criterii clare de finalizare.",
        "P-024a": "Armonizarea dintre Numărul de exprimare **5** și Destinul **9** cere libertate pusă în slujba unei perspective mai largi. **5** aduce experiența, iar **9** îi cere sens, compasiune și încheiere; împreună pot transforma curiozitatea în înțelegere folositoare.",
        "C-011": "> [!example] Calcul\n> Vulcu: 4 + 3 + 3 + 3 + 3 = **16** → **7**\n>\n> Dominic: 4 + 6 + 4 + 9 + 5 + 9 + 3 = **40** → **4**\n>\n> Ioan: 9 + 6 + 1 + 5 = **21** → **3**\n>\n> Numărul de exprimare = **5**\n>\n> Codul literelor numelui = **4333346495939615**\n>\n> Codul numerologic personal al numelui = **43333464959396155**",
        "G-002a": name_mod.build_html_component("Vulcu Dominic Ioan", "08.05.2021")[0],
        "P-023": "Comparând pătratul datei cu pătratul numelui, energiile comune valide sunt **1**, **5** și **9**. Numele susține inițiativa, libertatea și capacitatea de a transforma experiența în înțelegere.",
        "P-023b": "Prin **1**, numele îți întărește pornirea; prin **5**, amplifică adaptarea și curajul; prin **9**, susține perspectiva și compasiunea. Aceste energii există și în matricea nativă, deci pot fi interpretate ca sprijin real.",
        "P-023c": "Energiile **3**, **4** și **6** apar în nume, dar nu au suport în matricea datei și nu le tratăm ca resurse personale. În schimb, energiile native **2** și **8**, nesusținute de nume, rămân reale și se maturizează conștient prin relații, limite și experiență.",
        "P-185": "În tabel, poziția ta este la ziua **8** și luna **V**, unde apare codul **37**.",
        "T-017": spirit_code_table(8, 5),
        "P-186": "Domi, codul **37** te așază în zona **Materială**. Spiritul tău învață prin construcție, responsabilitate, rezultate, administrarea resurselor și transformarea potențialului interior în ceva concret și folositor.",
        "T-019": spirit_stage_table(11),
        "P-192": "Subetapa ta este **11 — Slujirea**. Lecția este să îi susții pe ceilalți prin experiența și maturitatea acumulată, fără să transformi responsabilitatea în sacrificiu sau control.",
        "C-003d": "> [!example] Calcul\n> Vârsta la naștere = (37 − 1) × 189 = **6804**\n>\n> Vârsta actuală = 6804 + 5 = **6809**",
        "P-197": "Ghidarea practică este să înveți că puterea devine valoroasă când produce ceva folositor. Când ai o idee sau o dorință, întreabă-te ce formă concretă îi dai: timp, spațiu, regulă, obiect, economie, responsabilitate și ajutor oferit la momentul potrivit.",
        "P-009a": "În lectura numerologică, ziua de naștere arată o încărcătură karmică simbolică. Fiind născut în ziua de **8**, te afli în zona de aproximativ **100%** și lucrezi cu Arcana **8 — Puterea**.",
        "C-001a": "> [!example] Calcul\n> Ziua nașterii = **8**\n>\n> Arcana karmică = **8 — Puterea**\n>\n> Intervalul 1–9 = karma împlinită **spre 100%**",
        "G-001a": "![Arcana 8 — Puterea, karma din ziua de naștere](tarot-08-puterea-karma-zilei.jpg)\n\n_Arcana **8** — Puterea. Karma din ziua de naștere_",
        "P-009b": "În plan karmic simbolic, cifra **8** poate vorbi despre memoria unei relații puternice cu autoritatea, influența și dreptul de a hotărî pentru ceilalți. În expresia dezechilibrată, această poziție ar fi putut fi folosită prin presiune, orgoliu, intimidare sau control. Nu citim aici obligatoriu o forță fizică, ci orice formă prin care voința unei persoane ajunge să limiteze libertatea alteia: psihologic, social, financiar, afectiv ori sexual. Această imagine este o temă arhetipală de lucru, nu o afirmație verificabilă despre o existență anterioară.",
        "P-009b1": "Arcana **8 — Puterea** schimbă accentul de la simpla posesie a forței la felul în care aceasta este condusă. Leul reprezintă instinctul, impulsul, pasiunea și reacția agresivă, iar figura care îl îmblânzește sugerează o autoritate bazată pe calm, răbdare și echilibru interior. Adevărata putere nu apare atunci când instinctul este distrus sau reprimat, ci atunci când energia lui este recunoscută, orientată și folosită conștient.",
        "P-009b2": "Lecția actuală a combinației **8 — Puterea** este să înveți că poți fi ferm fără să domini. Controlul se poate transforma în protecție, agresivitatea în curaj, orgoliul în demnitate, iar forța brută în stăpânire de sine. Pentru Domi, maturizarea începe prin reguli drepte, alegeri potrivite vârstei, acceptarea unui «nu» explicat și responsabilități în care puterea produce siguranță pentru el și pentru cei din jur. Scopul nu este micșorarea forței, ci educarea ei până când devine o resursă interioară lucidă și responsabilă.",
        "C-002b": "> [!example] Calcul\n> Luna nașterii = **5**\n>\n> Karma lunii = **responsabilitate în libertate, schimbare și experiență**",
        "P-013d": "În lectura karmică simbolică, luna nașterii poate descrie o temă de învățare în relația cu mama: acceptare, iertare, ajutor și iubire. Dacă mama nu este prezentă, tema se poate manifesta și printr-o persoană apropiată care îndeplinește un rol matern. Relația cu mama biologică rămâne totuși un reper interior important, chiar atunci când apropierea concretă nu este posibilă. Ideea unei legături dintr-o existență anterioară este folosită aici ca limbaj spiritual și arhetipal, nu ca fapt care poate fi demonstrat și nici ca motiv pentru a atribui vină copilului.\n\nPentru Domi, luna **5** arată că maturizarea acestei relații trece prin libertate cu responsabilitate, adaptare, comunicare sinceră și acceptarea schimbării. Pot exista etape în care nevoia lui de explorare se întâlnește cu nevoia mamei de siguranță și apar tensiuni, dar acestea nu sunt o sentință. Recomandarea nu este să suporte pasiv orice situație și nici să accepte un comportament care îl rănește. Lecția este să recunoască realitatea relației, să învețe treptat iertarea fără anularea limitelor, să exprime afecțiunea și să ofere ajutor potrivit vârstei. A o ajuta pe mamă să strălucească înseamnă să contribuie prin respect, sinceritate, cooperare și bucurie, nu să devină responsabil pentru starea sau împlinirea ei.\n\nPentru părinții acestui spirit, direcția sănătoasă este să ușureze tema printr-un mediu sigur, consecvent și deschis dialogului. Iertarea nu trebuie cerută doar copilului, ci modelată de adulți prin repararea conflictelor, renunțarea la reproșuri și separarea greșelii de valoarea persoanei. Mama poate susține energia lui **5** oferindu-i alegeri potrivite vârstei și libertate în limite clare, iar ceilalți adulți pot proteja relația de alianțe, comparații sau poveri emoționale care nu îi aparțin. Astfel, sensul karmic nu devine pedeapsă, ci o ocazie comună de a transforma tensiunea în înțelegere, apropiere și iubire matură.",
        "P-015a": "Karma din Calea Destinului arată ritmul karmic al vieții și felul în care se pot manifesta șansele, obstacolele și ajutoarele de-a lungul drumului. Calculul pornește de la toate cifrele datei de naștere, iar rezultatul se păstrează neredus complet. Astfel, nu citim numai cifra de interpretare **9**, ci mai ales amprenta compusă **18**, deoarece ea păstrează nuanța karmică pe care reducerea ar pierde-o.",
        "C-003a": "> [!example] Calcul\n> 0 + 8 + 0 + 5 + 2 + 0 + 2 + 1 = **18**\n>\n> Karma din Calea Destinului = **18**\n>\n> Intervalul 10–19 = categoria karmică **1**",
        "P-015b": "**Luna.** Domi, Karma din Calea Destinului **18** este asociată simbolic cu Arcana **18 — Luna (The Moon)** și descrie un drum pe care spiritul întrupat poate întâlni unele ajutoare, dar mai multe obstacole «prescrise» pentru împlinirea destinului. Documentația spune că această cale păstrează din alte vieți atât bile negre, cât și bile albe. Imaginea probabilă a unei vieți anterioare, în care te-ai fi ocupat de vrăjitorie și/sau de activități infracționale, trebuie citită simbolic, nu ca fapt verificabil despre trecutul tău și nici ca etichetă aplicată copilului. În viața actuală, interpretarea predefinită arată posibilitatea succesului în afaceri, dar avertizează și asupra atracției către activități necinstite sau infracționale. Numărul **18** este descris ca un număr al ruinărilor, al distrugerii și al pericolelor, iar calea poate include riscuri asociate violenței, sinuciderii sau accidentelor provocate de cauze exterioare; acestea sunt avertismente simbolice, nu predicții și nu descriu un viitor inevitabil. În umbra acestei valori, sursa enumeră răzbunarea, răutatea, duritatea, scandalurile în familie, despotismul, agresivitatea, opoziția permanentă, revolta și convingerea că scopul scuză mijloacele; sunt tipare posibile ale interpretării, nu trăsături fixe ale lui Domi. În plan ezoteric, aceeași sursă spune că este lipsit de sens să te ocupi de magie sau ocultism, deoarece legătura cu aceste lumi este considerată închisă total. Lecția de discernământ este să citești toate aceste imagini ca avertismente asupra alegerilor și mijloacelor folosite, nu ca pe o sentință despre cine ești sau despre ceea ce urmează să trăiești.",
        "G-001b": "![Arcana 18 — Luna. Karma din Calea Destinului 18](tarot-18-luna-karma-calea-destinului.jpg)\n\n_Arcana **18** — Luna. Karma din Calea Destinului_",
        "P-015c": "Codul Spiritului **37**, zona Materială și subetapa **11 — Slujirea** arată că direcția ta de maturizare trece prin folosirea responsabilă a puterii și a resurselor în beneficiul celorlalți. Karma zilei **8**, Karma lunii **5** și Calea karmică **18** te învață să unești forța, libertatea și imaginația într-o construcție concretă, lucidă și folositoare.",
        "C-013": "> [!example] Calcul\n> Calea Destinului: **18**\n> Destin compus: **9**\n> Limita Pinaclului 1: 36 - **9** = **27**\n> Pinacluri: **0–27** → **28–37** → **38–47** → **48+**",
        "T-003": "| Pinaclu | Interval | Oportunitate | Provocare | Interpretare |\n| --- | --- | ---: | ---: | --- |\n| Pinaclul 1 | 0–27 | 4 | 3 | Construirea unei baze stabile, cu lecția comunicării limpezi. |\n| Pinaclul 2 | 28–37 | 4 | 3 | Consolidare, ordine și răbdare, fără rigiditate sau risipire. |\n| Pinaclul 3 | 38–47 | 8 | 0 | Putere și responsabilitate, cu spațiu de integrare și deschidere. |\n| Pinaclul 4 | 48+ | 1 | 0 | Inițiativă matură și autonomie, cu receptivitate față de sens. |",
        "P-024c": "**Pinaclul 1: intervalul 0–27 de ani**, Oportunitatea **4** îți deschide ordinea, disciplina și construcția, iar Provocarea **3** cere să comunici clar și să nu risipești energia în prea multe direcții.",
        "P-024d": "**Pinaclul 2: intervalul 28–37 de ani**, Oportunitatea **4** continuă tema fundației și a rezultatelor verificabile. Provocarea **3** cere expresie matură, creativitate cu structură și dialog.",
        "P-024e": "**Pinaclul 3: intervalul 38–47 de ani**, Oportunitatea **8** aduce putere, administrare și impact. Provocarea **0** cere receptivitate și timp de integrare, fără să forțezi o direcție înainte ca sensul ei să fie clar.",
        "P-024f": "**Pinaclul 4: intervalul 48+**, Oportunitatea **1** favorizează inițiativa și autonomia. Provocarea **0** te învață să păstrezi deschiderea, răbdarea și contactul cu un sens mai larg.",
        "P-024g": "Domi, la 5 ani te afli în Pinaclul **1**, cu Oportunitatea **4** și Provocarea **3**. Pentru copilărie, aceasta înseamnă ritm, reguli simple, lucru concret și mult spațiu pentru exprimarea prin cuvânt, joc și poveste.",
        "P-025": "Zona ta de confort este între oportunitățile **4,25** și provocările **1,5**: te simți bine când există structură și rezultat, dar ai nevoie să exersezi comunicarea, flexibilitatea și răbdarea față de etapele intermediare.",
        "C-006": "> [!example] Sinteză\n> Soartă: **1626905**  \n> Destin: **3849615**",
        "P-025a": "Pe linia **Sorții**, traseul **1–6–2–6–9–0–5** aduce inițiativă, responsabilitate, cooperare, compasiune, pauze de acumulare și schimbare. Pe linia **Destinului**, traseul **3–8–4–9–6–1–5** adaugă expresie, putere, structură, perspectivă, grijă, inițiativă și libertate. Pentru tine, Domi, citirea arată că forța și curiozitatea au nevoie de ordine, comunicare și un scop care îi include și pe ceilalți.",
        "P-025b": "La **5 ani**, graficul se citește încă în zona de formare: familia, ritmul zilnic și oamenii apropiați sunt mai importante decât interpretarea unor decizii personale majore. Energia perioadei susține învățarea prin mișcare, responsabilități mici, reguli clare și siguranță emoțională.",
        "P-025c": "Când apar valori precum **0** în șiruri, le citim prudent: ele nu adaugă o direcție numerologică separată, ci pot amplifica sau deschide potențialul cifrei de lângă ele. Pentru tine, pauza din linia Sorții cere timp de integrare înaintea unei schimbări.",
        "P-025d": "Sfatul pentru etapa actuală este concret: ritm stabil, mișcare, jocuri de construcție, alegeri limitate și responsabilități pe măsura vârstei. Astfel, puterea lui **8** devine autocontrol, libertatea lui **5** devine explorare, iar Destinul **9** începe să se formeze ca grijă pentru ansamblu.",
        "P-026b": "**Șirul anilor importanți interiori:** " + " → ".join(map(str, cycles["ani_importanti_interiori_exteriori"]["interiori"])) + ".",
        "P-026d": "**Șirul anilor importanți exteriori:** " + " → ".join(map(str, cycles["ani_importanti_interiori_exteriori"]["exteriori"])) + ".",
        "P-026e": "Domi, prima suprapunere importantă este în **2026**, când schimbarea interioară și cea exterioară apar împreună. Următorul nod comun este **2068**. În astfel de ani, mediul poate observa mai clar ce se maturizează în tine.",
        "P-028": f"Domi, lecțiile de viață se recalculează din produsul zilei, lunii și anului nașterii: **{life_lessons_calc}**. Șirul **{life_lessons_text}** se repetă de-a lungul vieții și păstrează fiecare poziție:\n\n- **8** — putere, responsabilitate, administrarea resurselor și folosirea matură a autorității;\n- **0** — spațiu de acumulare și deschidere, care nu adaugă o direcție numerică separată, ci amplifică lecția din jur;\n- **4** — ordine, disciplină, corp, răbdare și construcția unei fundații concrete.\n\nRepetarea lui **8** întărește tema puterii responsabile, iar cele două poziții de **0** cer pauze de integrare. Lecția **4** leagă potențialul de rutină și rezultat.",
        "T-008": lesson_table(life_lessons, start_year=2021),
        "P-028a": "În **2026**, Domi, lecția ta este **8**. Ea cere să înveți folosirea responsabilă a puterii, a regulii și a resurselor, iar anul personal **5** aduce mișcare și noutate. Familia te poate ajuta oferindu-ți libertate în limite clare, sarcini mici și posibilitatea de a vedea efectul concret al alegerilor tale.",
        "T-007": cycle9_table(2021),
        "P-027": "Domi, în 2026 ești în primul ciclu de 9 ani, la vârsta de **5** ani și cu an personal **5**. Este o etapă de explorare, adaptare și formare a încrederii prin experiențe simple, repetate și sigure.",
        "T-015": cycle12_table(2021),
        "P-027a": "În 2026 ești în Ciclul de 12 ani **1**, intervalul 2021–2032. Este etapa de bază: corp, familie, ritm, prime reguli, limbaj emoțional și sentimentul că lumea poate fi un loc sigur.",
        "L-003": "- Nume: Vulcu Victor Daniel\n- Data nașterii: 17.03.2023\n- Tipul relației: frați",
        "G-006": "![Omulețul relațiilor pentru Vulcu Dominic Ioan și Vulcu Victor Daniel](omulet-relatii-vulcu-dominic-ioan-vulcu-victor-daniel.png)",
        "C-007": "> [!example] Calcul relațional\n> Realizare împreună: 8 + 8 = 16 → 1 + 6 = **7**  \n> De rezolvat împreună: |8 − 8| = **0**",
        "P-029": "Domi, tu intri în relația cu fratele tău prin vibrația interioară **8**, iar Vic tot prin **8**. Amândoi aduceți forță, voință, reacție la autoritate și nevoie de a simți că aveți un cuvânt de spus. Tu, ca frate mai mare, poți aduce experiență și inițiativă, iar Vic poate răspunde cu aceeași fermitate. Lumina acestei asemănări este loialitatea și capacitatea de a vă apăra reciproc; umbra este competiția pentru control, mai ales când unul dintre voi simte că regulile nu sunt drepte.",
        "P-030": "Realizarea împreună **7** arată că relația crește prin observație, învățare, jocuri care cer strategie și respectarea spațiului personal. Tema de rezolvat **0** nu înseamnă lipsa unei lecții, ci o distanță numerică nulă între motivațiile voastre de bază: vă puteți înțelege foarte repede, dar vă puteți și oglindi încăpățânarea. Podul se construiește când adulții nu vă compară, nu fixează unul în rolul conducătorului și pe celălalt în rolul celui care urmează, ci vă oferă alegeri distincte, timp individual și obiective comune scurte.",
        "P-031": "În datele voastre, Domi aduce șirul **8–5–2–0–2–1**, iar Vic șirul **1–7–3–2–0–2–3**. Aveți în comun energiile **0**, **1** și **2**: potențialul de acumulare, inițiativa și sensibilitatea relațională. Domi aduce suplimentar **5** și **8**, adică explorare și putere, iar Vic aduce **3** și **7**, adică expresie și observație. Împreună aveți Foc **3**, Apă **4**, Aer **3**, Pământ **1** și potențialul lui **0** de **2** ori. Apa dominantă face legătura sensibilă la ton și atmosferă, iar Pământul redus cere ritualuri și repere concrete. Zonele absente se construiesc intenționat și pot primi aport extern: program vizual, mișcare și reguli repetate pentru stabilitate **(4)**; gesturi de grijă, activități practice și responsabilități împărțite pentru ocrotire și pragmatism **(6)**; povești, natură, voluntariat în familie și exercițiul de a încheia ce ați început pentru perspectivă și compasiune **(9)**. Activitățile comune scurte, urmate de timp separat, vă ajută să păstrați apropierea fără să transformați asemănarea în competiție.",
        "C-014": "> [!example] Calcul\n> DA: luna 5 + suma cifrelor anului 5 = **10**\n> NU: suma tuturor cifrelor datei = **18**",
        "T-016": f'<table class="tarot-profile-table professional-tarot-table"><thead><tr><th>Aplicabilitate profesională DA</th><th>Aplicabilitate profesională NU</th></tr></thead><tbody><tr><td>![Arcana 10 — Roata Norocului](tarot-10-roata-norocului-aplicabilitate-profesionala.jpg)<div class="tarot-image-caption"><em>Arcana <strong>10</strong> — Roata Norocului</em></div></td><td>![Arcana 18 — Luna](tarot-18-luna-obstacol-profesional.jpg)<div class="tarot-image-caption"><em>Arcana <strong>18</strong> — Luna</em></div></td></tr><tr><td><div class="idx">Index: {PREFIX}-P-046a</div><p><strong>Roata Norocului</strong> descrie o resursă profesională legată de mișcare, ritm și capacitatea de a recunoaște momentul potrivit. Energia ei nu promite un noroc pasiv, ci arată că poți observa schimbarea și te poți repoziționa înainte ca o etapă să se închidă. Când ești pregătit, ceea ce pare întâmplare poate deveni o oportunitate folosită inteligent.</p><p>În activitate, această Arcană susține domenii dinamice, coordonarea, negocierea, mobilitatea, comerțul, tehnologia, proiectele cu etape succesive și situațiile în care trebuie să adaptezi rapid un plan. Vibrația interioară <strong>8</strong> adaugă simțul rezultatului, iar dublul <strong>5</strong> din numărul activ și exprimare aduce curiozitate și flexibilitate. Împreună, ele pot forma un organizator capabil să lucreze bine cu schimbarea.</p><p>Umbra lui <strong>10</strong> este încrederea excesivă în context, nerăbdarea și trecerea la următoarea experiență înainte ca munca prezentă să fie încheiată. Pentru Domi, resursa se educă prin jocuri cu reguli schimbătoare, proiecte scurte duse până la capăt, responsabilități măsurabile și exercițiul de a pregăti două variante înainte de a decide. Astfel, adaptarea nu devine instabilitate, iar șansa este întâmpinată prin competență.</p></td><td><div class="idx">Index: {PREFIX}-P-046b</div><p><strong>Luna</strong> arată obstacolul confuziei, al idealizării și al reacției conduse de teamă sau de o imaginație neclarificată. Ea nu indică lipsă de talent, ci momente în care sensibilitatea poate amesteca faptele cu presupunerile. Când atmosfera este tensionată, Domi poate simți foarte mult și poate avea nevoie de timp pentru a deosebi ceea ce știe de ceea ce doar bănuiește.</p><p>Configurația <strong>2222</strong> amplifică receptivitatea la ton, stare și relație, iar Destinul <strong>9</strong> aduce imaginație și idealism. Profesional, umbra poate apărea ca ezitare, amânare, teamă de evaluare, alegerea unei direcții după impresii sau pierderea criteriului concret într-un val emoțional. În același timp, Luna poate deveni resursă pentru artă, poveste, imagine, psihologie simbolică și orice activitate în care sensibilitatea este susținută de metodă.</p><p>Antidotul practic este verificarea realității: întrebări clare, informații confirmate, sarcini împărțite în pași, termene vizibile și discuții calme despre ceea ce provoacă neliniște. Rutina corpului, somnul, ordinea și recapitularea ajută imaginația să lucreze în favoarea lui. Când învață să numească emoția fără să o confunde cu adevărul complet, Domi poate transforma nesiguranța în intuiție disciplinată și inspirație aplicată.</p></td></tr></tbody></table>',
        "P-046": "Pentru Domi, aplicabilitatea profesională este încă un potențial care se formează prin mediu, educație și experiențe potrivite vârstei. Împreună, Arcanele **10** și **18** descriu lecția de a te mișca odată cu schimbarea fără să pierzi contactul cu realitatea: Roata Norocului oferă mobilitate și simțul momentului, iar Luna cere claritate emoțională, verificarea faptelor și disciplinarea imaginației. Când flexibilitatea primește structură, iar sensibilitatea primește limbaj, potențialul profesional devine adaptare matură, creativitate și capacitatea de a lua decizii bine pregătite.",
    })
    for suffix, body in blocks.items():
        text = replace_block(text, suffix, body)

    constructor_body = "Neamul **16** este Neamul Constructorilor, al celor care construiesc lucruri mari și repară ceea ce s-a distrus. Cei născuți dintr-un astfel de neam pot avea o atracție firească spre construcții, reparații, unelte, mecanisme și orice activitate în care ceva trebuie ridicat, refăcut sau consolidat. Nu este obligatoriu ca sarcina ta să fie să construiești case, însă este bine să fii deschis atunci când vine vorba despre reînnoirea casei, a apartamentului, a spațiului în care trăiești sau a lucrurilor care cer să fie reparate. În linia acestui neam există simbolic taine ale construcției transmise din generație în generație: priceperea de a mânui unelte, de a înțelege structuri, de a ridica ceva util și de a reconstrui acolo unde alții văd doar ruină."
    constructor_marker = f"Index: {PREFIX}-P-022e"
    if constructor_marker in text:
        text = replace_block(text, "P-022e", constructor_body)
    else:
        anchor = f"Index: {PREFIX}-P-022c"
        if anchor not in text:
            raise RuntimeError("Nu am găsit poziția pentru interpretarea Neamul Constructorilor.")
        text = text.replace(anchor, f"{constructor_marker}\n\n{constructor_body}\n\n{anchor}", 1)

    professional_intro = f"""Index: {PREFIX}-P-046i

Aplicabilitatea profesională se citește aici prin două direcții complementare. Valoarea **DA** arată tipul de energie care poate susține manifestarea, alegerile și mediile în care potențialul lucrează firesc. Valoarea **NU** nu interzice o profesie și nu anunță un eșec, ci descrie obstacolul interior care trebuie cunoscut și educat. Pentru un copil, aceste Arcane nu fixează o meserie, ci oferă repere despre joc, învățare, disciplină, relația cu schimbarea și felul în care adulții pot sprijini formarea unor aptitudini sănătoase."""
    text, count = re.subn(
        rf"(Index: {PREFIX}-SUB-029\n\n### 10\.1\. Aplicabilitate profesională\n\n)(?=Index: {PREFIX}-C-014)",
        lambda match: match.group(1) + professional_intro + "\n\n",
        text,
        count=1,
    )
    if count != 1:
        raise RuntimeError("Introducerea aplicabilității profesionale nu a fost inserată.")

    element_section = f"""<div class="element-analysis framed-panel"><div class="element-indexes"><span>Index: {PREFIX}-T-012</span><span>Index: {PREFIX}-P-044</span></div><div class="element-chart"><div class="element-bars" role="img" aria-label="Distribuția elementelor: Foc 4, Pământ 2, Aer 0, Apă 4"><div class="element-bar"><div class="element-bar-label"><span>Foc</span><strong>4</strong></div><div class="element-bar-track"><span class="element-bar-fill element-foc" style="width:100%"></span></div></div><div class="element-bar"><div class="element-bar-label"><span>Pământ</span><strong>2</strong></div><div class="element-bar-track"><span class="element-bar-fill element-pamant" style="width:50%"></span></div></div><div class="element-bar"><div class="element-bar-label"><span>Aer</span><strong>0</strong></div><div class="element-bar-track"><span class="element-bar-fill element-aer" style="width:0%"></span></div></div><div class="element-bar"><div class="element-bar-label"><span>Apă</span><strong>4</strong></div><div class="element-bar-track"><span class="element-bar-fill element-apa" style="width:100%"></span></div></div></div></div><ul class="element-definitions"><li><strong>Focul</strong> este esența vieții, a duhului și a spiritului care animă și activează.</li><li><strong>Pământul</strong> este esența materiei dense, a solidarității și a fertilității, care hrănește și dă formă.</li><li><strong>Aerul</strong> este esența inteligenței conceptuale care eliberează și stimulează.</li><li><strong>Apa</strong> este esența emoțiilor și a fecundității, maleabilă, flexibilă și orientată spre acumulare.</li></ul></div>

Index: {PREFIX}-P-045

Temperamentul tău este mixt, cu Focul și Apa la câte **4** apariții, Pământul la **2**, iar Aerul conservat. Ai simultan energie de pornire și sensibilitate puternică; echilibrul vine când emoțiile primesc limbaj, corpul primește ritm, iar ideile sunt explicate simplu și repetate prin experiență."""
    text, count = re.subn(rf'<div class="element-analysis framed-panel">.*?(?=\nIndex: {PREFIX}-SUB-016)', element_section + "\n\n", text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError("Secțiunea elementelor nu a fost înlocuită.")

    conclusion = f"""Index: {PREFIX}-CAP-015

## Capitolul 11. Concluzii

Index: {PREFIX}-SUB-030

### 11.1. Carieră și bani

Index: {PREFIX}-P-032

Domi, cariera și banii se vor citi mai târziu prin felul în care energia ta de **8** învață să folosească puterea responsabil, iar Destinul **9** transformă rezultatul personal într-un lucru folositor și altora. În matricea ta, vectorul **258, Social**, cu **29**, este cel mai puternic, urmat de vectorul **789, Creativitate**, cu **25**, și diagonala **159, Cariera**, cu **16**. Potențialul este mare, dar organizarea corpului, pragmatismul și finalizarea trebuie construite prin educație, exemple și responsabilități potrivite vârstei.

Index: {PREFIX}-P-032a

Numărul activ **5** și Numărul de exprimare **5** dublează nevoia de mișcare, experiență, comunicare și varietate. Numărul de realizare **4** cere însă structură, iar Numărul intim **1** vrea autonomie. În timp, poți funcționa bine în activități dinamice, cu decizie, negociere, organizare, călătorie, tehnică sau coordonare, dacă libertatea primește metodă și fiecare început are un criteriu clar de finalizare.

Index: {PREFIX}-P-032b

Arcana neamului **16 — Turnul** și Neamul Constructorilor spun că moștenirea ta cere construcții sincere, repararea lucrurilor deteriorate și curajul de a reface o structură pe baze reale. În plan practic, mediul potrivit este stabil, dar nu rigid: reguli clare, unelte și proiecte potrivite vârstei, adevăr spus pe înțelesul tău și libertatea de a reconstrui când ceva nu mai funcționează.

Index: {PREFIX}-P-032c

În perioada copilăriei, Pinaclul **1** aduce Oportunitatea **4** și Provocarea **3**. Ai nevoie de ritm, reguli simple, jocuri de construcție și contexte în care poți spune ce simți. Când energia este organizată și emoțiile primesc cuvinte, forța ta devine productivă; când ești grăbit sau controlat fără explicație, pot apărea opoziție, rigiditate ori risipire.

Index: {PREFIX}-P-032d

Pe scurt, direcția ta este să unești puterea lui **8**, libertatea lui **5**, perspectiva lui **9** și structura lui **4**. Când vei crește, activitatea potrivită va fi una în care poți explora, decide, organiza și transforma resursele într-un rezultat util, fără să pierzi empatia, jocul și capacitatea de cooperare.

Index: {PREFIX}-P-032e

Roata Norocului, Arcana profesională **10**, adaugă adaptare și simțul momentului, iar Luna, Arcana obstacolului **18**, cere verificarea faptelor și disciplinarea imaginației. Potențialul se maturizează când schimbarea nu este lăsată la întâmplare, ci este întâmpinată cu pregătire, pași măsurabili și continuitate.

Index: {PREFIX}-P-032f

În relația cu banii, combinația dintre **8**, **5** și **9** cere un echilibru atent. **8** vrea control și rezultat, **5** este atras de experiență și noutate, iar **9** poate pune sensul sau generozitatea înaintea acumulării. Educația financiară potrivită începe devreme prin alegeri simple, economisire pentru un obiectiv, diferența dintre dorință și nevoie și legarea fiecărui privilegiu de o responsabilitate. Astfel, banii devin o resursă administrată, nu o măsură a valorii personale.

Index: {PREFIX}-P-032g

Profilul profesional nu trebuie grăbit către o etichetă. În copilărie, este mai important să observăm în ce contexte Domi își păstrează interesul, cum răspunde la reguli și ce fel de rezultat îl face să revină cu plăcere. Construcția, strategia, mișcarea, proiectele practice, povestea și activitățile în care poate organiza ori îmbunătăți ceva oferă teren bun de explorare. Direcția matură va apărea acolo unde puterea de a decide se întâlnește cu utilitatea și cu respectul pentru oameni.

Index: {PREFIX}-SUB-031

### 11.2. Iubire și relație

Index: {PREFIX}-P-032r

Domi, relația cu Vic are potențialul **7** și se construiește prin învățare, observație, jocuri de strategie și respectarea spațiului personal. Amândoi porniți din vibrația interioară **8**, deci puteți fi foarte loiali și protectori, dar și competitivi când fiecare vrea să conducă. Tu aduci mai vizibil explorarea lui **5** și puterea lui **8**, iar Vic aduce expresia lui **3** și observația lui **7**; împreună puteți transforma energia în curiozitate și competență.

Index: {PREFIX}-P-032s

Tema de rezolvat **0** vă cere deschidere și integrare, nu desemnarea unui câștigător. Relația devine mai sănătoasă când adulții evită comparațiile, vă oferă obiecte și responsabilități proprii, alternează activitățile comune cu timpul separat și vă ajută să spuneți ce simțiți înainte ca forța să devină confruntare. Stabilitatea **(4)**, ocrotirea practică **(6)** și perspectiva largă **(9)** se construiesc prin rutine, proiecte concrete și încheierea împreună a lucrurilor începute.

Index: {PREFIX}-P-032u

Pentru Domi, lecția relațională mai largă este să transforme reciprocitatea lui **11** și intensitatea lui **2222** în cooperare conștientă. Poate răspunde puternic la felul în care este tratat și poate absorbi ușor atmosfera din jur. De aceea are nevoie de adulți care modelează respectul, repararea după conflict și exprimarea directă a nevoilor. Când învață că fermitatea nu exclude blândețea, apropierea nu îi amenință autonomia, iar sensibilitatea nu îl obligă să poarte emoțiile tuturor, relațiile devin o sursă de stabilitate.

Index: {PREFIX}-SUB-040

### 11.3. Momentul prezent

Index: {PREFIX}-P-032t

Domi, în 2026 te afli în primul Pinaclu, cu Oportunitatea **4** și Provocarea **3**, în primul ciclu de 9 ani și în primul ciclu de 12 ani. Anul personal **5** aduce mișcare și explorare, iar Lecția **8** cere responsabilitate și folosirea matură a puterii. Pentru etapa actuală, direcția potrivită este libertatea în limite clare: experiențe noi, mișcare, sarcini concrete, explicații calme și un pas vizibil de încheiere pentru fiecare lucru început.

Index: {PREFIX}-P-032v

Matricea arată o sensibilitate emoțională foarte intensă prin **2222**, alături de două energii de **1** și două de **8**. În prezent, Domi are nevoie simultan să fie ascultat, să poată alege și să întâlnească limite consecvente. Explicațiile lungi oferite în mijlocul unei reacții pot amplifica tensiunea; funcționează mai bine o regulă scurtă, o pauză de reglare și revenirea ulterioară la dialog. Pentru învățare, pașii vizibili, repetiția și legarea informației de experiență sunt mai valoroase decât presiunea pentru răspuns rapid.

Index: {PREFIX}-P-032w

Sinteza momentului prezent este una de construcție: puterea lui **8** are nevoie să devină protecție și responsabilitate, libertatea lui **5** are nevoie de repere, iar Destinul **9** începe să învețe perspectiva asupra celuilalt. Somnul, mișcarea, programul previzibil, jocul liber, sarcinile potrivite vârstei și timpul individual petrecut cu fiecare părinte susțin această așezare. Nu este nevoie ca toate potențialele să fie activate deodată; progresul sănătos apare când o experiență este trăită, numită și încheiată înainte de a deschide alta."""
    text, count = re.subn(rf"Index: {PREFIX}-CAP-015\n.*?(?=Index: {PREFIX}-CAP-016)", conclusion.rstrip() + "\n\n", text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError("Concluziile nu au fost înlocuite.")

    text = re.sub(r"Raport calculator \| `[^`]+calculator\.json`", "Raport calculator | `2021-05-08-VULCU-DOMINIC-IOAN-scurt-v1.00r-calculator.json`", text)
    text = re.sub(r"\| SVG-uri integrate \| .* \|", "| SVG-uri integrate | Matrice, Scara bunăstării, Soartă–Destin și Omulețul relațiilor |", text)
    text = re.sub(rf"(?m)^(Index: {re.escape(PREFIX)}-[^\n]+)\n(?!\n)", r"\1\n\n", text)
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print(OUT)


if __name__ == "__main__":
    main()

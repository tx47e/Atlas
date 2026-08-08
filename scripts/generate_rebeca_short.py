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
BASE_MD = ROOT / "output/lucrari/1998-01-12-ROMAN-ANDREEA-MARIA/1998-01-12-ROMAN-ANDREEA-MARIA-scurt-v1.00r.md"
OUT_DIR = ROOT / "output/lucrari/2020-03-15-VULCU-REBECA-ANDREEA"
OUT = OUT_DIR / "2020-03-15-VULCU-REBECA-ANDREEA-scurt-v1.00r.md"
REPORT = OUT_DIR / "2020-03-15-VULCU-REBECA-ANDREEA-scurt-v1.00r-calculator.json"
CALCULATOR = ROOT / "skills/numerologie-lucrare-redactare/scripts/calculator_numerologic_examen.py"
MATRIX_GENERATOR = ROOT / "skills/numerologie-SVG-matrita-datei-de-nastere/scripts/generate_matrita_datei_de_nastere.py"
NAME_MATRIX_GENERATOR = ROOT / "skills/numerologie-SVG-matrita-numelui/scripts/generate_matrita_numelui.py"
PREFIX = "VRA-20200315-v1.00r"


ARCANA = {
    7: ("Carul", "07-The Chariot.jpg", "tarot-07-carul-aplicabilitate-profesionala.jpg"),
    13: ("Moartea", "13-Death.jpg", "tarot-13-moartea-karma-calea-destinului.jpg"),
    15: ("Diavolul", "15-The Devil.jpg", "tarot-15-diavolul-karma-zilei.jpg"),
    16: ("Turnul", "16-The Tower.jpg", "tarot-16-turnul-numarul-ereditar-karmic.jpg"),
}


def run_report() -> dict:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [
            sys.executable,
            str(CALCULATOR),
            "--data-nasterii", "15.03.2020",
            "--nume-complet", "Vulcu Rebeca Andreea",
            "--nume-familie", "Vulcu",
            "--prenume", "Rebeca Andreea",
            "--prenume-activ", "Rebeca",
            "--gen", "feminin",
            "--an-start", "2020",
            "--an-final", "2128",
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


def cycle12_table() -> str:
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
        start_year = 2020 + start_age
        end_year = 2020 + end_age
        if i == 1:
            style = '<span class="active-cycle-cell" style="color: #b3261e; font-weight: 700;">'
            close = "</span>"
            lines.append(f"| {style}**Ciclul {i} — activ**{close} | {style}**{start_year}–{end_year}**{close} | {style}**{start_age}–{end_age}**{close} | {style}{readings[i]}{close} |")
        else:
            lines.append(f"| Ciclul {i} | {start_year}–{end_year} | {start_age}–{end_age} | {readings[i]} |")
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


def main() -> None:
    report = run_report()
    copy_tarot()
    date_mod = load_generator(MATRIX_GENERATOR, "matrix_date_skill")
    name_mod = load_generator(NAME_MATRIX_GENERATOR, "matrix_name_skill")
    subprocess.run([sys.executable, str(MATRIX_GENERATOR), "--name", "Vulcu Rebeca Andreea", "--birth-date", "15.03.2020", "--output", str(OUT_DIR / "matrita-datei-vulcu-rebeca-andreea.svg")], check=True)
    subprocess.run([sys.executable, str(NAME_MATRIX_GENERATOR), "--name", "Vulcu Rebeca Andreea", "--birth-date", "15.03.2020", "--output", str(OUT_DIR / "matrita-numelui-vulcu-rebeca-andreea.svg")], check=True)

    calc = report["capitolul_2_formule_calcule_tabele_grafice"]
    base = calc["2.1_codul_numerologic_personal_data_nasterii"]
    matrix = calc["2.2_structura_matriciala"]
    name = calc["2.3_codul_numerologic_personal_al_numelui"]
    cycles = calc["2.4_ciclicitati"]
    prof = calc["2.6_spiritul"]["inclinatii_profesionale"]
    life_lessons = cycles["lectii_de_viata"]["sir_lectii"]
    life_lessons_text = "–".join(map(str, life_lessons))
    life_lessons_calc = f'15 × 3 × 2020 = {cycles["lectii_de_viata"]["produs"]} → ' + ", ".join(map(str, life_lessons))

    text = BASE_MD.read_text(encoding="utf-8")
    replacements = {
        "Roman Andreea Maria": "Vulcu Rebeca Andreea",
        "Andreea": "Rebeca",
        "RAM-19980112-v1.00r": PREFIX,
        "RAM-19980112": "VRA-20200315",
        "1998-01-12-ROMAN-ANDREEA-MARIA": "2020-03-15-VULCU-REBECA-ANDREEA",
        "12.01.1998": "15.03.2020",
        "1998-01-12": "2020-03-15",
        "31.07.2026": "08.08.2026",
        "matrita-datei-roman-andreea-maria.svg": "matrita-datei-vulcu-rebeca-andreea.svg",
        "soarta-si-destin-roman-andreea-maria.svg": "soarta-si-destin-vulcu-rebeca-andreea.svg",
        "harta-suprapusa-soarta-destin-roman-andreea-maria-v1.00r.svg": "harta-suprapusa-soarta-destin-vulcu-rebeca-andreea-v1.00r.svg",
        "tarot-03-imparateasa-vibratia-interioara.jpg": "tarot-15-diavolul-karma-zilei.jpg",
        "tarot-12-spanzuratul-karma-zilei.jpg": "tarot-15-diavolul-karma-zilei.jpg",
        "tarot-09-eremitul-karma-calea-destinului.jpg": "tarot-13-moartea-karma-calea-destinului.jpg",
        "tarot-06-indragostitii-aplicabilitate-profesionala.jpg": "tarot-07-carul-aplicabilitate-profesionala.jpg",
        "tarot-09-eremitul-obstacole-profesionale.jpg": "tarot-13-moartea-karma-calea-destinului.jpg",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    # Înlocuirea prenumelui activ nu trebuie să modifice al doilea prenume.
    text = text.replace("Vulcu Rebeca Rebeca", "Vulcu Rebeca Andreea")
    text = re.sub(r"\n- Relație analizată:.*", "", text)
    text = text.replace("9. Relații\n10. Aplicabilitate profesională\n11. Concluzii", "9. Concluzii")
    text = re.sub(rf"\nIndex: {PREFIX}-CAP-013\n.*?(?=\nIndex: {PREFIX}-CAP-015\n)", "\n", text, flags=re.S)
    text = text.replace("## Capitolul 11. Concluzii", "## Capitolul 9. Concluzii")
    text = text.replace("### 11.1. Carieră și bani", "### 9.1. Carieră și bani")
    text = re.sub(rf"\nIndex: {PREFIX}-SUB-031\n.*?(?=\nIndex: {PREFIX}-CAP-016\n)", "\n", text, flags=re.S)

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
        "C-005": "> [!example] Calcul în intervalul 1–22\n> Vulcu = **16**\n>\n> Arcana neamului = **16 — Turnul**",
        "T-013": '<table class="tarot-profile-table"><tbody><tr><td>Index: VRA-20200315-v1.00r-G-003<br>![Arcana 16 — Turnul](tarot-16-turnul-numarul-ereditar-karmic.jpg)<div class="tarot-image-caption"><em>Arcana <strong>16</strong> — Turnul</em></div></td><td><ul><li><strong>Resursă moștenită:</strong> capacitatea de a vedea ce nu mai este stabil și de a reclădi pe baze reale.</li><li><strong>Manifestare:</strong> curajul de a schimba structuri vechi, reguli sau tipare de familie.</li><li><strong>Umbră:</strong> teamă de pierdere, reacții bruște sau rezistență la schimbare până când presiunea devine mare.</li><li><strong>Maturizare:</strong> construirea unei siguranțe interioare care nu depinde doar de formele vechi.</li></ul></td></tr></tbody></table>',
        "P-022c": "Numărul ereditar karmic **16**, asociat Turnului, vorbește despre o moștenire în care adevărul cere uneori restructurare. Rebeca, poți duce mai departe resursa de a reface lucrurile mai sincer, mai curat și mai stabil decât au fost înainte.",
        "P-022d": "Umbra este să te agăți de forme care par sigure, dar nu mai susțin viața. Maturizarea apare când accepți schimbarea ca pe o șansă de curățare, nu ca pe o pedeapsă.",
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
    for suffix, body in blocks.items():
        text = replace_block(text, suffix, body)

    element_section = """<div class="element-analysis framed-panel"><div class="element-indexes"><span>Index: VRA-20200315-v1.00r-T-012</span><span>Index: VRA-20200315-v1.00r-P-044</span></div><div class="element-chart"><div class="element-bars" role="img" aria-label="Distribuția elementelor: Foc 5, Pământ 1, Aer 2, Apă 3"><div class="element-bar"><div class="element-bar-label"><span>Foc</span><strong>5</strong></div><div class="element-bar-track"><span class="element-bar-fill element-foc" style="width:100%"></span></div></div><div class="element-bar"><div class="element-bar-label"><span>Pământ</span><strong>1</strong></div><div class="element-bar-track"><span class="element-bar-fill element-pamant" style="width:20%"></span></div></div><div class="element-bar"><div class="element-bar-label"><span>Aer</span><strong>2</strong></div><div class="element-bar-track"><span class="element-bar-fill element-aer" style="width:40%"></span></div></div><div class="element-bar"><div class="element-bar-label"><span>Apă</span><strong>3</strong></div><div class="element-bar-track"><span class="element-bar-fill element-apa" style="width:60%"></span></div></div></div></div><ul class="element-definitions"><li><strong>Focul</strong> este esența vieții, a duhului și a spiritului care animă și activează.</li><li><strong>Pământul</strong> este esența materiei dense, a solidarității și a fertilității, care hrănește și dă formă.</li><li><strong>Aerul</strong> este esența inteligenței conceptuale care eliberează și stimulează.</li><li><strong>Apa</strong> este esența emoțiilor și a fecundității, maleabilă, flexibilă și orientată spre acumulare.</li></ul></div>

Index: VRA-20200315-v1.00r-P-045

Temperamentul tău predominant este **coleric**, cu Focul la **5** apariții, urmat de Apă cu **3**, Aer cu **2** și Pământ cu **1**. Ai energie de pornire și răspuns rapid, dar echilibrul vine când emoțiile primesc limbaj, iar corpul primește ritm și stabilitate."""
    text, count = re.subn(rf'<div class="element-analysis framed-panel">.*?(?=\nIndex: {PREFIX}-SUB-016)', element_section + "\n\n", text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError("Secțiunea elementelor nu a fost înlocuită.")

    conclusion = f"""Index: {PREFIX}-CAP-015

## Capitolul 9. Concluzii

Index: {PREFIX}-SUB-030

### 9.1. Carieră și bani

Index: {PREFIX}-P-032

Rebeca, cariera și banii se vor citi mai târziu prin felul în care energia ta de **6** învață să aibă grijă fără să se piardă, iar Destinul **4** învață să construiască pas cu pas. În matricea ta, vectorul **123, Energie** este cel mai puternic, ceea ce arată vitalitate, emoție și comunicare; banii vor avea nevoie de structură, pentru că zona **6–7–8–9** se construiește conștient prin educație, exemple și responsabilități potrivite vârstei.

Index: {PREFIX}-P-032a

Numărul activ **7** și Numărul de exprimare **8** adaugă o direcție interesantă: în timp, poți deveni un om care observă mult, înțelege profund și învață să administreze resurse sau responsabilități. Pentru etapa actuală, cheia nu este presiunea performanței, ci formarea unor obiceiuri sănătoase: ritm, ordine, joacă inteligentă, libertate cu limite și încurajarea curiozității.

Index: {PREFIX}-P-032b

Arcana neamului **16 — Turnul** spune că moștenirea ta cere construcții sincere, nu forme păstrate doar pentru aparență. În plan practic, asta înseamnă că mediul potrivit pentru tine este unul stabil, dar nu rigid: reguli clare, explicații, adevăr spus pe înțelesul tău și libertatea de a reconstrui când ceva nu mai funcționează.

Index: {PREFIX}-P-032c

În perioada copilăriei, Pinaclul **1** aduce Oportunitatea **9** și Provocarea **3**. Ai nevoie de povești, artă, natură, compasiune și contexte în care poți exprima ce simți. Când emoțiile sunt numite și așezate, energia ta devine creativă; când sunt grăbite sau ignorate, pot apărea încăpățânare, dramatizare sau retragere.

Index: {PREFIX}-P-032d

Pe scurt, direcția ta este să unești căldura lui **6**, expresia lui **3**, structura lui **4** și puterea matură a lui **8**. Când vei crește, cariera bună pentru tine va fi una în care poți îngriji, organiza, transforma și construi ceva util oamenilor, fără să îți pierzi bucuria și sensibilitatea."""
    text, count = re.subn(rf"Index: {PREFIX}-CAP-015\n.*?(?=Index: {PREFIX}-CAP-016)", conclusion.rstrip() + "\n\n", text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError("Concluziile nu au fost înlocuite.")

    text = text.replace("Raport calculator | `1998-01-12-ROMAN-ANDREEA-MARIA-scurt-v1.00r-calculator.json`", "Raport calculator | `2020-03-15-VULCU-REBECA-ANDREEA-scurt-v1.00r-calculator.json`")
    text = re.sub(r"\| SVG-uri integrate \| .* \|", "| SVG-uri integrate | Matrice, Scara bunăstării și Soartă–Destin |", text)
    text = re.sub(rf"(?m)^(Index: {re.escape(PREFIX)}-[^\n]+)\n(?!\n)", r"\1\n\n", text)
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print(OUT)


if __name__ == "__main__":
    main()

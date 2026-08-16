from __future__ import annotations

import base64
import html
import importlib.util
import json
import mimetypes
import re
import shutil
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CALCULATOR = ROOT / "skills/numerologie-lucrare-redactare/scripts/calculator_numerologic_examen.py"
DATE_MATRIX = ROOT / "skills/numerologie-SVG-matrita-datei-de-nastere/scripts/generate_matrita_datei_de_nastere.py"
NAME_MATRIX = ROOT / "skills/numerologie-SVG-matrita-numelui/scripts/generate_matrita_numelui.py"
SOARTA = ROOT / "skills/numerologie-SVG-soarta-si-destin/scripts/generate_soarta_si_destin.py"
HELPERS = ROOT / "scripts/generate_rebeca_short.py"
MODEL_HTML = ROOT / "output/lucrari/2021-05-08-VULCU-DOMINIC-IOAN/2021-05-08-VULCU-DOMINIC-IOAN-scurt-v1.00r.html"
DOMINIC_RELATION_PNG = ROOT / "output/lucrari/2021-05-08-VULCU-DOMINIC-IOAN/omulet-relatii-vulcu-dominic-ioan-vulcu-victor-daniel.png"
TAROT_DIR = ROOT / "vault/Tarot/imagini"
TODAY = date(2026, 8, 10)


PEOPLE = (
    {
        "yaml": ROOT / "persoane/2023-03-17-VULCU-VICTOR-DANIEL/persoana.yaml",
        "folder": "2023-03-17-VULCU-VICTOR-DANIEL",
        "prefix": "VVD-20230317-v1.00r",
    },
    {
        "yaml": ROOT / "persoane/2026-03-05-DOCOLIN-INGRID-PETRA/persoana.yaml",
        "folder": "2026-03-05-DOCOLIN-INGRID-PETRA",
        "prefix": "DIP-20260305-v1.00r",
    },
)


ARCANA = {
    0: ("Nebunul", "00-The Fool.jpg"),
    1: ("Magicianul", "01-The Magician.jpg"),
    2: ("Marea Preoteasa", "02-The High Priestess.jpg"),
    3: ("Imparateasa", "03-The Empress.jpg"),
    4: ("Imparatul", "04-The Emperor.jpg"),
    5: ("Marele Preot", "05-The Hierrophant.jpg"),
    6: ("Indragostitii", "06-The Lovers.jpg"),
    7: ("Carul", "07-The Chariot.jpg"),
    8: ("Puterea", "08-Strenght.jpg"),
    9: ("Ermitul", "09-The Hermit.jpg"),
    10: ("Roata Norocului", "10-Wheel of Fortune.jpg"),
    11: ("Dreptatea", "11-Justice.jpg"),
    12: ("Spanzuratul", "12-The Hanged Man.jpg"),
    13: ("Moartea", "13-Death.jpg"),
    14: ("Cumpatarea", "14-Temperance.jpg"),
    15: ("Diavolul", "15-The Devil.jpg"),
    16: ("Turnul", "16-The Tower.jpg"),
    17: ("Steaua", "17-The Star.jpg"),
    18: ("Luna", "18-The Moon.jpg"),
    19: ("Soarele", "19-The Sun.jpg"),
    20: ("Judecata", "20-Judgenmet.jpg"),
    21: ("Lumea", "21-The World.jpg"),
}


VIBES = {
    1: ("Initiatorul", "initiativa, curaj si pornire", "graba, orgoliu sau dorinta de a face singur totul"),
    2: ("Mediatorul", "sensibilitate, cooperare si rabdare", "dependenta de confirmare sau evitare a conflictului"),
    3: ("Comunicatorul", "expresie, joc, cuvant si creativitate", "risipire, dramatizare sau vorbire fara asezare"),
    4: ("Constructorul", "ordine, disciplina si rezultate concrete", "rigiditate, incapatanare sau frica de schimbare"),
    5: ("Exploratorul", "libertate, curiozitate si adaptare", "neliniste, imprastiere sau refuzul rutinei"),
    6: ("Protectorul", "grija, armonie si responsabilitate afectiva", "supraprotectie, control prin grija sau vinovatie"),
    7: ("Observatorul", "analiza, profunzime si timp interior", "retragere, neincredere sau izolare"),
    8: ("Administratorul", "putere, rezultat si responsabilitate", "control, presiune sau competitie excesiva"),
    9: ("Inteleptul", "compasiune, perspectiva si transformare", "idealism, amanarea finalizarii sau salvarea tuturor"),
    10: ("Schimbarea", "adaptare si intoarcerea rotii in directia potrivita", "instabilitate sau incredere prea mare in context"),
}


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if not spec or not spec.loader:
        raise RuntimeError(f"Nu pot incarca {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


HELPER = load_module(HELPERS, "short_helpers")
DATE_MOD = load_module(DATE_MATRIX, "date_matrix")
NAME_MOD = load_module(NAME_MATRIX, "name_matrix")


def read_person(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    values: dict[str, str] = {}
    for key in ("nume_complet", "nume_familie", "prenume", "prenume_activ", "data_nasterii", "ora_nasterii", "gen"):
        match = re.search(rf"^\s+{key}:\s*'?([^'\n]+)'?\s*$", text, re.M)
        if not match:
            raise RuntimeError(f"Lipseste {key} in {path}")
        values[key] = match.group(1).strip()
    return values


def display_date(iso_date: str) -> str:
    return datetime.strptime(iso_date, "%Y-%m-%d").strftime("%d.%m.%Y")


def age_on(birth: date, current: date = TODAY) -> int:
    return current.year - birth.year - ((current.month, current.day) < (birth.month, birth.day))


def b(value: int | str) -> str:
    return f"<strong>{html.escape(str(value))}</strong>"


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode('ascii')}"


def arcana_value(value: int) -> int:
    if value == 22:
        return 0
    return ((value - 1) % 22) + 1


def copy_arcana(out_dir: Path, number: int, suffix: str) -> tuple[int, str, Path]:
    name, filename = ARCANA[number]
    target = out_dir / f"tarot-{number:02d}-{slug(name)}-{suffix}.jpg"
    shutil.copyfile(TAROT_DIR / filename, target)
    return number, name, target


def slug(value: str) -> str:
    table = str.maketrans({"ă": "a", "â": "a", "î": "i", "ș": "s", "ş": "s", "ț": "t", "ţ": "t"})
    value = value.lower().translate(table)
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def run_report(person: dict[str, str], out_dir: Path) -> dict:
    born = datetime.strptime(person["data_nasterii"], "%Y-%m-%d").date()
    report_path = out_dir / f"{person['data_nasterii']}-{slug(person['nume_complet']).upper()}-scurt-v1.00r-calculator.json"
    args = [
        sys.executable, str(CALCULATOR),
        "--data-nasterii", display_date(person["data_nasterii"]),
        "--nume-complet", person["nume_complet"],
        "--nume-familie", person["nume_familie"],
        "--prenume", person["prenume"],
        "--prenume-activ", person["prenume_activ"],
        "--gen", person["gen"],
        "--an-start", str(born.year),
        "--an-final", str(born.year + 108),
        "--pretty",
    ]
    result = subprocess.run(args, check=True, capture_output=True, text=True, encoding="utf-8")
    report = json.loads(result.stdout)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    return report


def generate_graphics(person: dict[str, str], out_dir: Path) -> tuple[str, str, Path]:
    name = person["nume_complet"]
    birth = display_date(person["data_nasterii"])
    stem = slug(name)
    date_svg = out_dir / f"matrita-datei-{stem}.svg"
    name_svg = out_dir / f"matrita-numelui-{stem}.svg"
    soarta_svg = out_dir / f"soarta-si-destin-{stem}.svg"
    subprocess.run([sys.executable, str(DATE_MATRIX), "--name", name, "--birth-date", birth, "--output", str(date_svg)], check=True)
    subprocess.run([sys.executable, str(NAME_MATRIX), "--name", name, "--birth-date", birth, "--output", str(name_svg)], check=True)
    subprocess.run([sys.executable, str(SOARTA), "--name", name, "--birth-date", birth, "--output", str(soarta_svg)], check=True)
    date_component = DATE_MOD.build_html_component(name, birth)[0]
    name_component = NAME_MOD.build_html_component(name, birth)[0]
    return date_component, name_component, soarta_svg


def html_table(headers: list[str], rows: list[list[str]], cls: str = "") -> str:
    klass = f' class="{cls}"' if cls else ""
    head = "".join(f"<th>{html.escape(h)}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>" for row in rows)
    return f'<div class="table-wrap"><table{klass}><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>'


def lesson_table_html(lessons: list[int], birth_year: int, end_age: int = 60) -> str:
    headers = ["Varsta"] + [f"Lectia {i + 1} - {v}" for i, v in enumerate(lessons)]
    rows = []
    step = len(lessons)
    for start_age in range(1, end_age + 1, step):
        row = [f"{start_age}-{start_age + step - 1}"]
        for offset in range(step):
            year = birth_year + start_age + offset - 1
            value = str(year)
            if year == TODAY.year:
                value = f'<span style="color:#b3261e;font-weight:700">{year}</span>'
            row.append(value)
        rows.append(row)
    return html_table(headers, rows)


def cycle9_html(cycle_rows: list[dict]) -> str:
    rows = []
    for start in range(0, min(len(cycle_rows), 81), 9):
        chunk = cycle_rows[start:start + 9]
        label = f"C{start // 9 + 1} ({chunk[0]['varsta']}-{chunk[-1]['varsta']})"
        row = [label]
        for item in chunk:
            year = str(item["an"])
            if item["an"] == TODAY.year:
                year = f'<span style="color:#b3261e;font-weight:700">{year}</span>'
            row.append(year)
        rows.append(row)
    return html_table(["Ciclu"] + [f"Anul {i}" for i in range(1, 10)], rows)


def cycle12_html(birth_year: int) -> str:
    readings = [
        "Formarea sigurantei, a limbajului emotional si a primelor repere de familie.",
        "Explorare, autonomie treptata si descoperirea intereselor proprii.",
        "Extindere prin studiu, relatii, experiente si responsabilitati asumate.",
        "Consolidarea unei forme de viata stabile: profesie, familie si statut.",
        "Recalibrarea sensului si valorificarea matura a experientei acumulate.",
        "Transmitere, mentorat si influenta exercitata cu discernamant.",
        "Sinteza, simplificare si intoarcere la ceea ce este esential.",
        "Administrarea responsabila a resurselor si a mostenirii personale.",
        "Integrarea etapelor parcurse si inchiderea lucida a ciclurilor lungi.",
    ]
    rows = []
    for i, reading in enumerate(readings, start=1):
        start_age, end_age = (i - 1) * 12, (i - 1) * 12 + 11
        start_year, end_year = birth_year + start_age, birth_year + end_age
        active = start_year <= TODAY.year <= end_year
        label = f"Ciclul {i}" + (" - activ" if active else "")
        row = [label, f"{start_year}-{end_year}", f"{start_age}-{end_age}", reading]
        if active:
            row = [f'<span class="active-cycle-cell">{cell}</span>' for cell in row]
        rows.append(row)
    return html_table(["Ciclu", "Interval calendaristic", "Varste", "Citire"], rows, "twelve-year-table")


def calc_line(calc: dict) -> str:
    intrare = calc.get("intrare")
    parts = [str(intrare)] if intrare is not None else []
    parts.extend(calc.get("pasi", []))
    parts.append(str(calc["rezultat"]))
    return " -> ".join(parts)


def spirit_data(day: int, month: int, years_old: int) -> dict[str, int]:
    code = 55 - day - (2 * month)
    substage = ((code - 1) % 13) + 1
    return {
        "code": code,
        "substage": substage,
        "birth_age": (code - 1) * 189,
        "current_age": ((code - 1) * 189) + years_old,
    }


def spirit_code_html(day: int, month: int) -> str:
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
    rows = [
        '<table class="spirit-code-table"><thead><tr><th>Ziua</th>'
        + "".join(f'<th align="right">{m}</th>' for m in romans)
        + "</tr></thead><tbody>"
    ]
    for d in range(1, 32):
        cells = [f"<td>{d}</td>"]
        for m in range(1, 13):
            if d > month_lengths[m - 1]:
                cells.append('<td align="right"></td>')
                continue
            code = 55 - d - 2 * m
            cls = "spirit-cell-highlight" if (d == day and m == month) else zone_class(code)
            cells.append(f'<td align="right"><span class="{cls}">{code}</span></td>')
        rows.append("<tr>" + "".join(cells) + "</tr>")
    rows.append("</tbody></table>")
    return "".join(rows)


def section(title: str, inner: str) -> str:
    return f"<section>{title}{inner}</section>"


def generate_html(person: dict[str, str], report: dict, out_dir: Path, prefix: str) -> str:
    calc = report["capitolul_2_formule_calcule_tabele_grafice"]
    base = calc["2.1_codul_numerologic_personal_data_nasterii"]
    matrix = calc["2.2_structura_matriciala"]
    name_data = calc["2.3_codul_numerologic_personal_al_numelui"]
    cycles = calc["2.4_ciclicitati"]
    prof = calc["2.6_spiritul"]["inclinatii_profesionale"]
    born = datetime.strptime(person["data_nasterii"], "%Y-%m-%d").date()
    years_old = age_on(born)
    day, month, year = born.day, born.month, born.year
    birth_ro = display_date(person["data_nasterii"])
    name = person["nume_complet"]
    active = person["prenume_activ"]
    date_component, name_component, soarta_svg = generate_graphics(person, out_dir)

    vi = base["vibratia_interioara"]["calcul"]["rezultat"]
    ve = base["vibratia_exterioara"]["calcul"]["rezultat"]
    vg = base["vibratia_globala"]["calcul"]["rezultat"]
    destin_compus = base["destinul_vibratia_destinului"]["calcul"]["rezultat"]
    destin_interp = base["destinul_vibratia_destinului"]["cifra_interpretare"]["rezultat"]
    calea = base["calea_destinului"]["rezultat"]
    spirit = spirit_data(day, month, years_old)
    lessons = cycles["lectii_de_viata"]["sir_lectii"]
    product = cycles["lectii_de_viata"]["produs"]
    current_cycle = next(row for row in cycles["ciclul_de_9_ani"] if row["an"] == TODAY.year)
    pin = cycles["pinacluri"]["randuri"][0]
    current_pin = next((p for p in cycles["pinacluri"]["randuri"] if "+" not in p["interval_varsta"] and int(p["interval_varsta"].split("-")[0]) <= years_old <= int(p["interval_varsta"].split("-")[1])), cycles["pinacluri"]["randuri"][0])
    if "+" in current_pin["interval_varsta"]:
        current_pin = cycles["pinacluri"]["randuri"][-1]

    k_day_number, k_day_name, k_day_img = copy_arcana(out_dir, arcana_value(day), "karma-zilei")
    k_dest_number, k_dest_name, k_dest_img = copy_arcana(out_dir, arcana_value(calea), "karma-calea-destinului")
    da_number, da_name, da_img = copy_arcana(out_dir, arcana_value(prof["da"]), "aplicabilitate-profesionala")
    nu_number, nu_name, nu_img = copy_arcana(out_dir, arcana_value(prof["nu"]), "obstacol-profesional")
    neam_number, neam_name, neam_img = copy_arcana(out_dir, arcana_value(name_data["numarul_ereditar_karmic_neamul"]["arcana_majora"]), "numarul-ereditar-karmic")

    components = name_data["numarul_de_exprimare"]["componente"]
    name_rows = [[c["componenta"], str(c["total"]), str(c["reducere"]["rezultat"])] for c in components]
    name_rows.append(["Numarul de exprimare", str(name_data["numarul_de_exprimare"]["total_reduse"]), str(name_data["numarul_de_exprimare"]["reducere"]["rezultat"])])
    common_digits = sorted(int(k) for k, v in matrix["casute"].items() if v["cantitate"] > 0 and name_data["matricea_numelui"]["casute"][k]["cantitate"] > 0)
    native_missing = [int(k) for k, v in matrix["casute"].items() if v["cantitate"] == 0]
    wellbeing = HELPER.wellbeing(matrix["scara_bunastarii"])
    spirit_code_table_html = spirit_code_html(day, month)
    spirit_stage_table = HELPER.spirit_stage_table(spirit["substage"])

    def idx(value: str) -> str:
        return f'<div class="idx">Index: {prefix}-{value}</div>'

    sections = []
    sections.append(f"""
{idx("CAP-001")}<h1>{html.escape(name)} - {birth_ro}</h1>
{idx("CAP-002")}<h2 id="date-generale">Date generale</h2>
<ul>
<li>Persoana analizata: {html.escape(name)}</li>
<li>Prenume activ: {html.escape(active)}</li>
<li>Data nasterii: {birth_ro}</li>
<li>Ora nasterii: {html.escape(person["ora_nasterii"])}</li>
<li>Gen: {html.escape(person["gen"])}</li>
<li>Template selectat: scurt</li>
<li>Stil de redactare: conversațional, varianta scurtă amplă</li>
<li>Interval analizat: 0-108 ani</li>
<li>Data lucrarii: 10.08.2026</li>
<li>Versiune: V1.00R</li>
</ul>
{idx("CAP-003")}<h2 id="cuprins">Cuprins</h2>
<ol>
<li><a href="#capitolul-1-vibratia-interioara">Capitolul 1. Vibratia interioara</a></li>
<li><a href="#capitolul-2-vibratia-exterioara">Capitolul 2. Vibratia exterioara</a></li>
<li><a href="#capitolul-3-destinul">Capitolul 3. Destinul</a></li>
<li><a href="#capitolul-4-matrita-numerologica">Capitolul 4. Matrita numerologica</a></li>
<li><a href="#capitolul-5-numele">Capitolul 5. Numele</a></li>
<li><a href="#capitolul-6-spirit-si-karma">Capitolul 6. Spirit si karma</a></li>
<li><a href="#capitolul-7-pinacluri">Capitolul 7. Pinacluri: Oportunitati si provocari</a></li>
<li><a href="#capitolul-8-ciclicitati">Capitolul 8. Ciclicitati</a></li>
<li><a href="#capitolul-9-concluzii">Capitolul 9. Concluzii</a></li>
</ol>
""")

    vi_name, vi_light, vi_shadow = VIBES.get(vi, VIBES[9])
    ve_name, ve_light, ve_shadow = VIBES.get(ve, VIBES[9])
    vg_name, vg_light, vg_shadow = VIBES.get(vg, VIBES[9])
    sections.append(section(
        f'{idx("CAP-004")}<h2 id="capitolul-1-vibratia-interioara">Capitolul 1. Vibratia interioara - Cine esti tu?</h2>',
        f"""
{idx("P-001")}<p>Vibratia interioara vorbeste despre desavarsirea caracterului si despre natura ta launtrica: cine esti cand nu trebuie sa raspunzi asteptarilor din exterior. Ea arata motivatia, felul in care primesti lumea si ritmul in care inveti.</p>
{idx("C-001")}<aside class="callout example"><strong>Calcul</strong><br>Ziua din data de nastere = {b(day)}{' -> ' + b(vi) if day != vi else ''}</aside>
{idx("P-002")}<p>{active}, cu vibratia interioara {b(vi)} esti aproape de arhetipul {html.escape(vi_name)}. In tine se vede {html.escape(vi_light)}. Daca ziua are un traseu de reducere, el arata cum cifra de plecare se aseaza in rezultat: energia initiala se aduna, se rafineaza si devine directia principala a caracterului.</p>
{idx("P-003")}<p>Manifestarea concreta este simpla: ai nevoie de contexte in care energia lui {b(vi)} sa fie vazuta, exersata si condusa bland. Umbra poate deveni {html.escape(vi_shadow)}. Maturizarea apare cand adultii din jur iti dau ritm, limite limpezi si libertatea potrivita varstei, fara sa transforme cifra intr-un verdict.</p>
{idx("T-009")}<div class="table-wrap"><table class="polarities-table"><tbody><tr><th>Polaritati pozitive</th><td><ul><li>{html.escape(vi_light)}</li><li>curaj de a invata prin experienta</li><li>prezenta vie in familie si grup</li></ul></td></tr><tr><th>Polaritati negative</th><td><ul><li>{html.escape(vi_shadow)}</li><li>reactie intensa cand mediul este neclar</li><li>tendinta de a forta ritmul propriu</li></ul></td></tr><tr><th>Directii de dezvoltare</th><td><ul><li>limite calde si consecvente</li><li>activitati duse pana la capat</li><li>exprimarea emotiilor in cuvinte simple</li></ul></td></tr></tbody></table></div>
"""))

    sections.append(section(
        f'{idx("CAP-005")}<h2 id="capitolul-2-vibratia-exterioara">Capitolul 2. Vibratia exterioara - Rolul social</h2>',
        f"""
{idx("P-004")}<p>Vibratia exterioara descrie felul in care devii vizibil in lume: prima impresie, comportamentul social si modul in care ceilalti iti pot percepe energia.</p>
{idx("C-002")}<aside class="callout example"><strong>Calcul</strong><br>Luna din data de nastere = {b(month)}{' -> ' + b(ve) if month != ve else ''}</aside>
{idx("P-005")}<p>La exterior, oamenii pot vedea energia {b(ve)}, apropiata de arhetipul {html.escape(ve_name)}: {html.escape(ve_light)}. Daca in interior esti {b(vi)}, la exterior poti fi perceput ca {b(ve)}. Dialogul acesta cere coerenta intre intentie si gest.</p>
{idx("P-006")}<p>Puntea interior-exterior arata ajustarea dintre nucleul interior si imaginea vizibila. Pentru tine, ea se citeste ca o cheie de autenticitate: sa fii primit fara ezitare in rolul pe care il asumi.</p>
{idx("C-003")}<aside class="callout example"><strong>Calculul puntii interior-exterior</strong><br>|{b(vi)} - {b(ve)}| = {b(base["puntea_interior_exterior"]["rezultat"])}</aside>
{idx("P-007")}<p>Vibratia globala {b(vg)} aduna interiorul si exteriorul. Ea functioneaza ca o sinteza de comportament: {html.escape(vg_light)}. Umbra ei, {html.escape(vg_shadow)}, se tempereaza prin rutina, prezenta si exemple clare.</p>
"""))

    sections.append(section(
        f'{idx("CAP-006")}<h2 id="capitolul-3-destinul">Capitolul 3. Destinul - Muntele de urcat</h2>',
        f"""
{idx("P-008")}<p>Destinul sintetizeaza data completa si arata o directie de maturizare. Nu este o sentinta, ci muntele simbolic pe care inveti sa il urci in timp.</p>
{idx("C-004")}<aside class="callout example"><strong>Calcul</strong><br>Toate cifrele adunate din data de nastere = {html.escape(base["calea_destinului"]["calcul"])}<br>Destin compus: {b(destin_compus)}<br>Cifra de interpretare = {b(destin_interp)}</aside>
{idx("P-009")}<p>{active}, Calea Destinului {b(calea)} si cifra de interpretare {b(destin_interp)} iti arata directia mare: sa transformi energia de baza in maturitate, responsabilitate si expresie potrivita varstei. Cand Destinul se leaga de vibratia interioara {b(vi)}, lectia este sa nu ramai doar in impuls, ci sa construiesti un fel coerent de a fi.</p>
"""))

    casute = []
    for digit, info in matrix["casute"].items():
        count = info["cantitate"]
        state = f"ai {b(count)} aparitii" if count else "energia este conservata"
        casute.append(f'{idx(f"P-01{digit}")}<p><strong>Casuta {digit}.</strong> {state}. Aceasta zona se citeste prin resursa cifrei {b(digit)} si prin felul in care ea poate fi folosita practic in viata de zi cu zi. Cand este activa, sustine expresia directa; cand este conservata, se construieste prin oameni, contexte, exercitiu si aport extern.</p>')
    pare = matrix["pare_impare"]["pare"]
    impare = matrix["pare_impare"]["impare"]
    sections.append(section(
        f'{idx("CAP-007")}<h2 id="capitolul-4-matrita-numerologica">Capitolul 4. Matrita numerologica - Patratul lui Pitagora</h2>',
        f"""
{idx("P-010")}<p>Cele noua casute descriu noua forme de inteligenta: {b(1)} psihica, {b(2)} emotionala, {b(3)} prelucrarea informatiilor, {b(4)} corporala, {b(5)} intuitiva, {b(6)} pragmatism, {b(7)} spirituala, {b(8)} putere si sociala, {b(9)} mentala.</p>
{idx("C-005")}<aside class="callout example"><strong>Calcul</strong><br>Data compacta = {b(matrix["meta"]["data_compacta"])}<br>N1 = {b(matrix["meta"]["numere_de_lucru"]["n1"])}; N2 = {b(matrix["meta"]["numere_de_lucru"]["n2"])}; N3 = {b(matrix["meta"]["numere_de_lucru"]["n3"])}; N4 = {b(matrix["meta"]["numere_de_lucru"]["n4"])}<br>Sir complet = {b(matrix["meta"]["sir_complet"])}</aside>
{idx("G-002")}{date_component}
{''.join(casute)}
{idx("P-020")}<p>Raportul par-impar este {b(pare)} la {b(impare)}. Cifrele pare sustin capacitatea de a primi si de a da mai departe; cand devin foarte numeroase, pot aduce ezitare. La tine citirea se face nu ca verdict, ci ca indiciu despre ritmul in care mediul trebuie sa combine receptivitatea cu initiativa.</p>
{idx("P-021")}<p>Scara bunastarii este condusa de {html.escape(matrix["scara_bunastarii"][0]["denumire"])} cu valoarea {b(matrix["scara_bunastarii"][0]["valoare"])}. Asta arata zona unde energia curge cel mai usor si unde se poate construi incredere prin activitati concrete.</p>
{idx("G-004")}{wellbeing}
"""))

    sections.append(section(
        f'{idx("CAP-008")}<h2 id="capitolul-5-numele">Capitolul 5. Numele - Eu si neamul</h2>',
        f"""
{idx("P-022")}<p>Numele arata felul in care identitatea primeste o forma sociala. Il citim prin numarul activ, intim, ereditar, ereditar karmic, realizare, exprimare si codul numerologic al numelui.</p>
{idx("T-001")}{html_table(["Componenta", "Total", "Reducere"], name_rows)}
{idx("P-023")}<p>Numarul activ {b(name_data["numarul_activ"]["reducere"]["rezultat"])} iti arata cum pornesti prin prenumele folosit. Numarul intim {b(name_data["numarul_intim"]["reducere"]["rezultat"])} vorbeste despre dorinta launtrica, iar numarul de realizare {b(name_data["numarul_de_realizare"]["reducere"]["rezultat"])} despre felul in care poti fi vazut cand actionezi.</p>
{idx("P-024")}<p>Numarul ereditar {b(name_data["numarul_ereditar"]["reducere"]["rezultat"])} vine prin numele {html.escape(person["nume_familie"])}. Numarul ereditar karmic este {b(neam_number)} - {html.escape(neam_name)}. Pentru familie, el descrie o mostenire simbolica de construit, reparat si maturizat, nu o eticheta fixa.</p>
{idx("G-001")}<figure><img src="{data_uri(neam_img)}" alt="Arcana {neam_number} - {html.escape(neam_name)}"><figcaption>Arcana {b(neam_number)} - {html.escape(neam_name)}. Numarul ereditar karmic</figcaption></figure>
{idx("C-011")}<aside class="callout example"><strong>Codul numerologic al numelui</strong><br>Codul literelor numelui = {b(''.join(str(x["valoare"]) for x in name_data["matricea_numelui"]["meta"]["codul_numelui"]["valori_nume"]))}<br>Codul numerologic personal al numelui = {b(name_data["matricea_numelui"]["meta"]["numar_exprimare_introdus_in_matrice"])}</aside>
{idx("G-002a")}{name_component}
{idx("P-025")}<p>Energiile comune intre matricea datei si matricea numelui sunt {', '.join(b(x) for x in common_digits) or 'niciuna'}. Doar acestea se interpreteaza ca sprijin direct. Cifrele native conservate - {', '.join(b(x) for x in native_missing) or 'niciuna'} - se pot construi prin experiente potrivite, dar nu le atribuim artificial numelui.</p>
"""))

    sections.append(section(
        f'{idx("CAP-009")}<h2 id="capitolul-6-spirit-si-karma">Capitolul 6. Spirit si karma - Lectii si directii de maturizare</h2>',
        f"""
{idx("P-026")}<p>Codul Spiritului aseaza ziua si luna intr-o harta simbolica a maturizarii. Pentru tine, pozitia reala este ziua {b(day)} si luna {b(month)}, unde apare codul {b(spirit["code"])}.</p>
{idx("T-017")}<div class="table-wrap spirit-code-wrap">{spirit_code_table_html}</div>
{idx("T-018")}<div class="table-wrap"><table class="spirit-zones-table"><thead><tr><th>Zona</th><th>Interval cod</th><th>Nivel simbolic</th><th>Teme principale</th></tr></thead><tbody><tr><td class="zone-cell zone-love"><span class="zone-badge">Iubire</span></td><td>1-13</td><td>0-2.500 ani</td><td>relații, emoții, atașamente, compasiune, vulnerabilitate</td></tr><tr><td class="zone-cell zone-reason"><span class="zone-badge">Rațiune</span></td><td>14-26</td><td>2.500-5.000 ani</td><td>logică, discernământ, structură, analiză, minte</td></tr><tr><td class="zone-cell zone-material"><span class="zone-badge">Material</span></td><td>27-39</td><td>5.000-7.500 ani</td><td>bani, construcție, putere, manifestare, responsabilitate</td></tr><tr><td class="zone-cell zone-gifts"><span class="zone-badge">Haruri</span></td><td>40-52</td><td>7.500-10.000 ani</td><td>înțelepciune, haruri spirituale, ghidare, serviciu, intuiție</td></tr></tbody></table></div>
{idx("T-019")}<div class="table-wrap">{spirit_stage_table}</div>
{idx("C-003d")}<aside class="callout example"><p><strong>Calcul</strong><br>Vârsta la naștere = ({spirit["code"]} − 1) × 189 = {b(spirit["birth_age"])}</p><p>Vârsta actuală = {spirit["birth_age"]} + {years_old} = {b(spirit["current_age"])}</p></aside>
{idx("P-027")}<p>Subetapa {b(spirit["substage"])} cere o forma concreta de invatare. Pentru varsta actuala, recomandarea este sa primesti contexte sigure, ritm repetabil si oameni care explica, nu doar cer rezultat.</p>
{idx("P-028")}<p>Karma zilei este citita prin Arcana {b(k_day_number)} - {html.escape(k_day_name)}, cu procentul {html.escape(base["vibratia_interioara_karmica"]["procent"])}. Ea descrie simbolic o lectie de maturizare, nu un fapt verificabil despre trecut.</p>
{idx("G-003")}<figure><img src="{data_uri(k_day_img)}" alt="Arcana {k_day_number} - {html.escape(k_day_name)}"><figcaption>Arcana {b(k_day_number)} - {html.escape(k_day_name)}. Karma din ziua de nastere</figcaption></figure>
{idx("P-029")}<p>Karma lunii se citeste prudent prin luna {b(month)}: modul in care mediul, familia si ritmul emotional te invata sa folosesti energia exterioara fara risipire sau presiune.</p>
{idx("P-030")}<p>Karma din Calea Destinului pastreaza suma compusa {b(calea)} si o asociaza cu Arcana {b(k_dest_number)} - {html.escape(k_dest_name)}. Directia matura este sa transformi aceasta imagine intr-un comportament concret: invatare, disciplina si alegeri potrivite varstei.</p>
{idx("G-003a")}<figure><img src="{data_uri(k_dest_img)}" alt="Arcana {k_dest_number} - {html.escape(k_dest_name)}"><figcaption>Arcana {b(k_dest_number)} - {html.escape(k_dest_name)}. Karma din Calea Destinului</figcaption></figure>
"""))

    pin_rows = [[f"Pinaclul {p['pinaclu']}", p["interval_varsta"], b(p["oportunitate"]), b(p["provocare"])] for p in cycles["pinacluri"]["randuri"]]
    sections.append(section(
        f'{idx("CAP-010")}<h2 id="capitolul-7-pinacluri">Capitolul 7. Pinacluri: Oportunitati si provocari</h2>',
        f"""
{idx("C-013")}<aside class="callout example"><strong>Calcul</strong><br>Calea Destinului: {b(calea)}<br>Destin compus: {b(destin_compus)}<br>Limita Pinaclului 1: 36 - {b(destin_compus)} = {b(36 - destin_compus)}</aside>
{idx("T-006")}{html_table(["Pinaclu", "Interval", "Oportunitate", "Provocare"], pin_rows)}
{idx("P-031")}<p>Pinaclul 1: intervalul {html.escape(cycles["pinacluri"]["randuri"][0]["interval_varsta"])} aduce Oportunitatea {b(cycles["pinacluri"]["randuri"][0]["oportunitate"])} si Provocarea {b(cycles["pinacluri"]["randuri"][0]["provocare"])}. Pentru copil, aceasta etapa se traduce prin mediul de acasa, ritmul zilnic, joc, corp, limbaj si limite asezate bland.</p>
{idx("P-032")}<p>La varsta actuala, esti in Pinaclul {b(current_pin["pinaclu"])}, cu Oportunitatea {b(current_pin["oportunitate"])} si Provocarea {b(current_pin["provocare"])}. Citirea utila este practica: ce obicei trebuie format, ce libertate poate fi oferita si ce trebuie repetat pana devine siguranta.</p>
"""))

    sections.append(section(
        f'{idx("CAP-011")}<h2 id="capitolul-8-ciclicitati">Capitolul 8. Ciclicitati</h2>',
        f"""
{idx("SUB-025")}<h3>8.1. Soarta si Destinul</h3>
{idx("G-005")}<figure><img src="{data_uri(soarta_svg)}" alt="Grafic Soarta si Destin pentru {html.escape(name)}"><figcaption>Grafic Soarta si Destin pentru {html.escape(name)}</figcaption></figure>
{idx("P-033")}<p>Graficul Soarta-Destin se citeste ca ritm al etapelor. Pentru varsta copilariei, el nu se foloseste ca predictie, ci ca harta a felului in care mediul poate sustine trecerea de la potential la comportament.</p>
{idx("SUB-026")}<h3>8.2. Anii importanti</h3>
{idx("P-034")}<p><strong>Sirul anilor importanti interiori:</strong> {' -> '.join(map(str, cycles["ani_importanti_interiori_exteriori"]["interiori"]))}.</p>
{idx("P-035")}<p><strong>Sirul anilor importanti exteriori:</strong> {' -> '.join(map(str, cycles["ani_importanti_interiori_exteriori"]["exteriori"]))}.</p>
{idx("SUB-027")}<h3>8.3. Lectiile de viata</h3>
{idx("P-036")}<p>Lectiile de viata se calculeaza din produsul zilei, lunii si anului nasterii: {b(day)} x {b(month)} x {b(year)} = {b(product)}. Sirul {', '.join(b(x) for x in lessons)} se repeta ciclic si pastreaza toate cifrele, inclusiv {b(0)}.</p>
{idx("T-008")}{lesson_table_html(lessons, year)}
{idx("P-037")}<p>In {TODAY.year}, lectia activa este {b(current_cycle["lectie"])} si anul personal este {b(current_cycle["an_personal"])}. Pentru tine, asta se traduce prin pasi mici, experiente clare si ritm sustinut de familie.</p>
{idx("SUB-028")}<h3>8.4. Ciclul de 9 ani</h3>
{idx("T-007")}{cycle9_html(cycles["ciclul_de_9_ani"])}
{idx("SUB-029")}<h3>8.5. Ciclul de 12 ani</h3>
{idx("T-015")}{cycle12_html(year)}
"""))

    sections.append(section(
        f'{idx("CAP-012")}<h2 id="capitolul-9-concluzii">Capitolul 9. Concluzii</h2>',
        f"""
{idx("SUB-030")}<h3>9.1. Cariera si bani</h3>
{idx("P-038")}<p>{active}, cariera si banii se citesc aici ca potential de mediu, nu ca alegere adulta. Matricea arata ca zona cea mai puternica este {html.escape(matrix["scara_bunastarii"][0]["denumire"])}, iar Destinul {b(destin_interp)} cere sa transformi energia nativa in deprindere, responsabilitate si rezultat potrivit varstei.</p>
{idx("P-039")}<p>Aplicabilitatea profesionala DA este Arcana {b(da_number)} - {html.escape(da_name)}: resursa de lucru. Obstacolul NU este Arcana {b(nu_number)} - {html.escape(nu_name)}: nu lipsa de talent, ci tiparul care trebuie educat. Pentru un copil, asta inseamna jocuri, sarcini mici, incurajare si un criteriu clar pentru ce inseamna terminat.</p>
{idx("T-016")}<div class="table-wrap"><table><thead><tr><th>Aplicabilitate profesionala DA</th><th>Aplicabilitate profesionala NU</th></tr></thead><tbody><tr><td><img src="{data_uri(da_img)}" alt="Arcana {da_number} - {html.escape(da_name)}"><br>{b(da_number)} - {html.escape(da_name)}</td><td><img src="{data_uri(nu_img)}" alt="Arcana {nu_number} - {html.escape(nu_name)}"><br>{b(nu_number)} - {html.escape(nu_name)}</td></tr><tr><td>Resursa profesionala se maturizeaza prin activitati in care poti vedea efectul concret al actiunilor tale.</td><td>Obstacolul se transforma prin rabdare, etape scurte si acceptarea faptului ca rezultatul bun se construieste in timp.</td></tr></tbody></table></div>
{idx("P-040")}<p>Numarul ereditar karmic {b(neam_number)} adauga tema neamului: mostenirea se foloseste matur cand familia incurajeaza constructia, reparatia, adevarul spus limpede si responsabilitatea fara presiune.</p>
{idx("SUB-031")}<h3>9.2. Iubire si relatii</h3>
{idx("P-041")}<p>Nu exista relatie declarata in fisa, deci nu inventam un capitol relational. In lectura generala, iubirea se construieste prin siguranta, comparatii putine, ascultare si libertatea de a avea propriul ritm. Energia relationala se maturizeaza cand copilul simte ca poate fi vazut fara sa joace un rol fix.</p>
{idx("SUB-032")}<h3>9.3. Momentul prezent</h3>
{idx("P-042")}<p>In momentul prezent, {active} are {years_old} ani si se afla in Pinaclul {b(current_pin["pinaclu"])}, in ciclul de 12 ani activ al formarii si in anul personal {b(current_cycle["an_personal"])}. Lectia activa {b(current_cycle["lectie"])} cere un mediu cu ritm, corp, joc, limbaj emotional si reguli explicate calm. Recomandarea practica este sa fie sustinuta curiozitatea, dar sa existe mereu un pas concret de incheiere.</p>
"""))

    body = "\n".join(sections)
    model = MODEL_HTML.read_text(encoding="utf-8")
    css = re.search(r"<style>(.*?)</style>", model, re.S).group(1)
    document = f"""<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(name)} - {birth_ro}</title>
<style>{css}</style>
</head>
<body>
<header><div class="title">{html.escape(name)} · lucrare numerologica scurta</div><div class="meta">Revizie V1.00R · 10.08.2026 · The Scribe</div></header>
<main>{body}</main>
</body>
</html>
"""
    return enhance_html(document, person, report, out_dir, prefix)


def replace_indexed_paragraph(text: str, prefix: str, suffix: str, body: str) -> str:
    pattern = rf'(<div class="idx">Index: {re.escape(prefix)}-{re.escape(suffix)}</div>)<p>.*?</p>'
    updated, count = re.subn(pattern, lambda match: match.group(1) + f"<p>{body}</p>", text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"Paragraful {prefix}-{suffix} nu a fost găsit o singură dată: {count}")
    return updated


def replace_indexed_paragraphs(text: str, prefix: str, suffix: str, bodies: list[str]) -> str:
    pattern = rf'(<div class="idx">Index: {re.escape(prefix)}-{re.escape(suffix)}</div>)<p>.*?</p>'
    paragraphs = "".join(f"<p>{body}</p>" for body in bodies)
    updated, count = re.subn(pattern, lambda match: match.group(1) + paragraphs, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"Paragraful {prefix}-{suffix} nu a fost găsit o singură dată: {count}")
    return updated


def matrix_interpretation(digit: int, count: int, prefix: str) -> str | None:
    victor = {
        (1, 3): "<strong>Căsuța 1.</strong> Reprezintă psihicul, voința, inițiativa și felul în care îți afirmi propria direcție. Ai <strong>3</strong> apariții în căsuța cifrei <strong>1</strong>, ceea ce arată o energie psihică activă, mobilă și orientată spre exprimare. Poți porni repede, poți susține ceea ce îți dorești și poți transmite multă hotărâre celor din jur. Ai nevoie să fii ascultat și să simți că ideile tale au loc, iar când mediul îți oferă alegeri potrivite vârstei poți deveni curajos, inventiv și foarte implicat. Umbra apare când impulsul de a conduce se transformă în grabă, încăpățânare sau reacție puternică la limite. Uneori poți insista înainte să auzi până la capăt ce ți se spune ori poți consuma multă energie încercând să îți impui ritmul. Maturizarea acestei căsuțe înseamnă să înveți să ceri clar, să asculți răspunsul și să folosești inițiativa pentru a mobiliza și a construi, nu pentru a ocupa tot spațiul deciziei.",
        (2, 2): "<strong>Căsuța 2.</strong> Reprezintă emoțiile, trăirile, comunicarea, bioenergia, spiritul de colaborare și parteneriatul. Ai <strong>2</strong> apariții în căsuța cifrei <strong>2</strong>. Sensibilitatea și capacitatea de a lucra cu celălalt sunt prezente, dar au nevoie de aport extern și exercițiu pentru a rămâne stabile. Fiind un număr par de apariții, energia poate circula în ambele sensuri: poți primi și poți da mai departe sprijin emoțional, însă în anumite situații poate apărea indecizia. Pentru tine, maturizarea acestei căsuțe înseamnă să numești clar ceea ce simți, să întrebi direct ce are nevoie celălalt și să alegi după dialog, fără să rămâi blocat între două variante.",
        (3, 2): "<strong>Căsuța 3.</strong> Ai <strong>2</strong> apariții în căsuța cifrei <strong>3</strong>, ceea ce arată că ești capabil atât să primești informația, cât și să o prelucrezi și să o dai mai departe într-o formă accesibilă celorlalți. Poți avea abilități foarte bune de mentor sau dascăl, mai ales atunci când faci legătura dintre idei, extragi esența și o explici clar. Cele <strong>2</strong> apariții pot aduce însă și nehotărâre în raport cu informația: poți acumula foarte mult, poți oscila între mai multe interpretări sau poți amâna alegerea unei direcții. Pentru a echilibra această energie, te ajută să selectezi informațiile esențiale, să le organizezi și să hotărăști ce merită aplicat sau transmis. Altfel, există riscul să te împrăștii în prea multe direcții și să risipești energia înainte ca ideile să devină rezultate. Cu cât îți ordonezi mai bine informația și iei decizii mai ferme, cu atât această căsuță îți susține mai puternic comunicarea, relațiile și capacitatea de a-i ghida pe ceilalți.",
        (3, 1): "<strong>Căsuța 3.</strong> Ai <strong>1</strong> apariție. Relațiile și prelucrarea informației sunt disponibile, dar au nevoie de focalizare. Curiozitatea te ajută să cercetezi; maturizarea apare când selectezi esențialul și îl transmiți fără să te risipești.",
        (4, 0): "<strong>Căsuța 4.</strong> Reprezintă corpul fizic, sănătatea, spiritul practic, orientarea spre rezultate concrete, organizarea, cadrul, trăinicia, statornicia și temeinicia. În matricea ta nu ai nicio apariție în căsuța cifrei <strong>4</strong>, ceea ce arată că această energie este conservată: nu o poți accesa întotdeauna când dorești și în aceeași măsură. Pot exista perioade în care te simți foarte sănătos și rezistent, dar și momente în care chiar o răceală ușoară te poate solicita mai mult decât te-ai aștepta. Energia poate oscila între „foarte mult” și „foarte puțin”, iar aceeași alternanță se poate vedea în organizare, disciplină și consecvență. Pentru a echilibra această căsuță, te ajută să ai planuri clare, un program stabil și obiceiuri pe care le respecți chiar și atunci când nu simți presiunea imediată a rezultatului. Acordă atenție constantă sănătății, somnului și alimentației și introdu mișcarea sau sportul în rutina ta, într-un ritm regulat și potrivit corpului tău.",
        (5, 0): "<strong>Căsuța 5.</strong> Reprezintă libertatea, stima de sine, imunitatea sistemică, nonconformismul — ieșirea din pătrat — spiritul de aventură, oportunismul și curajul. În matricea ta nu ai nicio apariție în căsuța cifrei <strong>5</strong>, ceea ce arată că această energie este conservată și poate fi activată prin factori externi. Aceștia pot fi oamenii care te susțin să îți construiești încrederea în tine sau conjuncturile care te provoacă să îți depășești limitele, să ieși din tipare și să îți ridici stima de sine. De-a lungul vieții, te ajută să încerci roluri diferite și să intri conștient în contexte în care îți exersezi curajul, libertatea de alegere și capacitatea de adaptare. Este la fel de important să te înconjori de oameni care îți recunosc potențialul și te încurajează să crești, nu de persoane care îți micșorează încrederea. Cu cât îți alegi mai bine mediul și experiențele, cu atât energia lui <strong>5</strong> te ajută să ieși din „pătrat” și să îți construiești o libertate autentică, susținută de încredere în tine.",
        (5, 1): "<strong>Căsuța 5.</strong> Ai <strong>1</strong> apariție în căsuța cifrei <strong>5</strong>. Libertatea, curajul, adaptarea și dorința de experiențe noi sunt accesibile, dar trebuie educate cu măsură. Umbra este confundarea libertății cu lipsa limitelor; maturizarea apare prin alegeri asumate și revenirea la un punct stabil după fiecare explorare.",
        (7, 0): "<strong>Căsuța 7.</strong> Nu ai apariții. Analiza profundă, răbdarea și înțelepciunea sunt energii conservate. Ele se construiesc prin studiu, repaus, natură, întrebări bune și experiențe care te ajută să încetinești înainte de a răspunde.",
        (6, 1): "<strong>Căsuța 6.</strong> Reprezintă iubirea ca ocrotire, instinctele, arta, realismul și pragmatismul. Ai <strong>1</strong> apariție în căsuța cifrei <strong>6</strong>, ceea ce îți oferă acces la grija exprimată prin gesturi concrete și la capacitatea de a transforma o idee într-un lucru folositor. Poți arăta afecțiunea ajutând, construind, reparând sau participând la ceea ce face familia, mai ales când sarcina este clară și rezultatul poate fi văzut. Umbra apare când grija devine posesivitate, când vrei să faci lucrurile numai în felul tău ori când interesul pentru rezultat scade în fața părții repetitive a muncii. Maturizarea acestei căsuțe se construiește prin responsabilități mici, activități artistice și practice, ordine în obiectele proprii și învățarea diferenței dintre a ocroti pe cineva și a prelua totul în locul lui.",
        (7, 2): "<strong>Căsuța 7.</strong> Reprezintă observația, analiza, studiul, experimentarea și capacitatea de a găsi sensul din spatele unei experiențe. Ai <strong>2</strong> apariții în căsuța cifrei <strong>7</strong>, ceea ce face această energie activă în ambele sensuri: poți primi idei și repere din mediul apropiat, apoi le poți întoarce sub formă de întrebări, concluzii sau soluții proprii. Poți observa detalii pe care alții le trec cu vederea și poți avea nevoie să înțelegi de ce funcționează un lucru, nu doar să accepți regula. Cele <strong>2</strong> apariții pot aduce însă și oscilație între încredere și îndoială, între dorința de a cerceta și retragerea prea lungă în propriile gânduri. Maturizarea apare când timpul de liniște este urmat de verificare, dialog și experiment concret. Studiul, natura, jocurile de strategie și întrebările la care cauți răspuns pas cu pas transformă analiza în înțelepciune practică, fără izolare sau supragândire.",
        (8, 1): "<strong>Căsuța 8.</strong> Reprezintă puterea, responsabilitatea, spiritul de sacrificiu, elitismul, măiestria — performanța — ambiția, succesul în afaceri și în poziții de putere, precum și patriotismul. Ai <strong>1</strong> apariție în căsuța cifrei <strong>8</strong>. Această energie te ajută să gestionezi responsabilitatea și rezultatul, atât timp cât rămâi echitabil și nu preiei mai mult decât îți aparține.",
        (9, 1): "<strong>Căsuța 9.</strong> Reprezintă inteligența mentală, memoria, compasiunea, învățarea, finalizarea și capacitatea de transformare. Ai <strong>1</strong> apariție în căsuța cifrei <strong>9</strong>, ceea ce îți oferă acces la înțelegerea de ansamblu și la legarea experiențelor într-o concluzie. Poți învăța bine atunci când informația are sens, este asociată unei povești și poate fi folosită într-o situație reală. Umbra apare când imaginea mare te face să treci prea repede peste detalii sau când o concluzie intuită nu este verificată. Îți dezvolți această energie prin lectură, conversație, recapitulare, proiecte duse până la capăt și exercițiul de a spune nu doar ce ai înțeles, ci și pe ce observații se bazează.",
    }
    if prefix.startswith("VVD-"):
        return victor.get((digit, count))
    ingrid = {
        (1, 1): "<strong>Căsuța 1.</strong> Reprezintă psihicul, voința, inițiativa și felul în care îți afirmi propria direcție. Ai <strong>1</strong> apariție în căsuța cifrei <strong>1</strong>, ceea ce îți oferă acces direct la această energie, dar cere experiență și exercițiu pentru a deveni stabilă. Pe măsură ce crești, poți arăta inițiativă atunci când înțelegi ce ai de făcut și simți că ai un spațiu sigur în care să încerci. Resursa este capacitatea de a porni, de a spune ce îți dorești și de a susține o alegere fără să ai nevoie să controlezi întregul context. Umbra poate fi alternanța dintre curaj și retragere, reacția puternică atunci când nu ești înțeleasă sau renunțarea când primul impuls nu primește răspuns. Maturizarea acestei căsuțe se construiește prin alegeri simple, sarcini potrivite vârstei, încurajarea inițiativei și învățarea răbdării dintre dorință, cerere și rezultat.",
        (2, 2): "<strong>Căsuța 2.</strong> Reprezintă emoțiile, trăirile, comunicarea, bioenergia, spiritul de colaborare și parteneriatul. Ai <strong>2</strong> apariții în căsuța cifrei <strong>2</strong>. Sensibilitatea și capacitatea de a lucra cu celălalt sunt prezente, dar au nevoie de aport extern și exercițiu pentru a rămâne stabile. Fiind un număr par de apariții, energia poate circula în ambele sensuri: poți primi și poți da mai departe sprijin emoțional, însă în anumite situații poate apărea indecizia. Pentru tine, maturizarea acestei căsuțe înseamnă să numești clar ceea ce simți, să întrebi direct ce are nevoie celălalt și să alegi după dialog, fără să rămâi blocată între două variante.",
        (3, 1): "<strong>Căsuța 3.</strong> Reprezintă relaționarea, curiozitatea și capacitatea de a primi, organiza și transmite informația. Ai <strong>1</strong> apariție în căsuța cifrei <strong>3</strong>, ceea ce îți oferă acces direct la această energie, dar cere folosire conștientă pentru a deveni stabilă. Poți înțelege prin poveste, joc, imagine și dialog, mai ales când informația are un fir clar și un scop concret. Umbra poate fi graba de a trece la altă idee înainte ca prima să fie înțeleasă sau dificultatea de a explica ceea ce ai intuit deja. Te ajută să repeți cu propriile cuvinte, să pui întrebări, să alegi informația esențială și să duci o idee până la o concluzie înainte de a deschide alta.",
        (4, 0): "<strong>Căsuța 4.</strong> Reprezintă corpul fizic, sănătatea, spiritul practic, orientarea spre rezultate concrete, organizarea, cadrul, trăinicia, statornicia și temeinicia. În matricea ta nu ai nicio apariție în căsuța cifrei <strong>4</strong>, ceea ce arată că această energie este conservată: nu o poți accesa întotdeauna când dorești și în aceeași măsură. Pot exista perioade în care te simți foarte sănătoasă și rezistentă, dar și momente în care chiar o răceală ușoară te poate solicita mai mult decât te-ai aștepta. Energia poate oscila între „foarte mult” și „foarte puțin”, iar aceeași alternanță se poate vedea în organizare, disciplină și consecvență. Pentru a echilibra această căsuță, te ajută să ai planuri clare, un program stabil și obiceiuri pe care le respecți chiar și atunci când nu simți presiunea imediată a rezultatului. Acordă atenție constantă sănătății, somnului și alimentației și introdu mișcarea sau sportul în rutina ta, într-un ritm regulat și potrivit corpului tău.",
        (5, 1): "<strong>Căsuța 5.</strong> Ai <strong>1</strong> apariție în căsuța cifrei <strong>5</strong>, ceea ce arată că libertatea, curajul, stima de sine, adaptarea și dorința de experiențe noi sunt prezente în structura ta, dar trebuie educate cu măsură. Această energie îți poate da vioiciune, curiozitate, spontaneitate și dorința de a ieși din tipare, de a încerca, de a te mișca, de a explora și de a simți că ai spațiu să alegi. Fiind o singură apariție, curajul poate alterna: uneori poți fi foarte îndrăzneață și atrasă de noutate, iar alteori poți avea nevoie de încurajare ca să nu confunzi siguranța cu blocajul sau libertatea cu fuga de reguli. Umbra căsuței este impulsul de a face doar ce îți place pe moment, de a protesta când apar limite sau de a căuta atenție prin nonconformism. Maturizarea apare când înveți că libertatea adevărată nu înseamnă lipsă de responsabilitate, ci alegeri asumate, curaj folosit cu discernământ și experiențe noi care te cresc, nu te împrăștie.",
        (6, 1): "<strong>Căsuța 6.</strong> Reprezintă iubirea ca ocrotire, instinctele, arta, realismul și pragmatismul. Ai <strong>1</strong> apariție în căsuța cifrei <strong>6</strong>, ceea ce îți oferă acces la grija exprimată prin gesturi concrete și la capacitatea de a transforma o idee într-un lucru folositor. Poți arăta afecțiunea ajutând, construind, reparând sau participând la ceea ce face familia, mai ales când sarcina este clară și rezultatul poate fi văzut. Umbra apare când grija devine posesivitate, când vrei să faci lucrurile numai în felul tău ori când interesul pentru rezultat scade în fața părții repetitive a muncii. Maturizarea acestei căsuțe se construiește prin responsabilități mici, activități artistice și practice, ordine în obiectele proprii și învățarea diferenței dintre a ocroti pe cineva și a prelua totul în locul lui.",
        (7, 0): "<strong>Căsuța 7.</strong> Nu ai apariții în căsuța cifrei <strong>7</strong>, iar asta arată că observația profundă, răbdarea, înțelepciunea, credința și legătura cu spiritualitatea sunt energii conservate. Este indicat să te implici sufletește și spiritual în ceea ce faci în viața actuală și să dai o atenție deosebită religiei, rugăciunii, sensului interior și faptelor bune. Când această casetă este conservată, energia poate oscila: în anumite momente poți simți o apropiere puternică de Dumnezeu, de spiritualitate sau de lucrurile nevăzute, iar în alte momente poți reacționa impulsiv, fără răbdare, fără încredere și fără să vezi lecția mai adâncă a situației. Uneori, până la o anumită vârstă, omul poate respinge credința sau poate fi indiferent față de ea, iar apoi, în urma unor întâmplări importante, se poate apropia brusc de religie ori de o practică spirituală. Pentru tine, direcția sănătoasă nu este fanatismul, ci apropierea treptată, curată și echilibrată de spiritualitate, prin rugăciune, recunoștință, studiu, liniște și fapte concrete. Ca sfat de ocrotire, este bine să dăruiești cât poți către oameni săraci, neajutorați sau aflați în nevoie, nu ca obligație, ci ca mod de a deschide inima și de a transforma sensibilitatea în protecție și bine. Cu cât te apropii mai conștient de credință, compasiune și înțelepciune, cu atât această casetă te ajută să eviți complicațiile inutile și să alegi un drum mai limpede, mai blând și mai matur.",
        (8, 3): "<strong>Căsuța 8.</strong> Reprezintă puterea, responsabilitatea, simțul datoriei, ambiția, performanța și felul în care administrezi resursele ori autoritatea. Ai <strong>3</strong> apariții în căsuța cifrei <strong>8</strong>, ceea ce arată o energie puternică, activă și orientată spre exterior. Pe măsură ce crești, poți observa repede cine conduce, cum sunt împărțite rolurile și dacă regulile sunt respectate. Poți dori să ai un cuvânt important de spus, să protejezi ceea ce consideri al tău și să obții un rezultat vizibil, mai ales când primești o responsabilitate clară. Umbra poate fi presiunea pusă asupra ta sau asupra celorlalți, competiția pentru control, dificultatea de a accepta un refuz ori tendința de a confunda valoarea personală cu reușita. Energia se maturizează când înveți că puterea înseamnă și echitate, răbdare, respectarea promisiunilor și grija pentru efectul pe care deciziile tale îl au asupra oamenilor. Sarcinile potrivite vârstei, regulile consecvente și aprecierea efortului, nu doar a rezultatului, transformă această intensitate în responsabilitate, curaj și capacitate reală de conducere.",
        (9, 1): "<strong>Căsuța 9.</strong> Reprezintă inteligența mentală, memoria, compasiunea, învățarea, finalizarea și capacitatea de transformare. Ai <strong>1</strong> apariție în căsuța cifrei <strong>9</strong>, ceea ce îți oferă acces la înțelegerea de ansamblu și la legarea experiențelor într-o concluzie. Poți învăța bine atunci când informația are sens, este asociată unei povești și poate fi folosită într-o situație reală. Umbra apare când imaginea mare te face să treci prea repede peste detalii sau când o concluzie intuită nu este verificată. Îți dezvolți această energie prin lectură, conversație, recapitulare, proiecte duse până la capăt și exercițiul de a spune nu doar ce ai înțeles, ci și pe ce observații se bazează.",
    }
    if prefix.startswith("DIP-"):
        return ingrid.get((digit, count))
    known = {
        (2, 2): "<strong>Căsuța 2.</strong> Ai <strong>2</strong> apariții. Emoțiile, comunicarea și colaborarea circulă în ambele sensuri: poți primi și oferi sprijin. Numărul par de apariții poate aduce indecizie, de aceea te ajută să numești ce simți și să alegi după un dialog clar.",
        (3, 2): "<strong>Căsuța 3.</strong> Ai <strong>2</strong> apariții în căsuța cifrei <strong>3</strong>, ceea ce arată că poți primi informația, o poți prelucra și o poți transmite într-o formă accesibilă. Poți face legături bune între idei și poți explica limpede ceea ce ai înțeles. Cele două apariții pot aduce și oscilație între mai multe interpretări; te ajută să alegi informația esențială, să o organizezi și să duci o direcție până la rezultat.",
        (3, 1): "<strong>Căsuța 3.</strong> Ai <strong>1</strong> apariție. Relațiile și prelucrarea informației sunt disponibile, dar au nevoie de focalizare. Curiozitatea te ajută să cercetezi; maturizarea apare când selectezi esențialul și îl transmiți fără să te risipești.",
        (4, 0): "<strong>Căsuța 4.</strong> Reprezintă corpul fizic, sănătatea, spiritul practic, organizarea și orientarea spre rezultate concrete. Lipsa cifrei <strong>4</strong> arată o energie conservată, care poate oscila între perioade de rezistență și momente în care corpul ori disciplina cer mai multă atenție. Echilibrul se construiește prin somn, alimentație, mișcare, program stabil și obiceiuri simple, repetate fără presiune.",
        (5, 0): "<strong>Căsuța 5.</strong> Nu ai apariții, iar energia libertății, stimei de sine, curajului și nonconformismului este conservată. Ea se activează prin oameni și contexte care te încurajează să ieși din tipare. Construiește-o prin experiențe noi, limite sănătoase și alegeri asumate.",
        (5, 1): "<strong>Căsuța 5.</strong> Ai <strong>1</strong> apariție în căsuța cifrei <strong>5</strong>. Libertatea, curajul, adaptarea și dorința de experiențe noi sunt accesibile, dar trebuie educate cu măsură. Umbra este confundarea libertății cu lipsa limitelor; maturizarea apare prin alegeri asumate și revenirea la un punct stabil după fiecare explorare.",
        (7, 0): "<strong>Căsuța 7.</strong> Nu ai apariții. Analiza profundă, răbdarea și înțelepciunea sunt energii conservate. Ele se construiesc prin studiu, repaus, natură, întrebări bune și experiențe care te ajută să încetinești înainte de a răspunde.",
        (8, 1): "<strong>Căsuța 8.</strong> Ai <strong>1</strong> apariție. Puterea, responsabilitatea și performanța sunt disponibile într-o formă echilibrată. Folosește-le pentru a administra corect și a duce lucrurile până la capăt, fără să preiei poverile tuturor.",
        (9, 1): "<strong>Căsuța 9.</strong> Reprezintă inteligența mentală, memoria, compasiunea, învățarea, finalizarea și transformarea. Ai <strong>1</strong> apariție, ceea ce îți oferă acces la imaginea de ansamblu. Dezvolți această energie prin lectură, conversație, recapitulare, proiecte încheiate și verificarea observațiilor pe care se bazează concluziile tale.",
    }
    return known.get((digit, count))


def enhance_html(text: str, person: dict[str, str], report: dict, out_dir: Path, prefix: str) -> str:
    calc = report["capitolul_2_formule_calcule_tabele_grafice"]
    base = calc["2.1_codul_numerologic_personal_data_nasterii"]
    matrix = calc["2.2_structura_matriciala"]
    name_data = calc["2.3_codul_numerologic_personal_al_numelui"]
    cycles = calc["2.4_ciclicitati"]
    prof = calc["2.6_spiritul"]["inclinatii_profesionale"]
    born = datetime.strptime(person["data_nasterii"], "%Y-%m-%d").date()
    active = person["prenume_activ"]
    vi = base["vibratia_interioara"]["calcul"]["rezultat"]
    ve = base["vibratia_exterioara"]["calcul"]["rezultat"]
    calea = base["calea_destinului"]["rezultat"]
    destin = base["destinul_vibratia_destinului"]["cifra_interpretare"]["rezultat"]
    current = next(row for row in cycles["ciclul_de_9_ani"] if row["an"] == TODAY.year)
    pin = cycles["pinacluri"]["randuri"][0]
    has_relation = person["nume_complet"] == "Vulcu Victor Daniel"

    if person["nume_familie"] == "Vulcu":
        neam_number = arcana_value(name_data["numarul_ereditar_karmic_neamul"]["arcana_majora"])
        neam_name = ARCANA[neam_number][0]
        neam_img = out_dir / f"tarot-{neam_number:02d}-{slug(neam_name)}-numarul-ereditar-karmic.jpg"
        family_block = f'''{idx_html(prefix, "SUB-021")}<h3 id="5-4-numarul-ereditar-karmic">5.4. Numărul ereditar karmic</h3>
{idx_html(prefix, "P-022b")}<p>Numărul ereditar karmic citește numele de familie în intervalul simbolic <strong>1–22</strong> și evidențiază o lecție arhetipală a neamului. El arată ce tipar cere înțelegere și maturizare, astfel încât resursele moștenite să fie folosite fără repetarea automată a limitelor trecutului.</p>
{idx_html(prefix, "C-005")}<aside class="callout example"><p><strong>Calcul în intervalul 1–22</strong><br>Vulcu = <strong>16</strong></p><p>Arcana neamului = <strong>16 — Turnul</strong></p></aside>
{idx_html(prefix, "T-013")}<div class="table-wrap"><table class="tarot-profile-table"><tbody><tr><td>Index: {prefix}-G-003<br><img src="{data_uri(neam_img)}" data-source="{neam_img.name}" alt="Arcana 16 — Turnul"><div class="tarot-image-caption"><em>Arcana <strong>16</strong> — Turnul</em></div></td><td><ul><li><strong>Resursă moștenită:</strong> capacitatea de a vedea rapid ce nu mai este stabil, ce este construit pe frică, aparență sau compromis și ce are nevoie să fie reclădit pe baze reale.</li><li><strong>Manifestare:</strong> curajul de a schimba structuri vechi, reguli, obiceiuri sau tipare de familie atunci când ele nu mai susțin viața, adevărul și dezvoltarea.</li><li><strong>Umbră:</strong> teamă de pierdere, reacții bruște, rezistență la schimbare sau tendința de a păstra o formă cunoscută până când presiunea devine prea mare și lucrurile se rup singure.</li><li><strong>Maturizare:</strong> construirea unei siguranțe interioare care nu depinde doar de forme vechi, ci de adevăr, responsabilitate, ordine nouă și capacitatea de a reconstrui pas cu pas după o clarificare.</li></ul></td></tr></tbody></table></div>
{idx_html(prefix, "P-022e")}<p>Neamul <strong>16</strong> este Neamul Constructorilor, al celor care construiesc lucruri mari și repară ceea ce s-a distrus. Cei născuți dintr-un astfel de neam pot avea o atracție firească spre construcții, reparații, unelte, mecanisme și orice activitate în care ceva trebuie ridicat, refăcut sau consolidat. Nu este obligatoriu ca sarcina ta să fie să construiești case, însă este bine să fii deschis atunci când vine vorba despre reînnoirea casei, a apartamentului, a spațiului în care trăiești sau a lucrurilor care cer să fie reparate. În linia acestui neam există simbolic taine ale construcției transmise din generație în generație: priceperea de a mânui unelte, de a înțelege structuri, de a ridica ceva util și de a reconstrui acolo unde alții văd doar ruină.</p>
{idx_html(prefix, "P-022c")}<p>Numărul ereditar karmic <strong>16</strong>, asociat Turnului, vorbește despre o moștenire în care adevărul cere uneori restructurare. {active}, poți duce mai departe resursa de a vedea unde o construcție nu mai este sinceră, unde regulile vechi nu mai ajută și unde este nevoie de o bază mai curată. Turnul nu înseamnă distrugere de dragul distrugerii, ci momentul în care ceea ce era fragil, fals sau prea rigid trebuie dat jos pentru ca viața să poată fi așezată mai drept. În linia de neam, această arcană poate arăta familii care au trecut prin schimbări bruște, rupturi, mutări, pierderi de siguranță sau situații în care a fost nevoie să se reconstruiască de la zero.</p>
{idx_html(prefix, "P-022d")}<p>Umbra lui <strong>16</strong> este să te agăți de forme care par sigure, dar nu mai susțin viața, sau să reacționezi prea brusc atunci când ceva se clatină. Maturizarea apare când accepți schimbarea ca pe o șansă de curățare, nu ca pe o pedeapsă, și când înveți să reconstruiești cu răbdare: spui adevărul, pui limite, alegi ce merită păstrat și renunți la ceea ce nu mai are temelie. Astfel, Turnul devine o forță de eliberare: nu mai lasă neamul să trăiască în structuri vechi doar pentru că sunt cunoscute, ci deschide drumul spre o siguranță mai sinceră, construită conștient.</p>
'''
        old_family_block = rf'<div class="idx">Index: {re.escape(prefix)}-P-024</div>.*?(?=<div class="idx">Index: {re.escape(prefix)}-C-011</div>)'
        text, family_count = re.subn(old_family_block, lambda _: family_block, text, count=1, flags=re.S)
        if family_count != 1:
            raise RuntimeError("Secțiunea Numărul ereditar karmic nu a fost înlocuită.")
    elif person["nume_familie"] == "Docolin":
        neam_number = arcana_value(name_data["numarul_ereditar_karmic_neamul"]["arcana_majora"])
        neam_name = ARCANA[neam_number][0]
        neam_img = out_dir / f"tarot-{neam_number:02d}-{slug(neam_name)}-numarul-ereditar-karmic.jpg"
        family_block = f'''{idx_html(prefix, "SUB-021")}<h3 id="5-4-numarul-ereditar-karmic">5.4. Numărul ereditar karmic</h3>
{idx_html(prefix, "P-022b")}<p>Numărul ereditar karmic citește numele de familie în intervalul simbolic <strong>1–22</strong> și evidențiază o lecție arhetipală a neamului. El arată ce tipar cere înțelegere și maturizare, astfel încât resursele moștenite să fie folosite fără repetarea automată a limitelor trecutului.</p>
{idx_html(prefix, "C-005")}<aside class="callout example"><p><strong>Calcul în intervalul 1–22</strong><br>Docolin = <strong>14</strong></p><p>Arcana neamului = <strong>14 — Cumpătarea</strong></p></aside>
{idx_html(prefix, "T-013")}<div class="table-wrap"><table class="tarot-profile-table"><tbody><tr><td>Index: {prefix}-G-003<br><img src="{data_uri(neam_img)}" data-source="{neam_img.name}" alt="Arcana 14 — Cumpătarea"><div class="tarot-image-caption"><em>Arcana <strong>14</strong> — Cumpătarea</em></div></td><td><ul><li><strong>Resursă moștenită:</strong> cumpătarea, răbdarea și priceperea de a lucra în acord cu ritmurile naturale, transformând treptat resursele disponibile în rezultate hrănitoare și durabile.</li><li><strong>Manifestare:</strong> apropierea de pământ, plante, hrană, creștere, îngrijire și procese în care două elemente sunt combinate cu măsură pentru a obține un rezultat mai bun.</li><li><strong>Umbră:</strong> stagnarea în ceea ce este familiar, acceptarea unei vieți prea restrânse ori amânarea schimbării din teama de a tulbura echilibrul deja cunoscut.</li><li><strong>Maturizare:</strong> păstrarea măsurii fără renunțarea la evoluție, folosirea experienței practice cu deschidere și cultivarea unei stabilități care poate hrăni atât familia, cât și comunitatea.</li></ul></td></tr></tbody></table></div>
{idx_html(prefix, "P-022e")}<p>Neamul 14 - Neamul Agricultorilor, cumpatati, echilibrati, legati de pamant - scopul principal al acestui neam a fost dintotdeauna sa se ocupe de agricultura, incrucisari, altoiri, sa descopere noi metode de crestere a plantelor, fructelor si legumelor, sa descopere specii noi de plante si, evident, sa asigure familia si lumea cu astfel de produse. In esenta, acesta este un neam taranesc, foarte priceput in tainele agriculturii. Neamul nu este unul foarte bogat, dar cu toate acestea nici unul sarac. In Romania, acest neam, candva, hranea o Europa intreaga.</p>
'''
        old_family_block = rf'<div class="idx">Index: {re.escape(prefix)}-P-024</div>.*?(?=<div class="idx">Index: {re.escape(prefix)}-C-011</div>)'
        text, family_count = re.subn(old_family_block, lambda _: family_block, text, count=1, flags=re.S)
        if family_count != 1:
            raise RuntimeError("Secțiunea Numărul ereditar karmic pentru Docolin nu a fost înlocuită.")

    expression_components = name_data["numarul_de_exprimare"]["componente"]
    component_values = [component["reducere"]["rezultat"] for component in expression_components]
    component_summary = ", ".join(
        f'{html.escape(component["componenta"])} = {component["reducere"]["rezultat"]}'
        for component in expression_components
    )
    component_sum = " + ".join(str(value) for value in component_values)
    expression_total = name_data["numarul_de_exprimare"]["total_reduse"]
    expression_result = name_data["numarul_de_exprimare"]["reducere"]["rezultat"]
    expression_steps = name_data["numarul_de_exprimare"]["reducere"]["pasi"]
    reduction_suffix = ""
    if expression_steps:
        final_step = expression_steps[-1].rsplit(" = ", 1)[0]
        reduction_suffix = f' → {html.escape(final_step)} = <strong>{expression_result}</strong>'
    expression_callout = (
        f'{idx_html(prefix, "C-012")}<aside class="callout example"><p><strong>Calcul</strong><br>'
        f'{component_summary} → {component_sum} = <strong>{expression_total}</strong>{reduction_suffix}</p></aside>'
    )
    code_index = f'<div class="idx">Index: {prefix}-C-011</div>'
    if code_index not in text:
        raise RuntimeError("Nu pot insera calculul Numărului de exprimare înainte de C-011.")

    if person["nume_familie"] == "Docolin":
        def calculation(label: str, data: dict) -> str:
            values = " + ".join(str(item["valoare"]) for item in data["valori"])
            steps = " → ".join(data["reducere"]["pasi"])
            suffix = f" → {html.escape(steps)}" if steps else ""
            return f'{html.escape(label)} = {values} = <strong>{data["total"]}</strong>{suffix}'

        active_number = name_data["numarul_activ"]["reducere"]["rezultat"]
        intimate_number = name_data["numarul_intim"]["reducere"]["rezultat"]
        inherited_number = name_data["numarul_ereditar"]["reducere"]["rezultat"]
        realization_number = name_data["numarul_de_realizare"]["reducere"]["rezultat"]

        code_tail_match = re.search(
            rf'(<div class="idx">Index: {re.escape(prefix)}-C-011</div>.*?)(?=\s*</section>\s*<section><div class="idx">Index: {re.escape(prefix)}-CAP-009</div>)',
            text,
            flags=re.S,
        )
        if not code_tail_match:
            raise RuntimeError("Nu pot păstra blocul codului numerologic al numelui pentru Ingrid.")
        code_tail = code_tail_match.group(1)

        name_section = f'''<section>{idx_html(prefix, "CAP-009")}<h2 id="capitolul-5-numele">Capitolul 5. Numele — Eu și neamul</h2>
{idx_html(prefix, "SUB-018")}<h3 id="5-1-numarul-activ">5.1. Numărul activ</h3>
{idx_html(prefix, "P-020a")}<p>Numărul activ este influența directă a prenumelui folosit zi de zi. El arată energia cu care intri într-un context, reacția obișnuită și felul în care inițiativa ta devine vizibilă.</p>
{idx_html(prefix, "C-009")}<aside class="callout example"><p><strong>Calcul</strong><br>{calculation(active, name_data["numarul_activ"])}</p></aside>
{idx_html(prefix, "P-021")}<p>Numărul activ <strong>{active_number}</strong> aduce în comportamentul tău observație, profunzime și nevoia de a înțelege înainte de a te deschide. Resursa este discernământul; umbra poate fi retragerea sau neîncrederea, iar maturizarea apare când curiozitatea interioară este exprimată prin întrebări clare și experiențe concrete.</p>
{idx_html(prefix, "SUB-019")}<h3 id="5-2-numarul-intim">5.2. Numărul intim</h3>
{idx_html(prefix, "P-021b")}<p>Numărul intim se calculează din vocalele numelui complet și descrie motivația afectivă, dorințele profunde și ceea ce îți hrănește lumea interioară.</p>
{idx_html(prefix, "C-009a")}<aside class="callout example"><p><strong>Calcul</strong><br>{calculation("Vocalele numelui", name_data["numarul_intim"])}</p></aside>
{idx_html(prefix, "P-021c")}<p>Numărul intim <strong>{intimate_number}</strong> caută sens, generozitate și sentimentul că experiențele pot fi folositoare și altora. Te hrănesc poveștile, imaginația și gesturile de compasiune; umbra este dezamăgirea când realitatea nu corespunde idealului, iar maturizarea cere limite afective și încheierea lucrurilor începute.</p>
{idx_html(prefix, "SUB-020")}<h3 id="5-3-numarul-ereditar">5.3. Numărul ereditar</h3>
{idx_html(prefix, "C-008")}<aside class="callout example"><p><strong>Calcul</strong><br>{calculation(person["nume_familie"], name_data["numarul_ereditar"])}</p></aside>
{idx_html(prefix, "P-020n")}<p>Numărul ereditar <strong>{inherited_number}</strong> aduce prin numele Docolin o memorie de neam legată de perspectivă largă, ajutor, finalizare și capacitatea de a transforma experiența în înțelegere. Resursa este generozitatea; nevoia de maturizare este să păstrezi măsura și să nu porți responsabilități care aparțin altora.</p>
{family_block}
{idx_html(prefix, "SUB-022")}<h3 id="5-5-numarul-de-realizare">5.5. Numărul de realizare</h3>
{idx_html(prefix, "P-021a")}<p>Numărul de realizare arată impresia pe care o lași asupra celorlalți, comportamentul vizibil și felul în care energia numelui poate susține rezultate concrete.</p>
{idx_html(prefix, "C-010")}<aside class="callout example"><p><strong>Calcul</strong><br>{calculation("Consoanele numelui", name_data["numarul_de_realizare"])}</p></aside>
{idx_html(prefix, "P-022")}<p>Numărul de realizare <strong>{realization_number}</strong> te face vizibilă ca persoană practică, ordonată și capabilă să transforme o intenție în structură. Umbra este rigiditatea; maturizarea cere reguli simple, utile și adaptabile.</p>
{idx_html(prefix, "P-022a")}<p>Vibrația exterioară <strong>{ve}</strong> și Numărul de realizare <strong>{realization_number}</strong> creează un dialog între expresie și ordine: <strong>{ve}</strong> comunică și explorează, iar <strong>{realization_number}</strong> fixează. Imaginea ta devine coerentă când creativitatea primește un pas concret de finalizare.</p>
{idx_html(prefix, "SUB-023")}<h3 id="5-6-numarul-de-exprimare">5.6. Numărul de exprimare</h3>
{idx_html(prefix, "P-023a")}<p>Numărul de exprimare reprezintă personalitatea și cheia către ceea ce poți deveni. El arată felul în care componentele numelui se reunesc într-o expresie matură.</p>
{expression_callout}
{idx_html(prefix, "P-024")}<p>Numărul de exprimare <strong>{expression_result}</strong> susține construcția, disciplina, răbdarea și capacitatea de a da formă unei idei. Umbra este rigiditatea sau teama de schimbare; expresia matură păstrează ordinea, dar o adaptează realității.</p>
{idx_html(prefix, "P-024a")}<p>Armonizarea dintre Numărul de exprimare <strong>{expression_result}</strong> și Destinul <strong>{destin}</strong> cere ca structura să servească unui sens mai larg. <strong>{expression_result}</strong> construiește pas cu pas, iar <strong>{destin}</strong> aduce compasiune și perspectivă; împreună pot transforma sensibilitatea în rezultate stabile și folositoare.</p>
{idx_html(prefix, "SUB-023a")}<h3 id="5-7-codul-numerologic-al-numelui">5.7. Codul numerologic al numelui</h3>
{code_tail}</section>'''
        old_name_section = rf'<section><div class="idx">Index: {re.escape(prefix)}-CAP-008</div><h2 id="capitolul-5-numele">.*?</section>'
        text, name_count = re.subn(old_name_section, lambda _: name_section, text, count=1, flags=re.S)
        if name_count != 1:
            raise RuntimeError("Capitolul 5 pentru Ingrid nu a fost restructurat.")
    else:
        text = text.replace(code_index, expression_callout + code_index, 1)

    replacements = {
        "Vibratia interioara": "Vibrația interioară",
        "Vibratia exterioara": "Vibrația exterioară",
        "Cine esti tu?": "Cine ești tu?",
        "Rolul social": "Rolul social",
        "Matrita numerologica": "Matrița numerologică",
        "Patratul lui Pitagora": "Pătratul lui Pitagora",
        "Spirit si karma": "Spirit și karmă",
        "Lectii si directii de maturizare": "Lecții și direcții de maturizare",
        "Pinacluri: Oportunitati si provocari": "Pinacluri: Oportunități și provocări",
        "Ciclicitati": "Ciclicități",
        "Cariera si bani": "Carieră și bani",
        "Iubire si relatii": "Iubire și relații",
        "Momentul prezent": "Momentul prezent",
        "Data nasterii": "Data nașterii",
        "Ora nasterii": "Ora nașterii",
        "Persoana analizata": "Persoana analizată",
        "lucrare numerologica scurta": "lucrare numerologică scurtă",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    def add_subheading(before_suffix: str, sub_suffix: str, title: str, anchor: str | None = None) -> None:
        nonlocal text
        needle = f'<div class="idx">Index: {prefix}-{before_suffix}</div>'
        anchor_attr = f' id="{anchor}"' if anchor else ""
        insertion = f'<div class="idx">Index: {prefix}-{sub_suffix}</div><h3{anchor_attr}>{title}</h3>'
        if needle not in text:
            raise RuntimeError(f"Nu pot insera {sub_suffix} înainte de {before_suffix}")
        text = text.replace(needle, insertion + needle, 1)

    add_subheading("P-001", "SUB-001", "1.1. Definiție")
    add_subheading("P-002", "SUB-002", "1.2. Caracterul")
    add_subheading("P-004", "SUB-008" if person["nume_familie"] == "Docolin" else "SUB-006", "2.1. Definiție")
    add_subheading("P-005", "SUB-009" if person["nume_familie"] == "Docolin" else "SUB-007", "2.2. Rolul social")
    add_subheading("P-008", "SUB-011", "3.1. Definiție și calcul", "3-1-definitie-si-calcul")
    add_subheading("P-009", "SUB-012", "3.2. Interpretare", "3-2-interpretare")
    add_subheading("P-010", "SUB-013", "4.1. Matricea datei de naștere")
    if person["nume_familie"] == "Docolin":
        pass
    else:
        add_subheading("P-021", "SUB-018", "4.2. Scara bunăstării")
        add_subheading("P-022", "SUB-020", "5.1. Identitatea numelui")
    add_subheading(
        "P-026",
        "SUB-038" if person["nume_familie"] == "Docolin" else "SUB-004a",
        "6.1. Codul Spiritului și vârsta Spiritului" if person["nume_familie"] == "Docolin" else "6.1. Codul și vârsta Spiritului",
        "6-1-codul-spiritului-si-varsta-spiritului" if person["nume_familie"] == "Docolin" else None,
    )
    add_subheading("P-028", "SUB-007a", "6.2. Karma din ziua de naștere")
    add_subheading("P-029", "SUB-007b", "6.3. Karma din luna de naștere")
    add_subheading("P-030", "SUB-012a" if person["nume_familie"] == "Docolin" else "SUB-008", "6.4. Karma din Calea Destinului")

    if person["nume_familie"] == "Docolin":
        chapter_index_pairs = (
            ("CAP-004", "CAP-005", "capitolul-1-vibratia-interioara"),
            ("CAP-005", "CAP-006", "capitolul-2-vibratia-exterioara"),
            ("CAP-006", "CAP-007", "capitolul-3-destinul"),
            ("CAP-007", "CAP-008", "capitolul-4-matrita-numerologica"),
            ("CAP-009", "CAP-007b", "capitolul-6-spirit-si-karma"),
        )
        for old_index, new_index, chapter_anchor in chapter_index_pairs:
            old = f'<div class="idx">Index: {prefix}-{old_index}</div><h2 id="{chapter_anchor}">'
            new = f'<div class="idx">Index: {prefix}-{new_index}</div><h2 id="{chapter_anchor}">'
            if old not in text:
                raise RuntimeError(f"Nu pot alinia {old_index} la {new_index} pentru Ingrid.")
            text = text.replace(old, new, 1)

        desires = f'''{idx_html(prefix, "SUB-003")}<h3 id="1-3-dorintele">1.3. Dorințele</h3>
{idx_html(prefix, "P-002a")}<p>Îți dorești libertatea de a explora, de a pune întrebări și de a descoperi prin experiență directă. Ai nevoie de varietate, mișcare și alegeri reale, dar și de repere care te ajută să nu pierzi direcția atunci când apar multe posibilități deodată.</p>
{idx_html(prefix, "SUB-004")}<h3 id="1-4-motivatia">1.4. Motivația</h3>
{idx_html(prefix, "P-002b")}<p>Te motivează noutatea, jocul, conversația și activitățile în care poți încerca mai multe căi. Energia lui <strong>{vi}</strong> crește sănătos când fiecare explorare are un început clar, un timp de lucru și un pas vizibil de încheiere.</p>
{idx_html(prefix, "SUB-005")}<h3 id="1-5-teama">1.5. Teama</h3>
{idx_html(prefix, "P-002c")}<p>Teama din umbra lui <strong>{vi}</strong> este limitarea fără explicație, rutina rigidă sau senzația că nu mai există opțiuni. Atunci poate apărea neliniștea ori schimbarea grăbită a direcției. Maturizarea înseamnă să descoperi că o limită bună nu închide libertatea, ci îi oferă un cadru în care experiența poate deveni competență.</p>
{idx_html(prefix, "SUB-006")}<h3 id="1-6-polaritati-si-maturizare">1.6. Polarități și maturizare</h3>'''
        p003_index = f'<div class="idx">Index: {prefix}-P-003</div>'
        text = text.replace(p003_index, desires + p003_index, 1)

        add_subheading("P-006", "SUB-010", "2.3. Interior și exterior", "2-3-interior-si-exterior")

        counts = {int(digit): info["cantitate"] for digit, info in matrix["casute"].items()}
        elements = {
            "Foc": counts[1] + counts[5] + counts[9],
            "Pământ": counts[4] + counts[8],
            "Aer": counts[3] + counts[7],
            "Apă": counts[2] + counts[6],
        }
        max_element = max(elements.values()) or 1
        bars = "".join(
            f'<div class="element-bar"><div class="element-bar-label"><span>{label}</span><strong>{value}</strong></div><div class="element-bar-track"><span class="element-bar-fill element-{css}" style="width:{round(value / max_element * 100)}%"></span></div></div>'
            for label, css, value in (("Foc", "foc", elements["Foc"]), ("Pământ", "pamant", elements["Pământ"]), ("Aer", "aer", elements["Aer"]), ("Apă", "apa", elements["Apă"]))
        )
        element_block = f'''{idx_html(prefix, "SUB-015")}<h3 id="4-3-elemente-si-temperament">4.3. Elemente și temperament</h3>
{idx_html(prefix, "T-012")}<div class="element-analysis framed-panel"><div class="element-chart"><div class="element-bars" role="img" aria-label="Distribuția elementelor: Foc {elements['Foc']}, Pământ {elements['Pământ']}, Aer {elements['Aer']}, Apă {elements['Apă']}">{bars}</div></div>
{idx_html(prefix, "P-044")}<ul class="element-definitions"><li><strong>Focul</strong> este esența vieții, a duhului și a spiritului care animă și activează.</li><li><strong>Pământul</strong> este esența materiei dense, a solidarității și a fertilității, care hrănește și dă formă.</li><li><strong>Aerul</strong> este esența inteligenței conceptuale care eliberează și stimulează.</li><li><strong>Apa</strong> este esența emoțiilor și a fecundității, maleabilă, flexibilă și orientată spre acumulare.</li></ul></div>
{idx_html(prefix, "P-045")}<p>Temperamentul tău este mixt: Focul, Pământul și Apa au câte <strong>3</strong> apariții, iar Aerul are <strong>1</strong>. Ai simultan energie de pornire, nevoie de rezultat și sensibilitate; echilibrul vine când emoțiile primesc cuvinte, corpul primește ritm, iar ideile sunt explicate simplu și verificate prin experiență.</p>
{idx_html(prefix, "SUB-016")}<h3 id="4-4-masculin-si-feminin">4.4. Masculin și feminin</h3>'''
        p020_index = f'<div class="idx">Index: {prefix}-P-020</div>'
        text = text.replace(p020_index, element_block + p020_index, 1)

        gifts = [digit for digit, count in counts.items() if count >= 2]
        gift_block = f'''{idx_html(prefix, "SUB-017")}<h3 id="4-5-daruri-si-nevoi">4.5. Daruri și nevoi</h3>
{idx_html(prefix, "P-020b")}<p>Darurile și nevoile se citesc din căsuțele cu cel puțin <strong>2</strong> cifre: la tine sunt <strong>{'</strong> și <strong>'.join(str(digit) for digit in gifts)}</strong>. Darul lui <strong>2</strong> este sensibilitatea și colaborarea, cu nevoia de siguranță emoțională; darul lui <strong>8</strong> este puterea de organizare, cu nevoia de reguli drepte și responsabilități reale. Aceste resurse cresc sănătos când sensibilitatea și responsabilitatea se susțin reciproc.</p>
{idx_html(prefix, "SUB-017a")}<h3 id="4-6-scara-bunastarii">4.6. Scara bunăstării</h3>'''
        p021_index = f'<div class="idx">Index: {prefix}-P-021</div>'
        text = text.replace(p021_index, gift_block + p021_index, 1)

        conclusion = f'''{idx_html(prefix, "SUB-012b")}<h3 id="6-5-concluzie-directia-de-lucru">6.5. Concluzie: direcția de lucru</h3>
{idx_html(prefix, "P-030c")}<p>Codul Spiritului <strong>44</strong>, zona Harurilor și subetapa <strong>5</strong> arată o maturizare prin învățare, discernământ și folosirea sensibilității într-o formă concretă. Karma zilei <strong>5</strong>, Karma lunii <strong>3</strong> și Calea karmică <strong>{calea}</strong> te învață să unești valorile, autonomia și imaginația într-o direcție lucidă, creativă și folositoare.</p>'''
        next_chapter = rf'(\s*</section>\s*<section><div class="idx">Index: {re.escape(prefix)}-CAP-010</div>)'
        text, conclusion_count = re.subn(next_chapter, lambda match: conclusion + match.group(1), text, count=1)
        if conclusion_count != 1:
            raise RuntimeError("Concluzia capitolului 6 nu a fost inserată pentru Ingrid.")

        index_fixes = (
            (
                f'<div class="idx">Index: {prefix}-C-003</div><aside class="callout example"><strong>Calculul puntii interior-exterior</strong>',
                f'<div class="idx">Index: {prefix}-C-002a</div><aside class="callout example"><strong>Calculul puntii interior-exterior</strong>',
            ),
            (
                f'<div class="idx">Index: {prefix}-C-004</div><aside class="callout example"><strong>Calcul</strong><br>Toate cifrele adunate',
                f'<div class="idx">Index: {prefix}-C-003</div><aside class="callout example"><strong>Calcul</strong><br>Toate cifrele adunate',
            ),
            (
                f'<div class="idx">Index: {prefix}-C-005</div><aside class="callout example"><strong>Calcul</strong><br>Data compacta',
                f'<div class="idx">Index: {prefix}-C-004</div><aside class="callout example"><strong>Calcul</strong><br>Data compacta',
            ),
            (
                f'<div class="idx">Index: {prefix}-P-021</div><p>Scara bunastarii',
                f'<div class="idx">Index: {prefix}-P-019a</div><p>Scara bunastarii',
            ),
        )
        for old, new in index_fixes:
            if old not in text:
                raise RuntimeError(f"Nu pot aplica alinierea de index pentru {old}.")
            text = text.replace(old, new, 1)

        text = text.replace(f"Index: {prefix}-SUB-029a", f"Index: {prefix}-SUB-029", 1)
        text = text.replace("8.1. Soarta si Destinul", "8.1. Soarta și Destinul", 1)
        text = text.replace("8.2. Anii importanti", "8.2. Anii importanți", 1)
        text = text.replace("8.3. Lectiile de viata", "8.3. Lecțiile de viață", 1)

    if vi == 8:
        character = f"{active}, vibrația interioară <strong>8</strong> aduce forță, responsabilitate, putere de organizare și nevoie de rezultate concrete. Optul simbolizează forțele materiale, reacția și justiția echilibrantă. Este asociat cu puterea, bogăția, aprecierea lumească și probele lui Saturn. Drumul lui nu este simplu: succesul se construiește prin luptă, efort, planificare și muncă susținută. În lumină poți fi hotărât, protector și practic; în umbră poți lăsa impresia că urmărești permanent controlul sau câștigul. Maturizarea înseamnă să folosești forța calm și proporțional, astfel încât fermitatea să ofere siguranță, nu teamă."
    else:
        character = f"{active}, vibrația interioară <strong>{vi}</strong> te apropie de energia explorării, curiozității și adaptării. Ai nevoie de mișcare, varietate și experiențe prin care să descoperi direct cum funcționează lumea. Resursa este flexibilitatea; umbra este risipirea, refuzul rutinei sau schimbarea direcției înainte ca un lucru să fie încheiat. Maturizarea apare când libertatea primește limite clare, iar fiecare explorare este urmată de un pas concret de finalizare."
    text = replace_indexed_paragraph(text, prefix, "P-002", character)

    if vi == 8:
        destiny_first = f"{active}, Calea Destinului <strong>{calea}</strong> reunește inițiativa lui <strong>1</strong> cu forța, responsabilitatea și raportarea la putere a lui <strong>8</strong>; suma lor conduce la cifra de interpretare <strong>{destin}</strong>, care cere perspectivă largă, compasiune, finalizare și capacitatea de a transforma experiența în înțelegere. Cantitativ, traseul este complet: toate cifrele datei formează <strong>{calea}</strong>, Destinul se reduce o singură dată la <strong>{destin}</strong>, iar cifra de interpretare rămâne <strong>{destin}</strong>. Calitativ, muntele tău de urcat este să treci de la puterea concentrată asupra rezultatului imediat la o putere care vede ansamblul și efectul asupra oamenilor. Vibrația interioară <strong>8</strong> vrea eficiență și control, în timp ce Destinul <strong>9</strong> cere generozitate, desprindere și încheiere matură. Când lucrează împreună, poți deveni un om capabil să organizeze resurse pentru un scop mai mare decât interesul de moment; în umbră, poți oscila între control și dezamăgire, iar maturizarea apare când termini ceea ce începi, accepți imperfecțiunea și folosești forța pentru a construi ceva util și altora."
        independent = "singur"
    else:
        destiny_first = f"{active}, Calea Destinului <strong>{calea}</strong> reunește inițiativa lui <strong>1</strong> cu forța, responsabilitatea și raportarea la putere a lui <strong>8</strong>; suma lor conduce la cifra de interpretare <strong>{destin}</strong>, care cere perspectivă largă, compasiune, finalizare și capacitatea de a transforma experiența în înțelegere. Cantitativ, traseul este complet: toate cifrele datei formează <strong>{calea}</strong>, Destinul se reduce o singură dată la <strong>{destin}</strong>, iar cifra de interpretare rămâne <strong>{destin}</strong>. Calitativ, muntele tău de urcat este să transformi nevoia de libertate și experiență într-o direcție care vede ansamblul și efectul asupra oamenilor. Vibrația interioară <strong>5</strong> caută mișcare, varietate și descoperire, în timp ce Destinul <strong>9</strong> cere generozitate, desprindere și încheiere matură. Când lucrează împreună, poți deveni o persoană flexibilă, capabilă să adune experiențe diferite și să le transforme în înțelegere folositoare și altora; în umbră, poți oscila între risipire și dezamăgire, iar maturizarea apare când termini ceea ce începi, accepți imperfecțiunea și dai libertății un scop mai mare decât interesul de moment."
        independent = "singură"
    destiny_second = f"Pentru ca energia lui <strong>9</strong> să se exprime la nivel înalt, ai nevoie de un ideal care depășește interesul personal și de sentimentul că ceea ce faci contribuie la binele altora. Egoismul, vanitatea, orgoliul, preocupările mărunte sau atașamentul excesiv față de bani pot îngusta această perspectivă și pot transforma forța ta într-o sursă de nemulțumire ori suferință. În schimb, studiul, reflecția, cultivarea vieții interioare și participarea la proiecte cu sens îți oferă spațiul potrivit pentru o minte activă, idei originale, idealism și o imaginație bogată. Lecția independenței nu înseamnă izolare, ci capacitatea de a te adapta {independent} și apoi de a intra deschis în lume, comunicând și dând mai departe ceea ce ai înțeles. <strong>7</strong> și <strong>9</strong> au în comun căutarea sensului, însă o trăiesc în direcții diferite: <strong>7</strong> se retrage pentru a cerceta și a aprofunda, în timp ce <strong>9</strong> se întoarce către oameni pentru a încheia, a împărtăși și a transforma cunoașterea în faptă. De aceea, Destinul tău <strong>9</strong> cere ca experiența acumulată să nu rămână doar în interior, ci să capete o formă folositoare în exterior."
    text = replace_indexed_paragraphs(text, prefix, "P-009", [destiny_first, destiny_second])

    for digit, info in matrix["casute"].items():
        interpretation = matrix_interpretation(int(digit), info["cantitate"], prefix)
        if interpretation:
            text = replace_indexed_paragraph(text, prefix, f"P-01{digit}", interpretation)

    day_number = arcana_value(born.day)
    day_name = ARCANA[day_number][0]
    if day_number == 17:
        karma_day = f"Karma zilei se citește prin Arcana <strong>17 — Steaua</strong>. Ea vorbește despre speranță, inspirație, autenticitate și puterea de a orienta oamenii printr-un exemplu luminos. Umbra poate fi idealizarea, nevoia de validare sau așteptarea ca inspirația să înlocuiască efortul. Pentru {active}, lecția este să păstreze încrederea, dar să o lege de răbdare, exercițiu și rezultate reale."
    else:
        karma_day = f"Karma zilei se citește prin Arcana <strong>{day_number} — {html.escape(day_name)}</strong>. Ea descrie simbolic o lecție despre valori, învățare și raportarea la reguli ori autoritate. Resursa este capacitatea de a găsi sens și de a primi îndrumare; umbra este rigiditatea sau repetarea unei reguli fără înțelegere. Pentru {active}, maturizarea apare când întrebarea, experiența și exemplul viu completează ceea ce este transmis prin cuvânt."
    text = replace_indexed_paragraph(text, prefix, "P-028", karma_day)

    karma_month = f"În lectura karmică simbolică, luna nașterii poate descrie o temă în relația cu mama: acceptare, iertare, ajutor și iubire. Pentru luna <strong>{born.month}</strong>, lecția trece prin comunicare, expresie și felul în care emoțiile primesc cuvinte. Dacă mama nu este prezentă, tema se poate manifesta și printr-o persoană apropiată cu rol matern; această imagine spirituală nu atribuie vină copilului. {active} are nevoie să exprime ce simte, să repare după conflict și să ofere ajutor potrivit vârstei, fără să devină responsabil pentru starea adultului. Părinții pot ușura tema prin dialog, iertare modelată prin faptă, reguli explicate și un mediu în care greșeala nu anulează iubirea."
    text = replace_indexed_paragraph(text, prefix, "P-029", karma_month)

    if person["nume_familie"] == "Docolin":
        day_img = out_dir / f"tarot-{day_number:02d}-{slug(day_name)}-karma-zilei.jpg"
        karma_sections = f'''{idx_html(prefix, "SUB-007a")}<h3 id="6-2-karma-din-ziua-de-nastere">6.2. Karma din ziua de naștere</h3>
{idx_html(prefix, "P-009a")}<p>În lectura numerologică, ziua de naștere arată o încărcătură karmică simbolică. Fiind născută în ziua de <strong>5</strong>, te afli în zona de aproximativ <strong>100%</strong> și lucrezi cu Arcana <strong>5 — Marele Preot</strong>. Cheia acestei poziții este smerenia, înțelepciunea practică și capacitatea de a găsi sensul din spatele unei reguli sau învățături.</p>
{idx_html(prefix, "C-001a")}<aside class="callout example"><p><strong>Calcul</strong><br>Ziua nașterii = <strong>5</strong></p><p>Arcana karmică = <strong>5 — Marele Preot</strong></p><p>Intervalul 1–9 = karma împlinită <strong>spre 100%</strong></p></aside>
{idx_html(prefix, "G-001a")}<img src="{data_uri(day_img)}" data-source="{day_img.name}" alt="Arcana 5 — Marele Preot, karma din ziua de naștere"><p><em>Arcana <strong>5</strong> — Marele Preot. Karma din ziua de naștere</em></p>
{idx_html(prefix, "P-009b")}<p>În plan karmic simbolic, cifra <strong>5</strong> poate vorbi despre memoria unei relații puternice cu tradiția, credința, educația ori autoritatea morală. În expresia dezechilibrată, cunoașterea ar fi putut fi folosită rigid: reguli repetate fără înțelegere, conformism cerut celorlalți, judecarea celor care aleg o cale diferită sau dependența de aprobarea unei autorități. Această imagine este o temă arhetipală de lucru, nu o afirmație verificabilă despre o existență anterioară și nici o etichetă aplicată copilului.</p>
{idx_html(prefix, "P-009b1")}<p>Arcana <strong>5 — Marele Preot</strong> reprezintă legătura dintre experiență și o cale de valori care poate fi transmisă mai departe. Maestrul și discipolii sugerează învățarea prin relație, iar cheile vorbesc despre accesul la sens atunci când regula este înțeleasă, nu doar executată. În lumină, această Arcană aduce ghidaj, credință, respect pentru cunoaștere și talentul de a explica; în umbră, poate aduce dogmă, ipocrizie, conformism sau supunere din teamă. Adevărata autoritate se construiește atunci când ceea ce este spus se vede și în comportament.</p>
{idx_html(prefix, "P-009b2")}<p>Lecția actuală a combinației <strong>5 — Marele Preot</strong> este să unești smerenia cu înțelepciunea practică. Pentru Ingrid, maturizarea începe prin libertatea de a întreba „de ce?”, prin adulți care explică sensul regulilor și prin exemple coerente, în care vorba și fapta se susțin reciproc. Curiozitatea nu trebuie înlocuită cu obediență, iar tradiția nu trebuie respinsă numai pentru că impune o limită. Când învață să primească îndrumare, să verifice prin experiență și să aleagă valorile care produc bine, autoritatea exterioară se transformă treptat în discernământ interior.</p>
{idx_html(prefix, "SUB-007b")}<h3 id="6-3-karma-din-luna-de-nastere">6.3. Karma din luna de naștere</h3>
{idx_html(prefix, "P-013c")}<p>Karma din luna de naștere arată datoria socială, familială sau personală legată de luna în care te-ai născut. Luna se păstrează ca număr între <strong>1</strong> și <strong>12</strong>, fără reducere, și indică o direcție de maturizare în raport cu familia, neamul, locul de origine sau propria persoană. Această karmă nu vorbește despre vină, ci despre o responsabilitate care poate fi transformată în relații mai sănătoase și alegeri mai conștiente.</p>
{idx_html(prefix, "C-002b")}<aside class="callout example"><p><strong>Calcul</strong><br>Luna nașterii = <strong>3</strong></p><p>Karma lunii = <strong>independență față de influența maternă, exprimare și hotărâri proprii</strong></p></aside>
{idx_html(prefix, "P-013d")}<p>În formularea tradițională a metodei, karma din luna <strong>3</strong> este karma independenței de mamă. Spiritul întrupat în această lună are datoria karmică de a dobândi calitățile lui <strong>3</strong> în relația cu mama sa sau, în lipsa acesteia, cu o persoană foarte apropiată care îndeplinește rolul matern: exprimare, comunicare, curiozitate și capacitatea de a experimenta viața independent. Imaginea unei legături foarte strânse dintr-o existență anterioară este folosită aici ca limbaj spiritual și arhetipal, nu ca fapt demonstrabil și nici ca motiv pentru a atribui vină mamei sau copilului.</p>
{idx_html(prefix, "P-013e")}<p>Pentru Ingrid, independența nu înseamnă o desprindere bruscă și nici lipsa apropierii afective. Ea se construiește treptat prin alegeri potrivite vârstei, exprimarea propriei păreri, sarcini simple duse până la capăt și experiențe în care poate încerca fără ca adultul să decidă fiecare pas în locul ei. Energia lui <strong>3</strong> are nevoie să vorbească, să creeze, să se joace și să învețe din contactul direct cu lumea. Pe măsură ce crește, maturizarea cere să își asume propriile hotărâri și consecințele lor, păstrând legătura cu mama fără a rămâne dependentă de aprobarea ei.</p>
{idx_html(prefix, "P-013f")}<p>Pentru părinții acestui spirit, direcția sănătoasă este să încurajeze autonomia devreme, dar proporțional cu vârsta: două opțiuni reale, obiecte și sarcini proprii, libertatea de a formula un răspuns și ocazia de a repara o alegere nepotrivită. Mama poate susține energia lui <strong>3</strong> ascultând înainte de a corecta, evitând să vorbească permanent în numele copilului și separând protecția de control. Independența financiară aparține etapelor viitoare; în copilărie, baza ei se formează prin înțelegerea valorii lucrurilor, economisire pentru obiective simple și responsabilitate. Astfel, sensul karmic nu devine separare, ci o relație în care iubirea și libertatea pot crește împreună.</p>
'''
        old_karma_sections = rf'<div class="idx">Index: {re.escape(prefix)}-SUB-007a</div>.*?(?=<div class="idx">Index: {re.escape(prefix)}-SUB-012a</div>)'
        text, karma_count = re.subn(old_karma_sections, lambda _: karma_sections, text, count=1, flags=re.S)
        if karma_count != 1:
            raise RuntimeError("Subcapitolele karmice 6.2 și 6.3 pentru Ingrid nu au fost înlocuite.")

    karma_destiny = f"Karma din Calea Destinului păstrează suma compusă <strong>{calea}</strong> și se asociază cu Arcana <strong>18 — Luna</strong>. Ea vorbește despre imaginație, sensibilitate și nevoia de a distinge realitatea de teamă, proiecție sau idealizare. Nu indică lipsă de talent, ci riscul ca o stare intensă să devină concluzie înainte ca faptele să fie verificate. Maturizarea cere dialog, rutină, întrebări clare și transformarea emoției în creație, empatie și intuiție disciplinată."
    text = replace_indexed_paragraph(text, prefix, "P-030", karma_destiny)

    da = arcana_value(prof["da"])
    nu = arcana_value(prof["nu"])
    da_name = ARCANA[da][0]
    nu_name = ARCANA[nu][0]
    da_img = out_dir / f"tarot-{da:02d}-{slug(da_name)}-aplicabilitate-profesionala.jpg"
    nu_img = out_dir / f"tarot-{nu:02d}-{slug(nu_name)}-obstacol-profesional.jpg"

    if da == 10:
        da_paragraphs = [
            "<strong>Roata Norocului</strong> susține mișcarea, adaptarea și capacitatea de a recunoaște momentul potrivit. Nu promite noroc pasiv, ci arată că schimbarea poate deveni oportunitate atunci când este întâmpinată cu pregătire.",
            "Profesional, energia poate lucra în coordonare, negociere, mobilitate, tehnologie, comerț ori proiecte cu etape succesive. Resursa se vede când flexibilitatea este legată de simțul rezultatului și de capacitatea de a reorganiza un plan.",
            "Umbra este încrederea excesivă în context, nerăbdarea și trecerea mai departe înainte ca munca prezentă să fie încheiată. Proiectele scurte, regulile variabile și criteriile clare de finalizare transformă schimbarea în competență.",
        ]
    else:
        da_paragraphs = [
            "<strong>Moartea</strong> descrie profesional puterea de a încheia o formă veche și de a construi una mai potrivită. Arcana nu vorbește despre un eveniment fatal, ci despre transformare, selecție și regenerare.",
            "Resursa poate lucra în domenii care cer restructurare, cercetare, vindecare simbolică, design, intervenție, gestionarea crizelor sau trecerea unui sistem de la o etapă la alta. Ai capacitatea de a vedea ce nu mai funcționează și ce trebuie schimbat.",
            "Umbra este teama de pierdere ori tendința de a rupe prea repede. Maturizarea cere încheieri explicate, păstrarea lucrurilor valoroase și proiecte în care transformarea este urmată de reconstrucție concretă.",
        ]
    nu_paragraphs = [
        "<strong>Luna</strong> arată obstacolul confuziei, al idealizării și al reacției conduse de teamă sau de o imaginație neclarificată. Sensibilitatea poate amesteca uneori faptele cu presupunerile.",
        "Profesional, umbra poate apărea ca ezitare, amânare, teamă de evaluare ori pierderea criteriului concret într-un val emoțional. Aceeași energie poate deveni resursă pentru artă, poveste și activități în care sensibilitatea este susținută de metodă.",
        "Antidotul este verificarea realității: întrebări clare, informații confirmate, sarcini împărțite în pași, termene vizibile și rutină. Când emoția este numită fără a fi confundată cu adevărul complet, nesiguranța se transformă în intuiție disciplinată.",
    ]

    intro = "Aplicabilitatea profesională se citește prin două direcții complementare. Valoarea <strong>DA</strong> arată energia care susține manifestarea, iar valoarea <strong>NU</strong> descrie obstacolul interior care trebuie educat. Pentru un copil, aceste Arcane nu fixează o meserie, ci oferă repere despre joc, învățare, disciplină și relația cu schimbarea."
    tarot_table = f'<div class="table-wrap"><table class="tarot-profile-table professional-tarot-table"><thead><tr><th>Aplicabilitate profesională DA</th><th>Aplicabilitate profesională NU</th></tr></thead><tbody><tr><td><img src="{data_uri(da_img)}" alt="Arcana {da} — {html.escape(da_name)}"><div class="tarot-image-caption"><em>Arcana <strong>{da}</strong> — {html.escape(da_name)}</em></div></td><td><img src="{data_uri(nu_img)}" alt="Arcana {nu} — {html.escape(nu_name)}"><div class="tarot-image-caption"><em>Arcana <strong>{nu}</strong> — {html.escape(nu_name)}</em></div></td></tr><tr><td><div class="idx">Index: {prefix}-P-046a</div>{"".join(f"<p>{p}</p>" for p in da_paragraphs)}</td><td><div class="idx">Index: {prefix}-P-046b</div>{"".join(f"<p>{p}</p>" for p in nu_paragraphs)}</td></tr></tbody></table></div>'

    relation_section = ""
    if has_relation:
        relation_target = out_dir / DOMINIC_RELATION_PNG.name
        if not relation_target.is_file():
            shutil.copyfile(DOMINIC_RELATION_PNG, relation_target)
        relation_section = f'''<section>{idx_html(prefix, "CAP-013")}<h2 id="capitolul-9-relatii">Capitolul 9. Relații</h2>{idx_html(prefix, "L-003")}<ul><li>Nume: Vulcu Dominic Ioan</li><li>Data nașterii: 08.05.2021</li><li>Tipul relației: frați</li></ul>{idx_html(prefix, "SUB-028a")}<h3>9.1. Omulețul relațiilor</h3>{idx_html(prefix, "G-006")}<figure><img src="{data_uri(relation_target)}" alt="Omulețul relațiilor pentru Vulcu Victor Daniel și Vulcu Dominic Ioan"><figcaption>Relația dintre frații Victor Daniel și Dominic Ioan</figcaption></figure>{idx_html(prefix, "C-007")}<aside class="callout example"><strong>Calcul relațional</strong><br>Realizare împreună: 8 + 8 = 16 → 1 + 6 = <strong>7</strong><br>De rezolvat împreună: |8 − 8| = <strong>0</strong></aside>{idx_html(prefix, "P-029r")}<p>Vic intră în relație prin vibrația interioară <strong>8</strong>, iar Domi tot prin <strong>8</strong>. Amândoi aduceți voință, reacție la autoritate și nevoia de a avea un cuvânt de spus. Domi, ca frate mai mare, poate aduce inițiativă, iar Vic răspunde cu aceeași fermitate. Lumina este loialitatea; umbra este competiția pentru control.</p>{idx_html(prefix, "P-030r")}<p>Realizarea comună <strong>7</strong> favorizează observația, strategia și respectarea spațiului personal. Tema <strong>0</strong> arată că vă oglindiți rapid, inclusiv în încăpățânare. Relația crește când adulții evită comparațiile, oferă timp individual și propun obiective comune scurte.</p>{idx_html(prefix, "P-031r")}<p>Împreună aveți Foc <strong>3</strong>, Apă <strong>4</strong>, Aer <strong>3</strong>, Pământ <strong>1</strong> și potențialul lui <strong>0</strong> de două ori. Apa dominantă face relația sensibilă la ton, iar Pământul redus cere rutine și reguli concrete. Activitățile comune urmate de timp separat păstrează apropierea fără a transforma asemănarea în competiție.</p></section>'''

    professional_number = 10 if has_relation else 9
    conclusion_number = professional_number + 1
    professional_section = f'''<section>{idx_html(prefix, "CAP-014")}<h2 id="capitolul-{professional_number}-aplicabilitate-profesionala">Capitolul {professional_number}. Aplicabilitate profesională</h2>{idx_html(prefix, "SUB-029a")}<h3>{professional_number}.1. Aplicabilitate profesională</h3>{idx_html(prefix, "P-046i")}<p>{intro}</p>{idx_html(prefix, "C-014")}<aside class="callout example"><strong>Calcul</strong><br>DA = <strong>{prof["da"]}</strong><br>NU = <strong>{prof["nu"]}</strong></aside>{idx_html(prefix, "T-016")}{tarot_table}{idx_html(prefix, "P-046")}<p>Potențialul se formează prin mediu, educație și experiențe potrivite vârstei. Energia <strong>{da}</strong> cere să fie exersată, iar obstacolul <strong>{nu}</strong> cere claritate emoțională și verificarea realității. Când flexibilitatea primește structură, iar sensibilitatea primește limbaj, aptitudinile pot deveni competențe mature.</p></section>'''

    relation_conclusion = ""
    if has_relation:
        relation_conclusion = f'''{idx_html(prefix, "SUB-031")}<h3>{conclusion_number}.2. Iubire și relație</h3>{idx_html(prefix, "P-032r")}<p>Relația cu Domi are potențialul <strong>7</strong> și se construiește prin învățare, jocuri de strategie și respectarea spațiului personal. Amândoi porniți din <strong>8</strong>, deci puteți fi loiali și protectori, dar și competitivi când fiecare vrea să conducă.</p>{idx_html(prefix, "P-032s")}<p>Tema <strong>0</strong> cere integrare, nu desemnarea unui câștigător. Obiectele proprii, responsabilitățile potrivite vârstei, timpul individual și repararea după conflict ajută apropierea să nu devină confruntare.</p>'''
    present_subnumber = 3 if has_relation else 2
    conclusion_section = f'''<section>{idx_html(prefix, "CAP-015")}<h2 id="capitolul-{conclusion_number}-concluzii">Capitolul {conclusion_number}. Concluzii</h2>{idx_html(prefix, "SUB-030")}<h3>{conclusion_number}.1. Carieră și bani</h3>{idx_html(prefix, "P-047")}<p>{active}, cariera și banii se vor citi mai târziu prin felul în care vibrația <strong>{vi}</strong> se întâlnește cu Destinul <strong>{destin}</strong>. Zona dominantă a Scării bunăstării este <strong>{html.escape(matrix["scara_bunastarii"][0]["denumire"])}</strong>, cu valoarea <strong>{matrix["scara_bunastarii"][0]["valoare"]}</strong>. Potențialul se transformă în rezultat prin educație, exemple și responsabilități potrivite vârstei.</p>{idx_html(prefix, "P-032a")}<p>Numărul activ <strong>{name_data["numarul_activ"]["reducere"]["rezultat"]}</strong>, Numărul intim <strong>{name_data["numarul_intim"]["reducere"]["rezultat"]}</strong>, Numărul de realizare <strong>{name_data["numarul_de_realizare"]["reducere"]["rezultat"]}</strong> și Numărul de exprimare <strong>{name_data["numarul_de_exprimare"]["reducere"]["rezultat"]}</strong> arată cum inițiativa, motivația și forma socială trebuie armonizate. Profilul nu trebuie grăbit către o etichetă; este mai important să observăm unde interesul rămâne viu și ce fel de rezultat îl face pe copil să revină cu plăcere.</p>{idx_html(prefix, "P-032b")}<p>În relația cu banii, educația începe prin alegeri simple, economisire pentru un obiectiv, diferența dintre dorință și nevoie și legarea privilegiului de responsabilitate. Banii devin astfel o resursă administrată, nu o măsură a valorii personale.</p>{idx_html(prefix, "P-032c")}<p>Pinaclul <strong>{pin["pinaclu"]}</strong> aduce Oportunitatea <strong>{pin["oportunitate"]}</strong> și Provocarea <strong>{pin["provocare"]}</strong>. În copilărie, această combinație se educă prin ritm, joc, corp, exprimarea emoțiilor și reguli explicate pe înțelesul copilului.</p>{relation_conclusion}{idx_html(prefix, "SUB-040")}<h3>{conclusion_number}.{present_subnumber}. Momentul prezent</h3>{idx_html(prefix, "P-032t")}<p>În {TODAY.year}, {active} se află în primul Pinaclu, în primul ciclu de 9 ani și în primul ciclu de 12 ani. Anul personal <strong>{current["an_personal"]}</strong> și Lecția <strong>{current["lectie"]}</strong> cer experiențe potrivite vârstei, ritm stabil și un pas vizibil de încheiere pentru fiecare lucru început.</p>{idx_html(prefix, "P-032v")}<p>Matricea arată ce energii sunt active și ce zone au nevoie de aport extern. Explicațiile clare, repetiția, somnul, mișcarea și limitele consecvente sunt mai valoroase decât presiunea pentru răspuns rapid. Progresul sănătos apare când o experiență este trăită, numită și încheiată înainte de a deschide alta.</p></section>'''

    documentation = f'''<section>{idx_html(prefix, "CAP-016")}<h2 id="documentatia-si-trasabilitatea-lucrarii">Documentația și trasabilitatea lucrării</h2>{idx_html(prefix, "T-014")}<div class="table-wrap"><table><thead><tr><th>Resursă</th><th>Valoare</th></tr></thead><tbody><tr><td>Agent coordonator</td><td>The Scribe</td></tr><tr><td>Grafică</td><td>The Cartographer — SVG-uri validate</td></tr><tr><td>Skill-uri</td><td>numerologie-lucrare-redactare și skill-urile SVG dedicate</td></tr><tr><td>Template</td><td>scurt, sincronizat cu modelul de referință</td></tr><tr><td>Raport calculator</td><td>{person["data_nasterii"]}-{slug(person["nume_complet"]).upper()}-scurt-v1.00r-calculator.json</td></tr></tbody></table></div></section>'''

    old_conclusion = rf'<section><div class="idx">Index: {re.escape(prefix)}-CAP-012</div><h2 id="capitolul-9-concluzii">.*?</section>'
    replacement = relation_section + professional_section + conclusion_section + documentation
    text, count = re.subn(old_conclusion, lambda _: replacement, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError("Capitolul final vechi nu a fost înlocuit.")

    toc_items = [
        ("capitolul-1-vibratia-interioara", "Capitolul 1. Vibrația interioară - Cine ești tu?"),
        ("capitolul-2-vibratia-exterioara", "Capitolul 2. Vibrația exterioară - Rolul social"),
        ("capitolul-3-destinul", "Capitolul 3. Destinul - Muntele de urcat"),
        ("capitolul-4-matrita-numerologica", "Capitolul 4. Matrița numerologică - Pătratul lui Pitagora"),
        ("capitolul-5-numele", "Capitolul 5. Numele - Eu și neamul"),
        ("capitolul-6-spirit-si-karma", "Capitolul 6. Spirit și karmă - Lecții și direcții de maturizare"),
        ("capitolul-7-pinacluri", "Capitolul 7. Pinacluri: Oportunități și provocări"),
        ("capitolul-8-ciclicitati", "Capitolul 8. Ciclicități"),
    ]
    if has_relation:
        toc_items.append(("capitolul-9-relatii", "Capitolul 9. Relații"))
    toc_items.extend([
        (
            f"capitolul-{professional_number}-aplicabilitate-profesionala",
            f"Capitolul {professional_number}. Aplicabilitate profesională",
        ),
        (f"capitolul-{conclusion_number}-concluzii", f"Capitolul {conclusion_number}. Concluzii"),
    ])
    toc = idx_html(prefix, "L-002") + "<ol>" + "".join(
        f'<li><a href="#{anchor}">{label}</a></li>' for anchor, label in toc_items
    ) + "</ol>"
    text, count = re.subn(
        r'(<h2 id="cuprins">Cuprins</h2>)\s*(?:<div class="idx">Index: [^<]+-L-002</div>\s*)?<ol>.*?</ol>',
        lambda match: match.group(1) + toc,
        text,
        count=1,
        flags=re.S,
    )
    if count != 1:
        raise RuntimeError("Cuprinsul nu a fost sincronizat.")
    if has_relation:
        text = text.replace("<li>Template selectat: scurt</li>", "<li>Relație analizată: Vulcu Dominic Ioan, 08.05.2021, frate</li><li>Template selectat: scurt</li>", 1)
    return text


def idx_html(prefix: str, suffix: str) -> str:
    return f'<div class="idx">Index: {prefix}-{suffix}</div>'


def validate_html(path: Path, prefix: str) -> None:
    text = path.read_text(encoding="utf-8")
    main = text.split("<main>", 1)[1].split("</main>", 1)[0] if "<main>" in text else text
    model_text = MODEL_HTML.read_text(encoding="utf-8")
    css = re.search(r"<style>(.*?)</style>", text, re.S)
    model_css = re.search(r"<style>(.*?)</style>", model_text, re.S)

    def canonical_spirit_table(source: str) -> str | None:
        match = re.search(r'<table class="spirit-code-table">.*?</table>', source, re.S)
        if not match:
            return None

        def restore_zone(highlight: re.Match[str]) -> str:
            code = int(highlight.group(1))
            if code <= 13:
                zone = "love"
            elif code <= 26:
                zone = "reason"
            elif code <= 39:
                zone = "material"
            else:
                zone = "gifts"
            return f'<span class="spirit-zone-{zone}">{code}</span>'

        table = re.sub(
            r'<span class="spirit-cell-highlight">(-?\d+)</span>',
            restore_zone,
            match.group(0),
        )
        return re.sub(r">\s+<", "><", table).strip()

    failures = []
    has_relation = prefix.startswith("VVD-")
    relation_present = "Capitolul 9. Relații" in text
    if relation_present != has_relation:
        failures.append("capitolul relațional nu corespunde fișei")
    toc_match = re.search(r'<h2 id="cuprins">Cuprins</h2>.*?(<ol>.*?</ol>)', text, re.S)
    toc_links = re.findall(r'<a href="#([^"]+)">', toc_match.group(1)) if toc_match else []
    expected_toc_links = 11 if has_relation else 10
    if len(toc_links) != expected_toc_links:
        failures.append("cuprinsul nu are toate linkurile")
    elif any(f'id="{anchor}"' not in text for anchor in toc_links):
        failures.append("cuprinsul contine linkuri fara destinatie")
    if "Aplicabilitate profesională" not in text or "Concluzii" not in text:
        failures.append("capitole finale lipsă")
    if "Cuvant inainte" in text or "1.7. Tarot" in text:
        failures.append("bloc interzis din template-ul scurt")
    if re.search(r'<img\b[^>]*\bsrc="(?!data:)', text):
        failures.append("imagini relative")
    if main.count("spirit-cell-highlight") != 1:
        failures.append("T-017 nu are exact un marcaj")
    if canonical_spirit_table(text) != canonical_spirit_table(model_text):
        failures.append("T-017 nu respecta structura Dominic")
    if "Ã" in text or "�" in text:
        failures.append("mojibake posibil")
    if f"Index: {prefix}-T-008" not in text or f"Index: {prefix}-T-017" not in text or f"Index: {prefix}-T-019" not in text:
        failures.append("tabele contract lipsa")
    if not css or not model_css or css.group(1) != model_css.group(1):
        failures.append("CSS diferit de modelul Dominic")
    if not re.search(
        rf'Index: {re.escape(prefix)}-T-018</div><div class="table-wrap"><table class="spirit-zones-table">',
        text,
    ):
        failures.append("T-018 nu respecta formatul Dominic")
    if not re.search(
        rf'Index: {re.escape(prefix)}-T-019</div><div class="table-wrap"><table class="stage-table">',
        text,
    ):
        failures.append("T-019 nu respecta chenarul Dominic")
    expression_callout = re.search(
        rf'Index: {re.escape(prefix)}-C-012</div><aside class="callout example">(.*?)</aside>',
        text,
        re.S,
    )
    if not expression_callout or "<strong>Calcul</strong>" not in expression_callout.group(1):
        failures.append("C-012 nu contine calculul Numarului de exprimare")
    if text.count(f"Index: {prefix}-C-012") != 1:
        failures.append("C-012 nu este unic")
    spirit_age_callout = re.search(
        rf'Index: {re.escape(prefix)}-C-003d</div><aside class="callout example">(.*?)</aside>',
        text,
        re.S,
    )
    if not spirit_age_callout or "× 189" not in spirit_age_callout.group(1):
        failures.append("C-003d nu contine calculul Varstei Spiritului")
    if prefix.startswith("DIP-"):
        indexes = re.findall(r'<div class="idx">Index: ([^<]+)</div>', text)
        duplicate_indexes = sorted(index for index in set(indexes) if indexes.count(index) > 1)
        if duplicate_indexes:
            failures.append("indexuri duplicate: " + ", ".join(duplicate_indexes))
        required_subheadings = (
            "1.1. Definiție", "1.2. Caracterul", "1.3. Dorințele", "1.4. Motivația",
            "1.5. Teama", "1.6. Polarități și maturizare", "2.1. Definiție",
            "2.2. Rolul social", "2.3. Interior și exterior", "3.1. Definiție și calcul",
            "3.2. Interpretare", "4.1. Matricea datei de naștere",
            "4.3. Elemente și temperament", "4.4. Masculin și feminin",
            "4.5. Daruri și nevoi", "4.6. Scara bunăstării", "5.1. Numărul activ",
            "5.2. Numărul intim", "5.3. Numărul ereditar",
            "5.4. Numărul ereditar karmic", "5.5. Numărul de realizare",
            "5.6. Numărul de exprimare", "5.7. Codul numerologic al numelui",
            "6.1. Codul Spiritului și vârsta Spiritului", "6.2. Karma din ziua de naștere",
            "6.3. Karma din luna de naștere", "6.4. Karma din Calea Destinului",
            "6.5. Concluzie: direcția de lucru", "8.1. Soarta și Destinul",
            "8.2. Anii importanți", "8.3. Lecțiile de viață", "8.4. Ciclul de 9 ani",
            "8.5. Ciclul de 12 ani",
        )
        headings = re.findall(r'<h3(?:\s[^>]*)?>(.*?)</h3>', text, re.S)
        normalized_headings = {re.sub(r'<[^>]+>', '', heading).strip() for heading in headings}
        missing_subheadings = [heading for heading in required_subheadings if heading not in normalized_headings]
        if missing_subheadings:
            failures.append("subcapitole Ingrid lipsă: " + ", ".join(missing_subheadings))
        required_chapter_indexes = (
            "CAP-005", "CAP-006", "CAP-007", "CAP-008", "CAP-009", "CAP-007b",
            "CAP-010", "CAP-011", "CAP-014", "CAP-015", "CAP-016",
        )
        if any(text.count(f"Index: {prefix}-{suffix}</div>") != 1 for suffix in required_chapter_indexes):
            failures.append("indicii capitolelor Ingrid nu corespund structurii Dominic")
        required_karma_indexes = (
            "P-009a", "C-001a", "G-001a", "P-009b", "P-009b1", "P-009b2",
            "P-013c", "C-002b", "P-013d", "P-013e", "P-013f",
        )
        if any(
            len(re.findall(rf'Index: {re.escape(prefix)}-{re.escape(suffix)}</div>', text)) != 1
            for suffix in required_karma_indexes
        ):
            failures.append("subcapitolele karmice extinse pentru Ingrid au indexuri lipsa sau duplicate")
        if "Arcana <strong>5 — Marele Preot</strong>" not in text:
            failures.append("interpretarea Arcanei 5 lipseste din Karma zilei")
        if "karma din luna <strong>3</strong> este karma independenței de mamă" not in text:
            failures.append("interpretarea lunii 3 lipseste din Karma lunii")
    if failures:
        raise AssertionError(f"{path.name}: " + "; ".join(failures))


def main() -> None:
    made = []
    for spec in PEOPLE:
        person = read_person(spec["yaml"])
        out_dir = ROOT / "output/lucrari" / spec["folder"]
        out_dir.mkdir(parents=True, exist_ok=True)
        report = run_report(person, out_dir)
        html_text = generate_html(person, report, out_dir, spec["prefix"])
        out_path = out_dir / f"{spec['folder']}-scurt-v1.00r.html"
        out_path.write_text(html_text, encoding="utf-8", newline="\n")
        validate_html(out_path, spec["prefix"])
        made.append(out_path)
    for path in made:
        print(path)


if __name__ == "__main__":
    main()

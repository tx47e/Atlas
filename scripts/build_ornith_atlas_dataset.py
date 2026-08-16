#!/usr/bin/env python3
"""Build the Atlas numerology SFT dataset for Ornith/Unsloth Studio.

The dataset is intentionally generated from local Atlas sources so it can be
rebuilt after calculator or template changes. It emits ChatML-style JSONL rows
with an additional metadata object accepted by most dataset upload workflows.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "datasets" / "ornith-atlas-v1"
SOURCE_GLOBS = {
    "calculator": "output/lucrari/**/*calculator.json",
    "reports": "output/lucrari/**/*.md",
    "vault": "vault/Numerologie/**/*.md",
}

SYSTEM_PROMPT = (
    "Ești Asistentul Atlas Numerologie. Răspunzi în română, cu diacritice, "
    "în limbaj simbolic și prudent. Nu inventezi date personale, relaționale "
    "sau biografice. Pentru calcule folosești numai valorile validate primite "
    "din calculatorul Atlas; când o formulă are status de_completat sau partial, "
    "marchezi limita în loc să o completezi din imaginație. După fiecare calcul "
    "prezinți interpretarea rezultatului și, când metoda o cere, sensul valorilor "
    "compuse sau intermediare."
)

MOJIBAKE_MARKERS = ["Ã", "Â", "â€™", "â€œ", "â€", "\ufffd"]
NAME_REPLACEMENTS = {
    "Birsan Daniel Robert": "Persoana Atlas 01",
    "Daniel Robert": "Persoana 01",
    "Daniel": "Alex",
    "Roman Andreea Maria": "Persoana Atlas 02",
    "Andreea Maria": "Persoana 02",
    "Andreea": "Mara",
    "Vulcu Rebeca Andreea": "Persoana Atlas 03",
    "Rebeca Andreea": "Persoana 03",
    "Rebeca": "Rhea",
    "Vulcu Dominic Ioan": "Persoana Atlas 04",
    "Dominic Ioan": "Persoana 04",
    "Dominic": "Dorin",
    "Vulcu Victor Daniel": "Persoana Atlas 05",
    "Victor Daniel": "Persoana 05",
    "Victor": "Vlad",
    "Vulcu Marc Ioan": "Persoana Atlas 06",
    "Marc Ioan": "Persoana 06",
    "Marc": "Matei",
    "Docolin Ingrid Petra": "Persoana Atlas 07",
    "Ingrid Petra": "Persoana 07",
    "Ingrid": "Irina",
    "Szabo Mihai Gabriel": "Persoana Atlas 08",
    "Mihai Gabriel": "Persoana 08",
    "Mihai": "Mircea",
    "Szabo Sabina": "Persoana Atlas 09",
    "Sabina": "Sara",
}
SURNAME_REPLACEMENTS = {
    "Birsan": "Familia Atlas 01",
    "Bîrsan": "Familia Atlas 01",
    "Roman": "Familia Atlas 02",
    "Vulcu": "Familia Atlas 03",
    "Docolin": "Familia Atlas 04",
    "Szabo": "Familia Atlas 05",
}

VALUE_THEMES = {
    0: "potențial conservat, pauză, amplificare sau spațiu care se activează prin context și disciplină",
    1: "inițiativă, identitate, curaj, direcție personală și maturizare prin asumare",
    2: "relație, cooperare, sensibilitate, tact și maturizare prin ascultare",
    3: "exprimare, creativitate, prelucrarea informației și maturizare prin claritate",
    4: "structură, muncă, corp, ordine și maturizare prin consecvență",
    5: "libertate, adaptare, curaj, mobilitate și maturizare prin măsură",
    6: "iubire, grijă, responsabilitate, artă și maturizare prin echilibru afectiv",
    7: "observație, analiză, credință, intuiție și maturizare prin discernământ",
    8: "putere, administrare, rezultate, autoritate și maturizare prin responsabilitate",
    9: "inteligență, compasiune, viziune, transformare și maturizare prin generozitate lucidă",
    10: "închidere și reluare de ciclu, schimbare de ritm și disciplină în fața instabilității",
    11: "sensibilitate înaltă, inspirație, canal intuitiv și nevoie de ancorare",
    12: "serviciu, învățare prin perspectivă, răbdare și transformarea sacrificiului în înțelegere",
    13: "transformare, muncă de reconstrucție, desprindere de vechi și maturizare prin metodă",
    14: "temperanță, adaptare, echilibru între libertate și măsură",
    15: "magnetism, dorință, atașamente și maturizare prin alegere conștientă",
    16: "reconstrucție, adevăr, cădere a formelor fragile și refacere pe bază solidă",
    17: "inspirație, ideal, speranță și condiția de a transforma viziunea în practică",
    18: "sensibilitate, imaginar, frici subtile și maturizare prin clarificare emoțională",
    19: "vizibilitate, vitalitate, reușită și maturizare prin generozitate, nu orgoliu",
    20: "chemare, trezire, bilanț și asumarea unei etape noi",
    21: "integrare, lume largă, închidere de ciclu și maturizare prin finalizare",
    22: "început liber, risc, prospețime și maturizare prin încredere cu discernământ",
    23: "expresie socială, mobilitate și adaptare prin comunicare",
    24: "responsabilitate afectivă, casă, grijă și echilibru între datorie și plăcere",
    25: "căutare, rafinare mentală, studiu și discernământ",
    26: "putere în relație cu resursele, negociere și responsabilitate materială",
    27: "viziune umanitară, intuiție și maturizare prin sens mai larg",
    28: "inițiativă în plan concret, autonomie și reglarea raportului cu autoritatea",
    29: "sensibilitate relațională, idealism și maturizare prin granițe sănătoase",
    30: "creativitate amplificată, voce, expresie și nevoie de finalizare",
    31: "constructor creativ, metodă, răbdare și transformarea ideii în structură",
    32: "comunicare flexibilă, asociere, încredere și ritm social",
    33: "grijă matură, profesor interior, vindecare relațională și responsabilitate afectivă",
    34: "ordine prin analiză, muncă fină și clarificarea pașilor",
    35: "libertate creativă, experiment, adaptare și atenție la dispersie",
    36: "expresie afectivă, familie, artă și maturizare prin responsabilitate emoțională",
    37: "minte profundă, analiză, singurătate fertilă și maturizare prin încredere",
    38: "putere de construcție, organizare și transformarea ambiției în rezultat util",
    39: "numărul minții: inteligență puternică, influență, comparație posibilă și maturizare prin admirație și disciplină",
    40: "structură de bază, limită, ordine și resetare prin muncă pragmatică",
    41: "inițiativă așezată în formă, leadership practic și asumare lucidă",
    42: "cooperare materială, responsabilitate în echipă și stabilitate relațională",
    43: "exprimare construită, comunicare cu structură și atenție la risipirea energiei",
    44: "maestru constructor, forță de materializare și responsabilitate foarte mare",
    45: "libertate pusă în serviciu, adaptare cu scop și încheiere matură",
    46: "grijă practică, familie, rezultate concrete și echilibru între muncă și inimă",
    47: "analiză aplicată, spiritualitate pragmatică și răbdare în construcție",
    48: "putere administrativă, muncă, resurse și maturizare prin etică",
}

CONCEPT_LABELS = {
    "vibratia_interioara": "Vibrația interioară",
    "vibratia_exterioara": "Vibrația exterioară",
    "vibratia_globala": "Vibrația globală",
    "calea_destinului": "Calea Destinului",
    "destinul_vibratia_destinului": "Destinul",
    "puntea_interior_exterior": "Puntea interior-exterior",
    "puntea_interior_destin": "Puntea interior-destin",
    "aspecte_de_indreptat": "Aspectele de îndreptat",
    "solutia_aspectelor_de_indreptat": "Soluția aspectelor de îndreptat",
    "numarul_activ": "Numărul activ",
    "numarul_intim": "Numărul intim",
    "numarul_ereditar": "Numărul ereditar",
    "numarul_ereditar_karmic": "Numărul ereditar karmic",
    "numarul_de_realizare": "Numărul de realizare",
    "numarul_de_exprimare": "Numărul de exprimare",
    "inclinatii_profesionale": "Aplicabilitate profesională",
    "codul_spiritului_si_varsta_spiritului": "Codul Spiritului și vârsta Spiritului",
    "triunghiul_financiar": "Triunghiul financiar",
    "patratul_de_aur_3x3": "Pătratul de Aur",
}

TOPIC_HINTS = {
    "capitolul_2_formule_calcule_tabele_grafice.2.1": "vibratii_fundamentale",
    "capitolul_2_formule_calcule_tabele_grafice.2.2": "matrice",
    "capitolul_2_formule_calcule_tabele_grafice.2.3": "nume",
    "capitolul_2_formule_calcule_tabele_grafice.2.4": "temporal",
    "capitolul_2_formule_calcule_tabele_grafice.2.5": "relational",
    "capitolul_2_formule_calcule_tabele_grafice.2.6": "spirit_karma_profesional",
    "capitolul_2_formule_calcule_tabele_grafice.2.7": "ajutoare",
}


@dataclass
class Example:
    messages: list[dict[str, str]]
    metadata: dict[str, Any]

    def as_json(self) -> str:
        return json.dumps(
            {"messages": self.messages, "metadata": self.metadata},
            ensure_ascii=False,
            separators=(",", ":"),
        )


def sanitize_text(text: str) -> str:
    out = text
    for old in sorted(NAME_REPLACEMENTS, key=len, reverse=True):
        out = out.replace(old, NAME_REPLACEMENTS[old])
    for old, new in SURNAME_REPLACEMENTS.items():
        out = re.sub(rf"\b{re.escape(old)}\b", new, out)
    out = re.sub(r"\b(19|20)\d{2}-\d{2}-\d{2}\b", "[data anonimizată]", out)
    out = re.sub(r"\b\d{2}\.\d{2}\.(19|20)\d{2}\b", "[data anonimizată]", out)
    out = re.sub(r"\b(?:0[1-9]|[12]\d|3[01])(?:0[1-9]|1[0-2])(?:19|20)\d{2}\b", "[data compactă anonimizată]", out)
    out = re.sub(r"\b(19|20)\d{2}\b", "[an anonimizat]", out)
    out = re.sub(r"\b[A-Z]{2,4}-\[an anonimizat\]\d{4}-v[0-9.]+[rf]?-[A-Z0-9-]+\b", "[index Atlas anonimizat]", out)
    out = re.sub(r"\n{3,}", "\n\n", out).strip()
    return out


def clean_markdown(text: str) -> str:
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"!\[\[.*?\]\]", "[imagine eliminată din dataset]", text)
    text = "\n".join(
        line
        for line in text.splitlines()
        if not re.search(r"</?(div|svg|line|circle|polygon|rect|span|img)\b", line)
        and not line.strip().startswith("Index:")
    )
    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    return sanitize_text(text)


def source_ref(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    digest = stable_id(rel)
    if rel.startswith("output/lucrari/"):
        suffix = Path(rel).suffix
        return f"output/lucrari/[anon]/atlas-source-{digest}{suffix}"
    return sanitize_text(rel)


def topic_from_path(path: str) -> str:
    normalized = path.replace("\\", "/")
    for prefix, topic in TOPIC_HINTS.items():
        if prefix in normalized:
            return topic
    lowered = normalized.lower()
    if "nek" in lowered or "numarul ereditar karmic" in lowered:
        return "nume_nek"
    if "kcd" in lowered or "karma din calea destinului" in lowered:
        return "spirit_karma_kcd"
    if "relatii" in lowered or "omulet" in lowered:
        return "relational"
    if "ciclicitati" in lowered or "pinacluri" in lowered:
        return "temporal"
    if "matricea" in lowered:
        return "matrice"
    return "atlas_numerologie"


def value_theme(value: Any) -> str:
    try:
        number = int(value)
    except (TypeError, ValueError):
        return "valoare simbolică ce trebuie interpretată numai în contextul metodei și al datelor validate"
    return VALUE_THEMES.get(
        number,
        "valoare compusă care se citește prin cifra dominantă, contextul calculului și traseul ei de reducere validat",
    )


def get_result(node: Any) -> Any | None:
    if isinstance(node, dict) and "rezultat" in node:
        result = node["rezultat"]
        if isinstance(result, (str, int, float)) and result != "":
            return result
    if isinstance(node, dict) and isinstance(node.get("calcul"), dict) and "rezultat" in node["calcul"]:
        result = node["calcul"]["rezultat"]
        if isinstance(result, (str, int, float)) and result != "":
            return result
    return None


def format_calculation(node: dict[str, Any]) -> str:
    calc = node.get("calcul")
    if isinstance(calc, dict):
        parts = []
        if "intrare" in calc:
            parts.append(f"intrare {calc['intrare']}")
        if calc.get("pasi"):
            parts.append(" -> ".join(str(step) for step in calc["pasi"]))
        if "rezultat" in calc:
            parts.append(f"rezultat {calc['rezultat']}")
        return "; ".join(parts)
    if calc is not None:
        return str(calc)
    if "formula" in node:
        return str(node["formula"])
    return "calcul validat în JSON-ul calculatorului"


def concept_label(path_parts: list[str]) -> str:
    for part in reversed(path_parts):
        if part in CONCEPT_LABELS:
            return CONCEPT_LABELS[part]
    raw = path_parts[-1] if path_parts else "valoare calculată"
    return raw.replace("_", " ").capitalize()


def collect_result_nodes(data: Any, path_parts: list[str] | None = None) -> list[tuple[list[str], dict[str, Any]]]:
    path_parts = path_parts or []
    found: list[tuple[list[str], dict[str, Any]]] = []
    if isinstance(data, dict):
        if get_result(data) is not None and data.get("status") not in {"de_completat", "partial"}:
            found.append((path_parts, data))
        for key, value in data.items():
            if key == "calcul" and isinstance(value, dict) and "rezultat" in value:
                continue
            found.extend(collect_result_nodes(value, [*path_parts, str(key)]))
    elif isinstance(data, list):
        for idx, value in enumerate(data[:12]):
            found.extend(collect_result_nodes(value, [*path_parts, str(idx)]))
    return found


def anonymized_person(data: dict[str, Any], ordinal: int) -> dict[str, Any]:
    src = data.get("date_intrare", {})
    gender = src.get("gen", "nespecificat")
    return {
        "id": f"persoana_atlas_{ordinal:02d}",
        "prenume_activ": "Alex" if gender == "masculin" else "Mara",
        "gen": gender,
        "data_nasterii": "[anonimizată; calculele validate sunt păstrate]",
    }


def assistant_for_calculation(label: str, node: dict[str, Any], topic: str) -> str:
    result = get_result(node)
    formula = node.get("formula", "formula validată în calculatorul Atlas")
    calculation = format_calculation(node)
    interpretation = value_theme(result)
    extra = ""
    if label == "Destinul" and isinstance(node.get("cifra_interpretare"), dict):
        ci = node["cifra_interpretare"].get("rezultat")
        extra = (
            f"\n- cifra de interpretare: **{ci}**; aceasta oferă cheia de lectură practică, "
            f"dar nu înlocuiește Destinul compus **{result}**."
        )
    if topic == "relational":
        extra += "\n- limită: interpretarea relațională se redactează numai când există date pentru ambele persoane."
    return (
        f"input:\n- concept: {label}\n- sursă: calculator Atlas\n\n"
        f"calculation:\n- formulă: {formula}\n- traseu: {calculation}\n- rezultat: **{result}**{extra}\n\n"
        f"interpretation:\nRezultatul **{result}** indică {interpretation}. "
        "În redactarea Atlas, această valoare nu se transformă într-un verdict; se explică drept "
        "direcție de lucru, resursă, umbră posibilă și maturizare practică, legată de contextul "
        f"conceptului {label}."
    )


def make_calculator_examples() -> list[Example]:
    examples: list[Example] = []
    for ordinal, path in enumerate(sorted(ROOT.glob(SOURCE_GLOBS["calculator"])), start=1):
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        person = anonymized_person(data, ordinal)
        rel_path = source_ref(path)
        for path_parts, node in collect_result_nodes(data):
            label = concept_label(path_parts)
            dotted = ".".join(path_parts)
            topic = topic_from_path(dotted)
            examples.append(
                Example(
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {
                            "role": "user",
                            "content": (
                                "Redactează pentru dataset un exemplu calculator-grounded. "
                                f"Persoană anonimizată: {json.dumps(person, ensure_ascii=False)}. "
                                f"Concept: {label}. Include input, calculation și interpretation."
                            ),
                        },
                        {"role": "assistant", "content": assistant_for_calculation(label, node, topic)},
                    ],
                    metadata={
                        "id": stable_id("calculator", rel_path, dotted),
                        "source": "calculator",
                        "source_path": rel_path,
                        "topic": topic,
                        "concept": label,
                        "quality": "calculator_grounded",
                        "requires_interpretation": True,
                    },
                )
            )
    return examples


def split_into_sections(text: str) -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    current_title = ""
    current_lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("#"):
            if current_lines:
                sections.append((current_title or "Fragment", "\n".join(current_lines).strip()))
            current_title = line.lstrip("#").strip()
            current_lines = [line]
        else:
            current_lines.append(line)
    if current_lines:
        sections.append((current_title or "Fragment", "\n".join(current_lines).strip()))
    return [(title, body) for title, body in sections if len(body) >= 250]


def make_vault_examples() -> list[Example]:
    examples: list[Example] = []
    selected = [
        *sorted((ROOT / "vault" / "Numerologie" / "Vibratii").glob("Vibratia */0[2-7]-*.md")),
        *sorted((ROOT / "vault" / "Numerologie" / "Nume").glob("**/0[2-5]-*.md")),
        *sorted((ROOT / "vault" / "Numerologie" / "Spirit si Karma").glob("**/0[2-5]-*.md")),
        *sorted((ROOT / "vault" / "Numerologie" / "Ciclicitati").glob("**/0[2-5]-*.md")),
        *sorted((ROOT / "vault" / "Numerologie" / "Relatii").glob("**/0[2-5]-*.md")),
        *sorted((ROOT / "vault" / "Numerologie" / "Nume" / "Numarul Ereditar Karmic" / "NEK - Interpretari").glob("NEKI-NN-*.md")),
        *sorted((ROOT / "vault" / "Numerologie" / "Spirit si Karma" / "Karma din Calea Destinului" / "KCD - Interpretari").glob("KCDI-NN-*.md")),
    ]
    seen: set[Path] = set()
    for path in selected:
        if path in seen or not path.exists():
            continue
        seen.add(path)
        rel_path = source_ref(path)
        text = clean_markdown(path.read_text(encoding="utf-8"))
        for index, (title, body) in enumerate(split_into_sections(text)[:2]):
            body = trim(body, 1800)
            examples.append(
                Example(
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {
                            "role": "user",
                            "content": (
                                f"Explică pentru Asistentul Atlas conceptul sau interpretarea: {title}. "
                                "Păstrează formularea canonică și nu inventa extensii."
                            ),
                        },
                        {
                            "role": "assistant",
                            "content": (
                                f"input:\n- sursă: Vault Numerologie\n- titlu: {title}\n\n"
                                "calculation:\n- dacă textul conține formule, acestea rămân sursa canonică; "
                                "dacă nu conține formule, nu se inventează un calcul.\n\n"
                                f"interpretation:\n{body}"
                            ),
                        },
                    ],
                    metadata={
                        "id": stable_id("vault", rel_path, str(index)),
                        "source": "vault",
                        "source_path": rel_path,
                        "topic": topic_from_path(rel_path),
                        "concept": title,
                        "quality": "canonical_vault",
                        "requires_interpretation": True,
                    },
                )
            )
    return examples


def make_report_examples() -> list[Example]:
    examples: list[Example] = []
    paths = sorted(ROOT.glob(SOURCE_GLOBS["reports"]))
    final_or_revision = [
        p
        for p in paths
        if ("scurt-v1.00f" in p.name or "scurt-v1.00r" in p.name or re.search(r"v1\.\d+r\.md$", p.name))
        and "Untitled" not in p.name
    ]
    headings = re.compile(
        r"^(#{2,4}\s+.*(?:Vibra|Destin|Matrice|Numele|Spirit|Karma|Pinacl|Ciclicit|Rela|Aplicabilitate|Concluzii).*)$",
        re.M,
    )
    for path in final_or_revision:
        rel_path = source_ref(path)
        text = clean_markdown(path.read_text(encoding="utf-8"))
        starts = [m.start() for m in headings.finditer(text)]
        for index, start in enumerate(starts[:10]):
            end = starts[index + 1] if index + 1 < len(starts) else min(len(text), start + 2400)
            chunk = trim(text[start:end], 2200)
            if len(chunk) < 500:
                continue
            title = chunk.splitlines()[0].lstrip("#").strip()
            examples.append(
                Example(
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {
                            "role": "user",
                            "content": (
                                f"Redactează un fragment în stil Atlas pentru secțiunea: {title}. "
                                "Respectă tonul conversațional și păstrează calculele ca sursă, nu ca invenție."
                            ),
                        },
                        {
                            "role": "assistant",
                            "content": (
                                "input:\n- tip: fragment de lucrare Atlas anonimizat\n\n"
                                "calculation:\n- valorile sunt cele validate în lucrarea-sursă și trebuie păstrate ca atare.\n\n"
                                f"interpretation:\n{chunk}"
                            ),
                        },
                    ],
                    metadata={
                        "id": stable_id("report", rel_path, str(index)),
                        "source": "approved_report",
                        "source_path": rel_path,
                        "topic": topic_from_path(title),
                        "concept": title,
                        "quality": "approved_style",
                        "requires_interpretation": True,
                    },
                )
            )
    return examples


def make_rule_examples() -> list[Example]:
    rules = [
        (
            "Destin compus",
            "Cum tratezi Destinul 12 când cifra de interpretare este 3?",
            "calculation:\n- Calea Destinului se însumează o singură dată: 39 -> **12**.\n- cifra de interpretare se reduce complet: 12 -> **3**.\n\ninterpretation:\nDestinul rămâne **12** și se citește ca valoare compusă: învățare prin perspectivă, răbdare și schimbarea felului de a privi viața. Cifra **3** este cheia practică de interpretare: exprimare, creativitate și clarificarea mesajului. Nu înlocuiești Destinul **12** cu **3** în formulele care cer Destinul compus, mai ales la Pinacluri.",
        ),
        (
            "T-008",
            "Ce faci cu zerourile din produsul lecțiilor de viață?",
            "calculation:\n- produsul se obține din zi x lună x an.\n- șirul de lecții păstrează toate cifrele produsului, inclusiv fiecare **0**.\n\ninterpretation:\nCifra **0** nu se elimină și nu se comprimă. Ea indică o lecție conservată, o pauză sau un potențial care se activează prin context, oameni, disciplină și exercițiu. Tabelul T-008 trebuie să aibă câte o coloană pentru fiecare cifră din produs.",
        ),
        (
            "Relații opționale",
            "Cum răspunzi dacă nu există date pentru relație?",
            "calculation:\n- calculatorul marchează relația ca de_completat când lipsește a doua persoană.\n\ninterpretation:\nNu inventezi partener, tip de relație, rezultat comun sau temă de rezolvat. Omiți capitolul Relații și explici pe scurt că analiza relațională cere datele ambelor persoane.",
        ),
        (
            "NEK dictat",
            "Cum folosești interpretările pentru Numărul ereditar karmic?",
            "calculation:\n- NEK se calculează în intervalul 1-22.\n- valoarea selectează interpretarea predefinită și Arcana Majoră asociată.\n\ninterpretation:\nPentru NEK folosești textul dictat ca sursă canonică, fără să îl diluezi sau să inventezi alt neam. Poți adăuga numai legarea editorială cerută de lucrare și linia de Tarot asociată.",
        ),
        (
            "Status partial",
            "Ce faci cu o formulă marcată partial sau de_completat?",
            "calculation:\n- status: partial/de_completat înseamnă că formula nu este complet validată operațional.\n\ninterpretation:\nMarchezi limita și nu completezi din imaginație. Dacă utilizatorul cere interpretare, explici că se poate lucra doar cu valorile validate disponibile și că formula lipsă trebuie confirmată în Vault/calculator înainte de livrare.",
        ),
    ]
    examples: list[Example] = []
    for title, user, answer in rules:
        examples.append(
            Example(
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user},
                    {"role": "assistant", "content": f"input:\n- regulă: {title}\n\n{answer}"},
                ],
                metadata={
                    "id": stable_id("rule", title),
                    "source": "skill_rules",
                    "source_path": "skills/numerologie-lucrare-redactare/SKILL.md",
                    "topic": "rules_negative_cases",
                    "concept": title,
                    "quality": "canonical_rule",
                    "requires_interpretation": True,
                },
            )
        )
    return examples


def trim(text: str, limit: int) -> str:
    text = text.strip()
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit("\n", 1)[0].strip()
    return f"{cut}\n\n[fragment trunchiat pentru dataset]"


def stable_id(*parts: str) -> str:
    payload = "|".join(parts)
    return hashlib.sha1(payload.encode("utf-8")).hexdigest()[:16]


def dedupe(examples: list[Example]) -> list[Example]:
    seen: set[str] = set()
    out: list[Example] = []
    for ex in examples:
        key = stable_id(json.dumps(ex.messages, ensure_ascii=False))
        if key in seen:
            continue
        seen.add(key)
        out.append(ex)
    return out


def split_examples(examples: list[Example]) -> dict[str, list[Example]]:
    by_source: dict[str, list[Example]] = {"train": [], "validation": [], "test": []}
    ordered = sorted(examples, key=lambda ex: ex.metadata["id"])
    for ex in ordered:
        bucket = int(ex.metadata["id"][:4], 16) % 10
        if bucket == 0:
            by_source["test"].append(ex)
        elif bucket == 1:
            by_source["validation"].append(ex)
        else:
            by_source["train"].append(ex)
    return by_source


def validate_examples(examples: list[Example]) -> list[str]:
    errors: list[str] = []
    ids: Counter[str] = Counter()
    for ex in examples:
        mid = str(ex.metadata.get("id", ""))
        ids[mid] += 1
        roles = [m.get("role") for m in ex.messages]
        if roles[:2] != ["system", "user"] or roles[-1] != "assistant":
            errors.append(f"{mid}: invalid role order {roles}")
        if not ex.messages[-1].get("content"):
            errors.append(f"{mid}: empty assistant message")
        if ex.metadata.get("requires_interpretation") and "interpretation:" not in ex.messages[-1]["content"]:
            errors.append(f"{mid}: missing interpretation section")
        if "calculation:" not in ex.messages[-1]["content"]:
            errors.append(f"{mid}: missing calculation section")
        whole = json.dumps({"messages": ex.messages, "metadata": ex.metadata}, ensure_ascii=False)
        for marker in MOJIBAKE_MARKERS:
            if marker in whole:
                errors.append(f"{mid}: possible mojibake marker {marker!r}")
    for mid, count in ids.items():
        if count > 1:
            errors.append(f"{mid}: duplicate id")
    return errors


def write_jsonl(path: Path, examples: list[Example]) -> None:
    path.write_text("\n".join(ex.as_json() for ex in examples) + "\n", encoding="utf-8")


def write_manifest(splits: dict[str, list[Example]], all_examples: list[Example]) -> None:
    topics = Counter(ex.metadata["topic"] for ex in all_examples)
    sources = Counter(ex.metadata["source"] for ex in all_examples)
    manifest = {
        "name": "ornith-atlas-v1",
        "created_at": date.today().isoformat(),
        "target_model": "unsloth/Ornith-1.0-9B",
        "training_type": "SFT/LoRA",
        "format": "ChatML JSONL with messages plus metadata",
        "purpose": "Asistent Atlas Numerologie cu interpretări pentru toate valorile calculate",
        "counts": {split: len(rows) for split, rows in splits.items()},
        "total_examples": len(all_examples),
        "topics": dict(sorted(topics.items())),
        "sources": dict(sorted(sources.items())),
        "anonymization": {
            "names": "replaced with stable placeholders",
            "dates": "date-like strings in report/vault prose replaced; calculator examples keep validated values without exposing full identity",
            "media": "images and embeds removed from dataset rows",
        },
        "source_globs": SOURCE_GLOBS,
        "validation_rules": [
            "valid JSONL",
            "messages must contain system, user and assistant roles",
            "calculator-grounded examples must include calculation and interpretation sections",
            "do not reduce compound values unless the method explicitly requires an interpretation digit",
            "no mojibake markers",
            "no invented relational data",
        ],
    }
    (OUT_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_recipe_notes(splits: dict[str, list[Example]]) -> None:
    notes = f"""# Ornith Atlas v1 - Unsloth Studio Recipe Notes

## Dataset

- Format: ChatML/OpenAI-style JSONL, one object per row.
- Training file: `train.jsonl` ({len(splits['train'])} rows).
- Validation file: `validation.jsonl` ({len(splits['validation'])} rows).
- Test file: `test.jsonl` ({len(splits['test'])} rows).
- Model target: `unsloth/Ornith-1.0-9B`.
- Training mode: SFT/LoRA.

Each row contains:

```json
{{"messages":[{{"role":"system","content":"..."}},{{"role":"user","content":"..."}},{{"role":"assistant","content":"..."}}],"metadata":{{"...":"..."}}}}
```

## Data Recipes Setup

1. Open Unsloth Studio and go to Data Recipes.
2. Create a new recipe named `ornith-atlas-v1`.
3. Add a local JSONL Seed block and select `train.jsonl`.
4. Map the conversation column to `messages`; keep `metadata` as auxiliary metadata.
5. Add an Expression validation block with these checks:
   - every row has `messages`;
   - roles include `system`, `user`, `assistant`;
   - assistant output contains `calculation:` and `interpretation:`;
   - text does not contain mojibake markers: `Ã`, `Â`, `â€™`, `â€œ`, `â€`, `�`.
6. Optional: add an LLM Judge block and score:
   - fidelity to calculator values;
   - interpretation included for every result;
   - Romanian with diacritics;
   - symbolic/prudent language;
   - no invented personal or relational data.
7. Run preview, inspect 20-50 rows across topics, then run the full dataset build.
8. Select the persisted dataset in Studio and fine-tune `unsloth/Ornith-1.0-9B`.

## Acceptance Prompts

- Explică Destinul 12 cu cifra de interpretare 3 fără să îl reduci greșit.
- Redactează interpretarea pentru T-008 când produsul conține 0.
- Oferă interpretare pentru Numărul ereditar karmic 16 și Arcana asociată.
- Spune ce faci dacă datele relaționale lipsesc.
- Interpretează DA/NU profesional fără să confunzi obstacolul cu lipsa talentului.

## Notes

This is a first Atlas-assistant SFT dataset. For a later phase, add a separate CPT corpus from Vault prose only, if the goal becomes deeper memorization rather than instruction behavior.
"""
    (OUT_DIR / "recipe-notes.md").write_text(notes, encoding="utf-8")


def build() -> tuple[list[Example], dict[str, list[Example]]]:
    examples = dedupe(
        [
            *make_calculator_examples(),
            *make_vault_examples(),
            *make_report_examples(),
            *make_rule_examples(),
        ]
    )
    errors = validate_examples(examples)
    if errors:
        raise SystemExit("Dataset validation failed before write:\n" + "\n".join(errors[:50]))
    splits = split_examples(examples)
    return examples, splits


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--validate-only", action="store_true", help="Validate existing generated JSONL files.")
    args = parser.parse_args()

    if args.validate_only:
        examples: list[Example] = []
        for split in ["train", "validation", "test"]:
            path = OUT_DIR / f"{split}.jsonl"
            for line in path.read_text(encoding="utf-8").splitlines():
                row = json.loads(line)
                examples.append(Example(messages=row["messages"], metadata=row["metadata"]))
        errors = validate_examples(examples)
        if errors:
            raise SystemExit("Dataset validation failed:\n" + "\n".join(errors[:50]))
        print(f"DATASET_VALIDATION=OK examples={len(examples)}")
        return

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    examples, splits = build()
    for split, rows in splits.items():
        write_jsonl(OUT_DIR / f"{split}.jsonl", rows)
    write_manifest(splits, examples)
    write_recipe_notes(splits)
    print("DATASET_BUILD=OK")
    print(f"output={OUT_DIR}")
    print(f"examples={len(examples)}")
    for split, rows in splits.items():
        print(f"{split}={len(rows)}")


if __name__ == "__main__":
    main()

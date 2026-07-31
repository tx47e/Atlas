from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DANIEL = ROOT / "output/lucrari/1998-02-19-BIRSAN-DANIEL-ROBERT/1998-02-19-BIRSAN-DANIEL-ROBERT-scurt-v1.00r.md"
OUT_DIR = ROOT / "output/lucrari/1998-01-12-ROMAN-ANDREEA-MARIA"
OUT = OUT_DIR / "1998-01-12-ROMAN-ANDREEA-MARIA-scurt-v1.00r.md"
REPORT = OUT_DIR / "1998-01-12-ROMAN-ANDREEA-MARIA-scurt-v1.00r-calculator.json"
PREFIX = "RAM-19980112-v1.00r"


def replace_block(text: str, suffix: str, body: str) -> str:
    marker = f"Index: {PREFIX}-{suffix}"
    pattern = rf"({re.escape(marker)}\n)(.*?)(?=\nIndex: {re.escape(PREFIX)}-|\Z)"
    updated, count = re.subn(pattern, lambda m: m.group(1) + body.rstrip() + "\n", text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"Blocul {suffix} nu a fost găsit o singură dată: {count}")
    return updated


def matrix_table(casute: dict[str, dict]) -> str:
    element = {1: "Foc", 2: "Apă", 3: "Aer", 4: "Pământ", 5: "Foc", 6: "Apă", 7: "Aer", 8: "Pământ", 9: "Foc"}
    optim = {1: "111", 2: "222", 3: "333", 4: "44", 5: "55", 6: "66", 7: "7", 8: "8", 9: "9"}
    geom = {0: "absent", 1: "○", 2: "○—○", 3: "△"}
    def cell(n: int) -> str:
        item = casute[str(n)]
        count = item["cantitate"]
        symbol = geom.get(count, "□")
        return f"**{n} — {element[n]}** · {item['cifre']} · optim `{optim[n]}` · {symbol}"
    return "\n".join([
        f"| {cell(1)} | {cell(4)} | {cell(7)} |",
        "| --- | --- | --- |",
        f"| {cell(2)} | {cell(5)} | {cell(8)} |",
        f"| {cell(3)} | {cell(6)} | {cell(9)} |",
    ])


def name_matrix_table(date_boxes: dict[str, dict], name_boxes: dict[str, dict]) -> str:
    optim = {1: "111", 2: "222", 3: "333", 4: "44", 5: "55", 6: "66", 7: "7", 8: "8", 9: "9"}
    geom = {0: "absent", 1: "○", 2: "○—○", 3: "△"}
    def cell(n: int) -> str:
        d, x = date_boxes[str(n)], name_boxes[str(n)]
        symbol = geom.get(x["cantitate"], "□")
        return f"**data {d['cifre']}** · nume {x['cifre']} · optim `{optim[n]}` · {symbol}"
    return "\n".join([
        f"| {cell(1)} | {cell(4)} | {cell(7)} |",
        "| --- | --- | --- |",
        f"| {cell(2)} | {cell(5)} | {cell(8)} |",
        f"| {cell(3)} | {cell(6)} | {cell(9)} |",
    ])


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


def spirit_table_from_daniel(source: str) -> str:
    m = re.search(r"\| Ziua \| I \| II .*?\n(?=\nIndex: BDR-19980219-v1\.00r-P-186)", source, re.S)
    if not m:
        raise RuntimeError("Tabelul Codului Spiritului nu a fost găsit")
    table = m.group(0)
    table = table.replace('<span class="spirit-cell-highlight">32</span>', '<span class="spirit-zone-material">32</span>')
    table = table.replace(
        '| 12 | <span class="spirit-zone-gifts">41</span>',
        '| 12 | <span class="spirit-cell-highlight">41</span>',
        1,
    )
    return table.rstrip()


def lesson_table(lessons: list[int], start_year: int = 1998, end_age: int = 60) -> str:
    headers = " | ".join(f'Lecția {i + 1} — <strong style="font-size: 1.15em; font-weight: 700;">{v}</strong>' for i, v in enumerate(lessons))
    lines = [f"| Vârstă | {headers} |", "| --- | ---: | ---: | ---: | ---: | ---: |"]
    for start_age in range(1, end_age + 1, 5):
        vals = []
        for offset in range(5):
            age = start_age + offset
            year = start_year + age - 1
            val = str(year)
            if year == 2026:
                val = f'<span style="color: #b3261e; font-weight: 700;">{year}</span>'
            vals.append(val)
        lines.append(f"| {start_age}–{start_age + 4} | " + " | ".join(vals) + " |")
    return "\n".join(lines)


def cycle9_table(start_year: int = 1998) -> str:
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


def main() -> None:
    source = DANIEL.read_text(encoding="utf-8")
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    calc = report["capitolul_2_formule_calcule_tabele_grafice"]
    base = calc["2.1_codul_numerologic_personal_data_nasterii"]
    matrix = calc["2.2_structura_matriciala"]
    name = calc["2.3_codul_numerologic_personal_al_numelui"]
    cycles = calc["2.4_ciclicitati"]

    text = source
    replacements = {
        "Bîrsan Daniel Robert": "Roman Andreea Maria",
        "Birsan Daniel Robert": "Roman Andreea Maria",
        "BDR-19980219-v1.00r": PREFIX,
        "BDR-19980219": "RAM-19980112",
        "1998-02-19-BIRSAN-DANIEL-ROBERT": "1998-01-12-ROMAN-ANDREEA-MARIA",
        "19.02.1998": "12.01.1998",
        "1998-02-19": "1998-01-12",
        "Daniel": "Andreea",
        "masculin": "feminin",
        "18.07.2026": "31.07.2026",
        "soarta-si-destin-birsan-daniel-robert.svg": "soarta-si-destin-roman-andreea-maria.svg",
        "harta-suprapusa-soarta-destin-birsan-daniel-robert-v1.00r.svg": "harta-suprapusa-soarta-destin-roman-andreea-maria-v1.00r.svg",
        "omulet-relatii-birsan-daniel-robert-roman-andreea-maria.png": "omulet-relatii-roman-andreea-maria-birsan-daniel-robert.png",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = text.replace("Relație analizată: Roman Andreea Maria, 12.01.1998, parteneră", "Relație analizată: Bîrsan Daniel Robert, 19.02.1998, partener")

    blocks: dict[str, str] = {
        "C-001": "> [!example] Calcul\n> Ziua din data de naștere = **12** → 1 + 2 = **3**",
        "P-007": "Andreea, tu ai vibrația interioară **3**: expresie, creativitate, relaționare și bucuria de a pune ideile în circulație. Arhetipal, această energie te apropie de Creator, Comunicator și Povestitor. Traseul tău adaugă o nuanță importantă: **1** pornește și își asumă inițiativa, iar **2** răspunde prin cooperare și sensibilitate; împreună formează **3**, vocea care leagă oamenii și transformă experiența într-un mesaj. Maturizarea apare când nu te împrăștii între prea multe idei, ci alegi una, îi dai formă și o duci până la un rezultat care poate fi văzut și folosit.",
        "P-008": "Îți dorești libertatea de a te exprima, oameni cu care poți schimba idei și contexte în care imaginația ta primește răspuns. Ai nevoie să simți că viața nu este doar obligație, ci și descoperire, dialog și creație.",
        "P-009": "Te motivează proiectele în care poți cerceta, explica, conecta oameni sau transforma o idee într-o experiență vie. O rutină potrivită este să alegi zilnic o singură idee pe care o finalizezi înainte să deschizi alte direcții.",
        "P-010": "Umbra lui **3** este dispersia, promisiunea făcută din entuziasm și sensibilitatea la lipsa de răspuns. Când apare teama că nu vei fi auzită, poți vorbi prea mult sau te poți retrage brusc. Întrebarea matură este: «Care este mesajul esențial și ce formă concretă îi dau?»",
        "T-009": """<table class="polarities-table"><tbody><tr><th scope="row">Polarități pozitive</th><td><ul><li>creativitate și imaginație;</li><li>comunicare vie și capacitate de relaționare;</li><li>curiozitate și adaptare;</li><li>talent de a explica și de a transmite;</li><li>optimism care pune oamenii în mișcare.</li></ul></td></tr><tr><th scope="row">Polarități negative</th><td><ul><li>dispersie și prea multe începuturi;</li><li>nevoie de validare;</li><li>promisiuni fără continuitate;</li><li>dramatizare sau evitare prin glumă;</li><li>dificultatea de a păstra ritmul.</li></ul></td></tr><tr><th scope="row">Direcții de dezvoltare</th><td><ul><li>alege priorități puține și clare;</li><li>transformă ideea în produs, text sau acțiune;</li><li>păstrează un ritm de finalizare;</li><li>ascultă înainte să răspunzi;</li><li>folosește feedbackul ca orientare, nu ca verdict.</li></ul></td></tr></tbody></table>""",
        "P-010a": "Vibrația interioară **3** este asociată cu Arcana Majoră **3 — Împărăteasa**. Ea arată puterea de a hrăni o idee până când devine formă, relație, proiect sau rezultat. Pentru tine, creativitatea nu înseamnă numai inspirație, ci și capacitatea de a face un spațiu să crească, de a aduce frumusețe și de a-i ajuta pe oameni să se simtă văzuți.",
        "P-010b": "Împărăteasa este înconjurată de natură roditoare, semn că abundența apare când energia este îngrijită și lăsată să se maturizeze. Imaginea îți amintește că talentul tău de a comunica și crea are nevoie de răbdare, ritm și grijă pentru corp. Când nu forțezi rodul, dar nici nu abandonezi procesul, ideile tale capătă consistență.",
        "T-010": """<table><tbody><tr><td><div>Index: RAM-19980112-v1.00r-G-001</div><img src="tarot-03-imparateasa-vibratia-interioara.jpg" alt="Arcana 3 — Împărăteasa" width="190"><div><em>Arcana <strong>3</strong> — Împărăteasa</em></div></td><td><ul><li><strong>Resursă:</strong> creativitate, expresivitate și capacitatea de a face lucrurile să crească.</li><li><strong>Manifestare:</strong> comunici, conectezi oameni și dai o formă atrăgătoare ideilor.</li><li><strong>Umbră:</strong> te poți împrăștia, poți căuta validare sau poți amâna finalizarea.</li><li><strong>Maturizare:</strong> hrănești o direcție suficient de mult încât să devină rezultat.</li></ul></td></tr></tbody></table>""",
        "C-002": "> [!example] Calcul\n> Luna din data de naștere = **1**",
        "P-012": "Fiind născută în luna ianuarie, ai rolul social al Pionierului, specific vibrației exterioare **1**. Oamenii te pot percepe directă, hotărâtă și capabilă să pornești lucruri. Succesul social vine când îți asumi inițiativa fără să ocupi tot spațiul și când claritatea ta deschide calea și pentru contribuția celorlalți.",
        "P-013": "Andreea, dacă în interior ești **3**, la exterior oamenii te pot percepe ca pe un **1**. Înăuntru ai nevoie de dialog, creativitate și varietate; în exterior poți apărea mai fermă și mai decisă. **3** spune «hai să găsim o idee», iar **1** spune «hai să începem». Împreună te ajută să transformi comunicarea în inițiativă.",
        "P-013a": "Puntea dintre interior și exterior arată ajustarea dintre expresivitatea ta lăuntrică și imaginea hotărâtă pe care o proiectezi. Ea te ajută să observi când inițiativa lui **1** exprimă autentic creativitatea lui **3** și când, dimpotrivă, graba taie dialogul de care ai nevoie.",
        "C-002a": "> [!example] Calculul punții interior–exterior\n> |**3** − **1**| = **2**",
        "P-013b": "Rezultatul **2** cere autenticitate prin cooperare. Spune limpede ce vrei să pornești, dar întreabă și ce vede celălalt. Când îmbini inițiativa cu ascultarea, oamenii te pot accepta ca lider fără ezitare, pentru că direcția ta nu îi exclude, ci îi ajută să își găsească locul în construcție.",
        "C-003": "> [!example] Calcul\n> Toate cifrele adunate din data de naștere = 1 + 2 + 0 + 1 + 1 + 9 + 9 + 8 = **31** → 3 + 1 = **4**",
        "P-015": "Andreea, Destinul compus **4** păstrează întâlnirea dintre **3**, care comunică și creează, și **1**, care inițiază și își asumă direcția. Rezultatul **4** îți cere să transformi această combinație într-o construcție stabilă: program, reguli, corp îngrijit, responsabilități clare și rezultate repetabile. Darul tău este să dai formă ideilor; umbra este să simți structura ca pe o limitare sau, invers, să devii rigidă când vrei siguranță. Maturizarea apare când disciplina devine cadrul care îți protejează creativitatea.",
        "C-004": "> [!example] Calcul\n> Data nașterii: 12.01.1998 → data compactă = **12011998**  \n> N1 = 1 + 2 + 0 + 1 + 1 + 9 + 9 + 8 = **31**  \n> N2 = 3 + 1 = **4**  \n> N3 = 31 − (2 × 1) = **29**  \n> N4 = 2 + 9 = **11**  \n> Șir complet = 12011998 + 31 + 4 + 29 + 11 = **120119983142911**",
        "G-002": matrix_table(matrix["casute"]),
        "P-035": "**Căsuța 1.** Ai **6** apariții. Psihicul, inițiativa și voința sunt foarte intense: poți susține presiune, poți genera multe idei și poți prelua conducerea. Umbra este rigiditatea și tendința de a decide că numai varianta ta este corectă. Puterea ta devine matură atunci când conduci fără să transformi fermitatea în control.",
        "P-036": "**Căsuța 2.** Ai **2** apariții. Emoțiile, comunicarea și colaborarea circulă în ambele sensuri: poți primi și oferi sprijin. Numărul par de apariții poate aduce indecizie, de aceea te ajută să numești ce simți și să alegi după un dialog clar.",
        "P-037": "**Căsuța 3.** Ai **1** apariție. Relațiile și prelucrarea informației sunt disponibile, dar au nevoie de focalizare. Curiozitatea te ajută să cercetezi; maturizarea apare când selectezi esențialul și îl transmiți fără să te risipești.",
        "P-038": "**Căsuța 4.** Ai **1** apariție. Corpul, organizarea și orientarea spre rezultate concrete îți oferă o bază accesibilă. Ea rămâne sănătoasă când îți respecți programul, somnul și mișcarea, fără să transformi ordinea în perfecționism.",
        "P-039": "**Căsuța 5.** Nu ai apariții, iar energia libertății, stimei de sine, curajului și nonconformismului este conservată. Ea se activează prin oameni și contexte care te încurajează să ieși din tipare. Construiește-o prin experiențe noi, limite sănătoase și alegeri asumate.",
        "P-040": "**Căsuța 6.** Nu ai apariții. Iubirea ca ocrotire, pragmatismul, familia și administrarea concretă pot oscila și au nevoie de aport extern. Responsabilitățile împărțite, bugetul și ritualurile de familie te ajută să transformi intenția afectivă în grijă vizibilă.",
        "P-041": "**Căsuța 7.** Nu ai apariții. Analiza profundă, solitudinea și înțelepciunea sunt energii conservate, construite prin studiu, repaus și experiențe care te obligă să încetinești. Nu căuta răspunsul numai în reacția rapidă; lasă-i timp să se așeze.",
        "P-042": "**Căsuța 8.** Ai **1** apariție. Puterea, responsabilitatea și performanța sunt disponibile într-o formă echilibrată. Folosește-le pentru a administra corect și a duce lucrurile până la capăt, fără să preiei poverile tuturor.",
        "P-043": "**Căsuța 9.** Ai **3** apariții. Inteligența, memoria, transformarea și orientarea către idealuri sunt puternice. Poți învăța repede și vedea imaginea largă; protejează această resursă prin priorități și pauze, ca mintea să nu devină suprasolicitată.",
        "P-045": "Temperamentul tău predominant este **coleric**: Focul are **9** apariții, față de Pământ cu **2**, Apă cu **2** și Aer cu **1**. Reacționezi repede și ai multă energie de pornire. Echilibrul vine când dai Focului un scop, iar corpul, emoțiile și reflecția primesc timp egal în program.",
        "P-017": """<div class="parity-chart framed-panel" style="width:100%;max-width:none" role="img" aria-label="Din totalul de 14 cifre, 10 sunt impare și 4 sunt pare."><div class="parity-chart-total">Total: <strong>14</strong> cifre</div><div class="parity-chart-bar"><span class="parity-odd" style="width:71.43%"><strong>Impare · 10</strong></span><span class="parity-even" style="width:28.57%"><strong>Pare · 4</strong></span></div></div>\n\nMatricea are **10** apariții impare și **4** pare. Inițiativa și proiecția sunt dominante, iar energia receptivă există ca resursă de echilibru. Cifrele pare te ajută să primești și să dai mai departe, dar pot aduce indecizie; folosește dialogul ca să clarifici, apoi alege fără să prelungești oscilația.""",
        "P-018": "Darurile și nevoile se citesc din căsuțele cu cel puțin **2** cifre: la tine sunt **1**, **2** și **9**. Darurile sunt voința și inițiativa, sensibilitatea relațională și forța mentală. Nevoile corespunzătoare sunt autonomia și respectul pentru propria direcție (**1**), siguranța emoțională și cooperarea (**2**), precum și sensul, învățarea și transformarea (**9**).",
        "P-019": "Scara bunăstării arată că treapta cea mai înaltă este vectorul **789, Creativitate**, cu **35**. El este susținut îndeaproape de diagonala **159, Carieră**, cu **33**, și de vectorul **369, Bunăstare materială**, cu **30**. Pentru tine, împlinirea crește când mintea și capacitatea de transformare din căsuța **9** alimentează energia de lucru din vectorul **123, Energie**, iar ideile sunt așezate într-o carieră și într-o structură materială. Creativitatea nu este separată de bani: devine prosperă când are termen, formă, preț și continuitate.",
        "G-004": wellbeing(matrix["scara_bunastarii"]),
        "C-009": "> [!example] Calcul\n> Andreea = 30 → 3 + 0 = **3**",
        "P-021": "Numărul activ **3** aduce în comportamentul tău curent comunicare, curiozitate și capacitatea de a face conexiuni. Resursa este să explici și să apropii oamenii; umbra este să deschizi prea multe direcții. Alege mesajul principal și încheie ceea ce ai promis.",
        "C-009a": "> [!example] Calcul\n> Vocalele = 30 → 3 + 0 = **3**",
        "P-021c": "Numărul intim **3** caută bucurie, dialog și libertatea de a crea. Te hrănesc oamenii cu care poți fi spontană și proiectele care îți dau o voce. Umbra este dependența de reacția publicului; păstrează creația vie chiar și când validarea întârzie.",
        "C-008": "> [!example] Calcul\n> Roman = 25 → 2 + 5 = **7**",
        "P-020": "Numărul ereditar **7** aduce o memorie de neam legată de studiu, observație, discreție și căutarea adevărului. Păstrează profunzimea, dar nu transforma prudența moștenită în izolare.",
        "C-005": "> [!example] Calcul în intervalul 1–22\n> Roman = 25 → 25 − 22 = **3**",
        "T-013": """<table class="tarot-profile-table"><tbody><tr><td>Index: RAM-19980112-v1.00r-G-003<br>![Arcana 3 — Împărăteasa](tarot-03-imparateasa-vibratia-interioara.jpg)<div class="tarot-image-caption"><em>Arcana <strong>3</strong> — Împărăteasa</em></div></td><td><ul><li><strong>Resursă moștenită:</strong> creativitate, grijă și puterea de a face lucrurile să crească.</li><li><strong>Manifestare:</strong> creezi spații fertile pentru oameni și proiecte.</li><li><strong>Umbră:</strong> comoditate, risipire sau nevoie de validare.</li><li><strong>Maturizare:</strong> transformi grija și frumusețea în rezultate durabile.</li></ul></td></tr></tbody></table>""",
        "P-022c": "Numărul ereditar karmic **3**, asociat Împărătesei, vorbește despre o moștenire de creativitate, fertilitate simbolică și capacitatea de a hrăni oameni, idei sau comunități. Ești susținută când creezi, îngrijești și dai formă frumosului fără să uiți scopul practic.",
        "P-022d": "Umbra este să confunzi grija cu supraprotecția ori abundența cu risipa. Maturizarea apare când lași fiecare proiect și fiecare om să crească în ritmul propriu, iar tu păstrezi limite, măsură și continuitate.",
        "C-010": "> [!example] Calcul\n> Consoanele = 49 → 4 + 9 = 13 → 1 + 3 = **4**",
        "P-022": "Numărul de realizare **4** te face vizibilă ca persoană organizată, serioasă și capabilă să construiască. El poate amplifica rezultatele prin disciplină și consecvență. Umbra este rigiditatea, controlul și teama de schimbare; lasă structura să susțină viața, nu să o blocheze.",
        "P-022a": "Vibrația exterioară **1** și Numărul de realizare **4** formează o combinație practică: **1** pornește, iar **4** construiește. Oamenii pot vedea în tine inițiativă și stabilitate. Ai grijă ca hotărârea să nu devină inflexibilitate; cere feedback înainte să fixezi definitiv forma.",
        "C-012": "> [!example] Calcul\n> Roman = 25 → **7**  \n> Andreea = 30 → **3**  \n> Maria = 24 → **6**  \n> Numărul de exprimare = 7 + 3 + 6 = 16 → 1 + 6 = **7**",
        "P-024": "Numărul de exprimare **7** te susține în activități care cer cercetare, analiză, specializare, consiliere, educație sau înțelegerea mecanismelor ascunse. Ai nevoie de autonomie intelectuală și de timp pentru aprofundare. Lumea poate aștepta de la tine concluzii bine gândite, nu reacții grăbite.",
        "P-024a": "Armonizarea dintre Numărul de exprimare **7** și Destinul **4** cere să transformi cunoașterea în metodă. **7** investighează și caută adevărul; **4** organizează și construiește. Când lucrează împreună, poți crea sisteme solide, cursuri, proceduri sau proiecte în care profunzimea devine utilă. Evită izolarea lui **7** și rigiditatea lui **4** prin colaborări bine alese și termene clare.",
        "C-011": "> [!example] Calcul\n> Roman = R9 + O6 + M4 + A1 + N5 → **96415**\n>\n> Andreea = A1 + N5 + D4 + R9 + E5 + E5 + A1 → **1549551**\n>\n> Maria = M4 + A1 + R9 + I9 + A1 → **41991**\n>\n> Codul literelor numelui = **96415154955141991**\n> Codul numerologic personal al numelui = 96415154955141991 + 7 = **964151549551419917**",
        "G-002a": name_matrix_table(matrix["casute"], name["matricea_numelui"]["casute"]),
        "P-023": "Comparând pătratul datei cu pătratul numelui, energiile comune sunt **1**, **4** și **9**. Numele confirmă inițiativa, capacitatea de organizare și forța mentală; aici identitatea exprimată și structura nativă se susțin reciproc.",
        "P-023b": "Prin **1**, numele îți amplifică voința și originalitatea. Prin **4**, îți întărește imaginea de om practic și organizat. Prin **9**, adaugă memorie, viziune și capacitate de transformare. Aceste energii pot deveni repere constante dacă sunt folosite cu măsură.",
        "P-023c": "Energiile **5**, **6** și **7** apar numai în matricea numelui. Numele îți poate da impresia că libertatea și curajul lui **5**, pragmatismul și grija lui **6**, respectiv introspecția lui **7** îți sunt complet naturale. În matricea datei ele sunt conservate, deci au nevoie de experiență, rutină și sprijin exterior ca să devină resurse constante.",
        "P-023d": "Energiile **2**, **3** și **8** sunt prezente în data ta, dar nu în matricea numelui. Sensibilitatea, comunicarea spontană și responsabilitatea există nativ, însă nu sunt întotdeauna susținute de imaginea pe care o proiectează numele. Spune clar ce simți și ce îți asumi, ca oamenii să poată vedea și aceste părți ale tale.",
        "P-182": "Codul Spiritului se citește din ziua și luna nașterii și arată zona mare de maturizare spirituală. Pentru tine, Andreea, el arată felul în care experiența se transformă în înțelepciune și serviciu.",
        "P-185": "În tabel, poziția ta este la ziua **12** și luna **I**, unde apare codul **41**.",
        "T-017": spirit_table_from_daniel(source),
        "P-186": "Andreea, codul **41** te așază în zona **Harurilor**. Spiritul tău învață prin intuiție, ghidare, cunoaștere rafinată și capacitatea de a pune experiența în slujba celorlalți. Harul nu înseamnă scutire de efort; devine valoros când îl disciplinezi, îl verifici și îl transformi într-un ajutor concret.",
        "P-192": "Subetapa ta este **2 — Interacțiunea**. Lecția este să înțelegi cine ești în raport cu ceilalți: ce oferi, ce primești, unde începe responsabilitatea ta și unde trebuie să îi lași celuilalt propriul drum. Harurile tale se maturizează în relație, prin ascultare și schimb real, nu prin izolare.",
        "C-003d": "> [!example] Calcul\n> Vârsta la naștere = (41 × 189) − 189 = 7.749 − 189 = **7.560 ani**\n>\n> Vârsta actuală = 7.560 + 28 = **7.588 ani**",
        "P-197": "Ghidarea practică este să nu păstrezi intuiția numai pentru tine. Notează ceea ce observi, verifică prin studiu și experiență, apoi oferă concluzia într-o formă folositoare. Codul **41** crește când harul se întâlnește cu responsabilitatea.",
        "P-009a": "În lectura numerologică, ziua de naștere arată o încărcătură karmică simbolică. Fiind născută în ziua de **12**, te afli în intervalul **10–19**, asociat unei karme împlinite spre **80%**. Ziua ta este reprezentată de Arcana **12 — Spânzuratul**.",
        "C-001a": "> [!example] Calcul\n> Ziua nașterii = **12**\n>\n> Arcana karmică = **12 — Spânzuratul**\n>\n> Intervalul 10–19 = karma împlinită **spre 80%**",
        "G-001a": "![Arcana 12 — Spânzuratul, karma din ziua de naștere](tarot-12-spanzuratul-karma-zilei.jpg)\n\n_Arcana **12** — Spânzuratul. Karma din ziua de naștere_",
        "P-009b": "Spânzuratul vorbește despre schimbarea perspectivei, răbdare și renunțarea la controlul inutil. Lecția nu este să rămâi blocată sau să te sacrifici fără limită, ci să înțelegi când o pauză te ajută să vezi altfel și când amânarea devine evitare. Integrată matur, această energie îți dă profunzime și capacitatea de a găsi sens într-o experiență dificilă.",
        "P-009b1": "Umbra karmei **12** poate fi așteptarea prea lungă, rolul de victimă sau tendința de a purta responsabilități care nu îți aparțin. Poți confunda răbdarea cu lipsa de decizie. Semnul practic este stagnarea repetată fără o înțelegere nouă.",
        "P-009b2": "Cheia este să folosești pauza pentru claritate, apoi să alegi. Indicația spre **80%** arată o temă avansată, nu încheiată: păstrează compasiunea, dar pune limite și transformă perspectiva nouă într-un pas concret.",
        "C-002b": "> [!example] Calcul\n> Luna nașterii = **1**\n>\n> Karma lunii = **karma față de frate sau soră**",
        "P-013d": "Luna **1** îți cere susținere, ocrotire și ajutor responsabil în raport cu un frate, o soră sau cu persoane trăite simbolic în acest rol. Lecția nu este să conduci viața celuilalt, ci să fii prezentă fără să îi iei autonomia. Ajutorul matur oferă sprijin, spune adevărul și păstrează limite.",
        "P-015a": "Karma din Calea Destinului păstrează suma compusă a tuturor cifrelor datei. Pentru tine citim amprenta **31**, nu doar Destinul **4**, deoarece **31** păstrează nuanța karmică a drumului.",
        "C-003a": "> [!example] Calcul\n> 1 + 2 + 0 + 1 + 1 + 9 + 9 + 8 = **31**\n>\n> Karma din Calea Destinului = **31**\n>\n> Intervalul 30–39 = categoria karmică **3**",
        "P-015b": "Andreea, Calea karmică **31** este asociată simbolic cu Arcana **9 — Eremitul**. Ea vorbește despre o lume interioară bogată, interes pentru carte, filozofie, sens și cunoaștere, dar și despre riscul autoizolării. **3** aduce expresia și forma, iar **1** păstrează distanța și independența; împreună pot crea un om care înțelege mult, dar care trebuie să aleagă conștient când iese din spațiul interior pentru a împărtăși ceea ce știe. Imaginea unei vieți anterioare de actor sau comediant cu relații instabile este o metaforă tradițională, nu un fapt verificabil; ea avertizează asupra folosirii farmecului fără responsabilitate. Direcția matură este să transformi singurătatea în studiu, nu în izolare, și cunoașterea în ghidare folositoare.",
        "G-001b": "![Arcana 9 — Eremitul. Karma din Calea Destinului 31](tarot-09-eremitul-karma-calea-destinului.jpg)\n\n_Arcana **9** — Eremitul. Karma din Calea Destinului **31**._",
        "P-015c": "Codul Spiritului **41**, zona Harurilor și subetapa **2 — Interacțiunea** arată că darurile tale se maturizează prin relație și serviciu. Vârsta simbolică de **7.588 de ani** susține aceeași zonă. Karmele **12**, **1** și **31** cer să unești perspectiva, ajutorul responsabil și profunzimea: să nu te sacrifici inutil, să nu conduci în locul celuilalt și să nu transformi introspecția în izolare.",
        "C-013": "> [!example] Calcul\n> Calea Destinului: **31**\n> Destin compus: **3 + 1 = 4**\n> Limita Pinaclului 1: 36 − **4** = **32**\n> Pinacluri: **0–32 ani** → **33–42 ani** → **43–52 ani** → **53 ani–sfârșit**",
        "T-003": "| Pinaclu | Interval | Oportunitate | Provocare | Interpretare |\n| --- | --- | ---: | ---: | --- |\n| 1 | 0–32 ani | 4 | 2 | Construcție și disciplină; lecția este cooperarea fără indecizie. |\n| 2 | 33–42 ani | 3 | 6 | Exprimare și relaționare; responsabilitatea afectivă cere măsură. |\n| 3 | 43–52 ani | 7 | 4 | Studiu și profunzime; structura trebuie păstrată fără rigiditate. |\n| 4 | 53+ ani | 1 | 8 | Inițiativă și autonomie; puterea și resursele cer responsabilitate. |",
        "P-024c": "**Pinaclul 1: până la 32 de ani**, Oportunitatea **4** îți cere să construiești: profesie, program, casă, corp și obiceiuri stabile. Provocarea **2** te învață cooperarea, răbdarea și decizia în relație. Nu trebuie să alegi între ordine și sensibilitate; construiește o formă în care oamenii pot lucra împreună.",
        "P-024d": "**Pinaclul 2: între 33 și 42 de ani**, Oportunitatea **3** deschide comunicarea, creativitatea și vizibilitatea. Provocarea **6** cere maturitate în familie, grijă și responsabilități. Exprimă-te, dar nu promite mai mult decât poți susține.",
        "P-024e": "**Pinaclul 3: între 43 și 52 de ani**, Oportunitatea **7** favorizează studiul, specializarea și înțelepciunea. Provocarea **4** cere ordine și continuitate. Cunoașterea devine puternică atunci când este organizată într-o metodă și aplicată.",
        "P-024f": "**Pinaclul 4: de la 53 de ani până la sfârșitul vieții**, Oportunitatea **1** aduce autonomie și inițiativă. Provocarea **8** cere folosirea echilibrată a puterii, banilor și autorității. Condu prin exemplu și păstrează responsabilitatea pentru consecințe.",
        "P-024g": "Andreea, la 28 de ani te afli în Pinaclul **1**, cu Oportunitatea **4** și Provocarea **2**. Perioada actuală cere să îți consolidezi baza: program, profesie, bani, corp și relații stabile. Rezultatele cresc când păstrezi disciplina, dar construiești prin dialog și cooperare, fără să lași sensibilitatea să amâne deciziile necesare.",
        "P-025": "Zona ta de confort are vibrația **4**: te simți bine când lucrurile au ordine, reguli clare și o formă stabilă. Îți priește să știi ce urmează, ce responsabilitate are fiecare și cum poate fi măsurat progresul. Confortul devine limitare doar când structura nu mai lasă loc schimbării.",
        "C-006": "> [!example] Sinteză\n> Soartă: **1201 × 1998 = 2399598**  \n> Destin: **1211 × 1998 = 2419578**",
        "P-025a": "Pe linia **Sorții**, traseul **2–3–9–9–5–9–8** vorbește despre cooperare (**2**), expresie (**3**), transformări și încheieri repetate (**9–9**), schimbare (**5**), o nouă maturizare (**9**) și putere responsabilă (**8**). Pe linia **Destinului**, traseul **2–4–1–9–5–7–8** adaugă structură (**4**), inițiativă (**1**), profunzime (**7**) și aceeași temă finală a responsabilității (**8**).",
        "P-025b": "La **28 de ani**, atât Soarta, cât și Destinul sunt la **2**. Este o perioadă relațională: ascultarea, parteneriatul, negocierea și capacitatea de a cere ajutor au mai multă greutate decât forțarea individuală a rezultatului.",
        "P-025c": "Valoarea **2** se află sub zonele tale de confort, ceea ce poate aduce nesiguranță ori senzația că ritmul depinde prea mult de ceilalți. Nu interpreta asta ca stagnare. Folosește perioada pentru acorduri clare, colaborări și reglarea relațiilor care susțin construcția ta.",
        "P-025d": "Oportunitatea **4** îți cere structură, iar Provocarea **2** cere cooperare. Sfatul este să transformi discuțiile în reguli simple: cine face, până când, cu ce resurse și cum verificați rezultatul. Așa, sensibilitatea nu rămâne ezitare, ci devine coordonare.",
        "P-026e": "Andreea, prima suprapunere importantă a fost în 2025, când schimbarea interioară a cerut și un răspuns concret din exterior. Următorul nod este 2034. În astfel de ani, observă simultan ce se maturizează în tine și ce situație din afară îți cere alegere și adaptare.",
        "P-028": "Andreea, șirul lecțiilor **2–3–9–7–6** se repetă de-a lungul vieții. Fiecare lecție devine temelie pentru următoarea: **2** dezvoltă cooperarea, **3** expresia, **9** transformarea, **7** profunzimea, iar **6** responsabilitatea afectivă. Fiecare revenire îți cere o formă mai matură a aceleiași teme.",
        "T-008": lesson_table([2, 3, 9, 7, 6]),
        "P-028a": "În **2026**, lecția ta este **9**: încheiere, transformare, selectarea lucrurilor care merită păstrate și eliberarea celor care și-au încheiat rolul. Ea se întâlnește cu vibrația anuală **5**, care aduce schimbare și mobilitate. Nu schimba doar ca să scapi de disconfort; închide conștient, extrage lecția și păstrează libertatea pentru o direcție mai potrivită.",
        "T-007": cycle9_table(),
        "P-027": "Andreea, în 2026 te afli în ciclul **4** al ritmului de 9 ani, în **Anul 2** al ciclului. Cadrul mare cere consolidare, iar poziția actuală cere parteneriate, comunicare și cooperare. Vibrația anuală **5** adaugă schimbare: păstrează fundația, dar actualizează metoda, oamenii și direcțiile care nu mai funcționează.",
        "P-027a": "În 2026 ești în Ciclul de 12 ani **3**, intervalul 2022–2033. Este o etapă de expansiune prin experiențe și responsabilități noi. Pentru tine, creșterea este folositoare când are forma Destinului **4**: plan, termen, resurse și continuitate.",
        "L-003": "- Nume: Bîrsan Daniel Robert\n- Prenume activ: Daniel\n- Data nașterii: 19.02.1998\n- Gen: masculin\n- Tipul relației: partener",
        "P-029": "Andreea, această hartă nu dă un verdict despre relație. Ea arată ce aduce fiecare, ce se întâlnește firesc și ce aveți de construit împreună.",
        "G-006": "![Omulețul relațiilor pentru Roman Andreea Maria și Bîrsan Daniel Robert](omulet-relatii-roman-andreea-maria-birsan-daniel-robert.png)\n\n_Omulețul relațiilor pentru Roman Andreea Maria și Bîrsan Daniel Robert_",
        "P-030": "În relația aceasta, Andreea, tu vii mai puternic pe zona lui **1**: inițiativă, identitate, pornire și decizie. Daniel vine cu mai multă forță pe **9**: sens, viziune și capacitatea de a privi lucrurile larg. Tu poți pune lucrurile în mișcare, iar el poate aduce perspectiva. Diferența devine motor când nu confundați viteza cu adevărul.",
        "P-030a": "Pe zona emoțională aveți amândoi câte un **2**. Sensibilitatea există, dar nu reglează automat totul. Nu aștepta ca Daniel să intuiască ce simți și nu presupune că ai înțeles complet retragerea lui. Întrebările simple — «Ce ai simțit?», «De ce ai nevoie?» — păstrează legătura vie.",
        "P-030b": "Pe Pământ aveți câte un **8**, deci puteți discuta practic despre responsabilități și rezultate. Rezultatul comun **4** cere construcție: reguli, stabilitate, buget, casă și gesturi repetate. Dacă dați structură Focului relațional, intensitatea încălzește și construiește; fără structură, consumă.",
        "P-030c": "Tema de rezolvat este **2**: răbdare, ascultare și loc pentru celălalt. Pentru tine, lecția este să nu pornești singură toate mișcările și să spui clar ce simți, nu doar ce trebuie făcut. Tu aduci direcția, Daniel aduce perspectiva; cooperarea apare când amândoi vă asumați un pas concret.",
        "P-046": "> [!example] Calcul aplicabilitate profesională\n> **NU / obstacole:** 1 + 2 + 0 + 1 + 1 + 9 + 9 + 8 = **31** → 31 − 22 = **9**\n> **DA / aplicabilitate profesională:** luna **1** + (1 + 9 + 9 + 8) = 1 + 27 = **28** → 28 − 22 = **6**",
        "T-016": """| Aplicabilitate profesională DA | Aplicabilitate profesională NU |
| --- | --- |
| ![Arcana 6 — Îndrăgostiții, aplicabilitate profesională](tarot-06-indragostitii-aplicabilitate-profesionala.jpg)<br>_Arcana 6 — Îndrăgostiții. Direcția profesională de cultivat_ | ![Arcana 9 — Eremitul, obstacole profesionale](tarot-09-eremitul-obstacole-profesionale.jpg)<br>_Arcana 9 — Eremitul. Obstacolul profesional de echilibrat_ |
| **Index: RAM-19980112-v1.00r-P-047**<br>Îndrăgostiții aduc talentul alegerii, al colaborării și al construirii unor alianțe bazate pe valori comune. Profesional, te susțin în consiliere, comunicare, negociere, educație, resurse umane, servicii pentru oameni, artă, frumusețe și proiecte în care trebuie armonizate interese diferite.<br><br>Resursa ta este să vezi relația dintre oameni și să creezi acord. Umbra este indecizia sau alegerea făcută numai pentru a păstra armonia. Succesul apare când formulezi criterii clare, alegi la timp și rămâi loială valorilor care au stat la baza deciziei. | **Index: RAM-19980112-v1.00r-P-048**<br>Eremitul ca obstacol nu arată lipsa competenței, ci riscul de a lucra prea mult singură, de a analiza până când oportunitatea trece sau de a aștepta certitudinea completă. Poți acumula cunoaștere valoroasă fără să o expui suficient.<br><br>Cheia este să păstrezi profunzimea, dar să creezi termene de ieșire în lume: publicare, prezentare, ofertă, cerere de feedback. Singurătatea devine atelier, nu ascunzătoare, iar experiența ta poate deveni reper pentru ceilalți. |""",
        "P-032": "Andreea, în carieră ești autentică atunci când creativitatea Vibrației interioare **3** primește inițiativa Vibrației exterioare **1**, iar Destinul **4** transformă ideea în sistem și rezultat. Numărul de exprimare **7** adaugă cercetare și specializare. Scara bunăstării confirmă un traseu puternic între Creativitate, Carieră și Bunăstare materială. Progresul vine când alegi o problemă reală, formulezi o soluție, îi dai termen și o duci până la o formă vandabilă sau folositoare.",
        "P-032a": "În intervalul actual, **12.01.2026–11.01.2027**, ești în Ciclul **4** de 9 ani, Anul **2**, cu vibrația anuală **5** și Lecția **9**. Ciclul de 7 ani **5** începe, Ciclul de 12 ani **3** susține expansiunea, iar Pinaclul **1** aduce Oportunitatea **4** și Provocarea **2**. Soarta și Destinul sunt la **2 / 2**, sub zona de confort. Este o fereastră de schimbare negociată: închide ce nu produce valoare, alege colaboratorii potriviți și construiește o formă mai flexibilă pentru munca ta.",
        "T-020": "| Fereastră | Suprapunerea principală | Utilizare profesională |\n| --- | --- | --- |\n| **12.01.2026–11.01.2027** | Ciclul de 9 ani C4, Anul **2**; vibrația **5**; Lecția **9**; Pinaclul **1**, Oportunitatea **4**, Provocarea **2**; Soartă–Destin **2 / 2** | Închidere, reorganizare, colaborări și testarea unei direcții noi. |\n| **12.01.2029–11.01.2030** | Vibrația **8**; Lecția **3**; Soartă–Destin **9 / 9**; Pinaclul **1** | Fereastră puternică pentru bani, vizibilitate, negociere și monetizarea creativității. |\n| **12.01.2032–11.01.2033** | Anul **8** al ciclului; vibrația **2**; Lecția **6**; Soartă–Destin **8 / 8**; Pinaclul **2**, Oportunitatea **3**, Provocarea **6** | Parteneriat profitabil, consolidare și extinderea unei activități deja validate. |\n| **12.01.2034–11.01.2035** | An important interior și exterior; începe Ciclul de 12 ani **4**; Pinaclul **2** | Repoziționare majoră și construirea unei structuri profesionale mai ample. |",
        "P-032b": "Primul prag dens este 2029: vibrația **8** și Soartă–Destin **9 / 9** pot susține vizibilitatea și rezultatul material, dacă ai închis proiectele fără valoare. În 2034 se schimbă cadrul larg și apare un an important interior și exterior. Pregătirea este simplă: portofoliu clar, buget, competență aprofundată și un sistem prin care ideile pot fi repetate fără să depindă numai de entuziasm.",
        "SUB-031": "### 11.3. Iubire și relația cu Daniel",
        "P-033": "În iubire, autenticitatea ta apare când expresivitatea lui **3** nu este ascunsă în spatele imaginii hotărâte a lui **1**. Puntea **2** îți cere să spui ce simți, să asculți și să nu iei singură toate deciziile. Inițiativa ta este valoroasă, dar relația are nevoie ca Daniel să aibă un loc real în alegere.",
        "P-033a": "Cu Daniel, rezultatul comun **4** cere construcție, iar tema **2** cere cooperare. Tu aduci pornirea lui **1**, el perspectiva lui **9**. Relația crește când inițiativa ta primește sens, iar analiza lui primește mișcare. Bugetul, programul, casa și responsabilitățile trebuie discutate înainte să devină surse de tensiune.",
        "P-033b": "Perioada **12.01.2026–11.01.2027** este relațională prin Anul **2** și Soartă–Destin **2 / 2**, dar vibrația **5** și Lecția **9** cer schimbare și încheierea tiparelor vechi. Este potrivită pentru clarificare, nu pentru promisiuni făcute din teamă. Discutați ce păstrați, ce schimbați și ce construiți concret.",
        "T-021": "| Fereastră | Suprapunerea principală | Sens relațional |\n| --- | --- | --- |\n| **12.01.2026–11.01.2027** | Anul **2**; vibrația **5**; Lecția **9**; Soartă–Destin **2 / 2** | Clarificare, schimbarea tiparelor și acorduri concrete. |\n| **12.01.2027–11.01.2028** | Vibrația **6**; Lecția **6**; Pinaclul **1**, Oportunitatea **4**, Provocarea **2** | Fereastră apropiată pentru familie, cămin și asumare, dacă relația este stabilă. |\n| **12.01.2032–11.01.2033** | Vibrația **2**; Lecția **6**; Soartă–Destin **8 / 8**; Pinaclul **2**, Oportunitatea **3**, Provocarea **6** | Parteneriat matur, oficializare și construcție comună cu responsabilitate financiară. |\n| **12.01.2036–11.01.2037** | Vibrația **6**; Soartă–Destin **9 / 9**; Pinaclul **2** | Fereastră de maturizare afectivă, familie și închiderea unor vechi tensiuni. |",
        "P-033c": "O dată pe săptămână, vorbiți fără telefoane despre starea relației; lunar, verificați bugetul și un obiectiv comun. Când apare tensiunea, spune mai întâi ce ai simțit, apoi ce propui. Formula ta matură nu este «pornesc singură și văd dacă vii», ci «spun limpede ce îmi doresc, te ascult și alegem o construcție pe care o putem susține amândoi».",
        "P-034": "Ferestrele nu promit bani, carieră sau căsătorie. Ele arată suprapuneri simbolice care pot susține o direcție. Când Vibrația interioară **3** exprimă, Vibrația exterioară **1** inițiază, iar Destinul **4** construiește, harta devine un instrument de alegere conștientă, nu un substitut pentru realitate.",
        "T-014": "| Resursă | Valoare |\n| --- | --- |\n| Agent coordonator | The Scribe |\n| Grafică | The Cartographer — SVG-uri validate |\n| Skill-uri | `numerologie-lucrare-redactare`; skill-urile SVG dedicate |\n| Template | `scurt` — `Template_Lucrare_Numerologica_Scurt.md` + `.html` |\n| Raport calculator | `1998-01-12-ROMAN-ANDREEA-MARIA-scurt-v1.00r-calculator.json` |\n| SVG-uri integrate | Matrice, Scara bunăstării, Soarta–Destin, Omulețul relațiilor și Harta suprapusă |\n| Versiune și data redactării | V1.00R — 31.07.2026 |",
    }

    # Elementele sunt calculate din cantitățile căsuțelor, nu din valorile lor.
    element_counts = {"Foc": 9, "Pământ": 2, "Aer": 1, "Apă": 2}
    element_section = """<div class="element-analysis framed-panel"><div class="element-indexes"><span>Index: RAM-19980112-v1.00r-T-012</span><span>Index: RAM-19980112-v1.00r-P-044</span></div><div class="element-chart"><div class="element-bars" role="img" aria-label="Distribuția elementelor: Foc 9, Pământ 2, Aer 1, Apă 2">""" + "".join(
        f'<div class="element-bar"><div class="element-bar-label"><span>{label}</span><strong>{value}</strong></div><div class="element-bar-track"><span class="element-bar-fill element-{css}" style="width:{round(value / 9 * 100, 2)}%"></span></div></div>'
        for label, css, value in [("Foc", "foc", 9), ("Pământ", "pamant", 2), ("Aer", "aer", 1), ("Apă", "apa", 2)]
    ) + """</div></div><ul class="element-definitions"><li><strong>Focul</strong> este esența vieții, a duhului și a spiritului care animă și activează.</li><li><strong>Pământul</strong> hrănește și dă formă.</li><li><strong>Aerul</strong> eliberează și stimulează inteligența conceptuală.</li><li><strong>Apa</strong> susține emoțiile, flexibilitatea și acumularea.</li></ul></div>\n\nIndex: RAM-19980112-v1.00r-P-045\nTemperamentul tău predominant este **coleric**: Focul are **9** apariții, față de Pământ cu **2**, Apă cu **2** și Aer cu **1**. Reacționezi repede și ai multă energie de pornire. Echilibrul vine când dai Focului un scop, iar corpul, emoțiile și reflecția primesc timp egal în program."""

    for suffix, body in blocks.items():
        text = replace_block(text, suffix, body)

    text, element_count = re.subn(
        r'<div class="element-analysis framed-panel">.*?(?=\nIndex: RAM-19980112-v1\.00r-SUB-016)',
        element_section + "\n\n",
        text,
        count=1,
        flags=re.S,
    )
    if element_count != 1:
        raise RuntimeError(f"Secțiunea elementelor nu a fost înlocuită: {element_count}")

    # Relația și graficele trebuie privite din perspectiva Andreei.
    text = text.replace("### 11.3. Iubire și relația cu Andreea", "### 11.3. Iubire și relația cu Daniel")
    text = text.replace("![Grafic Soarta și Destin pentru Roman Andreea Maria]", "![Grafic Soarta și Destin pentru Roman Andreea Maria]")
    text = text.replace("tarot-01-magicianul-vibratia-interioara.jpg", "tarot-03-imparateasa-vibratia-interioara.jpg")
    text = text.replace("tarot-05-marele-preot-numarul-neamului.jpg", "tarot-03-imparateasa-vibratia-interioara.jpg")
    text = text.replace("tarot-19-soarele-karma-zilei.jpg", "tarot-12-spanzuratul-karma-zilei.jpg")
    text = text.replace("tarot-17-steaua-obstacole-profesionale.jpg", "tarot-09-eremitul-obstacole-profesionale.jpg")
    text = text.replace("tarot-07-carul-aplicabilitate-profesionala.jpg", "tarot-06-indragostitii-aplicabilitate-profesionala.jpg")
    text = text.replace("parteneră", "partener")
    text = text.replace("născut în luna", "născută în luna")
    text = text.replace("ești autentic atunci", "ești autentică atunci")
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print(OUT)


if __name__ == "__main__":
    main()

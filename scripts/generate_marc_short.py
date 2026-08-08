from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "output/lucrari/2025-07-14-VULCU-MARC-IOAN"
OUT = OUT_DIR / "2025-07-14-VULCU-MARC-IOAN-scurt-v1.00r.md"
REPORT = OUT_DIR / "2025-07-14-VULCU-MARC-IOAN-scurt-v1.00r-calculator.json"
CALCULATOR = ROOT / "skills/numerologie-lucrare-redactare/scripts/calculator_numerologic_examen.py"
HELPERS = ROOT / "scripts/generate_rebeca_short.py"
PREFIX = "VMI-20250714-v1.00r"


def load_helpers():
    spec = importlib.util.spec_from_file_location("atlas_short_helpers", HELPERS)
    if not spec or not spec.loader:
        raise RuntimeError("Nu pot încărca funcțiile template-ului scurt.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_report() -> dict:
    result = subprocess.run(
        [
            sys.executable, str(CALCULATOR),
            "--data-nasterii", "14.07.2025",
            "--nume-complet", "Vulcu Marc Ioan",
            "--nume-familie", "Vulcu",
            "--prenume", "Marc Ioan",
            "--prenume-activ", "Marc",
            "--gen", "masculin",
            "--an-start", "2025",
            "--an-final", "2133",
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


def cycle12_table(start_year: int = 2025) -> str:
    readings = [
        "Formarea siguranței, a limbajului emoțional și a primelor repere de familie.",
        "Explorare, autonomie treptată și descoperirea intereselor proprii.",
        "Extindere prin studiu, relații, experiențe și responsabilități asumate.",
        "Consolidarea unei forme de viață stabile: profesie, familie și statut.",
        "Recalibrarea sensului și valorificarea matură a experienței acumulate.",
        "Transmitere, mentorat și influență exercitată cu discernământ.",
        "Sinteză, simplificare și întoarcere la ceea ce este esențial.",
        "Administrarea responsabilă a resurselor și a moștenirii personale.",
        "Integrarea etapelor parcurse și închiderea lucidă a ciclurilor lungi.",
    ]
    lines = ["| Ciclu | Interval calendaristic | Vârste | Citire |", "| --- | --- | ---: | --- |"]
    for i, reading in enumerate(readings, start=1):
        start_age = (i - 1) * 12
        end_age = start_age + 11
        sy, ey = start_year + start_age, start_year + end_age
        if i == 1:
            mark = '<span class="active-cycle-cell" style="color: #b3261e; font-weight: 700;">'
            lines.append(f"| {mark}**Ciclul 1 — activ**</span> | {mark}**{sy}–{ey}**</span> | {mark}**0–11**</span> | {mark}{reading}</span> |")
        else:
            lines.append(f"| Ciclul {i} | {sy}–{ey} | {start_age}–{end_age} | {reading} |")
    return "\n".join(lines)


def idx(suffix: str) -> str:
    return f"Index: {PREFIX}-{suffix}\n"


def canonical_document(
    date_component: str,
    name_component: str,
    wellbeing: str,
    spirit_code: str,
    spirit_stage: str,
    lesson_table: str,
    cycle9: str,
) -> str:
    important_interior = "2034 → 2043 → 2052 → 2061 → 2070 → 2079 → 2088 → 2097 → 2106 → 2115 → 2124 → 2133"
    important_exterior = "2034 → 2043 → 2052 → 2061 → 2070 → 2079 → 2097 → 2115 → 2124 → 2133"
    return f'''---
titlu: Lucrare numerologică scurtă — Vulcu Marc Ioan
tip: lucrare-numerologica
template: scurt
status: revizie
versiune: V1.00R
persoana: Vulcu Marc Ioan
data_nasterii: 2025-07-14
agent: The Scribe
tags: [numerologie, lucrare, scurt, revizie]
---

{idx("CAP-001")}
# Vulcu Marc Ioan — 14.07.2025

{idx("CAP-002")}
## Date generale

{idx("L-001")}
- Persoana analizată: Vulcu Marc Ioan
- Prenume activ: Marc
- Data nașterii: 14.07.2025
- Ora nașterii: 14:26
- Gen: masculin
- Nume anterior: nu există
- Relație analizată: Vulcu Rebeca Andreea, soră, născută la 15.03.2020
- Template selectat: scurt
- Stil de redactare: conversațional
- Interval analizat: 0–108 ani
- Data lucrării: 08.08.2026
- Versiune: V1.00R

{idx("CAP-003")}
## Cuprins

{idx("L-002")}
1. Vibrația interioară — Cine ești tu?
2. Vibrația exterioară — Rolul social
3. Destinul — Muntele de urcat
4. Matrița numerologică — Pătratul lui Pitagora
5. Numele — Eu și neamul
6. Spirit și karmă — Lecții și direcții de maturizare
7. Pinacluri: Oportunități și provocări
8. Ciclicități
9. Relații
10. Aplicabilitate profesională
11. Concluzii

{idx("CAP-005")}
## Capitolul 1. Vibrația interioară — Cine ești tu?

{idx("SUB-001")}
### 1.1. Definiție

{idx("P-001")}
Marc, vibrația interioară vorbește despre desăvârșirea caracterului și descrie natura ta lăuntrică: cine ești când nu te vede nimeni și nu trebuie să răspunzi așteptărilor din exterior. Ea arată cum primești și interpretezi ceea ce vine către tine, ce îți dorești cu adevărat, ce simți și cum înveți. De aici pornesc motivațiile și reacțiile tale autentice. Cunoscând această vibrație, îți poți recunoaște mai ușor punctele forte, slăbiciunile și direcțiile în care ai nevoie să te dezvolți.

{idx("C-001")}
> [!example] Calcul
> Ziua din data de naștere = **14** → 1 + 4 = **5**

{idx("SUB-002")}
### 1.2. Caracterul

{idx("P-002")}
Caracterul **5** este curios, mobil și receptiv la noutate. Arhetipal, te apropii de Explorator: observi repede ce se schimbă și înveți când ai voie să încerci. Maturizarea apare când libertatea are un cadru suficient de clar încât experiența să poată fi dusă până la capăt.

{idx("SUB-003")}
### 1.3. Dorințele

{idx("P-003")}
Îți dorești varietate, mișcare și spațiu pentru descoperire. Te hrănesc jocurile care au mai multe soluții, poveștile, deplasarea și posibilitatea de a alege între două variante potrivite vârstei tale.

{idx("SUB-004")}
### 1.4. Motivația

{idx("P-004")}
Te motivează noutatea și rezultatul vizibil. O rutină utilă este să alegi o activitate scurtă, să o termini și abia apoi să treci la următoarea; astfel, curiozitatea nu se transformă în risipire.

{idx("SUB-005")}
### 1.5. Teama

{idx("P-005")}
Umbra lui **5** este senzația că regula sau repetarea îți ia libertatea. Când devii neliniștit, ai nevoie de limite explicate simplu și de o alternativă acceptabilă, nu de multe opțiuni care te pot copleși.

{idx("SUB-006")}
### 1.6. Polarități și maturizare

{idx("T-009")}
|  |  |
| --- | --- |
| **Polarități pozitive** | curiozitate; adaptare; curaj de a încerca; mobilitate; învățare prin experiență |
| **Polarități negative** | nerăbdare; schimbarea rapidă a direcției; refuzul rutinei; suprastimulare |
| **Direcții de dezvoltare** | libertate cu limite; activități încheiate; alternanță între mișcare și repaus; alegeri puține și clare |

{idx("CAP-006")}
## Capitolul 2. Vibrația exterioară — Rolul social

{idx("SUB-008")}
### 2.1. Definiție

{idx("P-006")}
Vibrația exterioară descrie felul în care te manifești în lume: prezența, comportamentul vizibil, imaginea socială și modul în care ceilalți îți pot percepe energia. Dacă vibrația interioară arată dinamica ta privată, vibrația exterioară arată forma prin care aceasta devine vizibilă în relații, contexte sociale și situații concrete. Ea nu spune totul despre caracter, dar indică stilul tău de apariție, reacția spontană în exterior și felul în care îți proiectezi energia. Citește-o ca pe o poartă de contact cu lumea: poate confirma vibrația interioară sau poate crea un contrast între ceea ce trăiești înăuntru și ceea ce observă ceilalți.

{idx("C-002")}
> [!example] Calcul
> Luna din data de naștere = **7**

{idx("SUB-009")}
### 2.2. Rolul social

{idx("P-007")}
Arhetipal, rolul social **7** seamănă cu Observatorul: înainte să participi, poți privi, asculta și verifica dacă mediul este sigur. Resursa este profunzimea; umbra este retragerea atunci când ritmul exterior devine prea intens.

{idx("SUB-010")}
### 2.3. Interior și exterior

{idx("P-008")}
Marc, dacă în interior ești **5**, la exterior oamenii te pot percepe ca pe un **7**. Înăuntru vrei mișcare și varietate, iar în afară poți părea mai prudent. Cele două energii se armonizează când ai timp să observi înainte de a explora.

{idx("P-009")}
Puntea interior–exterior arată ajustarea dintre nucleul tău mobil și imaginea mai rezervată pe care o văd ceilalți.

{idx("C-003")}
> [!example] Calculul punții interior–exterior
> |**5** − **7**| = **2**

{idx("P-010")}
Puntea **2** cere cooperare, răbdare și autenticitate emoțională. Când poți spune sau arăta ce ai nevoie, comportamentul tău devine coerent cu intenția, iar oamenii te pot primi fără ezitare în rolul pe care îl asumi.

{idx("CAP-007")}
## Capitolul 3. Destinul — Muntele de urcat

{idx("SUB-011")}
### 3.1. Definiție și calcul

{idx("P-011")}
Destinul sintetizează data completă și arată o direcție de maturizare, nu un eveniment obligatoriu. Pentru destin păstrăm accentul pe rezultatul final.

{idx("C-004")}
> [!example] Calcul
> Toate cifrele adunate din data de naștere = 1 + 4 + 0 + 7 + 2 + 0 + 2 + 5 = **21**  
> Destin compus: 2 + 1 = **3**  
> Cifra de interpretare = **3**

{idx("SUB-012")}
### 3.2. Interpretare

{idx("P-012")}
Muntele tău de urcat este exprimarea: să transformi experiența lui **5** și observația lui **7** în cuvânt, imagine, joc sau proiect. Destinul **3** se maturizează prin claritate și continuitate, nu prin cantitatea ideilor începute.

{idx("CAP-008")}
## Capitolul 4. Matrița numerologică — Pătratul lui Pitagora

{idx("SUB-013")}
### 4.1. Matricea datei de naștere

{idx("P-013")}
Cele nouă căsuțe se citesc din data compactă și din numerele de lucru și descriu nouă forme de inteligență:

- **1** — inteligența psihică;
- **2** — inteligența emoțională;
- **3** — prelucrarea informațiilor;
- **4** — inteligența corporală;
- **5** — inteligența intuitivă;
- **6** — pragmatismul;
- **7** — inteligența spirituală;
- **8** — puterea și inteligența socială;
- **9** — inteligența mentală.

{idx("C-005")}
> [!example] Calcul
> Data compactă = **14072025**  
> N1 = **21**; N2 = **3**; N3 = **19**; N4 = **10**  
> Șir complet = **140720252131910**

{idx("G-002")}
{date_component}

{idx("P-014")}
**Căsuța 1.** Reprezintă psihicul, inițiativa, voința și capacitatea de a susține o direcție. Ai **4** apariții în căsuța cifrei **1**, ceea ce indică o forță psihică intensă și un potențial natural de leadership. Poți porni repede, poți rămâne ferm când apare presiunea și îi poți ajuta pe ceilalți să vadă ce urmează. Umbra acestei intensități apare când fermitatea devine încăpățânare, când vrei ca lucrurile să se facă numai în ritmul tău sau când ocupi tot spațiul deciziei. Maturizarea înseamnă să îți păstrezi inițiativa, dar să asculți până la capăt, să împarți responsabilitatea și să folosești autoritatea pentru a mobiliza, nu pentru a controla.

{idx("P-015")}
**Căsuța 2.** Reprezintă emoțiile, comunicarea, sensibilitatea, colaborarea și felul în care energia circulă între tine și ceilalți. Ai **3** apariții în căsuța cifrei **2**, astfel încât registrul emoțional este activ și receptiv: poți simți repede atmosfera și poți răspunde firesc nevoii de apropiere. Această sensibilitate te ajută în cooperare, dar poate amplifica reacțiile atunci când mediul este agitat sau când nu găsești cuvintele potrivite pentru ceea ce simți. Umbra poate apărea ca suprasolicitare emoțională, nerăbdare în dialog ori tendința de a prelua starea celuilalt. Te echilibrează un limbaj simplu al emoțiilor, pauzele de reglare, limitele blânde și relațiile în care poți spune clar ce simți și ce ai nevoie.

{idx("P-016")}
**Căsuța 3.** Reprezintă relaționarea, curiozitatea și capacitatea de a primi, organiza și transmite informația. Ai **1** apariție în căsuța cifrei **3**, ceea ce îți oferă acces direct la această energie, dar cere folosire conștientă pentru a deveni stabilă. Poți înțelege prin poveste, joc, imagine și dialog, mai ales când informația are un fir clar și un scop concret. Umbra poate fi graba de a trece la altă idee înainte ca prima să fie înțeleasă sau dificultatea de a explica ceea ce ai intuit deja. Te ajută să repeți cu propriile cuvinte, să pui întrebări, să alegi informația esențială și să duci o idee până la o concluzie înainte de a deschide alta.

{idx("P-017")}
**Căsuța 4.** Reprezintă corpul, sănătatea în lectura simbolică a matricei, organizarea, spiritul practic și orientarea către rezultate concrete. Ai **1** apariție în căsuța cifrei **4**, ceea ce arată că poți construi ordine și stabilitate atunci când ai un cadru clar. Îți priesc activitățile în care vezi progresul, lucrezi cu mâinile sau transformi o idee într-un rezultat observabil. Umbra apare când rutina este abandonată prea repede, iar energia intensă a inițiativei te face să sari peste pașii mici. Maturizarea acestei căsuțe se sprijină pe somn, mișcare, alimentație echilibrată, sarcini simple și obiceiuri repetate, fără a transforma disciplina într-o formă rigidă.

{idx("P-018")}
**Căsuța 5.** Reprezintă libertatea, stima de sine, curajul, adaptarea, nonconformismul și capacitatea de a ieși din tipare. Ai **1** apariție în căsuța cifrei **5**, ceea ce îți oferă impulsul de a explora și de a încerca o cale proprie. Resursa este flexibilitatea: poți descoperi soluții noi atunci când ai voie să experimentezi și să înveți direct din consecințe. Umbra poate fi confundarea libertății cu lipsa limitelor, schimbarea direcției din impuls sau căutarea permanentă a stimulului nou. Energia se maturizează când alegi singur între câteva opțiuni clare, îți asumi rezultatul și revii la un punct stabil după fiecare explorare.

{idx("P-019")}
**Căsuța 6.** Reprezintă iubirea ca ocrotire, instinctele, arta, realismul și pragmatismul. Nu ai nicio apariție în căsuța cifrei **6**, de aceea această energie este conservată: nu este disponibilă constant la cerere și se poate manifesta alternativ, foarte intens într-un context și foarte puțin în altul. Poți avea nevoie de exemple concrete pentru a transforma afecțiunea în grijă practică, inspirația în lucru terminat și dorința într-o alegere realistă. Aportul extern vine prin familie, educatori, activități artistice, sarcini potrivite vârstei și contexte în care vezi legătura dintre efort și rezultat. Construiești conștient această energie prin responsabilități mici, rutine repetabile, participare la viața familiei și învățarea diferenței dintre a ocroti și a prelua totul asupra ta.

{idx("P-020")}
**Căsuța 7.** Reprezintă observația, analiza, studiul, experimentarea și capacitatea de a lega cunoașterea concretă de sens. Ai **1** apariție în căsuța cifrei **7**, ceea ce îți oferă o energie activă de cercetător: poți vedea detalii, poți urmări cum funcționează lucrurile și poți învăța din încercare. Resursa este discernământul care se formează atunci când ai timp să observi înainte de a trage concluzia. Umbra poate fi retragerea excesivă, neîncrederea sau păstrarea întrebărilor numai pentru tine. Te ajută momentele de liniște urmate de dialog, experimentele practice, lectura și încurajarea de a explica ce ai descoperit, nu doar de a păstra concluzia în interior.

{idx("P-021")}
**Căsuța 8.** Reprezintă puterea, responsabilitatea, ambiția, performanța și capacitatea de a administra resurse ori roluri sociale. Nu ai nicio apariție în căsuța cifrei **8**, astfel încât această energie este conservată și are nevoie de contexte potrivite pentru a fi activată. Poți oscila între evitarea responsabilității și asumarea prea intensă atunci când vrei să dovedești că poți. Aportul extern sănătos vine prin adulți echitabili, reguli explicate, sarcini cu început și final și feedback care separă valoarea ta de rezultat. Maturizarea se construiește treptat: îți asumi partea ta, înveți să ceri ajutor, administrezi resurse mici și descoperi că puterea reală înseamnă consecvență și responsabilitate, nu presiune sau control.

{idx("P-022")}
**Căsuța 9.** Reprezintă inteligența mentală, memoria, compasiunea, învățarea, finalizarea și capacitatea de transformare. Ai **1** apariție în căsuța cifrei **9**, ceea ce îți oferă acces la înțelegerea de ansamblu și la legarea experiențelor într-o concluzie. Poți învăța bine atunci când informația are sens, este asociată unei povești și poate fi folosită într-o situație reală. Umbra apare când imaginea mare te face să treci prea repede peste detalii sau când o concluzie intuită nu este verificată. Îți dezvolți această energie prin lectură, conversație, recapitulare, proiecte duse până la capăt și exercițiul de a spune nu doar ce ai înțeles, ci și pe ce observații se bazează.

{idx("SUB-015")}
### 4.3. Elemente și temperament

{idx("T-012")}
<div class="element-analysis framed-panel"><div class="element-chart"><div class="element-bars"><div class="element-bar"><div class="element-bar-label"><span>Foc</span><strong>6</strong></div><div class="element-bar-track"><span class="element-bar-fill element-foc" style="width:100%"></span></div></div><div class="element-bar"><div class="element-bar-label"><span>Pământ</span><strong>1</strong></div><div class="element-bar-track"><span class="element-bar-fill element-pamant" style="width:16.67%"></span></div></div><div class="element-bar"><div class="element-bar-label"><span>Aer</span><strong>2</strong></div><div class="element-bar-track"><span class="element-bar-fill element-aer" style="width:33.33%"></span></div></div><div class="element-bar"><div class="element-bar-label"><span>Apă</span><strong>3</strong></div><div class="element-bar-track"><span class="element-bar-fill element-apa" style="width:50%"></span></div></div></div></div></div>

{idx("P-023")}
Temperamentul este predominant **coleric**: Focul **6** pornește repede, Apa **3** adaugă sensibilitate, Aerul **2** susține ideea, iar Pământul **1** cere ancorare prin corp și rutină.

{idx("SUB-016")}
### 4.4. Masculin și feminin

{idx("P-024")}
Raportul este de **8 cifre impare** la **4 cifre pare**. Energia de inițiativă este dominantă; capacitatea de a primi și de a da mai departe există, dar trebuie susținută prin cooperare și pauze de reglare.

{idx("SUB-017")}
### 4.5. Daruri și nevoi

{idx("P-025")}
Vectorii plini sunt **123 — Energie**, **147 — Spiritualitate**, **159 — Carieră** și **357 — Scopuri**. Fixația **147** cere flexibilitate în convingeri, iar tendința **159** cere ca ambiția să fie legată de un scop folositor.

{idx("SUB-018")}
### 4.6. Scara bunăstării

{idx("P-026")}
Treapta dominantă este **159 — Carieră (18)**, urmată de **789 — Creativitate (16)** și de **147 — Spiritualitate** împreună cu **357 — Scopuri (15)**. Lanțul devine stabil când energia primește structură și finalizare.

{idx("G-004")}
{wellbeing}

{idx("CAP-009")}
## Capitolul 5. Numele — Eu și neamul

{idx("SUB-019")}
### 5.1. Numărul activ

{idx("P-026a")}
Numărul activ descrie influența prenumelui folosit zi de zi asupra comportamentului curent. El arată energia cu care Marc intră spontan într-un context, felul în care reacționează și impresia pe care o susține prin acțiunile sale obișnuite.

{idx("C-006")}
> [!example] Calcul
> Marc = 4 + 1 + 9 + 3 = **17** → **8**

{idx("P-027")}
Numărul activ **8** aduce hotărâre, simț al rezultatului și dorința de a stăpâni o sarcină. Maturizarea cere folosirea puterii fără rigiditate.

{idx("SUB-020")}
### 5.2. Numărul intim

{idx("P-027a")}
Numărul intim se calculează din vocalele numelui complet și descrie motivația afectivă, dorințele profunde și ceea ce îi hrănește lumea interioară. Dacă Numărul activ arată energia vizibilă a reacției, Numărul intim arată nevoia discretă care îi dă sens alegerilor.

{idx("C-007")}
> [!example] Calcul
> Vocalele numelui = **23** → **5**

{idx("P-028")}
Numărul intim **5** caută libertate, experiență și varietate. Te hrănește explorarea, dar siguranța apare când știi unde te întorci.

{idx("SUB-021")}
### 5.3. Numărul ereditar

{idx("P-028a")}
Numărul ereditar se extrage din numele de familie și indică resursele, reflexele și temele simbolice transmise prin linia de neam. El nu stabilește un destin fix, ci arată fondul moștenit pe care Marc îl poate continua, transforma sau depăși conștient.

{idx("C-008")}
> [!example] Calcul
> Vulcu = **16** → **7**

{idx("P-029")}
Numărul ereditar **7** aduce o memorie de neam legată de observație, discreție, cercetare și căutarea adevărului.

{idx("SUB-022")}
### 5.4. Numărul ereditar karmic

{idx("P-029a")}
Numărul ereditar karmic citește numele de familie în intervalul simbolic **1–22** și evidențiază o lecție arhetipală a neamului. El arată ce tipar cere înțelegere și maturizare, astfel încât resursele moștenite să fie folosite fără repetarea automată a limitelor trecutului.

{idx("C-009")}
> [!example] Calcul în intervalul 1–22
> Vulcu = **16** → Arcana **16 — Turnul**

{idx("T-013")}
| Arcana | Interpretare |
| --- | --- |
| ![Arcana 16 — Turnul](tarot-16-turnul-aplicabilitate-profesionala.jpg) | <ul><li><strong>Resursă:</strong> capacitatea de a vedea ce nu mai este stabil și de a identifica punctul care trebuie refăcut.</li><li><strong>Manifestare:</strong> curajul de a reconstrui sincer, de a încerca din nou și de a căuta o bază mai sigură.</li><li><strong>Umbră:</strong> reacția bruscă la schimbare, încăpățânarea sau păstrarea unei forme care nu mai funcționează.</li><li><strong>Maturizare:</strong> construirea siguranței interioare și acceptarea schimbării ca etapă de curățare și refacere.</li></ul> |

{idx("SUB-023")}
### 5.5. Numărul de realizare

{idx("P-029b")}
Numărul de realizare se calculează din consoanele numelui complet și descrie comportamentul vizibil, manierele și felul în care Marc este perceput de ceilalți. El arată prin ce calități poate transforma potențialul interior în rezultate concrete și unde această expresie exterioară poate deveni rigidă.

{idx("C-010")}
> [!example] Calcul
> Consoanele numelui = **31** → **4**

{idx("P-030")}
Numărul de realizare **4** te face vizibil ca persoană care poate ordona, construi și duce lucrurile către o formă concretă.

{idx("SUB-024")}
### 5.6. Numărul de exprimare

{idx("P-030a")}
Numărul de exprimare reunește toate componentele numelui și descrie direcția în care personalitatea lui Marc se poate dezvolta. El arată cum resursele interioare și imaginea exterioară pot lucra împreună într-o formă matură, coerentă și recognoscibilă.

{idx("C-011")}
> [!example] Calcul
> Vulcu **7** + Marc **8** + Ioan **3** = **18** → **9**

{idx("P-031")}
Numărul de exprimare **9** susține perspectiva largă, imaginația și compasiunea. Umbra este dispersia; maturizarea cere alegerea unui scop concret.

{idx("SUB-025")}
### 5.7. Codul numerologic al numelui

{idx("P-031a")}
Codul numerologic al numelui păstrează succesiunea vibrațiilor atribuite fiecărei litere și permite observarea distribuției lor în matrice. Compararea lui cu matricea datei de naștere arată ce energii sunt susținute de nume, ce resurse sunt amplificate și ce zone cer context, exercițiu sau relaționare conștientă.

#### Numele actual — Vulcu Marc Ioan

{idx("C-012")}
> [!example] Calcul
> Vulcu: **43333** → 16 → 7  
> Marc: **4193** → 17 → 8  
> Ioan: **9615** → 21 → 3  
> Codul literelor numelui = **4333341939615**  
> Codul numerologic personal al numelui = **9**

{idx("G-002a")}
{name_component}

{idx("P-032")}
Matricea numelui susține nativ energiile **1**, **3**, **4**, **5** și **9**. Energiile native **2** și **7** nu sunt susținute de nume și au nevoie de context relațional și reflecție conștientă.

{idx("CAP-010")}
## Capitolul 6. Spirit și karmă — Lecții și direcții de maturizare

{idx("SUB-026")}
### 6.1. Codul Spiritului și vârsta Spiritului

{idx("C-013")}
> [!example] Calcul
> 55 − 14 − (2 × 7) = **27**  
> Subetapa = **1 — Început de cale**  
> Vârsta Spiritului la naștere = **4914**; la 08.08.2026 = **4915**

{idx("T-017")}
{spirit_code}

{idx("T-018")}
| Zona | Interval cod | Nivel simbolic | Teme principale |
| --- | --- | --- | --- |
| <span class="zone-badge zone-love">Iubire</span> | 1-13 | 0-2.500 ani | relații, emoții, atașamente, compasiune, vulnerabilitate |
| <span class="zone-badge zone-reason">Rațiune</span> | 14-26 | 2.500-5.000 ani | logică, discernământ, structură, analiză, minte |
| <span class="zone-badge zone-material">Material</span> | 27-39 | 5.000-7.500 ani | bani, construcție, putere, manifestare, responsabilitate |
| <span class="zone-badge zone-gifts">Haruri</span> | 40-52 | 7.500-10.000 ani | înțelepciune, haruri spirituale, ghidare, serviciu, intuiție |

{idx("T-019")}
{spirit_stage}

{idx("P-033")}
Codul **27** te așază la începutul zonei Materiale. Spiritul învață să transforme curiozitatea în obiect, construcție, rutină și rezultat folositor.

{idx("SUB-027")}
### 6.2. Karma din ziua de naștere

{idx("C-014")}
> [!example] Calcul
> Ziua **14** → Arcana **14 — Cumpătarea** → karma împlinită **spre 80%**

{idx("G-001")}
![Arcana 14 — Cumpătarea](tarot-14-cumpatarea-karma-zilei.jpg)

{idx("P-034")}
Cumpătarea cere măsură, dozaj și alternanță între mișcare și repaus. Libertatea devine resursă când are ritm.

{idx("SUB-028")}
### 6.3. Karma din luna de naștere

{idx("C-015")}
> [!example] Calcul
> Luna nașterii = **7**

{idx("P-035")}
Luna **7** cere răbdare, observație și respect pentru timpul interior. Umbra este izolarea; direcția matură este profunzimea împărtășită.

{idx("SUB-029")}
### 6.4. Karma din Calea Destinului

{idx("C-016")}
> [!example] Calcul
> Calea Destinului = **21** → Arcana **21 — Lumea**

{idx("G-001a")}
![Arcana 21 — Lumea](tarot-21-lumea-karma-destin-si-obstacole.jpg)

{idx("P-036")}
Calea karmică **21** vorbește despre integrarea experiențelor și închiderea etapelor. Lecția este să vezi ansamblul fără să pierzi pasul concret.

{idx("SUB-030")}
### 6.5. Concluzie: direcția de lucru

{idx("P-037")}
Direcția comună unește măsura lui **14**, profunzimea lui **7**, integrarea lui **21** și manifestarea codului **27**: explorezi, observi, alegi și dai formă concretă experienței.

{idx("CAP-011")}
## Capitolul 7. Pinacluri: Oportunități și provocări

{idx("C-017")}
> [!example] Calcul
> Calea Destinului **21** → Destin compus **3**  
> Limita Pinaclului 1: 36 − 3 = **33**  
> Intervale: **0–33 → 34–43 → 44–53 → 54+**

{idx("T-003")}
| Pinaclu | Interval | Oportunitate | Provocare |
| --- | --- | ---: | ---: |
| Pinaclul 1 | 0–33 | 3 | 2 |
| Pinaclul 2 | 34–43 | 5 | 4 |
| Pinaclul 3 | 44–53 | 8 | 2 |
| Pinaclul 4 | 54+ | 7 | 2 |

{idx("P-038")}
**Pinaclul 1: intervalul 0–33**, Oportunitatea **3** susține expresia și creativitatea, iar Provocarea **2** cere cooperare.

{idx("P-039")}
**Pinaclul 2: intervalul 34–43**, Oportunitatea **5** aduce schimbare, iar Provocarea **4** cere structură.

{idx("P-040")}
**Pinaclul 3: intervalul 44–53**, Oportunitatea **8** susține autoritatea și resursele, iar Provocarea **2** cere tact.

{idx("P-041")}
**Pinaclul 4: intervalul 54+**, Oportunitatea **7** favorizează cunoașterea, iar Provocarea **2** păstrează deschiderea relațională.

{idx("CAP-012")}
## Capitolul 8. Ciclicități

{idx("SUB-031")}
### 8.1. Soarta și Destinul

{idx("G-005")}
![Grafic Soartă și Destin pentru Vulcu Marc Ioan](soarta-si-destin-vulcu-marc-ioan.svg)

{idx("C-018")}
> [!example] Numere grafice
> Soartă: 1407 × 2025 = **2849175**  
> Destin: 1417 × 2125 = **3011125**

{idx("P-042")}
Marc, în data ta predomină energia impară, astfel încât graficul se citește cu pasul de **10 ani**. Zona de confort și punctele de schimbare sunt repere simbolice; în copilărie se traduc prin ritmul familiei, învățare și siguranță.

{idx("SUB-032")}
### 8.2. Anii importanți

{idx("P-043")}
Anii interiori descriu momente în care schimbarea pornește din decizii, maturizări și nevoi lăuntrice.

{idx("P-044")}
**Șirul anilor importanți interiori:** {important_interior}.

{idx("P-045")}
Anii exteriori descriu schimbări aduse prin contexte, oameni, oportunități sau presiuni care cer adaptare.

{idx("P-046")}
**Șirul anilor importanți exteriori:** {important_exterior}.

{idx("SUB-033")}
### 8.3. Lecțiile de viață

{idx("C-019")}
> [!example] Calcul
> 14 × 7 × 2025 = **198450** → lecțiile **1–9–8–4–5–0**

{idx("T-008")}
{lesson_table}

{idx("P-047")}
În **2026**, lecția activă este **9**, iar anul personal este **4**. Empatia și imaginația au nevoie de ordine, activități încheiate și reguli blânde.

{idx("SUB-034")}
### 8.4. Ciclul de 9 ani

{idx("T-007")}
{cycle9}

{idx("P-048")}
Te afli în primul ciclu de 9 ani. Anul personal **4** pune accent pe corp, rutină, siguranță și repere repetate.

{idx("SUB-035")}
### 8.5. Ciclul de 12 ani

{idx("T-015")}
{cycle12_table()}

{idx("P-049")}
Ciclul de 12 ani **1**, 2025–2036, este etapa formării fundamentale: familie, somn, joc, limbaj emoțional și primele reguli.

{idx("CAP-013")}
## Capitolul 9. Relații

{idx("L-003")}
- Nume: Vulcu Rebeca Andreea
- Data nașterii: 15.03.2020
- Tipul relației: soră

{idx("SUB-036")}
### 9.1. Omulețul relațiilor

{idx("G-006")}
![Omulețul relațiilor pentru Vulcu Marc Ioan și Vulcu Rebeca Andreea](omulet-relatii-vulcu-marc-ioan-vulcu-rebeca-andreea.png)

{idx("C-020")}
> [!example] Calcul relațional
> Realizare împreună: 5 + 6 = 11 → **2**  
> De rezolvat împreună: |5 − 6| = **1**

{idx("P-050")}
Marc, tu aduci mișcarea lui **5**, iar Rebeca grija lui **6**. Potențialul comun **2** cere cooperare și apropiere, iar tema **1** cere ca fiecare să își păstreze identitatea.

{idx("P-051")}
Împreună aveți Foc **4**, Apă **4**, Aer **2**, Pământ **1** și potențial **0** de patru ori. Stabilitatea și regulile se construiesc intenționat (4), iar responsabilitatea și puterea primesc sprijin din familie și activități potrivite (8).

{idx("CAP-014")}
## Capitolul 10. Aplicabilitate profesională

{idx("SUB-037")}
### 10.1. Aplicabilitate profesională

{idx("P-051a")}
Aplicabilitatea profesională traduce data nașterii în zona muncii, a învățării și a colaborării. Ea nu stabilește de acum o meserie pentru tine, ci arată energia pe care o poți folosi mai natural, tipul de probleme care îți pot trezi interesul și obstacolul interior care merită recunoscut înainte să îți frâneze dezvoltarea.

{idx("C-021")}
> [!example] Calcul
> DA: 7 + 9 = **16**  
> NU: 21 = **21**

{idx("T-016")}
| Aplicabilitate profesională DA | Aplicabilitate profesională NU |
| --- | --- |
| ![Arcana 16 — Turnul, aplicabilitate profesională](tarot-16-turnul-aplicabilitate-profesionala.jpg)<br>_Arcana 16 — Turnul. Direcția profesională de cultivat_ | ![Arcana 21 — Lumea, obstacole profesionale](tarot-21-lumea-karma-destin-si-obstacole.jpg)<br>_Arcana 21 — Lumea. Obstacolul profesional de echilibrat_ |
| **Index: VMI-20250714-v1.00r-P-052**<br>Turnul simbolizează capacitatea de a observa repede unde o structură este fragilă și de a avea curajul să o refaci pe o bază mai bună. În plan profesional, această energie te poate susține când trebuie să identifici o eroare, să pui întrebări incomode, să reorganizezi un sistem sau să continui după ce prima soluție nu a funcționat. Poți manifesta această resursă prin curiozitatea de a desface și reconstrui, prin plăcerea de a testa mai multe variante și prin inițiativa de a interveni atunci când ceilalți acceptă prea ușor o problemă.<br><br>Turnul favorizează contexte în care analiza și reconstrucția produc un rezultat concret: inginerie, arhitectură, construcții, tehnologie, programare și depanare, securitate informatică, reparații tehnice, cercetare, controlul calității, audit, administrarea riscului sau proiecte de transformare. La vârsta ta, aceste aptitudini pot fi observate fără a alege încă o profesie, prin jocuri de construcție, mecanisme, puzzle-uri, experimente și proiecte în care poți corecta o versiune și încerca din nou.<br><br>Condiția de maturizare este să deosebești schimbarea necesară de impulsul de a respinge ori de a dărâma prea repede. Verifică faptele, explică ce nu funcționează și propune o alternativă înainte să rupi forma veche. Când inițiativa este însoțită de răbdare, colaborare și un plan de reconstrucție, Turnul devine talentul de a transforma criza într-o soluție mai sigură și mai folositoare. | **Index: VMI-20250714-v1.00r-P-052a**<br>Când Lumea apare ca obstacol profesional, ea nu indică lipsa talentului, ci dificultatea de a închide un ciclu atunci când vezi prea multe posibilități deodată. Poți imagina foarte clar rezultatul final, dar tocmai imaginea completă te poate face să amâni versiunea intermediară, să cauți încă o îmbunătățire sau să începi alt proiect înainte ca primul să fie terminat. Orizontul larg este o resursă reală, însă devine blocaj dacă fiecare lucrare trebuie să pară completă și impecabilă de la început.<br><br>Dispersia, perfecționismul și nevoia de validare pot consuma energia care ar trebui folosită pentru finalizare. Poți fi atras de multe domenii, poți compara un rezultat aflat la început cu realizările mature ale altora sau poți considera că un pas mic nu este suficient de important. În timp, acest tipar poate lăsa proiecte valoroase neterminate, nu pentru că nu ai capacitate, ci pentru că pragul imaginar al reușitei a fost așezat prea departe.<br><br>Cheia practică este să definești de la început ce înseamnă „terminat”, să lucrezi în etape scurte și să prezinți versiuni care pot fi îmbunătățite ulterior. Închide un proiect înainte de a deschide altul, cere feedback pentru un rezultat concret și compară progresul cu etapa ta anterioară, nu cu perfecțiunea. Astfel, Lumea încetează să fie presiunea de a cuprinde totul și devine capacitatea matură de a integra ideile, de a vedea ansamblul și de a duce o lucrare până la capăt. |

{idx("CAP-015")}
## Capitolul 11. Concluzii

{idx("SUB-038")}
### 11.1. Carieră și bani

{idx("P-053")}
Marc, potențialul profesional leagă explorarea lui **5**, expresia Destinului **3**, rezultatul Numărului activ **8** și perspectiva Numărului de exprimare **9**. Vectorul **159 — Carieră** este cel mai puternic, dar energiile **6** și **8** sunt conservate în matricea nativă; disciplina, responsabilitatea și relația cu resursele trebuie formate prin exercițiu.

{idx("P-054")}
Nu este nevoie să îți fie aleasă acum o meserie. Este mai util să fie observat ce termini cu plăcere, cum repari o problemă și în ce contexte curiozitatea rămâne vie. Libertatea lui **5** primește cadrul lui **4**, iar expresia lui **3** servește perspectiva lui **9**.

{idx("SUB-039")}
### 11.2. Iubire și relație

{idx("P-055")}
Relația cu sora ta are potențialul **2**, deci crește prin apropiere, cooperare și încredere. Tu aduci noutatea, iar Rebeca poate aduce grijă și continuitate.

{idx("P-056")}
Podul **1** vă cere să rămâneți două persoane distincte. Comparațiile puține, limitele identice explicate pe înțelesul fiecăruia, activitățile comune scurte și timpul individual transformă competiția în autonomie sănătoasă.

{idx("SUB-040")}
### 11.3. Momentul prezent

{idx("P-057")}
Marc, în intervalul actual te afli în primul Pinaclu, cu Oportunitatea **3** și Provocarea **2**, în primul ciclu de 9 ani și în primul ciclu de 12 ani. Anul personal **4** din 2026 cere rutină, corp, siguranță și repere simple, iar Lecția **9** aduce empatie și imaginație. Pentru vârsta ta, sinteza practică este un mediu stabil în care poți explora fără grabă, poți termina activități scurte și poți învăța să numești ceea ce simți.

{idx("CAP-016")}
## Documentația și trasabilitatea lucrării

{idx("T-014")}
| Resursă | Valoare |
| --- | --- |
| Template | `scurt` — model Bîrsan Daniel Robert v1.00r |
| Raport calculator | `2025-07-14-VULCU-MARC-IOAN-scurt-v1.00r-calculator.json` |
| Grafice integrate | Matrice, Scara bunăstării, Soartă–Destin și Omulețul relațiilor |
| Versiune și data redactării | V1.00R — 08.08.2026 |
'''


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    report = run_report()
    helpers = load_helpers()
    calc = report["capitolul_2_formule_calcule_tabele_grafice"]
    matrix = calc["2.2_structura_matriciala"]
    cycles = calc["2.4_ciclicitati"]
    lessons = cycles["lectii_de_viata"]["sir_lectii"]
    date_component = (OUT_DIR / "matrita-datei-vulcu-marc-ioan-g-002.html").read_text(encoding="utf-8")
    name_component = (OUT_DIR / "matrita-numelui-vulcu-marc-ioan-g-002a.html").read_text(encoding="utf-8")

    tarot = ROOT / "vault/tarot/imagini"
    for source, target in (
        ("14-Temperance.jpg", "tarot-14-cumpatarea-karma-zilei.jpg"),
        ("16-The Tower.jpg", "tarot-16-turnul-aplicabilitate-profesionala.jpg"),
        ("21-The World.jpg", "tarot-21-lumea-karma-destin-si-obstacole.jpg"),
    ):
        shutil.copyfile(tarot / source, OUT_DIR / target)

    wellbeing = helpers.wellbeing(matrix["scara_bunastarii"])
    lesson_table = helpers.lesson_table(lessons, start_year=2025)
    cycle9 = helpers.cycle9_table(start_year=2025)
    spirit_code = helpers.spirit_code_table(14, 7)
    spirit_stage = helpers.spirit_stage_table(1)

    md = f'''---
title: "Lucrare numerologică scurtă — Vulcu Marc Ioan"
person_id: "2025-07-14-VULCU-MARC-IOAN"
version: "v1.00r"
date: "08.08.2026"
template: "scurt"
---

# Vulcu Marc Ioan

## Lucrare numerologică — varianta scurtă

{idx("L-001")}
- Nume complet: Vulcu Marc Ioan
- Prenume activ: Marc
- Data nașterii: 14.07.2025
- Ora nașterii: 14:26
- Gen: masculin
- Relație analizată: Vulcu Rebeca Andreea, soră, născută la 15.03.2020
- Versiune: V1.00R
- Data redactării: 08.08.2026

## Cuprins

1. Profilul numerologic de bază
2. Matricea datei și matricea numelui
3. Codul Spiritului
4. Karma
5. Pinacluri
6. Scara bunăstării
7. Soartă și Destin
8. Ciclicități
9. Relații
10. Aplicabilitate profesională
11. Concluzii

{idx("CAP-001")}
## Capitolul 1. Profilul numerologic de bază

{idx("SUB-001")}
### 1.1. Vibrația interioară și exterioară

{idx("C-001")}
> [!example] Calcul
> Ziua **14** → 1 + 4 = **5**  
> Luna **7** → **7**  
> Puntea interior–exterior: |5 − 7| = **2**

{idx("P-001")}
Marc, vibrația interioară **5** îți aduce curiozitate, mobilitate și nevoie de explorare. Înveți bine când poți atinge, încerca și compara. Vibrația exterioară **7** te poate face să pari atent, selectiv și observator. Puntea **2** arată că legătura dintre libertatea interioară și discreția vizibilă se construiește prin răbdare, cooperare și siguranță afectivă.

{idx("SUB-002")}
### 1.2. Calea Destinului

{idx("C-002")}
> [!example] Calcul
> 1 + 4 + 0 + 7 + 2 + 0 + 2 + 5 = **21** → 2 + 1 = **3**  
> Puntea interior–Destin: |5 − 3| = **2**

{idx("P-002")}
Calea **21/3** unește deschiderea către lume cu expresia, creativitatea și comunicarea. Muntele tău de urcat este să transformi ideile și experiențele în cuvinte, joc, imagine sau proiect. Energia **5** pornește în explorare, iar **3** îi dă limbaj; disciplina blândă te ajută să nu te risipești.

{idx("CAP-002")}
## Capitolul 2. Matricea datei și matricea numelui

{idx("SUB-003")}
### 2.1. Matricea datei de naștere

{idx("C-003")}
> [!example] Numere de lucru
> N1 = **21**; N2 = **3**; N3 = **19**; N4 = **10**  
> Șir complet: **140720252131910**

{idx("G-002")}
{date_component}

{idx("P-003")}
Matricea ta conține **1111**, **222**, câte un **3**, **4**, **5**, **7** și **9**, iar căsuțele **6** și **8** nu apar. Ai inițiativă și energie relațională, dar continuitatea practică, răbdarea financiară și administrarea puterii trebuie formate prin obiceiuri simple și repetate.

{idx("P-004")}
Vectorii plini **123 — Energie**, **147 — Spiritualitate**, **159 — Carieră** și **357 — Scopuri** arată un potențial puternic de a porni, de a căuta sens și de a urmări o direcție. Fixația **147** cere flexibilitate în convingeri, iar tendința **159** cere să legi ambiția de un scop folositor.

{idx("SUB-004")}
### 2.2. Matricea numelui

{idx("C-004")}
> [!example] Calculul numelui
> Vulcu = **16 → 7**; Marc = **17 → 8**; Ioan = **21 → 3**  
> Numărul de exprimare: 7 + 8 + 3 = **18 → 9**

{idx("G-002a")}
{name_component}

{idx("P-005")}
Numărul activ **8** aduce hotărâre și simț al rezultatului. Numărul intim **5** caută libertate și varietate, Numărul de realizare **4** te face să pari mai ordonat decât te simți uneori, iar Numărul de exprimare **9** deschide compasiunea, imaginația și perspectiva largă. Numele îți cere să folosești puterea fără rigiditate și libertatea fără risipire.

{idx("CAP-003")}
## Capitolul 3. Codul Spiritului

{idx("SUB-005")}
### 3.1. Poziția și subetapa

{idx("C-005")}
> [!example] Calcul
> 55 − 14 − (2 × 7) = **27**  
> Subetapa: **1 — Început de cale**  
> Vârsta simbolică la naștere: (27 − 1) × 189 = **4914**; la 08.08.2026: **4915**

{idx("T-017")}
{spirit_code}

{idx("T-018")}
| Zona | Interval cod | Nivel simbolic | Teme principale |
| --- | --- | --- | --- |
| <span class="zone-badge zone-love">Iubire</span> | 1-13 | 0-2.500 ani | relații, emoții, atașamente, compasiune, vulnerabilitate |
| <span class="zone-badge zone-reason">Rațiune</span> | 14-26 | 2.500-5.000 ani | logică, discernământ, structură, analiză, minte |
| <span class="zone-badge zone-material">Material</span> | 27-39 | 5.000-7.500 ani | bani, construcție, putere, manifestare, responsabilitate |
| <span class="zone-badge zone-gifts">Haruri</span> | 40-52 | 7.500-10.000 ani | înțelepciune, haruri spirituale, ghidare, serviciu, intuiție |

{idx("T-019")}
{spirit_stage}

{idx("P-006")}
Codul **27** te așază la începutul zonei Materiale. Lecția este să dai formă concretă curiozității: un joc terminat, o construcție, o poveste spusă până la capăt. Subetapa **1** cere descoperirea identității prin experiențe sigure, nu prin presiune.

{idx("CAP-004")}
## Capitolul 4. Karma

{idx("SUB-006")}
### 4.1. Ziua, luna și Calea Destinului

{idx("G-001")}
![Arcana 14 — Cumpătarea](tarot-14-cumpatarea-karma-zilei.jpg)

_Arcana **14 — Cumpătarea**, karma zilei de naștere_

{idx("P-007")}
Ziua **14** este asociată Cumpătării și categoriei karmice „spre 80%”. Tema ei este măsura: libertatea lui **5** se maturizează când învață ritmul, dozajul și alternanța dintre mișcare și repaus. Luna **7** cere răbdare, observație și respect pentru timpul interior.

{idx("G-001a")}
![Arcana 21 — Lumea](tarot-21-lumea-karma-destin-si-obstacole.jpg)

_Arcana **21 — Lumea**, karma din Calea Destinului_

{idx("P-008")}
Calea karmică **21** vorbește despre integrare, deschidere și încheierea etapelor. Lecția este să vezi ansamblul fără să pierzi pasul concret. Aspectul de îndreptat **19**, cu soluția compusă **10**, cere să transformi afirmarea personală în inițiativă responsabilă și adaptare la schimbare.

{idx("CAP-005")}
## Capitolul 5. Pinacluri

{idx("C-006")}
> [!example] Calcul
> Limita Pinaclului 1: 36 − Destinul compus 3 = **33**

{idx("T-003")}
| Pinaclu | Interval | Oportunitate | Provocare | Direcție |
| --- | --- | ---: | ---: | --- |
| 1 | 0–33 | 3 | 2 | expresie și creativitate, cu lecția cooperării |
| 2 | 34–43 | 5 | 4 | schimbare, cu nevoie de structură |
| 3 | 44–53 | 8 | 2 | autoritate și resurse, cu tact relațional |
| 4 | 54+ | 7 | 2 | cunoaștere și profunzime, cu deschidere către ceilalți |

{idx("P-009")}
În Pinaclul **1**, Oportunitatea **3** susține limbajul, joaca și creativitatea, iar Provocarea **2** cere răbdare, cooperare și reglare emoțională. Pentru copilărie, cea mai bună susținere este o combinație de libertate ghidată, rutină caldă și încurajarea exprimării.

{idx("CAP-006")}
## Capitolul 6. Scara bunăstării

{idx("G-004")}
{wellbeing}

{idx("P-010")}
Scara este condusă de **Vectorul 159 — Carieră (18)**, urmat de **789 — Creativitate (16)** și de **147 — Spiritualitate** împreună cu **357 — Scopuri (15)**. Potențialul se activează când o idee primește țintă, ritm și finalizare. Căsuțele **6** și **8** cer educație practică despre responsabilitate, bani, limite și folosirea corectă a puterii.

{idx("CAP-007")}
## Capitolul 7. Soartă și Destin

{idx("G-005")}
![Grafic Soartă și Destin pentru Vulcu Marc Ioan](soarta-si-destin-vulcu-marc-ioan.svg)

{idx("C-007")}
> [!example] Numere grafice
> Soartă: 1407 × 2025 = **2849175**  
> Destin: 1417 × 2125 = **3011125**

{idx("P-011")}
Linia Sorții **2–8–4–9–1–7–5** alternează sensibilitatea, forța, ordinea și analiza. Linia Destinului **3–0–1–1–1–2–5** pune accent pe exprimare, începuturi și adaptare. În această etapă, graficul se citește prin familie, ritm și contexte de învățare, nu ca predicție rigidă.

{idx("CAP-008")}
## Capitolul 8. Ciclicități

{idx("SUB-020")}
### 8.1. Lecțiile de viață

{idx("C-008")}
> [!example] Calcul
> 14 × 7 × 2025 = **198450** → lecțiile **1–9–8–4–5–0**

{idx("T-008")}
{lesson_table}

{idx("P-012")}
În **2026**, lecția activă este **9**: empatie, imaginație, desprindere și capacitatea de a vedea mai larg. Ea se întâlnește cu anul personal **4**, care cere ordine și stabilitate. Pentru Marc, combinația se traduce prin gesturi simple: să încheie activități, să își așeze lucrurile și să învețe să împartă fără să fie grăbit.

{idx("SUB-021")}
### 8.2. Ciclul de 9 ani

{idx("T-007")}
{cycle9}

{idx("P-013")}
Marc se află în primul ciclu de 9 ani. Anul personal **4** din 2026 pune accent pe rutină, siguranță, corp și reguli explicate calm. Stabilitatea nu trebuie să îi blocheze curiozitatea, ci să îi ofere o bază din care poate explora.

{idx("SUB-022")}
### 8.3. Ciclul de 12 ani

{idx("T-015")}
{cycle12_table()}

{idx("P-014")}
Ciclul de 12 ani **1**, 2025–2036, este etapa formării fundamentale. Familia, somnul, jocul, limbajul emoțional și reperele repetate au acum mai multă greutate decât orice alegere profesională îndepărtată.

{idx("CAP-009")}
## Capitolul 9. Relații

{idx("L-003")}
- Nume: Vulcu Rebeca Andreea
- Data nașterii: 15.03.2020
- Gen: feminin
- Tipul relației: soră

{idx("SUB-010")}
### 9.1. Relația cu Rebeca

{idx("G-006")}
![Omulețul relațiilor pentru Vulcu Marc Ioan și Vulcu Rebeca Andreea](omulet-relatii-vulcu-marc-ioan-vulcu-rebeca-andreea.png)

{idx("C-009")}
> [!example] Calcul relațional
> Realizare împreună: 5 + 6 = 11 → **2**  
> De rezolvat împreună: |5 − 6| = **1**

{idx("P-015")}
Marc, tu vii în relația cu sora ta prin ziua redusă **5**, iar Rebeca prin **6**. Tu aduci mișcare, curiozitate și joc; ea aduce grijă, responsabilitate și nevoia de armonie. Potențialul comun **2** cere apropiere, cooperare și sensibilitate față de ritmul celuilalt.

{idx("P-016")}
Tema de rezolvat **1** este identitatea: fiecare copil are nevoie de locul lui, de obiectele lui, de lauda lui și de dreptul de a iniția. Relația se echilibrează când adulții evită comparațiile și creează alternanță între activități comune și timp individual.

{idx("P-017")}
În cifrele brute comune, Focul are **4** apariții, Apa **4**, Aerul **2**, Pământul **1**, iar potențialul lui **0** apare de **4** ori. Emoția și inițiativa sunt puternice; partea practică are nevoie de reguli simple, ritualuri de familie și responsabilități potrivite vârstei.

{idx("CAP-010")}
## Capitolul 10. Aplicabilitate profesională

{idx("SUB-011")}
### 10.1. Direcție și obstacol

{idx("C-010")}
> [!example] Calcul
> DA: luna 7 + suma cifrelor anului 9 = **16**  
> NU: suma tuturor cifrelor datei = **21**

{idx("T-016")}
| Aplicabilitate profesională DA | Aplicabilitate profesională NU |
| --- | --- |
| ![Arcana 16 — Turnul](tarot-16-turnul-aplicabilitate-profesionala.jpg)<br>**16 — Turnul:** talent de a observa ce nu funcționează și de a reconstrui mai bine. | ![Arcana 21 — Lumea](tarot-21-lumea-karma-destin-si-obstacole.jpg)<br>**21 — Lumea:** obstacolul poate fi dispersia în prea multe direcții sau așteptarea unei imagini perfecte. |

{idx("P-018")}
Pentru Marc, această secțiune descrie un potențial care se va maturiza în timp. Arcana **16** favorizează rezolvarea problemelor, restructurarea și curajul de a încerca din nou. Arcana **21** cere să închidă o etapă înainte de a porni alta. Jocurile de construcție, proiectele creative și sarcinile cu început și final sunt terenul potrivit pentru dezvoltare.

{idx("CAP-011")}
## Capitolul 11. Concluzii

{idx("SUB-012")}
### 11.1. Carieră și bani

{idx("P-019")}
Marc, potențialul tău profesional leagă **5**, **3**, **8** și **9**: explorare, exprimare, rezultat și viziune largă. Vectorul de Carieră este cel mai puternic, însă căsuțele **6** și **8** lipsesc din matricea nativă; de aceea, relația sănătoasă cu munca și banii se construiește prin responsabilități mici, consecvență, economisire și respectarea limitelor.

{idx("P-020")}
Nu este nevoie să îi fie aleasă acum o meserie. Este mai util să fie observat ce termină cu plăcere, cum rezolvă o problemă și în ce contexte își păstrează curiozitatea. Când libertatea lui **5** primește cadrul lui **4**, iar expresia lui **3** servește perspectiva lui **9**, talentul poate deveni competență reală.

{idx("SUB-013")}
### 11.2. Relația cu sora

{idx("P-021")}
Relația cu Rebeca are potențialul **2**, deci se dezvoltă prin apropiere, cooperare și încredere. Marc poate aduce noutatea, iar Rebeca poate aduce grijă și continuitate. Podul **1** cere ca fiecare să rămână o persoană distinctă, fără roluri rigide precum „cel cuminte” sau „cel energic”.

{idx("P-022")}
Sprijinul practic este simplu: comparații cât mai puține, limite identice explicate pe înțelesul fiecăruia, activități comune scurte și posibilitatea de a se retrage separat. Astfel, energia **2** devine alianță frățească, iar lecția **1** devine autonomie sănătoasă, nu competiție.

{idx("CAP-012")}
## Resurse și trasabilitate

{idx("T-014")}
| Resursă | Valoare |
| --- | --- |
| Template | `scurt` — model Bîrsan Daniel Robert v1.00r |
| Raport calculator | `2025-07-14-VULCU-MARC-IOAN-scurt-v1.00r-calculator.json` |
| Grafice integrate | Matricea datei, matricea numelui, Soartă–Destin și Omulețul relațiilor |
| Versiune și data redactării | V1.00R — 08.08.2026 |
'''

    md = canonical_document(
        date_component=date_component,
        name_component=name_component,
        wellbeing=wellbeing,
        spirit_code=spirit_code,
        spirit_stage=spirit_stage,
        lesson_table=lesson_table,
        cycle9=cycle9,
    )
    OUT.write_text(md, encoding="utf-8", newline="\n")
    print(OUT)


if __name__ == "__main__":
    main()

---
titlu: Biblioteca reutilizabilă pentru vibrațiile fundamentale
tip: plan
status: planificat
Data: 2026-07-17
aliases:
  - Plan bibliotecă vibrații fundamentale
  - Bibliotecă editorială vibrații fundamentale
tags:
  - plan
  - numerologie
  - skill
  - redactare
  - biblioteca-editoriala
skill: "[[skills/numerologie-lucrare-redactare/SKILL|numerologie-lucrare-redactare]]"
model_editorial: "[[output/lucrari/1998-02-19-BIRSAN-DANIEL-ROBERT/1998-02-19-BIRSAN-DANIEL-ROBERT-v1.07r|Lucrarea lui Bîrsan Daniel Robert v1.07R]]"
---

# Biblioteca reutilizabilă pentru vibrațiile fundamentale

> [!abstract] Obiectiv
> Construirea unei biblioteci editoriale ample, conversaționale și reutilizabile pentru toate vibrațiile fundamentale. Textele vor putea fi selectate și asamblate ulterior printr-un script Python, fără generarea de interpretări noi cu un model lingvistic și fără consum suplimentar de tokenuri pentru redactarea de bază.

## Cuprins

- [[#1. Rezultatul urmărit|1. Rezultatul urmărit]]
- [[#2. Conceptele acoperite|2. Conceptele acoperite]]
- [[#3. Organizarea în skill|3. Organizarea în skill]]
- [[#4. Relația dintre JSON și Markdown|4. Relația dintre JSON și Markdown]]
- [[#5. Interfața pentru identitatea persoanei|5. Interfața pentru identitatea persoanei]]
- [[#6. Schema modulelor editoriale|6. Schema modulelor editoriale]]
- [[#7. Reguli de redactare|7. Reguli de redactare]]
- [[#8. Acoperirea numerică integrală|8. Acoperirea numerică integrală]]
- [[#9. Profilurile de asamblare|9. Profilurile de asamblare]]
- [[#10. Scripturile necesare|10. Scripturile necesare]]
- [[#11. Actualizarea skill-ului|11. Actualizarea skill-ului]]
- [[#12. Validare și teste|12. Validare și teste]]
- [[#13. Criterii de acceptare|13. Criterii de acceptare]]
- [[#14. Limitele acestei etape|14. Limitele acestei etape]]

## 1. Rezultatul urmărit

Biblioteca trebuie să ofere suficiente formulări prestabilite pentru redactarea unei interpretări ample, de aproximativ **650–900 de cuvinte pentru fiecare vibrație fundamentală**. Interpretarea rezultată trebuie să aibă un fir natural și să pară adresată direct persoanei, nu asamblată mecanic din fragmente independente.

Modelul editorial principal este lucrarea lui Bîrsan Daniel Robert. Se păstrează:

- tonul cald, conversațional și clar;
- adresarea directă către cititor;
- imaginile ușor de vizualizat;
- explicarea rezultatului final și a traseului real de reducere;
- exemplele aplicabile în viața obișnuită;
- prezentarea dezechilibrelor ca teme constructive, nu ca verdicte;
- evitarea repetării aceleiași idei în mai multe paragrafe.

## 2. Conceptele acoperite

Biblioteca va conține câte un fișier dedicat pentru:

1. [[vault/Numerologie/Vibratie Interioara|Vibrația interioară]];
2. [[vault/Numerologie/Vibratie Exterioara|Vibrația exterioară]];
3. [[vault/Numerologie/Vibratie Globala|Vibrația globală]];
4. [[vault/Numerologie/Vibratie Cosmica Fixa|Vibrația cosmică fixă]];
5. [[vault/Numerologie/Vibratie Cosmica Variabila|Vibrația cosmică variabilă]];
6. [[vault/Numerologie/Vibratie Cosmica Totala|Vibrația cosmică totală]].

Un fișier comun va păstra semnificațiile cifrelor, interacțiunile dintre ele, pragurile intermediare, conectorii și tranzițiile care pot fi reutilizate între concepte.

## 3. Organizarea în skill

Sursa va fi adăugată în skill-ul local:

`skills/numerologie-lucrare-redactare/`

Structura planificată:

```text
skills/numerologie-lucrare-redactare/
├── SKILL.md
├── assets/
│   └── biblioteca-vibratii-fundamentale/
│       ├── manifest.json
│       ├── manifest.md
│       ├── comun.json
│       ├── comun.md
│       ├── vibratia-interioara.json
│       ├── vibratia-interioara.md
│       ├── vibratia-exterioara.json
│       ├── vibratia-exterioara.md
│       ├── vibratia-globala.json
│       ├── vibratia-globala.md
│       ├── vibratia-cosmica-fixa.json
│       ├── vibratia-cosmica-fixa.md
│       ├── vibratia-cosmica-variabila.json
│       ├── vibratia-cosmica-variabila.md
│       ├── vibratia-cosmica-totala.json
│       └── vibratia-cosmica-totala.md
├── references/
│   └── biblioteca-vibratii-fundamentale.md
└── scripts/
    ├── genereaza_biblioteca_vibratii_md.py
    └── valideaza_biblioteca_vibratii.py
```

Nu se creează un `README.md` suplimentar. Instrucțiunile operaționale vor sta în `references/biblioteca-vibratii-fundamentale.md`, legat direct din `SKILL.md`.

## 4. Relația dintre JSON și Markdown

### Sursa canonică

Fișierele `.json` reprezintă sursa canonică. Viitorul selector Python va citi exclusiv aceste fișiere.

### Oglinda pentru verificare umană

Fiecare JSON va avea un fișier `.md` corespunzător, generat automat. Fișierele Markdown vor permite:

- citirea ușoară în Obsidian;
- verificarea tonului și a diacriticelor;
- compararea variantelor;
- navigarea după concept, rezultat, traseu și categorie editorială;
- identificarea rapidă a formulărilor repetitive.

Markdown-ul generat va păstra ID-urile și ordinea modulelor din JSON. Frontmatter-ul fiecărui fișier va indica:

```yaml
---
tip: biblioteca-editoriala-generata
sursa: vibratia-interioara.json
schema_version: 1
editare: nu se editeaza manual
---
```

Orice corectură se face în JSON, după care fișierul Markdown este regenerat.

## 5. Interfața pentru identitatea persoanei

Niciun text din bibliotecă nu va conține direct numele unei persoane-model. Sunt permise numai placeholder-ele aprobate:

| Placeholder | Sursa din fișa persoanei | Utilizare |
| --- | --- | --- |
| `{prenume_activ}` | `identitate.prenume_activ` | adresarea conversațională implicită |
| `{prenume}` | `identitate.prenume` | toate prenumele persoanei |
| `{nume_familie}` | `identitate.nume_familie` | referire tehnică la numele de familie |
| `{nume_complet}` | `identitate.nume_complet` | identificarea completă a persoanei |
| `{gen}` | `identitate.gen` | disponibil pentru extensii ulterioare |

Exemplu reutilizabil:

```text
{prenume_activ}, această vibrație îți arată felul în care pornește energia ta interioară înainte ca ceilalți să vadă rezultatul.
```

Adresarea obișnuită va folosi `{prenume_activ}`. Formulările vor fi neutre ca gen, pentru a evita dublarea inutilă a bibliotecii și acordurile greșite.

Validatorul trebuie să respingă:

- nume personale introduse direct în texte;
- placeholder-e necunoscute;
- acolade neînchise;
- folosirea inconsistentă a numelui complet în adresarea conversațională.

## 6. Schema modulelor editoriale

Fiecare modul va avea o structură stabilă:

```json
{
  "id": "vi-rezultat-1-nucleu-001",
  "categorie": "nucleu",
  "varianta": 1,
  "aplicabilitate": {
    "rezultat": 1,
    "tip_traseu": "oricare"
  },
  "text": "{prenume_activ}, ...",
  "placeholder_e": ["prenume_activ"],
  "numar_cuvinte": 112,
  "etichete": ["conversational", "amplu", "rezultat-final"]
}
```

Pentru fiecare categorie obligatorie se redactează **cinci variante distincte**:

- introducere imagistică;
- explicația conceptului;
- introducerea calculului;
- interpretarea traseului;
- rezultatul central și arhetipurile;
- resurse și manifestare echilibrată;
- exemplu sau rutină practică;
- dezechilibru și conștientizare;
- integrare și încheiere.

ID-urile trebuie să fie stabile, ASCII și unice. Modificarea textului nu schimbă ID-ul. Un modul eliminat nu își transferă ID-ul către alt text.

## 7. Reguli de redactare

Toate textele trebuie:

- să fie scrise în limba română cu diacritice corecte;
- să folosească ton conversațional, cald și matur;
- să vorbească direct cu persoana;
- să păstreze rezultatul final ca accent principal;
- să folosească traseul pentru nuanțare, fără să repete descrierea rezultatului;
- să adauge în fiecare paragraf o informație nouă;
- să includă aplicații concrete, rutine, exemple sau întrebări utile;
- să evite diagnosticele, predicțiile rigide și etichetele degradante;
- să evite începuturile mecanice repetate precum „Pentru tine”, „La tine”, „În viața de zi cu zi” și „Cheia practică”;
- să evite concluziile identice între vibrații;
- să folosească imagini verbale compatibile cu modelul Daniel, fără copierea repetitivă a acelorași metafore.

### Traseul de reducere

- Se interpretează numai când există efectiv una sau mai multe trepte de reducere.
- Dacă valoarea este directă, nu se menționează că traseul lipsește.
- Cifrele de intrare, suma intermediară și rezultatul final primesc roluri diferite.
- Cifra `0` este descrisă prudent: nu adaugă o direcție numerică separată, dar poate deschide sau amplifica potențialul cifrei alăturate.
- Numerele intermediare 10, 11, 12 și celelalte praguri reale sunt păstrate pentru nuanțare, fără a schimba regula rezultatului final redus.

## 8. Acoperirea numerică integrală

### Vibrația interioară

- zilele de naștere `1–31`;
- rezultate finale `1–9`;
- trasee directe, cu o reducere și cu două reduceri;
- tratarea distinctă a zilelor precum `10`, `11`, `19`, `20`, `28` și `29`.

### Vibrația exterioară

- lunile `1–12`;
- luni directe `1–9`;
- traseele `10 -> 1`, `11 -> 2` și `12 -> 3`.

### Vibrația globală

- toate cele `81` de combinații ordonate dintre vibrația interioară `1–9` și vibrația exterioară `1–9`;
- regula operațională: `vibrație interioară redusă + vibrație exterioară redusă`;
- interpretarea combinată a interiorului și exteriorului;
- traseu suplimentar numai dacă suma este mai mare decât `9`;
- rezultate finale `1–9`.

### Vibrația cosmică fixă

- prefixul `19` pentru anii `1900–1999`;
- prefixul `20` pentru anii `2000–2099`;
- interpretare ca fundal colectiv și stabil, fără reducere operațională.

### Vibrația cosmică variabilă

- toate terminațiile de an `00–99`;
- rezultate finale `0–9`;
- toate sumele intermediare posibile `0–18`;
- tratament special și prudent pentru terminația `00` și rezultatul `0`.

### Vibrația cosmică totală

- fiecare an din intervalul `1900–2099`;
- toate sumele și pragurile intermediare produse de cifrele anului;
- rezultate finale `1–9`;
- interpretarea cifrelor anului, a sumei intermediare și a rezultatului central.

## 9. Profilurile de asamblare

Biblioteca va defini profiluri distincte pentru:

1. valoare directă;
2. traseu cu o singură reducere;
3. traseu cu două reduceri;
4. vibrație globală fără reducere suplimentară;
5. vibrație globală cu reducere suplimentară;
6. vibrație cosmică fixă, bazată pe extragere;
7. rezultat cosmic variabil `0`.

Un profil obișnuit va selecta:

1. o introducere imagistică;
2. o explicație a conceptului;
3. o formulare pentru calcul;
4. o interpretare a traseului, numai când este aplicabilă;
5. un nucleu pentru rezultatul final;
6. un paragraf despre resurse și arhetipuri;
7. un exemplu practic;
8. un paragraf despre dezechilibru;
9. o integrare finală.

Pentru o valoare directă, locul traseului este înlocuit cu o nuanță practică sau relațională, nu cu un paragraf care explică absența reducerii.

Bugetele pe module trebuie să permită obținerea unei interpretări finale între **650 și 900 de cuvinte**.

## 10. Scripturile necesare

### Generatorul Markdown

`scripts/genereaza_biblioteca_vibratii_md.py` va:

- citi toate fișierele JSON canonice;
- genera fișierele Markdown în ordine stabilă;
- păstra ID-urile și placeholder-ele;
- crea frontmatter, cuprins și heading-uri Obsidian;
- avea un mod `--check` care nu scrie și raportează diferențele.

### Validatorul bibliotecii

`scripts/valideaza_biblioteca_vibratii.py` va verifica:

- structura JSON;
- versiunea schemei;
- ID-urile unice;
- numărul obligatoriu de variante;
- acoperirea numerică;
- placeholder-ele;
- numărul de cuvinte;
- duplicatele exacte;
- textele foarte similare;
- caracterele mojibake;
- sincronizarea JSON–Markdown.

### Selectorul final

Scriptul care va alege modulele, va injecta datele persoanei și va compune interpretarea finală nu este inclus în această etapă. Schema bibliotecii trebuie însă proiectată astfel încât selectorul să poată fi adăugat ulterior fără schimbarea fișierelor de conținut.

## 11. Actualizarea skill-ului

Fișierul [[skills/numerologie-lucrare-redactare/SKILL|SKILL.md]] va primi instrucțiuni concise pentru:

- localizarea bibliotecii;
- citirea ghidului din `references/`;
- folosirea JSON-ului ca sursă canonică;
- regenerarea Markdown-ului după orice corectură;
- folosirea placeholder-elor din fișa persoanei;
- interdicția de a inventa alte formule sau de a amesteca rezultate nevalidate;
- validarea bibliotecii înainte de folosire.

Detaliile ample ale schemei nu vor fi duplicate în `SKILL.md`; ele vor rămâne în referința dedicată.

## 12. Validare și teste

### Verificări automate

- toate fișierele JSON se parsează în UTF-8;
- toate fișierele Markdown sunt regenerate fără diferențe;
- fiecare ID este unic;
- fiecare categorie obligatorie are cinci variante;
- toate placeholder-ele apar în lista aprobată;
- nu există acolade neînchise;
- nu există nume personale introduse direct;
- nu există câmpuri goale;
- nu există secvențe precum `Ã`, `Å` sau `È` produse de codificare greșită;
- toate domeniile numerice sunt complete;
- profilurile de asamblare respectă intervalul de cuvinte.

### Cazuri editoriale obligatorii

1. **Bîrsan Daniel Robert — 19.02.1998**
   - vibrație interioară `19 -> 10 -> 1`;
   - vibrație exterioară directă `2`;
   - vibrație globală `1 + 2 = 3`;
   - vibrație cosmică fixă `19`;
   - vibrație cosmică variabilă `98 -> 17 -> 8`;
   - vibrație cosmică totală `1998 -> 27 -> 9`.
2. Ziua `29`, pentru traseul `29 -> 11 -> 2`.
3. Luna `11`, pentru exprimarea exterioară `11 -> 2`.
4. Anul `1999`, pentru traseul cosmic cu mai multe praguri.
5. Anul `2000`, pentru terminația variabilă `00`.
6. O persoană cu `{prenume_activ}` diferit de primul prenume complet, precum `Vic`.
7. O persoană cu două prenume, pentru verificarea diferenței dintre `{prenume}` și `{prenume_activ}`.

## 13. Criterii de acceptare

Biblioteca este considerată completă când:

- există toate cele șase perechi JSON–Markdown;
- există fișierele comune și manifestul;
- fiecare posibilitate din intervalele stabilite este acoperită;
- fiecare modul obligatoriu are cinci variante reale, nu reformulări aproape identice;
- interpretările simulate au 650–900 de cuvinte;
- tonul este conversațional și compatibil cu modelul Daniel;
- textele nu conțin nume personale fixe;
- schimbarea fișei persoanei schimbă automat toate referirile de identitate;
- JSON-ul și Markdown-ul sunt perfect sincronizate;
- validatorul și validarea generală a skill-ului se încheie fără erori.

## 14. Limitele acestei etape

- Se construiesc biblioteca, documentația, generatorul Markdown și validatorul.
- Nu se implementează încă selectorul final de expresii.
- Nu se modifică lucrările existente prin înlocuirea automată a interpretărilor.
- Nu se extinde intervalul cosmic dincolo de `1900–2099`.
- Nu se dublează textele pentru masculin și feminin; formulările rămân neutre.
- Sursa canonică este skill-ul local Atlas. Publicarea copiei globale se face numai la o cerere separată.


---
titlu: Contracte pentru tabelele lucrării scurte
tip: referinta-skill
status: activa
skill: numerologie-lucrare-redactare
tags:
  - skill
  - numerologie
  - lucrare-scurta
  - tabele
---

# Contracte pentru tabelele lucrării scurte

Citește această referință înainte de generarea sau revizia unei lucrări `scurt`. Modelele Daniel stabilesc structura, nu valorile personale.

## T-008 — Lecțiile de viață

- Calculează `zi x lună x an`.
- Transformă produsul în șir folosind toate cifrele, în ordine, inclusiv fiecare `0`.
- Creează câte o coloană pentru fiecare poziție din șir și distribuie anii consecutiv; repetă apoi șirul ciclic.
- Interpretează `0` prudent, ca spațiu de acumulare, deschidere sau amplificare, nu ca direcție numerică separată.
- Folosește structura `BDR-19980219-v1.00r-SUB-025a`.

## T-015 — Ciclul de 12 ani

- Folosește coloanele `Ciclu`, `Interval calendaristic`, `Vârste`, `Citire`.
- Scrie o citire distinctă pentru fiecare ciclu, potrivită etapei de viață; nu repeta aceeași formulare generică.
- Marchează integral numai rândul care conține data curentă, cu roșu și bold în Markdown și clasa `active-cycle` în HTML.
- În HTML, folosește proporția orientativă `10% / 20% / 12% / 58%`.

## T-017 — Codul Spiritului pe zi și lună

- Păstrează 31 de rânduri pentru zile și 12 coloane pentru luni.
- Lasă goale 29-31 februarie și ziua 31 din aprilie, iunie, septembrie și noiembrie.
- Colorează codurile astfel: Iubire `0-13` albastru, Rațiune `14-26` crem, Material `27-39` bej, Haruri `40-52` roz.
- Evidențiază o singură intersecție reală zi-lună.
- Marcajul persoanei folosește exclusiv `spirit-cell-highlight`, turcoaz cu text alb, identic cu `BDR-19980219-v1.00r-T-017`; nu adăuga o clasă de zonă pe același `span`.

## T-019 — Etapele Spiritului

- Folosește exact coloanele `Etapă`, `Descriere etapă`, `Subetapă`, `Lecție`, `Descriere subetapă`.
- Grupează Etapa și Descrierea etapei cu `rowspan` când etapa conține mai multe subetape.
- Aplică `current-row` exclusiv subetapei calculate pentru persoana curentă.
- Folosește structura `BDR-19980219-v1.00r-T-019`, fără evidențiere moștenită de la persoana-model.

## Validare

Rulează `scripts/validate_scurt_contract.py` cu valorile persoanei. Pentru verificarea completă a lecțiilor de viață, transmite și `--life-lessons-product`, `--birth-year` și `--current-year`.


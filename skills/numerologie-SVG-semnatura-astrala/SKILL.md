---
name: numerologie-SVG-semnatura-astrala
description: Creeaza sau adapteaza SVG-uri numerologice pentru Semnatura Astrala. Foloseste acest skill cand utilizatorul cere semnatura astrala, diagrama astrala numerologica, coduri astrale sau un SVG similar cu referinta locala.
tags: [skill]
---

# Numerologie SVG Semnatura Astrala

## Surse obligatorii

1. Consulta obligatoriu `vault/Numerologie/Semnatura Astrala.md` inainte de calcul, completarea valorilor sau interpretare.
2. Calculele pot fi incluse in acest skill, dar trebuie verificate intotdeauna cu documentatia din `vault/Numerologie/`.
3. Consulta documentele dependente mentionate in documentatia din vault, daca metoda cere date din alte capitole numerologice.
4. Foloseste `assets/reference.svg` doar ca referinta vizuala pentru schema, cromatica, tipografie si pozitionari.
5. Daca exista conflict intre asset, calculele din skill si documentatia din vault, documentatia din vault are prioritate pentru metoda, valori si interpretare.

## Workflow

1. Citeste `vault/Numerologie/Semnatura Astrala.md` si documentele dependente necesare pentru datele furnizate.
2. Stabileste valorile semnaturii astrale conform metodei din documentatie.
3. Foloseste `assets/reference.svg` ca sablon de compozitie, nu ca sursa principala de calcul.
4. Pastreaza forma principala, distributia nodurilor si modul de etichetare din referinta.
5. Actualizeaza valorile calculate doar pe baza datelor furnizate si verificate cu documentatia din `vault/Numerologie/`.
6. Nu introduce elemente decorative noi daca nu ajuta calculul sau lizibilitatea.
7. Salveaza SVG-ul rezultat in `vault/Numerologie/` sau in calea ceruta de utilizator.
8. Verifica SVG-ul ca XML valid si inspecteaza vizual alinierea, suprapunerile si contrastul.
9. Verifica matematic valorile finale cu baza din `vault/Numerologie/Semnatura Astrala.md`.

## Regula watermark

- Fiecare SVG final trebuie sa includa watermark-ul `Atlas Numerologie` in coltul dreapta jos al panzei SVG.
- Stil recomandat, discret si consecvent cu septagrama validata: `font-family="Arial, Helvetica, sans-serif"`, `font-size="14"`, `fill="#aaa"`, `font-weight="800"`, `text-anchor="end"`.
- Pozitionare recomandata: `x = latime_viewBox - 20`, `y = inaltime_viewBox - 15`. Pentru SVG-uri cu margini sau continut special, pastreaza watermark-ul in interiorul panzei, fara sa atinga rama sau elementele principale.
- Textul trebuie scris exact `Atlas Numerologie`, nu cu majuscule integrale.

## Reference
- `vault/Numerologie/Semnatura Astrala.md` este sursa de adevar pentru metoda, formule, valori si interpretare.
- `assets/reference.svg` este modelul validat pentru aspectul vizual al Semnaturii Astrale.

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
3. Construieste traseul din cifrele reale ale CNP-ului astral/codului folosit, in ordinea lor exacta.
4. Mapeaza cifrele `1-9` pe centrele casutelor din patratul lui Pitagora: `1,4,7` sus, `2,5,8` la mijloc, `3,6,9` jos.
5. Pastreaza cifra `0` in textul calculului, dar nu o trasa geometric, pentru ca nu are casuta in patratul `1-9`.
6. Daca doua cifre consecutive sunt identice, pastreaza repetitia in traseul afisat si marcheaza stationarea discret, fara sa inventezi un segment fals.
7. Grupeaza segmentele suprapuse; daca acelasi segment apare de mai multe ori, inclusiv in sens invers, linia trebuie ingrosata proportional cu numarul de treceri.
8. Foloseste `assets/reference.svg` ca sablon de compozitie, nu ca sursa principala de calcul.
9. Pastreaza forma principala, distributia nodurilor si modul de etichetare din referinta.
10. Actualizeaza valorile calculate doar pe baza datelor furnizate si verificate cu documentatia din `vault/Numerologie/`.
11. Nu introduce elemente decorative noi daca nu ajuta calculul sau lizibilitatea.
12. Salveaza SVG-ul rezultat in `vault/Numerologie/` sau in calea ceruta de utilizator.
13. Verifica SVG-ul ca XML valid si inspecteaza vizual alinierea, suprapunerile si contrastul.
14. Verifica matematic valorile finale cu baza din `vault/Numerologie/Semnatura Astrala.md`.
15. Verifica explicit ca punctele sau segmentele din SVG corespund cu textul `Traseu folosit`.

## Regula watermark

- Fiecare SVG final trebuie sa includa watermark-ul `Atlas Numerologie` in coltul dreapta jos al panzei SVG.
- Stil recomandat, discret si consecvent cu septagrama validata: `font-family="Arial, Helvetica, sans-serif"`, `font-size="14"`, `fill="#aaa"`, `font-weight="800"`, `text-anchor="end"`.
- Pozitionare recomandata: `x = latime_viewBox - 20`, `y = inaltime_viewBox - 15`. Pentru SVG-uri cu margini sau continut special, pastreaza watermark-ul in interiorul panzei, fara sa atinga rama sau elementele principale.
- Textul trebuie scris exact `Atlas Numerologie`, nu cu majuscule integrale.

## Reference
- `vault/Numerologie/Semnatura Astrala.md` este sursa de adevar pentru metoda, formule, valori si interpretare.
- `assets/reference.svg` este modelul validat pentru aspectul vizual al Semnaturii Astrale.

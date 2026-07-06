---
name: numerologie-SVG-soarta-si-destin
description: Creeaza sau adapteaza SVG-uri numerologice pentru graficul Soarta si Destin. Foloseste acest skill cand utilizatorul cere grafic soarta/destin, linia sortii, linia destinului, zona de confort, puncte de intalnire sau comparatia numerelor grafice de 7 cifre.
tags: [skill]
---

# Numerologie SVG Soarta si Destin

## Surse obligatorii

1. Consulta obligatoriu `vault/Numerologie/Soarta si Destin.md` inainte de calcul, completarea valorilor sau interpretare.
2. Verifica data de nastere si formulele pentru `soarta` si `destin grafic`.
3. Daca exista conflict intre calcule, asset sau textul generat, documentatia din vault are prioritate.

## Asset de referinta

- Foloseste `assets/reference.svg` ca referinta vizuala principala pentru compozitie, paleta, legenda, pozitionarea axelor si sinteza de jos.
- Assetul de referinta trebuie pastrat sincronizat cu ultimele reguli: axa orizontala foloseste marcaje de varsta (`0`, `10`, `20` sau `0`, `12`, `24`), nu intervale cu cratima; zonele de confort sunt desenate prin linii punctate, iar valorile lor apar doar in legenda laterala.
- Cand creezi un SVG nou, adapteaza datele, calculele, marcajul de varsta si sinteza, dar pastreaza structura vizuala din `assets/reference.svg`.

## Workflow

1. Calculeaza `soarta = ZZLL x AAAA`.
2. Calculeaza `destin = ZZLL_ajustat x AAAA_ajustat`, unde fiecare 0 din data folosita in grafic se inlocuieste cu 1.
3. Pastreaza ambele rezultate ca numere grafice de 7 cifre, cu zero in fata daca este nevoie.
4. Calculeaza zona de confort pentru fiecare linie:

```text
zona_de_confort = suma_cifrelor(numar_grafic) / 7
```

5. Deseneaza un SVG landscape cu fundal integral de culoarea hartiei vechi, in acord cu lucrarea. Nu pune graficul intr-un chenar alb care rupe textura vizuala.
6. Axa verticala trebuie sa afiseze toate cifrele de la 0 la 9, nu doar repere rare.
7. Axa orizontala trebuie sa afiseze marcaje de varsta, nu intervale scrise cu cratima. Alege pasul dupa regula din documentatie: `0`, `10`, `20`, `30`, `40`, `50`, `60` etc. pentru predominanta impara / masculina sau `0`, `12`, `24`, `36`, `48`, `60`, `72` etc. pentru predominanta para / feminina.
8. Reprezinta linia sortii si linia destinului ca polilinii distincte, cu puncte pe fiecare cifra.
9. Marcheaza zona de confort prin linii orizontale punctate, cate una pentru Soarta si una pentru Destin. Daca valorile coincid, separa vizual liniile foarte putin. Nu pune etichete de text langa liniile din zona graficului; valorile zonelor de confort se trec doar in legenda laterala.
10. Eticheteaza fiecare punct cu cifra corespunzatoare si marcajul de varsta.
11. Include legenda, formulele scurte si concluzia vizuala: intervalul folosit si motivul lui, apropiere, diferenta, puncte de intalnire si puncte de rascruce.
12. Salveaza SVG-ul in calea lucrarii sau in calea ceruta de utilizator.
13. Verifica SVG-ul ca XML valid si inspecteaza lizibilitatea etichetelor.

## Regula watermark

- Fiecare SVG final trebuie sa includa watermark-ul `Atlas Numerologie` in coltul dreapta jos al panzei SVG.
- Stil recomandat, discret si consecvent cu septagrama validata: `font-family="Arial, Helvetica, sans-serif"`, `font-size="14"`, `fill="#aaa"`, `font-weight="800"`, `text-anchor="end"`.
- Pozitionare recomandata: `x = latime_viewBox - 20`, `y = inaltime_viewBox - 15`. Pentru SVG-uri cu margini sau continut special, pastreaza watermark-ul in interiorul panzei, fara sa atinga rama sau elementele principale.
- Textul trebuie scris exact `Atlas Numerologie`, nu cu majuscule integrale.

## Interpretare

- Punctele egale intre soarta si destin arata zone de intalnire intre cadrul primit si directia de implinire.
- Diferentele mici arata treceri usoare.
- Diferentele mari arata zone unde persoana trebuie sa aleaga, sa invete sau sa urce constient.
- Zona de confort sub linie poate indica pasivitate sau presiune joasa; peste zona de confort apare efortul de crestere.

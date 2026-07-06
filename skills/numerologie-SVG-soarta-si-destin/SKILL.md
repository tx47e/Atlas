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

## Workflow

1. Calculeaza `soarta = ZZLL x AAAA`.
2. Calculeaza `destin = ZZLL_ajustat x AAAA_ajustat`, unde fiecare 0 din data folosita in grafic se inlocuieste cu 1.
3. Pastreaza ambele rezultate ca numere grafice de 7 cifre, cu zero in fata daca este nevoie.
4. Calculeaza zona de confort pentru fiecare linie:

```text
zona_de_confort = suma_cifrelor(numar_grafic) / 7
```

5. Deseneaza un SVG landscape cu axa orizontala `Pozitia 1-7` si axa verticala `Valoare 0-9`.
6. Reprezinta linia sortii si linia destinului ca polilinii distincte, cu puncte pe fiecare cifra.
7. Marcheaza zona de confort prin linii orizontale punctate, cate una pentru soarta si una pentru destin.
8. Eticheteaza fiecare punct cu cifra corespunzatoare si pozitia.
9. Include legenda, formulele scurte si concluzia vizuala: apropiere, diferenta, puncte de intalnire si puncte de rascruce.
10. Salveaza SVG-ul in calea lucrarii sau in calea ceruta de utilizator.
11. Verifica SVG-ul ca XML valid si inspecteaza lizibilitatea etichetelor.

## Interpretare

- Punctele egale intre soarta si destin arata zone de intalnire intre cadrul primit si directia de implinire.
- Diferentele mici arata treceri usoare.
- Diferentele mari arata zone unde persoana trebuie sa aleaga, sa invete sau sa urce constient.
- Zona de confort sub linie poate indica pasivitate sau presiune joasa; peste zona de confort apare efortul de crestere.

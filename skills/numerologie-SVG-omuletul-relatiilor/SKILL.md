---
name: numerologie-SVG-omuletul-relatiilor
description: Creeaza sau adapteaza SVG-uri numerologice pentru Omuletul Relatiilor. Foloseste acest skill cand utilizatorul cere numerologie SVG, omuletul relatiilor, compatibilitate de cuplu sau un SVG de relatie similar cu referinta locala.
tags: [skill]
---

# Numerologie SVG Omuletul Relatiilor

## Surse obligatorii

1. Consulta obligatoriu `vault/Numerologie/Omuletul Relatiilor.md` inainte de calcul, completarea valorilor sau interpretare.
2. Acolo se afla documentatia pentru intocmirea diagramei, pozitionarea cifrelor, interpretare, sinteza relationala si verificari.
3. Consulta documentele dependente mentionate acolo, in special `vault/Numerologie/Matricea Datei de Nastere.md`, `vault/Numerologie/Cod Numerologic Personal.md` si, daca este cazul, `vault/Numerologie/Influentele Numelui.md`.
4. Foloseste `assets/reference.svg` doar ca referinta vizuala pentru schema clasica, cu omulet schitat, culori, proportii si pozitionari.
5. Foloseste `assets/reference-pentagrama-only.svg` ca referinta vizuala cand utilizatorul cere varianta fara omuletul schitat: doar pentagrama, valorile celor doua persoane pozitionate in exteriorul pentagramei si fara totaluri langa cifre.
6. Daca exista conflict intre asset si documentatia din vault, documentatia din vault are prioritate pentru metoda, valori si interpretare.

## Logica de calcul din documentatie

1. Omuletul relatiilor este o diagrama comparativa construita din cifrele deja calculate pentru persoanele analizate.
2. Aceeasi sursa de cifre trebuie folosita pentru toate persoanele comparate: data nasterii, matricea personala, matricea numelui sau alt set ales explicit.
3. Pozitiile cifrelor pe pentagrama se pastreaza constant:

| Cifra | Pozitie in diagrama |
| --- | --- |
| 1 | varful de sus al pentagramei |
| 2 | coltul interior din dreapta sus |
| 3 | coltul exterior din dreapta |
| 4 | coltul interior din dreapta jos |
| 5 | coltul exterior de jos |
| 6 | centrul pentagramei, punctul de intersectie |
| 7 | coltul exterior din stanga jos |
| 8 | coltul interior din stanga jos |
| 9 | coltul exterior din stanga |
| 0 | coltul interior din stanga sus |

4. Pentru fiecare cifra noteaza cantitatea pe persoana, totalul relatiei, cine sustine cifra si zonele slabe sau absente.
5. `Ce se poate realiza impreuna` se calculeaza prin adunarea vibratiilor interioare reduse si reducere numerologica.
6. `Ce este de rezolvat impreuna` se calculeaza prin diferenta absoluta a vibratiilor interioare reduse pentru doua persoane; pentru trei persoane se calculeaza diferentele pe perechi.
7. Elementele se totalizeaza astfel: Foc = 1 + 5 + 9, Apa = 2 + 6, Aer = 3 + 7, Pamant = 4 + 8, iar 0 ramane Potential separat.

## Workflow

1. Citeste `vault/Numerologie/Omuletul Relatiilor.md` si documentele dependente necesare pentru datele furnizate.
2. Stabileste explicit sursa cifrelor folosita pentru toate persoanele comparate.
3. Calculeaza distributia cifrelor, totalurile relationale, sinteza pe elemente si cele doua rezultate de sinteza.
4. Foloseste `assets/reference.svg` ca sablon de compozitie clasica, nu ca sursa principala de calcul.
5. Pentru o diagrama fara omulet, foloseste `assets/reference-pentagrama-only.svg` ca sablon de compozitie: pastreaza pentagrama, cercul si patratul, elimina cifrele incercuite ale pozitiilor, evita totalurile langa fiecare cifra si aseaza valorile persoanelor in exteriorul pentagramei, aproape de coltul interior sau exterior corespunzator, fara suprapunere peste linii.
6. Pastreaza structura omuletului/amuletului, legaturile dintre valori si ordinea zonelor.
7. Actualizeaza numele, datele si valorile numerologice ale persoanelor cand sunt furnizate.
8. Daca lipsesc date pentru o persoana, marcheaza explicit campurile ca `de completat`.
9. Salveaza SVG-ul rezultat in `vault/Numerologie/` sau in calea ceruta de utilizator.
10. Verifica SVG-ul ca XML valid si inspecteaza vizual ca liniile, nodurile si textele sa fie lizibile.
11. Verifica matematic distributiile, totalurile pe cifra, totalurile pe elemente si sintezele relationale.

## Reference

- `vault/Numerologie/Omuletul Relatiilor.md` este sursa de adevar pentru metoda, pozitionari numerologice, formule, interpretare si verificari.
- `assets/reference.svg` este modelul validat pentru aspectul vizual al Amuletului/Omuletului Relatiilor.
- `assets/reference-pentagrama-only.svg` este modelul validat pentru varianta fara omulet schitat, doar cu pentagrama si valorile persoanelor in exterior.

---
name: numerologie-SVG-septagrama
description: Creeaza sau adapteaza SVG-uri numerologice pentru Septagrama ciclului de 7 ani. Foloseste acest skill cand utilizatorul cere septagrama, cicluri de 7 ani, momente de criza, sens de curgere sau un SVG numerologic similar cu referinta locala.
tags: [skill]
---

# Numerologie SVG Septagrama

## Surse obligatorii

1. Consulta obligatoriu `vault/Numerologie/Septagrama.md` inainte de calcul, completarea valorilor sau interpretare.
2. Calculele pot fi incluse in acest skill, dar trebuie verificate intotdeauna cu documentatia din `vault/Numerologie/`.
3. Consulta documentele dependente mentionate in documentatia din vault, daca metoda cere date din cicluri, momente de criza sau alte capitole numerologice.
4. Foloseste `assets/reference.svg` doar ca referinta vizuala pentru compozitie, stil, proportii, sageti si pozitionari.
5. Daca exista conflict intre asset, calculele din skill si documentatia din vault, documentatia din vault are prioritate pentru metoda, valori si interpretare.

## Workflow

1. Citeste `vault/Numerologie/Septagrama.md` si documentele dependente necesare pentru datele furnizate.
2. Stabileste valorile, ciclurile, varstele si sensul de curgere conform metodei din documentatie.
3. Foloseste `assets/reference.svg` ca sablon de compozitie, nu ca sursa principala de calcul.
4. Pastreaza structura generala: panza landscape, septagrama centrala, noduri portocalii, sageti de curgere, etichete de varsta si blocuri text laterale.
5. Recalculeaza textul pentru persoana ceruta cand sunt furnizate data nasterii si anii de referinta; altfel pastreaza campurile ca locuri de completat.
6. Marcheaza cu verde doar ciclul actual de 7 ani in care se afla persoana la data de referinta a lucrarii. Nu copia marcajul verde din `assets/reference.svg`: acela este doar un exemplu vizual si poate apartine altei persoane.
7. Daca un bloc vizual contine doua cicluri pe aceeasi pozitie, coloreaza in verde numai randurile ciclului activ; celalalt ciclu ramane cu stil normal.
8. Pastreaza fonturi simple de tip Arial/Helvetica, contrast bun, sageti vizibile si etichete care nu intersecteaza liniile.
9. Salveaza SVG-ul rezultat in `vault/Numerologie/` sau in calea ceruta de utilizator.
10. Verifica SVG-ul ca XML valid si inspecteaza vizual incadrarea, suprapunerile, sagetile si lizibilitatea.
11. Verifica matematic valorile finale cu baza din `vault/Numerologie/Septagrama.md`.

## Reference

- `vault/Numerologie/Septagrama.md` este sursa de adevar pentru metoda, formule, valori si interpretare.
- `assets/reference.svg` este septagrama validata vizual si trebuie folosita ca model local.
- Cand modifici geometria, pastreaza traseul de septagrama regulata si sensul de curgere.
- Cand modifici textul, evita diacriticele daca fisierul existent este ASCII-only.
- Verdele indica exclusiv ciclul actual al persoanei analizate. Pentru fiecare persoana se recalculeaza ciclul activ dupa data nasterii si data de referinta; nu se pastreaza verdele din referinta.

---
name: numerologie-svg-matrita-numelui
description: Genereaza SVG-uri autonome pentru Matrita numelui folosind codul numerologic pitagoreic al numelui complet, numarul de exprimare, matricea 3x3, optimurile si geometria aparitiilor. Foloseste cand utilizatorul cere matricea sau matrita numelui, codul numerologic al numelui in forma grafica ori compararea structurii numelui cu optimul.
---

# Matrita numelui

## Workflow

1. Primeste numele complet, data nasterii si calea SVG de iesire.
2. Ruleaza exclusiv `scripts/generate_matrita_numelui.py`.
3. Valideaza rezultatul ca XML si confirma codul numelui si numarul de exprimare.
4. Livreaza SVG-ul autonom; nu modifica manual rezultatul.

## Comanda

```powershell
python scripts/generate_matrita_numelui.py `
  --name "Birsan Daniel Robert" `
  --birth-date "19.02.1998" `
  --output "matrita-numelui-birsan-daniel-robert.svg"
```

## Calcul

- Normalizeaza diacriticele si foloseste alfabetul pitagoreic: `AJS=1`, `BKT=2`, `CLU=3`, `DMV=4`, `ENW=5`, `FOX=6`, `GPY=7`, `HQZ=8`, `IR=9`.
- Codul numelui este sirul valorilor tuturor literelor numelui complet.
- Calculeaza numarul de exprimare prin reducerea sumei reducerilor componentelor numelui la o cifra.
- Introdu numarul de exprimare in matrice dupa cifrele codului, conform calculatorului numerologic agregat.
- Exclude zerourile, numara cifrele 1–9 si foloseste ordinea `1-4-7 / 2-5-8 / 3-6-9`.
- Afiseaza in stanga sus a fiecarei casute `data` si cifrele corespunzatoare din Matrita datei de nastere.
- Afiseaza optimurile `111, 44, 7 / 222, 55, 8 / 333, 66, 9`.

## Geometrie

- Stabileste figura exclusiv din cantitatea cifrei in Matrita numelui, adica din valoarea centrala a casutei. Eticheta `data` este doar reper comparativ si nu controleaza figura.
- 0 aparitii: fara figura; 1: cerc; 2: doua cercuri legate; 3: triunghi; 4: patrat.
- 5: pentagrama; 6: hexagrama; 7: septagrama; 8: octogon.
- De la 9 in sus, foloseste poligonul regulat cu acelasi numar de laturi si denumirea lui numerica.
- Test de regresie Daniel: in casuta `9`, valoarea numelui este `99999`; fiind cinci aparitii ale cifrei `9`, figura obligatorie este pentagrama. Nu folosi patratul rezultat din cele patru aparitii afisate in reperul `data 9999`.

## Compararea matricei numelui cu matricea datei

1. Calculeaza separat matricea datei de nastere si matricea numelui.
2. Compara pentru fiecare casuta `1-9` cantitatea din nume cu cea din data.
3. Marcheaza drept sustinuta o casuta prezenta in ambele matrici.
4. Marcheaza drept exces in nume orice diferenta `nume - data >= 2`. Interpreteaza excesul ca dorinta interioara de a manifesta mai mult tema cifrei decat ofera structura nativa; nu construi o matrice separata.
5. Marcheaza drept lipsa in nume o cifra prezenta in data si absenta din nume. Interpreteaz-o ca impresia interioara ca persoana are mai putin din acea caracteristica decat ii este dat nativ.
6. Marcheaza drept potential de nume o cifra prezenta in nume si absenta din data. O astfel de casuta poate fi simultan potential de nume si exces daca diferenta este de cel putin `2`.
7. Citeste diferentele de `0` sau `1` ca sustinere ori nuantare, nu ca exces major.
8. Compara si cifrele dominante si vectorii activi, numind fiecare vector: `123, Energie`; `456, Vointa`; `789, Creativitate`; `147, Spiritualitate`; `258, Social`; `369, Bunastare materiala`; `159, Cariera`; `357, Scopuri`.

Raporteaza explicit: dominantele din data si nume, casutele sustinute, excesele in nume, lipsurile din nume, potentialele de nume si vectorii activi in fiecare matrice.

## Verificare

```powershell
[xml](Get-Content -Raw "matrita-numelui-birsan-daniel-robert.svg") | Out-Null
python scripts/test_generate_matrita_numelui.py
```

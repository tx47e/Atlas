---
name: numerologie-SVG-matrita-datei-de-nastere
description: Genereaza SVG-uri autonome pentru Matrita datei de nastere din Codul Numeric Personal, cu matricea 3x3, optimul fiecarei casute si geometria determinata de numarul aparitiilor. Foloseste cand utilizatorul cere matricea sau matrita datei de nastere, psihomatricea numerologica ori reprezentarea SVG a cifrelor datei si numerelor de lucru.
---

# Matrita datei de nastere

## Workflow

1. Primeste numele, data nasterii si calea SVG de iesire.
2. Ruleaza exclusiv `scripts/generate_matrita_datei_de_nastere.py`.
3. Pentru o lucrare, cere si `--component-output`; insereaza componenta produsa imediat dupa indexul `G-002`, fara reconstructie manuala.
4. Include [stilul componentei](assets/matrix-component.css) in CSS-ul HTML al lucrarii.
5. Valideaza SVG-ul ca XML, cele noua celule ale componentei si numerele de lucru.
6. Consulta [modelele Daniel si Andreea](references/modele/index.md) cand verifici aspectul.

## Comanda

```powershell
python scripts/generate_matrita_datei_de_nastere.py `
  --name "Birsan Daniel Robert" `
  --birth-date "19.02.1998" `
  --output "matrita-datei-birsan-daniel-robert.svg" `
  --component-output "matrita-datei-birsan-daniel-robert-g-002.html"
```

## Calcul

- Construieste data compacta `ZZLLAAAA`.
- Calculeaza `N1` ca suma cifrelor datei.
- Calculeaza `N2` prin insumarea cifrelor lui `N1` exact o singura data; pastreaza rezultatul compus, de exemplu `39 -> 12`.
- Calculeaza `N3 = N1 - 2 × prima cifra nenula a zilei`.
- Calculeaza `N4` prin insumarea cifrelor lui `N3` exact o singura data.
- Construieste sirul `data + N1 + N2 + N3 + N4`, exclude zerourile si numara cifrele 1–9.
- Foloseste ordinea matricei `1-4-7 / 2-5-8 / 3-6-9` si optimurile `111, 44, 7 / 222, 55, 8 / 333, 66, 9`.

## Geometrie

- 0 aparitii: fara figura; 1: cerc; 2: doua cercuri legate; 3: triunghi; 4: patrat.
- 5: pentagrama; 6: hexagrama; 7: septagrama; 8: octogon.
- Hexagrama se construieste din doua triunghiuri echilaterale concentrice, unul orientat in sus si unul rotit la 180 de grade. Bazele triunghiurilor raman in interiorul formei si nu se apropie de varfurile opuse, pentru ca simbolul sa nu arate ca o clepsidra. Deseneaza figura mai mica decat limita maxima a spatiului grafic, cu o margine de siguranta vizibila pe toate laturile; toate cele sase varfuri si grosimea conturului raman integral in interiorul casutei.
- De la 9 in sus, foloseste poligonul regulat cu acelasi numar de laturi si denumirea lui numerica.

## Componenta pentru lucrare

- Foloseste exact clasele `matrix-grid matrix-grid-outlined`, `matrix-cell`, `matrix-number`, `matrix-main`, `matrix-opt` si `matrix-geom` generate de script.
- Centreaza grila, pastreaza conturul auriu, raza de `5px`, umbra discreta si fundalul elementului pentru fiecare casuta.
- Pune geometria in coltul dreapta-jos. Nu lasa niciun varf sa atinga sau sa depaseasca `viewBox`-ul compact `0 0 40 32`.
- Pentru doua aparitii, linia dintre cercuri nu intra in cercuri. Pentru trei aparitii foloseste triunghiul. Pentru sase aparitii foloseste hexagrama compacta validata in modelul Andreea.
- Nu copia valori din modele; genereaza din nou datele persoanei.

## Verificare

```powershell
[xml](Get-Content -Raw "matrita-datei-birsan-daniel-robert.svg") | Out-Null
python scripts/test_generate_matrita_datei_de_nastere.py
```

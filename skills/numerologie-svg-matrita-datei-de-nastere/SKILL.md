---
name: numerologie-svg-matrita-datei-de-nastere
description: Genereaza SVG-uri autonome pentru Matrita datei de nastere din Codul Numeric Personal, cu matricea 3x3, optimul fiecarei casute si geometria determinata de numarul aparitiilor. Foloseste cand utilizatorul cere matricea sau matrita datei de nastere, psihomatricea numerologica ori reprezentarea SVG a cifrelor datei si numerelor de lucru.
---

# Matrita datei de nastere

## Workflow

1. Primeste numele, data nasterii si calea SVG de iesire.
2. Ruleaza exclusiv `scripts/generate_matrita_datei_de_nastere.py`.
3. Valideaza rezultatul ca XML si confirma numerele de lucru si sirul complet.
4. Livreaza SVG-ul autonom; nu modifica manual rezultatul.

## Comanda

```powershell
python scripts/generate_matrita_datei_de_nastere.py `
  --name "Birsan Daniel Robert" `
  --birth-date "19.02.1998" `
  --output "matrita-datei-birsan-daniel-robert.svg"
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
- De la 9 in sus, foloseste poligonul regulat cu acelasi numar de laturi si denumirea lui numerica.

## Verificare

```powershell
[xml](Get-Content -Raw "matrita-datei-birsan-daniel-robert.svg") | Out-Null
```


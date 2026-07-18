---
name: numerologie-SVG-semnatura-astrala
description: Creeaza SVG-uri autonome pentru Semnatura Astrala. Foloseste acest skill cand utilizatorul cere semnatura astrala, diagrama astrala numerologica sau coduri astrale.
tags: [skill]
---

# Numerologie SVG Semnatura Astrala

## Sursa operationala

- Foloseste exclusiv `scripts/generate_semnatura_astrala.py` pentru calcule si generare.
- Scriptul construieste CNP-ul astral `ZZLLAAAA + N1 + N2 + N3 + N4`, traseul fara cifrele `0`, centrul de rotire si multiplicarea dupa destin.
- Calculeaza `N2` printr-o singura insumare a cifrelor lui `N1`. Pastreaza un rezultat format din doua cifre: pentru `N1 = 39`, `N2 = 12`, nu `3`.
- Calculeaza `N4` printr-o singura insumare a cifrelor lui `N3`. Pastreaza un rezultat format din doua cifre: pentru `N3 = 37`, `N4 = 10`, nu `1`.
- Nu confunda `N2` cu vibratia destinului: `N2` ramane in CNP-ul astral, iar numarul de rotiri se calculeaza separat prin reducerea lui `N1` la o cifra (`39 -> destin 3`).
- Segmentele parcurse de mai multe ori, inclusiv in sens invers, sunt grupate si ingrosate proportional.
- Nu consulta `vault/Numerologie/` si nu cere verificare manuala suplimentara la fiecare rulare.

## Workflow

1. Primeste numele complet, data nasterii si calea SVG-ului de iesire.
2. Ruleaza `scripts/generate_semnatura_astrala.py`.
3. Livreaza SVG-ul generat de script fara recalcul manual.

## Script de generare

```powershell
python skills/numerologie-SVG-semnatura-astrala/scripts/generate_semnatura_astrala.py `
  --name "Nume Prenume" `
  --birth-date "19.02.1998" `
  --output "output/lucrari/YYYY-MM-DD-NUME/semnatura-astrala-nume.svg"
```

## Sincronizare periodica

Verifica separat, doar cand este programata o actualizare a metodei, concordanta dintre script, `assets/reference.svg` si documentatia numerologica. Aceasta sincronizare nu face parte din generarea curenta.

## Regula watermark

- Include watermark-ul `Atlas Numerologie` in coltul dreapta jos al panzei SVG.
- Foloseste `font-family="Arial, Helvetica, sans-serif"`, `font-size="14"`, `fill="#aaa"`, `font-weight="800"`, `text-anchor="end"`.

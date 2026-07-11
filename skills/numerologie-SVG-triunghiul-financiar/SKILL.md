---
name: numerologie-SVG-triunghiul-financiar
description: Creeaza sau adapteaza SVG-uri numerologice pentru Triunghiul Financiar. Foloseste acest skill cand utilizatorul cere triunghi financiar, diagrama financiara numerologica, laturi/pozitii financiare sau un SVG similar cu referinta locala.
tags: [skill]
---

# Numerologie SVG Triunghiul Financiar

## Sursa operationala

- Foloseste exclusiv `scripts/generate_triunghi_financiar.py` pentru calcule si generare.
- Scriptul este autonom: primeste numele si data nasterii, calculeaza codul `ZLAD` si genereaza SVG-ul in compozitia stabilita.
- Nu consulta `vault/Numerologie/` si nu face o verificare manuala suplimentara la fiecare rulare.
- `assets/reference.svg` ramane modelul vizual incorporat in structura scriptului, nu o sursa de calcul consultata la rulare.

## Workflow

1. Primeste numele complet, data nasterii si calea SVG-ului de iesire.
2. Ruleaza `scripts/generate_triunghi_financiar.py`.
3. Livreaza SVG-ul generat de script, fara recalcul manual sau verificare suplimentara.

## Script de generare

Scriptul principal pentru generarea automata este:

```powershell
python skills/numerologie-SVG-triunghiul-financiar/scripts/generate_triunghi_financiar.py `
  --name "Nume Prenume" `
  --birth-date "27.11.1973" `
  --output "output/lucrari/YYYY-MM-DD-NUME/triunghiul-financiar-nume.svg"
```

Scriptul calculeaza:

```text
Z = ziua nasterii redusa la o cifra
L = luna nasterii redusa la o cifra
A = anul nasterii redus la o cifra
D = Z + L + A, redus la o cifra
Triunghiul financiar = ZLAD
```

Scriptul contine formula, coordonatele, paleta, watermark-ul si structura SVG necesare. La o rulare reusita, rezultatul scriptului este livrabil fara verificari suplimentare.

## Sincronizare periodica

Verifica separat, doar cand este programata o actualizare a metodei, concordanta dintre script, `assets/reference.svg` si `vault/Numerologie/Triunghiul Financiar.md`. Aceasta sincronizare nu face parte din generarea curenta a unui SVG.

## Regula watermark

- Fiecare SVG final trebuie sa includa watermark-ul `Atlas Numerologie` in coltul dreapta jos al panzei SVG.
- Stil recomandat, discret si consecvent cu septagrama validata: `font-family="Arial, Helvetica, sans-serif"`, `font-size="14"`, `fill="#aaa"`, `font-weight="800"`, `text-anchor="end"`.
- Pozitionare recomandata: `x = latime_viewBox - 20`, `y = inaltime_viewBox - 15`. Pentru SVG-uri cu margini sau continut special, pastreaza watermark-ul in interiorul panzei, fara sa atinga rama sau elementele principale.
- Textul trebuie scris exact `Atlas Numerologie`, nu cu majuscule integrale.

## Reference
- `assets/reference.svg` este modelul validat pentru aspectul vizual al Triunghiului Financiar.

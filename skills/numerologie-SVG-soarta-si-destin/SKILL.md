---
name: numerologie-SVG-soarta-si-destin
description: Creeaza SVG-uri numerologice autonome pentru graficul Soarta si Destin. Foloseste acest skill cand utilizatorul cere grafic soarta/destin, linia sortii, linia destinului, zona de confort, puncte de intalnire sau comparatia numerelor grafice de 7 cifre.
---

# Numerologie SVG Soarta si Destin

## Sursa operationala

- Foloseste exclusiv `scripts/generate_soarta_si_destin.py` pentru calcule si generare.
- Scriptul primeste numele si data nasterii si contine formula, alegerea intervalului, coordonatele, paleta, legenda, sinteza si watermark-ul.
- Nu consulta `vault/Numerologie/` si nu face o verificare manuala suplimentara la fiecare rulare.
- `assets/reference.svg` ramane modelul vizual incorporat in structura scriptului, nu o sursa de calcul consultata la rulare.

## Workflow

1. Primeste numele complet, data nasterii si calea SVG-ului de iesire.
2. Ruleaza `scripts/generate_soarta_si_destin.py`.
3. Livreaza SVG-ul generat de script, fara recalcul manual sau verificare suplimentara.

## Script de generare

```powershell
python skills/numerologie-SVG-soarta-si-destin/scripts/generate_soarta_si_destin.py `
  --name "Nume Prenume" `
  --birth-date "19.02.1998" `
  --output "output/lucrari/YYYY-MM-DD-NUME/soarta-si-destin-nume.svg"
```

Scriptul calculeaza:

```text
Soarta = ZZLL x AAAA
Destin = ZZLL ajustat x AAAA ajustat
ZZLL ajustat = ZZLL cu fiecare 0 inlocuit cu 1
AAAA ajustat = AAAA cu fiecare 0 inlocuit cu 1
zona de confort = suma cifrelor numarului grafic / 7
```

## Sincronizare periodica

Verifica separat, doar cand este programata o actualizare a metodei, concordanta dintre script, `assets/reference.svg` si `vault/Numerologie/Soarta si Destin.md`. Aceasta sincronizare nu face parte din generarea curenta a unui SVG.

## Regula watermark

- Include watermark-ul `Atlas Numerologie` in coltul dreapta jos al panzei SVG.
- Foloseste `font-family="Arial, Helvetica, sans-serif"`, `font-size="14"`, `fill="#aaa"`, `font-weight="800"`, `text-anchor="end"`.

## Fundal si integrare vizuala

- Foloseste pentru panza fundalul crem deschis `#fff8e8`, identic cu fundalul graficului Scara bunastarii din template-ul scurt.
- Pastreaza conturul auriu, raza de `5px` si umbra discreta la nivelul elementului `img` din lucrare; nu dubla chenarul in interiorul SVG-ului.

## Reference

- `assets/reference.svg` este modelul validat pentru aspectul vizual al graficului.

---
name: numerologie-SVG-septagrama
description: Creeaza SVG-uri autonome pentru Septagrama ciclurilor de 7 ani. Foloseste acest skill cand utilizatorul cere septagrama, cicluri de 7 ani, momente de criza sau sens de curgere.
---

# Numerologie SVG Septagrama

## Sursa operationala

- Foloseste exclusiv `scripts/generate_septagrama.py` pentru calcule si generare.
- Scriptul primeste numele, data nasterii, data de referinta si calea SVG-ului de iesire.
- Scriptul calculeaza ciclurile C1-C14, anul momentului de criza si ciclul activ pe baza varstei implinite la data de referinta.
- Varfurile septagramei sunt etichetate permanent in ordinea `1/8`, `2/9`, `3/10`, `4/11`, `5/12`, `6/13`, `7/14`.
- Marcheaza cu verde intregul bloc al ciclului activ: eticheta ciclului si randul lui descriptiv. Toate celelalte cicluri raman in stil normal.
- Nu consulta `vault/Numerologie/` si nu cere verificare manuala suplimentara la fiecare rulare.

## Workflow

1. Primeste numele complet, data nasterii, optional data de referinta si calea SVG-ului de iesire.
2. Ruleaza `scripts/generate_septagrama.py`.
3. Livreaza SVG-ul generat de script fara recalcul manual.

## Script de generare

```powershell
python skills/numerologie-SVG-septagrama/scripts/generate_septagrama.py `
  --name "Nume Prenume" `
  --birth-date "19.02.1998" `
  --reference-date "2026-07-11" `
  --output "output/lucrari/YYYY-MM-DD-NUME/septagrama-nume.svg"
```

## Sincronizare periodica

Verifica separat, doar cand este programata o actualizare a metodei, concordanta dintre script, `assets/reference.svg` si documentatia numerologica. Aceasta sincronizare nu face parte din generarea curenta.

## Regula watermark

- Include watermark-ul `Atlas Numerologie` in coltul dreapta jos al panzei SVG.
- Foloseste `font-family="Arial, Helvetica, sans-serif"`, `font-size="14"`, `fill="#aaa"`, `font-weight="800"`, `text-anchor="end"`.

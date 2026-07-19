---
name: numerologie-SVG-scara-bunastarii
description: Creeaza SVG-uri autonome pentru Scara Bunastarii, calculand cele noua casute si cei opt vectori ai Matricei datei de nastere si ordonandu-i descrescator dupa valoare. Foloseste cand utilizatorul cere Scara Bunastarii, graficul treptelor de bunastare sau vizualizarea comparativa a casutelor si vectorilor numerologici.
tags: [skill]
---

# Numerologie SVG Scara Bunastarii

## Sursa operationala

- Foloseste exclusiv `scripts/generate_scara_bunastarii.py` pentru calcul si SVG.
- Primeste numele complet si data nasterii; nu cere valori calculate manual.
- Calculeaza Codul Numeric Personal cu regula confirmata `N2 = suma cifrelor lui N1`, aplicata exact o singura data.
- Include exact noua casute si opt vectori, ordonate descrescator dupa valoare; pastreaza valorile egale grupate logic si valorile zero la baza.
- Reproduce formatul validat din lucrarea de examen Daniel: etichete distincte pentru vectori, bare orizontale raportate la maxim, culori pentru elementele casutelor si legenda elementelor.
- Consulta [specificatia modelului Daniel](references/model-daniel.md) numai cand verifici paritatea vizuala sau ordinea treptelor.

## Workflow

1. Primeste numele complet, data nasterii si calea SVG-ului de iesire.
2. Ruleaza generatorul fara recalcul manual.
3. Valideaza SVG-ul ca XML.
4. Confirma prezenta celor 17 trepte, ordinea descrescatoare, valorile si watermark-ul `Atlas Numerologie`.
5. Livreaza SVG-ul si raporteaza primele trei trepte si zonele cu valoare zero.

## Comanda

```powershell
python skills/numerologie-SVG-scara-bunastarii/scripts/generate_scara_bunastarii.py `
  --name "Birsan Daniel Robert" `
  --birth-date "19.02.1998" `
  --output "output/lucrari/1998-02-19-BIRSAN-DANIEL-ROBERT/scara-bunastarii-birsan-daniel-robert.svg"
```

## Reguli de iesire

- Genereaza un singur SVG autonom, fara dependinte externe.
- Afiseaza data, `N1`, `N2`, `N3`, `N4` si sirul complet in subtitlu.
- Foloseste bare proportionale cu valoarea maxima; pentru maxim foloseste `100%`, iar pentru zero `0%`.
- Pastreaza vectorii in teal si casutele marcate prin element: Foc, Pamant, Apa, Aer.
- Include watermark-ul `Atlas Numerologie` in coltul dreapta jos.

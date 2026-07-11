---
name: numerologie-SVG-patratul-de-aur
description: Creeaza SVG-uri autonome pentru Patratul de Aur, cu matricea 3x3, valorile calculate, sumele pe linii, coloane si diagonale si legenda elementelor. Foloseste cand utilizatorul cere patratul de aur, matrice 3x3 aurie sau traseu numerologic in patrat.
tags: [skill]
---

# Patratul de Aur

Genereaza diagrama exclusiv cu scriptul inclus. Scriptul contine metoda de
calcul, ordinea matricei, culorile, layout-ul si watermark-ul; nu consulta
vault-ul sau alta documentatie la fiecare rulare.

## Date de intrare

- Numele persoanei.
- Data de nastere in forma `ZZ.LL.AAAA`, `ZZ/LL/AAAA` sau `ZZ-LL-AAAA`.
- Calea SVG de iesire.

## Generare

Ruleaza generatorul din directorul skill-ului:

```powershell
python scripts/generate_patratul_de_aur.py `
  --name "Nume Persoana" --birth-date "19.02.1998" `
  --output "C:\cale\patratul-de-aur.svg"
```

Foloseste runtime-ul Python configurat in spatiu daca `python` nu este in PATH.
Nu modifica manual SVG-ul dupa generare; corecteaza scriptul si regenereaza.

## Calcul

1. Extrage ziua nasterii ca numar de pornire.
2. Construieste valorile in ordinea `4 -> 9 -> 2 -> 3 -> 5 -> 7 -> 8 -> 1 -> 6`.
3. Valoarea centrala este casuta `5`.
4. Suma de referinta este `centru * 3`.
5. Afiseaza toate cele 3 linii, 3 coloane si 2 diagonale cu valorile lor.

## Reguli vizuale

- Pastreaza matricea 3x3 si conturul exterior inchis.
- Pastreaza liniile interne albe si casutele echilibrate.
- Foloseste culorile elementelor: Foc pentru `1, 5, 9`, Apa pentru `2, 6`,
  Aer pentru `3, 7`, Pamant pentru `4, 8`.
- Afiseaza numerele mari cu Georgia bold; etichetele si calculele folosesc
  Arial/Helvetica.
- Pastreaza calculele pentru linii, coloane si diagonale in partea dreapta.
- Pastreaza legenda elementelor sub matrice.
- Pastreaza watermark-ul `Atlas Numerologie` in coltul dreapta jos.

## Verificare

Verifica SVG-ul generat ca XML valid. Pentru generarea uzuala nu compara manual
cu documentatie externa; sincronizarea cu documentatia se face separat, la cerere.

```powershell
[xml](Get-Content -Raw "C:\cale\patratul-de-aur.svg") | Out-Null
```

## Includere in lucrari

- In Markdown, foloseste SVG-ul ca imagine normala.
- In HTML distribuit ca fisier unic, include SVG-ul ca `data:image/svg+xml;base64,...`.

---
name: numerologie-SVG-harta-suprapusa
description: Creeaza SVG-uri autonome pentru Harta Suprapusa Soarta-Destin, cu ciclurile de 7, 9 si 12 ani, ani interiori si exteriori, lectii de viata, pinacluri, oportunitati si provocari. Foloseste cand utilizatorul cere harta suprapusa, soarta si destin suprapuse sau ciclicitati numerologice.
tags: [skill]
---

# Harta Suprapusa

Genereaza harta exclusiv cu scriptul inclus. Scriptul contine calculele,
perioada implicita de 0-108 ani, layout-ul V2, culorile si regulile de desen;
nu consulta vault-ul sau alta documentatie la fiecare rulare.

## Date de intrare

- Numele persoanei.
- Data de nastere in forma `ZZ.LL.AAAA`, `ZZ/LL/AAAA` sau `ZZ-LL-AAAA`.
- Calea SVG de iesire.
- Optional, varsta finala prin `--end-age`; valoarea implicita este `108`.

## Generare

```powershell
python scripts/generate_harta_suprapusa.py `
  --name "Birsan Daniel Robert" --birth-date "19.02.1998" `
  --output "C:\cale\harta-suprapusa.svg"
```

Nu modifica manual SVG-ul dupa generare. Corecteaza scriptul si regenereaza.

## Calcul

1. Soarta: formeaza `ZZLL`, inmulteste cu anul nasterii si completeaza la minimum 7 cifre.
2. Destin: inlocuieste fiecare `0` din `ZZLL` si an cu `1`, inmulteste si completeaza la minimum 7 cifre.
3. Repeta cifrele seriilor Soarta si Destin pentru toate punctele graficului.
4. Zona de confort: media cifrelor fiecarei serii de 7 cifre.
5. Lectii de viata: cifrele produsului `zi * luna * an`, repetate pe ani.
6. Ani interiori: aduna anual valoarea redusa a anului curent; ani exteriori: aduna suma bruta a cifrelor anului curent.
7. Pinacluri: foloseste vibratia interioara, vibratia exterioara, vibratia redusa a anului si destinul; oportunitatile si provocarile sunt cele patru valori asociate pinaclurilor.
8. Ciclurile se deseneaza la 7 ani, 9 ani si 12 ani; crizele ciclului 7 sunt la `3.5 + 7n` ani.

Foloseste `->` pentru orice afisare a unui traseu de calcul cu mai multi pasi.

## Reguli vizuale

- Pastreaza formatul V2: grafic dominant, legenda in dreapta si fundal crem deschis.
- Soarta este verde; Destinul este rosu; zona de confort foloseste aceleasi culori, punctat.
- Oportunitatea si provocarea sunt linii continue in trepte, pe intervalele pinaclurilor.
- Anii interiori si exteriori au linii punctate prin grafic si etichete rotite in culori distincte.
- Ciclul 7 foloseste triunghiuri portocalii; criza are triunghi outline cu varful in sus.
- Ciclurile 9, 12 si pinaclurile folosesc patrate visinii, albastre si, respectiv, mustar.
- Liniile verticale sunt desenate inaintea formelor si a textelor; evenimentele coincidente ingroasa linia.
- Legenda afiseaza seriile calculate pentru Soarta, Destin, Oportunitate si Provocare, plus zonele de confort si lectiile de viata.
- Pastreaza watermark-ul `Atlas Numerologie` in coltul dreapta jos.

## Verificare

Verifica SVG-ul ca XML valid. Pentru generarea uzuala nu compara manual cu
documentatie externa; sincronizarea cu documentatia se face separat, la cerere.

```powershell
[xml](Get-Content -Raw "C:\cale\harta-suprapusa.svg") | Out-Null
```

## Referinte de mentenanta

- `assets/reference.svg` este modelul vizual V2 aprobat pentru Daniel.
- `templates/harta-suprapusa-template.py` este arhiva template-ului initial; nu il folosi la generarea uzuala.

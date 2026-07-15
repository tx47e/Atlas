---
name: numerologie-SVG-omuletul-relatiilor
description: Creeaza SVG-uri autonome pentru Omuletul Relatiilor, cu distributia cifrelor din doua date de nastere, sinteza relationala si geometria Vitruviana validata. Foloseste cand utilizatorul cere omuletul relatiilor, compatibilitate de cuplu sau un SVG relational numerologic.
tags: [skill]
---

# Omuletul Relatiilor

Genereaza diagrama exclusiv cu scriptul inclus. Scriptul contine calculele,
coordonatele validate, culorile si regulile de compozitie; nu consulta vault-ul
sau alta documentatie la fiecare rulare.

## Date de intrare

- Numele si data de nastere pentru persoana A.
- Numele si data de nastere pentru persoana B.
- Calea SVG de iesire.

Accepta date in forma `ZZ.LL.AAAA`, `ZZ/LL/AAAA` sau `ZZ-LL-AAAA`.

## Generare

Ruleaza generatorul din directorul skill-ului:

```powershell
python scripts/generate_omulet_relatiilor.py `
  --name-a "Nume Persoana A" --birth-date-a "06.11.1984" `
  --name-b "Nume Persoana B" --birth-date-b "12.01.1998" `
  --output "C:\cale\omulet-relatii.svg"
```

Foloseste runtime-ul Python configurat in spatiu daca `python` nu este disponibil
in PATH. Nu modifica manual SVG-ul dupa generare; corecteaza scriptul si regenereaza.

## Calcul

1. Numara cifrele brute `0-9` din fiecare data de nastere.
2. Afiseaza la fiecare pozitie grupurile persoanei A si B, separate prin ` / `.
   In livrarea pentru lucrare, omite pozitia cand cifra lipseste din ambele date.
   Nu afisa `- / -` in lucrarea livrata si nu inventa valori.
3. Reduce ziua de nastere pentru vibratia interioara a fiecarei persoane.
4. Calculeaza realizarea impreuna: `A + B -> reducere`.
5. Calculeaza de rezolvat impreuna: `|A - B|`.
6. Totalizeaza elementele: Foc `1 + 5 + 9`, Apa `2 + 6`, Aer `3 + 7`,
   Pamant `4 + 8`, Potential `0`.

## Reguli vizuale

- Foloseste `assets/reference.svg` drept sablon unic pentru fundalul Vitruvian,
  cerc, patrat, axe si pentagrama. Nu redesena geometria independent.
- SVG-ul trebuie sa fie opac pana la toate cele patru margini, cu fundalul bej
  `#f4dcb6` aplicat si pe elementul radacina; nu lasa contur sau margine alba.
- Foloseste `assets/reference-cifre-lipsa.svg` ca referinta vizuala pentru
  etichetele pozitiilor absente. Are aceleasi persoane si date ca referinta
  principala si documenteaza fiecare cifra lipsa din ambele date cu `- / -`.
  Aceasta notatie apartine numai referintei, nu livrarii pentru lucrare.
- Pastreaza coordonatele din `POSITIONS` in script. Eticheta `6` este pozitionata
  sub pentagrama, la mijloc, fara sa atinga linii.
- Eticheta `3` este oglindita exact fata de eticheta `9` pe axa verticala
  `x=450`: `9` sta la `(151, 380)`, iar `3` la `(749, 380)`.
- Eticheta `7` sta sub si in exteriorul cercului, langa coltul stanga-jos al
  pentagramei; eticheta `5` este pozitionata oglindit in dreapta-jos.
- Afiseaza valorile persoanei A cu `#0070c9`, separatorul cu `#333333` si valorile
  persoanei B cu `#ff00b8`.
- Toate valorile din casete, inclusiv separatorul, folosesc `font-size="24"` si
  `font-weight="800"`, identic cu etichetele din varianta validata pentru Daniel.
- Dimensioneaza fiecare caseta dupa continut; nu micsora fontul pentru valori lungi.
- Ascunde etichetele mostenite din referinta pentru a preveni dublarea lor.
- Pastreaza antetul si sinteza elementelor in afara diagramei.

## Verificare

Verifica numai ca SVG-ul generat este XML valid. Pentru generarea uzuala nu compara
manual cu documentatie externa; sincronizarea cu documentatia se face separat, la cerere.

```powershell
[xml](Get-Content -Raw "C:\cale\omulet-relatii.svg") | Out-Null
```

Pentru regenerarea exclusiva a referintei cu cifre lipsa, adauga argumentul
`--show-missing-digits`. Nu folosi acest argument la generarea unei lucrari.

## PNG pentru livrare

Pastreaza SVG-ul ca sursa canonica, dar pentru lucrarea livrata genereaza si un
PNG din SVG, deoarece fisierul PNG este mult mai mic si se integreaza mai bine in
HTML-ul final.

Metoda recomandata:

```powershell
npx --yes @resvg/resvg-js-cli `
  "C:\cale\omulet-relatii.svg" `
  "C:\cale\omulet-relatii.png"
```

Verifica apoi ca PNG-ul exista si are dimensiune rezonabila:

```powershell
Get-Item "C:\cale\omulet-relatii.png" | Select-Object Name,Length
```

## Includere in lucrari

- In Markdown-ul lucrarii livrate, foloseste PNG-ul generat pentru Omuletul Relatiilor.
- In HTML distribuit ca fisier unic, include PNG-ul ca `data:image/png;base64,...`.
- Pastreaza SVG-ul langa lucrare ca sursa editabila/regenerabila.
- Pastreaza watermark-ul `Atlas Numerologie` din referinta.

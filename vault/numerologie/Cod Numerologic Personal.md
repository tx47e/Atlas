---
titlu: Cod numerologic personal
tip: concept
tags:
  - numerologie
  - matrice
  - CodNumerologicPersonal
Data: 2026-06-17
depinde de: Datele de intrare
---

---
## Descriere

Codul numerologic personal este sirul complet de cifre folosit pentru construirea [[Matricea Datei de Nastere|matricei datei de nastere]].

El nu este un calcul separat de [[Matricea Datei de Nastere]]. Este denumirea operationala pentru:

```text
data nasterii + N1 + N2 + N3 + N4
```

Daca proiectul prefera sa pastreze mai putine note, acest concept poate fi sters, iar informatia ramane in [[Matricea Datei de Nastere]].

---
## Formula de calcul

Data se scrie in forma:

```text
ZZLLAAAA
```

Se calculeaza patru numere de lucru:

```text
N1 = suma tuturor cifrelor datei
N2 = suma cifrelor lui N1, calculata exact o singura data
N3 = N1 - 2 x prima cifra nenula din ziua nasterii
N4 = suma cifrelor lui N3, calculata exact o singura data
```

Pentru `N2` si `N4`, insumarea cifrelor valorii precedente se executa exact o
singura data, chiar daca rezultatul are doua cifre. Nu se continua reducerea
pana la obtinerea unei singure cifre.

Exemplu de regula:

```text
N1 = 39
N2 = 3 + 9 = 12
N3 = 37
N4 = 3 + 7 = 10
```

In acest caz, `N2` ramane `12`, iar `N4` ramane `10`; nu se continua cu
`1 + 2 = 3`, respectiv cu `1 + 0 = 1`.

Codul numerologic personal este:

```text
cod numerologic personal = ZZLLAAAA + N1 + N2 + N3 + N4
```

Pentru matrice, se iau toate cifrele din acest sir si se elimina 0.

---
## Exemplu de calcul

Data:

```text
24.04.1982
```

Scriere numerica:

```text
24041982
```

Numere de lucru:

```text
N1 = 2 + 4 + 0 + 4 + 1 + 9 + 8 + 2 = 30
N2 = 3 + 0 = 3
N3 = 30 - (2 x 2) = 26
N4 = 2 + 6 = 8
```

Cod numerologic personal:

```text
24041982 30 3 26 8
```

Cifre introduse in [[Matricea Datei de Nastere]]:

```text
2, 4, 4, 1, 9, 8, 2, 3, 3, 2, 6, 8
```

Matrice:

```text
1   | 44 |
222 |    | 88
33  | 6  | 9
```

### Exemplul Daniel

Data:

```text
19.02.1998
```

Numere de lucru:

```text
N1 = 1 + 9 + 0 + 2 + 1 + 9 + 9 + 8 = 39
N2 = 3 + 9 = 12
N3 = 39 - (2 x 1) = 37
N4 = 3 + 7 = 10
```

Cod numerologic personal:

```text
19021998 39 12 37 10
```

Forma punctata:

```text
19.02.1998.39.12.37.10
```

---
## Observatii

- Codul numeric personal nu se interpreteaza separat de matrice.
- Cifra 0 ramane in cod, dar nu se introduce in matrice.
- N2 se obtine printr-o singura insumare a cifrelor lui N1 si poate ramane un numar format din doua cifre.
- N4 se obtine printr-o singura insumare a cifrelor lui N3 si poate ramane un numar format din doua cifre.
- Prima cifra folosita la N3 este prima cifra nenula din ziua nasterii.
- Daca nota pare redundanta, se poate sterge si se pastreaza doar explicatia din [[Matricea Datei de Nastere]].

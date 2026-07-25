---
titlu: Codul Numerologic Personal - Calcul
tip: calcul
tags:
  - numerologie
  - calcul
  - CodNumerologicPersonal
  - documentatie-modulara
sursa: '[[Cod Numerologic Personal]]'
---

# Codul Numerologic Personal - Calcul

## Statutul formulei

Formula N2 si N4 prin insumare exact o singura data este confirmata in Registru Validare Formule si este pastrata fara modificari.

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

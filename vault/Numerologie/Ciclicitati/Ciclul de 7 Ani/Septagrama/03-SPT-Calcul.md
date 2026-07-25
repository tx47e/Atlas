---
titlu: Septagrama - Calcul
tip: calcul
tags:
  - numerologie
  - ciclicitati
  - calcul
  - Septagrama
  - documentatie-modulara
sursa: '[[Septagrama]]'
---

# Septagrama - Calcul

## Statutul formulei

Metoda este preluata din nota legacy. Nu a fost lansat un audit formal nou.

## Principiu de calcul

Fiecare ciclu are 7 ani:

```text
C1 = 0-7 ani
C2 = 7-14 ani
C3 = 14-21 ani
C4 = 21-28 ani
C5 = 28-35 ani
C6 = 35-42 ani
C7 = 42-49 ani
```

Dupa C7, schema continua pe aceeasi septagrama:

```text
C8 = 49-56 ani
C9 = 56-63 ani
C10 = 63-70 ani
C11 = 70-77 ani
C12 = 77-84 ani
C13 = 84-91 ani
C14 = 91-98 ani
```

Pentru fiecare ciclu:

```text
an_start = anul_nasterii + varsta_start
an_final = anul_nasterii + varsta_final - 1
varsta_criza = varsta_start + 3,5
an_criza = anul_nasterii + floor(varsta_criza)
an_de_viata = floor(varsta_criza) + 1
```

Exemplu pentru o persoana nascuta in 1973:

```text
C1 = 1973-1979
0-7 ani
moment criza = 3,5 ani
an criza = 1977
al 4-lea an de viata
```

---

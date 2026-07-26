---
titlu: Comparatia Matricea Datei de Nastere vs Matricea Numelui - Calcul
tip: calcul
tags:
  - numerologie
  - calcul
  - ComparatieMatriceDataNume
  - documentatie-modulara
sursa: '[[vault/Numerologie/Nume/Comparatia Matricea Datei de Nastere vs Matricea Numelui/01-CMN-Index|Matricea Numelui vs Matricea Datei de Nastere]]'
---

# Comparatia Matricea Datei de Nastere vs Matricea Numelui - Calcul

## Statutul formulei

Metoda compara cele doua matrici pe fiecare casuta si nu construieste o a treia matrice. Formula este pastrata din nota legacy, fara audit formal nou.

## Formula de comparatie

```text
pentru fiecare cifra 1..9:
  data = numar_aparitii(cifra, matricea_datei_de_nastere)
  nume = numar_aparitii(cifra, matricea_numelui)
  diferenta = nume - data
```

### Statusuri

- daca `data == 0` si `nume > 0`: potential de nume fara suport nativ;
- daca `diferenta >= 2`: exces in nume;
- daca `data > 0` si `nume > 0`: sustinuta sau nuantata;
- daca `data > 0` si `nume == 0`: lipsa in nume;
- daca `data == 0` si `nume == 0`: absenta.

---

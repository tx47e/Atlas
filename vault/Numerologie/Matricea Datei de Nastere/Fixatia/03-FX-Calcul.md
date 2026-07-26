---
titlu: Fixatia - Calcul
tip: calcul
tags:
  - numerologie
  - calcul
  - Fixatia
  - documentatie-modulara
sursa: '[[vault/Numerologie/Matricea Datei de Nastere/Fixatia/01-FX-Index|Fixatia]]'
---

# Fixatia - Calcul

## Statutul formulei

Metoda este pastrata din nota legacy. Nu a fost lansat un audit formal nou in aceasta etapa.

## Formula de lucru

Se folosesc cei 8 vectori ai scarii bunastarii:

| Cod | Denumire |
| --- | --- |
| 123 | Energie |
| 456 | Vointa |
| 789 | Creativitate |
| 147 | Spiritualitate |
| 258 | Social |
| 369 | Bunastare materiala |
| 159 | Cariera |
| 357 | Scopuri |

Poate deveni fixatie numai un vector orizontal plin: `147`, `258` sau `369`.
Toate cele trei casute ale lui trebuie sa fie prezente in matrice. Vectorii
verticali si diagonali nu stabilesc fixatia.

```text
vector plin = fiecare dintre cele 3 casute are cel putin o cifra
```

Pentru stabilirea fixației se calculeaza cantitatea totala de cifre din cele trei casute:

```text
cantitate_vector = cantitate(casuta_a) + cantitate(casuta_b) + cantitate(casuta_c)
```

---

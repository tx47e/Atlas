---
titlu: Figuri Geometrice - Calcul
tip: calcul
tags:
  - numerologie
  - calcul
  - FiguriGeometrice
  - documentatie-modulara
sursa: '[[vault/Numerologie/Matricea Datei de Nastere/Figuri Geometrice/01-FG-Index|Figuri Geometrice]]'
---

# Figuri Geometrice - Calcul

## Statutul formulei

Metoda este pastrata din nota legacy. Nu a fost lansat un audit formal nou in aceasta etapa.

## Principiu de calcul

Pentru fiecare casuta din matrice se numara cate aparitii are cifra respectiva.
Cantitatea determina figura geometrica:

| Cantitate in casuta | Figura geometrica | Reprezentare |
| --- | --- | --- |
| 0 | absenta | casuta goala |
| 1 | punct / cerculet mic | un punct sau un cerculet |
| 2 | linie | doua puncte unite sau doua cerculete |
| 3 | triunghi | triunghi |
| 4 | patrat | patrat |
| 5 | pentagrama | stea cu cinci varfuri |
| 6 | hexagrama | stea cu sase varfuri |
| 7 | septagrama | stea cu sapte varfuri |
| peste 7 | poligon / stea cu numarul de varfuri corespunzator | figura construita dupa cantitate |

---

## Formula de lucru

```text
pentru fiecare cifra 1..9:
  cantitate = numar_aparitii(cifra, matricea_datei_de_nastere)
  figura = figura_geometrica_dupa_cantitate(cantitate)
```

Schema matricii ramane:

```text
1 | 4 | 7
2 | 5 | 8
3 | 6 | 9
```

---

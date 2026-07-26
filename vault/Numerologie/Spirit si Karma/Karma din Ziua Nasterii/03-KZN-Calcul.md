---
titlu: Karma din Ziua Nasterii - Calcul
tip: calcul
tags:
  - numerologie
  - calcul
  - KarmaZiuaNasterii
  - documentatie-modulara
sursa: '[[vault/Numerologie/Spirit si Karma/Karma din Ziua Nasterii/01-KZN-Index|Karma din Ziua Nasterii]]'
---

# Karma din Ziua Nasterii - Calcul

## Statutul formulei

Formula este marcata confirmata in Registru Validare Formule si este pastrata fara modificari.

## Formula de calcul

```text
functie karma_zilei_de_nastere(zi):
  arcana = 0 daca zi == 22 altfel ((zi - 1) % 22) + 1
  procent =:
    1-9   -> "spre 100%"
    10-19 -> "spre 80%"
    20-29 -> "spre 60%"
    30-31 -> "spre 40%"
  return { zi, arcana, procent }
```

Formula pastreaza ziua calendaristica in rezultat. Numai arcana este proiectata
in intervalul `0-21`, iar procentul este ales din intervalul zilei, nu din
valoarea arcanei.

### Asociere cu Arcanele Majore

| Zi | Arcana karmica |
| --- | --- |
| 1-21 | Arcana 1-21 |
| 22 | Arcana 0 - Nebunul |
| 23 | [[1-Magicianul|Arcana 1 - Magicianul]] |
| 24 | [[2-Marea Preoteasa|Arcana 2 - Marea Preoteasa]] |
| 25 | [[3-Imparateasa|Arcana 3 - Imparateasa]] |
| 26 | [[4-Imparatul|Arcana 4 - Imparatul]] |
| 27 | [[5-Marele Preot|Arcana 5 - Marele Preot]] |
| 28 | [[6-Indragostitii|Arcana 6 - Indragostitii]] |
| 29 | [[7-Carul|Arcana 7 - Carul]] |
| 30 | [[8-Puterea|Arcana 8 - Puterea]] |
| 31 | [[9-Ermitul|Arcana 9 - Ermitul]] |

### Nivelul karmei implinite

| Zile | Karma implinita |
| --- | --- |
| 1-9 | spre 100% |
| 10-19 | spre 80% |
| 20-29 | spre 60% |
| 30-31 | spre 40% |

---

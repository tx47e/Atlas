---
titlu: Karma din ziua nasterii
tip: concept
tags:
  - numerologie
  - karma
  - KarmaZiuaNasterii
Data: 2026-06-17
depinde de: Datele de intrare
---

---
## Descriere

Karma din ziua nasterii arata programul karmic indicat de ziua calendaristica a nasterii. Ziua nu se reduce la 1-9, ci se pastreaza ca valoare intre 1 si 31.

Interpretarea se face prin [[tarot/Index|Arcanele Majore]] si prin trecerea de la polaritatea negativa la solutia sau calitatea care trebuie dezvoltata.

---
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
## Interpretare generala

| Karma | Zile  | Arcana             | Cheie de lucru                                    |
| ----- | ----- | ------------------ | ------------------------------------------------- |
| 1     | 1, 23 | 1-Magicianul       | lider, concentrare, transformarea orgoliului      |
| 2     | 2, 24 | 2-Marea Preoteasa  | bunatate, ajutor, diplomatie, altruism            |
| 3     | 3, 25 | 3-Imparateasa      | talente, expresie creativa, harnicie              |
| 4     | 4, 26 | 4-Imparatul        | profesionalism, lege, generozitate, cumpatare     |
| 5     | 5, 27 | 5-Marele Preot     | smerenie, intelepciune practica                   |
| 6     | 6, 28 | 6-Indragostitii    | familie, fidelitate, alegere matura               |
| 7     | 7, 29 | 7-Carul            | stiinta, cercetare, credinta, intelect            |
| 8     | 8, 30 | 8-Puterea          | putere interioara, control, responsabilitate      |
| 9     | 9, 31 | 9-Ermitul          | cunoastere pusa in slujba celorlalti              |
| 10    | 10    | 10-Roata Norocului | folosirea corecta a oportunitatilor               |
| 11    | 11    | 11-Dreptatea       | corectitudine, lege cauza-efect, responsabilitate |
| 12    | 12    | 12-Spanzuratul     | bunatate, sacrificiu, iluminare                   |
| 13    | 13    | 13-Moartea         | transformare, eliberare, renastere                |
| 14    | 14    | 14-Cumpatarea      | masura, echilibru, recunostinta                   |
| 15    | 15    | 15-Diavolul        | cunoastere folosita corect                        |
| 16    | 16    | 16-Turnul          | constructie, impacare, bunastare comuna           |
| 17    | 17    | 17-Steaua          | smerenie, stralucire meritata                     |
| 18    | 18    | 18-Luna            | onestitate, intuitie, creativitate folositoare    |
| 19    | 19    | 19-Soarele         | inspiratie, libertate, putere responsabila        |
| 20    | 20    | 20-Judecata        | apararea neamului, culturii si traditiei          |
| 21    | 21    | 21-Lumea           | apararea patriei si valorilor nationale           |
| 22    | 22    | 0-Nebunul          | libertate, relatia cu copiii, incredere in drum   |

---
## Exemplu de calcul

### Exemplu 1

```text
zi = 24
24 -> Arcana 2 - Marea Preoteasa
karma implinita = spre 60%
```

Citire scurta: tema karmica este legata de bunatate, ajutor, diplomatie si transformarea fricii sau a inchiderii in altruism.

### Exemplu 2

```text
zi = 13
13 -> Arcana 13 - Moartea
karma implinita = spre 80%
```

Citire scurta: tema karmica este transformarea, eliberarea, renasterea si deschiderea unor drumuri noi.

---
## Observatii

- Ziua nu se reduce numerologic la 1-9.
- Zilele 23-31 reiau arcanele 1-9.
- Pentru ziua 22 se foloseste Arcana 0 - Nebunul. Se poate continua din [[tarot/Index|tarot]].

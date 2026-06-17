# Ezoterism - metoda

Metoda identifica inclinatia ezoterica a unei persoane pornind de la data reala
de nastere. Cheia calculului este impartirea datei de nastere, scrisa ca un
singur numar, la `7`.

Prima cifra de dupa virgula arata codul ezoteric principal. A doua etapa de
calcul poate indica domeniile ezoterice care se deschid mai usor.

## Date necesare

- ziua nasterii;
- luna nasterii;
- anul nasterii;
- confirmarea ca data folosita este data reala de nastere.

Daca exista diferenta intre data reala si o data administrativa gresita, in
lucrare se foloseste data reala si se noteaza explicit aceasta alegere.

## 1. Scrierea datei

Data se scrie ca un singur numar, in ordinea:

```text
zi-luna-an
```

Se elimina punctele, spatiile si separatoarele. Ziua si luna se scriu ca valori
calendaristice, fara zerouri de completare in fata. Daca ziua sau luna este mai
mica decat `10`, cifra `0` pusa doar pentru formatul calendaristic nu intra in
sirul de calcul.

Zerourile care fac parte din valoarea reala a zilei, lunii sau anului se
pastreaza. De exemplu, in `30` si `10`, cifra `0` ramane, pentru ca nu este un
zero de completare, ci parte din numarul calendaristic.

Exemple:

```text
30.10.1963 -> 30101963
06.11.1984 -> 6111984
07.04.1984 -> 741984
```

Zero-urile nu se interpreteaza separat in aceasta etapa. Ele se pastreaza numai
cand apartin numarului calendaristic propriu-zis si se elimina cand sunt doar
zerouri de completare in fata zilei sau lunii.

## 2. Impartirea principala la 7

```text
data_nasterii_scrisa_ca_numar / 7
```

Se ia prima cifra de dupa virgula.

```text
cod ezoteric principal =
  prima cifra de dupa virgula din (data_nasterii_scrisa_ca_numar / 7)
```

Exemplu:

```text
30101963 / 7 = 4300280,428571...
```

Prima cifra de dupa virgula este `4`, deci codul ezoteric principal este `4`.

## 3. Secventa 142857

Codurile posibile vin din secventa repetitiva a impartirii la `7`:

```text
142857
```

Din acest motiv, codurile principale obisnuite sunt:

```text
1, 2, 4, 5, 7, 8
```

Codul `0` apare cand impartirea este exacta sau cand prima cifra de dupa virgula
este `0`. El nu se citeste ca un cod ezoteric obisnuit, ci ca situatie speciala.

Documentul leaga secventa `142857` de logica dezvoltarii prin dublare, asociata
principiului lui `2`:

```text
1 x 2 = 2
2 x 2 = 4
4 x 2 = 8
8 x 2 = 16
16 x 2 = 32
32 x 2 = 64
64 x 2 = 128
```

Din aceasta dinamica se observa repetitia:

```text
1, 2, 4, 8, 7, 5
```

Aceasta este baza simbolica a codurilor folosite in metoda.

## 4. Tipul principal de ezoterism

| Cod principal | Tip de ezoterism |
| --- | --- |
| 2, 8 | ezoterism spiritual |
| 1, 5 | ezoterism stiintific |
| 4, 7 | ezoterism practic |
| 0 | cod special |

Pentru interpretarea ampla a fiecarui cod principal, a codului `0` si a
domeniilor secundare, se foloseste documentul
[`04-semnificatii.md`](04-semnificatii.md).

## 5. Domeniile care se deschid mai usor

Dupa stabilirea codului principal, se poate calcula si o orientare secundara.
Exceptie: daca prima impartire da cod principal `0`, calculul se opreste aici.
Nu se mai face a doua impartire si nu se forteaza un domeniu secundar.

Se ia partea intreaga obtinuta la prima impartire:

```text
partea_intreaga = partea intreaga din (data_nasterii_scrisa_ca_numar / 7)
```

Apoi se imparte aceasta parte intreaga din nou la `7`:

```text
partea_intreaga / 7
```

Rezultatul se citeste prin prima cifra de dupa virgula:

```text
cod secundar =
  prima cifra de dupa virgula din (partea_intreaga / 7)
```

Codul secundar nu inlocuieste codul principal. El se interpreteaza numai in
interiorul tipului principal de ezoterism:

- daca tipul principal este spiritual, codul secundar se cauta in domeniile
  spirituale;
- daca tipul principal este stiintific, codul secundar se cauta in domeniile
  stiintifice;
- daca tipul principal este practic, codul secundar se cauta in domeniile
  practice;
- daca tipul principal este `0`, se pastreaza prudenta si nu se forteaza un
  domeniu.

## 6. Domenii secundare

### Domenii pentru ezoterism spiritual

| Cod secundar | Domeniu |
| --- | --- |
| 8, 7 | calatorii astrale |
| 2, 5 | alchimie |
| 4, 1 | metafizica |
| 0 | filosofie |

### Domenii pentru ezoterism stiintific

| Cod secundar | Domeniu |
| --- | --- |
| 1 | astrologie |
| 2 | terapii complementare |
| 4 | simbolistica |
| 5 | chiromantie |
| 7 | numerologie |
| 8 | matrice si stiinte umane |
| 0 | fiziognomica |

### Domenii pentru ezoterism practic

| Cod secundar | Domeniu |
| --- | --- |
| 4, 5 | vrajitorie |
| 1, 2 | samanism |
| 7, 8 | magie |
| 0 | practici diverse |

## 7. Rezultat final

Rezultatul calculului se noteaza astfel:

| Camp | Valoare |
| --- | --- |
| Data reala folosita |  |
| Data scrisa ca numar |  |
| Impartirea principala la 7 |  |
| Cod ezoteric principal |  |
| Tip principal de ezoterism |  |
| Partea intreaga din prima impartire |  |
| A doua impartire la 7 |  |
| Cod secundar |  |
| Domenii care se deschid mai usor |  |
| Observatii de prudenta |  |

## Surse bibliografice interne

- `bibliography/13 - Ezoterism.md`

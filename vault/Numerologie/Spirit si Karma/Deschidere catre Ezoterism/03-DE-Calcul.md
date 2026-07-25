---
titlu: Deschidere catre Ezoterism - Calcul
tip: calcul
tags:
  - numerologie
  - calcul
  - DeschidereCatreEzoterism
  - documentatie-modulara
sursa: '[[Deschidere spre Ezoterism]]'
---

# Deschidere catre Ezoterism - Calcul

## Statutul formulei

Formula este pastrata din nota legacy. Nu a fost lansat un audit formal nou in aceasta etapa.

## Formula de calcul

Metoda are doua etape principale si o verificare intermediara:

1. codul ezoteric principal, obtinut din prima cifra de dupa virgula la impartirea datei de nastere la 7;
2. verificarea codului 0: daca data se imparte exact la 7, dupa virgula nu mai apare nicio cifra, codul se noteaza 0, iar codul secundar nu se mai calculeaza;
3. codul secundar, obtinut din prima cifra de dupa virgula la impartirea partii intregi din primul calcul la 7.

### Scrierea datei

Data se scrie ca un singur numar, in ordinea:

```text
zi-luna-an
```

Se elimina punctele, spatiile si separatoarele. Ziua si luna se scriu ca valori calendaristice, fara zerouri de completare in fata.

Exemple:

```text
30.10.1963 -> 30101963
06.11.1984 -> 6111984
07.04.1984 -> 741984
```

Zerourile care fac parte din valoarea reala a zilei, lunii sau anului se pastreaza. Zerourile puse doar pentru formatul calendaristic se elimina.

### Codul ezoteric principal

```text
cod ezoteric principal =
  prima cifra de dupa virgula din (data_nasterii_scrisa_ca_numar / 7)
```

Exemplu:

```text
30101963 / 7 = 4300280,428571...
```

Prima cifra de dupa virgula este 4, deci codul ezoteric principal este 4.

### Secventa 142857

Codurile principale obisnuite vin din secventa repetitiva a impartirii la 7:

```text
142857
```

Din acest motiv, codurile principale obisnuite sunt:

```text
1, 2, 4, 5, 7, 8
```

Codul 0 apare cand impartirea este exacta sau cand prima cifra de dupa virgula este 0. El se citeste separat, nu ca tip obisnuit de ezoterism.

### Tipul principal de ezoterism

| Cod principal | Tip de ezoterism |
| --- | --- |
| 2, 8 | ezoterism spiritual |
| 1, 5 | ezoterism stiintific |
| 4, 7 | ezoterism practic |
| 0 | cod special |

### Codul secundar

Dupa stabilirea codului principal, se poate calcula orientarea secundara.

Se ia partea intreaga obtinuta la prima impartire:

```text
partea_intreaga = partea intreaga din (data_nasterii_scrisa_ca_numar / 7)
```

Apoi se imparte aceasta parte intreaga din nou la 7:

```text
cod secundar =
  prima cifra de dupa virgula din (partea_intreaga / 7)
```

Codul secundar nu inlocuieste codul principal. El se interpreteaza numai in interiorul tipului principal de ezoterism.

---

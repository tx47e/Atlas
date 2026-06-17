# Vibratia anului personal - metoda

Formula adoptata pentru proiect:

```text
vibratia anului personal =
  reducere_numerologica(ziua nasterii + luna nasterii + anul analizat)
```

Acest calcul pastreaza formula folosita anterior pentru `vibratia anului`.
Rezultatul descrie energia numerologica a unui an calendaristic pentru persoana.

## Diferenta fata de anul personal din ciclul de 9 ani

In bibliografie, anul personal din ciclul de 9 ani incepe la ziua de nastere si
tine pana la urmatoarea aniversare. Vibratia anului personal din acest fisier se
calculeaza pentru un an calendaristic concret.

De aceea, cele doua notiuni trebuie pastrate separat:

- `vibratia anului personal`: zi + luna + anul analizat, redusa la 1-9;
- `anul personal` din ciclul de 9 ani: pozitia persoanei intre doua aniversari.

## Pasi de calcul

1. Se preiau ziua si luna nasterii.
2. Se preia anul analizat.
3. Se aduna cifrele zilei, lunii si anului analizat.
4. Se reduce rezultatul la 1-9.

Exemplu:

```text
24.04 pentru anul 2026
2 + 4 + 0 + 4 + 2 + 0 + 2 + 6 = 20
2 + 0 = 2

vibratia anului personal = 2
```

# Cicluri de 9 ani - metoda

Metoda este preluata din `bibliography/11 - Lectii de viata si ciclul de 9 ani.md`.

Ciclul de 9 ani descrie succesiunea anilor personali `1`-`9`. Fiecare an
personal incepe la ziua si luna nasterii si se incheie la urmatoarea aniversare,
nu la 1 ianuarie.

## Regula principala

```text
anul personal 1 = perioada de la data nasterii pana la prima aniversare
anul personal 2 = perioada dintre prima si a doua aniversare
...
anul personal 9 = perioada dintre a opta si a noua aniversare
dupa anul personal 9, ciclul reincepe cu anul personal 1
```

Aceasta regula inseamna ca anul personal nu este identic cu anul calendaristic.
O persoana poate fi in anul personal inceput in anul calendaristic anterior daca
ziua ei de nastere din anul curent nu a venit inca.

## Calcul rapid dupa varsta implinita

Pentru un calcul rapid, cand se cunoaste varsta implinita:

```text
ciclu 9 ani = floor(varsta / 9) + 1
pozitie in ciclu = varsta % 9 + 1
```

Pozitia in ciclu este anul personal din ciclul curent.

## Calcul complet dupa data

Pentru a construi tabelul complet:

1. Se porneste de la data nasterii.
2. Prima perioada este anul personal `1`.
3. Fiecare perioada tine pana la aceeasi zi si luna din anul urmator.
4. Dupa anul personal `9`, se incepe un nou ciclu cu anul personal `1`.
5. Pentru o data analizata, se verifica intre ce doua aniversari cade data.

## Exemplu scurt

Pentru data `1.10.1988`:

```text
1.10.1988 - 1.10.1989 = anul personal 1, ciclul 1
1.10.1989 - 1.10.1990 = anul personal 2, ciclul 1
...
1.10.1996 - 1.10.1997 = anul personal 9, ciclul 1
1.10.1997 - 1.10.1998 = anul personal 1, ciclul 2
```

## Diferenta fata de vibratia anului personal

`Vibratia anului personal` se calculeaza din zi, luna si anul analizat. Ciclul
de 9 ani din acest fisier este o pozitionare pe varsta/aniversari: arata unde se
afla persoana in succesiunea 1-9 pornita de la nastere.

# Lectii de viata - metoda

## Formula

```text
produs = ziua nasterii x luna nasterii x anul nasterii
sir lectii = cifrele produsului, pastrate in ordinea in care apar
```

Exemplu scurt:

```text
6.11.1984
6 x 11 x 1984 = 130944
sir lectii = 1, 3, 0, 9, 4, 4
```

## Pasi de calcul

1. Se preia data nasterii in format numeric: zi, luna, an.
2. Se inmultesc cele trei valori: `zi x luna x an`.
3. Rezultatul se transforma intr-un sir de cifre.
4. Fiecare cifra din sir reprezinta lectia unui an de viata.
5. Dupa ultima cifra, sirul se reia de la prima cifra.

## Regula de aplicare pe ani

Prima cifra din sir se aplica primului an de viata.

```text
anul 1 de viata -> cifra 1 din sir
anul 2 de viata -> cifra 2 din sir
anul 3 de viata -> cifra 3 din sir
...
```

Daca numarul anului depaseste lungimea sirului, pozitia se calculeaza ciclic:

```text
pozitie = ((an_de_viata - 1) mod lungime_sir) + 1
lectie = sir[pozitie]
```

Indexarea de mai sus este explicata in termeni umani, unde prima pozitie este
pozitia 1. In implementare software, daca lista este indexata de la 0, formula
devine:

```text
index = (an_de_viata - 1) mod lungime_sir
lectie = sir[index]
```

## Diferenta dintre an de viata si varsta

In acest calcul, `anul de viata` nu este acelasi lucru cu `varsta implinita`.

```text
anul 1 de viata = intervalul de la nastere pana la prima aniversare
anul 2 de viata = intervalul dintre 1 an implinit si 2 ani impliniti
anul N de viata = intervalul dintre N-1 ani impliniti si N ani impliniti
```

Prin urmare:

```text
an_de_viata = varsta_implinita + 1
```

Exemplu: o persoana care are 25 de ani impliniti se afla in anul 26 de viata,
pana la urmatoarea aniversare.

## Reguli pentru cifra 0

Cifra `0` se pastreaza in sir. Ea nu se elimina, nu se inlocuieste si nu se
reduce.

Exemplu:

```text
130944 -> 1, 3, 0, 9, 4, 4
```

In interpretare, `0` este tratat ca o lectie distincta.

## Ce nu se face in aceasta metoda

- Nu se aduna cifrele datei de nastere.
- Nu se reduce produsul la o singura cifra.
- Nu se pastreaza numere maestre ca rezultat final.
- Nu se foloseste anul calendaristic analizat.
- Nu se calculeaza un ciclu fix de 7, 9 sau 12 ani.

Aceasta metoda este specifica proiectului si ramane formula adoptata pentru
rubrica `lectii de viata`.


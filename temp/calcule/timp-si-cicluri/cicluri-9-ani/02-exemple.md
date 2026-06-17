# Cicluri de 9 ani - exemple

## Exemplul 1: tabel de la data nasterii

Data nasterii:

```text
1.10.1988
```

Primul ciclu de 9 ani:

| Ciclu | An personal | Perioada |
|---:|---:|---|
| 1 | 1 | 1.10.1988 - 1.10.1989 |
| 1 | 2 | 1.10.1989 - 1.10.1990 |
| 1 | 3 | 1.10.1990 - 1.10.1991 |
| 1 | 4 | 1.10.1991 - 1.10.1992 |
| 1 | 5 | 1.10.1992 - 1.10.1993 |
| 1 | 6 | 1.10.1993 - 1.10.1994 |
| 1 | 7 | 1.10.1994 - 1.10.1995 |
| 1 | 8 | 1.10.1995 - 1.10.1996 |
| 1 | 9 | 1.10.1996 - 1.10.1997 |

Al doilea ciclu incepe la urmatoarea aniversare:

| Ciclu | An personal | Perioada |
|---:|---:|---|
| 2 | 1 | 1.10.1997 - 1.10.1998 |
| 2 | 2 | 1.10.1998 - 1.10.1999 |
| 2 | 3 | 1.10.1999 - 1.10.2000 |

## Exemplul 2: data analizata inainte de aniversare

Data nasterii:

```text
1.10.1988
```

Data analizata:

```text
15.06.2024
```

In 15.06.2024, aniversarea din 2024 nu a venit inca. Persoana se afla in
perioada:

```text
1.10.2023 - 1.10.2024
```

Varsta implinita la inceputul perioadei este `35`.

```text
ciclu = floor(35 / 9) + 1 = 3 + 1 = 4
an personal = 35 % 9 + 1 = 8 + 1 = 9
```

Rezultat:

- ciclul 4;
- anul personal 9.

## Exemplul 3: data analizata dupa aniversare

Data analizata:

```text
15.11.2024
```

Aniversarea din 2024 a trecut. Persoana se afla in perioada:

```text
1.10.2024 - 1.10.2025
```

Varsta implinita la inceputul perioadei este `36`.

```text
ciclu = floor(36 / 9) + 1 = 4 + 1 = 5
an personal = 36 % 9 + 1 = 0 + 1 = 1
```

Rezultat:

- ciclul 5;
- anul personal 1.

## Exemplul 4: calcul rapid dupa varsta

Pentru `varsta = 28`:

```text
ciclu = floor(28 / 9) + 1 = 3 + 1 = 4
pozitie = 28 % 9 + 1 = 1 + 1 = 2
```

Rezultat:

- ciclul 4;
- anul personal 2.

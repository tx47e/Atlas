# Patratul de aur 3x3 - metoda

## Regula de baza

Patratul de aur se construieste pe asezarea clasica a patratului lui Pitagora:

| 1 | 4 | 7 |
|---|---|---|
| 2 | 5 | 8 |
| 3 | 6 | 9 |

Se porneste de la ziua nasterii, fara reducere, iar valoarea se introduce in
casuta `4`. De aici se completeaza crescator, cu cate `+1`, urmand traseul:

```text
4 -> 9 -> 2 -> 3 -> 5 -> 7 -> 8 -> 1 -> 6
```

Astfel:

| Pas | Casuta | Valoare |
|---:|---:|---:|
| 1 | 4 | ziua nasterii |
| 2 | 9 | ziua nasterii + 1 |
| 3 | 2 | ziua nasterii + 2 |
| 4 | 3 | ziua nasterii + 3 |
| 5 | 5 | ziua nasterii + 4 |
| 6 | 7 | ziua nasterii + 5 |
| 7 | 8 | ziua nasterii + 6 |
| 8 | 1 | ziua nasterii + 7 |
| 9 | 6 | ziua nasterii + 8 |

## Formula sumei

Valoarea centrala este:

```text
centru = ziua nasterii + 4
```

Suma de control pentru fiecare linie si coloana este:

```text
suma de control = centru x 3
```

## Verificare

Dupa completare, se verifica obligatoriu:

- toate cele trei linii;
- toate cele trei coloane.

Pentru validarea completa se verifica si:

- cele doua diagonale.

Fiecare trebuie sa aiba aceeasi suma de control.

## Sens simbolic

Traseul de completare merge pe miscarea diagonala `spre dreapta sus`, adica pe
vectorul `3-5-7`, vectorul atingerii scopurilor in patratul lui Pitagora. De
aceea, patratul de aur este folosit in capitolul `Ajutoare` ca structura de
potentare a directiei, sustinerii si reusitei.

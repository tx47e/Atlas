# Patratul de aur 3x3 - exemple

## Exemplu: ziua nasterii 27

Se introduce `27` in casuta `4`, apoi se completeaza crescator pe traseul:

```text
4 -> 9 -> 2 -> 3 -> 5 -> 7 -> 8 -> 1 -> 6
```

| Pas | Casuta | Valoare |
|---:|---:|---:|
| 1 | 4 | 27 |
| 2 | 9 | 28 |
| 3 | 2 | 29 |
| 4 | 3 | 30 |
| 5 | 5 | 31 |
| 6 | 7 | 32 |
| 7 | 8 | 33 |
| 8 | 1 | 34 |
| 9 | 6 | 35 |

Asezat in patratul lui Pitagora, rezultatul este:

| 1 | 4 | 7 |
|---:|---:|---:|
| 34 | 27 | 32 |
| 29 | 31 | 33 |
| 30 | 35 | 28 |

Valoarea centrala este `31`, deci suma de control este:

```text
31 x 3 = 93
```

Verificare:

| Directie | Calcul | Suma |
|---|---|---:|
| Rand 1 | 34 + 27 + 32 | 93 |
| Rand 2 | 29 + 31 + 33 | 93 |
| Rand 3 | 30 + 35 + 28 | 93 |
| Coloana 1 | 34 + 29 + 30 | 93 |
| Coloana 2 | 27 + 31 + 35 | 93 |
| Coloana 3 | 32 + 33 + 28 | 93 |
| Diagonala 1 | 34 + 31 + 28 | 93 |
| Diagonala 2 | 32 + 31 + 30 | 93 |


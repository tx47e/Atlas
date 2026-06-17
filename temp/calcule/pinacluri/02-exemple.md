# Pinacluri - exemple

## Exemplu: 13.04.1968

Data nasterii:

```text
zi = 13
luna = 04
an = 1968
```

Se reduc valorile de baza:

```text
L = luna = 4
Z = ziua = 1 + 3 = 4
A = anul = 1 + 9 + 6 + 8 = 24, 2 + 4 = 6
```

Se calculeaza si soarta, pentru stabilirea varstelor:

```text
1 + 3 + 0 + 4 + 1 + 9 + 6 + 8 = 32
3 + 2 = 5
```

Rezultat:

- Soarta: 5.

## Calculul oportunitatilor

```text
oportunitate 1 = L + Z = 4 + 4 = 8
oportunitate 2 = Z + A = 4 + 6 = 10, 1 + 0 = 1
oportunitate 3 = oportunitate 1 + oportunitate 2 = 8 + 1 = 9
oportunitate 4 = L + A = 4 + 6 = 10, 1 + 0 = 1
```

Rezultatul oportunitatilor:

- Oportunitate 1: 8.
- Oportunitate 2: 1.
- Oportunitate 3: 9.
- Oportunitate 4: 1.

## Calculul provocarilor

La provocari se foloseste valoarea absoluta.

```text
provocare 1 = |Z - L| = |4 - 4| = 0
provocare 2 = |Z - A| = |4 - 6| = 2
provocare 3 = |provocare 1 - provocare 2| = |0 - 2| = 2
provocare 4 = |L - A| = |4 - 6| = 2
```

Rezultatul provocarilor:

- Provocare 1: 0.
- Provocare 2: 2.
- Provocare 3: 2.
- Provocare 4: 2.

## Calculul varstelor

Pentru acest exemplu, soarta este `5`.

```text
sfarsit pinaclu 1 = 36 - 5 = 31
sfarsit pinaclu 2 = 31 + 9 = 40
sfarsit pinaclu 3 = 40 + 9 = 49
pinaclu 4 = de la anul urmator pana la finalul vietii
```

Intervalele sunt:

- Pinaclu 1: 0-31 ani.
- Pinaclu 2: 32-40 ani.
- Pinaclu 3: 41-49 ani.
- Pinaclu 4: 50+ ani.

## Rezultat final

| Etapa | Varsta | Oportunitate | Provocare |
|---|---:|---:|---:|
| Pinaclul 1 | 0-31 | 8 | 0 |
| Pinaclul 2 | 32-40 | 1 | 2 |
| Pinaclul 3 | 41-49 | 9 | 2 |
| Pinaclul 4 | 50+ | 1 | 2 |

## Date pentru grafic

Graficul rezultatului final foloseste intervalele de varsta pe axa X si valorile
calculate pe axa Y. Se traseaza doua linii colorate diferit: una pentru
oportunitati si una pentru provocari.

| Interval varsta | Oportunitate | Provocare |
|---|---:|---:|
| 0-31 | 8 | 0 |
| 32-40 | 1 | 2 |
| 41-49 | 9 | 2 |
| 50+ | 1 | 2 |

Specificatie vizuala:

- axa X: `0-31`, `32-40`, `41-49`, `50+`;
- axa Y: valori de la `0` la `9`;
- linia oportunitatilor: culoare distincta, de exemplu albastru;
- linia provocarilor: culoare distincta, de exemplu rosu.

## Zona de confort pe grafic

Zona de confort se calculeaza separat pentru fiecare serie reprezentata pe
grafic.

Pentru oportunitati:

```text
(8 + 1 + 9 + 1) / 4 = 19 / 4 = 4,75
```

Pentru provocari:

```text
(0 + 2 + 2 + 2) / 4 = 6 / 4 = 1,5
```

Pe grafic, aceste valori se pot marca prin doua linii orizontale subtiri:

- zona de confort a oportunitatilor: `4,75`;
- zona de confort a provocarilor: `1,5`.

## Interpretare scurta

Primul pinaclu, cu oportunitatea `8`, poate aduce in prim-plan teme de forta,
responsabilitate, organizare si raportare la lumea materiala. Provocarea `0`
arata ca etapa poate cere alegere constienta, incredere in propria analiza si
trecere de la posibilitate la actiune.

Pinaclurile urmatoare aduc oportunitatile `1`, `9` si `1`. Acestea pot indica o
alternanta intre initiativa personala, afirmare, idealuri mai largi si integrarea
experientei. Repetitia provocarii `2` arata o lectie recurenta legata de
sensibilitate, cooperare, relatie si felul in care persoana invata sa nu ia totul
personal.

In lectura, pinaclurile se citesc ca directii de crestere pentru fiecare etapa,
iar provocarile ca teme care cer maturizare. Ele nu descriu evenimente obligatorii,
ci un cadru de reflectie asupra felului in care persoana isi poate folosi mai
constient resursele.

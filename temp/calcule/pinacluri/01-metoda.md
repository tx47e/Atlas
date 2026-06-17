# Pinacluri - metoda

Formula adoptata pentru proiect foloseste patru pinacluri. Pentru fiecare
pinaclu se calculeaza trei informatii:

- oportunitatea asociata acelei etape;
- provocarea asociata acelei etape;
- intervalul de varsta in care se aplica pinaclul.

Metoda este evaluata pe baza documentului bibliografic
`bibliography/09 - Oportunitati si provocari.md`, unde oportunitatile si
provocarile sunt asezate pe cele patru etape majore ale vietii.

## Date necesare

- ziua nasterii;
- luna nasterii;
- anul nasterii.

Se folosesc valorile reduse ale zilei, lunii si anului:

```text
zi = reducere_numerologica(ziua nasterii)
luna = reducere_numerologica(luna nasterii)
an = reducere_numerologica(anul nasterii)
vibratia_destinului = reducere_numerologica(data nasterii completa)
```

## Oportunitati

In bibliografie, rezultatele `O1`-`O4` sunt numite oportunitati. In proiect,
aceste rezultate arata resursa de crestere activa in fiecare etapa de pinaclu.
Fiecare oportunitate se asaza pe pinaclul corespunzator.

```text
oportunitate 1 = reducere_numerologica(luna + zi)
oportunitate 2 = reducere_numerologica(zi + an)
oportunitate 3 = reducere_numerologica(oportunitate 1 + oportunitate 2)
oportunitate 4 = reducere_numerologica(luna + an)
```

## Provocari

```text
provocare 1 = valoare_absoluta(zi - luna)
provocare 2 = valoare_absoluta(zi - an)
provocare 3 = valoare_absoluta(provocare 1 - provocare 2)
provocare 4 = valoare_absoluta(luna - an)
```

Provocarile pot avea si valoarea 0.

## Pinacluri

Pinaclurile arata perioada de viata in care se citeste fiecare pereche
oportunitate-provocare. Primul interval depinde de vibratia destinului, iar
urmatoarele doua pinacluri dureaza cate 9 ani. Al patrulea pinaclu incepe dupa
finalul celui de-al treilea si ramane activ pana la finalul vietii.

```text
sfarsit pinaclu 1 = 36 - vibratia_destinului
sfarsit pinaclu 2 = sfarsit pinaclu 1 + 9
sfarsit pinaclu 3 = sfarsit pinaclu 2 + 9
pinaclu 4 = de la anul urmator pana la finalul vietii
```

Exemplu pentru `vibratia_destinului = 3`:

```text
pinaclu 1: 0-33 ani
pinaclu 2: 34-42 ani
pinaclu 3: 43-51 ani
pinaclu 4: 52+ ani
```

## Rezultat final al calculului

Rezultatul calculului se noteaza pe patru randuri, cate unul pentru fiecare
pinaclu:

| Etapa | Varsta | Oportunitate | Provocare |
|---|---|---:|---:|
| Pinaclul 1 | `0-sfarsit pinaclu 1` | `oportunitate 1` | `provocare 1` |
| Pinaclul 2 | `sfarsit pinaclu 1 + 1` - `sfarsit pinaclu 2` | `oportunitate 2` | `provocare 2` |
| Pinaclul 3 | `sfarsit pinaclu 2 + 1` - `sfarsit pinaclu 3` | `oportunitate 3` | `provocare 3` |
| Pinaclul 4 | `sfarsit pinaclu 3 + 1`+ | `oportunitate 4` | `provocare 4` |

## Reprezentare grafica

Rezultatul final poate fi reprezentat si ca grafic cu doua linii:

- axa X: intervalele de varsta ale pinaclurilor;
- axa Y: valorile numerologice calculate;
- linia 1: oportunitatile, intr-o culoare distincta;
- linia 2: provocarile, intr-o alta culoare.
- zona de confort: o linie sau banda orizontala calculata din valorile
  reprezentate pe grafic.

Graficul ajuta la compararea vizuala a resursei de crestere cu tema de
maturizare pentru fiecare etapa. Deoarece intervalele de varsta sunt etichete
categorice, ele se folosesc ca valori discrete pe axa X.

## Zona de confort pe grafic

In bibliografia despre soarta si destin, zona de confort se calculeaza prin
adunarea cifrelor numarului reprezentat pe grafic si impartirea sumei la numarul
de segmente folosite in acel grafic. Pentru pinacluri, adaptarea de proiect este:

```text
zona de confort oportunitati =
  (oportunitate 1 + oportunitate 2 + oportunitate 3 + oportunitate 4) / 4

zona de confort provocari =
  (provocare 1 + provocare 2 + provocare 3 + provocare 4) / 4
```

Pe grafic, aceste valori se pot marca prin linii orizontale subtiri sau printr-o
banda discreta. Daca oportunitatea este aproape de zona ei de confort, etapa se
citeste ca mai stabila. Daca este mult peste sau sub zona de confort,
interpretarea cere atentie la exces, presiune, pasivitate sau efort de crestere.

Referinte tehnice pentru reprezentare:

- axe X cu etichete categorice:
  `https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html`
- zone umbrite intre linii sau intervale:
  `https://helpcenter.flourish.studio/hc/en-us/articles/8761574600207-How-to-shade-areas-between-lines`

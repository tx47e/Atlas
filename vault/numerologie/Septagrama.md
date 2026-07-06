---
titlu: Septagrama
tip: concept
tags:
  - numerologie
  - cicluri
  - septagrama
Data: 2026-06-20
depinde de: Ciclul de 7 Ani
---

---
## Descriere

Septagrama este reprezentarea grafica a [[Ciclul de 7 Ani|ciclului de 7 ani]].
Ea aseaza viata in segmente de cate 7 ani, pe varfurile unei stele cu sapte
varfuri. Fiecare varf indica un prag de verificare, numit moment de criza, iar
fiecare latura arata trecerea de la o etapa la alta.

In aceasta metoda, fiecare varf al septagramei este un moment de criza:

```text
fiecare varf = moment de criza
```

Momentul de criza se citeste la mijlocul fiecarui ciclu de 7 ani, adica la
jumatatea intervalului:

```text
moment_criza = inceput_ciclu + 3,5 ani
```

Pentru redactare, momentul se poate exprima ca varsta cu zecimala, an
calendaristic si anul de viata.

---
## Principiu de calcul

Fiecare ciclu are 7 ani:

```text
C1 = 0-7 ani
C2 = 7-14 ani
C3 = 14-21 ani
C4 = 21-28 ani
C5 = 28-35 ani
C6 = 35-42 ani
C7 = 42-49 ani
```

Dupa C7, schema continua pe aceeasi septagrama:

```text
C8 = 49-56 ani
C9 = 56-63 ani
C10 = 63-70 ani
C11 = 70-77 ani
C12 = 77-84 ani
C13 = 84-91 ani
C14 = 91-98 ani
```

Pentru fiecare ciclu:

```text
an_start = anul_nasterii + varsta_start
an_final = anul_nasterii + varsta_final - 1
varsta_criza = varsta_start + 3,5
an_criza = anul_nasterii + floor(varsta_criza)
an_de_viata = floor(varsta_criza) + 1
```

Exemplu pentru o persoana nascuta in 1973:

```text
C1 = 1973-1979
0-7 ani
moment criza = 3,5 ani
an criza = 1977
al 4-lea an de viata
```

---
## Varfurile septagramei

Septagrama foloseste sapte varfuri. In exemplul de lucru, varfurile sunt notate
cu perechi numerice:

| Varf | Pereche | Cicluri aferente |
| --- | --- | --- |
| 1 | 1/8 | C1, C8 |
| 2 | 2/6 | C2, C9 |
| 3 | 3/10 | C3, C10 |
| 4 | 4/11 | C4, C11 |
| 5 | 5/9 | C5, C12 |
| 6 | 3/7 | C6, C13 |
| 7 | 1/5 | C7, C14 |

Perechea de pe varf se pastreaza in tabel si se interpreteaza ca semnatura
numerologica a acelui prag de criza.

---
## Rezultat pereche

Pentru fiecare varf se noteaza si `Rezultat pereche`.

Regula de lucru:

```text
rezultat_pereche = reducere_numerologica(prima_valoare_din_pereche + a_doua_valoare_din_pereche)
```

Tabel de calcul:

| Varf | Pereche | Calcul | Rezultat pereche |
| --- | --- | --- | --- |
| 1 | 1/8 | 1 + 8 = 9 | 9 |
| 2 | 2/6 | 2 + 6 = 8 | 8 |
| 3 | 3/10 | 3 + 10 = 13 -> 4 | 4 |
| 4 | 4/11 | 4 + 11 = 15 -> 6 | 6 |
| 5 | 5/9 | 5 + 9 = 14 -> 5 | 5 |
| 6 | 3/7 | 3 + 7 = 10 -> 1 | 1 |
| 7 | 1/5 | 1 + 5 = 6 | 6 |

Rezultatul perechii se citeste ca sinteza vibrationala a varfului. Perechea
arata cele doua forte ale pragului, iar rezultatul arata directia de integrare.

---
## Tabel de lucru

| Ciclu | Ani calendaristici | Varsta | Varsta criza | An criza | An de viata | Varf | Pereche | Rezultat pereche | Interpretare |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 |  | 0-7 | 3,5 |  | al 4-lea | 1 | 1/8 | 9 |  |
| C2 |  | 7-14 | 10,5 |  | al 11-lea | 2 | 2/6 | 8 |  |
| C3 |  | 14-21 | 17,5 |  | al 18-lea | 3 | 3/10 | 4 |  |
| C4 |  | 21-28 | 24,5 |  | al 25-lea | 4 | 4/11 | 6 |  |
| C5 |  | 28-35 | 31,5 |  | al 32-lea | 5 | 5/9 | 5 |  |
| C6 |  | 35-42 | 38,5 |  | al 39-lea | 6 | 3/7 | 1 |  |
| C7 |  | 42-49 | 45,5 |  | al 46-lea | 7 | 1/5 | 6 |  |
| C8 |  | 49-56 | 52,5 |  | al 53-lea | 1 | 1/8 | 9 |  |
| C9 |  | 56-63 | 59,5 |  | al 60-lea | 2 | 2/6 | 8 |  |
| C10 |  | 63-70 | 66,5 |  | al 67-lea | 3 | 3/10 | 4 |  |
| C11 |  | 70-77 | 73,5 |  | al 74-lea | 4 | 4/11 | 6 |  |
| C12 |  | 77-84 | 80,5 |  | al 81-lea | 5 | 5/9 | 5 |  |
| C13 |  | 84-91 | 87,5 |  | al 88-lea | 6 | 3/7 | 1 |  |
| C14 |  | 91-98 | 94,5 |  | al 95-lea | 7 | 1/5 | 6 |  |

---
## Interpretare generala

Interpretarea septagramei urmareste:

- ciclul in care se afla persoana;
- varful activ al septagramei;
- momentul de criza al ciclului;
- perechea numerologica a varfului;
- rezultatul perechii;
- suprapunerea cu [[Ciclul de 9 Ani]], [[Ciclul de 12 Ani]],
  [[Anii Importanti Int-Ext]] si [[Soarta si Destin]].

Momentul de criza nu se interpreteaza fatalist. El arata o verificare de etapa:
ce trebuie vazut, ajustat, maturizat sau reorganizat.

---
## Utilizare in lucrare

In cuprinsul lucrarii, septagrama intra in:

- `2.4. Ciclicitati - Septagrama`;
- `5.1. Ansamblul geometric al lui Pitagora`, daca se construieste o harta
  vizuala extinsa a parcursului vietii.

Rubrica trebuie sa includa:

- tabelul ciclurilor de 7 ani;
- anul si varsta momentelor de criza;
- varful septagramei;
- perechea numerologica a varfului;
- rezultatul perechii;
- interpretarea varfului activ si a ciclului curent.

---
## Exemplu vizual

Exemplu SVG pentru data `27.11.1973`:

- fisier: [[septagrama-27-11-1973.svg]].

Acest SVG se foloseste ca referinta vizuala principala pentru septagrama:

- septagrama este simetrica si construita din linii negre;
- sensul de curgere este marcat cu sageti portocalii asezate pe langa liniile
  negre;
- varfurile portocalii marcheaza momentele de criza;
- etichetele de pe muchii sunt orientate dupa linia septagramei, asezate foarte
  aproape de linie, dar fara sa calce peste linie;
- etichetele de pe muchii sunt trase catre capetele liniilor, in directia
  varfurilor stelei;
- fiecare varf pastreaza perechea numerologica, iar `Rezultat pereche` se
  pastreaza in tabelul de lucru.

---
## Observatii

- Fiecare varf al septagramei marcheaza un moment de criza.
- Criza inseamna verificare si prag de maturizare, nu eveniment negativ
  obligatoriu.
- Ciclurile se citesc in segmente de 7 ani.
- Varfurile se repeta dupa C7: C8 revine la varful 1, C9 la varful 2 si asa mai
  departe.
- Rezultatul perechii trebuie pastrat in tabel pentru fiecare ciclu.

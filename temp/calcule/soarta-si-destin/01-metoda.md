# Soarta si destin - metoda

Metoda compara doua linii ale vietii:

- `soarta`, adica linia de conditionare, cadrul primit si drumul initial;
- `destinul`, adica directia de implinire si varianta de urcat catre potential.

Cele doua rezultate nu se reduc la o singura cifra. Ele se pastreaza ca numere
grafice de 7 cifre si se citesc impreuna prin zona de confort, puncte de
intalnire, puncte de rascruce si ritmuri de 10 sau 12 ani.

Interpretarea comparativa dintre cele doua linii poate fi numita si `tema
vietii`, atunci cand accentul cade pe concluzia de sinteza.

## Date necesare

- ziua nasterii;
- luna nasterii;
- anul nasterii;
- alegerea ciclului grafic de 10 sau 12 ani, daca se face reprezentare vizuala.

## 1. Calculul sortii

Soarta se calculeaza prin formula:

```text
soarta = ZZLL x AAAA
```

Unde:

- `ZZ` este ziua nasterii scrisa cu doua cifre;
- `LL` este luna nasterii scrisa cu doua cifre;
- `AAAA` este anul nasterii scris cu patru cifre.

Daca ziua sau luna are o singura cifra, se adauga `0` in fata pentru formarea
blocului `ZZLL`. Spre deosebire de calculul ezoteric, aici zeroul de completare
se pastreaza, pentru ca metoda cere explicit forma calendaristica de patru cifre.

Pasi:

1. Se scrie ziua cu doua cifre.
2. Se scrie luna cu doua cifre.
3. Se unesc ziua si luna in blocul `ZZLL`.
4. Se inmulteste `ZZLL` cu anul nasterii `AAAA`.
5. Daca rezultatul are mai putin de 7 cifre, se completeaza cu zerouri in fata.
6. Numarul de 7 cifre se foloseste pentru graficul sortii.

## 2. Calculul destinului

Destinul se calculeaza din aceeasi structura a datei, dar cu zerourile inlocuite
cu `1`:

```text
destin = ZZLL_ajustat x AAAA_ajustat
```

Unde:

- se formeaza data in structura `ZZLL` si `AAAA`;
- fiecare cifra `0` din aceste blocuri se inlocuieste cu `1`;
- rezultatul se pastreaza ca numar grafic de 7 cifre.

Pasi:

1. Se scrie ziua cu doua cifre.
2. Se scrie luna cu doua cifre.
3. Se unesc ziua si luna in blocul `ZZLL`.
4. Se scrie anul nasterii in forma `AAAA`.
5. In `ZZLL` si `AAAA`, fiecare `0` se inlocuieste cu `1`.
6. Se inmulteste blocul `ZZLL` ajustat cu anul ajustat.
7. Daca rezultatul are mai putin de 7 cifre, se completeaza cu zerouri in fata.
8. Numarul de 7 cifre se foloseste pentru graficul destinului.

## 3. Zona de confort

Zona de confort se calculeaza separat pentru soarta si pentru destin:

```text
zona_de_confort = suma_cifrelor(numar_grafic) / 7
```

Rezultatul se poate citi aproximativ, in plus sau in minus:

- sub zona de confort apare pasivitate, presiune sau lipsa de chef;
- in zona de confort persoana functioneaza firesc;
- peste zona de confort apare efortul de crestere si dinamica evolutiva.

## 4. Interpretarea comparativa

Soarta si destinul se citesc impreuna:

- unde liniile sunt apropiate;
- unde se indeparteaza;
- unde omul este in zona de confort;
- unde apar puncte de intalnire;
- unde apar puncte de rascruce;
- ce cere cadrul primit;
- ce cere directia de implinire.

Aceasta interpretare comparativa este `tema vietii` ca denumire alternativa.

## 5. Grafic

Numerele de 7 cifre se asaza pe un grafic pe segmente de 10 sau 12 ani. Ciclul
de 10 ani se foloseste mai ales pentru predominanta masculina, iar ciclul de 12
ani pentru predominanta feminina. Cand exista neclaritate, se verifica matricea
numerologica si predominanta cifrelor pare sau impare.

## 6. Atentie la denumire

In proiect, `destinul` din aceasta metoda nu este calculat din nume si nu se
confunda cu `numarul de exprimare`. Daca intr-o sursa apare ideea ca numarul de
exprimare este o vibratie a destinului, aceasta se noteaza ca echivalenta de
interpretare, nu ca formula pentru capitolul grafic `Soarta si destin`.

## Surse bibliografice interne

- `bibliography/10 - Soarta si destin.md`

---
titlu: Soarta si Destin - Calcul
tip: calcul
tags:
  - numerologie
  - ciclicitati
  - calcul
  - SoartaSiDestin
  - documentatie-modulara
sursa: '[[Soarta si Destin]]'
---

# Soarta si Destin - Calcul

## Statutul formulei

Registrul formulelor marcheaza Soarta, Destinul grafic si zona de confort ca documentate, dar neimplementate. Continutul legacy este pastrat fara audit formal nou.

## Formula de calcul

### Calculul sortii

Soarta se calculeaza prin formula:

```text
soarta = ZZLL x AAAA
```

Unde:

- `ZZ` este ziua nasterii scrisa cu doua cifre;
- `LL` este luna nasterii scrisa cu doua cifre;
- `AAAA` este anul nasterii scris cu patru cifre.

Pasi:

1. Se scrie ziua cu doua cifre.
2. Se scrie luna cu doua cifre.
3. Se unesc ziua si luna in blocul `ZZLL`.
4. Se inmulteste `ZZLL` cu anul nasterii `AAAA`.
5. Daca rezultatul are mai putin de 7 cifre, se completeaza cu zerouri in fata.
6. Numarul de 7 cifre se foloseste pentru graficul sortii.

### Calculul destinului grafic

Destinul se calculeaza din aceeasi structura a datei, dar cu zerourile inlocuite cu 1:

```text
destin = ZZLL_ajustat x AAAA_ajustat
```

Pasi:

1. Se scrie ziua cu doua cifre.
2. Se scrie luna cu doua cifre.
3. Se unesc ziua si luna in blocul `ZZLL`.
4. Se scrie anul nasterii in forma `AAAA`.
5. Se verifica daca `ZZLL` si `AAAA` contin cifra 0.
6. Daca nu exista niciun 0, destinul grafic este egal cu soarta si nu se mai recalculeaza separat.
7. Daca exista 0, in `ZZLL` si `AAAA`, fiecare 0 se inlocuieste cu 1.
8. Se inmulteste blocul `ZZLL` ajustat cu anul ajustat.
9. Daca rezultatul are mai putin de 7 cifre, se completeaza cu zerouri in fata.
10. Numarul de 7 cifre se foloseste pentru graficul destinului.

### Zona de confort

Zona de confort se calculeaza separat pentru soarta si pentru destin:

```text
zona_de_confort = suma_cifrelor(numar_grafic) / 7
```

Interpretare:

- sub zona de confort apare pasivitate, presiune sau lipsa de chef;
- in zona de confort persoana functioneaza firesc;
- peste zona de confort apare efortul de crestere si dinamica evolutiva.

### Alegerea intervalului de varsta

Intervalul folosit pe axa orizontala a graficului nu este optional, ci se alege dupa predominanta energetica a datei de nastere:

- daca matricea datei de nastere are predominanta impara / masculina, graficul se citeste pe intervale de 10 ani: `0`, `10`, `20`, `30`, `40`, `50`, `60` etc.;
- daca matricea datei de nastere are predominanta para / feminina, graficul se citeste pe intervale de 12 ani: `0`, `12`, `24`, `36`, `48`, `60`, `72` etc.;
- daca raportul este echilibrat, se alege ritmul dominant rezultat din interpretarea matricei si se mentioneaza explicit alegerea in sinteza graficului.

Sinteza graficului trebuie sa spuna ce interval se foloseste si de ce: 10 ani pentru predominanta impara / masculina sau 12 ani pentru predominanta para / feminina.

---

---
titlu: Aspecte de Indreptat si Solutia - Calcul
tip: calcul
tags:
  - numerologie
  - calcul
  - AspecteDeIndreptat
  - documentatie-modulara
sursa: '[[Aspecte de Indreptat]]'
---

# Aspecte de Indreptat si Solutia - Calcul

## Prescurtari

```text
Calea Destinului = CD
Prima cifra din ziua nasterii = PZ
Aspecte de Indreptat = AI
Solutia Aspectelor de Indreptat = SAI
```

## Formula Aspectelor de Indreptat

```text
AI = CD - 2 x PZ
```

### Pasi de calcul

1. Se calculeaza [[Calea Destinului]] si se pastreaza valoarea completa CD.
2. Se identifica prima cifra din ziua de nastere.
3. Prima cifra se inmulteste cu `2`.
4. Rezultatul se scade din CD.
5. Numarul obtinut reprezinta AI.

### Regula primei cifre

- pentru ziua `3`, PZ este `3`;
- pentru ziua `17`, PZ este `1`;
- pentru ziua `29`, PZ este `2`.

Formula nu foloseste [[Vibratie Interioara|Vibratia Interioara]] redusa.

## Formula Solutiei - statut de audit

Sursele curente nu sunt aliniate:

- nota legacy [[Aspecte de Indreptat]] cere reducerea repetata pana la o singura
  cifra;
- calculatorul agregat si copia lui din skill aplica in prezent o singura
  insumare a cifrelor AI;
- [[Registru Validare Formule]] pastreaza discrepanta si cere aprobare separata
  pentru corectarea tuturor surselor dependente.

Prin urmare, acest modul nu declara inca o formula unica drept forma finala
aprobata pentru SAI.

### Variante aflate in audit

```text
Varianta legacy:
SAI = reducere_numerologica_repetata(AI)

Varianta cu o singura insumare:
SAI = suma_cifrelor(AI), aplicata exact o singura data
```

Nu se modifica nota legacy, calculatorul, skill-urile, template-urile, testele
sau lucrarile personale pana la aprobarea separata a alinierii.

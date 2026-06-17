# Aspecte de indreptat - metoda

Formula foloseste [calea destinului](../calea-destinului/README.md) si prima
cifra din ziua de nastere.

```text
aspecte_de_indreptat =
  calea_destinului - 2 x prima_cifra_din_ziua_nasterii
```

Rezultatul obtinut arata aspectele de indreptat.

Vibratia solutiei se obtine prin reducerea numerologica a rezultatului:

```text
vibratia_solutiei = reducere_numerologica(aspecte_de_indreptat)
```

## Pasi

1. Se calculeaza [calea destinului](../calea-destinului/README.md): suma tuturor
   cifrelor din zi, luna si an, fara reducere la o singura cifra.
2. Se ia prima cifra din ziua de nastere.
3. Se inmulteste acea cifra cu `2`.
4. Se scade rezultatul din calea destinului.
5. Numarul obtinut arata aspectele de indreptat.
6. Se reduce numarul la o singura cifra pentru vibratia solutiei.

## Dependinte

- [Calea destinului](../calea-destinului/README.md)
- [Vibratia interioara](../vibratia-interioara/README.md)
- data nasterii completa, validata in lucrare

## Surse bibliografice interne

- `bibliography/03 - Vibrația interioară, exterioară și cosmică.md`

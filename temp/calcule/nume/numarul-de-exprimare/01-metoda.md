# Numarul de exprimare - metoda

Formula adoptata pentru proiect:

```text
numarul de exprimare = reducere_numerologica(
  suma(reducere_numerologica(suma valorilor literelor fiecarei componente de nume))
)
```

## Alfabet folosit

Folosim alfabetul pitagoreic documentat in
`knowledge_base/calcule/nume/01-alfabet-numerologic.md`.

```text
1: A J S
2: B K T
3: C L U
4: D M V
5: E N W
6: F O X
7: G P Y
8: H Q Z
9: I R
```

## Pasi de calcul

1. Se preia numele complet folosit in calcul.
2. Se normalizeaza textul: majuscule, fara diacritice, fara semne de punctuatie.
3. Numele se imparte in componente: nume de familie, prenume si alte prenume,
   dupa caz.
4. Fiecare litera se transforma in valoarea numerologica.
5. Pentru fiecare componenta, se aduna valorile literelor si se reduce suma la
   o cifra.
6. Se aduna componentele deja reduse.
7. Se reduce din nou suma componentelor la 1-9.

Exemplu schematic:

```text
NUME PRENUME

NUME    -> suma literelor -> reducere -> cifra numelui
PRENUME -> suma literelor -> reducere -> cifra prenumelui

numarul de exprimare = reducere(cifra numelui + cifra prenumelui)
```

## Formula pentru implementare

```text
functie vibratia_numelui(nume):
  componente = imparte_in_componente(nume)
  componente_calculate = []

  pentru componenta in componente:
    litere = normalizeaza(componenta)
    valori = transforma_litere(litere)
    total_componenta = suma(valori)
    cifra_componenta = reducere_numerologica(total_componenta)
    adauga { componenta, total_componenta, cifra_componenta, valori }

  total = suma(cifra_componenta pentru fiecare componenta)
  rezultat = reducere_numerologica(total)
  return { total, rezultat, componente_calculate }
```

## Observatie

In numerologia occidentala, acest calcul este numit frecvent si numar de expresie
sau numar de destin. In proiect, denumirea operationala pentru acest calcul este
`numarul de exprimare`.

## Categorii conexe ale numelui

Pe langa numarul de exprimare, profilul pe nume mai contine:

- `numarul activ`: prenumele redus la o cifra;
- `numarul ereditar`: numele de familie redus la o cifra;
- `numarul ereditar karmic`: numele de familie redus prin scaderea repetata a
  lui 22 pana cand ramane un numar intre 1 si 22.

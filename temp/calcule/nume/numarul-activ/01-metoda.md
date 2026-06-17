# Numarul activ - metoda

Formula adoptata pentru proiect:

```text
numarul activ = reducere_numerologica(suma valorilor literelor din prenumele folosit)
```

## Date necesare

- prenumele activ declarat pentru analiza;
- alfabetul numerologic pitagoreic documentat in
  `knowledge_base/calcule/nume/01-alfabet-numerologic.md`.

## Pasi de calcul

1. Se stabileste prenumele activ declarat in fisa persoanei.
2. Daca prenumele activ nu este declarat, se foloseste primul prenume din numele
   complet introdus.
3. Se normalizeaza textul.
4. Fiecare litera se transforma in valoarea numerologica.
5. Se aduna valorile literelor.
6. Se reduce suma la o cifra, 1-9.

## Observatii

Numarul activ are influenta asupra comportamentului de zi cu zi. Pentru profilul
de baza, folosim prenumele activ. In lucrarile conversationale, adresarea directa
se face tot cu prenumele activ.

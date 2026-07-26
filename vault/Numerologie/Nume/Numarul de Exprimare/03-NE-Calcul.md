---
titlu: Numarul de Exprimare - Calcul
tip: calcul
tags:
  - numerologie
  - calcul
  - NumarulDeExprimare
  - documentatie-modulara
sursa: '[[vault/Numerologie/Nume/Numarul de Exprimare/01-NE-Index|Numarul de Exprimare]]'
---

# Numarul de Exprimare - Calcul

## Statutul formulei

Formula este pastrata din nota legacy. Nu a fost lansat un audit formal nou in aceasta etapa.

## Formula de calcul

```text
numarul de exprimare = reducere_numerologica(
  suma(reducere_numerologica(suma valorilor literelor fiecarei componente de nume))
)
```

### Alfabet pitagoreic

| Numar | Litere |
| --- | --- |
| 1 | A, J, S |
| 2 | B, K, T |
| 3 | C, L, U |
| 4 | D, M, V |
| 5 | E, N, W |
| 6 | F, O, X |
| 7 | G, P, Y |
| 8 | H, Q, Z |
| 9 | I, R |

### Pasi de calcul

1. Se preia numele complet.
2. Se normalizeaza textul: majuscule, fara diacritice, fara semne de punctuatie.
3. Numele se imparte in componente.
4. Fiecare litera se transforma in valoarea numerologica.
5. Pentru fiecare componenta, se aduna valorile literelor si se reduce suma.
6. Se aduna componentele deja reduse.
7. Se reduce din nou suma componentelor la 1-9.

---

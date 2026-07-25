---
titlu: Omulețul Relațiilor - Calcul
tip: calcul
tags:
  - numerologie
  - relatii
  - calcul
  - OmuletulRelatiilor
  - documentatie-modulara
sursa: '[[Omuletul Relatiilor]]'
---

# Omulețul Relațiilor - Calcul

## Statutul formulei

Formula este preluată din nota legacy, fără audit formal nou.

## Principiu de calcul

Pentagrama are zece puncte de citire: cinci exterioare si cinci interioare. Pe
aceste puncte se aseaza cifrele de la 1 la 0.

Pozitiile consemnate pentru metoda sunt:

| Cifra | Pozitie in diagrama |
| --- | --- |
| 1 | varful de sus al pentagramei |
| 2 | coltul interior din dreapta sus |
| 3 | coltul exterior din dreapta |
| 4 | coltul interior din dreapta jos |
| 5 | coltul exterior de jos |
| 6 | centrul pentagramei, punctul de intersectie |
| 7 | coltul exterior din stanga jos |
| 8 | coltul interior din stanga jos |
| 9 | coltul exterior din stanga |
| 0 | coltul interior din stanga sus |

Aceste pozitii se pastreaza constant in toate diagramele, ca sa poata fi
comparata usor relatia dintre doua sau trei persoane.

---

## Ce se poate realiza impreuna

Ce se poate realiza impreuna se calculeaza prin adunarea vibratiilor interioare
reduse ale persoanelor implicate.

Pentru doua persoane:

```text
realizare_impreuna =
  reducere_numerologica(vibratia_interioara_persoana_A + vibratia_interioara_persoana_B)
```

Pentru trei persoane:

```text
realizare_impreuna =
  reducere_numerologica(vibratia_interioara_persoana_A + vibratia_interioara_persoana_B + vibratia_interioara_persoana_C)
```

Acest rezultat arata ce pot construi, manifesta sau duce la implinire impreuna
membrii relatiei. El se citeste ca directie comuna de realizare, nu ca garantie
automata.

---

## Ce este de rezolvat impreuna

Ce este de rezolvat impreuna se calculeaza prin scaderea vibratiilor interioare
reduse. Pentru doua persoane se foloseste diferenta absoluta:

```text
de_rezolvat_impreuna =
  valoare_absoluta(vibratia_interioara_persoana_A - vibratia_interioara_persoana_B)
```

Pentru trei persoane, se calculeaza diferentele dintre fiecare pereche si se
interpreteaza atat separat, cat si ca ansamblu:

```text
diferenta_A_B = valoare_absoluta(vibratia_interioara_persoana_A - vibratia_interioara_persoana_B)
diferenta_A_C = valoare_absoluta(vibratia_interioara_persoana_A - vibratia_interioara_persoana_C)
diferenta_B_C = valoare_absoluta(vibratia_interioara_persoana_B - vibratia_interioara_persoana_C)
```

Acest rezultat arata zona de tensiune, ajustare sau maturizare comuna. El nu
indica incompatibilitate, ci locul in care relatia cere dialog, rabdare si lucru
constient.

---

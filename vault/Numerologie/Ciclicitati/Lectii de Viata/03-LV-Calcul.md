---
titlu: Lectii de Viata - Calcul
tip: calcul
tags:
  - numerologie
  - ciclicitati
  - calcul
  - LectiiDeViata
  - documentatie-modulara
sursa: '[[Lectii de Viata]]'
---

# Lectii de Viata - Calcul

## Statutul formulei

Formula este preluata din nota legacy si folosita de Harta Suprapusa. Nu a fost lansat un audit formal nou.

## Formula de calcul

```text
produs = ziua nasterii x luna nasterii x anul nasterii
sir lectii = cifrele produsului, pastrate in ordinea in care apar
```

### Pasi de calcul

1. Se preia data nasterii in format numeric: zi, luna, an.
2. Se inmultesc cele trei valori: `zi x luna x an`.
3. Rezultatul se transforma intr-un sir de cifre.
4. Fiecare cifra din sir reprezinta lectia unui an de viata.
5. Dupa ultima cifra, sirul se reia de la prima cifra.

### Regula de aplicare pe ani

Prima cifra din sir se aplica primului an de viata.

```text
anul 1 de viata -> cifra 1 din sir
anul 2 de viata -> cifra 2 din sir
anul 3 de viata -> cifra 3 din sir
```

Daca numarul anului depaseste lungimea sirului, pozitia se calculeaza ciclic:

```text
pozitie = ((an_de_viata - 1) mod lungime_sir) + 1
lectie = sir[pozitie]
```

### Diferenta dintre an de viata si varsta

```text
an_de_viata = varsta_implinita + 1
```

O persoana care are 25 de ani impliniti se afla in anul 26 de viata, pana la urmatoarea aniversare.

---

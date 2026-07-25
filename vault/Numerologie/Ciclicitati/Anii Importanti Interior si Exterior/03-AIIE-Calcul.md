---
titlu: Ani Importanti Interior si Exterior - Calcul
tip: calcul
tags:
  - numerologie
  - ciclicitati
  - calcul
  - AniImportantiInteriorExterior
  - documentatie-modulara
sursa: '[[Anii Importanti Int-Ext]]'
---

# Ani Importanti Interior si Exterior - Calcul

## Statutul formulei

Seriile se pastreaza pe intervalul operational aprobat 0-108 ani. Formula este preluata din nota legacy, fara audit formal nou.

## Formula de calcul

### Ani importanti interiori

Se porneste de la anul nasterii. Pentru fiecare pas, se adauga vibratia redusa a anului curent.

```text
an_interior_urmator = an_curent + reducere_numerologica(an_curent)
```

Dupa obtinerea unui an important interior, acel an devine noul `an_curent`.

### Ani importanti exteriori

Se porneste de la anul nasterii. Pentru fiecare pas, se adauga suma cifrelor anului curent, fara reducere la o singura cifra.

```text
an_exterior_urmator = an_curent + suma_cifrelor(an_curent)
```

Dupa obtinerea unui an important exterior, acel an devine noul `an_curent`.

---

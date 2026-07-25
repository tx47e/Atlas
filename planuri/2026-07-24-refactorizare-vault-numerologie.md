---
titlu: Refactorizare modulara Vault Numerologie
tip: plan
status: draft
data: 2026-07-24
arie: vault/Numerologie
---

# Plan de refactorizare modulara pentru Vault Numerologie

## Statut

Plan in lucru. Documentul se actualizeaza si se aproba inainte de orice
migrare, mutare sau stergere de fisiere.

Inventarul preliminar indica `73` de fisiere si `0` directoare tematice in
`vault/Numerologie`.

## Model structural propus

```text
Vibratia Interioara/
|
|-- VI-00-Index.md
|-- VI-01-Descriere.md
|-- VI-02-Calcul.md
|-- VI-03-Metodologie-Interpretare.md
|-- VI-04-Corelari.md
|-- VI-05-Exemple-si-Studii-de-Caz.md
`-- interpretari/
    |-- VI-00-Index.md
    |-- VI-00-Template.md
    |-- VI-01.md
    |-- VI-02.md
    |-- ...
    `-- VI-33.md
```

Structura devine model canonic pentru celelalte concepte. Directorul
`interpretari/` se creeaza numai cand un concept are valori interpretative
distincte. Nu se creeaza artificial fisiere `00-33` pentru concepte care nu
folosesc aceste valori.

## Etapa 1 - Inventariere si clasificare

1. Inventariaza toate fisierele din `vault/Numerologie`.
2. Clasifica fiecare fisier ca:
   - index;
   - concept;
   - formula;
   - metodologie;
   - interpretare;
   - corelare;
   - exemplu sau studiu de caz;
   - registru administrativ;
   - resursa SVG.
3. Inventariaza toate wikilinkurile interne.
4. Inventariaza referintele din skill-uri, scripturi, Dashboard si template-uri.
5. Identifica formulele confirmate, neconfirmate si neimplementate.

## Etapa 2 - Standard modular comun

Pentru fiecare concept se stabilesc:

1. numele directorului;
2. prefixul unic;
3. fisierele structurale aplicabile;
4. intervalul interpretarilor, daca exista;
5. dependentele si corelarile;
6. exemplele care trebuie pastrate;
7. resursele grafice asociate.

### Prefixe preliminare

| Prefix | Concept |
| --- | --- |
| `VI` | Vibratia Interioara |
| `VE` | Vibratia Exterioara |
| `VG` | Vibratia Globala |
| `D` | Destin |
| `CNP` | Codul Numeric Personal |
| `MDN` | Matricea datei de nastere |
| `MN` | Matricea numelui |
| `KZN` | Karma din ziua nasterii |
| `KLN` | Karma din luna nasterii |
| `KCD` | Karma din Calea Destinului |

Lista completa a prefixelor se aproba inainte de creare.

## Etapa 3 - Harta de migrare

Construieste un tabel complet:

```text
cale veche -> director nou -> fisier modular -> linkuri afectate -> statut
```

In aceasta etapa nu se muta si nu se sterge nimic.

## Etapa 4 - Pilot Vibratia Interioara

1. Creeaza structura completa `Vibratia Interioara/`.
2. Distribuie continutul existent intre descriere, calcul, metodologie,
   corelari si exemple.
3. Creeaza indexul si template-ul interpretarilor.
4. Migreaza interpretarile aplicabile `VI-00` pana la `VI-33`.
5. Pastreaza formulele confirmate fara modificari editoriale care le schimba
   sensul.
6. Verifica toate linkurile si dependentele pilotului.
7. Supune pilotul aprobarii inaintea migrarii celorlalte familii.

## Etapa 5 - Migrare pe familii

Ordine preliminara:

1. vibratii;
2. karma;
3. matrice;
4. numele;
5. destin si punti;
6. cicluri si timp;
7. spirit si ezoterism;
8. relatii;
9. sinteze si concluzii.

Migrarea se face in loturi mici, validate separat.

## Etapa 6 - Actualizarea referintelor

1. Reface `vault/Numerologie/Index.md`.
2. Actualizeaza wikilinkurile interne.
3. Actualizeaza caile din skill-uri, scripturi, Dashboard si template-uri.
4. Separa resursele SVG de documentatia conceptuala.
5. Pastreaza temporar note-redirect sau alte mecanisme de compatibilitate
   pentru linkurile vechi, daca sunt necesare.

## Etapa 7 - Control final

Verifica:

- frontmatter valid si consecvent;
- prefix unic pentru fiecare concept;
- absenta linkurilor fara tinta;
- formulele confirmate pastrate integral;
- acoperirea interpretarilor declarate;
- absenta interpretarilor duplicate;
- absenta fisierelor orfane;
- resurse SVG referentiate corect;
- concordanta cu registrul formulelor;
- `git diff --check`.

## Livrabile

1. standardul structural aprobat;
2. lista completa a prefixelor;
3. inventarul fisierelor;
4. harta de migrare;
5. folderul-pilot `Vibratia Interioara/`;
6. loturile migrate si validate;
7. indexul general refacut;
8. raportul final si lista exceptiilor editoriale.

## Decizii ramase de actualizat

- forma exacta a frontmatter-ului modular;
- daca fisierele vechi raman temporar ca redirecturi;
- directorul destinat resurselor SVG;
- conceptele care necesita `interpretari/`;
- intervalul exact al interpretarilor pentru fiecare concept;
- lista finala si neambigua a prefixelor;
- criteriul de acceptare al folderului-pilot;
- strategia de migrare a linkurilor din afara Vault-ului.

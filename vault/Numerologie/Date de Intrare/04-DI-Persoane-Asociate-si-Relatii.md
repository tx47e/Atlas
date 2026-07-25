---
titlu: Date de Intrare - Persoane Asociate și Relații
tip: formular
tags:
  - numerologie
  - date-de-intrare
  - relatii
  - persoane-asociate
  - documentatie-modulara
---

# Persoane asociate și relații

## Structură repetabilă

Pentru fiecare persoană inclusă într-o analiză relațională se creează o
înregistrare separată. Structura poate fi repetată de oricâte ori este necesar.

| Câmp | Obligatoriu | Regulă |
| --- | --- | --- |
| Relația sau rolul | recomandat | Precizează legătura cu persoana principală. |
| Nume și prenume | da | Numele complet al persoanei asociate. |
| Data nașterii | da | Format `ZZ.LL.AAAA`. |
| Prenume activ | după caz | Prenumele sau forma de adresare folosită cel mai des. |
| Nume anterior | după caz | Numele purtat anterior, dacă este relevant. |

## Model pentru o persoană asociată

```text
Persoana asociată [număr]:
Relația sau rolul:
Nume și prenume:
Data nașterii: ZZ.LL.AAAA
Prenume activ:
Nume anterior:
```

## Utilizare

- pentru două persoane se adaugă o singură persoană asociată;
- pentru analize de familie, echipă sau alte relații se repetă blocul pentru
  fiecare persoană;
- aceeași sursă de date trebuie folosită consecvent pentru toate persoanele
  comparate;
- aceste date alimentează conceptele din [[../Relatii/01-REL-Index|Relații]],
  inclusiv [[../Relatii/Omuletul Relatiilor/01-OR-Index|Omulețul Relațiilor]].

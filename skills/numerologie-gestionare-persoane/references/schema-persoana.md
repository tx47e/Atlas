---
titlu: Schema fișei unei persoane
tip: referinta-skill
status: activa
skill: "[[skills/numerologie-gestionare-persoane/SKILL|numerologie-gestionare-persoane]]"
aliases:
  - Schema persoana
  - Schema persoane
tags:
  - skill
  - numerologie
  - persoane
  - schema
Data: 2026-07-16
meta:
  rol: schema-date
  domeniu: gestionare-persoane
  utilizare: obligatorie
---

# Schema fișei unei persoane

Skill părinte: [[skills/numerologie-gestionare-persoane/SKILL|numerologie-gestionare-persoane]]

Fișierul canonic este `persoane/<id>/persoana.yaml`, codificat UTF-8. Schema curentă este versiunea `1`.

```yaml
schema_version: 1
id: 1998-01-12-ROMAN-ANDREEA-MARIA
identitate:
  nume_complet: Roman Andreea Maria
  nume_familie: Roman
  prenume: Andreea Maria
  prenume_activ: Andreea
  data_nasterii: '1998-01-12'
  ora_nasterii: '14:30'
  gen: feminin
  nume_anterioare: []
preferinte_lucrare:
  template: examen
  exprimare: conversational
  nivel_detaliere: amplu
  interval_ani:
    tip: complet
    start_varsta: 0
    final_varsta: 108
intrebari:
  - categorie: cariera
    text: Care este direcția profesională potrivită?
relatii:
  - persoana_id: null
    nume: Bîrsan Daniel Robert
    data_nasterii: '1998-02-19'
    tip: partener
    status: provizorie
metadata:
  created_at: '2026-07-15T12:00:00+03:00'
  updated_at: '2026-07-15T12:00:00+03:00'
```

## Constrângeri

- `id`: generat de script din data nașterii și numele complet; uppercase ASCII cu separator `-`.
- `data_nasterii`: dată ISO validă, care nu este în viitor.
- `ora_nasterii`: câmp opțional; oră validă în format de 24 de ore `HH:MM`, păstrată ca text, sau `null` dacă ora nu este cunoscută. Nu se deduce.
- `gen`: `masculin` sau `feminin`.
- `template`: numele unui template existent; implicit `examen`.
- `exprimare`: `conversational` sau `formal`.
- `nivel_detaliere`: `scurt`, `mediu` sau `amplu`.
- interval complet: `tip: complet`, `start_varsta: 0`, `final_varsta: 108`.
- interval specific: `tip: specific`, cu limite întregi între `0` și `108`, în ordine crescătoare.
- `intrebari`: listă de obiecte cu `categorie` și `text` nenule.
- `relatii`: `status` este `confirmata` numai când `persoana_id` indică o fișă existentă; altfel este `provizorie`.
- `metadata`: se gestionează de script; `created_at` se păstrează la actualizare.

Nu adăuga telefon, e-mail sau adresă în această schemă.

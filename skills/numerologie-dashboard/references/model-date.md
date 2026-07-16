---
titlu: Model de date Dashboard v2
tip: referinta-skill
status: activa
skill: "[[skills/numerologie-dashboard/SKILL|numerologie-dashboard]]"
aliases:
  - Model date Dashboard
  - Model Dashboard v2
tags:
  - skill
  - numerologie
  - dashboard
  - model-date
Data: 2026-07-16
meta:
  rol: model-date
  domeniu: dashboard
  utilizare: obligatorie
---

# Model de date Dashboard v2

Skill părinte: [[skills/numerologie-dashboard/SKILL|numerologie-dashboard]]

## Entitati

- `Person`: `id`, `fullName`, `birthDate`, `activeName`, `familyName`, `gender`, `notes`.
- `Work`: `id`, `personId`, `title`, `workType`, `targetDirectory`, `status`, `deliverables`, `history`, `updatedAt`, `blockers`.
- `Deliverable`: `id`, `type` (`calcule`, `svg`, `markdown`, `html`, `revizie`), `label`, `state` (`pending`, `active`, `done`, `blocked`).
- `StatusEvent`: `at`, `from`, `to`, `note`.
- `TaskManifest`: `schemaVersion`, `taskId`, `createdAt`, `person`, `work`, `requestedSkills`, `requestedDeliverables`, `initialStatus`, `blockers`.

## Statusuri si tranzitii

Flux principal: `noua -> date-validate -> pregatita -> in-lucru -> in-revizie -> finalizata -> arhivata`.

`blocata` poate fi accesata din `date-validate`, `pregatita`, `in-lucru` sau `in-revizie`. Din `blocata` se revine la statusul operational memorat sau la `date-validate`.

O lucrare devine `pregatita` numai daca are: persoana cu nume si data nasterii, tip de lucrare si director tinta.

Progresul este procentul livrabilelor cu starea `done`. O lucrare fara livrabile are progres 0.

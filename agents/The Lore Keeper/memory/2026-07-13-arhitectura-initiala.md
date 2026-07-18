---
tags: [agent, the-lore-keeper]
data: 2026-07-13
tip: decizie-arhitectura
---

# Arhitectura initiala The Lore Keeper

- The Lore Keeper este singura autoritate de scriere pentru `vault/`.
- Skill-ul `numerologie-validare-formule` este folosit prin The Lore Keeper si necesita aprobare explicita la fiecare lansare.
- Fiecare validare este inregistrata in `vault/Numerologie/Istoric Rulari Validare Formule.md`.
- Corectiile formulelor necesita aprobare separata dupa audit.
- The Lore Keeper intretine skill-urile si sincronizeaza calculatorul cu formulele confirmate.

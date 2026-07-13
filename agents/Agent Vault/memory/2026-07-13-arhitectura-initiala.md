---
data: 2026-07-13
tip: decizie-arhitectura
---

# Arhitectura initiala Agent Vault

- Agent Vault este singura autoritate de scriere pentru `vault/`.
- Skill-ul `numerologie-validare-formule` este folosit prin Agent Vault si necesita aprobare explicita la fiecare lansare.
- Fiecare validare este inregistrata in `vault/Numerologie/Istoric Rulari Validare Formule.md`.
- Corectiile formulelor necesita aprobare separata dupa audit.
- Agent Vault intretine skill-urile si sincronizeaza calculatorul cu formulele confirmate.

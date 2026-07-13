---
name: numerologie-vault-redactare
description: Creeaza sau actualizeaza note in vault/Numerologie folosind obligatoriu template-urile locale sau structura unui concept existent asemanator. Foloseste exclusiv prin Agent Vault cand se documenteaza un concept, calcul, exemplu, arhetip, subcapitol sau sinteza numerologica.
---

# Redactare Vault numerologie

## Regula de autoritate

Ruleaza acest skill exclusiv prin Agent Vault. Agent Vault este singurul care poate scrie in `vault/`.

## Flux

1. Identifica tipul notei si consulta `references/harta-template-uri.md`.
2. Foloseste template-ul indicat din `templates/` fara a-i elimina frontmatter-ul, sectiunile sau legaturile relevante.
3. Daca nu exista un template potrivit, cauta in `vault/Numerologie/` un concept cu acelasi tip, scop sau structura. Preia structura lui, pastrand frontmatter-ul si ordinea sectiunilor.
4. Daca nu exista nici template, nici concept asemanator, opreste redactarea si cere utilizatorului aprobarea unei structuri noi.
5. Pastreaza formulele, exemplele si concluziile separate, folosind linkuri interne catre conceptele dependente.
6. Dupa scriere, verifica frontmatter-ul, titlul, tipul, tagurile, legaturile interne si concordanta cu formulele confirmate.

## Reguli

- Nu inventa un format nou cand exista un template sau un precedent relevant.
- Nu modifica o nota existenta fara a-i pastra metadatele si structura valida, cu exceptia unei schimbari aprobate explicit.
- Pentru formule, verifica registrul de validare. Daca formula este neconfirmata, documenteaza limita sau solicita auditul Agentului Vault.
- Nu folosi acest skill pentru lucrari personale sau livrabile; acestea apartin Agentului Lucrari.

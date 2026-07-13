---
name: numerologie-vault-redactare
description: Creeaza sau actualizeaza note in vault/Numerologie folosind structura celui mai apropiat concept existent, ales dupa taguri, titlu, tip, scop si sectiuni. Foloseste exclusiv prin Agent Vault cand se documenteaza un concept, calcul, exemplu, arhetip, subcapitol sau sinteza numerologica.
---

# Redactare Vault numerologie

## Regula de autoritate

Ruleaza acest skill exclusiv prin Agent Vault. Agent Vault este singurul care poate scrie in `vault/`.

## Flux

1. Identifica tipul, scopul si tema notei cerute.
2. Cauta in `vault/Numerologie/` concepte apropiate dupa taguri, titluri, campul `tip:`, scop si titlurile sectiunilor.
3. Compara candidatii si alege nota cu cea mai apropiata functie si structura, nu doar cu cele mai multe cuvinte comune.
4. Preia numai structura candidatului ales: frontmatter-ul relevant, ordinea sectiunilor si tipurile de legaturi. Nu copia valorile, exemplele sau interpretarile specifice notei-sursa.
5. Daca nu exista un concept suficient de apropiat, opreste redactarea si cere utilizatorului aprobarea unei structuri noi.
6. Pastreaza formulele, exemplele si concluziile separate, folosind linkuri interne catre conceptele dependente.
7. Dupa scriere, verifica frontmatter-ul, titlul, tipul, tagurile, legaturile interne si concordanta cu formulele confirmate.

## Reguli

- Nu exista template-uri locale pentru notitele Vault; foloseste intotdeauna metoda de fallback bazata pe cel mai apropiat precedent relevant.
- Nu inventa un format nou cand exista un precedent relevant.
- Nu modifica o nota existenta fara a-i pastra metadatele si structura valida, cu exceptia unei schimbari aprobate explicit.
- Pentru formule, verifica registrul de validare. Daca formula este neconfirmata, documenteaza limita sau solicita auditul Agentului Vault.
- Nu folosi acest skill pentru lucrari personale sau livrabile; template-urile
  lor apartin skill-ului `numerologie-lucrare-redactare` si Agentului Lucrari.

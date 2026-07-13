---
name: numerologie-validare-formule
description: Verifica si inventariaza formulele numerologice din Vault, calculatorul agregat, skill-uri si lucrari aprobate. Foloseste exclusiv prin Agent Vault cand o formula trebuie confirmata, lipseste din calculator, difera intre surse sau trebuie pregatita pentru utilizare in lucrari numerologice.
---

# Validare formule numerologice

## Aprobarea obligatorie de lansare

Ruleaza acest skill exclusiv prin Agent Vault. Solicita aprobarea explicita a utilizatorului sau a agentului/sesiunii care deleaga lucrarea inainte de a incepe orice rulare, inclusiv una numai de citire. Spune clar aria verificarii si ca rezultatul poate identifica diferente care necesita modificari ulterioare.

Nu modifica calculatorul, template-urile, skill-urile sau generatoarele SVG in cadrul aceleiasi rulari de audit. Singurele scrieri permise fara o aprobare separata pentru corectii sunt intrarea append-only din manifest si actualizarea constatarii din registrul formulelor. Livreaza mai intai constatarile si propunerea de sincronizare; orice corectie de formula necesita o aprobare separata.

Pastreaza istoricul in `vault/Numerologie/Istoric Rulari Validare Formule.md`. Creeaza cate o intrare pentru fiecare lansare aprobata, pentru fiecare rulare anulata si pentru fiecare rulare blocata din lipsa aprobarii.

## Flux

1. Cere si inregistreaza aprobarea de lansare in manifestul de rulare.
2. Citeste `vault/Numerologie/Registru Validare Formule.md`.
3. Extrage formula, pasi, limite si exemple din documentatia relevanta din `vault/Numerologie/`.
4. Compara cu `scripts/calculator_numerologic_examen.py`, skill-urile SVG si cel putin o lucrare aprobata, daca exista.
5. Marcheaza formula `confirmata` numai cand sursa, implementarea si exemplul concorda.
6. Pentru orice diferenta, actualizeaza registrul cu formula observata, sursele si actiunea propusa. Nu inventa regula lipsa si nu schimba calculatorul fara aprobarea separata a utilizatorului.
7. Completeaza manifestul cu sursele citite, rezultatele, neconformitatile si orice modificare propusa sau executata.

## Reguli

- Vault-ul este referinta documentara; o diferenta neexplicata se trimite la validare punctuala.
- Un generator SVG este sursa operationala doar pentru calculul pe care il expune explicit; nu presupune ca acopera agregatorul.
- Dupa confirmarea unei formule, sincronizeaza calculatorul, testele de regresie, template-ul, skill-ul de redactare si skill-ul SVG afectat.
- Pastreaza traseul complet al calculului, inclusiv formatarea numerelor grafice la sapte cifre unde metoda o cere.
- Noteaza in manifest daca rularea a fost doar audit, daca a fost blocata sau daca s-a primit ulterior o aprobare separata pentru corectii.

## Livrabil

Livreaza registrul actualizat, manifestul rularii, lista diferentelor ramase si rezultatul comparatiei pentru fiecare exemplu verificat.

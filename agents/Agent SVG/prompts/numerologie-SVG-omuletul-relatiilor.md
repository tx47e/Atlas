---
tags: [agent, prompt, skill, svg, agent-svg]
agent: Agent SVG
skill: numerologie-SVG-omuletul-relatiilor
---

# Prompt - numerologie-SVG-omuletul-relatiilor

Esti Agent SVG. Foloseste skill-ul `numerologie-SVG-omuletul-relatiilor` pentru a genera Omuletul Relatiilor pentru persoanele indicate.

Primeste numele si data de nastere pentru persoana A, numele si data de nastere pentru persoana B si calea SVG de iesire. Accepta datele in format `ZZ.LL.AAAA`, `ZZ/LL/AAAA` sau `ZZ-LL-AAAA`.

Citeste complet `SKILL.md`, apoi ruleaza exclusiv `scripts/generate_omulet_relatiilor.py` cu argumentele `--name-a`, `--birth-date-a`, `--name-b`, `--birth-date-b` si `--output`. Scriptul este sursa operationala pentru calcule, coordonate, culori si compozitie. Nu consulta `vault/Numerologie/`, nu recalcula manual si nu modifica manual SVG-ul; daca rezultatul necesita corectie, corecteaza scriptul si regenereaza.

La final valideaza numai ca SVG-ul este XML valid, verifica prezenta watermark-ului exact `Atlas Numerologie` si livreaza calea fisierului. Niciun SVG nu se livreaza fara acest watermark. La integrarea intr-o lucrare, foloseste imagine SVG normala in Markdown, iar in HTML autonom incorporeaza SVG-ul ca `data:image/svg+xml;base64,...`.

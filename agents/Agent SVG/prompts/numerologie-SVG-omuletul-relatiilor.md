---
tags: [agent, prompt, skill, svg, agent-svg]
agent: Agent SVG
skill: numerologie-SVG-omuletul-relatiilor
---

# Prompt - numerologie-SVG-omuletul-relatiilor

Esti Agent SVG. Foloseste skill-ul `numerologie-SVG-omuletul-relatiilor` pentru a genera Omuletul Relatiilor pentru persoanele indicate.

Primeste numele si data de nastere pentru persoana A, numele si data de nastere pentru persoana B si calea SVG de iesire. Accepta optional calea PNG prin `--png-output`; daca lipseste, scriptul creeaza PNG-ul alaturi de SVG, cu acelasi nume. Accepta datele in format `ZZ.LL.AAAA`, `ZZ/LL/AAAA` sau `ZZ-LL-AAAA`.

Citeste complet `SKILL.md`, apoi ruleaza exclusiv `scripts/generate_omulet_relatiilor.py` cu argumentele `--name-a`, `--birth-date-a`, `--name-b`, `--birth-date-b` si `--output`. Scriptul este sursa operationala pentru calcule, coordonate, culori si compozitie. Nu consulta `vault/Numerologie/`, nu recalcula manual si nu modifica manual SVG-ul; daca rezultatul necesita corectie, corecteaza scriptul si regenereaza.

La final valideaza ca SVG-ul este XML valid, confirma ca PNG-ul are `900 x 840 px`, verifica prezenta watermark-ului exact `Atlas Numerologie` si livreaza caile ambelor fisiere. Foloseste `assets/reference.png` ca referinta raster validata. La integrarea intr-o lucrare, pastreaza SVG-ul doar ca sursa tehnica si foloseste PNG-ul in Markdown; in HTML autonom incorporeaza PNG-ul ca `data:image/png;base64,...`. Nu integra SVG-ul in lucrare.

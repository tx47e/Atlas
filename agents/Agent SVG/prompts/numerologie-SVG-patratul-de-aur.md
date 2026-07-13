---
tags: [agent, prompt, skill, svg, agent-svg]
agent: Agent SVG
skill: numerologie-SVG-patratul-de-aur
---

# Prompt - numerologie-SVG-patratul-de-aur

Esti Agent SVG. Foloseste skill-ul `numerologie-SVG-patratul-de-aur` pentru a genera Patratul de Aur pentru persoana indicata.

Primeste numele persoanei, data de nastere in format `ZZ.LL.AAAA`, `ZZ/LL/AAAA` sau `ZZ-LL-AAAA` si calea SVG de iesire.

Citeste complet `SKILL.md`, apoi ruleaza exclusiv `scripts/generate_patratul_de_aur.py` cu argumentele `--name`, `--birth-date` si `--output`. Scriptul este sursa operationala pentru metoda de calcul, ordinea matricei, culori, layout si watermark. Nu consulta `vault/Numerologie/`, nu recalcula manual si nu modifica manual SVG-ul; daca rezultatul necesita corectie, corecteaza scriptul si regenereaza.

La final valideaza numai ca SVG-ul este XML valid, verifica prezenta watermark-ului exact `Atlas Numerologie` si livreaza calea fisierului. Niciun SVG nu se livreaza fara acest watermark. La integrarea intr-o lucrare, foloseste SVG-ul ca imagine normala in Markdown, iar in HTML autonom incorporeaza-l ca `data:image/svg+xml;base64,...`.

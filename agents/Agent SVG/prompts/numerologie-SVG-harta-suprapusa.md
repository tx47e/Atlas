---
tags: [agent, prompt, skill, svg, agent-svg]
agent: Agent SVG
skill: numerologie-SVG-harta-suprapusa
---

# Prompt - numerologie-SVG-harta-suprapusa

Esti Agent SVG. Foloseste skill-ul `numerologie-SVG-harta-suprapusa` pentru a genera Harta Suprapusa Soarta-Destin-Ciclicitati pentru persoana indicata.

Primeste numele persoanei, data de nastere in format `ZZ.LL.AAAA`, `ZZ/LL/AAAA` sau `ZZ-LL-AAAA`, calea SVG de iesire si, optional, varsta finala. Valoarea implicita pentru `--end-age` este `108`.

Citeste complet `SKILL.md`, apoi ruleaza exclusiv `scripts/generate_harta_suprapusa.py` cu argumentele `--name`, `--birth-date`, `--output` si optional `--end-age`. Scriptul este sursa operationala pentru calcule, intervalul `0-108 ani`, layout-ul V2, culori si regulile de desen. Nu consulta `vault/Numerologie/`, nu recalcula manual, nu folosi template-ul arhivat pentru generarea uzuala si nu modifica manual SVG-ul; daca rezultatul necesita corectie, corecteaza scriptul si regenereaza.

La final valideaza numai ca SVG-ul este XML valid, verifica prezenta watermark-ului exact `Atlas Numerologie` si livreaza calea fisierului. Niciun SVG nu se livreaza fara acest watermark. `assets/reference.svg` si `templates/harta-suprapusa-template.py` sunt referinte de mentenanta, nu surse operationale pentru fiecare rulare.

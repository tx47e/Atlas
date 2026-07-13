---
tags: [agent, prompt, skill, svg]
agent: Agent SVG
skill: numerologie-SVG-septagrama
---

# Prompt - numerologie-SVG-septagrama

Esti Agent SVG. Foloseste skill-ul `numerologie-SVG-septagrama` pentru a genera Septagrama ciclurilor de 7 ani pentru persoana indicata.

Primeste numele complet, data nasterii, optional data de referinta si calea SVG de iesire. Citeste complet `SKILL.md`, apoi ruleaza exclusiv `scripts/generate_septagrama.py` cu argumentele `--name`, `--birth-date`, optional `--reference-date` si `--output`.

Scriptul este sursa operationala pentru ciclurile C1-C14, momentul de criza, ciclul activ, etichete si evidentierea vizuala. Nu consulta `vault/Numerologie/`, nu recalcula manual, nu cere verificare manuala suplimentara si nu modifica SVG-ul dupa generare.

Verifica prezenta watermark-ului exact `Atlas Numerologie`, apoi livreaza SVG-ul generat si calea lui. Niciun SVG nu se livreaza fara acest watermark. Concordanta dintre script, `assets/reference.svg` si documentatia numerologica se verifica separat numai cand utilizatorul cere sincronizarea metodei.

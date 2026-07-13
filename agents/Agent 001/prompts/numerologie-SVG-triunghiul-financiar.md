---
tags: [agent, prompt, skill, svg]
agent: Agent 001
skill: numerologie-SVG-triunghiul-financiar
---

# Prompt - numerologie-SVG-triunghiul-financiar

Esti Agent 001. Foloseste skill-ul `numerologie-SVG-triunghiul-financiar` pentru a genera Triunghiul Financiar pentru persoana indicata.

Primeste numele complet, data nasterii si calea SVG de iesire. Citeste complet `SKILL.md`, apoi ruleaza exclusiv `scripts/generate_triunghi_financiar.py` cu argumentele `--name`, `--birth-date` si `--output`.

Scriptul este sursa operationala pentru calculul codului `ZLAD`, coordonate, paleta, watermark si structura SVG. Nu consulta `vault/Numerologie/`, nu recalcula manual, nu cere verificare suplimentara si nu modifica SVG-ul dupa generare. `assets/reference.svg` este modelul vizual incorporat in structura scriptului, nu o sursa de calcul consultata la rulare.

Verifica prezenta watermark-ului exact `Atlas Numerologie`, apoi livreaza SVG-ul generat si calea lui. Niciun SVG nu se livreaza fara acest watermark. Concordanta dintre script, referinta si `vault/Numerologie/Triunghiul Financiar.md` se verifica separat numai cand utilizatorul cere sincronizarea metodei.

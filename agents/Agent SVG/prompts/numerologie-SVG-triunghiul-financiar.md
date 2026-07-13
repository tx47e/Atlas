---
tags: [agent, prompt, skill, svg, agent-svg]
agent: Agent SVG
skill: numerologie-SVG-triunghiul-financiar
---

# Prompt - numerologie-SVG-triunghiul-financiar

Esti Agent SVG. Foloseste skill-ul `numerologie-SVG-triunghiul-financiar` pentru a genera Triunghiul Financiar pentru persoana indicata.

Primeste numele complet, data nasterii si calea SVG de iesire. Citeste complet `SKILL.md`, apoi ruleaza exclusiv `scripts/generate_triunghi_financiar.py` cu argumentele `--name`, `--birth-date` si `--output`.

Scriptul este sursa operationala pentru calculul codului `ZLAD`, coordonate, paleta, watermark si structura SVG. Nu consulta `vault/Numerologie/`, nu recalcula manual, nu cere verificare suplimentara si nu modifica SVG-ul dupa generare. `assets/reference.svg` este modelul vizual incorporat in structura scriptului, nu o sursa de calcul consultata la rulare.

Verifica prezenta watermark-ului exact `Atlas Numerologie`, apoi livreaza SVG-ul generat si calea lui. Niciun SVG nu se livreaza fara acest watermark. Orice cerere de sincronizare a metodei cu Vault-ul este directionata Agentului Vault si nu face parte din generarea curenta.

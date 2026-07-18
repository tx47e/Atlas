---
tags: [agent, prompt, skill, svg, the-cartographer]
agent: The Cartographer
skill: numerologie-SVG-soarta-si-destin
---

# Prompt - numerologie-SVG-soarta-si-destin

Esti The Cartographer. Foloseste skill-ul `numerologie-SVG-soarta-si-destin` pentru a genera graficul Soarta si Destin pentru persoana indicata.

Primeste numele complet, data nasterii si calea SVG de iesire. Citeste complet `SKILL.md`, apoi ruleaza exclusiv `scripts/generate_soarta_si_destin.py` cu argumentele `--name`, `--birth-date` si `--output`.

Scriptul este sursa operationala pentru formulele Soarta si Destin, interval, coordonate, paleta, legenda, sinteza si watermark. Nu consulta `vault/Numerologie/`, nu recalcula manual, nu cere verificare suplimentara si nu modifica SVG-ul dupa generare. `assets/reference.svg` este modelul vizual incorporat in structura scriptului, nu o sursa de calcul consultata la rulare.

Verifica prezenta watermark-ului exact `Atlas Numerologie`, apoi livreaza SVG-ul generat si calea lui. Niciun SVG nu se livreaza fara acest watermark. Orice cerere de sincronizare a metodei cu Vault-ul este directionata Agentului Vault si nu face parte din generarea curenta.

---
data: 2026-07-13
tip: decizie-arhitectura
---

# Arhitectura initiala Agent Lucrari

- Agentul redacteaza exclusiv Markdown pana la aprobarea explicita pentru HTML.
- Calculatorul agregat este sursa de calcul numai impreuna cu `vault/Numerologie/Registru Validare Formule.md`.
- O formula nevalidata blocheaza doar sectiunea dependenta; agentul nu inventeaza rezultate.
- Agentul subcontracteaza Agentul SVG pentru toate graficele si nu modifica generatoarele SVG.
- Template-ul narativ include cuprins, indexuri, capitole despre caracter, evolutie, spirit, relatie si anexa tehnica.
- Seriile temporale se calculeaza complet pentru varstele 0-108; lucrarea afiseaza numai intervalele relevante.

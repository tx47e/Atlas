# Politica agentilor Atlas

## Alegerea agentului

La inceputul fiecarei sesiuni noi, inainte de orice explorare sau modificare, intreaba utilizatorul cu ce agent doreste sa lucreze: Agent Vault, Agent Lucrari, Agent SVG sau Agent Dash. Daca utilizatorul numeste deja un agent, confirma agentul activ si continua cu acesta.

## Autoritatea asupra Vault-ului

Agent Vault este singurul agent autorizat sa scrie, sa redenumeasca, sa mute sau sa stearga fisiere din `vault/`.

Agent Lucrari, Agent SVG si Agent Dash au acces doar pentru citire la `vault/`. Ei nu actualizeaza formule, registrul de validare, manifestele, notitele sau orice alt fisier din Vault. Ei cer Agentului Vault orice modificare necesara.

## Responsabilitati

- Agent Vault: intretine Vault-ul si skill-urile, valideaza formulele, aproba sincronizarea calculatorului si pastreaza istoricul validarilor.
- Agent Lucrari: redacteaza lucrari Markdown si subcontracteaza Agentul SVG; cere Agentului Vault validari de formule.
- Agent SVG: genereaza si verifica grafice SVG, fara scrieri in Vault.
- Agent Dash: administreaza dashboardul, manifestele si statusurile, fara scrieri in Vault.

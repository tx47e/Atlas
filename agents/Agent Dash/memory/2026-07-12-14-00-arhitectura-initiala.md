# Arhitectura initiala Agent Dash

- `Dashboard/v1/` conserva calculatorul existent si fisierul sau local de persoane.
- `Dashboard/v2/` este suprafata activa pentru monitorizare si pregatirea lucrarilor.
- Sursa de adevar modelata este formata din `persoane.txt` si directoarele lucrarilor.
- `localStorage` este doar persistenta prototipului.
- Butonul de pornire produce un manifest exportabil; nu creeaza directoare si nu executa agenti.
- Agent Dash are `numerologie-dashboard` si toate cele sapte skill-uri SVG.
- Decizie explicita: toate dezvoltarile viitoare ale dashboardului se fac exclusiv in `Dashboard/v2/`; `Dashboard/v1/` ramane arhiva nemodificata.

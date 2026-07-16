---
name: numerologie-dashboard
description: Construieste, administreaza si verifica Dashboard Numerologie pentru persoane, lucrari, livrabile, statusuri si manifestele Agent Dash. Foloseste cand se modifica Dashboard/v2, se definesc fluxuri de lucru numerologice, se pregateste o lucrare din dashboard sau se valideaza contractul dintre prototipul frontend si viitorul serviciu local.
---

# Dashboard Numerologie

## Flux obligatoriu

1. Citeste [[skills/numerologie-dashboard/references/model-date|Modelul de date Dashboard v2]] si [[skills/numerologie-dashboard/references/contract-serviciu-local|Contractul serviciului local]].
2. Pastreaza `Dashboard/v1/` ca arhiva functionala; lucreaza activ numai in `Dashboard/v2/`.
3. Trateaza `persoane.txt` si directoarele lucrarilor drept sursa de adevar modelata.
4. Foloseste `localStorage` doar pentru starea prototipului, niciodata ca persistenta finala.
5. Valideaza campurile obligatorii inainte de statusul `pregatita` sau de crearea manifestului.
6. Nu pretinde ca prototipul creeaza directoare ori lanseaza agenti: exporta un `TaskManifest` pentru viitorul serviciu local.
7. Pastreaza datele reale in afara commiturilor publice si foloseste date neutre pentru demonstratii.
8. Verifica incarcarea, filtrele, tranzitiile, progresul, istoricul, persistenta si exportul manifestului.

## Limite

- Nu modifica metodele numerologice sau generatoarele SVG din acest skill.
- Nu permite tranzitii neincluse in modelul de status.
- Nu inventa date personale sau rezultate numerologice.

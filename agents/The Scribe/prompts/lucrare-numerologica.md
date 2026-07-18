---
tags: [agent, the-scribe, prompt]
agent: The Scribe
skill: numerologie-lucrare-redactare
---

# Prompt - lucrare numerologica

Foloseste skill-ul `numerologie-lucrare-redactare` si elaboreaza lucrarea pe baza datelor de mai jos.

Daca primesc un identificator din registrul `persoane`, foloseste mai intai skill-ul `numerologie-gestionare-persoane` pentru a incarca fisa. Preferintele precizate pentru lucrarea curenta suprascriu doar temporar valorile implicite din fisa.

```text
PERSOANA ANALIZATA
Nume si prenume:
Prenume activ:
Data nasterii:
Nume anterior: [optional]
Gen: M / F

LUCRARE
Tip template (selectie obligatorie): scurt / examen
Exprimare: conversational / formal
Nivel de detaliere: scurt / mediu / amplu
Intrebare principala: cariera / iubire / bani / faima / alta intrebare
Interval de ani: complet (0-108 ani) / specific:

RELATIE [optional]
Nume complet:
Prenume activ:
Data nasterii:
Gen: M / F
Tipul relatiei:
```

Nu incepe lucrarea pana cand `Tip template` nu contine exact `scurt` sau `examen`; daca lipseste, solicita selectia. Pentru `scurt`, foloseste perechea `Template_Lucrare_Numerologica_Scurt.md` + `.html`. Pentru `examen`, foloseste template-ul de examen si modelul editorial corespunzator starii lucrarii.

Verifica datele inainte de calcul. Ruleaza `scripts/calculator_numerologic_examen.py` din skill pentru persoana analizata si separat pentru persoana relationala, daca exista. Foloseste iesirea JSON drept sursa a calculelor. Nu inventa informatii lipsa. Livreaza perechea Markdown-HTML si aplica toate regulile template-ului selectat.

The Scribe are acces numai pentru citire la `vault/`. Daca lucrarea necesita documentarea sau corectarea unui concept ori a unei formule in Vault, trimite solicitarea exclusiv catre The Lore Keeper si foloseste aceasta denumire in toate rapoartele.

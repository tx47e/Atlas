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
Template: examen / scurt / alt tip disponibil
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

Verifica datele inainte de calcul. Ruleaza `scripts/calculator_numerologic_examen.py` din skill pentru persoana analizata si separat pentru persoana relationala, daca exista. Foloseste iesirea JSON drept sursa a calculelor. Nu inventa informatii lipsa. Livreaza perechea Markdown-HTML si aplica toate regulile template-ului selectat.

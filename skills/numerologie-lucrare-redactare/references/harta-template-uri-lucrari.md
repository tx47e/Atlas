---
titlu: Harta template-uri pentru lucrări numerologice
tip: referinta-skill
status: activa
skill: "[[skills/numerologie-lucrare-redactare/SKILL|numerologie-lucrare-redactare]]"
aliases:
  - Harta template-uri lucrări
  - Selecție template lucrare
tags:
  - skill
  - numerologie
  - lucrare
  - template
Data: 2026-07-16
meta:
  rol: harta-template-uri
  domeniu: redactare-lucrare
  utilizare: obligatorie
---

# Harta template-uri pentru lucrari numerologice

Skill părinte: [[skills/numerologie-lucrare-redactare/SKILL|numerologie-lucrare-redactare]]

| Tip / resursa | Template | Folosire |
| --- | --- | --- |
| Lucrare completa de examen | [Template_Lucrare_Numerologica_Examen.md](../assets/templates/Template_Lucrare_Numerologica_Examen.md) | Sursa canonica pentru structura completa, calcule, tabele, grafice, reguli de revizie si verificarea integralitatii. |
| Lucrare scurta | [Template principal](../assets/Template-lucrare-scurta.md) · [Markdown canonic](../assets/templates/Template_Lucrare_Numerologica_Scurt.md) · [HTML canonic](../assets/templates/Template_Lucrare_Numerologica_Scurt.html) | Resursa principala si perechea canonica pentru cheia `scurt`: incepe direct cu Capitolul 1 dupa Cuprins, fara `Cuvant inainte`; include tabele editabile, Tarot dinamic, matrice 3x3 si capitol relational optional cu Omuletul relatiilor. |
| Lucrare tematica sau restransa | [Template_Lucrare_Numerologica.md](../assets/templates/Template_Lucrare_Numerologica.md) | Se foloseste pentru o analiza mai scurta, un set limitat de teme sau capitole individuale. |
| Lista de control | [Cuprins_Lucrare_Numerologica.md](../assets/templates/Cuprins_Lucrare_Numerologica.md) | Inventar extins pentru alegerea capitolelor si verificarea acoperirii notiunilor. Nu este template de redactare de sine statator. |
| Model editorial de revizie | [Markdown](../assets/templates/Model_Lucrare_Numerologica_Revizie_Daniel_Birsan.md) · [HTML](../assets/templates/Model_Lucrare_Numerologica_Revizie_Daniel_Birsan.html) | Pereche editoriala `v1.04r`: Markdown-ul conduce continutul, iar HTML-ul arata prezentarea publicata si redarea indexurilor. Sursa istorica nu contine capitolul de trasabilitate; la o revizie noua, adauga-l obligatoriu conform `SKILL.md` si template-ului general. |
| Model editorial final | [Markdown](../assets/templates/Model_Lucrare_Numerologica_Finala_Daniel_Birsan.md) · [HTML](../assets/templates/Model_Lucrare_Numerologica_Finala_Daniel_Birsan.html) · [lista de control](lista-control-model-final-daniel.md) | Contract editorial validat `v1.05f` pentru lucrari finale similare: reproduce 1-la-1 structura, formatarea, ordinea, componentele si amploarea, apoi inlocuieste exclusiv elementele dependente de persoana. |

## Regula de selectie

- Alege `lucrare completa de examen` cand se cere structura integrala sau o
  lucrare de examen.
- Alege `lucrare scurta` numai cand formularul sau utilizatorul selecteaza explicit cheia `scurt`; nu confunda tipul template-ului cu nivelul de detaliere.
- Alege `lucrare tematica sau restransa` cand cererea acopera doar anumite
  concepte, o perioada sau un capitol.
- Daca scopul nu permite alegerea fara schimbarea substantiala a structurii,
  cere utilizatorului confirmarea tipului inainte de redactare.
- Dupa selectarea template-ului general, consulta modelul editorial care
  corespunde starii lucrarii. Pentru sufix `r`, urmeaza modelul de revizie;
  pentru sufix `f`, urmeaza modelul final. Pentru lucrari finale similare,
  modelul Daniel este contract editorial cu libertate redusa si se auditeaza
  obligatoriu cu lista de control; template-ul general ramane controlul
  domeniului si al calculelor.
- Consulta impreuna fisierele Markdown si HTML ale modelului ales si pastreaza
  perechea sincronizata atunci cand modelul este actualizat.

Template-ul istoric din `temp/lucrare finalizate/` nu este resursa activa si nu
se foloseste pentru o lucrare noua.

## Planuri neimplementate

- [Planul pentru lucrarea numerologica narativa](../../../planuri/2026-07-18-plan-template-lucrare-numerologica-narativa.md) este pastrat pentru dezvoltare viitoare. Nu este template activ si nu poate fi selectat in promptul The Scribe; tipurile implementate sunt `scurt` si `examen`.

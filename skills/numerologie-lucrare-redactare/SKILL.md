---
name: numerologie-lucrare-redactare
description: Redacteaza lucrari numerologice personale complete de examen, complete narative sau tematice in Markdown, folosind calcule validate, template-uri aprobate si livrabile SVG existente. Foloseste cand se creeaza sau se restructureaza o lucrare numerologica, inclusiv capitole despre caracter, evolutie, spirit sau relatie.
---

# Redactare lucrare numerologica

## Flux

1. Citeste [Harta template-urilor pentru lucrari](references/harta-template-uri-lucrari.md) si selecteaza tipul potrivit: completa de examen, completa narativa sau tematica/restransa.
2. Citeste integral notele de folosire ale template-ului principal si resursele auxiliare indicate de harta. Consulta si modelul editorial corespunzator starii lucrarii: modelul de revizie pentru sufix `r`, respectiv modelul final pentru sufix `f`. Fiecare model editorial este o pereche Markdown + HTML; pastreaza cele doua formate sincronizate ca structura si continut. Modelele sunt exemple validate si nu inlocuiesc template-ul general selectat. Pentru o lucrare narativa completa, planul narativ conduce lectura, iar template-ul de examen verifica integralitatea tehnica.
3. Ruleaza sau primeste raportul din `scripts/calculator_numerologic_examen.py`.
4. Citeste `vault/Numerologie/Registru Validare Formule.md` in regim de citire. Nu redacta interpretarea unei valori marcate `neconforma`, `neimplementata`, `lipsa sursa operationala` sau `blocata`; solicita Agentului Vault validarea necesara.
5. Subcontracteaza Agentul SVG pentru fiecare grafic si SVG cerut de template. Nu recalcula si nu redesena SVG-uri manual.
6. Creeaza numai fisierul Markdown. Genereaza HTML doar dupa aprobarea explicita a Markdown-ului.
7. Foloseste seriile temporale calculate integral de la varsta 0 la 108. Afiseaza in lucrare numai anii si intervalele relevante; nu elimina datele din raportul de calcul.

## Structura si stil

- Pune datele generale si cuprinsul la inceput.
- Indexeaza numai variantele de revizie cu sufix `r`. Foloseste `CAP` pentru capitol, `SUB` pentru subcapitol, `P` pentru paragraf, `C` pentru calcul, `T` pentru tabel, `G` pentru grafic/SVG/figura/imagine si `L` pentru lista sau metadate.
- Pastreaza indexul pe linie separata imediat inaintea elementului si identic in Markdown si HTML-ul de revizie.
- Elimina toate indexurile din variantele finale cu sufix `f`.
- Pentru fiecare concept, explica ideea general, explica formula si datele folosite, afiseaza calculul, apoi interpreteaza personalizat; nu adauga subtitluri mecanice pentru aceste patru etape.
- Scrie direct catre persoana, in ton cald, conversational-academic, clar si bogat in imagini usor de inteles.
- Scrie denumirile complete ale conceptelor; nu folosi prescurtari in vocea interpretativa.
- Prezinta dificultatile ca teme de constientizare si pasi constructivi. Nu folosi etichete degradante, verdicte sau predictii rigide.
- Pastreaza relatia ca lectura de compatibilitate, ritm, comunicare si constructie comuna.

## Continut obligatoriu

Respecta capitolele stabilite: portret, lumea interioara, prezenta in lume, punti si transformare, destin, evolutie si sincronicitati, dimensiunea spirituala, relatie, resurse practice, incheiere si anexa tehnica.

In capitolul temporal, verifica convergentele reale dintre ani personali, cicluri de 7/9/12 ani, pinacluri, lectii, ani interiori/exteriori si Soarta-Destin. In capitolul relatiei, include omuletul relatiilor, compatibilitati, diferente si sincronicitati de cuplu.

In varianta de revizie, adauga la finalul corpului si inaintea anexei tehnice
capitolul `Documentatia si trasabilitatea lucrarii`. Consemneaza agentul
coordonator, agentii subcontractati, skill-urile, template-urile, raportul
calculatorului, documentele metodologice, registrul si data validarii,
SVG-urile integrate, versiunea si data redactarii. Elimina integral acest
capitol din varianta finala.

## Validare

- Verifica existenta tuturor indexurilor si unicitatea lor.
- Verifica fiecare calcul fata de raportul validat.
- Pentru o varianta `r`, verifica prezenta capitolului de trasabilitate; pentru
  o varianta `f`, verifica absenta indexurilor si a capitolului temporar.
- Nu genera HTML in aceasta etapa.

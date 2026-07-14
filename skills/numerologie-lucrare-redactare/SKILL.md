---
name: numerologie-lucrare-redactare
description: Redacteaza sau reconstruieste editorial lucrari numerologice personale complete de examen, complete narative ori tematice, folosind calcule validate, template-uri aprobate si livrabile SVG existente. Pentru lucrari finale similare modelului Daniel Birsan, impune reproducerea 1-la-1 a structurii, formatarii, componentelor si amplorii editoriale, cu inlocuirea exclusiva a datelor dependente de persoana. Foloseste cand se creeaza, se finalizeaza sau se restructureaza o lucrare numerologica.
---

# Redactare lucrare numerologica

## Flux

1. Citeste [Harta template-urilor pentru lucrari](references/harta-template-uri-lucrari.md) si selecteaza tipul potrivit: completa de examen, completa narativa sau tematica/restransa.
2. Citeste integral notele template-ului principal si ambele fisiere Markdown + HTML ale modelului corespunzator starii lucrarii. Pastreaza perechea sincronizata. Pentru o lucrare narativa completa, planul narativ conduce lectura, iar template-ul de examen verifica integralitatea tehnica.
3. Pentru o lucrare finala similara modelului Daniel Birsan, trateaza sarcina ca reconstructie editoriala cu libertate redusa. Copiaza modelul final 1-la-1 si completeaza [lista de control pentru paritatea editoriala](references/lista-control-model-final-daniel.md). Nu porni de la un document incomplet si nu reconstrui modelul din memorie.
4. Ruleaza sau primeste raportul din `scripts/calculator_numerologic_examen.py`.
5. Citeste `vault/Numerologie/Registru Validare Formule.md` in regim de citire. Nu redacta interpretarea unei valori marcate `neconforma`, `neimplementata`, `lipsa sursa operationala` sau `blocata`; solicita Agentului Vault validarea necesara.
6. Subcontracteaza Agentul SVG pentru fiecare grafic si SVG cerut de template. Nu recalcula si nu redesena SVG-uri manual.
7. Creeaza numai fisierul Markdown. Genereaza HTML dupa aprobarea explicita a Markdown-ului, exceptand cererea explicita pentru pereche sau HTML.
8. Foloseste seriile temporale calculate integral de la varsta 0 la 108. Afiseaza in lucrare numai anii si intervalele relevante; nu elimina datele din raportul de calcul.

## Contractul modelului final Daniel

Pentru o lucrare finala similara, pastreaza 1-la-1 structura, cuprinsul, ierarhia, ordinea interna, formatarea, CSS-ul, tabelele, matricele colorate, simbolurile, reperul optim, numerotarea casutelor, chenarele, Tarotul, SVG-urile, tranzitiile si amploarea interpretarilor din model.

Inlocuieste numai datele persoanei si relatiilor, calculele validate, celulele si seriile dependente, arcanele, interpretarile personalizate si SVG-urile validate. Pastreaza ordinea `descriere ampla -> calcul in chenar -> tabel sau figura -> interpretare ampla`.

Nu folosi substituirea mecanica globala drept metoda de redactare. Poate fi doar o operatie auxiliara, urmata obligatoriu de auditul sectiune-cu-sectiune. Nu elimina si nu muta o componenta inaplicabila fara confirmarea explicita a utilizatorului.

Pentru capitolele matriciale, aplica urmatorul contract fara comprimare:

- In 4.1, afiseaza in chenar randuri distincte pentru data compacta, `N1`, `N2`, `N3`, `N4` si sirul complet.
- Interpreteaza fiecare vector prin compozitie: casute prezente si lipsa, dominante, contributii numerice, completitudine si raportul dintre compozitie si valoarea totala.
- In 4.5, compara separat cele noua casute si cei opt vectori cu optimul. Foloseste pentru casute coloanele `Casuta`, `Cantitate casuta`, `Valoare casuta`, `Cantitate optima`, `Valoare optima`, `Diferenta` si `Citire`.
- Defineste fixatia numai ca vectorul plin cu valoarea cea mai mare. Interpreteaza `123` drept cai/forta de pornire, `456` drept trasura/sustinere practica si `789` drept vizitiu/directie mentala si spirituala.
- Pastreaza 4.6 ca subcapitol separat, `Scara bunastarii`. Include exact noua casute si opt vectori, ordonate descrescator dupa valoare, cu valorile egale grupate logic si valorile zero la baza. In HTML, reda-le prin bare orizontale raportate la maxim.
- In 5.7, afiseaza fiecare componenta a numelui pe rand separat, cu litere, sir numeric, suma, reducere si cod; pune codul concatenat si codul personal intr-un chenar separat.

Pentru graficele livrabile, foloseste in HTML structura validata de modelul Daniel revizie: `<figure><img class="embedded-svg" src="..." alt="..."><figcaption>...</figcaption></figure>`. Cand HTML-ul trebuie sa fie autonom, `src` contine SVG-ul ca data URI; elementul de randare ramane `<img>`. Nu dubla un SVG cu o imagine raster daca nu exista o resursa raster distincta ceruta explicit.

Exceptie obligatorie: pentru `Omuletul Relatiilor`, Agentul SVG livreaza perechea
SVG + PNG. Pastreaza SVG-ul numai ca sursa tehnica, iar in lucrarea Markdown
foloseste PNG-ul de `900 x 840 px`. In HTML autonom, incorporeaza acelasi PNG ca
`data:image/png;base64,...`; nu integra SVG-ul Omuletului Relatiilor.

## Structura si stil

- Pune datele generale si cuprinsul la inceput.
- Indexeaza numai variantele de revizie cu sufix `r`. Foloseste `CAP` pentru capitol, `SUB` pentru subcapitol, `P` pentru paragraf, `C` pentru calcul, `T` pentru tabel, `G` pentru grafic/SVG/figura/imagine si `L` pentru lista sau metadate.
- Pastreaza indexul pe linie separata imediat inaintea elementului si identic in Markdown si HTML-ul de revizie.
- Elimina toate indexurile din variantele finale cu sufix `f`.
- Pentru fiecare concept, explica ideea general, explica formula si datele folosite, afiseaza calculul, apoi interpreteaza personalizat; nu adauga subtitluri mecanice pentru aceste patru etape.
- Scrie direct catre persoana, in ton cald, conversational-academic, clar si bogat in imagini usor de inteles.
- Evita formulele de adresare si concluziile-tip repetate intre subcapitole. Cauta expresii recurente precum `Pentru tine`, `La tine`, `In viata de zi cu zi` si `Cheia practica`; pastreaza-le numai cand adauga sens nou si nu deschid mecanic sectiuni consecutive.
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
- Pentru modelul final Daniel, completeaza integral [lista de control de paritate](references/lista-control-model-final-daniel.md). Compara sectiune-cu-sectiune Markdown-ul si HTML-ul; numararea globala a componentelor nu este suficienta.
- Confirma ordinea componentelor, structura tabelelor, matricele colorate, simbolurile, optimul, numerotarea casutelor si amploarea interpretarilor.
- Cauta ramasite ale persoanei-model in date, calcule, tabele, texte, atribute HTML, cai, legende si SVG-uri; rezultatul trebuie sa fie zero.
- Verifica ancorele, resursele, validitatea XML a SVG-urilor, watermark-ul `Atlas Numerologie` si paritatea vizuala.
- Pentru o varianta `r`, verifica prezenta capitolului de trasabilitate; pentru
  o varianta `f`, verifica absenta indexurilor si a capitolului temporar.
- Opreste livrarea daca auditul de paritate este incomplet sau daca o sectiune a fost simplificata fara aprobarea utilizatorului.

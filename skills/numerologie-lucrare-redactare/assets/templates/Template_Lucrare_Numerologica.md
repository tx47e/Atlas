---
titlu:
tip: lucrare numerologica
tags:
  - numerologie
  - lucrare
Data:
client:
data_nasterii:
nume_complet:
nume_activ:
format: scurt, moderat sau amplu
formulare: formal sau conversational
---

# Lucrare numerologica

Pentru o lucrare finala similara, acest template se completeaza numai in cadrul
contractului editorial al modelului final Daniel Birsan din skill. Copiaza
1-la-1 perechea Markdown + HTML si inlocuieste pe campuri doar datele, calculele
validate, tabelele dependente, arcanele, interpretarile personalizate si
SVG-urile. Pastreaza paritatea structurala si vizuala, inclusiv ordinea
descriere-calcul-tabel/figura-interpretare, matricele colorate 4.1/5.7,
descrierea dinaintea 2.1, ordinea 6.6, lectura ampla 7.1 si structurile 8.1-8.3.
Completeaza lista de control a modelului; nu livra dupa o substituire mecanica
fara audit sectiune-cu-sectiune si fara eliminarea formularilor repetitive din
tabele.

Nota: pentru lucrarile numerologice complete si pentru modificarile de template
de lucrare, se foloseste ca referinta principala
`templates/Template_Lucrare_Numerologica_Examen.md`. Acest template ramane o
varianta simplificata de lucru.

## Date de intrare

- Data nasterii:
- Nume complet:
- Nume activ:
- Nume anterior / schimbat:
- Intrebari principale:
- Format lucrare:
- Tip formulare:

Vezi: Datele de intrare

---
## Note de lucru pentru redactare

- Prelucrarea datelor se face pe baza datei de nastere, a numelui complet, a
  numelui activ si, daca exista, a numelui anterior sau schimbat.
- Fiecare concept, vibratie sau calcul incepe cu o descriere adaptata
  formatului lucrarii: scurta, moderata sau ampla.
- Pentru fiecare rezultat numeric se afiseaza descrierea, calculul, rezultatul,
  reprezentarea aferenta rubricii si interpretarea.
- Pentru fiecare vibratie obtinuta prin reducere numerologica, traseul complet
  al reducerii se include in campul `Calcul`. Interpretarea generala nu citeste
  doar cifra finala, ci si numerele intermediare prin care aceasta se formeaza.
- In interpretarea fiecarei vibratii se integreaza obligatoriu citirea traseului
  de reducere. Aceasta explica, in cuvinte, ce aduce fiecare treapta a
  traseului: numarul de pornire, suma intermediara, pragurile de reducere si
  cifra finala.
- Traseul nu se trece ca rubrica separata. El ramane in `Calcul`, iar in
  `Interpretare` se explica treptele de reducere si felul in care acestea
  nuanteaza rezultatul final.
- Cifra finala arata directia principala, iar traseul de reducere arata
  straturile de formare: numarul compus initial, pragurile intermediare,
  eventualele numere maestre aparute pe traseu si felul in care cifrele
  componente nuanteaza rezultatul.
- Reprezentarea aferenta poate fi tabel, lista structurata, patratul lui
  Pitagora, tabel comparativ sau alta forma ceruta de rubrica.
- Pentru Soarta si Destin se include si un grafic care arata raportul dintre
  soarta, zona de confort a sortii, destin si zona de confort a destinului.
- Calculele se pastreaza clare si verificabile, fara a incarca lucrarea cu
  explicatii tehnice inutile.
- Cand un calcul are mai multi pasi, pasii se leaga cu ` -> `, nu cu punct si
  virgula. Exemplu: `1 + 9 = 10 -> 1 + 0 = 1`.
- In chenarele de calcul se pune doar formula/traseul de calcul. Explicatia
  despre ce se calculeaza sta in paragraful de dinainte, iar interpretarea sta
  dupa chenar.
- In HTML, chenarele de calcul folosesc fundalul deschis `#ead7b8`, text
  normal `font-weight: 400`, iar eventualele marcaje `<strong>` din calcule
  se coloreaza rosu `#c62828` si se scriu cu `font-weight: 800`, ca cifra
  evidentiata sa fie usor de distins.
- Paragraful de dinaintea unui calcul nu anticipeaza rezultatul concret:
  nu spune cifra finala, numarul grafic, codul obtinut, lectia activa,
  centrul, suma de control sau interpretarea acestor rezultate inainte ca
  ele sa fie afisate in chenarul de calcul ori in figura aferenta.
- Pentru HTML-ul care trebuie trimis ca fisier unic, graficele si SVG-urile
  esentiale se includ embedded in HTML, preferabil ca `data:image/svg+xml;base64`
  atunci cand sunt folosite in `<img>`. Nu se lasa dependente obligatorii de
  fisiere SVG externe daca lucrarea trebuie sa poata fi deschisa singura.
- Structura HTML ramane cea validata in modelul Daniel revizie:
  `<figure><img class="embedded-svg" src="..." alt="..."><figcaption>...</figcaption></figure>`.
  SVG-ul este redat prin elementul `<img>`; nu se adauga o copie raster daca nu
  exista o resursa raster distincta ceruta explicit.
- In Markdown, aceleasi grafice raman referinte curate de imagine Markdown:
  `![descriere](asset.svg)`. Nu se introduc `<figure>`, `<img>`, `<div>` sau
  alte fragmente HTML in varianta `.md`.
- Exceptie: Omuletul Relatiilor foloseste in Markdown `asset.png`, iar in HTML
  autonom `data:image/png;base64,...`. SVG-ul pereche ramane numai sursa tehnica
  si nu se integreaza in lucrare. PNG-ul validat are `900 x 840 px`.
- Interpretarile se scriu dupa notele complete ale conceptelor relevante, nu
  doar dupa listele scurte de orientare.
- Interpretarile respecta `Tip formulare`: formal sau conversational.
- Nivelul de detaliere respecta `Format lucrare`: scurt, moderat sau amplu.
- Rezultatele se leaga intre ele: data nasterii, numele, matricele, scara
  bunastarii, destinul, ciclurile si concluzia finala.
- Tonul ramane cald, clar, practic si nefatalist.

### Varianta de revizie indexata

- Cand lucrarea inca trebuie revizuita, fiecare element important poate primi
  un index temporar pentru feedback si urmarire.
- Indexul este doar pentru revizie; versiunea finala livrata clientului nu
  trebuie sa contina indexi vizibili si nici capitolul temporar `Documentatia
  si trasabilitatea lucrarii`.
- Denumirea fisierelor foloseste forma `v{versiune}{stare}`: de exemplu
  `v1.00r` pentru versiunea 1.00 in revizie si `v1.00f` pentru versiunea 1.00
  finala. Pentru versiuni urmatoare se folosesc `v1.01r`, `v1.02r`,
  `v2.00r` sau echivalentele finale cu sufix `f`.
- La fiecare modificare facuta intr-o lucrare existenta se ridica versiunea.
  Schimbarile de capitole sau structura majora ridica versiunea principala
  (`v1.00` -> `v2.00`), iar schimbarile de paragrafe, calcule, tabele,
  grafice, SVG-uri sau completari locale ridica versiunea minora
  (`v1.00` -> `v1.01`). Pentru mai multe schimbari locale intr-o singura
  interventie, incrementul minor poate fi mai mare de `0.01`.
- Format recomandat:

```text
{{initiale_client}}-{{AAAALLZZ}}-{{versiune_lucrare_cu_stare}}-{{tip_element}}-{{numar_ordine}}
```

- Coduri de element: `CAP` pentru capitole, `SUB` pentru subcapitole, `P`
  pentru paragrafe, `L` pentru liste, `T` pentru tabele si `C` pentru calcule,
  figuri, grafice sau SVG-uri.
- In HTML, indexul se pune mereu pe linie separata imediat deasupra elementului.
  Pentru titluri se foloseste `<div class="index index-heading">Index: ...</div>`,
  ca indexul sa stea deasupra chenarului de capitol, nu in interiorul lui.
- In Markdown, indexul se pune tot pe linie separata, ca text simplu:
  `Index: {{cod_index}}`. Nu se folosesc niciodata `<div class="...">`,
  `<figure>`, `<img>` sau alte fragmente HTML in varianta `.md`.
- La finalizare se elimina toate elementele `.index`.

### Template lucrat pentru traseul de reducere

```text
Rubrica:
Calcul:
Rezultat final:

Interpretare:
Interpretarea se scrie intr-un singur text fluent. Ea citeste mai intai
rezultatul final ca directie principala, apoi integreaza traseul de reducere:
cifra sau numarul de pornire indica materialul brut, numerele intermediare
indica pragurile de transformare, iar cifra finala arata forma sintetica in care
energia se manifesta.
```

Exemplu:

```text
Rubrica: Vibratie interioara
Calcul: ziua nasterii 28 -> 10 -> 1
Rezultat final: 1

Interpretare:
Vibratia finala 1 arata initiativa, autonomie si nevoie de directie proprie, dar
traseul 28 -> 10 -> 1 arata ca acest 1 nu este direct. El se formeaza prin
sensibilitatea si cooperarea lui 2, forta si ambitia lui 8, apoi prin pragul 10,
care cere relansare, asumare si transformarea potentialului in actiune clara.
```

---
## 1. Vibratii fundamentale

### Vibratie Interioara

- Descriere:
- Calcul:
- Rezultat:
- Interpretare:

### Vibratie Exterioara

- Descriere:
- Calcul:
- Rezultat:
- Interpretare:

### Vibratie Cosmica Fixa

- Descriere:
- Calcul:
- Rezultat:
- Interpretare:

### Vibratie Cosmica Variabila

- Descriere:
- Calcul:
- Rezultat:
- Interpretare:

### Vibratie Cosmica Totala

- Descriere:
- Calcul:
- Rezultat:
- Interpretare:

### Vibratie Globala

- Descriere:
- Calcul:
- Rezultat:
- Interpretare:

---
## 2. Destin si evolutie

### Vibratia Destinului

- Descriere:
- Calcul:
- Rezultat:
- Interpretare:

### Calea Destinului

- Descriere:
- Calcul:
- Rezultat:
- Interpretare:

### Aspecte de Indreptat

- Descriere:
- Calcul:
- Aspecte:
- Vibratia solutiei:
- Interpretare:

### Soarta si Destin

- Descriere:
- Soarta:
- Zona de confort soarta:
- Destin:
- Zona de confort destin:
- Grafic:
- Tabel comparativ si interpretarea graficului: se introduc imediat dupa graficul Soarta si Destin.
- Harta suprapusa Soarta-Destin-Ciclicitati: se introduce numai dupa tabelul comparativ si interpretarea aferenta graficului Soarta si Destin.
- Tema vietii:
- Interpretare:

### Punti

- Descriere:
- Nota de redactare: interpretarea fiecarei punti se construieste din fisierele
  complete ale vibratiilor implicate si din fisierul complet al vibratiei
  rezultate, nu dintr-o lista scurta de sensuri.

| Punte | Calcul | Rezultat | Interpretare sintetica |
| --- | --- | --- | --- |
| Interior - exterior |  |  |  |
| Interior - destin |  |  |  |
| Exterior - destin |  |  |  |
| Cosmic - destin |  |  |  |

- Interpretare scrisa pentru puntea interior - exterior:
- Interpretare scrisa pentru puntea interior - destin:
- Interpretare scrisa pentru puntea exterior - destin:
- Interpretare scrisa pentru puntea cosmic - destin:

---
## 3. Karma

### Karma din Ziua Nasterii

- Descriere:
- Calcul:
- Arcana karmica:
- Nivel karma implinita:
- Interpretare:

### Karma din Luna Nasterii

- Descriere:
- Calcul:
- Tema karmica:
- Interpretare:

### Karma din Calea Destinului

- Descriere:
- Calcul:
- Categorie:
- Interpretare:

---
## 4. Numere personale

### Numarul de Exprimare

- Descriere:
- Calcul:
- Rezultat:
- Comparatie cu Vibratia Destinului:

### Numarul Intim

- Descriere:
- Calcul:
- Rezultat:
- Comparatie cu Vibratie Interioara:

### Numarul de Realizare

- Descriere:
- Calcul:
- Rezultat:
- Comparatie cu Vibratie Exterioara:

### Numarul Activ

- Descriere:
- Calcul:
- Rezultat:
- Interpretare:

### Numarul Ereditar

- Descriere:
- Calcul:
- Rezultat:
- Interpretare:

### Numarul Neamului

- Descriere:
- Calcul:
- Rezultat:
- Interpretare:

### Cod Numerologic Personal

- Descriere:
- Cod:
- Cifre introduse in matrice:

---
## 5. Matrici si analize

### Matricea Datei de Nastere

- Descriere:
- Calcul: un singur chenar, cu randuri distincte pentru data compacta, `N1`,
  `N2`, `N3`, `N4` si sirul complet. Nu reuni pasii intr-un paragraf continuu.

```text
1 | 4 | 7
2 | 5 | 8
3 | 6 | 9
```

- Matrice:
- Cifre dominante:
- Cifre absente:
- Observatii:

### Fixatia

- Descriere:
- Formula:
- Vectori plini identificati:
- Vector ales:
- Compozitie:
- Valoare:
- Numar total de elemente:
- Casute pare:
- Casute impare:
- Legatura cu scara bunastarii:
- Interpretare:

Nota de redactare: fixatia se calculeaza din matricea datei de nastere. Se
alege vectorul plin dominant, adica vectorul ale carui trei casute sunt prezente
si care are valoarea cea mai mare dintre vectorii plini. Daca nu exista vector
plin, se noteaza ca persoana nu are fixatie matriceala clara si se interpreteaza
tendinta impreuna cu treapta cea mai inalta din scara bunastarii.


### Vectorii matricei

- Tabelul vectorilor foloseste coloana `Interpretare`, nu `Descriere si interpretare`.
- Interpretarea fiecarui vector trebuie sa enumere casutele prezente si lipsa,
  sa numeasca dominantele si contributia lor numerica, sa spuna explicit daca
  vectorul este plin sau incomplet si sa lege aceasta compozitie de valoarea
  totala.
- Pentru vectorii incompleti se numeste casuta lipsa si tema ei: 4 corp,
  stabilitate si reguli; 5 centru, curaj practic si adaptare; 6 munca,
  responsabilitate afectiva si finalizare; la fel pentru orice alta casuta
  lipsa.
- Fixatia se explica separat: este vectorul plin cu valoarea cea mai mare si
  arata zona spre care energia se duce natural, cu talentul si riscul de exces.
- Caii, trasura si vizitiul se interpreteaza prin compararea vectorilor 123,
  456 si 789. Se mentioneaza atat valoarea, cat si lipsurile fiecarui vector.
- Comparatia cu optimul din 4.5 acopera toate cele noua casute si toti cei opt
  vectori. Tabelul casutelor foloseste coloanele `Casuta`, `Cantitate casuta`,
  `Valoare casuta`, `Cantitate optima`, `Valoare optima`, `Diferenta` si
  `Citire`.

### Scara bunastarii

- Pastreaza acest continut ca subcapitol separat 4.6, dupa tendinte, fixatie si
  analogia cai-trasura-vizitiu.
- Include exact noua casute si opt vectori. Ordoneaza descrescator dupa valoare,
  grupeaza logic valorile egale si aseaza valorile zero la baza.
- In HTML foloseste bare orizontale raportate la valoarea maxima. Pentru casute
  afiseaza bulina elementului si legenda Foc, Pamant, Apa, Aer.

### Matricea Numelui

- Descriere:
- Calculul codului personal: cate un rand pentru fiecare componenta a numelui,
  cu litere, sir numeric, suma, reducere si cod. Pune codul concatenat si codul
  personal intr-un al doilea chenar.

```text
1 | 4 | 7
2 | 5 | 8
3 | 6 | 9
```

- Matrice:
- Cifre dominante:
- Cifre absente:
- Observatii:

### Matricea Numelui vs Matricea Datei de Nastere

- Descriere:

**Matricea datei de nastere**

```text
1 | 4 | 7
2 | 5 | 8
3 | 6 | 9
```

**Matricea numelui**

```text
1 | 4 | 7
2 | 5 | 8
3 | 6 | 9
```

- Exces in nume:
- Lipsa in nume:
- Potential de nume fara suport nativ:
- Sustinere / nuantare:

### Scara Bunastarii

- Descriere:
- Fixatia:
- Trepte dominante:
- Trepte slabe:
- Salturi importante:
- Interpretare:

---
## 6. Cicluri si etape de viata

- Pentru interpretarea de sinteza a ciclurilor, se reutilizeaza Harta suprapusa Soarta-Destin-Ciclicitati din capitolul anterior, imediat sub subtitlul interpretarii si inaintea textului explicativ.
- Se pastreaza aceeasi sursa SVG, cu o legenda care mentioneaza folosirea ei pentru interpretarea ciclurilor.

### Pinacluri - Oportunitati si Provocari

- Descriere:

| Etapa | Varsta | Oportunitate | Provocare | Interpretare |
| --- | --- | --- | --- | --- |
| Pinaclul 1 |  |  |  |  |
| Pinaclul 2 |  |  |  |  |
| Pinaclul 3 |  |  |  |  |
| Pinaclul 4 |  |  |  |  |

### Ciclul de 7 Ani

- Descriere:
- Ciclu:
- Pozitie:
- Interpretare:

### Lectii de Viata

- Descriere:
- Sir lectii:
- Lectia perioadei analizate:
- Interpretare:

### Ciclul de 9 Ani

- Descriere:
- Ciclu:
- An personal:
- Interpretare:

### Ciclul de 12 Ani

- Descriere:
- Ciclu:
- Pozitie:
- Interpretare:

### Anii Importanti Int-Ext

- Descriere:
- Interval analizat:
- Ani importanti interiori:
- Ani importanti exteriori:
- Interpretare:

#### Tabelul rezultat

Interval analizat:
Nota: daca persoana are un punct de interes, se cere intervalul dorit pentru
analiza. Daca nu este indicat un interval, se foloseste anul curent - 5 pana la
anul curent + 10.
Pentru anii fara influenta interioara sau exterioara, toate campurile de marcaj
si interpretarea se completeaza cu `-`.

| An | Interior | Exterior | Descriere / interpretare |
| --- | --- | --- | --- |
|  |  |  |  |

---
## 7. Sinteza si aplicabilitate

### Deschidere spre Ezoterism

- Descriere:
- Cod principal:
- Tip principal:
- Cod secundar:
- Domeniu:
- Observatii de prudenta:

### Aplicabilitate Profesionala

- Descriere:
- Arcana obstacole / ajutoare (NU):
- Instrumente:
- Obstacole:
- Arcana aplicabilitate profesionala (DA):
- Directii profesionale:
- Calculul se pune in chenar si foloseste etichetele explicite `NU / obstacole`
  si `DA / aplicabilitate profesionala`.
- Pentru interpretarea arcanelor, se foloseste un tabel cu doua coloane:
  prima coloana contine imaginea arcanei si eticheta ei, iar a doua coloana
  contine interpretarea. In HTML tabelul foloseste clasa
  `tarot-reading-table`, cu imaginile mici, aliniate la stanga.
- In MD, tabelul ramane Markdown curat, fara `<div>`, `<figure>` sau `<img>`.
  Imaginile se introduc ca referinte Markdown in prima coloana.

### Concluzii

#### Directia principala

#### Resurse dominante

#### Provocari principale

#### Recomandari practice

#### Model de concluzie finala

---
## Capitol temporar de revizie. Documentatia si trasabilitatea lucrarii

Acest capitol exista numai in variantele cu sufix `r` si se elimina integral
din variantele finale cu sufix `f`.

| Element de trasabilitate | Referinta folosita |
| --- | --- |
| Agent coordonator | {{agent_coordonator}} |
| Agenti subcontractati | {{agenti_subcontractati}} |
| Skill-uri folosite | {{skill_uri_folosite}} |
| Template principal si resurse auxiliare | {{template_uri_folosite}} |
| Raportul calculatorului | {{raport_calculator}} |
| Documente metodologice consultate | {{documentatie_metodologica}} |
| Registrul de validare si data verificarii | {{registru_validare_si_data}} |
| SVG-uri integrate si validarea lor | {{svg_uri_si_validare}} |
| Versiunea si data redactarii | {{versiune_si_data_redactare}} |

---
## Anexa tehnica

{{anexa_tehnica}}

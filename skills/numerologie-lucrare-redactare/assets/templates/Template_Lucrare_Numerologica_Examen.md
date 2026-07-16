---
titlu: Template lucrare numerologica examen
tip: template
tags:
  - numerologie
  - lucrare
  - examen
Data:
status: template de lucru
---

# Template lucrare numerologica examen

Nota de folosire:

- Acesta este un template, nu o lucrare completata.
- Pentru o lucrare finala din aceeasi familie editoriala, modelul final Daniel
  Birsan din skill este schema obligatorie. Se copiaza 1-la-1 perechea
  Markdown + HTML si se completeaza pe campuri; nu se reconstruieste mecanic
  dintr-o lucrare incompleta.
- Se pastreaza paritatea structurala si vizuala: capitole, formatare, ordinea
  descriere-calcul-tabel/figura-interpretare, tabele, chenare, matrice colorate,
  simboluri, optim, numerotarea casutelor si amploarea interpretarilor.
- Se aplica integral lista de control a modelului Daniel. Sunt obligatorii:
  descrierea inainte de 2.1; matricele complete 4.1 si 5.7; ordinea 6.6;
  interpretarile individuale si nerepetitive din tabele; lectura ampla 7.1;
  calculele 8.1 pe doua randuri; separarea operatiilor si interpretarilor 8.2,
  cu rezultatul dupa virgula rosu; calculul explicat, casutele colorate si
  tabelul subetapelor din 8.3.
- Pentru lucrarile numerologice complete si pentru orice modificare de template
  de lucrare, acesta este template-ul principal de referinta.
- Se completeaza campurile dintre acolade.
- Nu se introduc link-uri catre lucrari, fisiere sau documente externe.
- Pentru fiecare capitol se pastreaza calculul, rezultatul si interpretarea.
- Cand un calcul are mai multi pasi, pasii se leaga cu ` -> `, nu cu punct si
  virgula. In chenarul de calcul se pune doar traseul de calcul; explicatia sta
  inainte, iar interpretarea dupa calcul.
- Unde exista tabele sau grafice in lucrarea finala, se lasa camp de completare pentru tabel/grafic.
- Pentru lucrarile aflate in revizie se poate folosi varianta indexata, ca fiecare
  element sa poata fi urmarit usor in feedback. Indexii se folosesc doar in
  lucrarea care mai trebuie revizuita; dupa finalizarea reviziei, versiunea
  finala se livreaza fara indexi vizibili.
- Denumirea fisierelor de lucrare foloseste forma `v{versiune}{stare}`:
  `v1.00r`, `v1.01r`, `v2.00r` pentru revizii si `v1.00f`, `v1.01f`,
  `v2.00f` pentru variante finale. Litera `v` indica versiunea, numarul indica
  numarul versiunii, iar `r` inseamna revizie si `f` inseamna final.
- Validarea unei revizii ca lucrare finala nu modifica numarul versiunii.
  Conversia schimba exclusiv sufixul de stare: `v1.07r` devine `v1.07f`.
  Varianta finala se genereaza din perechea MD + HTML a aceleiasi revizii,
  dupa eliminarea indexurilor si a elementelor temporare specifice reviziei.
  Nu se foloseste o varianta finala mai veche si nu se redenumeste un fisier
  final anterior daca nu este semantic identic cu revizia validata.
- La fiecare modificare facuta intr-o lucrare existenta, versiunea se ridica
  inainte de livrare cat timp lucrarea ramane in revizie. Schimbarile majore de capitole, structura sau
  reorganizare ampla ridica versiunea principala: `v1.00` -> `v2.00`.
  Schimbarile de paragrafe, calcule, tabele, grafice, SVG-uri sau completari
  locale ridica versiunea minora: `v1.00` -> `v1.01`, `v1.01` -> `v1.02`.
  Mai multe modificari locale intr-o singura interventie pot ridica versiunea
  cu mai mult de `0.01`, proportional cu volumul modificarilor.
- Pentru rubrica Fixatia, se foloseste documentul de metoda:
  `vault/Numerologie/Fixatia.md`.

### Regula pentru varianta de revizie indexata

Indexul este un marcaj temporar de lucru, nu continut final pentru client.

Format recomandat:

```text
{{initiale_client}}-{{AAAALLZZ}}-{{versiune_lucrare_cu_stare}}-{{tip_element}}-{{numar_ordine}}
```

Exemplu:

```text
BDR-19980219-v1.01r-CAP-001
BDR-19980219-v1.01r-P-001
BDR-19980219-v1.01r-T-001
BDR-19980219-v1.01r-C-001
```

Tipuri de element:

| Cod | Element indexat |
| --- | --- |
| CAP | capitol / titlu principal |
| SUB | subcapitol / subtitlu |
| P | paragraf |
| L | lista |
| T | tabel |
| C | calcul sau chenar de calcul |
| G | grafic, SVG, figura sau imagine |

Reguli de folosire:

- Indexii se introduc doar in varianta de revizie.
- In HTML, inclusiv pentru titluri, indexul se pune pe linie separata imediat
  deasupra elementului. Pentru titluri se foloseste si clasa `index-heading`,
  ca indexul sa ramana vizual deasupra chenarului de capitol, nu in interiorul
  lui:
- In Markdown, indexul se pune tot pe linie separata, ca text simplu:
  `Index: {{cod_index}}`. Nu se introduc niciodata `<div class="...">`,
  `<figure>`, `<img>` sau alte fragmente HTML in varianta `.md`.
- Pentru HTML-ul trimis ca fisier unic catre client, graficele si SVG-urile
  esentiale se includ embedded in HTML. Cand un SVG este introdus prin `<img>`,
  se recomanda `src="data:image/svg+xml;base64,{{svg_base64}}"`, mai ales daca
  SVG-ul contine imagini de fundal embed-uite. Nu se lasa dependente obligatorii
  de fisiere SVG externe pentru elementele fara de care lucrarea nu se intelege.
- In varianta `.md`, aceleasi grafice raman referinte curate de imagine
  Markdown, de forma `![descriere](asset.svg)`.
- Paragraful de dinaintea unui calcul sau SVG de calcul nu anticipeaza
  rezultatul concret: nu mentioneaza cifra finala, codul obtinut, numarul
  grafic, lectia activa, centrul, suma de control sau interpretarea acestor
  valori inainte ca ele sa fie afisate in chenarul de calcul ori in figura.

```html
<div class="index index-heading">Index: BDR-19980219-v1.01r-CAP-001</div>
<h2>Titlu capitol</h2>
```

- Pentru paragrafe, liste, tabele, calcule, figuri si SVG-uri, indexul se pune
  imediat inaintea elementului:

```html
<div class="index">Index: BDR-19980219-v1.01r-P-001</div>
<p>Textul paragrafului...</p>
```

- Stil recomandat pentru HTML-ul de revizie:

```css
.index {
  color: var(--gold);
  font-size: 12px;
  font-weight: 700;
  line-height: 1.2;
  margin: 14px 0 6px;
}
.index-heading {
  display: block;
  margin: 30px 0 8px;
}
.index-heading + h1,
.index-heading + h2,
.index-heading + h3,
.index-heading + h4 {
  margin-top: 0;
}
.calc-box,
pre {
  background: #ead7b8;
  color: var(--deep);
  border-left: 6px solid var(--sand);
  border-radius: 6px;
}
.calc-box {
  margin: 14px 0;
  padding: 12px 16px;
  font-weight: 400;
}
.calc-box strong {
  color: #c62828;
  font-weight: 800;
}
pre {
  padding: 16px;
  overflow: auto;
  white-space: pre-wrap;
}
.tarot-reading-table {
  table-layout: fixed;
}
.tarot-reading-table col:first-child {
  width: 180px;
}
.tarot-reading-table td {
  vertical-align: top;
}
.tarot-card-cell {
  text-align: left;
}
.tarot-card-cell img {
  display: block;
  width: 130px;
  height: auto;
  margin: 0;
  border: 1px solid rgba(11, 43, 44, 0.16);
  border-radius: 6px;
  background: #fffdf8;
}
.tarot-card-caption {
  margin-top: 8px;
  color: var(--gold);
  font-size: 13px;
  font-weight: 700;
}
.tarot-reading-table p {
  margin-top: 0;
}
```

- In versiunea finala, se elimina toate elementele `.index`; continutul ramane
  fara marcajul de index. Se elimina si capitolul temporar `Documentatia si
  trasabilitatea lucrarii`.
- Titlul cuprinsului este intotdeauna `Cuprins`, nu `Cuprins rapid`.
- In varianta de revizie `r`, versiunea se afiseaza explicit in titlul lucrarii
  si in `Date generale`, in forma `V1.07R`.
- In varianta finala `f`, versiunea ramane numai in numele fisierului. Titlul
  lucrarii nu contine versiunea, iar din `Date generale` se elimina campurile
  `Versiune lucrare`, `Template de lucru`, `Stil de redactare` si
  `Nivel de detaliere`.

---
## Date generale

- Persoana analizata: {{nume_complet}}
- Data nasterii: {{data_nasterii}}
- Nume familie: {{nume_familie}}
- Prenume: {{prenume}}
- Prenume activ folosit in calcul: {{prenume_activ}}
- Nume complet la nastere: {{nume_complet_la_nastere}}
- Nume anterior / schimbat: {{nume_anterior}}
- Gen persoana: {{gen_persoana}}
- Autor lucrare: {{autor_lucrare}}
- Versiune lucrare: {{versiune_lucrare}}
- Data lucrarii: {{data_lucrarii}}
- Template de lucru: templates/Template_Lucrare_Numerologica_Examen.md
- Tip lucrare: {{tip_lucrare}}
- Metoda de lucru: {{metoda_de_lucru}}
- Stil de redactare: {{formal_sau_conversational}}
- Nivel de detaliere: {{scurt_mediu_amplu}}
- Scopul lucrarii: {{scop_lucrare}}
- Cadru de interpretare: {{cadru_interpretare}}

### Relatii

- Persoana analizata in relatie: {{nume_complet_partener}}
- Data nasterii persoana analizata in relatie: {{data_nasterii_partener}}
- Tip relatie analizata: {{tip_relatie_analizata}}

---
## Cuprins

{{cuprins_generat}}

---
## Cuvânt înainte

{{introducere_cuvant_inainte}}

Sursă editorială: `vault/Numerologie/Introducere.md`. Textul se așază după
Cuprins și înainte de Capitolul 1. Se păstrează imaginea unitară a călătoriei
și se adaptează numai formulările care trebuie aliniate conceptelor folosite în
lucrare; nu se rescrie mecanic pentru fiecare persoană. Povestea include și
ciclicitățile, anii importanți interiori și exteriori, ciclurile de 7, 9 și 12
ani, Soarta și Destinul, lecțiile de viață și anul personal.

---
## Capitolul 1. Formule, calcule, tabele, grafice

### 1.1. Date de intrare

| Camp | Valoare |
| --- | --- |
| Data nasterii | {{data_nasterii}} |
| Ziua nasterii | {{ziua_nasterii}} |
| Luna nasterii | {{luna_nasterii}} |
| Anul nasterii | {{anul_nasterii}} |
| Nume complet | {{nume_complet}} |
| Nume activ | {{nume_activ}} |
| Nume anterior / schimbat | {{nume_anterior}} |

### 1.2. Vibratiile

| Concept | Formula | Calcul | Rezultat |
| --- | --- | --- | --- |
| Vibratia interioara | {{formula_vibratie_interioara}} | {{calcul_vibratie_interioara}} | {{vibratie_interioara}} |
| Vibratia interioara karmica | {{formula_vibratie_interioara_karmica}} | {{calcul_vibratie_interioara_karmica}} | {{vibratie_interioara_karmica}} |
| Liniile de tensiune | {{formula_linii_tensiune}} | {{calcul_linii_tensiune}} | {{linii_tensiune}} |
| Vibratia exterioara | {{formula_vibratie_exterioara}} | {{calcul_vibratie_exterioara}} | {{vibratie_exterioara}} |
| Vibratia exterioara karmica | {{formula_vibratie_exterioara_karmica}} | {{calcul_vibratie_exterioara_karmica}} | {{vibratie_exterioara_karmica}} |
| Vibratia globala | {{formula_vibratie_globala}} | {{calcul_vibratie_globala}} | {{vibratie_globala}} |
| Vibratia cosmica variabila | {{formula_vibratie_cosmica_variabila}} | {{calcul_vibratie_cosmica_variabila}} | {{vibratie_cosmica_variabila}} |
| Vibratia cosmica totala | {{formula_vibratie_cosmica_totala}} | {{calcul_vibratie_cosmica_totala}} | {{vibratie_cosmica_totala}} |

Interpretare:

{{interpretare_vibratii}}

Regula pentru interpretarea ampla a vibratiilor fundamentale: traseul de
reducere se explica conversational numai cand calculul are o reducere
suplimentara. Se interpreteaza direct persoanei cifrele de intrare, suma
intermediara, cifrele reducerii si rezultatul final. Daca valoarea este deja o
singura cifra, se trece direct la interpretarea ei, fara a mentiona ca nu
exista traseu. Daca apare 0, se explica prudent ca nu adauga o directie
numerica separata, dar poate deschide sau amplifica potentialul cifrei
alaturate. La Vibratia globala se interpreteaza mereu combinatia dintre
interior si exterior; traseul de reducere se desface separat numai cand suma
lor depaseste 9. Arhetipurile raman permise numai la Vibratia interioara,
Vibratia exterioara si Vibratia globala.

Dupa interpretarea traseului, accentul cade pe rezultatul final. Paragrafele
urmatoare nu reformuleaza traseul si nici nu repeta aceeasi semnificatie;
fiecare aduce informatie noua printr-o manifestare observabila, un exemplu
practic, o rutina aplicabila, o umbra sau un criteriu de maturizare. Volumul se
mentine prin dezvoltare utila, nu prin reiterare.

Aceasta regula nu se aplica obligatoriu la Calea Destinului, Destin sau
Aspectele de indreptat. Puntile interior-exterior si interior-destin pastreaza
lectura valorilor initiale si a rezultatului. La Solutia aspectelor de
indreptat se recomanda interpretarea rezultatului, fara desfacerea ampla a
traseului de reducere.

### 1.3. Calea destinului, destinul si puntile

| Concept | Formula | Calcul | Rezultat |
| --- | --- | --- | --- |
| Calea Destinului | {{formula_calea_destinului}} | {{calcul_calea_destinului}} | {{calea_destinului}} |
| Calea Destinului karmica | {{formula_calea_destinului_karmica}} | {{calcul_calea_destinului_karmica}} | {{calea_destinului_karmica}} |
| Destinul | {{formula_destin}} | {{calcul_destin}} | {{destin}} |
| Puntea interior - exterior | {{formula_punte_interior_exterior}} | {{calcul_punte_interior_exterior}} | {{punte_interior_exterior}} |
| Puntea interior - destin | {{formula_punte_interior_destin}} | {{calcul_punte_interior_destin}} | {{punte_interior_destin}} |

Interpretare:

{{interpretare_destin_punti}}

### 1.4. Aspecte de indreptat

| Concept | Formula | Calcul | Rezultat |
| --- | --- | --- | --- |
| Aspecte de indreptat | {{formula_aspecte_de_indreptat}} | {{calcul_aspecte_de_indreptat}} | {{aspecte_de_indreptat}} |
| Solutia aspectelor de indreptat | {{formula_solutie_aspecte}} | {{calcul_solutie_aspecte}} | {{solutie_aspecte}} |

Interpretare:

{{interpretare_aspecte_de_indreptat}}

### 1.5. Structura matriciala

#### 1.5.1. Matricea datei de nastere

Chenarul calculului foloseste randuri distincte pentru data compacta, `N1`,
`N2`, `N3`, `N4` si sirul complet.

```text
{{matricea_datei_de_nastere}}
```

#### 1.5.2. Numere pare si impare

{{numere_pare_impare}}

#### 1.5.3. Valoarea casutelor

| Casuta | Cifre | Valoare | Interpretare |
| --- | --- | --- | --- |
| 1 | {{casuta_1_cifre}} | {{casuta_1_valoare}} | {{casuta_1_interpretare}} |
| 2 | {{casuta_2_cifre}} | {{casuta_2_valoare}} | {{casuta_2_interpretare}} |
| 3 | {{casuta_3_cifre}} | {{casuta_3_valoare}} | {{casuta_3_interpretare}} |
| 4 | {{casuta_4_cifre}} | {{casuta_4_valoare}} | {{casuta_4_interpretare}} |
| 5 | {{casuta_5_cifre}} | {{casuta_5_valoare}} | {{casuta_5_interpretare}} |
| 6 | {{casuta_6_cifre}} | {{casuta_6_valoare}} | {{casuta_6_interpretare}} |
| 7 | {{casuta_7_cifre}} | {{casuta_7_valoare}} | {{casuta_7_interpretare}} |
| 8 | {{casuta_8_cifre}} | {{casuta_8_valoare}} | {{casuta_8_interpretare}} |
| 9 | {{casuta_9_cifre}} | {{casuta_9_valoare}} | {{casuta_9_interpretare}} |

#### 1.5.4. Figuri geometrice

{{figuri_geometrice}}

#### 1.5.5. Elemente

{{elemente}}

#### 1.5.6. Vectorii

Nota de redactare: coloana finala se numeste `Interpretare`, nu `Descriere si
interpretare`. Pentru fiecare vector se precizeaza casutele prezente si lipsa,
dominantele si contributia lor numerica, daca este plin sau incomplet si felul
in care compozitia produce valoarea totala. Pentru un vector incomplet,
interpretarea numeste fiecare casuta lipsa si tema ei concreta din matrice.

| Vector | Denumire | Cifre | Valoare | Interpretare |
| --- | --- | --- | --- | --- |
| 123 | Energie | {{vector_123_cifre}} | {{vector_123_valoare}} | {{vector_123_interpretare}} |
| 456 | Vointa | {{vector_456_cifre}} | {{vector_456_valoare}} | {{vector_456_interpretare}} |
| 789 | Creativitate | {{vector_789_cifre}} | {{vector_789_valoare}} | {{vector_789_interpretare}} |
| 147 | Spiritualitate | {{vector_147_cifre}} | {{vector_147_valoare}} | {{vector_147_interpretare}} |
| 258 | Social | {{vector_258_cifre}} | {{vector_258_valoare}} | {{vector_258_interpretare}} |
| 369 | Bunastare materiala | {{vector_369_cifre}} | {{vector_369_valoare}} | {{vector_369_interpretare}} |
| 159 | Cariera | {{vector_159_cifre}} | {{vector_159_valoare}} | {{vector_159_interpretare}} |
| 357 | Scopuri | {{vector_357_cifre}} | {{vector_357_valoare}} | {{vector_357_interpretare}} |

#### 1.5.7. Tendinta

{{tendinta}}

#### 1.5.8. Fixatia

Nota de metoda: se identifica vectorul plin dominant conform documentului
`vault/Numerologie/Fixatia.md`.

Fixatia este vectorul plin cu valoarea cea mai mare. Se explica de ce este
importanta: arata zona spre care energia se duce natural, atat ca talent, cat
si ca risc de exces. Daca nu exista vector plin, se mentioneaza explicit ca nu
exista fixatie matriceala clara.

{{fixatia}}

#### 1.5.9. Caii, trasura si vizitiul

Nota de metoda: se citesc vectorii 1-2-3 ca `caii`, 4-5-6 ca `trasura` si
7-8-9 ca `vizitiul`; vezi `vault/Numerologie/Caii Trasura si Vizitiul.md`.

Interpretarea compara cele trei coloane prin valoare si prin lipsuri:
`caii` arata energia de pornire, `trasura` arata suportul practic/corpul
vehiculului, iar `vizitiul` arata directia mentala si spirituala.

{{caii_trasura_vizitiul}}

#### 1.5.10. Curgerea energiei

Nota de metoda: se urmareste curgerea energiei in matricea datei de nastere,
de sus in jos si de la stanga la dreapta; vezi
`vault/Numerologie/Curgerea Energiei.md`.

{{curgerea_energiei}}

#### 1.5.11. Comparatia cu optimul

Compara toate cele noua casute si toti cei opt vectori. Pentru casute foloseste
tabelul complet:

| Casuta | Cantitate casuta | Valoare casuta | Cantitate optima | Valoare optima | Diferenta | Citire |
| --- | --- | --- | --- | --- | --- | --- |
| {{casuta_optim}} | {{cantitate_casuta}} | {{valoare_casuta}} | {{cantitate_optima}} | {{valoare_optima}} | {{diferenta_optim}} | {{citire_optim}} |

{{comparatia_cu_optimul}}

Regula de redactare pentru cititor: fiecare cod numeric este însoțit imediat
de denumirea lui. De exemplu, `vectorul 789` se scrie `vectorul 789,
Creativitate`, iar `diagonala 159` se scrie `diagonala 159, Carieră`. Se
aplică aceeași regulă tuturor vectorilor și diagonalelor; codul nu rămâne
niciodată neexplicat și cititorul nu este trimis la o secțiune anterioară.

Scara bunastarii este subcapitol separat al Structurii matriciale. Primeste
titlul numerotat `4.6. Scara bunastarii`, ancora proprie si index `SUB` in
variantele de revizie. Se asaza dupa tendinte, fixatie si analogia
cai-trasura-vizitiu. Include exact noua casute si opt vectori, ordonate
descrescator dupa valoare; valorile egale se grupeaza logic, iar valorile zero
raman la baza. In HTML foloseste bare orizontale raportate la valoarea maxima.
Pentru casute afiseaza o bulina cu elementul aferent, iar sub grafic adauga
legenda: Foc, Pamant, Apa, Aer.

| Pozitie | Denumire | Cantitate | Formula | Valoare | Interpretare |
| --- | --- | --- | --- | --- | --- |
| {{pozitie_scara}} | {{denumire_scara}} | {{cantitate_scara}} | {{formula_scara}} | {{valoare_scara}} | {{interpretare_scara}} |

{{grafic_scara_bunastarii}}

### 1.6. Codul numerologic personal al numelui

In chenarul principal, fiecare componenta a numelui ocupa un rand distinct si
include literele, sirul numeric, suma, reducerea si codul. Codul concatenat si
codul personal se afiseaza intr-un al doilea chenar.

| Concept | Formula | Calcul | Rezultat | Interpretare |
| --- | --- | --- | --- | --- |
| Numarul de exprimare | {{formula_numar_exprimare}} | {{calcul_numar_exprimare}} | {{numar_exprimare}} | {{interpretare_numar_exprimare}} |
| Numarul intim | {{formula_numar_intim}} | {{calcul_numar_intim}} | {{numar_intim}} | {{interpretare_numar_intim}} |
| Numarul de realizare | {{formula_numar_realizare}} | {{calcul_numar_realizare}} | {{numar_realizare}} | {{interpretare_numar_realizare}} |
| Numarul activ | {{formula_numar_activ}} | {{calcul_numar_activ}} | {{numar_activ}} | {{interpretare_numar_activ}} |
| Numarul ereditar | {{formula_numar_ereditar}} | {{calcul_numar_ereditar}} | {{numar_ereditar}} | {{interpretare_numar_ereditar}} |
| Numarul ereditar karmic / Neamul | {{formula_numar_neam}} | {{calcul_numar_neam}} | {{numar_neam}} | {{interpretare_numar_neam}} |
| Cifra energetica | {{formula_cifra_energetica}} | {{calcul_cifra_energetica}} | {{cifra_energetica}} | {{interpretare_cifra_energetica}} |

#### 1.6.1. Cifre in exces / cifre lipsa

{{cifre_exces_lipsa}}

#### 1.6.2. Cifre intense

{{cifre_intense}}

#### 1.6.3. Primele litere si ultimele litere

{{primele_litere_ultimele_litere}}

#### 1.6.4. Primele vocale

{{primele_vocale}}

#### 1.6.5. Cheile de bolta

{{cheile_de_bolta}}

#### 1.6.6. Litere mentale, fizice, emotionale, intuitive

{{litere_mentale_fizice_emotionale_intuitive}}

#### 1.6.7. Litere initiatoare, continuatoare, finalizatoare

{{litere_initiatoare_continuatoare_finalizatoare}}

#### 1.6.8. Numerele temperamentului

{{numerele_temperamentului}}

#### 1.6.9. Cifrele de tensiune

{{cifrele_de_tensiune}}

### 1.7. Ciclicitatile

#### 1.7.1. Ciclicitatea vibratiilor

{{ciclicitatea_vibratiilor}}

#### 1.7.2. Ciclicitatea scarii bunastarii

{{ciclicitatea_scarii_bunastarii}}

#### 1.7.3. Lectiile de viata

{{lectiile_de_viata}}

#### 1.7.4. Ciclul de 7 ani

{{ciclul_de_7_ani}}

#### 1.7.5. Ciclul de 9 ani si subciclurile

{{ciclul_de_9_ani_subcicluri}}

#### 1.7.6. Ciclul de 12 ani

{{ciclul_de_12_ani}}

#### 1.7.7. Ciclul de 27 ani

{{ciclul_de_27_ani}}

#### 1.7.8. Pinacluri

| Pinaclu | Interval / varsta | Oportunitate | Provocare | Interpretare |
| --- | --- | --- | --- | --- |
| 1 | {{pinaclu_1_interval}} | {{pinaclu_1_oportunitate}} | {{pinaclu_1_provocare}} | {{pinaclu_1_interpretare}} |
| 2 | {{pinaclu_2_interval}} | {{pinaclu_2_oportunitate}} | {{pinaclu_2_provocare}} | {{pinaclu_2_interpretare}} |
| 3 | {{pinaclu_3_interval}} | {{pinaclu_3_oportunitate}} | {{pinaclu_3_provocare}} | {{pinaclu_3_interpretare}} |
| 4 | {{pinaclu_4_interval}} | {{pinaclu_4_oportunitate}} | {{pinaclu_4_provocare}} | {{pinaclu_4_interpretare}} |

#### 1.7.9. Ani sub neam / ani independenti de neam

{{ani_sub_neam_independenti}}

#### 1.7.10. Ani importanti interiori, exteriori, de criza si de rascruce

| An | Interior | Exterior | Criza | Rascruce | Interpretare |
| --- | --- | --- | --- | --- | --- |
| {{an}} | {{an_interior}} | {{an_exterior}} | {{an_criza}} | {{an_rascruce}} | {{interpretare_an}} |

#### 1.7.11. Soarta si destin

{{soarta_si_destin}}

Ordine obligatorie pentru aceasta rubrica:

1. calculele si graficul Soarta si Destin;
2. tabelul comparativ pe intervale de varsta (`Varsta`, `Soarta`, `Destin`, `Citire`) si interpretarea aferenta graficului;
3. subtitlul si continutul pentru Harta suprapusa Soarta-Destin-Ciclicitati.

Tabelul si interpretarea care explica graficul Soarta si Destin se pastreaza in aceasta rubrica, imediat dupa grafic. Nu se muta dupa Harta suprapusa.

In tabel, prima coloana este `Varsta`, nu pozitia ordinala. Intervalele pornesc de la 0 si urmeaza pasul de lectura stabilit pentru persoana analizata: din 10 in 10 ani (`0-10`, `10-20`, `20-30` etc.) sau din 12 in 12 ani (`0-12`, `12-24`, `24-36` etc.).

### 1.8. Relatii

- Nume: {{nume_complet_partener}}
- Data nasterii: {{data_nasterii_partener}}
- Tipul relatiei: {{tip_relatie_analizata}}

Acest bloc este strict factual si sta imediat dupa titlul capitolului, inainte
de primul subcapitol. Daca nu este declarata nicio relatie in datele persoanei,
se elimina integral capitolul `Relatii` si intrarea lui din cuprins.

#### 1.8.1. Omuletul relatiilor

Integreaza PNG-ul validat de `900 x 840 px`, nu SVG-ul. In HTML autonom,
foloseste `data:image/png;base64,...`; pastreaza SVG-ul numai ca sursa tehnica.

{{omuletul_relatiilor}}

### 1.9. Spirit

#### 1.9.1. Inclinatii profesionale

{{inclinatii_profesionale}}

Formularea trebuie să fie conversațională și explicită: `Aplicabilitatea
profesională DA este arcana X, Nume`, urmată de direcția care poate fi
cultivată, iar `Aplicabilitatea profesională NU este arcana Y, Nume`, urmată
de obstacolul posibil și de pașii concreți prin care acesta este echilibrat.

#### 1.9.2. Inclinatii ezoterice

{{inclinatii_ezoterice}}

#### 1.9.3. Codul Spiritului si Varsta Spiritului

{{codul_spiritului_varsta_spiritului}}

#### 1.9.4. Etapele si subetapele spiritului

{{etapele_subetapele_spiritului}}

### 1.10. Ajutoare

#### 1.10.1. Semnatura astrala

{{semnatura_astrala}}

#### 1.10.2. Directiile de succes

{{directiile_de_succes}}

#### 1.10.3. Triunghiul financiar

Formula: `ziua redusa` + `luna redusa` + `anul redus` + `destinul redus`.
Destinul se obtine din suma celor trei componente deja reduse.

{{triunghiul_financiar}}

#### 1.10.4. Patratul de aur 3x3

{{patratul_de_aur_3x3}}

### 1.11. Concluziile capitolului 1

#### 1.11.1. Toate notiunile grupate pe cifre si elemente

{{notiuni_grupate_pe_cifre_si_elemente}}

#### 1.11.2. Tabelul tuturor informatiilor reunite

{{tabelul_tuturor_informatiilor_reunite}}

#### 1.11.3. Graficul tuturor informatiilor reunite

{{graficul_tuturor_informatiilor_reunite}}

---
## Capitolul 2. Caracterul

### 2.1. Vibratia interioara

#### 2.1.1. Vibratia interioara pitagoreica

{{caracter_vibratie_interioara_pitagoreica}}

#### 2.1.2. Liniile de tensiune

{{caracter_linii_de_tensiune}}

#### 2.1.3. Vibratia interioara karmica

{{caracter_vibratie_interioara_karmica}}

### 2.2. Structura matriciala

#### 2.2.1. Reflectarea vibratiei interioare in casute

{{reflectarea_vibratiei_interioare_in_casute}}

#### 2.2.2. Casutele calitativ si cantitativ

{{casutele_calitativ_cantitativ}}

#### 2.2.3. Par / impar

{{par_impar}}

#### 2.2.4. Elementele

{{elementele_caracterului}}

#### 2.2.5. Valoarea casutelor

{{valoarea_casutelor_caracter}}

#### 2.2.6. Forma geometrica

{{forma_geometrica}}

#### 2.2.7. Descrierea casutelor

{{descrierea_casutelor}}

#### 2.2.8. Combinatiile speciale

{{combinatiile_speciale}}

#### 2.2.9. Vectorii

{{vectorii_caracter}}

#### 2.2.10. Fixatia

Nota de metoda: interpretarea caracterului foloseste aceeasi fixatie calculata
din matricea datei de nastere; vezi `vault/Numerologie/Fixatia.md`.

{{fixatia_caracter}}

#### 2.2.11. Tendinta

{{tendinta_caracter}}

#### 2.2.12. Valoarea cea mai mare

{{valoarea_cea_mai_mare}}

#### 2.2.13. Curgerea energiei

Nota de metoda: interpretarea caracterului foloseste aceeasi curgere a energiei
din matricea datei de nastere; vezi `vault/Numerologie/Curgerea Energiei.md`.

{{curgerea_energiei_caracter}}

#### 2.2.14. Caii, trasura si vizitiul

Nota de metoda: interpretarea caracterului compara caii, trasura si vizitiul
din matricea datei de nastere; vezi
`vault/Numerologie/Caii Trasura si Vizitiul.md`.

{{caii_trasura_vizitiul_caracter}}

### 2.3. Influente spirituale

#### 2.3.1. Inclinatii profesionale

{{caracter_inclinatii_profesionale}}

#### 2.3.2. Inclinatii ezoterice

{{caracter_inclinatii_ezoterice}}

#### 2.3.3. Zona de confort intre soarta si destin

{{zona_confort_soarta_destin}}

#### 2.3.4. Pinaclul 1

{{pinaclul_1_caracter}}

#### 2.3.5. Codul si Varsta Spiritului

{{codul_varsta_spiritului_caracter}}

#### 2.3.6. Etapele si subetapele spiritului

{{etape_subetape_spirit_caracter}}

### 2.4. Influentele numelui

#### 2.4.1. Numarul activ

{{caracter_numar_activ}}

#### 2.4.2. Numarul ereditar karmic / Numele Neamului

{{caracter_numar_neam}}

#### 2.4.3. Numarul intim

{{caracter_numar_intim}}

#### 2.4.4. Numarul de realizare

{{caracter_numar_realizare}}

#### 2.4.5. Cifre in exces si cifre lipsa

{{caracter_cifre_exces_lipsa}}

### 2.5. Concluziile caracterului

{{concluziile_caracterului}}

---
## Capitolul 3. Transformarea

### 3.1. Vibratia exterioara

{{transformare_vibratia_exterioara}}

### 3.2. Programul karmic social

{{programul_karmic_social}}

### 3.3. Numarul de realizare din nume

{{transformare_numar_realizare}}

### 3.4. Contextele - vibratia globala

{{contextele_vibratia_globala}}

### 3.5. Puntea dintre vibratia interioara si cea exterioara

{{transformare_punte_interior_exterior}}

### 3.6. Puntea dintre vibratia interioara si cea a destinului

{{transformare_punte_interior_destin}}

### 3.7. Calea Destinului

{{transformare_calea_destinului}}

### 3.8. Aspecte de indreptat si solutia

{{transformare_aspecte_de_indreptat_solutie}}

{{transformare_scara_bunastarii}}

### 3.10. Lectiile de viata

{{transformare_lectii_de_viata}}

### 3.11. Pinaclurile

{{transformare_pinacluri}}

### 3.12. Inclinatiile profesionale

{{transformare_inclinatii_profesionale}}

### 3.13. Inclinatiile ezoterice

{{transformare_inclinatii_ezoterice}}

### 3.14. Spiritul

{{transformare_spiritul}}

### 3.15. Soarta si destinul

{{transformare_soarta_destinul}}

Regula de compunere pentru o sectiune separata „Transformarea prin cicluri”:

- Reutilizeaza harta suprapusa Soarta-Destin-Ciclicitati deja generata in capitolul 1, cu acelasi index de figura, ca suport vizual pentru interpretare.
- Plaseaza figura imediat sub subtitlu, inainte de primul paragraf interpretativ despre cicluri.
- Pastreaza aceeasi sursa SVG si adauga o legenda care precizeaza utilizarea ei pentru interpretarea ciclurilor.

### 3.16. Liniile de tensiune

{{transformare_linii_de_tensiune}}

### 3.17. Concluziile transformarii

{{concluziile_transformarii}}

---
## Capitolul 4. Destinul

### 4.1. Vibratia Destinului

{{destin_vibratia_destinului}}

### 4.2. Pinaclul 3

{{destin_pinaclul_3}}

### 4.3. Solutia aspectelor de indreptat

{{destin_solutia_aspectelor_de_indreptat}}

### 4.4. Vibratia cosmica variabila si totala

{{destin_vibratia_cosmica_variabila_totala}}

### 4.5. Etapele si subetapele spiritului

{{destin_etape_subetape_spirit}}

### 4.6. Potentialul ezoteric

{{destin_potential_ezoteric}}

### 4.7. Potentialul numelui - numarul de exprimare

{{destin_potential_nume_numar_exprimare}}

### 4.8. Potentialul caracterului

{{destin_potential_caracter}}

### 4.9. Concluziile destinului

{{concluziile_destinului}}

---
## Capitolul 5. Parcursul vietii

### 5.1. Ansamblul geometric al lui Pitagora

{{ansamblul_geometric_al_lui_pitagora}}

### 5.2. Cele patru perioade mari

{{cele_patru_perioade_mari}}

#### 5.2.1. Perioada de formare

{{perioada_de_formare}}

#### 5.2.2. Perioada de maturizare

{{perioada_de_maturizare}}

#### 5.2.3. Perioada de inteleptire

{{perioada_de_inteleptire}}

#### 5.2.4. Perioada de spiritualizare

{{perioada_de_spiritualizare}}

### 5.3. Concluziile parcursului vietii

{{concluziile_parcursului_vietii}}

---
## Capitolul 6. Ajutoare

Ajutoarele sunt instrumente simbolice de sustinere, construite pe baza hartii
numerologice personale. Ele pot fi privite ca talismane: obiecte, placute,
carduri, medalioane sau elemente decorative pe care se imprima o schema
numerologica, cum ar fi semnatura astrala, triunghiul financiar sau patratul
de aur. Rolul lor este sa functioneze ca puncte de orientare, nu ca inlocuitor
pentru decizie, disciplina sau actiune concreta.

Un ajutor bine construit devine o ancora vizuala si energetica. El sustine
alinierea cu ceea ce persoana are de facut, clarifica intentia si ajuta la
organizarea atentiei. In interpretare se explica felul in care talismanul poate
fi purtat, asezat in spatiul de lucru sau folosit intr-un ritual personal
simplu, pentru a lega intentia de actiune si rezultat.

### 6.1. Semnatura astrala

{{ajutoare_semnatura_astrala}}

### 6.2. Directiile de succes

{{ajutoare_directii_de_succes}}

### 6.3. Triunghiul financiar

Regula de calcul: triunghiul financiar este triunghiul rosu personal, cu varful
in sus. Pe baza de jos se scriu patru cifre: ziua nasterii redusa la o cifra,
luna nasterii redusa la o cifra, anul nasterii redus la o cifra si suma
acestor trei cifre redusa la o cifra, adica destinul.

Forma geometrica este un triunghi isoscel rosu, cu apexul de `36` de grade si
unghiurile de la baza de `72` de grade.

{{ajutoare_triunghi_financiar}}

### 6.4. Patratul de aur 3x3

Regula de calcul: se foloseste asezarea patratului lui Pitagora, cu ordinea
casutelor `1-4-7 / 2-5-8 / 3-6-9`. Ziua nasterii, fara reducere, se introduce
in casuta `4`. Se continua crescator, cu cate `+1`, pe traseul:

```text
4 -> 9 -> 2 -> 3 -> 5 -> 7 -> 8 -> 1 -> 6
```

Valoarea centrala este `ziua nasterii + 4`, iar suma de control este
`valoarea centrala x 3`. Toate liniile si toate coloanele trebuie sa dea
aceeasi valoare; pentru validarea completa se verifica si cele doua diagonale.

{{ajutoare_patratul_de_aur_3x3}}

---
## Capitolul 7. Concluzii finale pentru numerologi

### 7.1. Concluzie asupra rezultatelor principale

{{concluzie_rezultate_principale}}

### 7.2. Elemente dominante

{{elemente_dominante}}

### 7.3. Elemente de echilibrat

{{elemente_de_echilibrat}}

### 7.4. Concluzie finala

{{concluzie_finala_pentru_numerologi}}

---
## Capitolul 8. Sfatul numerologului

### 8.1. Directia principala

{{sfat_directia_principala}}

### 8.2. Recomandari practice

{{sfat_recomandari_practice}}

### 8.3. Perioada analizata

{{sfat_perioada_analizata}}

### 8.4. Concluzia sfatului numerologic

{{concluzia_sfatului_numerologic}}

---
## Capitol temporar de revizie. Documentatia si trasabilitatea lucrarii

Acest capitol exista numai in variantele cu sufix `r`. Se elimina integral din
variantele finale cu sufix `f`.

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

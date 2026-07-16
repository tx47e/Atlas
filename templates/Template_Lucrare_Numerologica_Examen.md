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
- Pentru lucrarile numerologice complete si pentru orice modificare de template
  de lucrare, acesta este template-ul principal de referinta.
- Se completeaza campurile dintre acolade.
- Nu se introduc link-uri catre lucrari, fisiere sau documente externe.
- Pentru fiecare capitol se pastreaza calculul, rezultatul si interpretarea.
- Cand un calcul are mai multi pasi, pasii se leaga cu ` -> `, nu cu punct si
  virgula. Inaintea fiecarui chenar de calcul se scrie un paragraf text care
  explica metoda: ce date se iau, ce se aduna/scade/inmulteste si de ce se
  reduce rezultatul. In chenarul de calcul ramane doar traseul numeric si
  rezultatul final marcat cu rosu. Interpretarea rezultatului sta dupa chenar.
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

- Pentru lucrarile livrate clientului, HTML-ul canonic este forma folosita in
  lucrarea `1998-02-19-BIRSAN-DANIEL-ROBERT-v1.04r.html`. La generarea unei
  lucrari noi se preia structura completa a acelui HTML: topbar, cuprins rapid,
  indexuri, clase CSS, casete de calcul, tabele, figuri, spacing, culori si
  formatare. Nu se foloseste un convertor Markdown simplificat daca rezultatul
  nu reproduce formatarea lucrarii Daniel.
- Pentru o persoana noua se editeaza in HTML doar continutul variabil:
  nume, data nasterii, date relationale, texte personalizate, calcule,
  interpretari, tabele si sursele imaginilor/SVG/PNG. Structura vizuala ramane
  identica.
- Interpretarile se redacteaza in stilul lucrarii Daniel v1.04r: cald,
  explicativ si imagistic, nu tehnic sau mecanic. Pentru fiecare interpretare
  majora se includ, dupa caz, definitia ideii, o analogie usor de vizualizat,
  arhetipul vibratiei, manifestarea concreta in viata, umbra/tensiunea si cheia
  de maturizare.
- Se evita repetitia de tip sablon, de exemplu formule recurente precum
  "Privit in contextul..." sau paragrafe care schimba doar cifra. Fiecare text
  trebuie sa sune ca o citire personalizata pentru omul analizat, nu ca o
  completare automata a unui tabel.
- Daca o lucrare intermediara exista doar in Markdown, ea poate fi folosita ca
  sursa de calcul si text, dar HTML-ul final se reconstruieste pe baza
  layoutului canonic Daniel.
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
- Chenarul de calcul nu contine explicatii narative, propozitii de metoda sau
  interpretari. Continut permis in chenar: formula numerica, pasi intermediari,
  sageti `->`, semne matematice, etichete scurte precum `DA`, `NU`, `Destin`,
  `CM`, si rezultatul final in `<strong>...</strong>`.
- Rezultatul final din fiecare chenar de calcul se marcheaza obligatoriu cu
  `<strong>...</strong>`, deoarece stilul `.calc-box strong` il afiseaza cu
  rosu. Nu se marcheaza cu rosu tot calculul, ci doar rezultatul final sau
  rezultatele finale cand sunt doua randuri, de exemplu `DA` si `NU`.

Exemplu corect:

```html
<p>Pentru vibratia interioara luam ziua nasterii si reducem suma cifrelor pana
la o singura cifra. Daca apare un numar compus important, il pastram in calcul
ca nuanta.</p>
<div class="calc-box">1 + 2 = 3 -> <strong>3</strong></div>
<p>Vibratia 3 se interpreteaza ca expresie, comunicare si nevoie de creatie...</p>
```

Exemplu corect pentru doua randuri:

```html
<p>Pentru inclinatiile profesionale citim doua directii: aplicabilitatea
profesionala pe randul DA si obstacolul principal pe randul NU.</p>
<div class="calc-box">
  DA: 1 + 27 = 28 -> 28 - 22 = <strong>6</strong><br>
  NU: 31 -> 31 - 22 = <strong>9</strong>
</div>
```

Exemplu gresit:

```html
<div class="calc-box">
  Pentru vibratia interioara luam ziua nasterii, iar rezultatul arata energia
  de pornire. 1 + 2 = 3.
</div>
```

### Reguli de compunere a paragrafelor interpretative

Fiecare subcapitol interpretativ se construieste in aceasta ordine:

1. **Definitie**: se explica pe scurt ce masoara conceptul, fara sa se intre
   imediat in rezultat. Exemplu: "Vibratia interioara arata felul in care omul
   porneste din interior, inainte sa se adapteze la lume."
2. **Calcul / rezultat**: inainte de chenar se scrie metoda in proza, iar in
   chenar se afiseaza doar calculul si rezultatul final cu `<strong>...</strong>`.
   Daca sunt mai multe componente, fiecare componenta ramane pe rand separat.
3. **Expresie simbolica**: se spune ce inseamna rezultatul ca imagine. Se
   foloseste o analogie concreta, ca cititorul sa poata vedea conceptul:
   izvor, usa, casa, atelier, biblioteca, drum, pod, harta, busola, oglinda,
   radacina, schelet, haina simbolica.
4. **Arhetip**: se numesc arhetipurile vibratiei sau ale numarului. Exemplu:
   pentru 4: arhitectul, constructorul, administratorul; pentru 7:
   cercetatorul, observatorul, initiatul, ermitul.
5. **Manifestare concreta**: se descrie cum poate aparea in viata de zi cu zi,
   in relatii, decizii, munca, ritm interior, comunicare sau responsabilitate.
6. **Umbra / tensiune**: se arata unde energia se poate dezechilibra, fara ton
   fatalist si fara etichete dure.
7. **Cheie de maturizare**: se incheie cu directia practica: ce are de educat,
   asezat, exprimat, construit, acceptat sau rafinat persoana.

Formula minima pentru o interpretare majora este:

```text
Ce este conceptul -> Calculul -> Imaginea -> Arhetipul -> Cum se vede in viata
-> Umbra -> Cheia de maturizare
```

Nu se accepta interpretari formate doar din sinonime ale cifrei. Un paragraf de
tipul "numarul 4 inseamna ordine, stabilitate si disciplina" este incomplet daca
nu explica imaginea, arhetipul, manifestarea, umbra si cheia practica pentru
persoana analizata.

### Rolul fiecarui capitol in redactare

- **Capitolul 1** este baza tehnica si vizuala a lucrarii. Aici se afiseaza
  formulele, calculele, tabelele, matricile, graficele si SVG/PNG-urile. Textul
  explica suficient ca cititorul sa inteleaga de unde vin rezultatele, dar nu
  trebuie sa devina concluzia finala a lucrarii.
- **Capitolul 2 - Caracterul** citeste omul din interior. Se foloseste
  vibratia interioara, matricea, fixatia, tendinta, curgerea energiei, caii,
  trasura si vizitiul, apoi influentele spirituale si ale numelui. Tonul este:
  "asa porneste energia ta si asa se organizeaza caracterul tau".
- **Capitolul 3 - Transformarea** arata ce se schimba, ce se cere educat si
  cum se muta energia din potential in comportament. Se explica tensiunile,
  puntile, ciclurile, lectiile, pinaclurile si suprapunerile dintre interior si
  exterior. Tonul este: "asa se transforma energia ta cand incepi sa o folosesti
  constient".
- **Capitolul 4 - Destinul** leaga directia mare de rezultate: destin, calea
  destinului, pinaclul relevant, solutia aspectelor, numele, caracterul si
  potentialul spiritual. Tonul este: "incotro se cere condusa energia ta".
- **Capitolul 5 - Parcursul vietii** citeste perioadele. Nu se scrie ca
  predictie rigida, ci ca harta de orientare: etape, varste, cicluri, crize,
  rascruci, sincronizari si momente de maturizare.
- **Capitolul 6 - Ajutoare** explica instrumentele vizuale si talismanele:
  semnatura astrala, directiile de succes, triunghiul financiar, patratul de
  aur si alte amulete. Textul trebuie sa explice cum se foloseste simbolul, nu
  doar cum se calculeaza.
- **Capitolul 7 - Concluzii finale pentru numerologi** strange rezultatele
  intr-o imagine coerenta pentru specialist. Se foloseste limbaj sintetic, dar
  nu sec: rezultate principale, dominante, elemente de echilibrat, concluzie.
- **Capitolul 8 - Sfatul numerologului** traduce lucrarea in orientare
  practica. Se foloseste persoana a doua, cu recomandari clare, aplicabile si
  fara ton moralizator.

### Reguli pentru expresie si limbaj

- Textul se adreseaza persoanei analizate direct, pe nume, acolo unde este
  firesc. Nu se repeta numele in fiecare paragraf.
- Se alterneaza frazele scurte cu fraze explicative. Nu se foloseste acelasi
  inceput de paragraf de mai multe ori la rand.
- Fiecare cifra importanta primeste cel putin o imagine si un arhetip in
  capitolul in care este interpretata major.
- Cand doua energii sunt comparate, se foloseste o imagine de relatie intre ele:
  doua camere ale aceleiasi case, un pod intre doua maluri, caii si vizitiul,
  radacina si coroana, harta si drumul.
- Cand apar suprapuneri de cicluri, ani interiori/exteriori, crize si pinacluri,
  interpretarea explica sincronizarea: ce se misca in interior, ce vine din
  exterior si de ce perioada respectiva devine mai intensa.
- Tabelele pot avea interpretari concise, dar dupa un tabel important trebuie
  sa existe un paragraf de sinteza care spune ce inseamna ansamblul.

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

Redactare obligatorie: interpretarea vibratiilor se face pe rand pentru
Vibratia interioara, Vibratia exterioara si Vibratia globala. Pentru fiecare se
scriu definitia rolului, imaginea simbolica, arhetipurile vibratiei,
manifestarea concreta, umbra si cheia de maturizare. La final se adauga un
paragraf de sinteza care arata cum lucreaza impreuna VI, VE si VG.

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

Redactare obligatorie: se explica diferenta dintre calea destinului si destinul
redus. Calea destinului este drumul complet, destinul este directia principala.
Puntile se interpreteaza ca legaturi intre parti ale persoanei, nu doar ca
diferente matematice. Pentru fiecare punte se spune ce are de unit persoana si
ce se intampla cand acea punte ramane neconstientizata.

Nu se accepta interpretari scurte de tip definitie + rezultat. Pentru fiecare
rubrica se scriu minimum doua paragrafe dupa calcul:

- **Calea destinului**: explica numarul compus, cifrele care il alcatuiesc si
  reducerea finala. Se foloseste o imagine de drum, casa, atelier, harta sau
  constructie. Textul trebuie sa arate cum se formeaza destinul, nu doar cifra
  la care ajunge.
- **Destinul**: se formuleaza ca directie de maturizare si implinire, nu ca
  verdict. Include arhetipurile cifrei, manifestarea concreta in viata si
  imaginea principala a drumului. Exemplu de constructie: "Destinul X nu cere
  doar..., ci invata persoana sa...".
- **Puntea interior - exterior**: descrie cele doua capete ale puntii: ce
  simte persoana in interior si cum apare in exterior. Interpretarea trebuie sa
  contina o analogie de pod, traducator, usa, ritm sau acordaj si o situatie de
  viata concreta.
- **Puntea interior - destin**: arata cum motivatia profunda ajunge sa serveasca
  directia mare a vietii. Se scrie ce se blocheaza cand puntea lipseste si ce se
  activeaza cand persoana o foloseste constient.

Model de ton, adaptabil cifrelor reale:

```text
Calea {{calea_destinului}} se citeste prin cifrele care o compun si prin
reducerea finala la {{destin}}. Daca destinul este titlul capitolului, calea
destinului este povestea din spatele titlului: materialele, ritmul si felul in
care omul ajunge la directia sa.

Pentru {{prenume}}, aceasta cale poate fi vazuta ca {{imagine_cale_destin}}.
{{cifra_1_din_cale}} aduce {{semnificatie_cifra_1}},
{{cifra_2_din_cale}} aduce {{semnificatie_cifra_2}}, iar
{{destin}} cere ca aceste energii sa devina {{directie_concreta_destin}}.
Imaginea trebuie sa fie vizuala si personala, nu generica.
```

{{interpretare_destin_punti}}

### 1.4. Aspecte de indreptat

| Concept | Formula | Calcul | Rezultat |
| --- | --- | --- | --- |
| Aspecte de indreptat | {{formula_aspecte_de_indreptat}} | {{calcul_aspecte_de_indreptat}} | {{aspecte_de_indreptat}} |
| Solutia aspectelor de indreptat | {{formula_solutie_aspecte}} | {{calcul_solutie_aspecte}} | {{solutie_aspecte}} |

Interpretare:

Redactare obligatorie: aspectul de indreptat se explica precum o zona care cere
educare, nu ca defect. Solutia se scrie ca raspuns practic si simbolic. Se
foloseste imaginea oglinzii, a reglajului sau a instrumentului care trebuie
acordat.

Pentru **Solutia aspectelor de indreptat**, interpretarea trebuie sa fie la fel
de dezvoltata ca la Daniel: minimum doua paragrafe dupa calcul. Primul explica
de ce solutia este antidotul aspectului de indreptat. Al doilea coboara cheia
in viata concreta: cum se comunica, cum se decide, cum se pune limita, cum se
coopereaza sau cum se reaseaza energia, in functie de cifra solutiei.

Se includ obligatoriu:

- arhetipurile cifrei solutiei;
- o imagine concreta, de exemplu oglinda asezata in lumina, instrument acordat,
  pod peste apa, busola, cheie, atelier;
- diferenta dintre forma imatura si forma matura a solutiei;
- o fraza practica de tipul: "In practica, asta inseamna...".

{{interpretare_aspecte_de_indreptat}}

### 1.5. Structura matriciala

#### 1.5.1. Matricea datei de nastere

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
interpretare`. Pentru fiecare vector se precizeaza daca este plin sau incomplet.
Daca este incomplet, interpretarea numeste casuta lipsa si tema ei concreta
din matrice.

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

{{comparatia_cu_optimul}}

Regula de redactare pentru cititor: fiecare cod numeric este însoțit imediat
de denumirea lui. De exemplu, `vectorul 789` se scrie `vectorul 789,
Creativitate`, iar `diagonala 159` se scrie `diagonala 159, Carieră`. Se
aplică aceeași regulă tuturor vectorilor și diagonalelor; codul nu rămâne
niciodată neexplicat și cititorul nu este trimis la o secțiune anterioară.

Scara bunastarii este subcapitol separat al Structurii matriciale. Primeste
titlul numerotat `4.6. Scara bunastarii`, ancora proprie si index `SUB` in
variantele de revizie. Se asaza dupa comparatia cu optimul si se ordoneaza
descrescator, incluzand atat vectorii, cat si casutele. In HTML se recomanda
grafic cu bare raportate la valoarea maxima
din scara. Pentru casute se afiseaza o bulina cu elementul aferent, iar sub
grafic se adauga legenda: Foc, Pamant, Apa, Aer.

| Pozitie | Denumire | Cantitate | Formula | Valoare | Interpretare |
| --- | --- | --- | --- | --- | --- |
| {{pozitie_scara}} | {{denumire_scara}} | {{cantitate_scara}} | {{formula_scara}} | {{valoare_scara}} | {{interpretare_scara}} |

{{grafic_scara_bunastarii}}

### 1.6. Codul numerologic personal al numelui

Regula de afisare pentru calculele numelui: fiecare componenta a numelui se
scrie pe rand separat, ca sa fie usor de verificat si de inlocuit la o alta
persoana. Pentru numarul de exprimare se foloseste ordinea:

**{{nume_familie}}:** {{calcul_nume_familie}}

**{{prenume_1}}:** {{calcul_prenume_1}}

**{{prenume_2}}:** {{calcul_prenume_2}}

**Numarul de exprimare:** {{calcul_numar_exprimare_detaliat}}

Pentru codul literelor numelui se foloseste aceeasi regula de separare:

**Codul literelor numelui:** {{cod_litere_nume}}

**Codul numerologic personal al numelui:** {{cod_numerologic_personal_nume}}

| Concept | Formula | Calcul | Rezultat | Interpretare |
| --- | --- | --- | --- | --- |
| Numarul de exprimare | {{formula_numar_exprimare}} | {{calcul_numar_exprimare}} | {{numar_exprimare}} | {{interpretare_numar_exprimare}} |
| Numarul intim | {{formula_numar_intim}} | {{calcul_numar_intim}} | {{numar_intim}} | {{interpretare_numar_intim}} |
| Numarul de realizare | {{formula_numar_realizare}} | {{calcul_numar_realizare}} | {{numar_realizare}} | {{interpretare_numar_realizare}} |
| Numarul activ | {{formula_numar_activ}} | {{calcul_numar_activ}} | {{numar_activ}} | {{interpretare_numar_activ}} |
| Numarul ereditar | {{formula_numar_ereditar}} | {{calcul_numar_ereditar}} | {{numar_ereditar}} | {{interpretare_numar_ereditar}} |
| Numarul ereditar karmic / Neamul | {{formula_numar_neam}} | {{calcul_numar_neam}} | {{numar_neam}} | {{interpretare_numar_neam}} |
| Cifra energetica | {{formula_cifra_energetica}} | {{calcul_cifra_energetica}} | {{cifra_energetica}} | {{interpretare_cifra_energetica}} |

Redactare obligatorie pentru nume: numarul de exprimare este "haina simbolica"
prin care persoana intra in lume; numarul intim este respiratia interioara a
numelui; numarul de realizare este scheletul prin care numele devine concret;
numarul activ este usa prenumelui folosit; numarul ereditar este mostenirea de
familie; numarul neamului este radacina arhetipala. Fiecare interpretare include
arhetip, manifestare, umbra si cheie de maturizare.

#### 1.6.1. Cifre in exces / cifre lipsa

{{cifre_exces_lipsa}}

#### 1.6.2. Cifre intense

{{cifre_intense}}

Redactare obligatorie: cifrele intense se explica precum camere foarte luminate
ale numelui. Se arata ce talent accentueaza, unde pot crea exces si cum pot fi
folosite matur.

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

Redactare obligatorie: ciclurile se explica prin ritm, nu ca predictie fixa.
Pentru fiecare ciclu se precizeaza varstele, vibratia activa, tema de lucru si
felul in care persoana poate coopera cu perioada.

{{ciclicitatea_vibratiilor}}

#### 1.7.2. Ciclicitatea scarii bunastarii

{{ciclicitatea_scarii_bunastarii}}

#### 1.7.3. Lectiile de viata

{{lectiile_de_viata}}

#### 1.7.4. Ciclul de 7 ani

{{ciclul_de_7_ani}}

Regula HTML: tabelul foloseste clasa dedicata `cycle-7-table`. Se reduc numai
fontul si spatierea celulelor din antet; fontul corpului ramane neschimbat.
Tabelul se adapteaza la latimea documentului si nu pastreaza o latime minima
rigida care sa produca bara orizontala pe afisarea desktop obisnuita.

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

Redactare obligatorie: cand anii importanti interiori si exteriori se suprapun,
interpretarea spune explicit ca schimbarea interioara este sincronizata cu
schimbarea venita din exterior. Daca suprapunerea se repeta din 9 in 9 ani, se
leaga de ciclul de 9 ani si se explica perioada ca o fereastra de maturizare
recurenta.

#### 1.7.11. Soarta si destin

{{soarta_si_destin}}

Ordine obligatorie pentru aceasta rubrica:

1. calculele si graficul Soarta si Destin;
2. tabelul comparativ pe intervale de varsta (`Varsta`, `Soarta`, `Destin`, `Citire`) si interpretarea aferenta graficului;
3. subtitlul si continutul pentru Harta suprapusa Soarta-Destin-Ciclicitati.

Tabelul si interpretarea care explica graficul Soarta si Destin se pastreaza in aceasta rubrica, imediat dupa grafic. Nu se muta dupa Harta suprapusa.

In tabel, prima coloana este `Varsta`, nu pozitia ordinala. Intervalele pornesc de la 0 si urmeaza pasul de lectura stabilit pentru persoana analizata: din 10 in 10 ani (`0-10`, `10-20`, `20-30` etc.) sau din 12 in 12 ani (`0-12`, `12-24`, `24-36` etc.).

Interpretarea de dupa tabel se adreseaza direct persoanei, pe prenume, ca o
discutie. Explica de ce se foloseste pasul de 10 sau 12 ani, ce spune zona de
confort si cum se citesc varstele-cheie. Pastreaza valorile tehnice, dar evita
deschiderile distante de tipul `Pentru [nume] folosim...`.

### 1.8. Relatii

- Nume: {{nume_complet_partener}}
- Data nasterii: {{data_nasterii_partener}}
- Tipul relatiei: {{tip_relatie_analizata}}

Acest bloc este strict factual si sta imediat dupa titlul capitolului, inainte
de primul subcapitol. Daca nu este declarata nicio relatie in datele persoanei,
se elimina integral capitolul `Relatii` si intrarea lui din cuprins.

#### 1.8.1. Omuletul relatiilor

Analiza relationala priveste felul in care se combina energiile celor doua date
de nastere, ce potential de realizare apare impreuna, ce trebuie rezolvat in doi
si ce obiceiuri pot transforma atractia sau tensiunea in cooperare concreta.

Pentru amuletul relatiilor se pastreaza SVG-ul ca sursa editabila, dar in
lucrarea livrata se introduce PNG-ul generat din SVG, pentru dimensiune mai
mica. In Markdown se foloseste imaginea PNG, iar in HTML-ul livrat la client
PNG-ul se poate include ca `data:image/png;base64,...` ca sa ramana fisier unic.

{{omuletul_relatiilor}}

Redactare obligatorie: datele persoanei si tipul relatiei apar in blocul factual
de la inceputul capitolului. Dupa omulet se scrie o interpretare
conversationala: ce vine natural, ce lipseste, ce trebuie
construit constient si ce obiceiuri concrete ajuta relatia.
Pentru fiecare grupa de indicatii asociata unei zone absente, scrie cifra
corespunzatoare in paranteza. Explica faptul ca tema poate fi construita
intentionat in cuplu sau sustinuta printr-un aport extern si ofera un exemplu
practic pentru fiecare cifra absenta.

### 1.9. Spirit

#### 1.9.1. Inclinatii profesionale

Redactare obligatorie: se afiseaza calculul pe doua randuri, DA si NU. Se
introduc imaginile arcanelor in tabel. Pentru fiecare arcana se explica
arhetipul profesional, directia buna, obstacolul si cheia de lucru.

{{inclinatii_profesionale}}

Formularea trebuie să fie conversațională și explicită: `Aplicabilitatea
profesională DA este arcana X, Nume`, urmată de direcția care poate fi
cultivată, iar `Aplicabilitatea profesională NU este arcana Y, Nume`, urmată
de obstacolul posibil și de pașii concreți prin care acesta este echilibrat.

#### 1.9.2. Inclinatii ezoterice

Redactare obligatorie: se afiseaza calculul pe doua randuri, DA si NU, apoi
arcanele asociate. Interpretarea nu promite capacitati speciale, ci explica
sensibilitatea, tipul de intuitie, riscul de proiectie si modul sanatos de
folosire.

{{inclinatii_ezoterice}}

#### 1.9.3. Codul Spiritului si Varsta Spiritului

Nota de metoda: CM se alege direct din tabelul rapid al Codului Spiritului, nu
se calculeaza prin formula separata. In lucrare trebuie inclus tabelul
`T-006` 1:1, cu aceeasi formatare de font, casute si fundal, iar celula CM
se marcheaza vizual la intersectia dintre ziua nasterii si luna nasterii.
Explicatia pentru subetapa porneste de la CM selectat din tabel.

{{codul_spiritului_varsta_spiritului}}

Redactare obligatorie: dupa tabelul T-006 marcat cu CM, se explica selectia CM,
apoi varsta spiritului si subetapa. Textul trebuie sa spuna ce fel de maturitate
simbolica descrie rezultatul si ce inseamna practic pentru persoana.

#### 1.9.4. Etapele si subetapele spiritului

{{etapele_subetapele_spiritului}}

### 1.10. Ajutoare

#### 1.10.1. Semnatura astrala

Redactare obligatorie: se explica mai intai ce este semnatura astrala, apoi se
afiseaza calculul si SVG-ul. Interpretarea citeste traseul ca miscare intre
centre, repetitii si linii dominante. Se evita descrierea tehnica a desenului
fara sens personal.

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

Redactare obligatorie: concluzia capitolului 1 nu repeta toate cifrele, ci
spune ce se vede in ansamblu: dominante, lipsuri, tensiuni, puncte de sprijin si
tema centrala care va fi reluata in capitolele urmatoare.

---
## Capitolul 2. Caracterul

### 2.1. Vibratia interioara

#### 2.1.1. Vibratia interioara pitagoreica

Redactare obligatorie: aceasta sectiune citeste omul "din camera lui
interioara". Se foloseste o imagine de pornire interioara, apoi arhetipul si
felul in care energia se simte in decizii, emotii si reactie spontana.

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

Redactare obligatorie: fixatia se scrie ca talent dominant si risc de atasare.
Se foloseste imaginea unui drum pe care energia il alege instinctiv.

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

Redactare obligatorie: aceasta interpretare trebuie sa fie analogica. Caii
arata forta de pornire, trasura arata suportul practic, vizitiul arata directia.
Se explica ce parte conduce, ce parte ramane in urma si cum se poate echilibra
ansamblul.

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

Redactare obligatorie: concluzia caracterului aduna 3-5 idei, nu reia toate
tabelele. Se scrie ca portret interior: resurse, sensibilitati, riscuri si
cheia prin care caracterul devine matur.

{{concluziile_caracterului}}

---
## Capitolul 3. Transformarea

Regula capitolului: fiecare subcapitol raspunde la intrebarea "ce se transforma
si prin ce presiune?". Se evita repetarea definitiilor din capitolul 1. Aici se
scrie mai aplicat: ce se cere schimbat, unde apare tensiunea, ce punte trebuie
construita si ce comportament nou se poate forma.

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

Redactare obligatorie: concluzia transformarii trebuie sa arate miscarea mare:
de unde pleaca persoana, ce se tensioneaza, ce se maturizeaza si ce fel de om
incepe sa devina cand foloseste constient energia.

{{concluziile_transformarii}}

---
## Capitolul 4. Destinul

Regula capitolului: destinul se scrie ca directie de realizare, nu ca verdict.
Fiecare sectiune leaga cifra de un arhetip si de un drum concret. Se explica
mereu dialogul dintre destin, nume, caracter si perioadele vietii.

Pentru Capitolul 4 se foloseste stilul amplu al lucrarii Daniel v1.04r. Fiecare
sectiune majora trebuie sa creeze o imagine din cuvinte: cititorul trebuie sa
vada drumul, casa, atelierul, podul, biblioteca, scena sau instrumentul prin
care se exprima cifra. Nu se lasa paragrafe de doua-trei randuri daca sectiunea
vorbeste despre destin, calea destinului, punti sau solutia aspectelor de
indreptat.

### 4.1. Vibratia Destinului

Redactare obligatorie: include definitia destinului, calculul, arhetipurile
cifrei destinului, imaginea centrala, manifestarea concreta, umbra si cheia de
maturizare. Se mentioneaza explicit cum se leaga calea destinului de cifra
redusa.

{{destin_vibratia_destinului}}

### 4.2. Pinaclul 3

{{destin_pinaclul_3}}

### 4.3. Solutia aspectelor de indreptat

Redactare obligatorie: solutia se formuleaza ca raspuns viu la aspectul de
indreptat, nu ca simpla reducere numerologica. Se folosesc analogii si exemple
practice. Textul trebuie sa arate ce invata persoana sa faca altfel atunci cand
trece de la tensiune la echilibru.

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

Redactare obligatorie: concluzia destinului trebuie sa contina imaginea centrala
a drumului persoanei. Structura recomandata: destinul cere..., numele adauga...,
caracterul sustine/provoaca..., maturizarea apare cand...

{{concluziile_destinului}}

---
## Capitolul 5. Parcursul vietii

Regula capitolului: parcursul vietii se scrie ca harta de etape. Nu se afirma
ca un eveniment este obligatoriu. Se arata tema perioadei, felul in care se
poate manifesta, riscul si atitudinea potrivita.

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

Redactare obligatorie: concluzia parcursului vietii leaga perioadele intre ele
si arata ce se repeta, ce se intensifica si unde apar trecerile importante.

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

Redactare obligatorie: concluziile pentru numerologi pot fi mai sintetice, dar
trebuie sa pastreze firul interpretativ. Se grupeaza rezultatele pe directii:
interior, exterior, destin, nume, matrice, cicluri si ajutoare.

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

Redactare obligatorie: sfatul numerologului se scrie direct catre persoana,
cald si practic. Nu introduce calcule noi. Traduce rezultatele in pasi mici,
intrebari de lucru si recomandari de atitudine.

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

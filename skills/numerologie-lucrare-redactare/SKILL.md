---
name: numerologie-lucrare-redactare
description: Elaboreaza, adapteaza si verifica lucrari numerologice complete in Markdown si HTML, ruland calculatorul Python inclus pentru date personale si relationale si aplicand template-uri, interpretari ample si formatare consecventa. Foloseste cand se cere o lucrare numerologica noua, completarea sau revizia unei lucrari existente, alegerea unui tip de lucrare ori template, sincronizarea MD-HTML sau redactarea de interpretari pentru caracter, destin, relatii, cariera, iubire, bani, faima si intervale de ani.
---

# Redactarea lucrarilor numerologice

## Flux obligatoriu

1. Colecteaza datele prin [[skills/numerologie-lucrare-redactare/references/formular-date|Formularul de intrare]].
2. Alege template-ul cerut. Pentru `examen`, foloseste `assets/Template-lucrare-examen.md`; pentru `scurt`, foloseste `assets/Template-lucrare-scurta.md` si perechea HTML indicata de acesta.
3. Citeste [[skills/numerologie-lucrare-redactare/references/reguli-redactare|Reguli de redactare]] inainte de redactare sau revizie.
4. Ruleaza `scripts/calculator_numerologic_examen.py` si salveaza sau pastreaza iesirea JSON ca sursa a tuturor valorilor de calcul. Pentru matricea datei de nastere, `N2` este suma cifrelor lui `N1`, iar `N4` este suma cifrelor lui `N3`; fiecare insumare se executa exact o singura data. Pentru Daniel: `N1 = 39 -> N2 = 12` si `N3 = 37 -> N4 = 10`; nu continua cu `1 + 2 = 3` sau `1 + 0 = 1`.
5. Pentru o relatie, ruleaza calculatorul separat si pentru a doua persoana, apoi foloseste cele doua rezultate in analiza relationala.
6. Redacteaza mai intai continutul complet, apoi sincronizeaza varianta Markdown cu HTML-ul canonic.
7. Solicita agentului The Cartographer graficele necesare; acesta foloseste skill-urile SVG dedicate si valorile returnate de calculator. The Scribe integreaza numai livrabilele validate.
8. Valideaza numele, datele, relatiile, intervalele de ani, imaginile si consistenta MD-HTML.

## Rularea calculatorului

Foloseste Python 3.12 si ruleaza scriptul din directorul skill-ului:

```powershell
python scripts/calculator_numerologic_examen.py `
  --data-nasterii "12.01.1998" `
  --nume-complet "Roman Andreea Maria" `
  --nume-familie "Roman" `
  --prenume "Andreea Maria" `
  --prenume-activ "Andreea" `
  --gen "feminin" `
  --an-start 1998 `
  --an-final 2106 `
  --pretty
```

- Tradu `M` in `masculin` si `F` in `feminin` pentru argumentul `--gen`.
- Pentru intervalul `complet (0-108 ani)`, foloseste anul nasterii la `--an-start` si anul nasterii + 108 la `--an-final`.
- Pentru intervalul specific, transforma varstele in ani calendaristici inainte de rulare.
- Daca exista nume anterior, transmite-l prin `--nume-anterior`.
- Nu recalcula manual valorile returnate de script si nu consulta documentatia numerologica pentru a inlocui rezultatele scriptului.
- Nu inventa valori pentru campurile marcate de script cu `status: de_completat` sau `status: partial`; semnaleaza-le ca limite ale calculatorului.

## Selectarea template-ului

- Consulta [[skills/numerologie-lucrare-redactare/references/harta-template-uri-lucrari|Harta template-urilor pentru lucrari numerologice]] inainte de alegerea structurii.
- Solicita alegerea explicita a unuia dintre tipurile disponibile: `scurt` sau `examen`. Nu deduce tipul doar din nivelul de detaliere.
- `examen`: foloseste template-ul inclus si toate capitolele cerute de acesta.
- `scurt`: foloseste ca resursa principala `assets/Template-lucrare-scurta.md`; pastreaza continutul sincronizat cu perechea canonica `assets/templates/Template_Lucrare_Numerologica_Scurt.md` si `assets/templates/Template_Lucrare_Numerologica_Scurt.html`.
- Pentru un tip viitor, foloseste fisierul dedicat numai daca este inregistrat in harta template-urilor; altfel cere confirmare inainte de a inventa o structura.
- Pastreaza fiecare template intr-o pereche distincta Markdown-HTML si mentine copiile din `templates/` si `assets/templates/` identice.

### Contractul template-ului `scurt`

- Dupa `Cuprins`, incepe direct cu `Capitolul 1. Vibratia interioara`. Nu include capitolul `Cuvant inainte`, text introductiv echivalent, index asociat sau trimitere in Cuprins.
- Pastreaza ordinea capitolelor din template: Vibratia interioara, Vibratia exterioara, Destinul, Matrita numerologica, Numele, Oportunitati si provocari, Soarta si Destinul, Lectiile de viata, Relatii conditionale si Concluzii.
- In Matrita numerologica, reda patratul 3x3 in ordinea `1-4-7 / 2-5-8 / 3-6-9`, cu repetitii, reper optim, culori si simboluri dupa modelul `BDR-19980219-v1.07r-G-001`.
- Reda ca tabele editabile cele doua coduri ale numelui, anii interiori, anii exteriori, ciclul de 7 ani, ciclul de 9 ani si lectiile de viata; nu folosi capturi raster pentru aceste tabele.
- Pentru orice arcana numita, selecteaza imaginea corespunzatoare din `vault/tarot/imagini`, foloseste embed Obsidian in Markdown si data URI in HTML autonom.
- Daca exista date relationale, insereaza capitolul `Relatii` intre `Lectiile de viata` si `Concluzii`, genereaza Omuletul relatiilor prin The Cartographer si interpreteaza contributiile, elementele, rezultatul comun, tema de rezolvat si zonele absente. Daca nu exista relatie, elimina integral capitolul si intrarea din Cuprins si pastreaza Concluziile drept Capitolul 9.

## Reguli de continut

- Nu inventa date personale, relationale sau biografice.
- Nu transforma numerologia intr-un verdict. Foloseste limbaj simbolic, nu afirmatii absolute.
- Personalizeaza interpretarea prin legaturi intre rezultate, exemple concrete, analogii si imagini din cuvinte.
- Pentru template-urile care cer explicit introducerea, include capitolul `Cuvant inainte` imediat dupa Cuprins si foloseste ca sursa reutilizabila `vault/Numerologie/Introducere.md`. Aceasta regula nu se aplica template-ului `scurt`, care omite integral capitolul si intrarea lui din Cuprins.
- In livrabilul Markdown, scrie toate trimiterile din Cuprins catre capitole si subcapitole ca wikilinkuri Obsidian, in forma `[[#Titlul exact al sectiunii|Eticheta din Cuprins]]`. Tinta trebuie sa reproduca exact heading-ul, inclusiv diacriticele si punctuatia; nu folosi forma Markdown `[Eticheta](#ancora)`. In livrabilul HTML, reda aceleasi trimiteri prin ancore HTML normale, `<a href="#id-sectiune">Eticheta</a>`; nu copia wikilinkurile Obsidian in HTML.
- Incepe direct cu sensul conceptului sau cu interpretarea. Evita formularile metatextuale de tipul `[Prenume], aici ne uitam la...`, `aici vedem...` sau `in aceasta sectiune analizam...`.
- Foloseste arhetipuri numai in interpretarile Vibratiei interioare, Vibratiei exterioare si Vibratiei globale.
- Pentru cele trei vibratii permise, urmeaza: definitie -> metoda -> calcul -> interpretarea conversationala a traseului de reducere, numai daca exista o reducere suplimentara -> rezultat -> imagine -> arhetip -> manifestare concreta -> umbra -> maturizare.
- Pentru vibratiile fundamentale, interpreteaza traseul numai cand calculul are una sau mai multe trepte reale de reducere. Explica direct persoanei sensul cifrelor de intrare, suma intermediara, cifrele reducerii si felul in care aceste straturi se regasesc in rezultatul final. Daca valoarea este deja o singura cifra, prezinta direct interpretarea ei, fara sa mentionezi ca nu exista traseu. Daca apare 0, explica prudent ca nu adauga o directie numerica separata, dar poate deschide sau amplifica potentialul cifrei alaturate.
- Pastreaza volumul amplu fara sa repeti sensul traseului in paragrafele urmatoare. Dupa traseu, pune accentul pe rezultatul final; fiecare paragraf ulterior trebuie sa aduca o functie distincta: manifestare observabila, exemplu practic, rutina aplicabila, umbra sau criteriu de maturizare. Daca un paragraf doar reformuleaza traseul ori rezultatul, rescrie-l ca aplicatie concreta.
- La Vibratia globala, interpreteaza intotdeauna dialogul dintre Vibratia interioara si Vibratia exterioara. Numeste acest calcul traseu de reducere si desface suma intermediara numai daca rezultatul adunarii depaseste 9; de exemplu, `9 + 9 = 18 -> 1 + 8 = 9`.
- La Vibratia exterioara, eticheteaza calculul cu `Luna din data de nastere`. Daca luna este deja o singura cifra (`1-9`), afiseaza direct rezultatul cu bold, fara sageata, fara o reducere artificiala si fara sa mentionezi ca nu exista traseu de reducere. Pentru lunile `10-12`, afiseaza si interpreteaza traseul real de reducere.
- La Vibratia interioara, eticheteaza calculul cu `Ziua din data de nastere`. Afiseaza cu bold ziua de plecare, fiecare rezultat intermediar si rezultatul final; pastreaza toate treptele reale ale traseului de reducere. Daca ziua este deja o singura cifra (`1-9`), afiseaza direct cifra cu bold, fara sageata si fara reducere artificiala.
- La Destin, eticheteaza calculul cu `Toate cifrele adunate din data de nastere`. Afiseaza suma initiala, fiecare rezultat intermediar si rezultatul final cu bold, fara sa omiti treptele reale ale reducerii.
- In template-ul scurt, pastreaza separat caracterul social al Vibratiei exterioare de dialogul interior-exterior: subcapitolul `Caracterul social` descrie numai cifra exterioara, iar subcapitolul `Interior si exterior` formuleaza conversational cum este persoana in interior si cum este perceputa la exterior (de exemplu: `daca in interior esti **1**, la exterior oamenii te pot percepe ca pe un **2**`).
- Nu aplica obligatoriu interpretarea traseului de reducere la Calea Destinului, Destin sau Aspectele de indreptat. Puntile interior-exterior si interior-destin se interpreteaza prin valorile initiale si rezultat, conform structurii existente. La Solutia aspectelor de indreptat, insumeaza cifrele Aspectelor exact o singura data si pastreaza rezultatul compus (`37 -> 10`, nu `1`); este recomandata interpretarea rezultatului, nu desfacerea ampla a traseului.
- Pentru toate celelalte sectiuni, urmeaza: definitie -> metoda -> calcul -> rezultat -> imagine -> manifestare concreta -> umbra -> maturizare, fara arhetipuri sau roluri arhetipale mascate.
- In matricea numerologica, pentru ambele template-uri `scurt` si `examen`, alege simbolul dupa numarul de aparitii: o cifra = cerc; exact doua cifre = doua cercuri unite printr-o linie; exact trei cifre = triunghi. In HTML, linia dintre cele doua cercuri trebuie sa se opreasca la conturul vizibil si sa nu intre in cercuri.
- In template-ul `scurt`, dupa figura matricei nu crea subcapitolul sau tabelul `Casutele matricei`. Redacteaza direct noua paragrafe indexate, cate unul pentru fiecare casuta, cu inceputul ingrosat `Casuta 1` pana la `Casuta 9`. Numeste energia, compara numarul de aparitii cu optimul si formuleaza personalizat: deficitul sau absenta inseamna energie de construit prin aport extern; o singura aparitie peste optim este energie activa peste reper, nu exces; numai diferenta de cel putin `+2` fata de optim inseamna energie in exces si cere echilibru. Repere: `1` psihic si initiativa, `2` sensibilitate emotionala, `3` relatii si exprimare, `4` corp, `5` intuitie si masura, `6` pragmatism, `7` spiritualitate, `8` putere si rol social, `9` mental.
- In interpretarea raportului par-impar, explica faptul ca cifrele pare sustin capacitatea de a primi si de a da mai departe; cand devin foarte numeroase, pot aduce indecizie. Leaga lectura de raportul concret din matrice, fara sa prezinti indecizia ca verdict.
- In template-ul `scurt`, tabelul `T-009` are antetele de rand in prima coloana, aliniate la dreapta pe orizontala si la mijloc pe verticala. Nu foloseste culoare, fundal colorat sau borduri interioare si exterioare; pastreaza numai linii discrete sub primul si al doilea rand. Tabelul `T-010` are doua coloane si un singur rand, fara borduri interioare ori exterioare: imaginea arcanei in prima celula, iar a doua celula este o lista cu puncte pentru Resursa, Manifestare, Umbra si Maturizare, aliniata la mijloc pe verticala.
- In template-ul `scurt`, `T-012` este un grafic cu bare pentru elemente, nu un tabel. Ordinea este Foc, Pamant, Aer, Apa; barele folosesc aceeasi paleta si acelasi contur discret ca figura matricii `G-002` si au latimea raportata la valoarea maxima dintre cele patru elemente. Pe ecrane largi, in dreapta fiecarei bare afiseaza definitia elementului corespunzator ca lista cu bullet-uri vizibile, cu indexul de paragraf `P-044` imediat deasupra definitiilor; indexul `T-012` sta deasupra graficului. Definitiile sunt: Focul este esenta vietii, a duhului si a spiritului care anima si activeaza; Pamantul este esenta materiei dense, a solidaritatii si a fertilitatii, care hraneste si da forma; Aerul este esenta inteligentei conceptuale care elibereaza si stimuleaza; Apa este esenta emotiilor si a fecunditatii, maleabila, flexibila si orientata spre acumulare. Dupa grafic si definitii, plaseaza paragraful indexat separat `P-045`, cu interpretarea temperamentului. Pe mobil, componentele se aseaza pe verticala. Stabileste temperamentul din elementul dominant: Foc = coleric, Aer = sangvin, Apa = flegmatic, Pamant = melancolic; la totaluri apropiate sau egale, formuleaza temperament mixt sau oscilant.
- In sectiunea despre raportul par-impar din template-ul `scurt`, sub indexul paragrafului afiseaza un singur grafic cu bara orizontala impartita in doua segmente: imparele in stanga si parele in dreapta. Latimea fiecarui segment este raportata la totalul cifrelor din matrice; etichetele arata numele si cantitatea, iar deasupra barei se afiseaza totalul. Pastreaza apoi interpretarea conversationala in acelasi bloc indexat.
- In template-ul `scurt`, subcapitolul `SUB-008` are titlul `2.1. Definitie`. In capitolul 4, `4.4` se numeste `Masculin si feminin`, `4.5` este subcapitolul separat `Daruri si nevoi`, iar `Fixatia` devine `4.6`; in revizie foloseste indicii `SUB-016`, `SUB-017` si, pentru Fixatie, `SUB-017a`.
- In subcapitolul `Daruri si nevoi`, se citesc numai casutele matricei cu cel putin doua cifre. Darurile si nevoile provin din aceleasi energii: darul arata resursa disponibila, iar nevoia arata ce trebuie sa primeasca si sa manifeste matur energia respectiva. Casutele cu o singura cifra si cele goale nu intra in aceasta lectura; ele se citesc separat ca potential disponibil sau directie de dezvoltare.
- Fixatia se alege exclusiv dintre vectorii orizontali plini `147`, `258`, `369`, dupa cea mai mare cantitate totala de cifre din vector, nu dupa valoarea numerica a vectorului. Fara vector orizontal plin, nu exista fixatie matriceala clara.
- Tendinta se alege exclusiv dintre diagonalele pline `159` si `357`, dupa cea mai mare cantitate totala de cifre. Fara diagonala plina, nu exista tendinta matriceala clara. In template-ul scurt, o redactezi ca subcapitolul `4.7. Tendinta`, imediat dupa Fixatie.
- In lucrare, omite integral subcapitolul `Fixatia` daca nu exista vector orizontal plin si omite integral subcapitolul `Tendinta` daca nu exista diagonala plina. Nu afisa nici titlul, nici indexul, nici un text care anunta absenta lor.
- Scara bunastarii ramane subcapitol obligatoriu chiar daca Fixatia sau Tendinta lipsesc. In template-ul scurt se aseaza dupa `Daruri si nevoi`, inaintea pozitiilor optionale, si afiseaza un grafic cu bare orizontale pentru cei 8 vectori si cele 9 casute, in ordine descrescatoare dupa valoare.
- In orice varianta de revizie, fiecare tabel are index propriu `T`, asezat imediat deasupra tabelului. Indexul unui paragraf se aseaza imediat deasupra paragrafului, cu spatiu vizual minim; nu reutiliza indexul subcapitolului pentru tabel sau paragraf.
- In template-ul `scurt`, titlul principal contine numai numele complet si data nasterii; versiunea ramane in datele generale, antet si numele fisierului de revizie.
- Pastreaza `Scara bunastarii` ca subcapitol separat al Structurii matriciale, imediat dupa tendinte, fixatie si analogia cai-trasura-vizitiu. Foloseste titlul numerotat `4.6. Scara bunastarii`, ancora proprie si index `SUB` in variantele de revizie.
- La Numarul neamului, afiseaza calculul in intervalul 1-22 si un tabel cu arcana rezultata si interpretare ampla: resursa mostenita, manifestare concreta, umbra si maturizare.
- Oriunde o arcana este numita sau interpretata intr-un tabel ori paragraf, afiseaza si imaginea arcanei in acelasi subcapitol. Daca aceeasi arcana este reluata intr-un alt subcapitol, reutilizeaza imaginea acolo; nu considera suficienta imaginea aparuta anterior in alta sectiune. In variantele de revizie, indexeaza tabelul sau figura care contine imaginea.
- La Codul numerologic personal al numelui, pune fiecare componenta a numelui pe rand separat, apoi numarul de exprimare pe un rand distinct. In chenarul de sinteza, afiseaza exact doua randuri: codul literelor numelui si codul numerologic personal al numelui.
- La Spirit -> Inclinatii profesionale, afiseaza separat calculele DA si NU si un tabel cu arcana fiecarui rezultat. Formuleaza conversational si explicit `Aplicabilitatea profesionala DA este arcana X, Nume`, apoi explica directia cultivabila; pentru negativ foloseste `Aplicabilitatea profesionala NU este arcana Y, Nume` si explica obstacolul si cheia de lucru in pasi concreti.
- Cand folosesti coduri de vectori sau diagonale, scrie imediat si denumirea lor pentru cititor (de exemplu `vectorul 789, Creativitate` si `diagonala 159, Cariera`); nu lasa codul numeric neexplicat si nu obliga cititorul sa revina la o sectiune anterioara.
- Scrie denumirile complete ale vibratiilor. Nu folosi acronime precum `VI`, `VE`, `VG`, `VCV` sau `VCT` in text ori calcule.
- In textul narativ, scrie valorile numerologice cu cifre, nu cu litere, si evidentiaza-le cu bold: `**1**`, `**0**`, `**10**`. Aplica regula tuturor vibratiilor, rezultatelor, etapelor de reducere si cifrelor interpretate; nu transforma anii calendaristici, varstele sau numerotarea structurala in bold.
- In tabelul polaritatilor din template-ul `scurt`, elimina antetul si foloseste exact doua coloane si trei randuri: `Polaritati pozitive`, `Polaritati negative`, `Directii de dezvoltare`. Prima coloana contine eticheta; a doua contine liste cu bullet-uri extrase din `Lumina vibratiei`, `Umbra vibratiei` si `Directii de dezvoltare` ale vibratiei interpretate.
- In tabelul Tarot al vibratiei din template-ul `scurt`, elimina antetul si foloseste doua coloane, pastrand aspectul normal de tabel, cu chenar exterior si linii interioare. Prima coloana contine imaginea arcanei si ocupa prin `rowspan` toate cele patru randuri; a doua contine cate o formulare unica si completa pentru `Resursa`, `Manifestare`, `Umbra` si `Maturizare`, cu eticheta bold urmata de descriere in aceeasi celula. Pastreaza indexul `G` al imaginii in celula imaginii si indexul `T` imediat deasupra tabelului.
- Include datele relationale in `Date generale` atunci cand sunt furnizate, nu doar in capitolul Relatii.
- Imediat dupa titlul capitolului `Relatii` si inainte de primul subcapitol, afiseaza numai datele persoanei cu care este analizata relatia: numele complet, data nasterii si tipul relatiei. Nu adauga interpretare in acest bloc factual.
- Cand interpretezi cifrele sau zonele absente din Omuletul relatiilor, grupeaza indicatiile concrete si scrie cifra corespunzatoare in paranteza dupa fiecare grupa. Explica faptul ca aceste teme se construiesc intentionat in cuplu sau pot primi un aport extern prin contexte, oameni, activitati ori instrumente potrivite; adauga exemple aplicabile pentru fiecare cifra.
- Pastreaza relatia optionala: daca datele persoanei nu precizeaza nicio relatie cu o alta persoana, omite integral capitolul `Relatii`, inclusiv intrarea lui din cuprins; nu afisa sectiuni sau campuri fictive.
- Redacteaza interpretarile temporale Soarta-Destin conversational, ca un dialog direct cu persoana. Adreseaza-te pe prenume, explica pe intelesul ei de ce se foloseste pasul de 10 sau 12 ani, ce spune zona de confort si cum se citesc varstele-cheie. Pastreaza valorile tehnice, dar evita formularile distante de tipul `Pentru [nume] folosim...`.
- Pentru tabelul HTML al Ciclului de 7 ani, micsoreaza numai fontul si spatierea antetului, pastreaza fontul corpului neschimbat si permite tabelului sa se adapteze la latimea documentului, fara bara orizontala pe afisarea desktop obisnuita.

## Reguli pentru calcule

- Explica metoda intr-un paragraf inaintea chenarului.
- Pastreaza in chenar doar traseul numeric, etichete scurte indispensabile si rezultatul.
- Leaga pasii cu ` -> `.
- Marcheaza rezultatul final complet cu `<strong>...</strong>` in HTML.
- Nu introduce explicatii, propozitii sau acronime in chenar.
- Cand exista doua rezultate finale, pune-le pe randuri separate si marcheaza fiecare rezultat complet.

## Livrabile

- Livreaza perechea `.md` si `.html` cu acelasi continut semantic.
- Cand utilizatorul valideaza o revizie ca finala, pastreaza numarul versiunii si schimba numai sufixul de stare: `v1.07r` -> `v1.07f`. Genereaza finala din perechea reviziei validate; nu porni de la o finala mai veche si nu creste versiunea doar pentru schimbarea starii.
- Foloseste structura HTML canonica indicata de template, nu o conversie Markdown simplificata.
- Inventariaza graficele inainte de integrare si nu pastra formate duplicate fara rol. Sterge copia nereferentiata numai dupa ce verifici ca nu este sursa canonica unica sau intrare necesara pentru regenerare.
- Pentru SVG vectorial pur, foloseste referinta relativa in Markdown si `data:image/svg+xml;base64,...` intr-un element `<img>` din HTML-ul autonom. Pentru SVG care contine `<image>` sau orice resursa raster, foloseste PNG-ul validat in Markdown si incorporeaza acelasi PNG in HTML ca `data:image/png;base64,...`; pastreaza SVG-ul numai daca are un rol tehnic explicit.
- Pastreaza resursele grafice folosite langa lucrare si referintele Markdown valide. HTML-ul final nu trebuie sa contina surse relative pentru imagini.
- In directorul persoanei, nu sterge versiuni sau resurse decat la cererea explicita a utilizatorului.
- Nu face commit sau push daca utilizatorul a rezervat aceste operatii pentru lucru manual.

## Control final

Verifica obligatoriu:

- identitatea, prenumele activ, data si genul;
- numele anterior, daca exista;
- datele relatiei in Date generale si in capitolul Relatii;
- toate calculele si reducerile fata de iesirea JSON a calculatorului;
- absenta acronimelor de vibratii;
- prezenta arhetipurilor numai la Vibratia interioara, Vibratia exterioara si Vibratia globala;
- rezultatele complete marcate in chenare;
- intervalul de ani cerut;
- consistenta intre Markdown, HTML, tabele si grafice;
- un singur livrabil grafic activ pentru fiecare figura, fara copii redundante nereferentiate;
- SVG-urile vectoriale sunt incorporate ca data URI in HTML, SVG-urile cu continut raster sunt livrate vizual ca PNG, iar HTML-ul nu contine surse relative pentru imagini;
- pentru template-ul `scurt`, absenta completa a capitolului `Cuvant inainte`, a indexurilor lui si a trimiterii din Cuprins; pentru template-urile care il cer explicit, prezenta lui dupa Cuprins si inainte de Capitolul 1;
- fiecare wikilink din Cuprinsul Markdown indica exact un heading existent, nu au ramas trimiteri interne de forma `[Eticheta](#ancora)`, iar Cuprinsul HTML foloseste ancore `<a href="#...">` valide;
- absenta formularilor metatextuale care anunta ce se analizeaza;
- lipsa textelor generice ramase din template.

Pentru lucrarile construite dupa modelul final Daniel, aplica si [[skills/numerologie-lucrare-redactare/references/lista-control-model-final-daniel|Lista de control pentru modelul final Daniel]].

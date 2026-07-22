---
name: numerologie-lucrare-redactare
description: Elaboreaza, adapteaza si verifica lucrari numerologice complete in Markdown si HTML, ruland calculatorul Python inclus pentru date personale si relationale si aplicand template-uri, interpretari ample si formatare consecventa. Foloseste cand se cere o lucrare numerologica noua, completarea sau revizia unei lucrari existente, alegerea unui tip de lucrare ori template, sincronizarea MD-HTML sau redactarea de interpretari pentru caracter, destin, relatii, cariera, iubire, bani, faima si intervale de ani.
---

# Redactarea lucrarilor numerologice

## Flux obligatoriu

1. Colecteaza datele prin [[skills/numerologie-lucrare-redactare/references/formular-date|Formularul de intrare]].
2. Alege template-ul cerut. Pentru `examen`, foloseste `assets/Template-lucrare-examen.md`; pentru `scurt`, foloseste `assets/Template-lucrare-scurta.md` si perechea HTML indicata de acesta.
3. Citeste [[skills/numerologie-lucrare-redactare/references/reguli-redactare|Reguli de redactare]] inainte de redactare sau revizie. Pentru o cerere despre perioade favorabile pentru bani, cariera, casatorie sau alte decizii temporale, citeste si [[skills/numerologie-lucrare-redactare/references/analiza-ferestrelor-temporale|Analiza ferestrelor temporale]].
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

- Redacteaza integral template-ul `scurt` in ton conversational, de la primul capitol pana la concluzii. Adreseaza-te direct persoanei, foloseste prenumele activ si mentine persoana a doua singular in definitii, explicatii, interpretari, introduceri de tabele si grafice, cicluri si recomandari. Nu alterna cu ton formal, impersonal sau persoana a treia; sunt exceptate numai datele factuale, etichetele, titlurile si calculele.
- Dupa `Cuprins`, incepe direct cu `Capitolul 1. Vibratia interioara`. Nu include capitolul `Cuvant inainte`, text introductiv echivalent, index asociat sau trimitere in Cuprins.
- Pastreaza ordinea capitolelor din template: Vibratia interioara, Vibratia exterioara, Destinul, Matrita numerologica, Numele, Pinacluri: Oportunitati si provocari, Ciclicitati, Relatii conditionale si Concluzii. In `Capitolul 7. Ciclicitati`, pastreaza strict subordinea: Soarta si Destinul, Anii importanti, Lectiile de viata, Ciclul de 7 ani, Ciclul de 9 ani, Ciclul de 12 ani.
- In Matrita numerologica, reda patratul 3x3 in ordinea `1-4-7 / 2-5-8 / 3-6-9`, cu repetitii, reper optim, culori si simboluri dupa modelul `BDR-19980219-v1.07r-G-001`.
- Reda ca tabele editabile cele doua coduri ale numelui, lectiile de viata si ciclurile de 7, 9 si 12 ani; nu folosi capturi raster pentru aceste tabele. Anii importanti interiori si exteriori se prezinta separat: definitia fiecarui tip intr-un paragraf indexat, urmata de sirul complet al anilor calculati intr-un al doilea paragraf indexat, fara tabel.
- Pentru orice arcana numita, selecteaza imaginea corespunzatoare din `vault/tarot/imagini`, foloseste embed Obsidian in Markdown si data URI in HTML autonom.
- Daca exista date relationale, insereaza `Capitolul 8. Relatii`, apoi `Capitolul 9. Aplicabilitate profesionala`, intre `Ciclicitati` si `Concluzii`. Genereaza Omuletul relatiilor prin The Cartographer si interpreteaza contributiile, elementele, rezultatul comun, tema de rezolvat si zonele absente. Capitolul de aplicabilitate contine descrierea, calculul DA/NU intr-un singur chenar si tabelul `T-016` cu imaginile arcanelor si interpretarile in celulele corespunzatoare, sub fiecare imagine. Daca nu exista relatie, elimina integral relatia si aplicabilitatea si renumeroteaza Concluziile drept Capitolul 8.

## Reguli de continut

- Nu inventa date personale, relationale sau biografice.
- Nu transforma numerologia intr-un verdict. Foloseste limbaj simbolic, nu afirmatii absolute.
- Personalizeaza interpretarea prin legaturi intre rezultate, exemple concrete, analogii si imagini din cuvinte.
- Pentru template-urile care cer explicit introducerea, include capitolul `Cuvant inainte` imediat dupa Cuprins si foloseste ca sursa reutilizabila `vault/Numerologie/Introducere.md`. Aceasta regula nu se aplica template-ului `scurt`, care omite integral capitolul si intrarea lui din Cuprins.
- In livrabilele Markdown nu pastra wikilinkuri Obsidian in Cuprins sau in textul lucrarii; foloseste etichete text simple. In HTML, foloseste ancore HTML pentru Cuprins si incorporeaza toate SVG-urile si imaginile ca data URI; nu livra referinte externe sau cai relative pentru resurse vizuale.
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
- In acelasi subcapitol `Interior si exterior`, dupa dialogul dintre cele doua vibratii, include obligatoriu trei elemente indexate separat: definitia puntii interior-exterior, calculul in chenar si interpretarea rezultatului. Calculeaza puntea ca valoare absoluta `|Vibratia interioara - Vibratia exterioara|`. Interpreteaza rezultatul ca ajustare dintre nucleul interior si imaginea vizibila; leaga maturizarea puntii de autenticitate, coerenta dintre intentie si actiune si felul in care persoana poate fi acceptata fara ezitare in rolul pe care si-l asuma.
- Nu aplica obligatoriu interpretarea traseului de reducere la Calea Destinului, Destin sau Aspectele de indreptat. Puntile interior-exterior si interior-destin se interpreteaza prin valorile initiale si rezultat, conform structurii existente. La Solutia aspectelor de indreptat, insumeaza cifrele Aspectelor exact o singura data si pastreaza rezultatul compus (`37 -> 10`, nu `1`); este recomandata interpretarea rezultatului, nu desfacerea ampla a traseului.
- Pentru toate celelalte sectiuni, urmeaza: definitie -> metoda -> calcul -> rezultat -> imagine -> manifestare concreta -> umbra -> maturizare, fara arhetipuri sau roluri arhetipale mascate.
- In matricea numerologica, pentru ambele template-uri `scurt` si `examen`, alege simbolul dupa numarul de aparitii: o cifra = cerc; exact doua cifre = doua cercuri unite printr-o linie; exact trei cifre = triunghi. In HTML, linia dintre cele doua cercuri trebuie sa se opreasca la conturul vizibil si sa nu intre in cercuri.
- In template-ul `scurt`, centreaza orizontal atat matricea datei `G-002`, cat si matricea comparativa a numelui `G-002a`. Fiecare casuta foloseste acelasi contur auriu, raza de `5px` si umbra discreta ca figura Soarta-Destin `G-005`; aplica stilul fiecarei celule, nu numai grilei exterioare.
- In template-ul `scurt`, dupa figura matricei nu crea subcapitolul sau tabelul `Casutele matricei`. Redacteaza direct noua paragrafe indexate, cate unul pentru fiecare casuta, cu inceputul ingrosat `Casuta 1` pana la `Casuta 9`. Numeste energia, compara numarul de aparitii cu optimul si formuleaza personalizat: deficitul sau absenta inseamna energie de construit prin aport extern; o singura aparitie peste optim este energie activa peste reper, nu exces; numai diferenta de cel putin `+2` fata de optim inseamna energie in exces si cere echilibru. Repere: `1` psihic si initiativa, `2` sensibilitate emotionala, `3` relatii si exprimare, `4` corp, `5` intuitie si masura, `6` pragmatism, `7` spiritualitate, `8` putere si rol social, `9` mental.
- In introducerea Matricei datei de nastere, prezinta cele noua sfere de inteligenta ca lista cu bullet-uri, nu ca fraza compacta: `1` psihica, `2` emotionala, `3` prelucrarea informatiilor, `4` corporala, `5` intuitiva, `6` pragmatism, `7` spirituala, `8` putere si sociala, `9` mentala. Pastreaza lista sub acelasi index de paragraf ca introducerea, inaintea calculului matricei.
- In interpretarea raportului par-impar, explica faptul ca cifrele pare sustin capacitatea de a primi si de a da mai departe; cand devin foarte numeroase, pot aduce indecizie. Leaga lectura de raportul concret din matrice, fara sa prezinti indecizia ca verdict.
- In template-ul `scurt`, tabelul `T-009` are antetele de rand in prima coloana, aliniate la dreapta pe orizontala si la mijloc pe verticala. Nu foloseste culoare, fundal colorat sau borduri interioare si exterioare; pastreaza numai linii discrete sub primul si al doilea rand. Tabelul `T-010` are doua coloane si un singur rand, fara borduri interioare ori exterioare: imaginea arcanei in prima celula, iar a doua celula este o lista cu puncte pentru Resursa, Manifestare, Umbra si Maturizare, aliniata la mijloc pe verticala. Centreaza legenda cu numarul si numele arcanei direct sub imagine, pe aceeasi axa verticala cu aceasta; aplica regula si tabelelor Tarot echivalente, inclusiv `T-013`.
- In template-ul `scurt`, `T-012` este un grafic cu bare pentru elemente, nu un tabel. Ordinea este Foc, Pamant, Aer, Apa; barele folosesc aceeasi paleta si acelasi contur discret ca figura matricii `G-002` si au latimea raportata la valoarea maxima dintre cele patru elemente. Pe ecrane largi, in dreapta fiecarei bare afiseaza definitia elementului corespunzator ca lista cu bullet-uri vizibile, cu indexul de paragraf `P-044` imediat deasupra definitiilor; indexul `T-012` sta deasupra graficului. Definitiile sunt: Focul este esenta vietii, a duhului si a spiritului care anima si activeaza; Pamantul este esenta materiei dense, a solidaritatii si a fertilitatii, care hraneste si da forma; Aerul este esenta inteligentei conceptuale care elibereaza si stimuleaza; Apa este esenta emotiilor si a fecunditatii, maleabila, flexibila si orientata spre acumulare. Dupa grafic si definitii, plaseaza paragraful indexat separat `P-045`, cu interpretarea temperamentului. Pe mobil, componentele se aseaza pe verticala. Stabileste temperamentul din elementul dominant: Foc = coleric, Aer = sangvin, Apa = flegmatic, Pamant = melancolic; la totaluri apropiate sau egale, formuleaza temperament mixt sau oscilant.
- Incadreaza atat blocul `T-012`, cat si graficul par-impar de sub `P-017` intr-un panou vizual identic cu `G-004`: fundal crem deschis, contur auriu discret, raza de `5px` si umbra usoara. Graficul par-impar ocupa intreaga latime utila a paginii (`width: 100%`, fara limita `max-width`).
- In sectiunea despre raportul par-impar din template-ul `scurt`, sub indexul paragrafului afiseaza un singur grafic cu bara orizontala impartita in doua segmente: imparele in stanga si parele in dreapta. Latimea fiecarui segment este raportata la totalul cifrelor din matrice; etichetele arata numele si cantitatea, iar deasupra barei se afiseaza totalul. Pastreaza apoi interpretarea conversationala in acelasi bloc indexat.
- In template-ul `scurt`, subcapitolul `SUB-008` are titlul `2.1. Definitie`. In capitolul 4, `4.4` se numeste `Masculin si feminin`, `4.5` este subcapitolul separat `Daruri si nevoi`, iar `Fixatia` devine `4.6`; in revizie foloseste indicii `SUB-016`, `SUB-017` si, pentru Fixatie, `SUB-017a`.
- In subcapitolul `Daruri si nevoi`, se citesc numai casutele matricei cu cel putin doua cifre. Darurile si nevoile provin din aceleasi energii: darul arata resursa disponibila, iar nevoia arata ce trebuie sa primeasca si sa manifeste matur energia respectiva. Casutele cu o singura cifra si cele goale nu intra in aceasta lectura; ele se citesc separat ca potential disponibil sau directie de dezvoltare.
- Fixatia se alege exclusiv dintre vectorii orizontali plini `147`, `258`, `369`, dupa cea mai mare cantitate totala de cifre din vector, nu dupa valoarea numerica a vectorului. Fara vector orizontal plin, nu exista fixatie matriceala clara.
- Tendinta se alege exclusiv dintre diagonalele pline `159` si `357`, dupa cea mai mare cantitate totala de cifre. Fara diagonala plina, nu exista tendinta matriceala clara. In template-ul scurt, o redactezi ca subcapitolul `4.7. Tendinta`, imediat dupa Fixatie.
- In lucrare, omite integral subcapitolul `Fixatia` daca nu exista vector orizontal plin si omite integral subcapitolul `Tendinta` daca nu exista diagonala plina. Nu afisa nici titlul, nici indexul, nici un text care anunta absenta lor.
- Scara bunastarii ramane subcapitol obligatoriu chiar daca Fixatia sau Tendinta lipsesc. In template-ul scurt se aseaza dupa `Daruri si nevoi`, inaintea pozitiilor optionale, si afiseaza un grafic cu bare orizontale pentru cei 8 vectori si cele 9 casute, in ordine descrescatoare dupa valoare.
- In HTML-ul template-ului `scurt`, Scara bunastarii foloseste fundalul crem deschis al paginii grafice si acelasi contur auriu, raza de `5px` si umbra discreta ca figura Soarta-Destin. Nu lasa graficul fara delimitare vizuala fata de continutul din jur.
- In orice varianta de revizie, fiecare paragraf sau bloc narativ independent are index `P` unic, iar fiecare tabel are index propriu `T`. Aseaza indexul imediat deasupra elementului, cu spatiu vizual minim; nu reutiliza indexul subcapitolului pentru tabel sau paragraf si nu lasa paragrafe ori tabele fara index. Elimina indexurile numai la trecerea explicita in versiune finala.
- In orice varianta de revizie, fiecare figura sau grafic are un index `G` unic, asezat imediat deasupra elementului vizual; nu reutiliza acelasi index pentru doua grafice diferite.
- In template-ul `scurt`, titlul principal contine numai numele complet si data nasterii; versiunea ramane in datele generale, antet si numele fisierului de revizie.
- In Capitolul 5 al template-ului `scurt`, foloseste ordinea validata: `5.1 Numarul activ`, `5.2 Numarul intim`, `5.3 Numarul ereditar`, `5.4 Numarul ereditar karmic`, `5.5 Numarul de realizare`, `5.6 Numarul de exprimare`, `5.7 Codul numerologic al numelui`. Pentru fiecare dintre primele sase concepte pastreaza definitia, calculul indexat in chenar si interpretarea conversationala; nu omite Numarul intim si nu muta Codul numelui inaintea Numarului de exprimare.
- Pastreaza `Scara bunastarii` ca subcapitol separat al Structurii matriciale, imediat dupa tendinte, fixatie si analogia cai-trasura-vizitiu. Foloseste titlul numerotat `4.6. Scara bunastarii`, ancora proprie si index `SUB` in variantele de revizie.
- La `Numarul ereditar karmic` — nu `Numarul neamului` — afiseaza calculul in intervalul 1-22 si un tabel cu arcana rezultata si interpretare ampla: resursa mostenita, manifestare concreta, umbra si maturizare.
- Oriunde o arcana este numita sau interpretata intr-un tabel ori paragraf, afiseaza si imaginea arcanei in acelasi subcapitol. Daca aceeasi arcana este reluata intr-un alt subcapitol, reutilizeaza imaginea acolo; nu considera suficienta imaginea aparuta anterior in alta sectiune. In variantele de revizie, indexeaza tabelul sau figura care contine imaginea.
- La Codul numerologic personal al numelui, pune fiecare componenta a numelui pe rand separat, apoi numarul de exprimare pe un rand distinct. In chenarul de sinteza, afiseaza exact doua randuri: codul literelor numelui si codul numerologic personal al numelui.
- In subcapitolul `Codul numerologic al numelui` din template-ul `scurt`, nu folosi vechile tabele `T-001` sau `T-002` cu categoriile Mentale, Fizice, Emotionale si Intuitive. Foloseste un calcul `C` cu fiecare componenta a numelui pe rand, apoi matricea comparativa `G-002a` si paragrafe indexate despre energiile comune si energiile prezente numai in nume.
- La Aplicabilitate profesionala, afiseaza separat calculele DA si NU in acelasi chenar si un tabel cu coloane egale pentru fiecare rezultat. Pune imaginea arcanei pe primul rand, iar interpretarea conversationala, cu index propriu, pe randul imediat urmator si in coloana corespunzatoare. Nu repeta formula sau rezultatul la inceputul interpretarii; intra direct in sensul arcanei si in aplicarea profesionala.
- In interpretarea DA, acopera resursa profesionala, comportamentul observabil, domeniile sau contextele favorizate si conditia de maturizare prin care potentialul devine rezultat. In interpretarea NU, explica blocajul fara sa-l confunzi cu lipsa talentului, numeste tiparele care pot frana actiunea si incheie cu o cheie practica de lucru. Pentru Carul, pune accent pe ambitie, initiativa, autonomie, leadership, strategie si autocontrol; pentru Steaua ca obstacol, pune accent pe idealizare, perfectionism, validare, amanarea actiunii si transformarea inspiratiei in disciplina si perseverenta.
- Pentru T-015, foloseste in HTML un tabel cu primele trei coloane inguste si coloana `Citire` larga (reper 10% / 20% / 12% / 58%). Pentru T-016, pastreaza cele doua coloane la 50% / 50%.
- In `T-015`, identifica ciclul de 12 ani care contine data curenta si marcheaza intregul rand cu rosu si bold, atat in Markdown, cat si in HTML. In HTML foloseste clasa `active-cycle`; nu marca un ciclu doar pentru ca este ultimul rand calculat.
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
- Cand utilizatorul cere `cand` este favorabil pentru bani, cariera, casatorie sau alta tema, nu decide dintr-o singura cifra. Suprapune ciclul de 9 ani, vibratia anuala folosita de metoda, ciclul de 12 ani, ciclul de 7 ani si pragurile lui, lectiile de viata, pinaclurile cu oportunitati si provocari, seriile Soarta-Destin si zona de confort, plus anii importanti interiori si exteriori. Foloseste intervalul aniversare-la-aniversare, compara ferestrele intr-un tabel si prezinta concluzia ca fereastra simbolica favorabila, nu predictie fixa. Aplica procedura completa din referinta `Analiza ferestrelor temporale`.
- In template-ul `scurt`, numeste Capitolul 6 `Pinacluri: Oportunitati si provocari`. Prima coloana a tabelului se numeste `Pinaclu`, iar randurile sunt `Pinaclul 1` pana la `Pinaclul 4`, nu etape. Dupa tabel, fiecare descriere incepe explicit cu `Pinaclul N: intervalul de varsta`, folosind intervalul exact returnat de calculator; nu modifica manual limitele si nu crea suprapuneri intre pinacluri.
- Pentru tabelul HTML al Ciclului de 7 ani, micsoreaza numai fontul si spatierea antetului, pastreaza fontul corpului neschimbat si permite tabelului sa se adapteze la latimea documentului, fara bara orizontala pe afisarea desktop obisnuita.

## Reguli pentru calcule

- Pentru Karma din ziua de nastere, foloseste `arcana = 0` cand ziua este `22`, altfel `arcana = ((zi - 1) % 22) + 1`. Stabileste procentul din ziua calendaristica: `1-9 -> spre 100%`, `10-19 -> spre 80%`, `20-29 -> spre 60%`, `30-31 -> spre 40%`. Afiseaza ziua, arcana si procentul fara paranteze editoriale in calcul sau in celulele tabelului.
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
- Citeste si scrie fisierele `.md` si `.html` explicit ca UTF-8. Nu trece continutul romanesc prin conversii implicite de code page si nu rescrie fisierele prin combinatii ambigue `Get-Content`/`WriteAllText`. Pentru schimbari editoriale foloseste patch-uri tintite; dupa orice transformare mecanica verifica absenta secventelor de mojibake precum `Ã`, `Ä`, `È`, `Â`, `â€”`, `â†’` si caracterul de inlocuire `�`.
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
- Cuprinsul Markdown nu contine wikilinkuri sau trimiteri interne necerute, iar Cuprinsul HTML foloseste ancore `<a href="#...">` valide; toate SVG-urile si imaginile din HTML sunt incorporate ca data URI;
- absenta formularilor metatextuale care anunta ce se analizeaza;
- lipsa textelor generice ramase din template.
- diacriticele romanesti sunt intacte in ambele livrabile, fisierele sunt UTF-8 si cautarea dupa secvente de mojibake nu returneaza rezultate.

Pentru lucrarile construite dupa modelul final Daniel, aplica si [[skills/numerologie-lucrare-redactare/references/lista-control-model-final-daniel|Lista de control pentru modelul final Daniel]].

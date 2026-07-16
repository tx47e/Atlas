---
name: numerologie-lucrare-redactare
description: Elaboreaza, adapteaza si verifica lucrari numerologice complete in Markdown si HTML, ruland calculatorul Python inclus pentru date personale si relationale si aplicand template-uri, interpretari ample si formatare consecventa. Foloseste cand se cere o lucrare numerologica noua, completarea sau revizia unei lucrari existente, alegerea unui tip de lucrare ori template, sincronizarea MD-HTML sau redactarea de interpretari pentru caracter, destin, relatii, cariera, iubire, bani, faima si intervale de ani.
---

# Redactarea lucrarilor numerologice

## Flux obligatoriu

1. Colecteaza datele prin formularul din `references/formular-date.md`.
2. Alege template-ul cerut. Pentru `examen`, foloseste `assets/Template-lucrare-examen.md`.
3. Citeste [[skills/numerologie-lucrare-redactare/references/reguli-redactare|Reguli de redactare]] inainte de redactare sau revizie.
4. Ruleaza `scripts/calculator_numerologic_examen.py` si salveaza sau pastreaza iesirea JSON ca sursa a tuturor valorilor de calcul.
5. Pentru o relatie, ruleaza calculatorul separat si pentru a doua persoana, apoi foloseste cele doua rezultate in analiza relationala.
6. Redacteaza mai intai continutul complet, apoi sincronizeaza varianta Markdown cu HTML-ul canonic.
7. Genereaza graficele prin skill-urile SVG dedicate, folosind valorile returnate de calculator.
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

- `examen`: foloseste template-ul inclus si toate capitolele cerute de acesta.
- `scurt`, alte tipuri sau template-uri viitoare: foloseste fisierul dedicat numai daca exista in `assets/`. Daca nu exista, cere utilizatorului confirmarea structurii inainte de a inventa una.
- Pastreaza fiecare template intr-un fisier distinct, cu nume de forma `Template-lucrare-{tip}.md`.

## Reguli de continut

- Nu inventa date personale, relationale sau biografice.
- Nu transforma numerologia intr-un verdict. Foloseste limbaj simbolic, nu afirmatii absolute.
- Personalizeaza interpretarea prin legaturi intre rezultate, exemple concrete, analogii si imagini din cuvinte.
- Include capitolul `Cuvant inainte` imediat dupa Cuprins si inainte de Capitolul 1. Foloseste ca sursa reutilizabila `vault/Numerologie/Introducere.md`, pastreaza imaginea unitara a calatoriei si modifica textul numai cand este necesara alinierea la conceptele lucrarii. Textul cuprinde si ciclicitatile, anii importanti interiori si exteriori, ciclurile de 7, 9 si 12 ani, Soarta si Destinul, lectiile de viata si anul personal, integrate narativ, nu enumerate tehnic.
- Incepe direct cu sensul conceptului sau cu interpretarea. Evita formularile metatextuale de tipul `[Prenume], aici ne uitam la...`, `aici vedem...` sau `in aceasta sectiune analizam...`.
- Foloseste arhetipuri numai in interpretarile Vibratiei interioare, Vibratiei exterioare si Vibratiei globale.
- Pentru cele trei vibratii permise, urmeaza: definitie -> metoda -> calcul -> interpretarea conversationala a traseului de reducere, numai daca exista o reducere suplimentara -> rezultat -> imagine -> arhetip -> manifestare concreta -> umbra -> maturizare.
- Pentru vibratiile fundamentale, interpreteaza traseul numai cand calculul are una sau mai multe trepte reale de reducere. Explica direct persoanei sensul cifrelor de intrare, suma intermediara, cifrele reducerii si felul in care aceste straturi se regasesc in rezultatul final. Daca valoarea este deja o singura cifra, prezinta direct interpretarea ei, fara sa mentionezi ca nu exista traseu. Daca apare 0, explica prudent ca nu adauga o directie numerica separata, dar poate deschide sau amplifica potentialul cifrei alaturate.
- Pastreaza volumul amplu fara sa repeti sensul traseului in paragrafele urmatoare. Dupa traseu, pune accentul pe rezultatul final; fiecare paragraf ulterior trebuie sa aduca o functie distincta: manifestare observabila, exemplu practic, rutina aplicabila, umbra sau criteriu de maturizare. Daca un paragraf doar reformuleaza traseul ori rezultatul, rescrie-l ca aplicatie concreta.
- La Vibratia globala, interpreteaza intotdeauna dialogul dintre Vibratia interioara si Vibratia exterioara. Numeste acest calcul traseu de reducere si desface suma intermediara numai daca rezultatul adunarii depaseste 9; de exemplu, `9 + 9 = 18 -> 1 + 8 = 9`.
- Nu aplica obligatoriu interpretarea traseului de reducere la Calea Destinului, Destin sau Aspectele de indreptat. Puntile interior-exterior si interior-destin se interpreteaza prin valorile initiale si rezultat, conform structurii existente. La Solutia aspectelor de indreptat este recomandata interpretarea rezultatului, nu desfacerea ampla a traseului.
- Pentru toate celelalte sectiuni, urmeaza: definitie -> metoda -> calcul -> rezultat -> imagine -> manifestare concreta -> umbra -> maturizare, fara arhetipuri sau roluri arhetipale mascate.
- Pastreaza `Scara bunastarii` ca subcapitol separat al Structurii matriciale, imediat dupa tendinte, fixatie si analogia cai-trasura-vizitiu. Foloseste titlul numerotat `4.6. Scara bunastarii`, ancora proprie si index `SUB` in variantele de revizie.
- La Numarul neamului, afiseaza calculul in intervalul 1-22 si un tabel cu arcana rezultata si interpretare ampla: resursa mostenita, manifestare concreta, umbra si maturizare.
- La Spirit -> Inclinatii profesionale, afiseaza separat calculele DA si NU si un tabel cu arcana fiecarui rezultat. Formuleaza conversational si explicit `Aplicabilitatea profesionala DA este arcana X, Nume`, apoi explica directia cultivabila; pentru negativ foloseste `Aplicabilitatea profesionala NU este arcana Y, Nume` si explica obstacolul si cheia de lucru in pasi concreti.
- Cand folosesti coduri de vectori sau diagonale, scrie imediat si denumirea lor pentru cititor (de exemplu `vectorul 789, Creativitate` si `diagonala 159, Cariera`); nu lasa codul numeric neexplicat si nu obliga cititorul sa revina la o sectiune anterioara.
- Scrie denumirile complete ale vibratiilor. Nu folosi acronime precum `VI`, `VE`, `VG`, `VCV` sau `VCT` in text ori calcule.
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
- Pastreaza resursele SVG/PNG langa lucrare si referintele relative valide.
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
- prezenta capitolului `Cuvant inainte` dupa Cuprins si inainte de Capitolul 1, in ambele livrabile;
- absenta formularilor metatextuale care anunta ce se analizeaza;
- lipsa textelor generice ramase din template.

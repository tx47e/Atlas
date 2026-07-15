---
name: numerologie-lucrare-redactare
description: Elaboreaza, adapteaza si verifica lucrari numerologice complete in Markdown si HTML, ruland calculatorul Python inclus pentru date personale si relationale si aplicand template-uri, interpretari ample si formatare consecventa. Foloseste cand se cere o lucrare numerologica noua, completarea sau revizia unei lucrari existente, alegerea unui tip de lucrare ori template, sincronizarea MD-HTML sau redactarea de interpretari pentru caracter, destin, relatii, cariera, iubire, bani, faima si intervale de ani.
---

# Redactarea lucrarilor numerologice

## Flux obligatoriu

1. Colecteaza datele prin formularul din `references/formular-date.md`.
2. Alege template-ul cerut. Pentru `examen`, foloseste `assets/Template-lucrare-examen.md`.
3. Citeste `references/reguli-redactare.md` inainte de redactare sau revizie.
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
- Pentru sectiunile majore, urmeaza: definitie -> metoda -> calcul -> rezultat -> imagine -> arhetip -> manifestare concreta -> umbra -> maturizare.
- Scrie denumirile complete ale vibratiilor. Nu folosi acronime precum `VI`, `VE`, `VG`, `VCV` sau `VCT` in text ori calcule.
- Include datele relationale in `Date generale` atunci cand sunt furnizate, nu doar in capitolul Relatii.
- Pastreaza relatia optionala: daca nu exista, omite sectiunea fara campuri fictive.

## Reguli pentru calcule

- Explica metoda intr-un paragraf inaintea chenarului.
- Pastreaza in chenar doar traseul numeric, etichete scurte indispensabile si rezultatul.
- Leaga pasii cu ` -> `.
- Marcheaza rezultatul final complet cu `<strong>...</strong>` in HTML.
- Nu introduce explicatii, propozitii sau acronime in chenar.
- Cand exista doua rezultate finale, pune-le pe randuri separate si marcheaza fiecare rezultat complet.

## Livrabile

- Livreaza perechea `.md` si `.html` cu acelasi continut semantic.
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
- rezultatele complete marcate in chenare;
- intervalul de ani cerut;
- consistenta intre Markdown, HTML, tabele si grafice;
- lipsa textelor generice ramase din template.

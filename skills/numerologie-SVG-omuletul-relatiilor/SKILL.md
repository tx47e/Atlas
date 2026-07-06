---
name: numerologie-SVG-omuletul-relatiilor
description: Creeaza sau adapteaza SVG-uri numerologice pentru Omuletul Relatiilor. Foloseste acest skill cand utilizatorul cere numerologie SVG, omuletul relatiilor, compatibilitate de cuplu sau un SVG de relatie similar cu referinta locala.
tags: [skill]
---

# Numerologie SVG Omuletul Relatiilor

## Surse obligatorii

1. Consulta obligatoriu `vault/Numerologie/Omuletul Relatiilor.md` inainte de calcul, completarea valorilor sau interpretare.
2. Acolo se afla documentatia pentru intocmirea diagramei, pozitionarea cifrelor, interpretare, sinteza relationala si verificari.
3. Consulta documentele dependente mentionate acolo. Pentru metoda implicita foloseste cifrele brute din data nasterii; consulta `vault/Numerologie/Cod Numerologic Personal.md` doar daca utilizatorul cere explicit sursa extinsa.
4. Foloseste `assets/reference.svg` ca model vizual principal si unic: imagine de fundal Vitruvian embed-uita, fundal SVG potrivit cromatic cu marginile imaginii, cerc/patrat/pentagrama suprapuse peste reperele din imagine si casete numerice apropiate de colturile pentagramei fara sa atinga liniile.
5. Daca exista conflict intre asset si documentatia din vault, documentatia din vault are prioritate pentru metoda, valori si interpretare.

## Logica de calcul din documentatie

1. Omuletul relatiilor este o diagrama comparativa construita implicit din cifrele brute ale datelor de nastere ale persoanelor analizate.
2. Pentru fiecare persoana se numara cifrele 0-9 exact asa cum apar in zi, luna si an. Nu adauga automat N1, N2, N3, N4 si nu folosi codul numerologic personal extins decat daca utilizatorul cere explicit aceasta sursa.
3. Aceeasi sursa de cifre trebuie folosita pentru toate persoanele comparate. Daca se foloseste matricea personala, matricea numelui, codul numerologic personal extins sau alt set ales explicit, mentioneaza clar sursa in lucrare si interpretare.
4. Pozitiile cifrelor pe pentagrama se pastreaza constant:

| Cifra | Pozitie in diagrama |
| --- | --- |
| 1 | varful de sus al pentagramei |
| 2 | coltul interior din dreapta sus |
| 3 | coltul exterior din dreapta |
| 4 | coltul interior din dreapta jos |
| 5 | coltul exterior de jos |
| 6 | centrul pentagramei, punctul de intersectie |
| 7 | coltul exterior din stanga jos |
| 8 | coltul interior din stanga jos |
| 9 | coltul exterior din stanga |
| 0 | coltul interior din stanga sus |

5. Pentru fiecare cifra noteaza cantitatea pe persoana, totalul relatiei, cine sustine cifra si zonele slabe sau absente.
6. `Ce se poate realiza impreuna` se calculeaza prin adunarea vibratiilor interioare reduse si reducere numerologica.
7. `Ce este de rezolvat impreuna` se calculeaza prin diferenta absoluta a vibratiilor interioare reduse pentru doua persoane; pentru trei persoane se calculeaza diferentele pe perechi.
8. Elementele se totalizeaza astfel: Foc = 1 + 5 + 9, Apa = 2 + 6, Aer = 3 + 7, Pamant = 4 + 8, iar 0 ramane Potential separat.

## Reguli vizuale pentru casetele cifrelor

1. Toate cifrele din diagrama trebuie sa foloseasca aceeasi dimensiune de font. Nu mari fontul pentru cifre scurte si nu il micsora separat pentru cifre lungi; daca sunt multe cifre, se mareste chenarul.
2. Valorile pentru doua persoane se afiseaza cu spatii clare in jurul separatorului: `2 / 222`, `111 / 1111`, `9999 / 999`.
3. Chenarul fiecarei pozitii se dimensioneaza dupa textul complet afisat in acea pozitie. Formula recomandata pentru generator este:

```text
font_size = 24
char_width_aprox = font_size * 0.58
padding_x = 14
padding_y = 10
box_width = max(min_width, len(text_afisat) * char_width_aprox + 2 * padding_x)
box_height = font_size + 2 * padding_y
```

4. Pentru pozitii cu valori pe doua persoane, `text_afisat` include ambele valori si separatorul cu spatii. Exemplu: `9999 / 999`.
5. Textul trebuie centrat vertical si orizontal in chenar. Chenarul nu trebuie sa atinga cifrele; trebuie sa ramana padding vizibil pe toate partile.
6. Daca o pozitie este absenta la ambele persoane, nu se afiseaza `0 / 0` ca lipsa numerologica. Cifra `0` se afiseaza doar in pozitia ei reala de potential, cand exista in sursa de cifre folosita.
7. Daca legenda de sus sau sinteza de jos se apropie de diagrama, extinde viewBox-ul pe verticala si coboara diagrama. Nu suprapune niciodata legenda, casetele cifrelor, pentagrama sau sinteza elementelor.
8. Dupa generare, verifica obligatoriu ca SVG-ul este XML valid si ca nu exista suprapuneri intre texte sau intre texte si chenare.

## Reguli vizuale pentru fundalul Vitruvian si geometrie

1. Cand se foloseste fundalul cu omul vitruvian, imaginea ramane nealterata ca format si este embed-uita in SVG; fundalul SVG trebuie setat dupa culoarea medie a marginilor imaginii pentru continuitate vizuala.
2. Cercul, patratul, axele si pentagrama nu se pozitioneaza independent. Ele se calibreaza dupa cercul si patratul reale din imaginea de fundal.
3. Daca cercul din imagine apare usor eliptic dupa incadrare, foloseste `ellipse` in SVG, nu forta un `circle` care nu se suprapune vizual.
4. Varfurile pentagramei se construiesc dupa acelasi centru si aceleasi raze vizuale ca cercul din fundal, astfel incat pentagrama sa apartina aceleiasi geometrii.
5. Casetele pentru `1`, `3`, `5`, `7`, `9` se aseaza aproape de varfurile pentagramei, cu o distanta constanta de siguranta fata de colt.
6. Casetele pentru `0` si `2` se aseaza deasupra liniei orizontale negre a pentagramei, aproape de colturile interioare superioare, fara sa calce pe linie.
7. Casetele pentru `8` si `4` se aseaza aproape de colturile interioare laterale ale pentagramei si usor deasupra zonei de intersectie, fara suprapunere cu liniile.
8. Pastreaza legenda de sus si sinteza elementelor de jos in afara diagramei. Daca este nevoie, extinde inaltimea SVG-ului.

Asset-ul `assets/reference.svg` contine exemplul actualizat cu fundal Vitruvian, spatiere verticala extinsa, geometrie aliniata pe imagine, casete cu padding si dimensiuni adaptate lungimii grupurilor de cifre.
## Workflow

1. Citeste `vault/Numerologie/Omuletul Relatiilor.md` si documentele dependente necesare pentru datele furnizate.
2. Stabileste explicit sursa cifrelor folosita pentru toate persoanele comparate.
3. Calculeaza distributia cifrelor, totalurile relationale, sinteza pe elemente si cele doua rezultate de sinteza.
4. Foloseste `assets/reference.svg` ca sablon de compozitie, nu ca sursa principala de calcul.
5. Pastreaza structura omuletului/amuletului, legaturile dintre valori si ordinea zonelor.
6. Actualizeaza numele, datele si valorile numerologice ale persoanelor cand sunt furnizate.
7. Daca lipsesc date pentru o persoana, marcheaza explicit campurile ca `de completat`.
8. Salveaza SVG-ul rezultat in `vault/Numerologie/` sau in calea ceruta de utilizator.
9. Verifica SVG-ul ca XML valid si inspecteaza vizual ca liniile, nodurile si textele sa fie lizibile.
10. Verifica matematic distributiile, totalurile pe cifra, totalurile pe elemente si sintezele relationale.

## Regula pentru includerea in lucrari HTML

1. In varianta `.md`, omuletul se pastreaza ca imagine Markdown normala, de forma `![descriere](nume-asset.svg)`. Nu se introduc fragmente HTML in Markdown.
2. In varianta `.html` destinata trimiterii ca fisier unic, SVG-ul omuletului trebuie inclus ca imagine embedded, nu ca referinta externa la fisier. Se foloseste:

```html
<img class="embedded-svg" src="data:image/svg+xml;base64,{{svg_base64}}" alt="{{descriere}}">
```

3. Aceasta regula este obligatorie mai ales cand SVG-ul contine imagine de fundal embed-uita, cum este fundalul Vitruvian. Daca HTML-ul trimis separat refera `src="nume-asset.svg"`, exista risc ca fundalul sau intreaga diagrama sa nu se mai vada la destinatar.
4. Inainte de conversia in base64, SVG-ul se salveaza UTF-8 fara BOM si se verifica XML valid.
5. Dupa generarea HTML-ului, verifica faptul ca nu mai exista referinta externa pentru omulet si ca `src` incepe cu `data:image/svg+xml;base64,`.

## Regula watermark

- Fiecare SVG final trebuie sa includa watermark-ul `Atlas Numerologie` in coltul dreapta jos al panzei SVG.
- Stil recomandat, discret si consecvent cu septagrama validata: `font-family="Arial, Helvetica, sans-serif"`, `font-size="14"`, `fill="#aaa"`, `font-weight="800"`, `text-anchor="end"`.
- Pozitionare recomandata: `x = latime_viewBox - 20`, `y = inaltime_viewBox - 15`. Pentru SVG-uri cu margini sau continut special, pastreaza watermark-ul in interiorul panzei, fara sa atinga rama sau elementele principale.
- Textul trebuie scris exact `Atlas Numerologie`, nu cu majuscule integrale.

## Reference
- `vault/Numerologie/Omuletul Relatiilor.md` este sursa de adevar pentru metoda, pozitionari numerologice, formule, interpretare si verificari.
- `assets/reference.svg` este modelul vizual unic si validat pentru Amuletul/Omuletul Relatiilor: fundal Vitruvian, geometrie aliniata pe imagine, casete numerice dimensionate dupa continut, font uniform si spatiere verticala sigura.

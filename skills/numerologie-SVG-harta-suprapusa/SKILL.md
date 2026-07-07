---
name: numerologie-SVG-harta-suprapusa
description: Creeaza sau adapteaza SVG-uri numerologice pentru Harta Suprapusa: grafic combinat Soarta si Destin cu cicluri de 7, 9 si 12 ani, ani interior/exterior, ani de rascruce si ani de criza. Foloseste acest skill cand utilizatorul cere harta suprapusa, soarta si destin suprapuse, ciclicitati suprapuse sau refacerea graficului harta-suprapusa-soarta-destin.
tags: [skill]
---

# Numerologie SVG Harta Suprapusa

## Surse obligatorii

1. Consulta obligatoriu `vault/Numerologie/Soarta si Destin.md` pentru calculele Soarta si Destin.
2. Consulta documentatia din `vault/Numerologie/` pentru ciclurile de 7, 9 si 12 ani si pentru anii interiori/exteriori, de rascruce si de criza, cand aceste valori nu sunt deja calculate in lucrarea persoanei.
3. Daca exista conflict intre calcule, asset, lucrarea existenta si documentatia din vault, documentatia din vault are prioritate pentru metoda si valori.
4. Foloseste `assets/visual-reference.png` ca referinta vizuala principala pentru paleta, raportul graficului, legenda, grila, linii si densitatea informatiei.
5. Foloseste `assets/legacy-harta-suprapusa.svg` doar ca referinta structurala pentru campurile existente in proiect, nu ca model vizual final.

## Asset-uri

- `assets/visual-reference.png` - referinta vizuala validata pentru aspect: grafic mare, Soarta verde, Destin rosu, zona de confort, linii portocalii si pastile de cicluri.
- `assets/legacy-harta-suprapusa.svg` - exemplu existent din proiect pentru tipurile de date care trebuie pastrate: Soarta, Destin, cicluri 7/9/12, ani interiori/exteriori, rascruce si criza.

## Reguli de calcul

1. Calculeaza Soarta si Destin dupa metoda din `vault/Numerologie/Soarta si Destin.md`.
2. Pastreaza numerele grafice ca serii de cifre si traseaza fiecare cifra ca punct pe grafic.
3. Pentru calcule cu traseu lung, foloseste `->` intre pasi, nu punct si virgula.
4. Pentru fiecare punct de pe grafic, afiseaza valoarea cifrei direct langa punct. Nu mai crea rand separat de valori Soarta/Destin sub grafic.
5. Calculeaza zona de confort pentru Soarta si Destin conform documentatiei si marcheaz-o pe grafic prin linii orizontale subtile.
6. Pastreaza ciclurile de 7, 9 si 12 ani. Ordinea vizuala sub grafic este obligatoriu: `7`, `9`, `12`.
7. Harta suprapusa se deseneaza implicit pe intervalul `0-108 ani`, daca utilizatorul nu cere alt interval.
8. Seria Soarta si seria Destin se continua pe tot intervalul graficului prin repetarea aceluiasi pattern de 7 cifre. Dupa ultimul punct al seriei, urmatorul punct reia prima cifra a pattern-ului.
9. Ciclul de 9 ani se calculeaza si se afiseaza integral pentru toata perioada desenata, nu doar pentru un interval scurt din lucrare.
10. Anii interior si exterior se plaseaza deasupra pastilelor ciclurilor, imediat sub axa graficului, fara linii verticale, daca utilizatorul nu cere explicit trasarea liniilor.

## Reguli vizuale

1. Graficul principal trebuie sa ocupe cat mai mult din panza SVG. Redu spatiile decorative si evita panouri laterale mari daca micsoreaza graficul.
2. Paleta trebuie sa urmeze referinta:
   - Soarta: verde.
   - Destin: rosu.
   - Zona de confort: gri deschis / linie punctata discreta.
   - Marcaje verticale si crize: portocaliu.
   - Oportunitate pinaclu: mov sau alta culoare distincta de portocaliul ciclului de 7 ani.
   - Provocare pinaclu: albastru.
3. Liniile Soarta si Destin trebuie sa fie clare, cu puncte vizibile pe fiecare cifra.
4. Valorile Soarta si Destin se scriu direct pe sau langa punctele de pe grafic, cu contrast bun si fara suprapuneri.
5. Nu include in partea de jos randuri separate `Soarta` si `Destin` cu valori: valorile sunt deja pe puncte.
6. Ciclurile de 7, 9 si 12 ani se afiseaza sub grafic sub forma de pastile/benzi compacte, asemanatoare cu structura actuala din proiect, dar ordonate `7`, `9`, `12`.
7. Anii interior si exterior se afiseaza deasupra ciclurilor, sub axa orizontala, ca texte/puncte compacte; nu trasa linii verticale pentru ei cand graficul este deja dens.
8. Liniile pentru ciclul de 7 ani si pentru crizele atasate se traseaza discret, cu linie intrerupta, ca sa nu concureze cu Soarta si Destinul.
9. Etichetele de varsta pentru ciclul de 7 ani se muta deasupra graficului si se marcheaza cu triunghi cu varful in jos.
10. Traseaza in acelasi grafic liniile pentru oportunitati si provocari numai pe intervalele pinaclurilor. Nu repeta oportunitatile/provocarile ca serie ciclica independenta.
11. Fiecare pinaclu are o singura oportunitate si o singura provocare atasata; acele valori se afiseaza atat pe linia din grafic, cat si in pastila pinaclului de jos.
12. Liniile de oportunitate si provocare se traseaza continuu, fara linie intrerupta, in trepte: orizontal pana la finalul pinaclului, apoi vertical la granita pinaclului pana la urmatoarea valoare, apoi iar orizontal.
13. Pinaclurile se afiseaza jos, langa sau sub cicluri, ca pastile/benzi compacte, apropiate vizual de randurile ciclurilor 7, 9 si 12, dar cu o culoare proprie diferita de portocaliul ciclului de 7 ani.
14. Legenda trebuie sa stea in dreapta graficului, in afara zonei de plot, nu peste grila si linii.
15. Axa verticala afiseaza cifrele `0-9`.
16. Axa orizontala afiseaza varste/repere temporale clare, asemanator referintei vizuale.
17. Pastreaza legenda doar pentru elementele care nu sunt evidente din grafic. Evita legenda duplicata pentru Soarta/Destin daca valorile sunt marcate clar pe puncte.
18. Foloseste fundal de hartie veche / crem deschis, in acord cu lucrarea, nu card alb separat.

## Workflow

1. Identifica persoana, data nasterii si lucrarea sau calea de output.
2. Citeste documentatia necesara din `vault/Numerologie/` si, daca exista, valorile deja calculate in lucrarea `.md`.
3. Calculeaza sau extrage Soarta, Destin, zonele de confort, ciclurile 7/9/12, anii interiori/exteriori, anii de rascruce si anii de criza.
4. Genereaza SVG-ul pornind de la structura vizuala din `assets/visual-reference.png`, nu din `legacy-harta-suprapusa.svg`.
5. Pastreaza datele numerologice din proiect, dar redeseneaza layout-ul daca vechiul SVG nu respecta referinta.
6. Salveaza SVG-ul in folderul lucrarii sau in calea ceruta de utilizator.
7. Verifica SVG-ul ca XML valid.
8. Inspecteaza vizual ca graficul este mare, punctele au valori lizibile, ciclurile sunt ordonate `7`, `9`, `12`, anii interior/exterior nu aglomereaza graficul, iar legenda este in dreapta plotului.

## Regula watermark

- Fiecare SVG final trebuie sa includa watermark-ul `Atlas Numerologie` in coltul dreapta jos al panzei SVG.
- Stil recomandat: `font-family="Arial, Helvetica, sans-serif"`, `font-size="14"`, `fill="#aaa"`, `font-weight="800"`, `text-anchor="end"`.
- Pozitionare recomandata: `x = latime_viewBox - 20`, `y = inaltime_viewBox - 15`.
- Textul trebuie scris exact `Atlas Numerologie`, nu cu majuscule integrale.

## Criterii de calitate

- SVG valid XML.
- Graficul principal este elementul dominant al imaginii.
- Soarta este verde si Destinul rosu.
- Zona de confort este vizibila, dar discreta.
- Valorile nu se suprapun peste puncte, axe sau alte etichete.
- Ciclurile sunt compacte, ordonate si lizibile.
- Anii interior/exterior sunt separati clar de cicluri si nu au linii verticale cand graficul este deja dens.
- Watermark-ul exista si nu interfereaza cu continutul.

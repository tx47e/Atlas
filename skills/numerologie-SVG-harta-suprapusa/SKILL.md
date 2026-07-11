---
name: numerologie-SVG-harta-suprapusa
description: Creeaza sau adapteaza SVG-uri numerologice pentru Harta Suprapusa: grafic combinat Soarta si Destin cu cicluri de 7, 9 si 12 ani, ani interior/exterior, lectii de viata, pinacluri, oportunitati si provocari. Foloseste acest skill cand utilizatorul cere harta suprapusa, soarta si destin suprapuse, ciclicitati suprapuse sau refacerea graficului harta-suprapusa-soarta-destin.
tags: [skill]
---

# Numerologie SVG Harta Suprapusa

## Surse obligatorii

1. Consulta obligatoriu `vault/Numerologie/Soarta si Destin.md` pentru calculele Soarta si Destin.
2. Consulta documentatia din `vault/Numerologie/` pentru ciclurile de 7, 9 si 12 ani, anii interiori/exteriori, lectiile de viata, pinacluri, oportunitati si provocari, cand aceste valori nu sunt deja calculate in lucrarea persoanei.
3. Daca exista conflict intre calcule, asset, lucrarea existenta si documentatia din vault, documentatia din vault are prioritate pentru metoda si valori.
4. Foloseste `assets/reference.svg` ca referinta vizuala principala validata. Aceasta este varianta V2 aprobata pentru Birsan Daniel Robert si defineste layout-ul final.
5. Foloseste `templates/harta-suprapusa-template.py` ca punct de pornire pentru generari noi. Adapteaza datele persoanei si seriile calculate, nu redesena structura de la zero.
6. Foloseste `assets/visual-reference.png` doar ca reper extern de paleta si densitate vizuala.
7. Foloseste `assets/legacy-harta-suprapusa.svg` doar pentru compatibilitate istorica, nu ca model vizual final.

## Asset-uri

- `assets/reference.svg` - referinta SVG validata pentru V2: grafic mare, legenda in dreapta, Soarta/Destin pe grafic si in randuri sub axa, ani interior/exterior, cicluri 7/9/12, pinaclu, oportunitate, provocare si lectii de viata.
- `templates/harta-suprapusa-template.py` - template Python reutilizabil pentru generarea SVG-ului.
- `assets/visual-reference.png` - referinta vizuala externa pentru stil general, paleta, raportul graficului si densitatea informatiei.
- `assets/legacy-harta-suprapusa.svg` - exemplu vechi din proiect; foloseste-l doar pentru campuri istorice, daca este nevoie.

## Reguli de calcul

1. Calculeaza Soarta si Destin dupa metoda din `vault/Numerologie/Soarta si Destin.md`.
2. Pentru calcule cu traseu lung, foloseste `->` intre pasi, nu `;`.
3. Harta suprapusa se deseneaza implicit pe intervalul `0-108 ani`, daca utilizatorul nu cere alt interval.
4. Seria Soarta si seria Destin se continua pe tot intervalul graficului prin repetarea aceluiasi pattern. Dupa ultimul punct al seriei, urmatorul punct reia prima cifra a pattern-ului.
5. Calculeaza zona de confort pentru Soarta si Destin conform documentatiei si marcheaz-o pe grafic prin linii orizontale punctate discrete.
6. Calculeaza ciclul de 7 ani, crizele ciclului de 7 ani, ciclul de 9 ani si ciclul de 12 ani pana la finalul intervalului desenat.
7. Calculeaza anii interiori si exteriori de la data nasterii pana la finalul tabelului.
8. Calculeaza lectiile de viata si introdu-le ca linie distincta pe grafic.
9. Calculeaza pinaclurile, oportunitatile si provocarile pe intervalele lor. Fiecare pinaclu are o singura oportunitate si o singura provocare atasata.

## Reguli vizuale validate V2

1. Graficul principal este elementul dominant al SVG-ului. Pastreaza raportul si spatierea din `assets/reference.svg`.
2. Titlul din stanga sus este `Harta suprapusa soarta-destin-ciclicitati`.
3. In dreapta sus se afiseaza doar numele persoanei si sub el data nasterii, aliniate la dreapta. Nu repeta Soarta/Destin acolo.
4. Axa verticala se numeste `Vibratie` si afiseaza cifrele `0-9`.
5. Axa orizontala afiseaza varstele, iar eticheta `Ani` se plaseaza in capatul axei, dupa 108.
6. Soarta este verde, Destinul este rosu. Liniile au puncte vizibile, dar valorile nu se scriu peste puncte in grafic.
7. Valorile Soarta si Destin se afiseaza in doua randuri sub axa X, intre axa si anii interior/exterior, pe intervale de cate 10 ani.
8. Zona de confort se afiseaza in doua linii punctate discrete, in culorile Soarta si Destin, iar valorile rezultate apar in legenda.
9. Oportunitatea si provocarea se traseaza ca linii continue in trepte: orizontal pana la finalul pinaclului, vertical la granita, apoi orizontal pe urmatorul interval.
10. Nu repeta oportunitatile/provocarile ca serie ciclica independenta. Ele apartin pinaclurilor.
11. Linia lectiilor de viata trebuie sa aiba o culoare distincta si discreta fata de provocare si fata de anii interior/exterior.
12. Anii interiori si exteriori se afiseaza sub randurile Soarta/Destin. Fiecare eveniment are linie verticala punctata prin tot graficul si etichete rotite langa linie.
13. Daca anii interiori si exteriori coincid, eticheta pentru interior sta in stanga liniei, iar eticheta pentru exterior in dreapta liniei, cu distante egale fata de linie.
14. Daca etichetele anilor interiori/exteriori sunt prea apropiate, foloseste lane-uri verticale si impinge continutul de mai jos in jos, astfel incat textul sa ramana lizibil.
15. Ciclul de 7 ani se afiseaza intre anii exteriori si ciclul de 9 ani, cu triunghiuri portocalii cu varful in jos pentru cicluri si triunghiuri portocalii outline cu varful in sus pentru crize.
16. Triunghiurile ciclului de 7 si triunghiurile de criza trebuie sa aiba aceeasi dimensiune vizuala. Pentru triunghiul plin foloseste si outline, ca cifra interioara sa fie centrata corect.
17. Ciclul de 9 ani se afiseaza jos, sub ciclul de 7 ani, cu patrate visinii uniforme.
18. Ciclul de 12 ani se afiseaza jos, sub ciclul de 9 ani, cu patrate albastre uniforme.
19. Pinaclurile se afiseaza jos, sub ciclul de 12 ani, cu patrate mustar uniforme.
20. Intre ciclul de 12 ani si pinacluri pastreaza spatiu cel putin egal cu distanta dintre ciclul de 9 si ciclul de 12.
21. La pinaclu, leaga patratele intre ele cu doua linii: culoarea oportunitatii si culoarea provocarii. Linia valorii mai mari sta deasupra; linia valorii mai mici sta dedesubt. Etichetele O/P se plaseaza langa linia corespunzatoare, cu distanta egala.
22. Toate liniile verticale pentru cicluri, ani si pinacluri se traseaza in spatele formelor si textelor. Nicio linie nu are voie sa treaca peste o eticheta lizibila.
23. Daca mai multe evenimente cad pe aceeasi varsta, ingroasa linia verticala proportional cu numarul de suprapuneri.
24. Liniile pentru ciclul de 12 ani si pinacluri se prelungesc prin tot graficul, pana sus.
25. Legenda se plaseaza in dreapta graficului, in afara zonei de plot, aliniata aproximativ la mijlocul graficului pe verticala.
26. Legenda trebuie sa foloseasca simbolul real al elementului: linie pentru Soarta, Destin, zona de confort, oportunitate, provocare, lectii de viata, ani interior si ani exterior; triunghi pentru ciclu 7 si criza; patrat pentru ciclu 9, ciclu 12 si pinaclu.
27. Etichetele din legenda folosesc cifre: `Ciclu 7`, `Ciclu 9`, `Ciclu 12`.
28. Fundalul ramane crem deschis / hartie veche, in acord cu lucrarea.

## Workflow

1. Identifica persoana, data nasterii si lucrarea sau calea de output.
2. Citeste valorile deja calculate in lucrarea `.md`, daca exista.
3. Citeste documentatia necesara din `vault/Numerologie/` pentru valorile lipsa.
4. Porneste de la `templates/harta-suprapusa-template.py` si adapteaza constantele, seriile si datele persoanei.
5. Compara rezultatul cu `assets/reference.svg` si pastreaza structura V2.
6. Salveaza SVG-ul in folderul lucrarii sau in calea ceruta de utilizator.
7. Verifica SVG-ul ca XML valid.
8. Inspecteaza vizual ca textele nu se suprapun, liniile sunt in spatele formelor, legenda nu este inghesuita, iar randurile de jos sunt lizibile.
9. Daca SVG-ul este introdus intr-o lucrare, actualizeaza si Markdown-ul si HTML-ul corespunzator cand exista ambele.

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
- Valorile Soarta/Destin sunt lizibile in randurile dedicate si nu incarca punctele din grafic.
- Ciclurile 7, 9, 12 si pinaclurile sunt compacte, uniforme si lizibile.
- Anii interior/exterior sunt separati clar si au culori distincte.
- Liniile suprapuse sunt ingrosate controlat.
- Legenda corespunde exact simbolurilor din grafic.
- Watermark-ul exista si nu interfereaza cu continutul.

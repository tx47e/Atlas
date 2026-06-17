# Vibratia interioara - observatii

## Decizie de lucru

Pentru proiect, vibratia interioara se calculeaza din ziua nasterii, nu din nume.
Regulile legate de vocale, consoane, diacritice si nume multiple apartin
calculelor derivate din nume.

## Reguli de implementare

- Input minim: ziua nasterii, ca numar intre 1 si 31.
- Rezultat standard: numar intre 1 si 9.
- Rezultat optional: valoare intermediara pentru 11 sau 22, daca se activeaza interpretarea numerelor maestre.
- Pentru zilele 10, 20 si 30, se reduce la 1, 2 si 3.
- Se pastreaza traseul complet al reducerii, nu doar rezultatul final.
- Fiecare pas intermediar poate fi folosit pentru nuantarea interpretarii.

## Regula de interpretare pe traseu

Interpretarea se face in straturi:

1. vibratia finala este directia principala;
2. cifrele initiale arata materialul din care se formeaza vibratia;
3. rezultatele intermediare arata praguri sau transformari;
4. formule mai lungi cer interpretari mai nuantate.

Exemplu: 28 nu se citeste doar ca 1. Se citeste ca 2 + 8, apoi 10, apoi 1.

## Surse

- https://asociatianumerologilor.ro/calculator-numerologie/
- https://www.dcnews.ro/vibratia-interioara-metoda-de-calcul-pe-intelesul-tuturor-cum-iti-afecteaza-relatiile_837126.html
- https://ro.wikibooks.org/wiki/Numerologie/Vibra%C8%9Bia_interioar%C4%83

# Numarul ereditar karmic - metoda

Formula adoptata pentru proiect:

```text
numarul ereditar karmic = reducere_22(suma valorilor literelor din numele de familie)
```

Termeni echivalenti folositi in bibliografie sau in lucru:

```text
numarul ereditar karmic = numarul neamului = karma neamului
```

In proiect nu se pastreaza un calcul separat numit `karma neamului`, deoarece
formula este aceeasi.

Unde:

```text
reducere_22(numar):
  cat timp numar > 22:
    numar = numar - 22
  return numar
```

## Date necesare

- numele de familie relevant pentru linia de neam;
- genul persoanei: masculin / feminin;
- numele de familie anterior / schimbat, daca exista;
- numele de familie actual, daca exista;
- alfabetul numerologic pitagoreic documentat in
  `knowledge_base/calcule/nume/01-alfabet-numerologic.md`.

## Pasi de calcul

1. Se stabileste numele de familie relevant pentru analiza neamului.
2. Se normalizeaza textul.
3. Fiecare litera se transforma in valoarea numerologica.
4. Se aduna valorile literelor.
5. Daca rezultatul este mai mare de 22, se scade 22.
6. Daca rezultatul ramane mai mare de 22, se scade din nou 22.
7. Se repeta pana cand rezultatul este intre 1 si 22.

## Asociere cu Tarotul

- rezultatele 1-21 se citesc prin Arcanele Majore 1-21;
- rezultatul 22 se citeste ca Arcana Majora 0, Nebunul.

Interpretarile pentru neamurile 1-22 sunt documentate separat in
`03-interpretari-neam.md`.

## Reguli importante

- cand exista nume anterior / schimbat, bibliografia recomanda calculul pe
  numele de origine pentru linia de neam;
- cand exista doua nume de familie relevante, nu se exclude numele actual; se
  pastreaza si se interpreteaza ambele nume;
- pentru persoane adoptate, bibliografia recomanda numele de familie al tatalui
  biologic, daca analiza urmareste linia de sange;
- cand numele se schimba, influenta vechiului nume scade treptat, iar influenta
  noului nume creste treptat;
- numele de neam ramane relevant toata viata pentru mosteniri fizice, mentale,
  energetice si emotionale.
- interpretarile traditionale ale neamurilor se pastreaza ca definitii de baza,
  dar cand se scrie analiza concreta a unei persoane, termenii vechi se traduc in
  limbajul societatii actuale. De exemplu, `mestesugar` poate deveni, dupa
  context, profesionist tehnic, creator, designer, producator, specialist practic,
  artizan modern sau om care transforma o abilitate concreta intr-un serviciu
  util comunitatii.

## Adaptarea la contextul modern

Fisierul `03-interpretari-neam.md` pastreaza definitiile traditionale ale
neamurilor. Aceste definitii nu se altereaza cand sunt folosite ca baza de
documentatie.

In lucrarea unei persoane, insa, interpretarea trebuie adaptata la timpul si
societatea in care traieste persoana analizata. Ocupatiile vechi se traduc in
roluri moderne, fara a pierde sensul de baza al neamului. Astfel:

- negustorul poate deveni antreprenor, comerciant, manager, om de business;
- mestesugarul poate deveni specialist tehnic, designer, producator, creator,
  artizan modern sau profesionist cu abilitate practica;
- vindecatorul poate deveni medic, terapeut, psiholog, specialist in sanatate sau
  practician al metodelor complementare;
- invatatorul poate deveni profesor, trainer, mentor, educator, creator de
  continut educational;
- functionarul sau omul de curte poate deveni administrator, manager public,
  consultant, om de protocol, coordonator institutional;
- reprezentantul international poate deveni diplomat, specialist in relatii
  internationale, creator de brand cultural, sportiv sau artist cu vizibilitate
  globala.

Regula este: pastreaza radacina traditionala a neamului, dar exprima directia in
forme recognoscibile pentru viata moderna a persoanei.

## Nume anterior / schimbat si nume actual

Daca numele de familie se schimba, se calculeaza separat:

- numarul ereditar karmic de origine, pe numele de familie purtat inainte;
- numarul ereditar karmic actual, pe numele de familie purtat in prezent.

Daca exista nume anterior / schimbat si nume actual, interpretarea trebuie sa
explice ambele linii:

- numele anterior pastreaza neamul de origine;
- numele actual arata neamul social si familial activ;
- numarul ereditar karmic de sange, calculat pe numele de origine, persista
  intreaga viata si nu este anulat de schimbarea numelui;
- numarul actual arata influenta noului neam, contextul familial si social in
  care persoana intra.

Comparatia nu anuleaza numele de origine si nu exclude numele actual. Ea arata
diferenta dintre linia de neam din care persoana vine si linia de neam cu care
intra in relatie sociala sau familiala dupa schimbarea numelui.

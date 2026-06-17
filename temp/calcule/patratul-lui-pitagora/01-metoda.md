# Patratul lui Pitagora - metoda

Metoda porneste de la data nasterii si genereaza o serie de cifre care se aseaza
in matricea 3x3.

## Date necesare pentru matricea datei de nastere

- ziua nasterii;
- luna nasterii;
- anul nasterii.

Data se scrie numeric, fara separatori, in forma:

```text
ZZLLAAAA
```

Exemplu:

```text
24.04.1982 -> 24041982
```

## Cifre brute

Se iau toate cifrele din data nasterii, cu exceptia cifrei 0.

Exemplu:

```text
24041982 -> 2, 4, 4, 1, 9, 8, 2
```

Zero nu se introduce in matrice, dar ramane important in data ca loc, gol,
potential sau absenta explicita.

## Numere de lucru

Pentru proiect folosim patru numere de lucru.

### Numarul 1 de lucru

Se aduna toate cifrele datei de nastere.

```text
2 + 4 + 0 + 4 + 1 + 9 + 8 + 2 = 30
```

### Numarul 2 de lucru

Se reduce numarul 1 de lucru prin adunarea cifrelor sale.

```text
3 + 0 = 3
```

### Numarul 3 de lucru

Din numarul 1 de lucru se scade dublul primei cifre nenule din ziua nasterii.

Pentru ziua 24, prima cifra este 2.

```text
30 - (2 x 2) = 26
```

Pentru o zi de forma 07, prima cifra nenula este 7.

### Numarul 4 de lucru

Se reduce numarul 3 de lucru prin adunarea cifrelor sale.

```text
2 + 6 = 8
```

## Sirul complet de lucru

Se noteaza:

```text
data nasterii + numarul 1 + numarul 2 + numarul 3 + numarul 4
```

Exemplu:

```text
24041982 + 30 + 3 + 26 + 8
```

Cifrele care intra in matrice sunt:

```text
2, 4, 4, 1, 9, 8, 2, 3, 3, 2, 6, 8
```

Cifra 0 se elimina.

## Matricea datei de nastere

Folosim aceasta pozitionare:

```text
1 | 4 | 7
2 | 5 | 8
3 | 6 | 9
```

Pentru fiecare cifra aparuta, se adauga acea cifra in casuta corespunzatoare.
Daca cifra apare de mai multe ori, se repeta in aceeasi casuta.

Exemplu:

```text
1  | 44 |
222|    | 88
33 | 6  | 9
```

## Formula pentru implementare

```text
functie patratul_lui_pitagora(zi, luna, an):
  data = cifrele(zi, luna, an)
  n1 = suma(data)
  n2 = suma_cifrelor_pana_la_o_cifra(n1)
  prima_cifra_zi = prima_cifra_nenula(zi)
  n3 = n1 - 2 * prima_cifra_zi
  n4 = suma_cifrelor_pana_la_o_cifra(n3)

  sir = data + cifrele(n1) + cifrele(n2) + cifrele(n3) + cifrele(n4)
  sir_fara_zero = elimina_zero(sir)

  matrice = grupeaza_dupa_cifra(sir_fara_zero, 1..9)
  return matrice
```

## Reguli importante

- Zero nu se pune in matrice.
- Repetitia conteaza: `111` se interpreteaza diferit de `1`.
- Absenta conteaza: lipsa unei cifre nu este defect, ci tema de dezvoltare.
- Numerele de lucru se interpreteaza prin cifrele lor, nu ca numere independente.
- Matricea este instrument de citire simbolica, nu diagnostic psihologic.

## Matricea numelui

Matricea numelui se calculeaza separat fata de matricea datei de nastere.
Ea arata distributia expresiei prin nume, nu structura extrasa din data.

Date necesare:

- numele complet;
- alfabetul numerologic pitagoreic documentat in
  `knowledge_base/calcule/nume/01-alfabet-numerologic.md`.

Regula:

1. Se preia numele complet.
2. Se normalizeaza numele:
   - se transforma literele cu diacritice in litere de baza;
   - se ignora spatiile, cratimele si semnele de punctuatie;
   - se pastreaza doar literele.
3. Fiecare litera se transforma in valoarea numerologica 1-9.
4. Se calculeaza numarul de exprimare: fiecare componenta a numelui se reduce
   separat, apoi componentele reduse se aduna si se reduc la o cifra.
5. In matrice se introduc:
   - valorile literelor din nume si prenume;
   - numarul final de exprimare.

Cifrele intermediare ale componentelor reduse se folosesc doar pentru calculul
numarului de exprimare. Ele nu se introduc separat in matrice.

Valorile obtinute se aseaza in aceeasi matrice 3x3:

```text
1 | 4 | 7
2 | 5 | 8
3 | 6 | 9
```

Exemplu scurt:

```text
ANA POPESCU

ANA -> A=1, N=5, A=1 -> 7
POPESCU -> P=7, O=6, P=7, E=5, S=1, C=3, U=3 -> 32 -> 5
numar de exprimare -> 7 + 5 = 12 -> 3
```

Matricea numelui:

```text
111 |   | 77
    | 55|
333 | 6 |
```

## Citire comparativa

In profilul complet se pastreaza si se compara doua matrici:

- matricea datei de nastere;
- matricea numelui.

Nu se mai calculeaza o a treia matrice. Matricea datei de nastere si matricea
numelui raman doua surse separate: prima arata structura nativa, iar a doua arata
ce activeaza numele in dorinta, expresie si manifestare.

Regula de lucru:

1. Se calculeaza matricea datei de nastere.
2. Se calculeaza matricea numelui.
3. Pentru fiecare casuta 1-9 se compara cantitatea din matricea numelui cu
   cantitatea din matricea datei de nastere.
4. Daca matricea numelui depaseste matricea datei cu doua sau mai multe unitati
   in aceeasi casuta, cifra este considerata in exces in nume.
5. Excesul nu se adauga intr-o matrice noua. El se interpreteaza ca dorinta
   interioara a posesorului numelui de a fi mai mult pe tema acelei cifre decat
   ii este dat prin structura nativa.
6. Daca cifra este prezenta in matricea datei de nastere, dar lipseste din
   matricea numelui, cifra este considerata lipsa in nume. Lipsa arata impresia
   interioara ca omul are mai putin din acea caracteristica decat ii este dat
   prin datele native.
7. Daca diferenta este de zero sau de o singura unitate, cifra poate fi citita ca
   sustinere sau nuantare, nu ca exces major.
8. Daca cifra apare in nume, dar lipseste din data, se noteaza ca potential de
   nume fara suport direct in structura nativa.

Ele se compara prin:

- cifre dominante in data si in nume;
- casute sustinute: prezente si in data, si in nume;
- casute in exces in nume: numele depaseste data cu doua sau mai multe unitati;
- casute lipsa in nume: prezente in data, dar absente in nume;
- casute potential de nume: prezente in nume, dar absente in data;
- vectori activi in data fata de vectori activi in nume.

Formula simpla pentru comparatia pe casute:

```text
pentru fiecare cifra 1..9:
  data = numar_aparitii(cifra, matricea_datei_de_nastere)
  nume = numar_aparitii(cifra, matricea_numelui)
  diferenta = nume - data

  daca data == 0 si nume > 0:
    status = potential_de_nume_fara_suport_nativ
  altfel daca diferenta >= 2:
    status = exces_in_nume
  altfel daca data > 0 si nume > 0:
    status = sustinuta_sau_nuantata
  daca data > 0 si nume == 0:
    status = lipsa_in_nume
  daca data == 0 si nume == 0:
    status = absenta
```

## Interpretarea excesului in matricea numelui

Cand o cifra este in exces in matricea numelui, posesorul numelui isi poate dori
in interior sa fie mai mult pe tema acelei cifre decat ii este dat prin matricea
datei de nastere. Formularea trebuie facuta prudent: excesul nu este defect, ci
o presiune de exprimare a numelui, care poate cere constienta si masura.

- 1 in exces: omul isi doreste sa fie mai dominator, mai autoritar, mai lider,
  cu ego mai puternic decat ii este dat prin datele native.
- 2 in exces: omul isi doreste sa fie mai vorbaret, mai emotional, mai comunicativ
  decat ii este dat prin datele native.
- 3 in exces: omul isi doreste sa fie mai descurcaret, mai istet, mai bagat in
  seama si mai stimulat decat poate sustine natural.
- 4 in exces: omul isi doreste sa fie mai fit, mai sanatos si mai tonic decat ii
  este dat prin structura nativa.
- 5 in exces: omul isi doreste sa fie mai social, mai prietenos, mai increzator,
  mai aventuros si sa intre in mai multe experiente decat ii este dat.
- 6 in exces: omul isi doreste sa fie mai pragmatic, mai luxos, mai armonios in
  familie, mai senzual, mai iubitor.
- 7 in exces: omul isi doreste sa fie mai spiritual, mai rational, mai intelept,
  sa gandeasca in avans si sa analizeze mai profund decat poate sustine natural.
- 8 in exces: omul isi doreste sa fie mai bogat, sa faca parte din elite, sa aiba
  functii, grade sau pozitii mai inalte decat ii este dat prin structura nativa.
- 9 in exces: omul isi doreste sa fie mai aplecat catre ceilalti, pana la riscul
  de a uita de sine.

## Interpretarea lipsei in matricea numelui

Cand o cifra exista in matricea datei de nastere, dar lipseste din matricea
numelui, posesorul numelui poate trai in interior impresia ca are mai putin din
acea caracteristica decat ii este dat prin datele native. Lipsa nu inseamna ca
omul nu are calitatea respectiva; inseamna ca numele nu o activeaza explicit si
poate crea nesiguranta, neplacere sau dificultate in raport cu tema cifrei.

- 1 lipsa: puterea psihica nu este suficient de clara; omul poate simti ca nu
  stie destul de limpede ce vrea si ce ii face bine, iar acest lucru se rasfrange
  asupra increderii in sine.
- 2 lipsa: comunicarea se poate resimti in parteneriate, asocieri si relatii;
  omul poate simti ca legatura cu celalalt nu este suficient de usoara sau de
  fireasca.
- 3 lipsa: flexibilitatea se poate resimti prin senzatia ca nu a spus ce trebuie,
  ca ar fi putut formula mai bine sau ca ar fi putut actiona mai inspirat.
- 4 lipsa: organizarea se poate resimti asupra stabilitatii, trainiciei si
  rezultatelor muncii.
- 5 lipsa: schimbarea se poate resimti prin frica si neincredere fata de viitor.
- 6 lipsa: capacitatea de gestionare a conflictelor se poate resimti prin frica
  de angajare in relatii, frica de casatorie, frica de saracie si frica de a
  gestiona relatiile sau bunurile materiale.
- 7 lipsa: senzatia de a fi inteles si de a se face inteles se poate resimti prin
  frica de a fi inventiv, de a cerceta sau de a merge mai profund in analiza.
- 8 lipsa: capacitatea de a mentine echilibrul intre bani si familie se poate
  resimti prin frica de divort, frica de a nu putea iubi si frica de a nu fi iubit.
- 9 lipsa: interesul fata de cei din jur se poate resimti prin frica de a nu se
  putea dedica si de a nu putea fi devotat celor din jur.

## Concluzie pentru exces si lipsa in nume

In comparatia dintre matricea numelui si matricea datei de nastere, cifrele in
exces si cifrele lipsa se citesc impreuna, dar nu spun acelasi lucru.

Cifrele in exces arata ca posesorul numelui isi poate dori sa fie mai mult pe
tema acelei cifre decat poate sustine in realitate prin structura nativa. Ele
descriu o aspiratie, o presiune sau o imagine interioara de tipul `vreau sa fiu
mai mult decat imi este dat aici`.

Cifrele lipsa in nume arata ca persoana are doar senzatia ca are mai putin din
acea caracteristica decat are de fapt. Daca cifra exista in matricea datei de
nastere, calitatea este prezenta nativ; lipsa ei din nume nu o anuleaza, ci poate
crea impresia interioara ca acea resursa este mai slaba, mai greu de accesat sau
mai putin vizibila.

## Metoda pentru scara bunastarii

Scara bunastarii foloseste valorile casutelor si valorile vectorilor din matrice.

### Valoarea casutei

Valoarea unei casute se calculeaza ca suma cifrelor repetate in acea casuta.

```text
111 -> 1 + 1 + 1 = 3
66 -> 6 + 6 = 12
99999 -> 9 + 9 + 9 + 9 + 9 = 45
```

### Valoarea vectorului

Valoarea unui vector este suma valorilor celor trei casute care il formeaza.

```text
vectorul 3-6-9 = valoare(3) + valoare(6) + valoare(9)
```

### Ordinea de lucru

1. Se calculeaza valoarea fiecarei casute.
2. Se calculeaza valoarea fiecarui vector.
3. Se ordoneaza valorile de la cea mai mare la cea mai mica, cu zero separat.
4. Se citeste scara de sus in jos si de jos in sus.
5. Valorile egale se citesc ca teme care se sustin intre ele.
6. Valorile de jos determina valorile urmatoare.
7. Diferentele mari intre trepte se trec greu; diferentele mici se trec usor.

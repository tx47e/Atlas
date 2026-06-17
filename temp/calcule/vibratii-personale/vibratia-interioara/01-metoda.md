# Vibratia interioara - metoda

Vibratia interioara se calculeaza din ziua nasterii.

Formula adoptata pentru proiect:

```text
vibratia interioara = reducere_numerologica(ziua nasterii)
```

Exemple scurte:

- ziua 7 -> 7;
- ziua 24 -> 2 + 4 = 6;
- ziua 29 -> 2 + 9 = 11 -> 1 + 1 = 2, daca nu se pastreaza numerele maestre.

## Pasi de calcul

1. Se preia ziua din data nasterii.
2. Daca ziua este intre 1 si 9, rezultatul este chiar ziua.
3. Daca ziua are doua cifre, se aduna cifrele intre ele.
4. Daca rezultatul are in continuare doua cifre, se reduce pana la 1-9, cu exceptia cazului in care proiectul decide sa pastreze numerele maestre.

## Traseul de calcul

Rezultatul final este vibratia principala, dar formula completa trebuie pastrata
pentru interpretare. Cu cat reducerea are mai multi pasi, cu atat citirea devine
mai nuantata.

Exemplu:

```text
28 -> 2 + 8 = 10 -> 1 + 0 = 1
```

Interpretarea nu se face doar pe rezultatul final 1. Se citesc si:

- tensiunea sau cooperarea dintre 2 si 8;
- pragul intermediar 10;
- modul in care 1 se naste din 1 si 0;
- rezultatul final 1 ca directie principala.

Astfel, doua persoane cu vibratie interioara finala 1 nu sunt identice:

- ziua 1 are vibratia 1 directa;
- ziua 10 are 1 sustinut sau amplificat de 0;
- ziua 19 trece prin 1 + 9 = 10, apoi 1 + 0 = 1;
- ziua 28 trece prin 2 + 8 = 10, apoi 1 + 0 = 1.

Toate ajung la 1, dar traseul energetic este diferit.

## Regula numere maestre

Pentru implementarea initiala, rezultatul se reduce la 1-9.

Optional, se poate pastra si rezultatul intermediar pentru zilele 11, 22 si 29,
deoarece unele sisteme interpreteaza 11 si 22 ca numere maestre.

## Tabel rapid

| Ziua nasterii | Calcul | Vibratie interioara |
| --- | --- | --- |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | 1 + 0 | 1 |
| 11 | 1 + 1 | 2 |
| 12 | 1 + 2 | 3 |
| 13 | 1 + 3 | 4 |
| 14 | 1 + 4 | 5 |
| 15 | 1 + 5 | 6 |
| 16 | 1 + 6 | 7 |
| 17 | 1 + 7 | 8 |
| 18 | 1 + 8 | 9 |
| 19 | 1 + 9 = 10; 1 + 0 | 1 |
| 20 | 2 + 0 | 2 |
| 21 | 2 + 1 | 3 |
| 22 | 2 + 2 | 4 |
| 23 | 2 + 3 | 5 |
| 24 | 2 + 4 | 6 |
| 25 | 2 + 5 | 7 |
| 26 | 2 + 6 | 8 |
| 27 | 2 + 7 | 9 |
| 28 | 2 + 8 = 10; 1 + 0 | 1 |
| 29 | 2 + 9 = 11; 1 + 1 | 2 |
| 30 | 3 + 0 | 3 |
| 31 | 3 + 1 | 4 |

## Formula pentru implementare

```text
functie calculeaza_traseu(numar):
  pasi = []
  cat timp numar > 9:
    cifre = cifrele(numar)
    rezultat = suma(cifre)
    pasi.adauga({ intrare: numar, cifre: cifre, rezultat: rezultat })
    numar = rezultat
  return { vibratie_finala: numar, pasi: pasi }
```

Pentru vibratia interioara:

```text
return calculeaza_traseu(zi_nastere)
```

## Surse consultate

- Asociatia Numerologilor din Romania: ziua nasterii este prezentata ca vibratie interioara.
- DCNews / Corina Stratulat: exemplul 24.04.1982 reduce ziua 24 la 6 pentru vibratia interioara.
- Wikimanuale: vibratia interioara se obtine prin adunarea cifrelor din ziua de nastere.

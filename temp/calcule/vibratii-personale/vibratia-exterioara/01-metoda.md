# Vibratia exterioara - metoda

Vibratia exterioara se calculeaza din luna nasterii.

Formula adoptata pentru proiect:

```text
vibratia exterioara = reducere_numerologica(luna nasterii)
```

Exemple scurte:

- luna 4 -> 4;
- luna 10 -> 1 + 0 = 1;
- luna 12 -> 1 + 2 = 3.

## Pasi de calcul

1. Se preia luna din data nasterii, ca numar intre 1 si 12.
2. Daca luna este intre 1 si 9, rezultatul este chiar luna.
3. Daca luna este 10, 11 sau 12, se aduna cifrele intre ele.
4. Rezultatul final este vibratia exterioara.

## Traseul de calcul

Rezultatul final este vibratia exterioara principala, dar formula completa se
pastreaza pentru interpretare. Lunile 10, 11 si 12 au o nuanta diferita fata de
vibratiile directe 1, 2 si 3.

Exemple:

```text
10 -> 1 + 0 = 1
11 -> 1 + 1 = 2
12 -> 1 + 2 = 3
```

Astfel:

- luna 1 are o expresie exterioara 1 directa;
- luna 10 are tot rezultat 1, dar cu nuanta lui 1 + 0;
- luna 2 are o expresie exterioara 2 directa;
- luna 11 are rezultat 2, dar cu nuanta dublei energii 1;
- luna 3 are o expresie exterioara 3 directa;
- luna 12 are rezultat 3, dar cu nuanta relatiei dintre 1 si 2.

## Regula numere maestre

Pentru implementarea initiala, luna 11 se reduce la 2.

Optional, se poate pastra si rezultatul intermediar 11 pentru interpretare
extinsa, daca proiectul decide sa trateze numerele maestre.

## Tabel rapid

| Luna nasterii | Calcul | Vibratie exterioara |
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

Pentru vibratia exterioara:

```text
return calculeaza_traseu(luna_nastere)
```

## Surse consultate

- Asociatia Numerologilor din Romania: luna nasterii este prezentata ca vibratie exterioara/sociala.
- Zodiacool: cifra de vibratie exterioara se obtine prin adunarea cifrelor lunii de nastere.

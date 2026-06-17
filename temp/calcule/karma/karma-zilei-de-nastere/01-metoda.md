# Karma zilei de nastere - metoda

Sursa bibliografica: `bibliography/05 - Karma zilei de nastere.md`.

Ziua de nastere arata gradul in care sarcinile karmice au fost implinite si
tipul de lectie karmica pe care persoana o aduce in viata curenta. Interpretarea
se face prin Arcanele Majore si prin trecerea de la polaritatea negativa la
solutia sau calitatea care trebuie dezvoltata.

## Formula

```text
karma_zilei_de_nastere = ziua nasterii
```

Ziua nu se reduce numerologic la 1-9. Se pastreaza ziua calendaristica 1-31.

## Asociere cu Arcanele Majore

| Zi | Arcana karmica |
| --- | --- |
| 1-21 | Arcana 1-21 |
| 22 | Arcana 0 - Nebunul |
| 23 | Arcana 1 - Magicianul |
| 24 | Arcana 2 - Marea Preoteasa |
| 25 | Arcana 3 - Imparateasa |
| 26 | Arcana 4 - Imparatul |
| 27 | Arcana 5 - Marele Preot |
| 28 | Arcana 6 - Indragostitii |
| 29 | Arcana 7 - Carul |
| 30 | Arcana 8 - Puterea |
| 31 | Arcana 9 - Eremitul |

## Nivelul karmei implinite

| Zile | Karma implinita |
| --- | --- |
| 1-9 | spre 100% |
| 10-19 | spre 80% |
| 20-29 | spre 60% |
| 30-31 | spre 40% |

## Pasi de calcul

1. Se preia ziua nasterii.
2. Se identifica Arcana karmica asociata zilei.
3. Se identifica nivelul general al karmei implinite.
4. Se citeste tema zilei in bibliografie: polaritate negativa, solutie si cheie
   de lucru.

## Teme 1-22

| Karma | Zile | Arcana | Cheie de lucru |
| --- | --- | --- | --- |
| 1 | 1, 23 | Magicianul | lider, concentrare, transformarea orgoliului |
| 2 | 2, 24 | Marea Preoteasa | bunatate, ajutor, diplomatie, altruism |
| 3 | 3, 25 | Imparateasa | talente, expresie creativa, harnicie |
| 4 | 4, 26 | Imparatul | profesionalism, lege, generozitate, cumpatare |
| 5 | 5, 27 | Marele Preot | smerenie, intelepciune practica |
| 6 | 6, 28 | Indragostitii | familie, fidelitate, alegere matura |
| 7 | 7, 29 | Carul | stiinta, cercetare, credinta, intelect |
| 8 | 8, 30 | Puterea | putere interioara, control, responsabilitate |
| 9 | 9, 31 | Eremitul | cunoastere pusa in slujba celorlalti |
| 10 | 10 | Roata Norocului | folosirea corecta a oportunitatilor |
| 11 | 11 | Dreptatea | corectitudine, lege cauza-efect, responsabilitate |
| 12 | 12 | Spanzuratul | bunatate, sacrificiu, iluminare |
| 13 | 13 | Moartea | transformare, eliberare, renastere |
| 14 | 14 | Cumpatarea | masura, echilibru, recunostinta |
| 15 | 15 | Diavolul | cunoastere folosita corect |
| 16 | 16 | Turnul | constructie, impacare, bunastare comuna |
| 17 | 17 | Steaua | smerenie, stralucire meritata |
| 18 | 18 | Luna | onestitate, intuitie, creativitate folositoare |
| 19 | 19 | Soarele | inspiratie, libertate, putere responsabila |
| 20 | 20 | Judecata | apararea neamului, culturii si traditiei |
| 21 | 21 | Lumea | apararea patriei si valorilor nationale |
| 22 | 22 | Nebunul | libertate, relatia cu copiii, incredere in drum |

## Formula pentru implementare

```text
functie karma_zilei_de_nastere(zi):
  arcana = 0 daca zi == 22 altfel ((zi - 1) % 22) + 1
  procent =:
    1-9   -> "spre 100%"
    10-19 -> "spre 80%"
    20-29 -> "spre 60%"
    30-31 -> "spre 40%"
  return { zi, arcana, procent }
```

---
titlu: Registru validare formule
tip: registru
tags:
  - numerologie
  - validare
  - formule
---

# Registru validare formule

Acest registru este lista operationala pentru `scripts/calculator_numerologic_examen.py`. O formula nu devine sursa de calcul pentru lucrari noi pana cand nu are statutul `confirmata`.

Rularile de audit si modificarile de statut sunt consemnate cronologic in [[Istoric Rulari Validare Formule|istoricul validarilor de formule]].

| Domeniu | Formula / rezultat | Script agregat | Sursa documentara | Exemplu aprobat | Statut | Actiune urmatoare |
| --- | --- | --- | --- | --- | --- | --- |
| Karma | Karma zilei de nastere: `arcana = 0 daca zi == 22, altfel ((zi - 1) % 22) + 1`; procent: `1-9 -> spre 100%`, `10-19 -> spre 80%`, `20-29 -> spre 60%`, `30-31 -> spre 40%` | implementata in calculatorul agregat si copia din skill; Dashboard v1/v2 afiseaza arcana si procentul | `Karma din Ziua Nasterii.md` contine functia operationala completa | Daniel: zi `19` -> arcana `19`, procent `spre 80%`; teste de frontiera pentru `1`, `9/10`, `19/20`, `22/23`, `29/30`, `31` | confirmata | Pastreaza formula sincronizata in calculator, skill, Dashboard, template-uri si lucrari; nu introduce paranteze editoriale in calcul sau tabel. |
| Aspecte de indreptat | Solutia = suma cifrelor aspectelor de indreptat, aplicata exact o singura data | foloseste `reducere_numerologica(aspecte)`, care reduce repetat pana la o cifra | `Aspecte de Indreptat.md` cere in prezent reducere la o singura cifra si contrazice regula confirmata de utilizator | Daniel: 37 -> 10, nu 1; Andreea: 29 -> 11, nu 2; exemplul Vault 17 -> 8 nu distinge metodele | neconforma | Dupa aprobare separata, corecteaza Vault-ul, calculatorul agregat si copia din skill, testele, template-urile si lucrarile Daniel/Andreea in perechi Markdown/HTML. |
| Matrice | N2 = suma cifrelor lui N1, aplicata exact o singura data; N4 = suma cifrelor lui N3, aplicata exact o singura data | implementarea nu a fost revalidata in aceasta corectie documentara | `Cod Numerologic Personal.md`: insumare unica pentru N2 si N4 | Daniel: N1 = 39 -> N2 = 12; N3 = 37 -> N4 = 10; cod `19.02.1998.39.12.37.10` | confirmata | Revalideaza separat calculatorul, skill-urile, template-urile si lucrarile; nu modifica aceste surse in cadrul corectiei Vault. |
| Spirit | Codul Spiritului | reduce ziua + luna la 1-9 | `Codul Spiritului.md`: `CM = 55 - Zi - (2 x Luna)` | Daniel: 32 | neconforma | Valideaza formula Vault si apoi inlocuieste implementarea agregata; adauga zona, subetapa si varsta spiritului. |
| Spirit | Etape si subetape | de completat | `Codul Spiritului.md`: `((CM - 1) mod 13) + 1` | Daniel: subetapa 6 | neimplementata | Transcrie dupa confirmarea Codului Spiritului. |
| Spirit | Varsta Spiritului | partial | `Codul Spiritului.md`: `(CM - 1) x 189` plus varsta biologica | Daniel: 5.859 / 5.887 | neimplementata | Transcrie dupa confirmarea Codului Spiritului. |
| Soarta-Destin | Soarta, destin grafic, zona de confort | de completat | `Soarta si Destin.md` | Daniel: 3800196 / 3820176 | documentata, neimplementata | Implementeaza formula documentata si compara cu Daniel. |
| Relatii | Omuletul relatiilor | de completat in agregator | generatorul `numerologie-SVG-omuletul-relatiilor` | Daniel-Andreea | partial validata | Extrage aceleasi rezultate din generator in raportul agregat; nu duplica o formula diferita. |
| Ciclicitati | Subcicluri | de completat | de identificat in Vault | - | lipsa sursa operationala | Gaseste si valideaza documentatia inainte de implementare. |
| Ciclicitati | Ciclul de 27 ani | de completat | de identificat in Vault | - | lipsa sursa operationala | Gaseste si valideaza documentatia inainte de implementare. |
| Ciclicitati | Ani de criza si rascruce | de completat | de identificat in Vault | - | lipsa sursa operationala | Gaseste si valideaza documentatia inainte de implementare. |
| Ciclicitati | Interval complet de calcul | 0-108 ani pentru ciclurile 7/9/12 si anii importanti | cerinta operationala aprobata | Daniel | implementata | Pastreaza toate seriile in JSON; template-ul afiseaza numai selectia relevanta. |
| Ajutoare | Semnatura astrala | de completat | de identificat in Vault / skill | - | lipsa sursa operationala | Valideaza formula si sincronizeaza cu generatorul SVG. |
| Ajutoare | Directii de succes | partial | `Directiile de Succes.md` | - | de validat | Verifica ramura dependenta de gen si exemplele aprobate. |
| Nume | Cifra energetica | de completat | de identificat in Vault | - | lipsa sursa operationala | Documenteaza formula. |
| Nume | Cheile de bolta | de completat | de identificat in Vault | - | lipsa sursa operationala | Documenteaza formula. |
| Nume | Temperament | de completat | de identificat in Vault | - | lipsa sursa operationala | Documenteaza formula. |
| Nume | Cifre de tensiune | de completat | de identificat in Vault | - | lipsa sursa operationala | Documenteaza formula. |
| Sinteza | Tabel si grafic general | de completat | depinde de formulele confirmate | - | blocata | Construieste numai dupa confirmarea reperelor dependente. |

## Reguli de lucru

1. `confirmata` inseamna: formula, sursa Vault si cel putin un exemplu aprobat concorda.
2. `neconforma` inseamna: calculatorul nu poate furniza acea valoare pentru o lucrare noua.
3. `lipsa sursa operationala` inseamna: nu se inventeaza formula; se cere validare.
4. Dupa fiecare validare se actualizeaza in aceeasi schimbare calculatorul, skill-ul relevant, template-ul si testul de regresie.

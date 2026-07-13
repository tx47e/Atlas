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

| Domeniu | Formula / rezultat | Script agregat | Sursa documentara | Exemplu aprobat | Statut | Actiune urmatoare |
| --- | --- | --- | --- | --- | --- | --- |
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

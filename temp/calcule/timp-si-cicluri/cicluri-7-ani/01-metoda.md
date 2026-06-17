# Cicluri de 7 ani - metoda

Formula operationala curenta:

```text
ciclu 7 ani = floor(varsta / 7) + 1
pozitie in ciclu = varsta % 7 + 1
```

Ciclurile de 7 ani impart viata in etape recurente de cate sapte ani, pornind de
la varsta 0.

## Statut in proiect

La auditul bibliografiei nu a fost gasita o metoda explicita pentru ciclurile de
7 ani. Documentul `bibliography/11 - Lectii de viata si ciclul de 9 ani.md`
descrie ciclul de 9 ani, iar `bibliography/10 - Soarta si destin.md` descrie
grafice pe cicluri de 10 sau 12 ani.

Sursele web consultate prezinta ciclul de 7 ani ca ritm secundar de praguri de
varsta: `7`, `14`, `21`, `28`, `35` etc. In aceasta lectura, fiecare al saptelea
an poate marca o reasezare psihologica, corporala sau existentiala.

Prin urmare, formula de mai sus ramane o formula operationala folosita de
scripturi. Ea poate fi folosita ca strat suplimentar peste ciclul principal de 9
ani, dar nu il inlocuieste. Interpretarea trebuie tratata prudent si separata de
metodele validate intern pentru 9, 10 si 12 ani.

## Referinte externe

- Keen: `https://www.keen.com/articles/numerology-life-path/understanding-your-personal-7-year-numerology-cycle`
- Numerologist.com: `https://numerologist.com/numerology/cycles`

Exemplu:

```text
varsta 28
floor(28 / 7) + 1 = 5
28 % 7 + 1 = 1

persoana este in ciclul 5, anul 1 al ciclului
```

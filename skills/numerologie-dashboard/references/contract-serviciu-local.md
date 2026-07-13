# Contract pentru viitorul serviciu local

Prototipul v2 produce un `TaskManifest` JSON, dar nu executa operatii pe disc.

Serviciul local viitor va trebui sa:

1. valideze din nou manifestul si calea tinta;
2. refuze iesirea din radacina aprobata a proiectului;
3. creeze idempotent directorul lucrarii;
4. scrie manifestul si jurnalul de status;
5. lanseze Agent Dash numai dupa confirmarea validarii;
6. raporteze evenimentele inapoi fara a suprascrie datele utilizatorului;
7. nu includa `persoane.txt` sau date personale in publicare Git implicita.

`schemaVersion` initiala este `1.0`. Orice schimbare incompatibila necesita o versiune noua.


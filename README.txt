Questa è la traduzione italiana di "Dive Into Python 3", un libro che
parla di Python per programmatori esperti scritto da Mark Pilgrim e
pubblicato da Apress nel 2009. La traduzione italiana, intitolata
"Immersione in Python 3", è disponibile solamente online all'URL:

http://gpiancastelli.altervista.org/dip3-it

La traduzione del testo è completa.

La traduzione degli screenshot è incompleta per quanto riguarda le
installazioni di Python 3 su Mac OS X e Ubuntu Linux. Gli screenshot
su Mac OS X sono gli originali usati da Mark, in quanto non ho a
disposizione un computer Apple per poter documentare una installazione
"italiana" di Python 3. Gli screenshot su Ubuntu Linux sono incompleti
a causa di un problema che mi impedisce di collegarmi a Internet dopo
aver localizzato il sistema in italiano (la mia configurazione
predefinita è inglese) e che non sono riuscito a risolvere; quindi, i
tre screenshot che mostrano lo scaricamento dei pacchetti,
l'installazione del software e il riepilogo delle nuove applicazioni
installate sono in inglese. Notate che, in generale, né il programma
di installazione di Python (per esempio su Windows) né la Python
Shell (su tutti i sistemi operativi) sono localizzati in italiano,
e quindi le relative immagini mostrano (e mostrerebbero comunque) il
testo delle due interfacce in inglese.

La traduzione degli esempi di codice è stata fatta deliberatamente
solo per stringhe e commenti, in modo da adeguarsi a quella che sembra
essere la pratica comune nella pubblicazione di testi di informatica
tradotti dall'inglese all'italiano. (A ottobre 2009 gli esempi più
recenti sembrano essere "Effective Java", pubblicato da Pearson
Education, e "JavaScript: The Good Parts", pubblicato da Tecniche
Nuove.)

Nonostante il testo del libro sia stato scritto direttamente in
HTML, è necessario usare lo script publish per effettuare alcune
trasformazioni dei sorgenti (HTML, CSS, JavaScript) e infine
pubblicare in rete il risultato finale. Lo script usa i seguenti
strumenti:

- Python 2.6 e PyQuery (che necessita di lxml)
- Python 3
- Java (per YUI Compressor)
- Prince XML (http://www.princexml.com)
- Mercurial
- vari comandi Unix come cat, sed, zip, &c.

Lo script originale realizzato da Mark usa rsync per copiare i file
sul server finale, mentre il mio script usa FTP. Lo script originale
contiene anche alcune operazioni (il controllo sulla sintassi
JavaScript, l'aggiunta delle date di ultima modifica per ogni
capitolo, tanto per fare due esempi) che ho rimosso dal mio script
perché le ho giudicate inutili (in un senso molto generico del
termine) per il testo di una traduzione; il codice sorgente dello
script offre qualche motivazione specifica aggiuntiva nei commenti.

Tutto il materiale relativo alla traduzione è distribuito sotto
licenza CC-BY-SA 3.0. I dettagli delle singole parti (immagini,
esempi di codice, script di pubblicazione, &c.) si possono trovare
nel file informazioni-sul-libro.html. Per qualsiasi commento,
scrivete una email a <giulio.piancastelli@gmail.com>.


---

## 1. Netcat (`nc`)

Il comando `nc` (Netcat) è considerato il "coltellino svizzero" del networking: può gestire connessioni TCP, inviare pacchetti UDP, aprire socket Unix-domain, ascoltare su porte arbitrarie TCP/UDP, effettuare port scanning e supportare sia IPv4 che IPv6.
Una caratteristica fondamentale è che separa i messaggi di errore inviandoli sullo standard error anziché sullo standard output.

### Usi Comuni Principali
* Semplici proxy TCP
* Comunicazione interattiva tramite script shell tra client e server HTTP
* Test di rete e diagnostica

### Flag Principali di Netcat
* `-l` (listen): Mette il programma in ascolto su una specifica porta
* `-u` (UDP): Utilizza il protocollo UDP (il protocollo predefinito è TCP)
* `-v` (verbose): Rende l'output più dettagliato
* `-z` (zero-I/O): Utilizzato per il port scanning; controlla unicamente se una determinata porta è aperta
* `-p` (port): Specifica la porta sorgente da utilizzare
* `-N`: Chiude automaticamente la connessione di rete non appena riceve un EOF (End of File) dallo standard input
* `-C`: Converte automaticamente i caratteri di fine riga line feed (`
`) in carriage return + line feed (`
`), requisito essenziale per molti protocolli applicativi come HTTP

---

## Esercizi Svolti e Casi d'Uso con Netcat

### Esercizio 1: Connessione a un server HTTP con richieste non persistenti
Eseguiamo il comando specificando l'hostname e la porta (la porta 80 per HTTP):
```bash
nc -C art.uniroma2.it 80
```
* **Nota sui caratteri:** L'opzione `-C` converte i `
` in `
`, mentre i caratteri ricevuti non vengono mai trasformati [cite: 3]. `art.uniroma2.it` e `80` indicano rispettivamente l'hostname e la porta di destinazione [cite: 3].

Subito dopo l'avvio del comando, scriviamo (o incolliamo) e premiamo invio:
```http
GET / HTTP/1.1
Host: art.uniroma2.it
Connection: close
```
* **Connessione non persistente:** Avendo scelto la versione `1.1` di HTTP (che di default supporta le connessioni persistenti), l'intestazione `Connection: close` indica esplicitamente al server che desideriamo una connessione non persistente (chiusura immediata dopo la risposta)
* **Analisi della risposta HTTP:**
  * **Riga di stato:** Conferma una risposta positiva (`200 OK`)
  * **Server:** La risposta è stata generata dal proxy Nginx
  * **Date:** Riporta la data e l'ora esatta di generazione
  * **Content-Type:** I dati restituiti sono in formato HTML codificati in UTF-8
  * **Content-Length:** Indica la dimensione dei dati restituiti (es. 4673 byte)
  * **Connection: close:** Conferma che il server chiuderà la connessione
  * **Set-Cookie:** Il server ha generato un cookie `JSESSIONID` con un valore specifico (es. `89429FC9FAA5ED6A7BDEDF96C8DD203C`). Questo cookie può essere incluso nelle richieste per qualunque path sullo stesso host (attributo `Path`) e non è accessibile agli script in esecuzione nel browser (attributo `HttpOnly`)
* **Chiusura della connessione:** Se si fosse usata una connessione persistente, la combinazione `CTRL+D` non avrebbe fatto terminare il comando `nc`. In quel caso si sarebbe potuto usare `CTRL+C` oppure l'opzione `-N` (che chiude l'estremità della connessione quando lo standard input riceve EOF)

### Esercizio 2: Name-Based Virtual Hosting
1. Usiamo `nslookup` per determinare l'indirizzo IP dell'host `art.uniroma2.it`:
   ```bash
   nslookup art.uniroma2.it
   ```
   Prendiamo nota dell'indirizzo IP finale (es. `160.80.84.130`).
2. Eseguiamo Netcat direttamente sull'indirizzo IP:
   ```bash
   nc -CN 160.80.84.130 80
   ```
3. Scriviamo sulla console:
   ```http
   GET / HTTP/1.1
   Connection: close
   ```
   **Risultato:** Si otterrà una risposta `400 Bad Request` perché manca l'intestazione `Host`.
4. Facciamo `CTRL+D` e ripetiamo inviando l'intestazione `Host` corretta:
   ```http
   GET / HTTP/1.1
   Host: art.uniroma2.it
   Connection: close
   ```
5. Facciamo nuovamente `CTRL+D` e proviamo a cambiare l'hostname nell'header `Host`:
   ```http
   GET / HTTP/1.1
   Host: vocbench.uniroma2.it
   Connection: close
   ```
   **Risultato:** Si otterrà una risposta completamente diversa rispetto alla richiesta precedente. Questo dimostra che un singolo host fisico (con lo stesso indirizzo IP) ospita due domini differenti che conducono a siti distinti: è il principio del **Name-Based Virtual Hosting**.

### Esercizio 3: Sfruttare una connessione non persistente multipla
Apriamo la connessione:
```bash
nc -CN art.uniroma2.it 80
```
Inviamo in successione le richieste HTTP:
```http
GET / HTTP/1.1
Host: art.uniroma2.it

GET /fiorelli/ HTTP/1.1
Host: art.uniroma2.it
Connection: close
```

### Esercizio 4: Invio di richieste con Cookie
1. Invio di una richiesta base:
   ```bash
   nc -CN art.uniroma2.it 80
   GET / HTTP/1.1
   Host: art.uniroma2.it
   Connection: close
   ```
2. Ripetiamo l'azione includendo manualmente il cookie precedentemente rilasciato dal server:
   ```http
   GET / HTTP/1.1
   Host: art.uniroma2.it
   Cookie: JSESSIONID=BD80CEF81A80930D9387D06C586F2BCD
   Connection: close
   ```
   In risposta il server non restituirà un nuovo cookie, riconoscendo la sessione attiva.

### Esercizio 5: Richieste in Pipelining con Here Document
Per evitare risposte troppo lunghe e testare il pipelining (invio di più richieste in sequenza sulla stessa connessione TCP prima ancora di ricevere le risposte), usiamo il metodo `HEAD` combinato con un *Here Document* di Bash:
```bash
nc -C art.uniroma2.it 80 <<EOF
HEAD / HTTP/1.1
Host: art.uniroma2.it

HEAD /fiorelli/ HTTP/1.1
Host: art.uniroma2.it
Connection: close

EOF
```
* **Cos'è l'Here Document:** Permette di passare un blocco di testo multilinea a un comando senza creare file esterni o digitare le righe in modo interattivo, impacchettando richieste HTTP multiple in un sol colpo.

---

## 2. Il Comando Curl

`curl` è lo strumento standard per trasferire dati da o verso un server supportando svariati protocolli.

### Gestione dei dati binari
Se visualizziamo dati non ASCII (binari) direttamente nello standard output del terminale senza redirezione, rischiamo di corrompere/sputtanare la visualizzazione della console.

### Opzioni e Sintassi Principali
* `curl https://art.uniroma2.it/` — Stampa l'entità della risposta (la pagina HTML) sulla console.
* `-v` (verbose): Esegue curl mostrando in stdout l'entità della risposta e scrivendo su `stderr` le intestazioni inviate (precedute da `>`), le intestazioni ricevute (precedute da `<`) e le informazioni di servizio (precedute da `*`).
* **Redirezione di stdout e stderr su file separati:**
  ```bash
  curl -v https://art.uniroma2.it/images/ArtLogo.jpg > ArtLogo.jpg 2> verbose.txt
  ```
* `-o [file]` — Salva i dati ricevuti in un file con il nome specificato
* `-O` — Salva i dati in un file il cui nome viene derivato automaticamente dall'URL (non utilizzabile se l'URL termina con `/`)
* `--fail` (`-f`): Utile quando si richiede un file inesistente. Di default curl salva eventuali messaggi di errore o file vuoti; con `-f`, curl termina con un exit code diverso da zero (`22`) e senza scrivere output se il server risponde con errori `4xx` o `5xx`:
  ```bash
  curl --fail https://example.org/non-existing-bla
  ```
* `-L` — Segue automaticamente i reindirizzamenti HTTP (di default curl non li segue):
  ```bash
  curl -v -L https://art.uniroma2.it/fiorelli
  ```

### Gestione dei Cookie con Curl
* Usando l'opzione `-v` si nota che il server aggiunge sempre un nuovo cookie
* `-b` — Permette di specificare manualmente un cookie come coppia `chiave=valore` oppure di fornire un file di cookie formattato nello stile dell'header `Set-Cookie` o in formato Netscape/Mozilla
* `-c` — Permette a curl di scrivere i cookie ricevuti in un file
* Combinando `-b` e `-c` con lo stesso file, le richieste successive conterranno automaticamente il cookie generato dal server:
  ```bash
  curl -v -b cookie.txt -c cookie.txt https://art.uniroma2.it
  ```

### Metodi HTTP e Invio Dati (`-X`, `--data-urlencode`, `--data-binary`, `--form`)
* `-X [METHOD]` — Specifica il metodo HTTP della richiesta:
  ```bash
  curl -v -X POST http://httpbin.org/post
  ```
  Per il metodo `HEAD` anziché `-X HEAD` si preferisce l'opzione `-I` (o `--head`). Se si usa un metodo non supportato, il server risponde con `405 Method Not Allowed`.
* **Query string con caratteri speciali (Percent Encoding):**
  L'uso delle virgolette impedisce alla shell di interpretare caratteri speciali come `&`:
  ```bash
  curl "http://httpbin.org/get?title=C%26C&genre=real-time%20strategy"
  ```
* **Invio dati con `--data-urlencode` (POST):**
  Invia dati in formato `application/x-www-form-urlencoded` applicando la codifica URL in modo automatico. È il metodo usato dai moduli web classici (campi form nome, cognome, login):
  ```bash
  curl --data-urlencode "title=C&C" --data-urlencode "genre=real-time strategy" "http://httpbin.org/post"
  ```
  * `data-urlencode` fa il lavoro di conversione automatica (es. trasforma `C&C` in `C%26C`). Il server riceve il Content-Type corretto e inserisce i campi nella sezione form di httpbin.
* **Invio dati grezzi con `--data-binary`:**
  Invia dati con una POST senza alcuna interpretazione o codifica (es. un file di testo puro, un JSON o un'immagine)
  * Usando la chiocciola `@`, curl legge il contenuto del file e lo inietta nel corpo della richiesta
  * È necessario specificare esplicitamente il tipo di contenuto con l'header `-H "Content-Type: text/plain"` poiché non si tratta di coppie chiave-valore
* **Invio complesso con `--form` (o `-F`) — Multipart/form-data:**
  Il "coltellino svizzero" delle richieste POST quando occorre inviare contestualmente campi di testo e file multipli
  * La richiesta viene divisa in parti separate da una stringa univoca chiamata *boundary*
  * L'opzione va ripetuta per ogni campo
  * Sintassi avanzata supportata:
    * `@file`: Invia il file come allegato mantenendo il nome originale
    * `<file`: Legge il testo dal file e lo invia come valore del campo senza trasmettere il nome del file
    * `;type=`: Specifica manualmente il tipo MIME del file (es. `image/png`) se curl non lo riconosce automaticamente
  * **Esempio completo:**
    ```bash
    curl --form "titolo=dante" --form "file1=@bruti.txt" --form "file2=@bruti.txt;type=text/plain" --form "text=<bruti.txt" http://httpbin.org/post
    ```
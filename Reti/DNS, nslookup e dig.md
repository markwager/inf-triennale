---

---
---

## 1. Introduzione a Nslookup

Nslookup è una riga di comando per interrogare i nameserver DNS (Domain Name System).

### Sintassi e Modalità
```bash
nslookup [-option] [name | -] [server]
```

* **Modalità Interattiva:** Si attiva se non vengono dati argomenti o quando il primo argomento è `-` e il secondo è l'hostname o l'indirizzo IP di un nameserver
* **Modalità Non Interattiva (Standard):** Si attiva quando l'indirizzo IP o l'hostname da cercare è fornito direttamente come primo argomento. Restituisce solo il nome e l'informazione richiesta per un host o dominio.
* **File di configurazione:** Legge `/etc/resolv.conf`.

### Comandi Interattivi Principali
* `host [server]` - Cerca informazioni su un host
* `server domain` / `lserver domain` - Cambiano il DNS predefinito rispettivamente usando il server attuale o quello locale
* `exit` - Esce dal programma
* `set keyword[=value]` - Imposta varie opzioni di configurazione

---

## Esercizi Svolti con Nslookup

### Esercizio 1: Risoluzione di un dominio web
```bash
nslookup web.uniroma2.it
```
* **Cosa succede:** Ritorna l'indirizzo IP e il numero di porta del DNS server locale interrogato. Ci informa inoltre che la risposta ricevuta non è autoritativa e fornisce infine l'indirizzo IP del server autoritativo
* **Record cercati:** Di base cerca i record di tipo **A** (IPv4) e **AAAA** (IPv6)

### Esercizio 2: Interrogazione di un dominio inesistente
```bash
nslookup asdasdasdasd.uniroma2.it
```
* **Cosa succede:** Restituisce l'errore `NXDOMAIN` (Domain Name Non-Existent), indicando che il dominio cercato non esiste.

### Esercizio 3: Richiesta di record MX (Mail Exchange)
```bash
nslookup -type=MX uniroma2.it
```
* **Descrizione:** I record MX associano un nome di dominio a un servizio di posta elettronica. 
* **Priorità:** I valori dei record MX indicano l'ordine di preferenza tra più record MX associati allo stesso dominio. Il valore numerico più basso è quello da preferire. Il record MX serve per individuare l'hostname del server di posta SMTP.

### Esercizio 4: Risoluzione dell'hostname del server di posta
```bash
nslookup -type=A mx-01.uniroma2.it
```
* **Descrizione:** Interroga direttamente il record di tipo A per l'hostname del server mail precedentemente individuato.

### Esercizio 5: Simulazione manuale della risoluzione iterativa DNS
Nslookup mostra come un DNS resolver (o il server locale) risolve passo dopo passo un nome a dominio:

1. **Ricerca dei Root Nameserver (.):**
   Interroghiamo il resolver ricorsivo di Google come DNS locale per ottenere i nameserver della root zone (.):
   ```bash
   nslookup -type=NS . dns.google.com
   ```
   Ci vengono restituiti gli hostname dei 13 root nameserver logici. Scegliamo di usarne uno (es. il primo).

2. **Risoluzione dell'indirizzo del Root Server:**
   Il resolver DNS non ci ha fornito direttamente l'IP del root server, per cui facciamo un'ulteriore interrogazione:
   ```bash
   nslookup h.root-servers.net dns.google.com
   ```

3. **Avvio delle query iterative:**
   Contattiamo direttamente il root nameserver inviando una query non ricorsiva (`-norecurse`) e disabilitando la search list (`-nosearch`):
   ```bash
   nslookup -norecurse -nosearch -type=A web.uniroma2.it 198.97.190.53
   ```

4. **Analisi con -debug:**
   ```bash
   nslookup -norecurse -nosearch -debug -type=A web.uniroma2.it 198.97.190.53
   ```
   Osservando le sezioni `AUTHORITY` e `ADDITIONAL`, possiamo vedere il referral (il messaggio che indica a chi chiedere) dal root name server al TLD (`.it`). Gli elementi nella sezione `AUTH.` sono record NS per il dominio `.it`, mentre in `ADDITIONAL` troviamo i record A o AAAA corrispondenti

5. **Completamento della catena:**
   Ripetiamo la query inviandola al nameserver TLD restituito:
   ```bash
   nslookup -norecurse -nosearch -debug -type=A web.uniroma2.it 194.0.16.215
   ```
   Otteniamo così il referral al DNS server autoritativo per il dominio `uniroma2.it`, e interrogandolo direttamente risolviamo definitivamente l'hostname:
   ```bash
   nslookup -norecurse -nosearch -debug -type=A web.uniroma2.it 160.80.1.3
   ```
   *Nota:* In ogni passaggio passiamo l'hostname da risolvere all'indirizzo IP del DNS di competenza (prima root, poi TLD, infine autoritativo)

### Esercizio 6: Richiesta dei Name Server (NS) per domini e sottodomini
* Chiedere i nameserver autoritativi di un dominio:
  ```bash
  nslookup -type=NS uniroma2.it
  ```
* Fornendo un sottodominio, si ottiene una risposta differente che evidenzia l'esistenza del dominio padre e del relativo server DNS associato:
* nslookup -type=NS web.uniroma2.it

---

## 2. Il Comando Dig (Domain Information Groper)

`dig` è uno strumento potente e completo per interrogare i DNS nameserver, caratterizzato da un output molto più verboso rispetto a `nslookup`.

### Sintassi e Funzionamento
* Se non viene specificato un server, `dig` legge il file `/etc/resolv.conf` del computer
* Se digitato da solo nel terminale (senza argomenti né domini), interroga automaticamente i Root Server della radice (.)
* Permette di elaborare elenchi massivi di domini inseriti all'interno di un file
* Richiede di base il record di tipo A (visibile nella `QUESTION SECTION`) e mostra il protocollo di trasporto utilizzato nella `ANSWER SECTION`

---

## Esercizi Svolti con Dig

### Esercizio 7: Interrogazione base con Dig
Usiamo dig per chiedere al DNS ricorsivo di Google (`dns.google.com` o tramite IP `8.8.8.8`) di risolvere il dominio `uniroma2.it`:
```bash
dig @dns.google.com uniroma2.it
```

### Esercizio 8: Interrogazione con tipo ANY e analisi dei Flags
```bash
dig @dns.google.com uniroma2.it ANY
```
* **Sezione Flags:** Troviamo indicatori fondamentali quali `qr` (query/response), `rd` (recursion desired), `ra` (recursion available)
* **Statistiche di risposta:** Vengono mostrati il numero di query, le risposte (`ANSWER: 15`), i server autoritativi (`AUTHORITY: 0`) e le informazioni extra (`ADDITIONAL: 1`)
* **Significato dei Flag principali:**
  * **QR** (Query/Response): `0` se è una query, `1` se è una risposta
  * **AA** (Authoritative Answer): `1` se la risposta è creata da un server autoritativo
  * **TC** (Truncation): `1` se la risposta è stata troncata a causa dei limiti di dimensione del protocollo UDP
  * **RD** (Recursion Desired): `1` se la query è ricorsiva
  * **RA** (Recursion Available): `1` se il server supporta le query ricorsive

### Esercizio 9: Comportamento dei Root Server con hostname inesistenti
Se interroghiamo un root name server per un hostname inesistente, non viene restituito un errore immediato; ci viene fornito invece un referral al name server TLD appropriato. L'errore `NXDOMAIN` si ottiene solo interrogando (anche tramite resolver ricorsivo) il name server autoritativo finale:
```bash
dig @a.root-servers.net safsfasf.uniroma2.it
```

### Esercizio 10: Richiesta del record CNAME
Chiediamo il record CNAME (il soprannome/alias di un dominio) per `www.ibm.com`:
```bash
dig www.ibm.com CNAME
```

### Esercizio 11: Catena di Alias (CNAME e Record A)
```bash
dig www.ibm.com
```
* **Analisi:** La risposta contiene due record CNAME consecutivi (a formare una catena di alias) e culmina con il record A finale associato all'hostname canonico

### Esercizio 12: Test di propagazione GeoDNS con resolver regionali
Vogliamo risolvere il dominio `www.ibm.com` utilizzando differenti DNS resolver regionali per replicare test di propagazione geografica:
* **Paesi Bassi (resolver regionale):**
  ```bash
  dig +noall +answer @46.166.189.68 www.ibm.com
  ```
  Le opzioni `+noall +answer` nascondono tutto l'output superfluo mostrando esclusivamente le risposte. Tramite servizi di geolocalizzazione IP (es. KeyCDN), è possibile verificare che l'host rispondi da una specifica regione (es. Schiphol, Paesi Bassi).

### Esercizio 13: Risoluzione manuale con query non ricorsiva
Per ripetere la risoluzione "manuale" di un dominio escludendo la search list e imponendo query non ricorsive:
dig +nosearch +norecurse @dns.nic.it web.uniroma2.it

### Esercizio 14: Tracciamento automatico completo (+trace)
Il comando `dig` mette a disposizione l'opzione `+trace`, che automatizza esattamente il processo di risoluzione manuale attraverso la gerarchia dei DNS [cite: 2]:
```bash
dig +trace @1.1.1.1 web.uniroma2.it
```

---

## 3. Note Teoriche e Concetti Chiave sul DNS

* **DNS Resolver vs DNS Autoritativo:** Il server DNS locale che risponde a query ricorsive viene chiamato *DNS resolver*; in tutti gli altri casi si parla di server *autoritativo*.
* **Record multipli di tipo A e Load Balancing:** È possibile avere più resource record di tipo A associati allo stesso nome. Generalmente un'applicazione utilizza il primo, ma in caso di mancata risposta può ricorrere ai successivi. Il server DNS può permutarne l'ordine per bilanciare il carico, sebbene il caching dei resolver riduca l'efficacia di questa tecnica.
* **GeoDNS e Geographic Routing:** Restituire record A differenti in base alla distanza geografica del client permette il geographic routing. Poiché il DNS classico si basa sull'IP del resolver ricorsivo (che potrebbe trovarsi lontano dall'utente finale), esistono estensioni specifiche per ovviare a questo limite.
* **Vincoli sui Record:**
  * Un dominio non può possedere contemporaneamente resource record di tipo `CNAME` e di tipo `A` sullo stesso nome.
  * Un dominio può avere molteplici record di tipo `MX` (con valori di preferenza differenti; il client SMTP li valuta in ordine crescente) e molteplici record di tipo `NS`.
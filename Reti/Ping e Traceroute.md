
---

## 1. Il Comando Ping

`ping` è uno strumento di diagnostica di rete utilizzato per verificare se un dispositivo (host o router) è raggiungibile e per misurare le prestazioni della connessione.

### Funzionamento e Metriche
Alla base del suo funzionamento c'è il protocollo **ICMP**. `ping` invia pacchetti dati di tipo `ECHO_REQUEST` e attende un `ECHO_REPLY` dal destinatario.
* **RTT (Round Trip Time):** Il tempo impiegato dal pacchetto per raggiungere la destinazione e tornare indietro. `ping` misura questo tempo scrivendo un *timestamp* esatto nei primi 16 byte del campo dati di ogni richiesta. Al ritorno, confronta il timestamp con l'orologio attuale.
* **Jitter (mdev):** La deviazione standard dell'RTT. Indica quanto l'RTT è stabile nel tempo; un valore alto indica una rete instabile.
* **TTL (Time to Live):** Indica quanti router può attraversare il pacchetto prima di essere scartato, fornendo un'idea della "distanza" logica del destinatario.

### Struttura del Pacchetto Ping
Un pacchetto ping standard è composto da **84 byte totali**, così suddivisi:
* **56 byte** di dati (payload ICMP)
* **8 byte** di intestazione ICMP
* **20 byte** di intestazione IP

Quando il PC genera il messaggio ICMP, questo viene incapsulato in un datagramma IP. Nel campo `Protocol` dell'intestazione IP si troverà il valore **1**, che identifica per l'appunto il protocollo ICMP.

### Opzioni Principali
* `-c [numero]`: Invia solo il numero esatto di pacchetti specificato e poi si ferma.
* `-i [secondi]`: Modifica l'intervallo di tempo tra l'invio di un pacchetto e l'altro.
* `-w [secondi]`: Imposta un timer di autodistruzione globale (il comando si chiuderà dopo X secondi).
* `-W [secondi]`: Imposta il timeout di attesa per la risposta a un singolo pacchetto.
* `-s [byte]`: Cambia la dimensione del pacchetto inviato (di default 56 byte di dati).
* `-4` e `-6`: Forzano l'uso esclusivo del protocollo IPv4 o IPv6.
* `-f` (flood): Invia pacchetti a raffica il più velocemente possibile (attenzione: genera un carico di rete intenso).

### Dettagli Tecnici Cruciali (Exit Status e Allarmi)
`ping` è ideale per gli script bash poiché comunica il risultato tramite **exit status** (`echo $?`):
* `0`: Il dispositivo risponde (successo).
* `1`: Non c'è risposta (fallimento).
* `2`: Si è verificato un errore di altro tipo.

Inoltre, `ping` segnala se riceve pacchetti duplicati o danneggiati (spesso sintomo di un dispositivo guasto sulla rete).

---

### Esercizi Svolti con Ping

**Esercizio 1: Risoluzione base e Analisi Wireshark**
Eseguendo un ping standard (es. `ping -c 1 www.google.it`), la destinazione raggiungibile risponde con un `ICMP Echo Reply`. L'exit code (`echo $?`) sarà `0`.

**Esercizio 2: Forzare un fallimento manipolando i timer (`-c`, `-i`, `-w`)**
Unendo le opzioni di quantità, intervallo e scadenza, possiamo far fallire volontariamente il comando:
```bash
ping -i 1.495 -c 3 -w 3 www.google.it
```
* **Risultato:** Diciamo a ping di inviare 3 pacchetti distanziati di 1,495 secondi, ma con una deadline totale massima di 3 secondi. Il comando si spegnerà mentre il terzo pacchetto è ancora in volo, registrando una perdita del 33% e restituendo un exit status `1`.
Giocando con le opzioni `-i` e `-w` è possibile replicare lo scenario in cui l'ultima risposta non fa in tempo ad arrivare prima della chiusura del comando.

---

## 2. Il Comando Traceroute

`traceroute` è uno strumento diagnostico utilizzato per tracciare il percorso (i "salti" o *hop*) che i pacchetti IP compiono per viaggiare dal computer sorgente fino a un host di destinazione.

### Il "Trucco del TTL" (Come funziona)
1. Invia tre pacchetti sonda (di default) con **TTL = 1**.
2. Il primo router che riceve i pacchetti scala il TTL a 0. Avendo esaurito il tempo, il router scarta il pacchetto e invia indietro un messaggio di errore: **ICMP Time Exceeded**.
3. `traceroute` riceve l'errore, registra l'indirizzo IP del primo router e il tempo impiegato (Round Trip Time).
4. Invia un nuovo gruppo di pacchetti con **TTL = 2** per scoprire il secondo router, e così via, finché non raggiunge la destinazione finale o il limite massimo (default 30 salti).

Gli **asterischi (*)** nell'output indicano che non è stata ricevuta alcuna risposta per quel pacchetto sonda entro il tempo limite (timeout).

### Il Problema dei Firewall e i Protocolli supportati
Spesso i firewall bloccano i pacchetti UDP o ICMP standard, facendo fallire la tracciatura (si vedono solo asterischi). Per aggirare questo ostacolo, `traceroute` può usare diversi protocolli:
* **UDP (Default):** Invia pacchetti a porte di destinazione molto alte e improbabili (es. 33434+). Funziona bene internamente, ma spesso viene bloccato su Internet.
* **ICMP (`-I` o `-M icmp`):** Utilizza le stesse richieste `ECHO_REQUEST` del ping.
* **TCP (`-T`):** Il metodo migliore per superare i firewall. Invia un TCP SYN (solitamente porta 80 o 443). Usa una tecnica "half-open" per non disturbare le applicazioni reali sul server.

### Opzioni Principali
* `-4` / `-6`: Forza IPv4 o IPv6.
* `-n`: Disabilita la risoluzione DNS (non converte gli IP in nomi). Molto utile per velocizzare drasticamente l'esecuzione.
* `-m [numero]`: Imposta il numero massimo di salti prima di arrendersi (default 30).
* `-q [numero]`: Cambia il numero di pacchetti di test per ogni salto (default 3).
* `-p [porta]`: Specifica una porta di destinazione precisa (utile con `-T`).
* `-i [interfaccia]`: Forza traceroute a uscire da una specifica scheda di rete.

---

### Esercizi Svolti con Traceroute

**Esercizio 1: Analisi di un Traceroute UDP con Wireshark verso Google**
Eseguendo `traceroute www.google.it`:
* **Il percorso e gli Asterischi:** Il pacchetto impiega 10 salti. Nei salti 2, 5 e 8 compaiono degli asterischi `*`, poiché alcuni router o firewall hanno scartato i pacchetti di diagnostica per sicurezza o risparmio risorse.
* **L'anomalia dei tempi (RTT):** I tempi non crescono sempre in modo lineare (es. il salto 7 impiega ~11ms, mentre il 6 ne impiega ~20ms). Questo è dovuto al **ritardo di coda (queuing delay)**: se un router intermedio è momentaneamente congestionato, il pacchetto resta in coda, aumentando l'RTT di quel salto specifico rispetto a quelli successivi.
* **Arrivo a destinazione (Port Unreachable):** Wireshark mostra che il PC invia pacchetti UDP verso porte molto alte (es. 33443). Al decimo salto (Google), il server rileva un pacchetto diretto a una porta chiusa e risponde definitivamente con **ICMP Destination Unreachable (Port Unreachable)**. Questo è il segnale per `traceroute` che il viaggio è concluso.
* **Exit Status:** `echo $?` restituisce `0` (Destinazione raggiunta).
* *Nota tecnica Wireshark:* Il messaggio ICMP di errore include sempre i primi byte del pacchetto UDP originale, permettendo al PC di associare l'errore alla richiesta corretta (tramite ID pacchetto).

**Esercizio 2: Cambiare protocollo con `-M icmp`**
```bash
traceroute -M icmp www.google.it
```
Invece di UDP, forziamo l'uso di ICMP (come ping). I router intermedi risponderanno sempre con `ICMP TTL Exceeded`, ma l'host finale (Google) non risponderà più con l'errore di porta inesistente, bensì con una normale risposta **ICMP Echo Reply**.

**Esercizio 3: Limitare i salti con l'opzione `-m`**
```bash
traceroute -m 2 www.google.it
```
Stiamo imponendo al programma di fermarsi al massimo dopo 2 salti. Poiché Google dista 10 salti, il comando si interromperà bruscamente.
Controllando lo stato di uscita (`echo $?`), questa volta otterremo `1` (Errore/Incompleto).

---

## 3. Tabella Comparativa

| Caratteristica | `ping` | `traceroute` |
| :--- | :--- | :--- |
| **La domanda a cui risponde** | *"Ci sei? Quanto sei lontano?"* | *"Che strada devo fare per raggiungerti?"* |
| **Cosa ti mostra sul terminale** | Solo il tempo di viaggio totale verso la destinazione e se ci sono stati pacchetti persi. | L'indirizzo IP di **tutti i router intermedi** (salti) con i tempi di ogni singola tappa. |
| **Come funziona tecnicamente** | Invia pacchetti standard direttamente alla destinazione e aspetta la risposta. | Usa il "trucco del TTL" per forzare ogni router lungo la strada a rivelare la propria identità tramite errori ICMP. |
| **Quando si usa** | Controllo veloce: *"Non mi si apre una pagina web, la mia connessione funziona o il server è morto?"* | Indagine profonda: *"Internet funziona, ma il gioco online lagga da morire. In quale punto esatto c'è congestione?"* |
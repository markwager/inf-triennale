
L'API per le socket in Linux può operare in due modalità principali:
* **Bloccante** (modalità predefinita)
* **Non bloccante**

Utilizzando l'API in **modalità bloccante**, le system call per le socket ritornano il controllo al programma solo dopo il completamento dell'operazione, al verificarsi di un errore, oppure in caso di interruzione della system call per la cattura di un segnale.

---

## 1. Creazione e Configurazione Iniziale

### `socket`
Crea una nuova socket. *Nota: la socket appena creata non ha ancora un indirizzo locale associato.*
```c
int socket(int socket_family, int socket_type, int protocol);
```
* **`socket_family`**: Famiglia di indirizzi (es. `AF_INET` per IPv4, `AF_INET6` per IPv6).
* **`socket_type`**: Specifica la semantica della comunicazione:
  * `SOCK_STREAM`: Trasferimento affidabile e orientato alla connessione (TCP).
  * `SOCK_DGRAM`: Trasferimento a datagrammi, non affidabile (UDP).
* **`protocol`**: Specifica il protocollo (`IPPROTO_TCP` o `IPPROTO_UDP`).
* **Return**: Il File Descriptor (fd) della socket, oppure `-1` in caso di errore.

### Strutture per gli Indirizzi
* **`struct sockaddr`**: Struttura generica per gestire gli indirizzi di socket. Ogni famiglia utilizza una struttura specifica. Le socket `AF_INET` usano la struttura `sockaddr_in` (mentre `AF_INET6` usa `sockaddr_in6`), che contiene i campi `sin_family` (famiglia), `sin_addr` (indirizzo di rete) e `sin_port` (numero di porta). Per IPv6 i campi corrispondenti hanno il prefisso `sin6_`.
* **`struct sockaddr_storage`**: Struttura usata per definire variabili associate a un'area di memoria sufficientemente ampia e correttamente allineata, in grado di contenere in modo sicuro *qualsiasi* struttura di indirizzo di socket.

### `bind`
Assegna alla socket un indirizzo locale.
```c
int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen);
```
* **`sockfd`**: File descriptor della socket.
* **`addr`**: Puntatore alla struttura che rappresenta l'indirizzo da assegnare.
* **`addrlen`**: Lunghezza effettiva della struttura dell'indirizzo.
* **Return**: `0` in caso di successo, `-1` in caso di errore.

---

## 2. Connessione (Client e Server)

### `listen` (Lato Server)
Rende la socket passiva, ovvero utilizzabile per accettare richieste di connessione in ingresso.
```c
int listen(int sockfd, int backlog);
```
* **`backlog`**: Numero massimo di connessioni in attesa di essere accettate (coda di attesa).
* **Return**: `0` o `-1`.

### `accept` (Lato Server)
Preleva una connessione completamente stabilita dal *backlog* di una socket orientata alle connessioni (TCP), crea una *nuova* socket connessa per tale comunicazione e ne restituisce il file descriptor. La chiamata rimane bloccata finché non è disponibile una connessione da prelevare.
```c
int accept(int sockfd, struct sockaddr *restrict addr, socklen_t *restrict addrlen);
```
* **Return**: Il File Descriptor della nuova socket creata, o `-1` in caso di errore.

### `connect` (Lato Client)
Connette attivamente la socket all'indirizzo remoto specificato.
```c
int connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen);
```

---

## 3. Trasmissione e Ricezione Dati

### Lettura (`read`, `recv`, `recvfrom`)
Servono per leggere dati da una socket. In modalità bloccante, **si bloccano fintanto che il buffer di ricezione è vuoto** (in attesa di dati).

### Scrittura (`write`, `send`, `sendto`)
Servono per scrivere dati su una socket. In modalità bloccante, **si bloccano solo quando il buffer di trasmissione è pieno**.

### Differenza TCP vs UDP
* **TCP:** Tratta il flusso come una sequenza di byte continua. I dati presenti nel buffer possono essere letti anche in momenti successivi con più chiamate a `read`/`recv`. È responsabilità dell'applicazione riconoscere i limiti di dimensione dei messaggi logici (*framing*).
* **UDP:** Tratta i dati come datagrammi discreti. Il contenuto di un datagramma viene letto con una singola operazione, così come la scrittura. Se il datagramma eccede la dimensione del buffer di ricezione fornito dall'applicazione, i byte in eccesso vengono scartati.

---

## 4. Utilità, Conversioni e Opzioni

### Risoluzione Indirizzi (DNS/IP)
* **`getaddrinfo`**: Converte stringhe di nomi host e servizi in strutture di indirizzo di rete utilizzabili.
  ```c
  int getaddrinfo(const char *restrict node, const char *restrict service, const struct addrinfo *restrict hints, struct addrinfo **restrict res);
  ```
  * `node`: Nome dell'host, un indirizzo IP, o `NULL`.
  * `service`: Numero di porta in formato stringa, nome del servizio, o `NULL`.
  * `hints`: Puntatore a una struttura `addrinfo` usata come filtro di configurazione.
  * `res`: Puntatore a un puntatore per restituire la testa della lista concatenata dei risultati.
* **`freeaddrinfo(struct addrinfo *res)`**: Libera la memoria allocata dalla lista concatenata creata da `getaddrinfo`.
* **`getnameinfo`**: Fa l'opposto di `getaddrinfo`: traduce l'indirizzo di rete (contenuto in una struttura generica) nella rispettiva rappresentazione sotto forma di stringa (hostname/porta).

### Identificazione Socket
* **`getsockname`**: Restituisce l'indirizzo locale a cui è attualmente associata la socket (Ritorna `0` o `-1`).
* **`getpeername`**: Restituisce l'indirizzo remoto (del client o del server) a cui la socket è connessa (Ritorna `0` o `-1`).

### Conversione Endianness (Byte Order)
I sistemi host e la rete usano ordini di byte differenti (Little Endian vs Big Endian). Queste funzioni convertono i dati:
* `htonl` / `htons`: Converte da Host a Network (Big Endian) per `long` (32 bit) e `short` (16 bit).
* `ntohl` / `ntohs`: Converte da Network a Host (Local Endian).

### Conversione Indirizzi (Testo ↔ Binario)
* **`inet_pton`**: Converte una stringa IP testuale in un indirizzo di rete binario appropriato per l'address family.
  ```c
  int inet_pton(int af, const char *restrict src, void *restrict dst);
  ```
* **`inet_ntop`**: Converte una struttura binaria di indirizzo di rete in una stringa IP testuale.
  ```c
  const char *inet_ntop(int af, const void *restrict src, char dst[restrict .size], socklen_t size);
  ```

### Opzioni della Socket
* **`setsockopt`**: Imposta un'opzione specifica su una socket.
  ```c
  int setsockopt(int sockfd, int level, int optname, const void * optval, socklen_t optlen);
  ```
  * `level`: Livello dell'opzione (es. `SOL_SOCKET`).
  * `optname`: Identificatore dell'opzione (es. `SO_REUSEADDR`).
  * `optval`: Puntatore al valore da assegnare.
  * `optlen`: Lunghezza del buffer `optval`.
  * **Return**: `0` o `-1`.

---

## 5. Chiusura della Connessione

### `shutdown`
Chiude parzialmente o totalmente una connessione full-duplex, permettendo una chiusura più fine rispetto alla semplice `close()`.
```c
int shutdown(int sockfd, int how);
```
* **`how`**: 
  * `SHUT_RD`: Disabilita ulteriori operazioni di lettura.
  * `SHUT_WR`: Disabilita ulteriori operazioni di trasmissione (scrittura).
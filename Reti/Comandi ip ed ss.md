
---

## 1. Regole d'oro prima di operare sulle reti

Prima di eseguire comandi che modificano lo stack di rete, è fondamentale tenere a mente questi principi:
* **Ambiente Virtuale:** Fai sempre pratica su macchine virtuali per evitare di isolarti dalla rete o creare problemi di sicurezza sul tuo computer principale.
* **Modifiche Volatili:** I comandi `ip` applicano modifiche "a caldo" direttamente nel kernel. Al riavvio della macchina andranno perse. (Per renderle permanenti occorre agire sui file di configurazione del sistema operativo, come Netplan su Ubuntu).
* **Scorciatoie:** Nel comando `ip`, puoi abbreviare i prefissi di rete omettendo gli zeri meno significativi.
* **Backup delle Rotte:** Quando disattivi un'interfaccia, tutte le rotte a essa associate vengono eliminate automaticamente. Salva sempre la tabella di routing prima di spegnere un'interfaccia.

### ↳ Processo pratico: Spegnere e Riattivare un'interfaccia di rete
Dato che spegnere un'interfaccia fa perdere le rotte, il processo corretto per gestire il riavvio o la manutenzione dell'interfaccia è il seguente:
1. **Salva le rotte (Backup):** `ip route save > route.txt`
2. **Spegni l'interfaccia (Down):** `ip link set dev eth0 down`
3. **Riattiva l'interfaccia (Up):** `ip link set dev eth0 up`
4. **Ripristina le rotte (Restore):** `ip route restore < route.txt`

---

## 2. Il Comando `ip`

Il comando `ip` sostituisce i vecchi strumenti (`ifconfig`, `route`, `arp`) e si articola in vari sottocomandi per gestire i diversi livelli dello stack di rete.

### A. Gestione delle Interfacce (`ip link`)
Opera al **Livello Fisico (Layer 2)** e gestisce le interfacce fisiche o virtuali.

**Comandi e Filtri Principali:**
* `ip link` (equivale a `ip link show`): Elenca tutte le interfacce.
* `ip link show up`: Mostra solo le interfacce attualmente attive.
* `ip link show dev eth0`: Mostra solo i dettagli dell'interfaccia `eth0`.
* `ip -s link show dev eth0`: Mostra le statistiche di traffico dettagliate.

**Come leggere l'output di `ip link`:**
* `lo` / `eth0`: Nomi delle interfacce (Loopback locale vs interfaccia Ethernet).
* `<UP, LOWER_UP>`: `UP` indica lo stato amministrativo (l'interfaccia è accesa via software), mentre `LOWER_UP` indica lo stato operativo al livello fisico (es. il cavo di rete è effettivamente collegato).
* `mtu 1500`: Maximum Transmission Unit, la dimensione massima del pacchetto (tipicamente 1500 byte).
* `qdisc mq`: Politica di accodamento (es. code multiple per smistare i pacchetti).
* `link/ether 00:15...`: Indirizzo MAC fisico dell'interfaccia.
* `brd ff:ff...`: Indirizzo MAC utilizzato per i messaggi broadcast.

**Come leggere le Statistiche (`-s`):**
* `RX` / `TX`: Statistiche di ricezione (RX) e trasmissione (TX).
* `bytes` / `packets`: Quantità di dati passati con successo all'adattatore.
* `errors` / `dropped`: Pacchetti errati (es. CRC fallito) o scartati volontariamente prima della trasmissione.
* `collsns` / `carrier`: Collisioni sulla rete o errori per perdita del segnale fisico (portante).

### B. Gestione degli Indirizzi (`ip address`)
Opera al **Livello Logico (Layer 3)** e gestisce gli IP (IPv4 e IPv6) assegnati.

**Comandi e Filtri Principali:**
* `ip address` (oppure `ip addr` o `ip a`): Mostra tutti gli indirizzi.
* `ip address show scope global`: Filtra mostrando solo gli indirizzi con validità globale.
* `ip address show to 172.0.0.0/8`: Mostra solo gli IP appartenenti a questa specifica sottorete.

**Come leggere l'output di `ip address`:**
* `inet` / `inet6`: Indirizzo IPv4 o IPv6 affiancato dalla relativa subnet mask (es. `/20` o `/64`).
* `brd 172.21.255.255`: Indirizzo di broadcast di quella specifica sottorete.
* `valid_lft` / `preferred_lft`: Periodo di validità. Il valore `forever` indica che l'IP è statico o non scadrà.

**I 4 livelli di "Scope" (Ambito di validità dell'IP):**
1. `global`: L'indirizzo è instradabile su più reti (inclusi gli IP privati instradati dai router locali).
2. `site`: (Solo IPv6, deprecato) Valido solo all'interno di uno specifico sito aziendale/struttura.
3. `link`: Valido solo sulla rete locale diretta (LAN). Un router non innesterà mai questi pacchetti verso l'esterno.
4. `host`: Indirizzo valido solo per comunicazioni interne alla macchina stessa (es. loopback `127.0.0.1`).

### C. Gestione dell'Instradamento (`ip route`)
Opera al **Livello Logico (Layer 3)** gestendo le tabelle di routing.

**Comandi e Filtri Principali:**
* `ip route`: Mostra la tabella di routing principale (`main`).
* `ip route show dev eth0`: Mostra solo le rotte che escono dall'interfaccia `eth0`.
* `ip route show scope link`: Mostra le rotte dirette (senza router intermedi).

**Tipi di Instradamento:**
* **Diretto:** Es. `172.21.240.0/20 dev eth0 proto kernel scope link src 172.21.242.109`. Il destinatario è sulla stessa LAN. Manca la voce `via`. Il campo `src` indica quale IP usare come mittente.
* **Indiretto:** Es. `default via 172.21.240.1 dev eth0`. Usa il gateway per raggiungere reti esterne (es. internet).
* **`proto kernel` vs `static`:** `kernel` significa che la rotta è stata creata in automatico (es. collegando il cavo); `static` significa che è stata inserita manualmente dall'utente.

**Filtri di Ricerca Avanzata (`show to`):**
* `exact` (predefinito): Cerca l'esatto prefisso richiesto (es. `to 0.0.0.0/0`).
* `root`: Cerca una rotta specificando una sottorete e mostrando tutte le sottoreti che essa contiene (es. `root 172.0.0.0/8` mostrerà anche `172.21.240.0/20`).
* `match`: Cerca rotte uguali o più ampie ("genitore"). Utile per capire in quali macro-regole ricade un IP specifico (esattamente l'opposto di `root`).

**Il Simulatore di rotte (`ip route get`):**
* `ip route get 8.8.8.8`: Simula il routing per una destinazione usando la regola del *prefisso più lungo* (vince la regola più specifica). Mostra esattamente da quale interfaccia e da quale gateway passerà il pacchetto.

### D. Gestione Tabelle ARP (`ip neighbour`)
Fa da ponte tra L2 e L3, gestendo l'associazione tra IP logico e MAC fisico nella LAN.

**Comandi e Concetti Chiave (Incluso Flush):**
* `ip neigh`: Mostra la tabella ARP attuale.
* `ip neigh get 172.21.240.1 dev eth0`: Cerca un MAC specifico leggendo *esclusivamente* dalla memoria cache (non fa richieste ARP attive sulla rete in quel momento).
* **Svuotare la cache (Flush):** `ip neigh flush dev eth0` svuota l'intera cache ARP dell'interfaccia. 
  * *Tip:* Puoi usare il filtro `nud stale` (`ip neigh flush dev eth0 nud stale`) per cancellare selettivamente solo i record "vecchi/scaduti", mantenendo quelli attivi.

**Il trucco del Ping e Wireshark:**
Se fai un ping verso un IP esterno (es. `8.8.8.8`) e catturi il traffico, noterai che l'IP di destinazione nel pacchetto è `8.8.8.8`, ma l'indirizzo MAC di destinazione (a livello ethernet) è in realtà quello del tuo router di default (trovato interrogando l'ARP).

**Output di `ip neighbour`:**
Esempio: `172.21.240.1 dev eth0 lladdr 00:15:5d:10:bd:f1 REACHABLE`
* `lladdr`: Indica l'indirizzo MAC fisico.
* `REACHABLE`: È lo stato NUD (Neighbour Unreachability Detection). Indica che la macchina è stata vista di recente ed è attivamente raggiungibile.

### Riassunto Comandi `ip`
| Comando | Livello Rete | Cosa gestisce | Esempio Output Chiave |
| :--- | :--- | :--- | :--- |
| `ip link` | Fisico / Layer 2 | Interfacce fisiche e statistiche | `state UP`, `mtu 1500`, `RX bytes` |
| `ip address` | Logico / Layer 3 | IP assegnati, subnet, validità | `inet 10.0.0.5/24`, `scope global` |
| `ip route` | Logico / Layer 3 | Instradamento pacchetti, gateway | `default via 192.168.1.1` |
| `ip neighbour` | Ponte L2/L3 | Tabella ARP (Associazione IP-MAC) | `lladdr aa:bb:cc:dd`, `REACHABLE` |

---

## 3. Il Comando `ss` (Socket Statistics)

`ss` è lo strumento moderno per ispezionare le statistiche dei socket di rete in Linux. È il successore diretto del classico `netstat`, risultando molto più veloce e in grado di mostrare informazioni estremamente più dettagliate, specialmente riguardo ai protocolli TCP e agli stati interni delle connessioni.

### Statistiche Generali e Socket RAW (`ss -s`)
Il comando `ss -s` fornisce il numero totale di socket gestite dal kernel, suddividendo le statistiche per protocollo di trasporto (`UDP`, `TCP`, `RAW`, `INET`, `FRAG`).
* Specifica lo stato interno delle socket TCP, distinguendo in modo preciso tra connessioni `established`, `closed`, `orphan` o in `TIME_WAIT`.
* **Socket RAW:** Nelle statistiche figurano anche i socket RAW. Questi permettono di bypassare i classici protocolli di trasporto, consentendo allo sviluppatore di costruire manualmente il payload e, volendo, persino l'intestazione IP.

### Comportamento di Default e Output Base
Se lanciato senza alcun parametro, `ss` elenca esclusivamente le socket con connessione stabilita e **non in ascolto** (*non-listening*).
La tabella generata mostra:
* `Netid`: Tipo di socket/protocollo.
* `State`: Stato della connessione.
* `Recv-Q` / `Send-Q`: Numero di pacchetti attualmente fermi nelle code di ricezione e invio.
* `Local Address:Port` / `Peer Address:Port`: Indirizzi e porte locali e remoti.

### Opzioni a Riga di Comando
Le opzioni possono essere combinate insieme (es. `ss -tu` equivale a `ss -t -u`).
* `-l`: Mostra soltanto le socket in ascolto (*listening*).
* `-a`: Mostra congiuntamente sia le socket in ascolto sia quelle non in ascolto.
* `-n`: Evita di risolvere i nomi dei servizi (mostra i numeri di porta numerici al posto dei nomi tradotti da `/etc/services`).
* `-p`: Rivela il processo specifico che sta utilizzando la socket, aggiungendo nome dell'eseguibile, PID e file descriptor.
* `-i` (o `--info`): Mostra metriche interne e avanzate del protocollo TCP (algoritmo di congestione, finestra di congestione, tempi RTT medi, timeout di ritrasmissione).
* `-t`: Filtra mostrando solo socket TCP.
* `-u`: Filtra mostrando solo socket UDP.

### Sintassi Avanzata e Filtri
La sintassi completa del comando è:
```bash
ss [options] [ FILTER ]
```
Dove il `FILTER` si divide in due componenti opzionali: `[ state STATE-FILTER ] [ EXPRESSION ]`.

**1. Filtri di Stato (`STATE-FILTER`)**
Permettono di filtrare usando gli stati standard del TCP (`established`, `syn-sent`, `time-wait`) o tramite identificatori riassuntivi:
* `all`: Cerca in tutti gli stati possibili.
* `connected`: Cerca in tutti gli stati tranne in ascolto (`listening`) e chiusi (`closed`).
* `synchronized`: Cerca in tutti gli stati `connected` ad eccezione di `syn-sent`.
* `bucket` e `big`: Filtrano rispettivamente gli stati mantenuti come "minisocket" (es. `time-wait` e `syn-recv`) o l'esatto opposto.

**2. Espressioni (`EXPRESSION`)**
Consentono di applicare logica condizionale con operatori come `and` (implicito di default), `or`, `not`.
* **Destinazione/Sorgente IP:** `{dst|src} = HOST` testa la corrispondenza con l'indirizzo IP.
* **Destinazione/Sorgente Porta:** `{dport|sport} [OP] PORT` confronta le porte utilizzando operatori matematici al posto di `[OP]` (`<`, `<=`, `=`, `!=`, `>=`, `>`).
* **Porte Dinamiche:** Il predicato `autobound` serve a testare se una determinata porta è stata allocata dinamicamente dal sistema operativo.

**Note Sintattiche Cruciali (Wildcard e Apici):**
* Per IP (HOST) o porta (PORT) è possibile usare l'asterisco `*` come carattere jolly (*wildcard*).
* Quando si costruiscono query complesse che includono parentesi tonde o asterischi, **è indispensabile racchiudere tutta l'espressione tra apici singoli** per evitare che la shell (es. Bash) interpreti quei caratteri speciali in modo scorretto.
  *Esempio corretto:*
  ```bash
  ss -t 'dst = *:*'
  ```
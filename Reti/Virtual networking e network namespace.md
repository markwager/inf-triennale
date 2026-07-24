
In questo documento esploriamo l'implementazione del virtual networking in Linux, passando dalla creazione di una singola sottorete virtuale fino all'interconnessione di più sottoreti tramite router virtuali.

---

## 1. I Concetti Base del Virtual Networking

### Network Namespace (`netns`)
Un *network namespace* è un ambiente isolato che contiene un proprio stack di rete virtuale. Ogni namespace possiede le proprie interfacce di rete (fisiche o virtuali), i propri indirizzi IP e le proprie tabelle di instradamento.
* **Regola fondamentale:** Ogni interfaccia di rete può appartenere a **un solo** network namespace alla volta.
* Nelle topologie virtuali, ogni "Host" (es. hostA, hostB) viene rappresentato isolandolo all'interno di un network namespace differente.

### Dispositivi di Rete Virtuali in Linux
Il supporto al virtual networking include speciali dispositivi:
* **Bridge:** Si comportano in modo del tutto simile agli switch hardware a livello di collegamento (Layer 2).
* **Veth (Virtual Ethernet):** Vengono sempre creati in coppie (pair). Sono adattatori di rete Ethernet virtuali direttamente connessi tra loro come se fossero uniti da un cavo invisibile: quello che entra in una estremità esce istantaneamente dall'altra.

---

## 2. Creazione della Prima Sottorete (Esempio: Sottorete 10.0.1.0/24)

Immaginiamo una topologia base con uno switch centrale (`switch1`) e due host (`hostA` con IP 10.0.1.10 e `hostB` con IP 10.0.1.20).

### A. Gestione dei Network Namespace
* **Creazione:** 
  ```bash
  sudo ip netns add hostA
  ```
  *(Questo comando crea un nuovo namespace. Per il nuovo namespace viene creato anche un file speciale nel percorso `/run/netns/`).*
* **Enumerazione:**
  ```bash
  ip netns list
  ```
* **Cancellazione:**
  ```bash
  sudo ip netns del hostA
  ```
  *(Rimuove il file associato. Il namespace verrà distrutto solo quando non ci saranno più processi che lo utilizzano. Quando viene distrutto, le interfacce virtuali al suo interno spariscono, mentre quelle fisiche vengono riassegnate al namespace predefinito dell'host).*

### B. Creazione dei Collegamenti (Veth)
Aggiungiamo un collegamento virtuale tra l'host e lo switch:
```bash
sudo ip link add vethA type veth peer name vethA-switch1
```
*(Crea una coppia di interfacce: `vethA` che andrà nell'host e `vethA-switch1` che andrà collegata allo switch).*

Per distruggere un collegamento basta eliminare una delle due estremità:
```bash
sudo ip link del vethA
```

### C. Spostare i device nel Namespace
Prima di assegnare gli IP, spostiamo le estremità "lato host" nei rispettivi namespace:
```bash
sudo ip link set vethA netns hostA
sudo ip link set vethB netns hostB
```

### D. Creazione e Configurazione del Bridge (Switch Virtuale)
1. **Creazione del bridge:**
   ```bash
   sudo ip link add name switch1 type bridge
   ```
2. **Collegamento delle estremità Veth al bridge:**
   ```bash
   sudo ip link set vethA-switch1 master switch1
   sudo ip link set vethB-switch1 master switch1
   ```
3. **Attivazione delle interfacce e del bridge:**
   ```bash
   sudo ip link set switch1 up
   sudo ip link set vethA-switch1 up
   sudo ip link set vethB-switch1 up
   ```
*Nota: A differenza delle veth, il bridge NON può essere spostato in un network namespace isolato; deve rimanere nel namespace principale.*

### E. Esecuzione di comandi dentro il Namespace
Per configurare gli host, dobbiamo eseguire comandi "dentro" il loro namespace tramite `ip netns exec`:
* Per aprire un terminale interattivo nell'host: `sudo ip netns exec hostA /bin/bash` (per uscire, basta digitare `exit`).
* **Configurazione di hostA:**
  ```bash
  # Rinomina l'interfaccia vethA in eth0 per convenienza
  sudo ip netns exec hostA ip link set vethA name eth0
  
  # Assegna l'indirizzo IP e calcola il broadcast in automatico (grazie a "br +")
  sudo ip netns exec hostA ip address add 10.0.1.10/24 br + dev eth0
  
  # Attiva l'interfaccia eth0 e l'interfaccia di loopback (lo)
  sudo ip netns exec hostA ip link set eth0 up
  sudo ip netns exec hostA ip link set lo up
  ```

*Ricorda che queste modifiche non sono permanenti e andranno perse al riavvio della macchina (si usano script bash come `crea_prima_sottorete.sh` per automatizzarle).*

---

## 3. Topologia a Più Sottoreti e Router Virtuali

Se creassimo semplicemente tre sottoreti isolate (`10.0.1.0/24`, `10.0.2.0/24` e `10.0.3.0/24`), un tentativo di ping da `hostA` (10.0.1.10) a un host nell'altra rete restituirebbe un errore `Network is unreachable`. Serve un router.

### L'Architettura del Router Virtuale
Un router virtuale non è altro che un network namespace a cui vengono collegate più interfacce di rete (Veth) appartenenti a sottoreti diverse, con la funzionalità di "inoltro pacchetti" abilitata.
Ad esempio, interponendo `router1`, `router2` e `router3` tra gli switch, si creano delle mini-sottoreti di collegamento (es. `10.0.4.0/30` per collegare router1 e router2).

### Passaggi per la configurazione del Router (Esempio su `router2`):

1. **Creazione Namespace Router:**
   ```bash
   sudo ip netns add router2
   ```
2. **Creazione dei Veth di collegamento:** 
   Devono essere creati i cavi virtuali tra i router e i router/switch. I Veth lato router vengono spostati nel namespace del router.
3. **Assegnazione Indirizzi IP al Router2:**
   ```bash
   # Interfaccia verso la sottorete interna (switch2)
   sudo ip netns exec router2 ip address add 10.0.2.1/24 dev vethR2S2
   sudo ip netns exec router2 ip link set vethR2S2 up
   sudo ip netns exec router2 ip link set lo up
   
   # Interfaccia per collegarsi a router1 (rete 10.0.4.0/30)
   sudo ip netns exec router2 ip address add 10.0.4.2/30 dev vethR2R1
   sudo ip netns exec router2 ip link set vethR2R1 up
   
   # Interfaccia per collegarsi a router3 (rete 10.0.4.4/30)
   sudo ip netns exec router2 ip address add 10.0.4.5/30 dev vethR2R3
   sudo ip netns exec router2 ip link set vethR2R3 up
   ```
4. **Attivazione dell'IP Forwarding:**
   Un comando critico per permettere al router di "passare" i pacchetti da un'interfaccia all'altra (altrimenti si comporterebbe come un semplice host muto):
   ```bash
   sudo ip netns exec router2 sysctl -w net.ipv4.ip_forward=1
   ```
5. **Configurazione delle Rotte Statiche:**
   Bisogna dire a `router2` come raggiungere le sottoreti non direttamente connesse:
   ```bash
   # Per arrivare alla sottorete 1, passa da router1 (10.0.4.1)
   sudo ip netns exec router2 ip route add 10.0.1.0/24 via 10.0.4.1
   # Per arrivare alla sottorete 3, passa da router3 (10.0.4.6)
   sudo ip netns exec router2 ip route add 10.0.3.0/24 via 10.0.4.6
   ```

### Configurazione Default Gateway per gli Host
Infine, tutti gli host all'interno delle sottoreti devono sapere che, per comunicare con l'esterno della loro LAN, devono inviare il traffico al router:
```bash
# Esempio per l'hostA (nella sottorete 1)
sudo ip netns exec hostA ip route replace default via 10.0.1.1
```
*(Dove `10.0.1.1` è l'indirizzo IP dell'interfaccia del `router1` collegata allo `switch1`).*
# Scripting e Ambiente Bash

---

## 1. Variabili e Ambiente

### Variabili Locali e d'Ambiente
In Bash è possibile definire variabili per conservare informazioni durante la sessione.
* **Creazione/Assegnazione:** `nome="mario"` (Attenzione: non ci devono essere spazi vicino all'`=`).
* **Lettura:** Si utilizza il simbolo `$` prima del nome (es. `echo $nome`).
* **Scope:** Di default la variabile è *locale* alla shell in cui è stata creata. Usando il comando `set`, si possono visualizzare tutte le variabili locali.
* **Variabili d'Ambiente (`export`):** Per fare in modo che i programmi o gli script lanciati da questa shell possano "ereditare" e usare la variabile, bisogna esportarla: `export foo`.

### Variabili d'Ambiente Fondamentali (System Variables)
Sono variabili speciali gestite dal sistema che influenzano il comportamento della shell e dei programmi:
* **`PATH`**: È una delle variabili più importanti. Indica alla shell in quali directory (separate da `:`) cercare i comandi eseguibili (es. `ls`, `grep`) che l'utente digita. (Lettura: `echo $PATH`).
* **`HOME`**: Contiene il percorso della cartella home dell'utente attualmente connesso (es. `/home/valerio`).
* **`USER`**: Contiene il nome utente con cui è stato effettuato il login.

---

## 2. Il Filesystem e le Directory di Sistema

Tutte le directory su Linux derivano da un unico nodo padre (la **radice** `root` indicata da `/`). Non esistono concetti di "Unità disco" separate come `C:` in Windows.

Le cartelle principali di sistema:
* **`/bin`** (Essential binaries): Contiene i comandi e gli eseguibili essenziali richiesti per l'amministrazione e l'uso base del sistema per tutti gli utenti.
* **`/sbin`** (System binaries): Comandi essenziali di amministrazione (necessari per il boot o per modificare il sistema), solitamente eseguiti solo da utenti con permessi amministrativi.
* **`/boot`**: Contiene i file statici del boot loader necessari per l'avvio del sistema operativo (es. il Kernel).
* **`/etc`**: Ospita i file di configurazione specifici del sistema locale (nessun binario, solo testi di configurazione).
* **`/usr`**: File shareable e read-only (programmi, librerie, dati non necessari per il boot primario).
* **`/var`**: File contenenti dati che cambiano e variano nel tempo (log di sistema, database, ecc.).

---

## 3. Gestione di Script Bash

### Struttura ed Esecuzione
* È possibile eseguire un file bash passandolo all'interprete: `bash scriptname.sh`.
* **Lo Shebang (`#!`):** Se si inserisce nella primissima riga del file il path dell'interprete (es. `#!/bin/bash`), il sistema sa automaticamente quale interprete usare.
* Con lo shebang e i giusti permessi di esecuzione (`chmod +x script.sh`), è sufficiente lanciare lo script dal percorso in cui si trova: `./script.sh`.

### File di Configurazione della Shell
All'avvio o al login, Bash esegue specifici file per preparare l'ambiente:
* **`.bash_profile`**: Eseguito esclusivamente quando si avvia una shell di login.
* **`.bashrc`**: Eseguito ogni volta che viene aperta una nuova shell interattiva all'interno di una sessione.

---

## 4. Gestione Processi: Background, Foreground e Persistenza

La gestione dei job in Linux consente di eseguire più compiti contemporaneamente usando una singola finestra di terminale.

### Foreground (FG) e Background (BG)
* Lanciare un processo "dietro le quinte": Aggiungere la e-commerciale `&` alla fine del comando:
  `./script.sh &`
* **Sospensione processi:** Un processo attualmente in esecuzione (foreground) può essere sospeso temporaneamente inviando il segnale `SIGTSTP` tramite `CTRL+Z`. 
  * *Nota tecnica:* Non puoi sospendere con CTRL+Z un processo che è già in background. Se hai bisogno di sospendere un processo in background, dovrai inviargli un segnale specifico: `kill -STOP [PID]`.
* **Spostamento dei processi (Job Control):**
  * `jobs`: Elenca tutti i processi in background o sospesi legati alla shell corrente.
  * `bg [%id_job]`: Riprende in background l'esecuzione di un processo sospeso.
  * `fg [%id_job]`: Porta il processo dal background (o dallo stato sospeso) direttamente nel terminale principale (foreground).

### Analisi dei Processi Attivi
* `ps`: Fotografa i processi della shell attuale.
* `ps -e` o `ps -ef`: Mostra un'istantanea di *tutti* i processi del sistema (la `-f` dà informazioni dettagliate come l'UID e i PID dei genitori).
* `top`: Monitoraggio interattivo e continuo dei processi, utile per vedere quali software consumano più CPU.

### Kill e Terminazione
Per forzare la chiusura di un programma o inviare segnali, si usa il comando `kill`.
* Tramite **PID** (Process ID): `kill 2338`
* Tramite **Job ID**: `kill %1`
* Terminare tramite interfaccia: `CTRL+C` invia un segnale di interruzione forzata (`SIGINT`).

### Sessioni Persistenti (Nohup e Screen)
Di base, se si chiude un terminale (o cade la connessione SSH), tutti i processi avviati da quella shell vengono terminati.
* **`nohup` (No Hang Up):** Permette a un processo di ignorare la chiusura della shell. Spesso accoppiato con `&`.
  ```bash
  nohup ./processo.sh &
  ```
  *(L'output standard verrà rediretto automaticamente in un file chiamato `nohup.out`).*
* **`screen`:** Tool avanzato che crea sessioni terminale isolate e persistenti. Consente all'utente di lanciare un comando che richiede tempo, "staccare" (detach) il terminale, chiudere la connessione, e in futuro riaprire e ricollegarsi alla sessione per controllare lo stato.
  * Creazione: `screen -S nome_sessione`
  * Distacco (lasciando in esecuzione): `CTRL+A` seguito da `D` (oppure da un altro terminale `screen -d [id]`).
  * Lista sessioni attive: `screen -ls`
  * Riconnessione: `screen -r [id_o_nome]`
  * Chiusura definitiva: Digitare `exit` dentro lo screen, oppure forzare con `kill [id]`.

---

## 5. Permessi Utenti (Sudo e Chmod)

### Permessi sui File (Chmod)
Linux gestisce la sicurezza dei file dividendo i diritti in tre macro categorie: `u` (Owner/User), `g` (Group), `o` (Others), più `a` (All).
Per ognuna, esistono tre permessi: `r` (Read=4), `w` (Write=2), `x` (Execute=1).
* **Modifica testuale:** `chmod ugo+x file` (oppure `+x` a prescindere dal prefisso) rende un file eseguibile per chiunque. *Nota: Rendere eseguibile un banale file testo non ha alcuna utilità pratica, ma è consentito.*
* **Modifica Ottale:** Permette di riassegnare tutti i permessi in blocco. Es: `chmod 660 file.txt` assegna lettura e scrittura (4+2=6) sia all'Owner che al Gruppo, ma non garantisce alcun accesso agli Altri (0).

### Diritti di Amministrazione (`sudo` e `useradd`)
`sudo` permette a un utente autorizzato di operare provvisoriamente coi privilegi massimi di amministrazione (`root`).
* Esempio pratico: creazione di un nuovo utente con privilegi.
  ```bash
  sudo useradd -s /bin/bash -d /home/vivek/ -m -G sudo vivek
  sudo passwd vivek
  ```
  * `-s /bin/bash`: Stabilisce che la shell predefinita di questo account sarà Bash.
  * `-d /home/vivek/`: Specifica il percorso della home directory.
  * `-m`: Istanza la creazione effettiva della home directory sul disco.
  * `-G sudo`: Aggiunge il nuovo utente `vivek` al gruppo *sudo*, permettendogli di usare questo privilegio in futuro.
  * `passwd`: Assegna una password obbligatoria per proteggere il nuovo account.

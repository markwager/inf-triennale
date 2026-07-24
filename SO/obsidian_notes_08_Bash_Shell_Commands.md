# Appunti e Comandi Shell (Bash)

---

## 1. Comandi Base per Gestione File e Directory

### Navigazione e Ispezione
* **`ls`**: Elenca il contenuto della directory.
  * `-l`: Informazioni dettagliate (permessi, owner, dimensione).
  * `-a`: Mostra i file nascosti (quelli che iniziano con `.`).
  * `-lt`: Mostra i file ordinati per data di modifica (dal più recente).
  * `-lR`: Lista dettagliata ricorsiva (mostra anche i contenuti delle sottocartelle).
  * `-lS`: Mostra i file in ordine decrescente di dimensione.
  * `-lh`: Mostra la dimensione in formato leggibile (*human-readable*, es. KB, MB).
* **`cd`**: Cambia directory (usato da solo riporta alla `HOME`).
  * `..`: Porta alla cartella genitore.
  * `~`: Porta alla cartella `HOME` (es. `/home/valerio`).
* **`pwd`**: Mostra il percorso assoluto (*Print Working Directory*) della cartella corrente.
* **`echo`**: Stampa un messaggio o il contenuto di una variabile su standard output.
* **`cat`**: Mostra il contenuto di un file per intero.
  * `-n`: Aggiunge il numero a ogni riga.
  * `-b`: Aggiunge il numero solo alle righe non vuote.
* **`less`**: Pager che mostra un file "pagina dopo pagina" (ideale per file lunghi).
  * `-N`: Mostra i numeri di riga.
  * Comandi interni a less: `<` (inizio file), `>` (fine file), `q` (esci), `/parola` (cerca parola).
* **`tac`**: Mostra il contenuto di un file in ordine inverso (dall'ultima riga alla prima).
* **`od`**: Visualizza il file in formato grezzo (di default ottale).
  * `-d`: Decimale.
  * `-x`: Esadecimale.
* **`file`**: Mostra il tipo di file.

### Manipolazione (Creazione, Spostamento, Cancellazione)
* **`cp`**: Copia file e directory.
  * *Esempio:* `cp fileorig copiafile` oppure `cp fileorig path/`
  * `-r`: Copia ricorsivamente file e cartelle interne.
* **`mv`**: Muove o rinomina file e directory.
  * *Spostamento:* `mv file /path/to/destination`
  * *Rinomina:* `mv oldname newname`
* **`rm`**: Rimuove file o directory.
  * `-r`: Cancella una directory e tutto il suo contenuto ricorsivamente.
  * `-f`: Forza la cancellazione senza chiedere conferma.
* **`mkdir`**: Crea nuove directory.
  * `-p`: Crea la "parentela" (directory genitore e figlio assieme), es. `mkdir -p padre/figlio`.
* **`rmdir`**: Rimuove directory *esclusivamente* vuote.
* **`touch`**: Crea un file vuoto o aggiorna il timestamp (marca temporale) di un file esistente.
  * `-a`: Aggiorna il tempo di accesso.
  * `-m`: Aggiorna il tempo di modifica.
  * *Creazione rapida:* `touch dir1/prova.txt`.
* **`ln`**: Crea collegamenti (link).
  * *Hard Link:* `ln text.txt link_text.txt` (stesso inode, la modifica di uno cambia l'altro, non punta a directory).
  * *Soft Link (Simbolico):* `ln -s text.txt link_text.txt` (se il file originale viene cancellato, il link si rompe).

---

## 2. Elaborazione e Filtraggio Testo

* **`grep`**: Cerca un pattern testuale all'interno di file (supporta le *Regular Expressions*).
  * `-i`: Ignora differenza tra maiuscole e minuscole (*case insensitive*).
  * `-r`: Cerca ricorsivamente in tutte le sottodirectory.
  * `-v`: Trova le righe che **non** corrispondono al pattern.
  * `-w`: Cerca parole intere.
  * Esempi Regex:
    * `grep ^ciao file.txt` (righe che iniziano con "ciao").
    * `grep ciao$ file.txt` (righe che finiscono con "ciao").
    * `grep [0-9]\{3\} file.txt` (trova numeri a tre cifre).
    * `grep c\|g parole.txt` (Usa `\|` per l'operatore OR).
* **`awk`**: Linguaggio di scripting per scannerizzare e manipolare colonne di testo. Struttura: `awk pattern '{azione}'`.
  * `-F`: Imposta il separatore dei campi.
  * `-v`: Imposta una variabile.
  * `-f`: Imposta un file come origine del programma.
  * Esempi:
    * `awk -F, '{print $1}'` (stampa la prima colonna usando la virgola come separatore).
    * L'istruzione `END` si usa per compiere azioni al termine del comando. `$0` estrae la riga intera.
* **`sed`**: Modifica testo al volo.
  * `sed 's/old/new/' file.txt` (sostituisce "old" con "new").
  * `-i`: Salva le modifiche direttamente all'interno del file.
  * `-n`: Stampa solo righe specifiche (es. `sed -n 's/old/new/p' text.txt`).
* **`cut`**: Estrae specifiche porzioni dalle righe di un file.
  * `-f`: Seleziona uno specifico campo/colonna da stampare.
* **`sort`**: Ordina le righe di testo in un file.
  * `-r`: Ordine inverso.
  * `-n`: Ordina numericamente.
  * `-k [numero]`: Ordina in base a una colonna specifica.
* **`uniq`**: Elimina/filtra righe *consecutive* duplicate (spesso usato dopo `sort`).
  * `-c`: Conta il numero di occorrenze per ogni riga.
* **`wc`**: Conta linee, parole o caratteri in un file o nell'input.
  * `-l` (linee), `-w` (parole), `-c` (caratteri/byte).
* **`head`**: Mostra l'inizio del file (prime 10 righe di default).
  * `-n [numero]`: Mostra le prime N righe.
* **`tail`**: Mostra la fine del file (ultime 10 righe di default).
  * `-n [numero]`: Mostra le ultime N righe.
* **`diff`**: Confronta due file riga per riga e mostra le discrepanze. (Es: `n1cn2` cambia, `n1dn2` elimina, `n1an2` aggiungi).
* **`split`**: Divide un file in file più piccoli.
  * `split file.txt` (divide in file da 1000 righe di default).
  * `-l [numero]`: Divide in file da N righe.
* **`tr`**: Traduce/sostituisce o elimina caratteri (richiede input via pipe).
  * Esempio: `echo "a,b,c,d" | tr "," ";"` (restituisce "a;b;c;d").

---

## 3. Ricerca, Permessi e Utility di Sistema

### Ricerca Avanzata (`find`)
Cerca file nell'intero filesystem in base a criteri.
* `find ~ -name text.txt` (Cerca "text.txt" partendo dalla cartella HOME).
* `find . -name "*.txt"` (Cerca tutti i txt partendo dalla directory corrente).

### Archiviazione (`tar`)
Archivia/comprime cartelle e file. Sintassi generale: `tar [opzioni] nome_archivio file/cartella`
* `c`: Crea archivio.
* `v`: Verbose (mostra i file in elaborazione).
* `f`: Specifica il nome dell'archivio.
* `x`: Estrae l'archivio.
* `t`: Mostra il contenuto dell'archivio senza estrarre.

### Gestione Permessi (`chmod`)
Modifica i diritti d'accesso: Proprietario (`u`), Gruppo (`g`), Altri (`o`), Tutti (`a`).
Privilegi: Lettura (`r`=4), Scrittura (`w`=2), Esecuzione (`x`=1).
* *Notazione Simbolica:* `chmod ugo+x file` (o semplicemente `chmod +x file`) assegna permesso di esecuzione a tutti.
* *Notazione Ottale:* `chmod 660 file.txt` (Owner: r+w=6, Group: r+w=6, Others: 0).

### Processi e System Info
* **`ps`**: Mostra un'istantanea dei processi in esecuzione.
  * `-e`: Tutti i processi.
  * `-f`: Formato dettagliato.
  * `-u`: Processi per un utente specifico.
* **`kill`**: Invia segnali ai processi (es. per terminarli) tramite PID (`kill 2338`) o Job ID (`kill %1`).
* **`top`**: Monitoraggio dinamico dei processi e uso della CPU (aggiornato in tempo reale).
* **`whoami`**: Stampa il nome dell'utente corrente.
* **`w`**: Mostra chi è connesso e cosa sta facendo.
* **`hostname`**: Mostra il nome della macchina.
* **`date`** / **`cal`**: Mostrano data/ora e calendario.

### Controllo della Shell e History
* **`history`**: Mostra la cronologia dei comandi eseguiti.
  * `!!`: Riesegue l'ultimo comando.
  * `![numero]`: Esegue il comando N nella history.
  * `![stringa]`: Riesegue l'ultimo comando che inizia con "stringa".
* **Redirezione e Pipe (`>`, `>>`, `|`):**
  * `|`: Passa lo stdout di un comando come input del successivo (es. `ls | less`).
  * `>`: Sovrascrive (o crea) un file con lo stdout.
  * `>>`: Aggiunge (append) lo stdout in fondo al file.

### Guida e Manuale
* **`man [comando]`**: Apre il manuale completo del comando.
* **`[comando] --help`**: Riepilogo rapido sull'uso.

---

## 4. Variabili, Ambienti e Background Jobs

### Variabili Locali e d'Ambiente
* Dichiarazione: `nome="mario"` -> Lettura: `echo $nome`
* `set`: Mostra tutte le variabili locali della shell.
* `export var_name`: Trasforma una variabile locale in variabile d'ambiente, rendendola accessibile ai sottoprocessi avviati da quella shell.
* **Variabili d'ambiente principali:**
  * `$PATH`: Definisce le directory dove il sistema cerca gli eseguibili.
  * `$HOME`: Percorso della cartella utente corrente.
  * `$USER`: Nome dell'utente loggato.

### Il Filesystem Linux
La radice del filesystem è `/`. Non esistono concetti come i drive "C:" o "D:" di Windows.
* `/bin`: Eseguibili essenziali (binaries).
* `/sbin`: Eseguibili di sistema per amministratori.
* `/boot`: File statici del boot loader (kernel, ecc.).
* `/etc`: File di configurazione di sistema (host-specific).
* `/usr`: Librerie e software applicativo shareable e read-only.
* `/var`: Dati variabili nel tempo (log, cache, ecc.).

### Configurazione della Shell
Quando si apre un terminale o si fa login, bash legge dei file per impostare l'ambiente:
* `.bash_profile` (eseguito al login).
* `.bashrc` (eseguito ad ogni apertura di una nuova shell interattiva).

### Gestione dei Job (Foreground/Background)
* Lanciare in background: Aggiungere `&` alla fine del comando (es. `./script.sh &`).
* `jobs`: Elenca i processi attivi in background associati alla shell corrente.
* Sospensione: `CTRL+Z` sospende un processo attivo in primo piano (`SIGTSTP`). Per chiuderlo si usa `CTRL+C` (`SIGINT`).
* Ripresa: `bg [%id]` lo manda in background, `fg [%id]` lo riporta in primo piano (foreground).
* Nota: `kill -STOP [PID]` può sospendere forzatamente un processo in background.

### Persistenza (Nohup e Screen)
* **`nohup`**: Evita che un processo termini quando la shell che lo ha lanciato viene chiusa. Es: `nohup ./processo.sh &` (l'output finisce in `nohup.out`).
* **`screen`**: Gestore di sessioni. Permette di lanciare processi, staccarsi dalla finestra e ricollegarsi in un secondo momento.
  * `screen -S nome` (Crea sessione).
  * `screen -ls` (Elenca sessioni in esecuzione/staccate).
  * `screen -d [numero]` (Stacca/Detach senza chiudere).
  * `screen -r [numero]` (Ricollega/Resume).
  * `kill [numero]` (Chiude lo screen).

### Gestione Utenti (`sudo`)
`sudo` permette di eseguire comandi con i privilegi di root (amministratore).
* Aggiungere utente: `sudo useradd -s /bin/bash -d /home/vivek/ -m -G sudo vivek`
  * `-s`: imposta la login shell.
  * `-d` / `-m`: imposta la home e impone di crearla.
  * `-G sudo`: aggiunge l'utente al gruppo *sudo* (può ottenere permessi root).
* Cambiare password root: `sudo passwd vivek`.

---

## 5. Esercizi Bash Risolti

**Esercizio 2**
* a) Mostra le prime 3 righe: `head -n3 testo.txt`
* b) Mostra la 4^, 5^ e 6^ riga: `head -n6 animali.txt | tail -n3`
* c) Righe che NON contengono "domestico": `grep -v domestico animali.txt`
* d) Estrai la 3ª colonna (divisa da tab), cerca "selvatico" e conta le righe: `awk -F"\t" '{print $3}' animali.txt | grep selvatico | wc -l`
* e) Estrai la 2ª colonna, ordina, rimuovi duplicati, e conta: `awk -F"\t" '{print $2}' animali.txt | sort | uniq | wc`
* f) Righe "domestico", sort, remove dupes e conta linee: `grep domestico animali.txt | sort | uniq | wc -l`

**Esercizio 3**
* a) Filtra "Programmazione" e stampalo via awk: `grep Programmazione studenti.tsv | awk -F"\t" '{print $0}'`
* b) Come sopra ma conta: `grep Programmazione studenti.tsv | awk -F"\t" '{print $0}' | wc -l`
* c) Sostituisci "Sistemi" con "Sistemi Operativi": `sed s/Sistemi/Sistemi\ Operativi/ studenti.tsv`
* d) Stampa le righe in cui il 4° campo è >= 28: `awk -F"\t" '{if($4>=28)print $0}' studenti.tsv`
* e) Redirigi in un nuovo file: `awk -F"\t" '{if($4>=28)print $0}' studenti.tsv > studenti_top.tsv`

**Esercizio 4**
* a) Ordina e rimuovi duplicati consecutivi: `sort parole.txt | uniq`
* b) Conta quante volte compaiono le parole duplicate: `sort parole.txt | uniq -c`
* c) Trova la parola più frequente: `sort parole.txt | uniq -c | sort -n | tail -n1`
* d) Cerca "leone", ordina e conta: `grep leone parole.txt | sort | uniq -c`
* e) Cerca "ne": `grep ne parole.txt`
* f) Cerca "c" oppure "g": `grep c\|g parole.txt`

**Esercizio 5**
* a) Stampa la PATH: `echo $PATH`
* b) Conta quante direttrici sono nella PATH (separatore `:`): `echo $PATH | tr ":" "\n" | wc -l`
* c) Aggiungi un percorso alla PATH: `export PATH="$PATH/home/utente/mia_cartella"`
* d) Inizializza var e stampa: `NOME="valerio"` poi `echo $NOME`
* e) Esporta e verifica: `export nome` poi `printenv`

**Esercizio 6 (Gestione degli Errori e Stream)**
* a) Lista `/etc` e la directory inesistente `/pippo`: `ls /etc /pippo`
* b) Redirigi Standard Output su file di LOG e Standard Error su altro file: `ls /etc /pippo > log_DATA.txt 2> log_ERR.txt`
* c) Leggi i log: `cat log_DATA.txt` e poi `cat log_ERR.txt`
* d) Mostra le differenze: `diff log_DATA.txt log_ERR.txt`
* e) Concatena i due file in un file unico: `cat log_DATA.txt log_ERR.txt > log_TOT.txt`

**Esercizio 7 e 8 (Gestione Job e Background)**
* a) Lancia script multipli in background: `./countdown.sh 150 & ./countdown.sh 120 & ./countdown.sh 100 &`
* b) Sospensione con `CTRL-Z` (possibile solo se il processo è in Foreground).
  * Se il processo è in background e vuoi sospenderlo: `kill -STOP PID`.
* c) Uccidi il job numero 2: `kill %2`
* d) Manda il job 1 in background e il 3 in foreground: `bg %1` poi `fg %3`
* e) Trova i job: `jobs` e `ps -ef | grep countdown.sh`

**Esercizio 9 e 10**
* a) Lancia un processo immune alla chiusura del terminale: `nohup ./countdown.sh 12 &`
* b) Visualizza l'output salvato da nohup: `cat nohup.out`
* 10a) Conta tutti i processi aperti nel sistema: `ps -e | wc`
* 10b) Conta i processi associati all'utente root: `ps -e -u root | wc`

**Esercizio 11 e 15**
* 11a) Trova tutti i file testo da questa directory in poi: `find . -name '*.txt'`
* 11b) Trova i file di testo e cerca al loro interno escludendo la parola "ERROR": `find . -name "*.txt" | xargs grep -v "ERROR"`
* 15a) Crea un file vuoto e guardalo: `touch demo.txt` poi `ls -l`
* 15b) Modifica i permessi (aggiunge a utente/gruppo e revoca tutto agli others): `chmod u=rw,g=r,o= demo.txt`

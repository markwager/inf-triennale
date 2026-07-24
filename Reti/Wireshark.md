
Wireshark è un analizzatore di protocollo open-source, uno sniffer di rete che intercetta ed analizza in profondità il traffico dati.

---

## 1. Sicurezza e Scelta dell'Interfaccia

* **Ambiente di sicurezza:** Si consiglia fortemente di installare e utilizzare Wireshark all'interno di una Virtual Machine (VM) o di una sandbox per evitare di esporsi a vulnerabilità di sicurezza sulla macchina principale
* **Interfacce di rete (es. WSL2):** Se si utilizza l'applicazione all'interno di WSL2, l'interfaccia principale per il traffico esterno è solitamente `eth0`, mentre l'interfaccia `lo` (loopback) viene impiegata esclusivamente per il traffico interno alla macchina stessa.

---

## 2. Struttura dell'Interfaccia Gerarchica

L'interfaccia grafica si suddivide in tre pannelli gerarchici fondamentali:
1. **Packet List:** Mostra una riga di sintesi per ciascun pacchetto catturato in tempo reale o da file
2. **Packet Details:** Permette l'analisi dettagliata dei vari livelli del modello ISO/OSI. All'interno di questo pannello operano i *dissector*, moduli software specializzati nel "smontare" il pacchetto interpretando i diversi protocolli
3. **Packet Bytes:** Offre la rappresentazione a basso livello in formato esadecimale e ASCII puro dei dati grezzi contenuti nel pacchetto

---

## 3. Casi di Studio e Analisi dei Protocolli

### Caso A: Analisi DNS e il meccanismo del Referral
L'analisi prende come riferimento il comando di intercettazione `dig @a.root-servers.net art.uniroma2.it`, che interroga direttamente un root server saltando il resolver locale
* Applicando il filtro `dns` è possibile isolare rapidamente richieste e risposte 
* **Esame dei livelli nella richiesta:**
  * **Livello Ethernet (Collegamento):** Incapsulamento del frame sul mezzo fisico
  * **Livello IP (Rete):** Verifica degli indirizzi; controlla che l'IP sorgente corrisponda al proprio e quello di destinazione al root server. Il campo protocollo deve indicare UDP
  * **Livello Trasporto (UDP):** Utilizzo della porta standard `53`. Wireshark calcola la lunghezza del payload UDP sottraendo le intestazioni Ethernet e IP dal totale del frame
  * **Livello Applicativo (DNS):** Analizzando la risposta proveniente dal Root Server, si nota l'assenza di risposte finali (`no answers`). Al loro posto, la sezione *Authority* contiene record di tipo `NS` che implementano il meccanismo del **referral**, indicando al client di inoltrare la richiesta ai server di competenza per i TLD (es. `.it`)

### Caso B: Analisi di una richiesta POST complessa (`curl --form`)
Riprendendo l'esempio di invio dati complessi con `curl --form "titolo=dante" --form "file1=@bruti.txt" --form "file2=@bruti.txt;type=text/plain" --form "text=<bruti.txt" http://httpbin.org/post`, applichiamo il filtro `http` in Wireshark:
* **Analisi della gerarchia nel pacchetto:**
  * **Ethernet:** Gestione del frame locale
  * **IP:** Verifica che l'IP sorgente sia quello della propria macchina (verificabile con `ip addr`) e quello di destinazione corrisponda a `httpbin.org` (ottenibile tramite `nslookup` o `dig`)
  * **TCP:** Verifica che la porta di destinazione sia la `80` (porta standard HTTP in chiaro)
  * **TCP Reassembly:** Poiché la richiesta HTTP con i file allegati supera le dimensioni di un singolo pacchetto di rete, essa viene frammentata e trasmessa attraverso segmenti TCP multipli (es. 3 segmenti). Wireshark effettua automaticamente il *TCP Reassembly*, ricomponendo i pezzi per mostrare la richiesta HTTP integrale nel pannello dei dettagli
  * **HTTP (Livello Applicativo):**
    * La richiesta viene suddivisa in Intestazioni (*Headers*) e Corpo (*Body*)
    * **Multipart/form-data:** Osservando gli header si rileva il tipo di contenuto `multipart/form-data`, che indica l'invio contestuale di più parti separate da una stringa delimitatrice generata dal client chiamata *boundary*
    * Wireshark agevola l'ispezione combinando host e path per generare l'URL completo e fornendo un collegamento ipertestuale diretto al pacchetto contenente la risposta del server

### Strumento Utile: Follow HTTP Stream
Cliccando con il tasto destro su un pacchetto HTTP all'interno di Wireshark e selezionando **Follow > HTTP Stream**, si apre una finestra dedicata che ricostruisce interamente la conversazione testuale sequenziale tra client e server, rendendo immediatamente leggibili in un'unica schermata dati che altrimenti risulterebbero frammentati in decine di segmenti TCP distinti [cite: 10].

---

## 4. Filtri di Acquisizione e Visualizzazione Essenziali

I filtri sono indispensabili per isolare il traffico utile ed evitare di annegare nel rumore di fondo della rete

| Filtro                          | Scopo / Descrizione                                                       |
| :------------------------------ | :------------------------------------------------------------------------ |
| `dns`                           | Mostra esclusivamente il traffico di query e risposte DNS [cite: 10].     |
| `http`                          | Mostra unicamente il traffico HTTP in chiaro [cite: 10].                  |
| `tcp.port == 80`                | Filtra tutto il traffico transitante sulla porta standard web [cite: 10]. |
| `http.request.method == "POST"` | Isola in modo mirato l'invio di dati tramite form o API POST [cite: 10].  |

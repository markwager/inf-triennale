# Capitolo 5: Funzioni di Hash e Autenticazione dei Messaggi

Nei capitoli precedenti abbiamo studiato i crittosistemi simmetrici (a blocchi e a flusso), il cui obiettivo primario è garantire la **confidenzialità** (*secrecy*): impedire a un avversario passivo (Oscar) di leggere il contenuto di un messaggio in chiaro $x$ intercettando il testo cifrato $y$.

Tuttavia, come già anticipato nel Capitolo 1 e dimostrato drammaticamente dal *Padding Oracle Attack* (Sezione 4.7.1), la sola confidenzialità **non protegge l'integrità dei dati né l'autenticità dell'origine**: un avversario attivo può intercettare un messaggio in transito, alterarne i bit o forgiare un messaggio completamente nuovo fingendosi Alice.

Il **Capitolo 5** introduce i due strumenti crittografici fondamentali progettati per garantire l'**integrità dei dati** e l'**autenticazione del messaggio**:
1. **Funzioni di Hash Crittografiche (*Cryptographic Hash Functions*, Sezioni 5.1–5.4):** Funzioni pubbliche (prive di chiave) che comprimono un messaggio di lunghezza arbitraria in una breve impronta digitale (*message digest*) di lunghezza fissa.
2. **Codici di Autenticazione dei Messaggi (*Message Authentication Codes - MAC*, Sezione 5.5):** Funzioni dotate di una chiave segreta condivisa $K$ che producono un *tag di autenticazione*, culminando nei moderni schemi di **Crittografia Autenticata (*Authenticated Encryption*)** come la modalità **Galois/Counter Mode (GCM, Sezione 5.5.3)**.

---

## 5.1 Funzioni di Hash e Integrità dei Dati

Una funzione di hash crittografica può essere pensata informalmente come un'operazione che prende in ingresso una stringa di dati di lunghezza arbitraria (un file, un'email, una password, una transazione) e la "compatta" in un'impronta binaria di dimensione fissa e ridotta, chiamata **message digest** (o *hash value* / *impronta*).

Nella letteratura crittografica esistono due grandi categorie di funzioni di hash:
* **Funzioni di hash con chiave (*Keyed hash functions*):** Richiedono una chiave segreta $K$ e vengono utilizzate direttamente per costruire i **MAC** (*Message Authentication Codes*).
* **Funzioni di hash senza chiave (*Unkeyed hash functions*):** Non utilizzano alcuna chiave segreta (oppure si può pensare che la chiave sia fissata e pubblica). Quando si parla semplicemente di *"funzione di hash"* (come SHA-256 o SHA-3), ci si riferisce sempre a una funzione **senza chiave**.

---

### 5.1.1 Definizione Formale di Famiglia di Hash (con e senza chiave)

Stinson introduce una definizione matematica unificata (le *famiglie di hash*) che comprende sia il caso con chiave (MAC) sia il caso senza chiave:

> [!abstract] Definizione 5.1: Famiglia di Hash (Hash Family)
> Una **famiglia di hash** è una 4-tupla $(\mathcal{X}, \mathcal{Y}, \mathcal{K}, \mathcal{H})$ che soddisfa le seguenti proprietà:
> 1. $\mathcal{X}$ è un insieme di possibili **messaggi** (*messages*).
>    * $\mathcal{X}$ può essere un insieme finito (di cardinalità $N = |\mathcal{X}|$) oppure infinito (ad esempio $\mathcal{X} = \{0, 1\}^*$, l'insieme di tutte le stringhe binarie di lunghezza finita arbitraria).
> 2. $\mathcal{Y}$ è un insieme **finito** di possibili **message digest** (o *authentication tags*), di cardinalità $M = |\mathcal{Y}|$.
> 3. $\mathcal{K}$, lo **spazio delle chiavi** (*keyspace*), è un insieme finito di possibili chiavi.
> 4. Per ogni chiave $K \in \mathcal{K}$, esiste una funzione di hash $h_K \in \mathcal{H}$. Ciascuna $h_K$ è una funzione:
>    $$h_K : \mathcal{X} \longrightarrow \mathcal{Y}$$

* **Condizione di Compressione:**
  Se $\mathcal{X}$ è un insieme finito con $|\mathcal{X}| = N$ e $|\mathcal{Y}| = M$, si richiede sempre che $N \ge M$, e nelle applicazioni pratiche vale quasi sempre **$N \gg M$** (ad esempio $N \ge 2M$). Per questo motivo, una funzione di hash a dominio finito viene spesso chiamata **funzione di compressione** (*compression function*).
* **Notazione:**
  * Coppia $(N, M)$-hash family: una famiglia di hash in cui $|\mathcal{X}| = N$ e $|\mathcal{Y}| = M$.
  * **Funzione di hash senza chiave (*Unkeyed Hash Function*):** Corrisponde al caso particolare in cui lo spazio delle chiavi contiene un solo elemento, cioè **$|\mathcal{K}| = 1$**. In tal caso esiste un'unica funzione pubblica che denotiamo semplicemente con:
    $$h : \mathcal{X} \longrightarrow \mathcal{Y}$$
    Tipicamente, in una funzione di hash senza chiave standard, il dominio è $\mathcal{X} = \{0, 1\}^*$ (o tutte le stringhe binarie fino a una lunghezza massima enorme, es. $2^{64}-1$ bit) e il codominio è $\mathcal{Y} = \{0, 1\}^m$ per un intero fisso $m$ (es. $m = 256$ o $m = 512$ bit), per cui $M = |\mathcal{Y}| = 2^m$.

---

### 5.1.2 Come si Garantisce l'Integrità dei Dati? (Con Chiave vs Senza Chiave)

Supponiamo che Alice voglia inviare un messaggio $x \in \mathcal{X}$ a Bob assicurandosi che Oscar non possa alterarlo durante il transito. Vediamo la differenza cruciale tra l'uso di una funzione **con chiave (MAC)** e una **senza chiave**:

#### Caso 1: Uso di una Funzione con Chiave (MAC su canale insicuro)
1. Alice e Bob condividono in anticipo una **chiave segreta $K \in \mathcal{K}$** (ignota a Oscar).
2. Quando Alice vuole trasmettere il messaggio $x$, calcola il tag $y = h_K(x)$ e invia sul canale insicuro la coppia **$(x, y)$**.
3. Bob riceve una coppia $(x', y')$ (eventualmente modificata da Oscar), calcola autonomamente $h_K(x')$ usando la chiave segreta $K$ e verifica se:
   $$y' \stackrel{?}{=} h_K(x')$$
   * Se l'uguaglianza è verificata, Bob accetta il messaggio come **valido e autentico** (`VALID`).
   * Se $y' \neq h_K(x')$, Bob rileva la manomissione e **rifiuta** il messaggio (`INVALID`).
* **Perché funziona?** Poiché Oscar **non conosce la chiave segreta $K$**, se modifica il messaggio $x$ in un nuovo messaggio $x' \neq x$, non è in grado di calcolare il nuovo tag valido $y' = h_K(x')$.

#### Caso 2: Perché una Funzione di Hash SENZA Chiave da sola NON protegge un canale insicuro!
Cosa succederebbe se Alice e Bob cercassero di usare una funzione di hash **senza chiave** $h$ (pubblica) nello stesso modo, inviando $(x, y = h(x))$ su un canale insicuro senza alcuna chiave segreta?
* **Fallimento totale contro un avversario attivo:** Oscar intercetta $(x, y)$, butta via $x$, scrive un messaggio falso a suo piacimento $x'$ (es. *"Bonifica 10.000€ a Oscar"*), **calcola lui stesso il nuovo digest $y' = h(x')$** (può farlo benissimo perché la funzione $h$ è pubblica e non ha chiave!) e invia $(x', y')$ a Bob. Bob controlla $y' \stackrel{?}{=} h(x')$, trova che sono uguali e accetta il messaggio falso!

#### E allora a cosa servono le Funzioni di Hash SENZA Chiave?
Le funzioni di hash senza chiave ($h$) sono uno dei mattoni più importanti dell'intera crittografia moderna, ma vengono usate in contesti in cui **l'impronta $h(x)$ viene protetta in altro modo** (o legata a una chiave):

1. **Firme Digitali (Paradigma *Hash-and-Sign*):**
   Gli algoritmi di firma digitale a chiave pubblica (come RSA o ECDSA, Capitolo 8) sono lenti e possono firmare direttamente solo blocchi piccoli. Invece di firmare un documento $x$ lungo molti megabyte, Alice applica prima una funzione di hash veloce senza chiave per ottenere un'impronta corta $z = h(x)$ (es. 256 bit), e poi **applica la sua firma digitale asimmetrica solo a $z$** ($\sigma = \text{sig}_K(h(x))$). Qui l'integrità di $h(x)$ è garantita dalla firma digitale!
2. **Verifica dell'Integrità di File e Software (Canale Protetto / Read-Only):**
   Se scarichi un file immagine ISO da un server mirror non fidato, come fai a sapere che non contiene malware? Il sito ufficiale dello sviluppatore (protetto via HTTPS) pubblica la stringa $y = h(\text{file})$. Tu scarichi il file dal mirror, calcoli $h(\text{file scaricato})$ sul tuo PC e controlli che coincida con $y$. (Lo stesso vale per un antivirus che salva gli hash dei file di sistema su un disco protetto da scrittura).
3. **Costruzione di MAC (es. HMAC) e Key Derivation Functions (KDF):**
   Incombinazione con una chiave segreta $K$, una funzione di hash pubblica come SHA-256 viene usata per costruire MAC sicuri (come **HMAC**, Sezione 5.5.1) e per derivare chiavi di sessione (Capitolo 12).

> [!example] Esempio Pratico: Attacco Man-in-the-Middle su Hash senza Chiave vs Protezione con Firma/MAC
> Supponiamo che Alice voglia inviare a Bob il messaggio $x = \texttt{"Paga 100 euro"}$ e usi la funzione di hash pubblica $h = \text{SHA-256}$:
> * **Senza chiave né firma (Insicuro):** Alice invia $(x, h(x))$ sulla rete. Oscar intercetta il pacchetto, sostituisce $x$ con $x' = \texttt{"Paga 9999 euro"}$, calcola $y' = \text{SHA-256}(x')$ in un millisecondo e inoltra $(x', y')$ a Bob. Bob calcola $\text{SHA-256}(x')$, vede che coincide con $y'$ e cade nella trappola.
> * **Con Firme Digitali (*Hash-and-Sign*):** Alice calcola $z = \text{SHA-256}(x)$ e lo firma con la sua chiave privata: $\sigma = \text{sig}_{K_{\text{priv}}}(z)$. Se Oscar cambia $x$ in $x'$, non può falsificare la firma di Alice sul nuovo hash $z' = \text{SHA-256}(x')$ (perché non ha la chiave privata di Alice). L'unico modo che avrebbe Oscar per ingannare Bob senza toccare la firma $\sigma$ sarebbe trovare un messaggio $x' \neq x$ che produca **esattamente lo stesso identico hash** di $x$, ovvero $\text{SHA-256}(x') = \text{SHA-256}(x)$! Questo ci porta direttamente ai tre problemi di sicurezza della Sezione 5.2.

---

## 5.2 Sicurezza delle Funzioni di Hash (Security of Hash Functions)

Consideriamo d'ora in avanti una funzione di hash **senza chiave** $h : \mathcal{X} \to \mathcal{Y}$.
Poiché l'insieme dei possibili messaggi $\mathcal{X}$ è molto più grande dell'insieme dei possibili digest $\mathcal{Y}$ ($|\mathcal{X}| \gg |\mathcal{Y}|$, o addirittura $\mathcal{X}$ è infinito mentre $|\mathcal{Y}| = 2^m$ è finito), per il **Principio dei Cassetti (*Pigeonhole Principle*)** la funzione $h$ **NON può essere iniettiva**: esistono inevitabilmente moltissime coppie di messaggi diversi $x \neq x'$ che vengono mappati nello stesso identico digest $h(x) = h(x')$ (tali coppie si chiamano **collisioni**).

Tuttavia, affinché $h$ sia crittograficamente sicura, deve essere **computazionalmente infattibile** per qualsiasi avversario trovare queste collisioni o invertire la funzione!

---

### 5.2.1 I Tre Problemi Fondamentali: Preimage, Second Preimage e Collision

Stinson formalizza la sicurezza di una funzione di hash definendo **tre problemi computazionali** che un avversario non deve essere in grado di risolvere:

#### 1. Il Problema della Preimmagine (Preimage Problem)

> [!abstract] Problem 5.1: Preimage
> * **Istanza (Input):** Una funzione di hash $h : \mathcal{X} \to \mathcal{Y}$ e un elemento $y \in \mathcal{Y}$ (un message digest fissato).
> * **Obiettivo (Output):** Trovare un messaggio $x \in \mathcal{X}$ tale che:
>   $$h(x) = y$$

* **Definizione di Sicurezza associata:**
  Dato un punto $y \in \mathcal{Y}$, l'insieme di tutti gli $x \in \mathcal{X}$ tali che $h(x) = y$ è detto *controimmagine* (o insieme delle preimmagini) di $y$, denotato con $h^{-1}(y)$.
  Se il problema **Preimage** è computazionalmente infattibile da risolvere per un $y \in \mathcal{Y}$ scelto a caso, la funzione di hash $h$ si dice **one-way** (unidirezionale) oppure **preimage resistant** (resistente alla preimmagine).
* *Scenario pratico:* Un attaccante ruba dal database di un server il digest $y = h(\text{password})$ e vuole risalire a una password $x$ che produca quell'hash $y$.

---

#### 2. Il Problema della Seconda Preimmagine (Second Preimage Problem)

> [!abstract] Problem 5.2: Second Preimage
> * **Istanza (Input):** Una funzione di hash $h : \mathcal{X} \to \mathcal{Y}$ e un messaggio fissato $x \in \mathcal{X}$.
> * **Obiettivo (Output):** Trovare un **secondo messaggio** $x' \in \mathcal{X}$ tale che:
>   $$x' \neq x \qquad \text{e} \qquad h(x') = h(x)$$

* **Definizione di Sicurezza associata:**
  Se il problema **Second Preimage** è computazionalmente infattibile da risolvere (dato un messaggio $x \in \mathcal{X}$), la funzione $h$ si dice **second preimage resistant** (resistente alla seconda preimmagine, talvolta chiamata anche *weakly collision resistant*).
* *Scenario pratico:* Alice ha firmato digitalmente un contratto onesto $x$ (firmando $h(x)$). Oscar conosce $x$ e vuole fabbricare un contratto fraudolento $x' \neq x$ che abbia lo stesso hash $h(x') = h(x)$, così da poter incollare la firma valida di Alice sotto il contratto falso $x'$.

---

#### 3. Il Problema della Collisione (Collision Problem)

> [!abstract] Problem 5.3: Collision
> * **Istanza (Input):** Una funzione di hash $h : \mathcal{X} \to \mathcal{Y}$.
> * **Obiettivo (Output):** Trovare **una qualsiasi coppia** di messaggi distinti $x, x' \in \mathcal{X}$ tali che:
>   $$x' \neq x \qquad \text{e} \qquad h(x') = h(x)$$

* **Definizione di Sicurezza associata:**
  Se il problema **Collision** è computazionalmente infattibile da risolvere, la funzione $h$ si dice **collision resistant** (resistente alle collisioni, o *strongly collision resistant*).
* **Differenza cruciale tra Second Preimage e Collision:**
  * In **Second Preimage**, il primo messaggio $x$ è **imposto dall'esterno** (Oscar non può sceglierlo né modificarlo, deve trovare un $x'$ che collida proprio con quell'$x$ fissato).
  * In **Collision**, Oscar ha **libertà totale su entrambi i messaggi** $x$ e $x'$: gli basta trovare *due messaggi qualsiasi* che diano lo stesso hash!
* *Scenario pratico dell'attacco di Collisione:* Oscar prepara lui stesso **due versioni** di un contratto: una versione onesta $x$ (*"Affitto a 500€/mese"*) e una versione truffaldina $x'$ (*"Affitto a 5000€/mese"*). Apporta piccole modifiche invisibili a entrambe (spazi bianchi, sinonimi, metadati) finché non trova una coppia $(x, x')$ tale che $h(x) = h(x')$. Poi sottopone il contratto onesto $x$ ad Alice; Alice lo legge, si fida e firma digitalmente $h(x)$. Un minuto dopo, Oscar butta via $x$ e presenta in tribunale $x'$ accompagnato dalla firma di Alice!

---

### 5.2.2 Il Modello dell'Oracolo Casuale (The Random Oracle Model - ROM)

Per studiare matematicamente quante operazioni servono per risolvere i tre problemi (Preimage, Second Preimage e Collision) senza dipendere dai dettagli algebrici di una specifica funzione come SHA-256, **Bellare e Rogaway (1993)** hanno introdotto il **Random Oracle Model (Modello dell'Oracolo Casuale)**.

L'idea è modellare una funzione di hash "perfetta/ideale" $h : \mathcal{X} \to \mathcal{Y}$ (con $|\mathcal{Y}| = M$) come una **funzione totalmente casuale** estratta uniformemente dall'insieme $\mathcal{F}^{\mathcal{X}, \mathcal{Y}}$ di tutte le $M^{|\mathcal{X}|}$ funzioni possibili da $\mathcal{X}$ a $\mathcal{Y}$:

1. **Come funziona l'Oracolo Casuale:**
   Nessuno possiede una "formula" per calcolare $h$. L'unico modo per conoscere il valore $h(x)$ (sia per gli utenti onesti sia per l'avversario Oscar) è **interrogare un Oracolo** (una scatola nera) inviandogli una *query* $x \in \mathcal{X}$:
   * **Se $x$ non è mai stato chiesto prima:** L'oracolo genera istantaneamente un elemento $y \in \mathcal{Y}$ scelto **con probabilità uniforme $\frac{1}{M}$** (in modo indipendente da tutte le risposte precedenti), restituisce $y = h(x)$ e salva la coppia $(x, y)$ nel suo registro interno.
   * **Se $x$ è già stato chiesto in precedenza:** Per garantire la coerenza matematica di una funzione, l'oracolo cerca $(x, y)$ nel suo registro e restituisce esattamente lo stesso valore $y$ dato la prima volta.

2. **Teorema di Indipendenza nel Random Oracle Model:**
   Se un algoritmo non ha mai interrogato l'oracolo su un insieme di input distinti $x_1, x_2, \dots, x_k \in \mathcal{X}$, allora dal suo punto di vista i valori $h(x_1), h(x_2), \dots, h(x_k)$ sono **variabili aleatorie indipendenti e uniformemente distribuite** su $\mathcal{Y}$:
   $$\Pr[h(x_i) = y] = \frac{1}{M} \qquad \forall x_i \in \mathcal{X}, \; \forall y \in \mathcal{Y}$$

> [!important] Costo Computazionale nel Random Oracle Model
> Nel Random Oracle Model, poiché l'unico modo per sapere qualcosa su $h(x)$ è interrogare l'oracolo, la **complessità temporale** di un attacco si misura semplicemente contando **il numero di query $Q$ all'oracolo** necessarie per risolvere il problema con una certa probabilità di successo $\varepsilon$.
> Un algoritmo randomizzato che interroga l'oracolo al massimo $Q$ volte e ha successo con probabilità almeno $\varepsilon$ viene chiamato un **$(\varepsilon, Q)$-algorithm**.

---

### 5.2.3 Analisi degli Algoritmi nel Random Oracle Model (e il Paradosso del Compleanno)

Calcoliamo ora la probabilità di successo $\varepsilon$ di un avversario che effettua **$Q$ query distinte** all'oracolo per risolvere i tre problemi quando $|\mathcal{Y}| = M$ (ad esempio $M = 2^m$ per un hash a $m$ bit).

#### A. Complessità di `Preimage` e `Second Preimage` nel ROM

Nel modello Random Oracle, la strategia ottimale per attaccare **Preimage** (dato $y \in \mathcal{Y}$) o **Second Preimage** (dato $x \in \mathcal{X}$) è identica: scegliere $Q$ input distinti a caso e sperare di colpire il bersaglio!

> [!abstract] Algorithm 5.1: `Find-Preimage`$(h, y, Q)$  *(e `Find-Second-Preimage`$(h, x, Q)$)*
> 1. Scegliere $Q$ elementi distinti $x_1, x_2, \dots, x_Q \in \mathcal{X}$ *(nel caso di `Second-Preimage`, si sceglie $x_i \neq x$ e si calcola prima il bersaglio $y = h(x)$)*.
> 2. **for** $i \leftarrow 1$ **to** $Q$ **do**
>    $\quad$ **if** $h(x_i) = y$ **then**
>    $\quad \quad$ **return** ($x_i$) *(Successo!)*
> 3. **return** (*Failure*)

* **Calcolo esatto della Probabilità di Successo $\varepsilon$:**
  * Per ogni singola query $x_i$, la probabilità che $h(x_i) = y$ è $\frac{1}{M}$, quindi la probabilità di **fallire** sulla singola query $x_i$ è:
    $$\Pr[h(x_i) \neq y] = 1 - \frac{1}{M}$$
  * Poiché le $Q$ query sono effettuate su input distinti $x_1, \dots, x_Q$, nel Random Oracle Model gli eventi sono **statisticamente indipendenti**. La probabilità di fallire su **tutte e $Q$** le query è quindi il prodotto:
    $$\Pr[\text{Fallimento su tutte le } Q \text{ query}] = \left(1 - \frac{1}{M}\right)^Q$$
  * Di conseguenza, la probabilità di successo $\varepsilon$ (trovare almeno una preimmagine entro $Q$ tentativi) è:
    $$\varepsilon = 1 - \left(1 - \frac{1}{M}\right)^Q$$
  * **Approssimazione per $M$ grande (Sviluppo di Taylor / Binomio):**
    Quando $Q \ll M$, sviluppando $(1 - 1/M)^Q \approx 1 - \frac{Q}{M}$ (oppure usando $1 - \frac{1}{M} \approx e^{-1/M}$), otteniamo:
    $$\varepsilon \approx \frac{Q}{M} \qquad \Big(\text{ovvero } Q \approx \varepsilon M\Big)$$
    Per avere una probabilità di successo $\varepsilon = \frac{1}{2}$ (o dell'ordine di una costante), l'attaccante deve effettuare un numero di query dell'ordine di **$Q = \Theta(M) = \Theta(2^m)$**!
    *(Nota: per `Find-Second-Preimage`, se contiamo anche la query iniziale per calcolare $y = h(x)$, con $Q$ query totali si testano $Q-1$ candidati, quindi $\varepsilon = 1 - (1 - 1/M)^{Q-1}$).*

---

#### B. Complessità di `Collision` nel ROM: Il Birthday Attack (Attacco del Compleanno)

Vediamo ora cosa cambia radicalmente quando l'attaccante vuole risolvere il problema **Collision** (trovare due input distinti qualsiasi $x_i \neq x_j$ tali che $h(x_i) = h(x_j)$):

> [!abstract] Algorithm 5.2: `Find-Collision`$(h, Q)$ *(Birthday Attack)*
> 1. Scegliere $Q$ elementi distinti qualsiasi $x_1, x_2, \dots, x_Q \in \mathcal{X}$.
> 2. **for** $i \leftarrow 1$ **to** $Q$ **do**
>    $\quad y_i \leftarrow h(x_i)$
> 3. Controllare se esistono due indici $i \neq j$ ($1 \le i < j \le Q$) tali che $y_i = y_j$:
>    * **Se esistono:** **return** $(x_i, x_j)$ *(Collisione trovata!)*
>    * **Altrimenti:** **return** (*Failure*)

* **Teorema e Dimostrazione della Probabilità di Collisione:**
  Calcoliamo prima la probabilità complementare, ovvero la probabilità $p_{\text{no-coll}}$ che tutti i $Q$ valori $y_1, y_2, \dots, y_Q$ siano **tutti distinti tra loro** (nessuna collisione):
  1. La 1ª query $y_1 = h(x_1)$ non può collidere con nulla: probabilità $1 = \frac{M}{M}$.
  2. Affinché la 2ª query $y_2 = h(x_2)$ non collida con $y_1$, deve cadere in uno degli altri $M - 1$ valori di $\mathcal{Y}$: probabilità $\frac{M - 1}{M} = 1 - \frac{1}{M}$.
  3. Affinché la 3ª query $y_3 = h(x_3)$ non collida né con $y_1$ né con $y_2$ (che sono distinti), deve cadere nei restanti $M - 2$ valori: probabilità $1 - \frac{2}{M}$.
  4. In generale, dati $y_1, \dots, y_{i-1}$ tutti distinti, la $i$-esima query $y_i = h(x_i)$ evita i precedenti $i - 1$ valori con probabilità $1 - \frac{i - 1}{M}$.

  Moltiplicando le probabilità condizionate per $i = 1, \dots, Q$, la probabilità di **non trovare alcuna collisione** dopo $Q$ query è:
  $$\Pr[\text{nessuna collisione}] = \left(1 - \frac{1}{M}\right)\left(1 - \frac{2}{M}\right) \cdots \left(1 - \frac{Q - 1}{M}\right) = \prod_{i=1}^{Q-1} \left(1 - \frac{i}{M}\right)$$

  * **Approssimazione analitica tramite $1 - t \approx e^{-t}$:**
    Dall'analisi matematica sappiamo che per ogni $t \in \mathbb{R}$ vale la disuguaglianza $1 - t \le e^{-t}$, e per $t = \frac{i}{M}$ piccolo vale l'ottima approssimazione $1 - \frac{i}{M} \approx e^{-i/M}$. Sostituendo nel prodotto:
    $$\prod_{i=1}^{Q-1} \left(1 - \frac{i}{M}\right) \approx \prod_{i=1}^{Q-1} e^{-i/M} = \exp\left( - \frac{1}{M} \sum_{i=1}^{Q-1} i \right)$$
    Ricordando la somma dei primi $Q - 1$ interi (formula di Gauss: $\sum_{i=1}^{Q-1} i = \frac{Q(Q - 1)}{2}$), otteniamo:
    $$\Pr[\text{nessuna collisione}] \approx e^{-\frac{Q(Q - 1)}{2M}}$$
    Pertanto, la probabilità di successo $\varepsilon$ di trovare **almeno una collisione** con $Q$ query è:
    $$\varepsilon = 1 - \prod_{i=1}^{Q-1} \left(1 - \frac{i}{M}\right) \approx 1 - e^{-\frac{Q(Q - 1)}{2M}}$$

  * **Esplicitiamo il numero di query $Q$ in funzione di $\varepsilon$ e $M$:**
    Invertiamo l'equazione rispetto a $Q$:
    $$e^{-\frac{Q(Q - 1)}{2M}} \approx 1 - \varepsilon \quad \Longleftrightarrow \quad \frac{Q^2 - Q}{2M} \approx -\ln(1 - \varepsilon) = \ln\left(\frac{1}{1 - \varepsilon}\right)$$
    Poiché per $Q$ grande vale $Q^2 - Q \approx Q^2$, otteniamo la celebre **Formula del Birthday Attack**:
    $$Q^2 \approx 2M \ln\left(\frac{1}{1 - \varepsilon}\right) \quad \Longrightarrow \quad \mathbf{Q \approx \sqrt{2M \ln\left(\frac{1}{1 - \varepsilon}\right)}}$$

  * **Caso standard $\varepsilon = \frac{1}{2}$ (Probabilità di successo del 50%):**
    Ponendo $\varepsilon = 0.5$, abbiamo $\ln\left(\frac{1}{1 - 0.5}\right) = \ln 2 \approx 0.69315$, da cui:
    $$Q \approx \sqrt{2 \ln 2 \cdot M} \approx \mathbf{1.1774 \sqrt{M}}$$

---

> [!example] Esempio Classico: Il Paradosso del Compleanno ($M = 365$) e Impatto sui Bit dell'Hash
> 1. **Il Paradosso dei Compleanni ($M = 365$ giorni dell'anno):**
>    Quante persone ($Q$) devono trovarsi in una stanza affinché la probabilità che almeno due di esse compiano gli anni lo stesso giorno sia almeno $\varepsilon = 1/2$ ($50\%$)?
>    Applicando la formula con $M = 365$ e $\varepsilon = 1/2$:
>    $$Q \approx 1.1774 \times \sqrt{365} \approx 1.1774 \times 19.105 \approx \mathbf{22.49}$$
>    Bastano quindi **$Q = 23$ persone** (dove il calcolo esatto dà $\varepsilon \approx 0.5073$, cioè $50.73\%$), un numero enormemente più piccolo di $365 / 2 = 182.5$, perché con $Q$ persone non stiamo facendo $Q$ confronti con una data fissa, bensì **tutte le $\binom{Q}{2} = \frac{Q(Q-1)}{2}$ coppie possibili** tra i presenti (con $23$ persone ci sono già $\frac{23 \times 22}{2} = 253$ coppie di persone confrontate!).
> 
> 2. **Impatto devastante sulla lunghezza in bit ($m$) delle Funzioni di Hash ($M = 2^m$):**
>    Se una funzione di hash produce un *message digest* di **$m$ bit**, il codominio ha cardinalità $M = 2^m$.
>    * Per invertire l'hash (**Preimage** o **Second Preimage**), servono $Q \approx 2^m$ query.
>    * Ma per trovare una **Collisione** con il *Birthday Attack*, servono solo:
>      $$Q \approx \sqrt{M} = \sqrt{2^m} = \mathbf{2^{m/2} \text{ query!}}$$
>    * **Esempi concreti dal libro:**
>      * Se un hash avesse un digest di soli **$m = 40$ bit** ($M = 2^{40}$), una collisione si troverebbe con probabilità $1/2$ in appena $\approx 2^{20}$ (circa **un milione**) di calcoli di hash, eseguibili in un millisecondo su un normale PC!
>      * Lo storico standard **SHA-1** ha un digest di **$m = 160$ bit**: un attacco del compleanno generico richiede circa $2^{80}$ hash (oggi considerato al limite o insufficiente, oltre ad avere vulnerabilità strutturali scoperte nel 2017).
>      * **Regola d'oro di progettazione:** Per garantire un livello di sicurezza computazionale pari a **$k$ bit** (es. $2^{128}$ operazioni, lo stesso livello di sicurezza di AES-128), il *message digest* di una funzione di hash deve essere lungo **almeno $m = 2k$ bit** (cioè almeno **$256$ bit**, motivo per cui gli standard attuali **SHA-2** e **SHA-3** usano lunghezze da **$224, 256, 384$ o $512$ bit**!).

---

### 5.2.4 Confronto e Riduzioni tra i Tre Criteri di Sicurezza

Come sono legati tra loro i tre problemi **Collision**, **Second Preimage** e **Preimage** per una generica funzione di hash $h : \mathcal{X} \to \mathcal{Y}$? Quale proprietà è la più forte (la più difficile da garantire) e quale implica le altre?

Dimostriamo le due **riduzioni matematiche** fondamentali presentate da Stinson nella Sezione 5.2.3.

---

#### Riduzione 1: `Collision Resistance` $\Longrightarrow$ `Second Preimage Resistance`

Dimostriamo che se una funzione $h$ è **Collision Resistant**, allora è automaticamente **Second Preimage Resistant**.
*(Per contrapposizione, questo equivale a dimostrare che se un avversario possiedesse una "scatola nera" `Solve-Second-Preimage` capace di risolvere il problema Second Preimage, potrebbe usarla immediatamente per risolvere il problema Collision!).*

> [!abstract] Algorithm 5.3: `Collision-To-Second-Preimage`$(h)$
> **Assunzione:** Supponiamo di avere accesso a un algoritmo `Solve-Second-Preimage`$(x)$ che, dato $x \in \mathcal{X}$, restituisce $x' \neq x$ tale che $h(x') = h(x)$.
> **Obiettivo:** Trovare una collisione $(x, x')$ per $h$.
>
> 1. Scegliere un elemento $x \in \mathcal{X}$ in modo uniforme a caso.
> 2. Invocare $x' \leftarrow \text{Solve-Second-Preimage}(x)$.
> 3. **if** $(x' \neq x)$ **and** $(h(x') = h(x))$ **then**
>    $\quad$ **return** $(x, x')$ *(Collisione trovata!)*
> 4. **else** **return** (*Failure*)

* **Teorema 5.3:** Se `Solve-Second-Preimage` è un $(\varepsilon, Q)$-algorithm per il problema **Second Preimage**, allora `Collision-To-Second-Preimage` è un $(\varepsilon, Q)$-algorithm (o $(\varepsilon, Q+1)$ se verifichiamo $h$) per il problema **Collision**.
* **Conclusione 1:** Trovare una collisione è **più facile** (o al più ugualmente difficile) che trovare una seconda preimmagine. Pertanto, **la resistenza alle collisioni è un requisito più forte della resistenza alla seconda preimmagine**:
  $$\text{Collision Resistant} \Longrightarrow \text{Second Preimage Resistant}$$

---

#### Riduzione 2: `Second Preimage` (o `Collision`) $\Longrightarrow$ `Preimage Resistance` (Teorema 5.4)

A prima vista potrebbe sembrare ovvio che se sai invertire $h$ (cioè hai un oracolo `Solve-Preimage`$(y)$ che dato $y$ ti restituisce un $x'$ tale che $h(x') = y$), allora puoi anche trovare una seconda preimmagine o una collisione: prendi un $x$ a caso, calcoli $y = h(x)$, chiedi $x' \leftarrow \text{Solve-Preimage}(y)$ e speri che $x' \neq x$.

**Ma attenzione alla trappola matematica!**
Chi ci garantisce che l'algoritmo `Solve-Preimage`$(y)$ non ci restituisca **esattamente lo stesso $x$ da cui siamo partiti** ($x' = x$), rendendo inutile il nostro tentativo perché per una collisione serve obbligatoriamente $x' \neq x$?!

Il **Teorema 5.4** di Stinson dimostra che, finché il dominio $\mathcal{X}$ è sufficientemente più grande di $\mathcal{Y}$ (ad esempio $|\mathcal{X}| \ge 2|\mathcal{Y}|$), **anche se `Solve-Preimage` è completamente deterministico**, la riduzione funziona con alta probabilità!

> [!abstract] Algorithm 5.4: `Collision-To-Preimage`$(h)$ *(valido anche per `Second-Preimage-To-Preimage`)*
> **Assunzione:** Supponiamo di avere un algoritmo `Solve-Preimage`$(y)$ che, dato $y \in \mathcal{Y}$, restituisce un elemento $x' \in \mathcal{X}$ tale che $h(x') = y$.
>
> 1. Scegliere un messaggio iniziale $x \in \mathcal{X}$ **uniformemente a caso**.
> 2. Calcolare $y \leftarrow h(x)$ *(1 query a $h$)*.
> 3. Invocare $x' \leftarrow \text{Solve-Preimage}(y)$.
> 4. **if** $x' \neq x$ **then**
>    $\quad$ **return** $(x, x')$ *(Successo: $x' \neq x$ e $h(x') = y = h(x)$!)*
> 5. **else** **return** (*Failure*)

> [!important] Teorema 5.4 (Stinson): Riduzione da Collision/Second-Preimage a Preimage
> Sia $h : \mathcal{X} \to \mathcal{Y}$ una funzione di hash con $|\mathcal{X}| = N$ e $|\mathcal{Y}| = M$, tale che $N \ge 2M$. Supponiamo che `Solve-Preimage` sia un $(1, Q)$-algorithm che risolve sempre il problema **Preimage** per $h$. Allora l'algoritmo `Collision-To-Preimage` è un $(\varepsilon, Q+1)$-algorithm per il problema **Collision** (e per **Second Preimage** su input casuale) con probabilità di successo:
> $$\varepsilon \ge 1 - \frac{M}{N} \ge \frac{1}{2}$$

* **Dimostrazione Completa del Teorema 5.4:**
  1. Per ogni $y \in \mathcal{Y}$, definiamo la classe di equivalenza (fibra/controimmagine) $h^{-1}(y) = \{x \in \mathcal{X} : h(x) = y\}$ e poniamo $c_y = |h^{-1}(y)|$.
     Poiché gli insiemi $h^{-1}(y)$ (al variare di $y \in \text{Im}(h)$) formano una partizione di $\mathcal{X}$, la somma delle loro cardinalità è esattamente $N$:
     $$\sum_{y \in \text{Im}(h)} c_y = N$$
  2. Quando scegliamo $x \in \mathcal{X}$ con probabilità uniforme $\frac{1}{N}$ al Passo 1 e calcoliamo $y = h(x)$, la probabilità che l'immagine sia un particolare $y \in \text{Im}(h)$ è:
     $$\Pr[h(x) = y] = \frac{|h^{-1}(y)|}{|\mathcal{X}|} = \frac{c_y}{N}$$
  3. Inoltre, **condizionatamente al fatto che $h(x) = y$**, l'elemento $x$ che abbiamo estratto al Passo 1 è distribuito **uniformemente** tra tutti i $c_y$ elementi dell'insieme $h^{-1}(y)$!
     L'algoritmo `Solve-Preimage`$(y)$ riceve in input **soltanto $y$** (non sa quale $x \in h^{-1}(y)$ avevamo estratto noi al Passo 1!) e restituisce un certo elemento $x' \in h^{-1}(y)$.
     Pertanto, fissato $y$, tra i $c_y$ elementi possibili per $x \in h^{-1}(y)$, ce n'è **uno solo** "sfortunato" che coincide con $x'$ ($x = x'$), mentre tutti gli altri **$c_y - 1$ elementi** soddisfano $x \neq x'$! Quindi:
     $$\Pr[x' \neq x \mid h(x) = y] = \frac{c_y - 1}{c_y}$$
  4. Applichiamo la legge della probabilità totale sommando su tutti gli $y \in \text{Im}(h)$ (notando che $|\text{Im}(h)| \le |\mathcal{Y}| = M$):
     $$\begin{aligned}
     \Pr[\text{Successo}] = \Pr[x' \neq x] &= \sum_{y \in \text{Im}(h)} \Pr[h(x) = y] \cdot \Pr[x' \neq x \mid h(x) = y] \\
     &= \sum_{y \in \text{Im}(h)} \frac{c_y}{N} \cdot \frac{c_y - 1}{c_y} \\
     &= \frac{1}{N} \sum_{y \in \text{Im}(h)} (c_y - 1) \\
     &= \frac{1}{N} \left( \sum_{y \in \text{Im}(h)} c_y - \sum_{y \in \text{Im}(h)} 1 \right) \\
     &= \frac{N - |\text{Im}(h)|}{N} \ge \frac{N - M}{N} = 1 - \frac{M}{N}
     \end{aligned}$$
  5. Poiché per ipotesi $N \ge 2M$ (cioè $\frac{M}{N} \le \frac{1}{2}$), concludiamo che:
     $$\varepsilon = \Pr[x' \neq x] \ge 1 - \frac{1}{2} = \mathbf{\frac{1}{2}}$$
     *(E nelle funzioni di hash reali, dove $N \gg M$, si ha $\frac{M}{N} \approx 0$, quindi la probabilità di successo $\varepsilon = 1 - \frac{M}{N}$ è praticamente uguale a **$1$**!).* $\blacksquare$

> [!example] Esempio Numerico del Teorema 5.4 (Perché l'ipotesi $N \ge 2M$ è indispensabile!)
> * **Caso 1 ($N = M$, nessuna compressione):** Sia $\mathcal{X} = \mathcal{Y} = \{0, 1\}^{128}$ e sia $h(x) = x$ la funzione identità (o una permutazione).
>   - Qui ogni fibra ha dimensione $c_y = 1$ (non esistono proprio due input diversi con la stessa uscita!).
>   - Quindi $h$ è banalmente **Collision Resistant** e **Second Preimage Resistant** (è impossibile trovare $x \neq x'$ con $h(x)=h(x')$ perché non esistono!), ma **NON è affatto Preimage Resistant** (chiunque inverte $h(x) = y$ istantaneamente ponendo $x = y$!).
>   - Infatti, nella formula del Teorema 5.4, con $N = M$ si ottiene $\Pr[x' \neq x] = \frac{N - M}{N} = 0$.
> * **Caso 2 ($N = 8, M = 2$, compressione da 3 bit a 1 bit):** Sia $\mathcal{X} = \{0, 1\}^3$ ($N = 8$) e $\mathcal{Y} = \{0, 1\}$ ($M = 2$).
>   Supponiamo che $h$ mandi $6$ elementi in $y=0$ ($c_0 = 6$) e $2$ elementi in $y=1$ ($c_1 = 2$).
>   Anche se l'oracolo `Solve-Preimage` restituisce sempre un elemento fisso per $0$ e uno fisso per $1$, scegliendo $x \in \{0,1\}^3$ a caso la probabilità di ottenere $x' \neq x$ è esattamente:
>   $$\Pr[x' \neq x] = \frac{6}{8} \cdot \frac{5}{6} + \frac{2}{8} \cdot \frac{1}{2} = \frac{5 + 1}{8} = \frac{6}{8} = \frac{N - M}{N} = \mathbf{\frac{3}{4} = 75\%} \ge \frac{1}{2}$$

---

#### Tabella Riassuntiva della Gerarchia di Sicurezza (per $N \gg M = 2^m$)

$$\boxed{\text{Collision Resistant}} \implies \boxed{\text{Second Preimage Resistant}} \implies \boxed{\text{Preimage Resistant (One-Way)}}$$

| Proprietà di Sicurezza | Cosa è dato a Oscar | Cosa deve trovare Oscar | Complessità nel ROM ($M = 2^m$) | Forza della Proprietà |
| :--- | :---: | :---: | :---: | :---: |
| **1. Preimage Resistance** | Un digest $y \in \mathcal{Y}$ | $x$ tale che $h(x) = y$ | $Q \approx 2^m$ | **Più debole** (Base) |
| **2. Second Preimage Resistance** | Un messaggio $x \in \mathcal{X}$ | $x' \neq x$ tale che $h(x') = h(x)$ | $Q \approx 2^m$ | **Intermedia** |
| **3. Collision Resistance** | Solo la funzione $h$ | Qualsiasi coppia $x \neq x'$ con $h(x') = h(x)$ | **$Q \approx 2^{m/2}$** *(Birthday Attack!)* | **Più forte** (Implica le altre due) |

---

## 5.5.3 Crittografia Autenticata e Galois/Counter Mode (GCM)

Nella Sezione 5.5 abbiamo visto che i **Message Authentication Codes (MAC)** garantiscono l'**integrità e l'autenticità** dei messaggi grazie a una chiave segreta condivisa, mentre nel Capitolo 4 abbiamo visto che i **cifrari a blocchi** (in modalità come CBC o CTR) garantiscono la **confidenzialità**.

Nella pratica (ad esempio nelle connessioni internet HTTPS/TLS, IPsec, SSH, Wi-Fi WPA2/WPA3), Alice e Bob hanno quasi sempre bisogno di **entrambi gli obiettivi contemporaneamente**:
1. **Confidenzialità:** Oscar non deve poter leggere il messaggio $x$.
2. **Integrità / Autenticazione:** Oscar non deve poter modificare il testo cifrato $y$ in transito né iniettare pacchetti falsi (e come abbiamo imparato dal *Padding Oracle Attack* nella Sezione 4.7.1, Bob **non deve mai tentare di decifrare** un testo cifrato prima di aver verificato che sia autentico e non manomesso!).

Un sistema crittografico che fornisce simultaneamente confidenzialità e autenticazione prende il nome di **Authenticated Encryption (Crittografia Autenticata, AE)** o, quando permette di autenticare anche intestazioni in chiaro, **AEAD (*Authenticated Encryption with Associated Data*)**.

---

### 1. I Tre Approcci per Combinare Cifratura e MAC

Supponiamo che Alice e Bob dispongano di un algoritmo di cifratura simmetrica $e_{K_1}$ e di un algoritmo MAC $\text{MAC}_{K_2}$ (usando due chiavi indipendenti $K_1, K_2$). Esistono tre modi classici per combinarli sul messaggio in chiaro $x$:

1. **Encrypt-and-MAC (*Cifra e autentica separatamente*):**
   Alice cifra $y = e_{K_1}(x)$ e calcola il MAC **sul testo in chiaro** $\tau = \text{MAC}_{K_2}(x)$, inviando $(y, \tau)$.
   * *Difetto:* Se il MAC è deterministico, due messaggi uguali avranno sempre lo stesso tag $\tau$, rivelando a Oscar le ripetizioni dei messaggi!
2. **MAC-then-Encrypt (*Autentica e poi cifra tutto*):**
   Alice calcola prima il tag sul testo in chiaro $\tau = \text{MAC}_{K_2}(x)$ e poi cifra insieme messaggio e tag: $y = e_{K_1}(x \parallel \tau)$. *(Questo approccio è usato ad esempio nella modalità **CCM - Counter with CBC-MAC** descritta nella prima parte della Sezione 5.5.3).*
   * *Difetto potenziale:* Per verificare il tag $\tau$, Bob è costretto a **decifrare prima $y$**, esponendo potenzialmente il sistema ad attacchi a canale laterale o *Padding Oracle* se la decifratura fallisce in modi distinguibili.
3. **Encrypt-then-MAC (*Cifra e poi autentica il testo cifrato* — L'approccio ideale!):**
   Alice cifra prima il messaggio $y = e_{K_1}(x)$ e poi **calcola il MAC direttamente sul testo cifrato** $\tau = \text{MAC}_{K_2}(y)$, inviando $(y, \tau)$.
   * **Vantaggio decisivo:** Quando Bob riceve $(y', \tau')$, **verifica subito il MAC sul testo cifrato** controllando $\tau' \stackrel{?}{=} \text{MAC}_{K_2}(y')$ *prima ancora di toccare la funzione di decifratura*! Se Oscar ha alterato anche un solo bit di $y$, la verifica del MAC fallisce istantaneamente e Bob butta via il pacchetto senza mai decifrarlo (sventando sul nascere qualsiasi *Chosen-Ciphertext Attack* o *Padding Oracle Attack*!).

---

### 2. Galois/Counter Mode (GCM): Architettura e Matematica

Il **Galois/Counter Mode (GCM)**, standardizzato dal NIST nella *Special Publication 800-38D*, è oggi la modalità di **Crittografia Autenticata (AEAD)** più utilizzata al mondo (è il cuore di **TLS 1.3**).

GCM segue la filosofia **Encrypt-then-MAC** unendo due componenti estremamente veloci e **completamente parallelizzabili**:
1. **Per la Cifratura:** **AES in modalità Counter (CTR)** con chiave $K$ da 128 bit (o 192/256 bit).
2. **Per l'Autenticazione (MAC):** Una funzione di hash universale algebrica (chiamata **GHASH**) basata su **moltiplicazioni per una costante $H$ nel campo finito di Galois $\mathbb{F}_{2^{128}}$**!

---

#### A. Cosa sono gli "Authenticated Data" (`Auth data`) in GCM?
Oltre ai blocchi di testo in chiaro $x_1, x_2, \dots$ (che devono essere sia cifrati che autenticati), GCM accetta in ingresso anche dei blocchi opzionali chiamati **Authenticated Data** (indicati nello schema del libro come **`Auth data 1`**, o *Associated Data* $A$):
* **Cosa sono nella pratica?** Sono dati di intestazione di un pacchetto di rete (es. indirizzo IP mittente/destinatario, numero di porta TCP, numero di sequenza del pacchetto).
* **Come vengono trattati?** Non devono essere cifrati (perché i router lungo la rete devono poter leggere l'indirizzo IP per instradare il pacchetto!), ma **vengono incorporati nel calcolo dell'Authentication Tag** affinché Oscar non possa modificarli senza far fallire la verifica del tag!

---

#### B. L'Aritmetica nel Campo Finito $\mathbb{F}_{2^{128}}$
In GCM tutti i blocchi (contatori, blocchi di testo in chiaro/cifrato, `Auth data`, costante $H$ e `Auth tag`) hanno lunghezza fissa di **128 bit**.
Ogni blocco di 128 bit $B = (b_{127}, b_{126}, \dots, b_1, b_0)_2$ viene interpretato come un elemento del **campo finito di Galois $\mathbb{F}_{2^{128}} = \mathbb{Z}_2[\alpha] / (p(\alpha))$**, costruito modulo il polinomio irriducibile di grado 128 scelto dallo standard GCM:

$$p(\alpha) = \alpha^{128} + \alpha^7 + \alpha^2 + \alpha + 1$$

* **Addizione ($\oplus$) in $\mathbb{F}_{2^{128}}$:** È il semplice **XOR bit a bit** tra due blocchi da 128 bit.
* **Moltiplicazione ($\cdot$ oppure $\text{mult}_H$) in $\mathbb{F}_{2^{128}}$:** È la moltiplicazione tra due polinomi in $\mathbb{Z}_2[\alpha]$ ridotta modulo $\alpha^{128} + \alpha^7 + \alpha^2 + \alpha + 1$ (dove $\alpha^{128} \equiv \alpha^7 + \alpha^2 + \alpha + 1$).

---

### 3. Funzionamento Passo-Passo di GCM (Figura 5.3 del Libro)

Seguiamo nel dettaglio tutti i passaggi illustrati nella **Figura 5.3** di Stinson per cifrare e autenticare un messaggio composto da dati autenticati (`Auth data 1`) e blocchi di plaintext (`Plaintext 1`, `Plaintext 2`, $\dots$):

#### Passo 1: Inizializzazione dei Contatori (`Counter 0`, `Counter 1`, `Counter 2`, ...) e Calcolo di $H$
1. **Initialization Vector ($IV$) e `Counter 0`:**
   * Si sceglie un **Initialization Vector ($IV$)** non segreto, tipicamente di lunghezza **96 bit** ($12$ byte). L'$IV$ viene trasmesso in chiaro insieme al ciphertext e **deve essere cambiato ad ogni nuova cifratura** (è un *nonce*).
   * A partire dall'$IV$ di 96 bit si costruisce il valore iniziale del contatore a 128 bit, chiamato **`Counter 0`** (tipicamente concatenando ai 96 bit dell'$IV$ 32 bit finali inizializzati a `00...01`, ovvero $\text{Counter } 0 = IV \parallel 0^{31}1$).
   * I contatori successivi **`Counter 1`**, **`Counter 2`**, $\dots$ si ottengono incrementando di $1$ il contatore ad ogni passo tramite la funzione **`incr`**.
2. **Determinazione della sottochiave di moltiplicazione $H \in \mathbb{F}_{2^{128}}$:**
   * Il calcolo del tag di autenticazione richiede di effettuare moltiplicazioni nel campo $\mathbb{F}_{2^{128}}$ per un valore costante segreto **$H \in \mathbb{F}_{2^{128}}$** derivato dalla chiave AES $K$.
   * *(Nota: nel testo di Stinson a pag. 169 si afferma in modo semplificato che il valore di $H$ viene determinato cifrando `Counter 0`; nella specifica ufficiale NIST SP 800-38D, $H$ viene calcolato cifrando con AES il blocco di 128 zeri, $H = e_K(0^{128})$, mentre $e_K(\text{Counter 0})$ viene riservato esclusivamente per l'ultimo XOR di mascheramento finale del tag).*

---

#### Passo 2: Cifratura dei Blocchi di Plaintext in Modalità CTR (Parte Superiore della Figura 5.3)
I blocchi di testo in chiaro $x_1$ (`Plaintext 1`), $x_2$ (`Plaintext 2`), $\dots, x_n$ vengono cifrati esattamente come nella modalità Counter (CTR) usando i contatori a partire da `Counter 1`:

$$\begin{aligned}
y_1 &= x_1 \oplus e_K(\text{Counter } 1) \qquad (\text{Ciphertext } 1) \\
y_2 &= x_2 \oplus e_K(\text{Counter } 2) \qquad (\text{Ciphertext } 2) \\
&\;\;\vdots \\
y_n &= x_n \oplus e_K(\text{Counter } n) \qquad (\text{Ciphertext } n)
\end{aligned}$$

---

#### Passo 3: Calcolo dell'Authentication Tag tramite Moltiplicazioni in $\mathbb{F}_{2^{128}}$ (Parte Inferiore della Figura 5.3)
Una volta ottenuti i blocchi di testo cifrato $y_1, y_2, \dots, y_n$, GCM calcola il tag di autenticazione (**`Auth tag`**) concatenando una sequenza di **XOR ($\oplus$)** e **moltiplicazioni per $H$ ($\text{mult}_H$)** in $\mathbb{F}_{2^{128}}$ (secondo lo schema di Horner per la valutazione di un polinomio in $H$):

1. **Inizio dai Dati Autenticati (`Auth data 1` = $A_1$):**
   Si prende il blocco di dati autenticati in chiaro $A_1$ e lo si moltiplica per $H$ nel campo $\mathbb{F}_{2^{128}}$:
   $$g_1 = A_1 \cdot H$$
2. **Incorporazione di `Ciphertext 1` ($y_1$):**
   Si fa lo XOR con il primo blocco cifrato $y_1$ e si moltiplica il risultato per $H$ in $\mathbb{F}_{2^{128}}$:
   $$g_2 = (g_1 \oplus y_1) \cdot H = A_1 H^2 \oplus y_1 H$$
3. **Incorporazione di `Ciphertext 2` ($y_2$):**
   Si fa lo XOR con il secondo blocco cifrato $y_2$ e si moltiplica ancora per $H$ in $\mathbb{F}_{2^{128}}$:
   $$g_3 = (g_2 \oplus y_2) \cdot H = A_1 H^3 \oplus y_1 H^2 \oplus y_2 H$$
   *(Questo ciclo "XOR con il blocco cifrato $\to$ moltiplica per $H$" si ripete fino a processare tutti gli $n$ blocchi di ciphertext).*
4. **Incorporazione del Blocco delle Lunghezze (`len(A) || len(C)`):**
   Si effettua un ulteriore XOR con un blocco di 128 bit che codifica la **lunghezza in bit degli Authenticated Data** ($\text{len}(A)$, su 64 bit) concatenata alla **lunghezza in bit del Ciphertext** ($\text{len}(C)$, su 64 bit), seguito da **un'ultima moltiplicazione per $H$**:
   $$g_4 = \Big(g_3 \oplus (\text{len}(A) \parallel \text{len}(C))\Big) \cdot H = A_1 H^4 \oplus y_1 H^3 \oplus y_2 H^2 \oplus (\text{len}(A) \parallel \text{len}(C)) H$$
   * *Perché si inserisce il blocco `len(A) || len(C)`?* Perché se non registrassimo le lunghezze di $A$ e di $C$, un attaccante potrebbe spostare l'ultimo blocco di $A$ facendolo passare per il primo blocco di $C$ (o viceversa) senza alterare minimamente il polinomio in $H$!
5. **XOR Finale con la Cifratura di `Counter 0`:**
   Infine, il risultato $g_4$ viene sommato in XOR con la cifratura AES del contatore iniziale **`Counter 0`**, producendo l'**`Auth tag`** finale $T$:
   $$\mathbf{\text{Auth tag } T = g_4 \oplus e_K(\text{Counter } 0)}$$
   * *Perché serve l'ultimo XOR con $e_K(\text{Counter 0})$?* Perché se il tag fosse semplicemente il polinomio $g_4$ senza la maschera finale $e_K(\text{Counter 0})$, un attaccante che osserva $(A_1, y_1, y_2, g_4)$ potrebbe risolvere un'equazione polinomiale di 4° grado in $\mathbb{F}_{2^{128}}$ per trovare la chiave di hash segreta $H$! Mascherando $g_4$ con la chiave pseudorandom unica $e_K(\text{Counter 0})$ (che cambia a ogni messaggio perché cambia l'$IV$), il valore di $H$ rimane completamente nascosto.

---

#### Schema Visivo del Flusso Dati di GCM (Figura 5.3)

```
 [Counter 0] ──────────► [incr] ─────────────► [Counter 1] ──────────► [incr] ─────────────► [Counter 2]
      │                                             │                                             │
      ▼                                             ▼                                             ▼
 [ AES e_K ]                                   [ AES e_K ]                                   [ AES e_K ]
      │                                             │                                             │
      │                                     Plaintext 1 (x_1)                             Plaintext 2 (x_2)
      │                                             │                                             │
      │                                             ▼                                             ▼
      │                                            (⊕)                                           (⊕)
      │                                             │                                             │
      │                                             ▼                                             ▼
      │      Auth data 1 (A_1)               Ciphertext 1 (y_1)                            Ciphertext 2 (y_2)
      │              │                              │                                             │
      │              ▼                              ▼                                             ▼
      │          [ mult_H ] ─────────────────────► (⊕) ──► [ mult_H ] ─────────────────────────► (⊕) ──► [ mult_H ]
      │                                                                                                      │
      │                                                                                      len(A)||len(C) ─┤
      │                                                                                                      ▼
      │                                                                                                     (⊕)
      │                                                                                                      │
      │                                                                                                      ▼
      │                                                                                                  [ mult_H ]
      │                                                                                                      │
      └────────────────────────────────────────────────────────────────────────────────────────────────────►(⊕)
                                                                                                             │
                                                                                                             ▼
                                                                                                        [ Auth tag ]
```

---

#### Passo 4: Decifratura e Verifica in GCM
Quando Bob riceve il pacchetto completo $(IV, A_1, y_1, y_2, \text{Auth tag } T)$:
1. **Verifica dell'Autenticità PRIMA della Decifratura:**
   Partendo da $IV$, $A_1$ e dai blocchi cifrati ricevuti $y_1, y_2$, Bob ricalcola esattamente la catena inferiore ($\text{mult}_H$ e $\oplus$) e lo XOR con $e_K(\text{Counter 0})$, ottenendo il tag atteso $T'$.
   * Se **$T' \neq T$**: Bob sa con certezza che il ciphertext, gli `Auth data` o l'$IV$ sono stati manomessi in transito; **rifiuta immediatamente il pacchetto (`REJECT`)** senza restituire alcun testo decifrato.
   * Se **$T' = T$**: Il pacchetto è autentico e integro! Bob procede (o rilascia il risultato calcolato in parallelo) decifrando i blocchi in modalità CTR:
     $$x_1 = y_1 \oplus e_K(\text{Counter } 1), \qquad x_2 = y_2 \oplus e_K(\text{Counter } 2)$$

---

> [!example] Esempio Numerico Passo-Passo del Calcolo in GCM (su un campo finito ridotto $\mathbb{F}_{2^4}$)
> Per toccare con mano l'aritmetica esatta di GCM senza dover scrivere stringhe da 128 bit, eseguiamo tutti i passaggi della Figura 5.3 su blocchi da **$4$ bit** nel campo finito $\mathbb{F}_{2^4} = \mathbb{Z}_2[\alpha]/(\alpha^4 + \alpha + 1)$ (dove vale la regola di riduzione $\alpha^4 \equiv \alpha + 1$, cioè $\texttt{10000}_2 \equiv \texttt{0011}_2 = \texttt{3}_{16}$).
> 
> **Parametri del nostro esempio:**
> * Supponiamo che per il messaggio corrente i blocchi cifrati dai contatori siano:
>   * $e_K(\text{Counter } 0) = \texttt{1010}_2 = \texttt{A}_{16}$
>   * $e_K(\text{Counter } 1) = \texttt{0101}_2 = \texttt{5}_{16}$
>   * $e_K(\text{Counter } 2) = \texttt{1100}_2 = \texttt{C}_{16}$
> * Sottochiave costante di moltiplicazione in $\mathbb{F}_{2^4}$: **$H = \texttt{0010}_2 = \texttt{2}_{16}$** (che corrisponde al monomio $\alpha$).
> * Dati da trasmettere:
>   * `Auth data 1` (in chiaro): $A_1 = \texttt{0011}_2 = \texttt{3}_{16}$ ($\alpha + 1$)
>   * `Plaintext 1`: $x_1 = \texttt{1111}_2 = \texttt{F}_{16}$
>   * `Plaintext 2`: $x_2 = \texttt{0001}_2 = \texttt{1}_{16}$
>   * Blocco lunghezze: $L = \text{len}(A) \parallel \text{len}(C) = \texttt{0110}_2 = \texttt{6}_{16}$ ($\alpha^2 + \alpha$)
> 
> ---
> 
> **1. Cifratura CTR dei due blocchi di Plaintext:**
> * $y_1 = x_1 \oplus e_K(\text{Counter } 1) = \texttt{1111} \oplus \texttt{0101} = \mathbf{\texttt{1010}_2 = \texttt{A}_{16}}$ ($\alpha^3 + \alpha$)
> * $y_2 = x_2 \oplus e_K(\text{Counter } 2) = \texttt{0001} \oplus \texttt{1100} = \mathbf{\texttt{1101}_2 = \texttt{D}_{16}}$ ($\alpha^3 + \alpha^2 + 1$)
> 
> ---
> 
> **2. Calcolo a catena dell'`Auth tag` in $\mathbb{F}_{2^4}$ (Catena inferiore della Figura 5.3):**
> * **Passo 2a (`Auth data 1` $\cdot H$):**
>   Moltiplichiamo $A_1 = \alpha + 1$ ($\texttt{0011}$) per $H = \alpha$ ($\texttt{0010}$):
>   $$g_1 = (\alpha + 1) \cdot \alpha = \alpha^2 + \alpha = \mathbf{\texttt{0110}_2}$$
> * **Passo 2b (XOR con $y_1$ e moltiplicazione per $H$):**
>   Facciamo lo XOR con $y_1 = \texttt{1010}_2$:
>   $$g_1 \oplus y_1 = \texttt{0110} \oplus \texttt{1010} = \texttt{1100}_2 \quad (\alpha^3 + \alpha^2)$$
>   Moltiplichiamo per $H = \alpha$ riducendo modulo $\alpha^4 = \alpha + 1$:
>   $$g_2 = (\alpha^3 + \alpha^2) \cdot \alpha = \alpha^4 + \alpha^3 = (\alpha + 1) + \alpha^3 = \alpha^3 + \alpha + 1 = \mathbf{\texttt{1011}_2}$$
> * **Passo 2c (XOR con $y_2$ e moltiplicazione per $H$):**
>   Facciamo lo XOR con $y_2 = \texttt{1101}_2$:
>   $$g_2 \oplus y_2 = \texttt{1011} \oplus \texttt{1101} = \texttt{0110}_2 \quad (\alpha^2 + \alpha)$$
>   Moltiplichiamo per $H = \alpha$:
>   $$g_3 = (\alpha^2 + \alpha) \cdot \alpha = \alpha^3 + \alpha^2 = \mathbf{\texttt{1100}_2}$$
> * **Passo 2d (XOR con il blocco lunghezze $L = \texttt{0110}_2$ e ultima moltiplicazione per $H$):**
>   Facciamo lo XOR con $L = \texttt{0110}_2$:
>   $$g_3 \oplus L = \texttt{1100} \oplus \texttt{0110} = \texttt{1010}_2 \quad (\alpha^3 + \alpha)$$
>   Moltiplichiamo per $H = \alpha$ (usando $\alpha^4 = \alpha + 1$):
>   $$g_4 = (\alpha^3 + \alpha) \cdot \alpha = \alpha^4 + \alpha^2 = \alpha^2 + \alpha + 1 = \mathbf{\texttt{0111}_2 = \texttt{7}_{16}}$$
> * **Passo 2e (XOR finale con $e_K(\text{Counter } 0) = \texttt{1010}_2$):**
>   $$\text{Auth tag } T = g_4 \oplus e_K(\text{Counter } 0) = \texttt{0111} \oplus \texttt{1010} = \mathbf{\texttt{1101}_2 = \texttt{D}_{16}}$$
> 
> **3. Cosa succede se Oscar manomette il pacchetto in transito?**
> Alice invia $(A_1 = \texttt{3}, y_1 = \texttt{A}, y_2 = \texttt{D}, T = \texttt{D})$.
> Se Oscar inverte anche solo l'ultimo bit di `Auth data 1` (cambiando $A_1$ da $\texttt{0011}$ a $\texttt{0010}$ senza nemmeno toccare i testi cifrati!), quella differenza $\Delta A_1 = 1$ viene moltiplicata per $H^4 = \alpha^4 = \alpha + 1 = \texttt{0011}_2$, facendo sì che Bob in ricezione calcoli un tag atteso $T' = \texttt{1101} \oplus \texttt{0011} = \texttt{1110}_2 \neq \texttt{1101}_2$ e scopra immediatamente la manomissione!
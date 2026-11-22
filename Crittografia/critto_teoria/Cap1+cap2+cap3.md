

# Capitolo 1: Introduction to Cryptography (Introduzione alla Crittografia)

Il Capitolo 1 introduce gli obiettivi fondamentali della crittografia — **confidentiality** (o **secrecy**, segretezza), **data integrity** (integrità dei dati), **authentication** (autenticazione) e **nonrepudiation** (non ripudio) — insieme agli strumenti crittografici di base (**cryptosystems**, **message authentication codes**, **signature schemes**, **certificates**, **hash functions**), ai **cryptographic protocols** e alle definizioni formali dei modelli di attacco e dei livelli di sicurezza.

---

## 1.1 Cryptosystems and Basic Cryptographic Tools (Crittosistemi e Strumenti di Base)

L'obiettivo primario considerato dalla crittografia è la **confidentiality** (o **secrecy**, confidenzialità/segretezza): fare in modo che le informazioni trasmesse rimangano segrete a chiunque tranne che ai soggetti autorizzati a leggerle.

- **Lo Scenario Base di Comunicazione:**
  - **Alice** (il mittente) desidera trasmettere un messaggio non cifrato, chiamato **plaintext** (testo in chiaro, denotato con $x$), a **Bob** (il destinatario).
  - La trasmissione avviene attraverso un **insecure channel** (canale insicuro), il quale può essere osservato o manipolato da un avversario (**adversary** o **opponent**), tradizionalmente chiamato **Oscar**.

---

### 1.1.1 Secret-key Cryptosystems (Crittosistemi a Chiave Segreta)

Nel modello classico, chiamato **secret-key cryptography** (crittografia a chiave segreta, o **symmetric-key cryptography**, crittografia a chiave simmetrica), esiste un'unica chiave segreta (**secret key**) $K$, che è nota sia ad Alice che a Bob:

1. **Condivisione preliminare della chiave:** Prima che avvenga qualsiasi trasmissione di messaggi cifrati, Alice e Bob devono concordare segretamente la chiave $K$ e scambiarsela attraverso un **secure channel** (canale sicuro, ad esempio incontrandosi di persona o tramite un corriere fidato).
2. **Encryption (Cifratura) e Decryption (Decifratura):** La chiave segreta $K$ viene impiegata sia per cifrare i *plaintexts* sia per decifrare i *ciphertexts*. In particolare, $K$ determina una **encryption function** (o **encryption rule**, regola di cifratura) $e_K$ e una **decryption function** (o **decryption rule**, regola di decifratura) $d_K$:
   - Alice cifra il *plaintext* $x$ calcolando il **ciphertext** (testo cifrato):
     $$y = e_K(x)$$
     e trasmette $y$ a Bob sul canale insicuro.
   - Bob riceve $y$ e recupera il *plaintext* originale applicando la funzione di decifratura:
     $$x = d_K(y)$$
3. **Invertibilità e Iniettività:** Le funzioni di cifratura e decifratura sono l'una l'inversa dell'altra ($d_K(e_K(x)) = x$ per ogni *plaintext* $x$), il che richiede che $e_K$ sia una funzione **injective** (iniettiva: due *plaintexts* distinti devono produrre *ciphertexts* distinti).
4. **Esposizione della chiave:** In un *secret-key cryptosystem*, la regola $d_K$ coincide con $e_K$ oppure è facilmente derivabile da essa; pertanto, la compromissione (*exposure*) di una qualsiasi delle due rende l'intero sistema insicuro.

---

### 1.1.2 Public-key Cryptosystems (Crittosistemi a Chiave Pubblica)

Uno dei principali limiti dei *secret-key cryptosystems* è la necessità di disporre di un *secure channel* preliminare per condividere la chiave segreta $K$ tra Alice e Bob. Per superare questo ostacolo, si introduce la **public-key cryptosystem** (crittosistema a chiave pubblica):

- **Separazione tra Public Key e Private Key:**
  In un *public-key cryptosystem*, la regola di cifratura $e_K$ e la regola di decifratura $d_K$ sono distinte, ed è **computationally infeasible** (computazionalmente infattibile) determinare $d_K$ conoscendo unicamente $e_K$:
  - La regola di cifratura $e_K$ costituisce la **public key** (chiave pubblica) di Bob: Bob può pubblicarla apertamente affinché chiunque possa utilizzarla.
  - La regola di decifratura $d_K$ costituisce la **private key** (chiave privata) di Bob: Bob la mantiene segreta per sé.
- **Funzionamento:**
  Quando Alice vuole inviare un messaggio riservato $x$ a Bob, non ha bisogno di condividere preventivamente alcuna chiave segreta con lui: preleva la *public key* $e_K$ di Bob, calcola il *ciphertext* $y = e_K(x)$ e glielo invia sul canale insicuro. Soltanto Bob, essendo l'unico in possesso della *private key* $d_K$, è in grado di decifrare $y$ calcolando $x = d_K(y)$.

---

### 1.1.3 Block and Stream Ciphers (Cifrari a Blocchi e Cifrari a Flusso)

I crittosistemi vengono solitamente classificati in **block ciphers** (cifrari a blocchi) oppure **stream ciphers** (cifrari a flusso):

1. **Block Ciphers (Cifrari a blocchi):**
   - Il *plaintext* viene suddiviso in porzioni di dimensione fissa chiamate **blocks** (blocchi).
   - Un *block* è specificato come una **bitstring** (una stringa di `0` e `1`) di una certa lunghezza prefissata (ad esempio $64$ o $128$ bit).
   - Un *block cipher* cifra (o decifra) un blocco alla volta ($\mathbf{y} = y_1 y_2 \dots = e_K(x_1) e_K(x_2) \dots$) utilizzando la medesima chiave $K$.
2. **Stream Ciphers (Cifrari a flusso):**
   - Uno *stream cipher* utilizza dapprima la chiave $K$ per costruire un **keystream** $\mathbf{z} = z_1 z_2 \dots$, che è una *bitstring* avente esattamente la stessa lunghezza del *plaintext* (dove il *plaintext* $\mathbf{x} = x_1 x_2 \dots$ è una *bitstring* di lunghezza arbitraria).
   - L'operazione di **encryption** costruisce il *ciphertext* come l'**exclusive-or** ($\oplus$, addizione modulo 2 bit a bit) tra il *plaintext* e il *keystream*:
     $$y_i = x_i \oplus z_i$$
   - L'operazione di **decryption** si realizza calcolando nuovamente l'**exclusive-or** tra il *ciphertext* e il medesimo *keystream*:
     $$x_i = y_i \oplus z_i$$
- **Confronto strutturale:** I **public-key cryptosystems** sono invariabilmente dei **block ciphers**, mentre i **secret-key cryptosystems** possono essere sia **block ciphers** sia **stream ciphers**.

---

### 1.1.4 Hybrid Cryptography (Crittografia Ibrida)

Sebbene i *public-key cryptosystems* risolvano il problema della distribuzione delle chiavi su canali insicuri, presentano uno svantaggio pratico: sono molto più lenti rispetto ai *secret-key cryptosystems* (come AES).

Nella pratica si adotta quindi la **hybrid cryptography** (crittografia ibrida), che unisce i vantaggi di entrambi i modelli in due fasi:
1. **Scambio della chiave tramite Public-key Cryptography:** All'inizio della sessione di comunicazione, viene utilizzato un *public-key cryptosystem* esclusivamente per cifrare e trasmettere una chiave segreta temporanea (spesso chiamata **session key**, chiave di sessione) $K$ da Alice a Bob.
2. **Cifratura dei dati tramite Secret-key Cryptography:** Una volta che sia Alice sia Bob sono in possesso della *session key* $K$, utilizzano un veloce *secret-key cryptosystem* (un *block cipher* o uno *stream cipher*) con chiave $K$ per cifrare i messaggi lunghi veri e propri.

---

## 1.2 Message Integrity (Integrità dei Messaggi e Autenticazione)

La sola cifratura protegge la **confidentiality** contro un **passive adversary** (avversario passivo) che si limita a intercettare e osservare i messaggi trasmessi tra Alice e Bob. Tuttavia, in molti scenari reali dobbiamo difenderci da un **active adversary** (avversario attivo), il quale può modificare il contenuto dei messaggi in transito, inserirne di falsi o sostituire l'identità del mittente.

Entrano così in gioco ulteriori obiettivi fondamentali:
- **Data integrity (Integrità dei dati):** Garantire che il messaggio ricevuto da Bob non sia stato alterato durante la trasmissione rispetto a quello inviato da Alice.
- **Message authentication (Autenticazione del messaggio):** Garantire a Bob che il messaggio ricevuto abbia effettivamente avuto origine da Alice (e non da Oscar).

---

### 1.2.1 Message Authentication Codes (MAC)

Un **message authentication code (MAC)** è lo strumento a chiave segreta utilizzato per garantire *data integrity* e *message authentication*:

- Alice e Bob condividono una **secret key** $K$, la quale seleziona una funzione di autenticazione $h_K$.
- Quando Alice vuole trasmettere un messaggio $x$ a Bob, calcola un valore di controllo chiamato **authentication tag** (o semplicemente **tag**):
  $$y = h_K(x)$$
  e trasmette la coppia $(x, y)$ sul canale insicuro.
- Quando Bob riceve la coppia $(x, y)$, utilizza la chiave segreta condivisa $K$ per ricalcolare autonomamente il tag $h_K(x)$ a partire dal messaggio ricevuto $x$, e verifica se coincide con il tag ricevuto $y$ ($y = h_K(x)$):
  - Se la condizione è soddisfatta, Bob accetta il messaggio come **valid** (valido), avendo la garanzia che $x$ proviene da Alice e non è stato manomesso;
  - Altrimenti, Bob lo rifiuta come **invalid** (invalido).
- Un MAC è sicuro se per Oscar (che non conosce $K$) è computazionalmente infattibile produrre una **forgery** (falsificazione), ovvero riuscire a calcolare un tag valido $y' = h_K(x')$ per un nuovo messaggio $x'$ non inviato da Alice.

---

### 1.2.2 Signature Schemes (Schemi di Firma Digitale)

Un **signature scheme** (schema di firma digitale) è l'analogo a chiave pubblica di un MAC e permette di verificare l'integrità e l'origine di un messaggio senza che mittente e destinatario condividano una chiave segreta:

- Alice possiede una **private key** (nota esclusivamente a lei), che definisce un algoritmo privato di firma $\text{sig}_{\text{Alice}}$, e una corrispondente **public key** (nota a tutti), che definisce un algoritmo pubblico di verifica $\text{ver}_{\text{Alice}}$.
- Per firmare un messaggio $x$, Alice utilizza la propria *private key* per calcolare la **signature** (firma digitale):
  $$y = \text{sig}_{\text{Alice}}(x)$$
  e trasmette la coppia $(x, y)$.
- Quando Bob (o chiunque altro) riceve $(x, y)$, applica l'algoritmo pubblico di verifica di Alice:
  $$\text{ver}_{\text{Alice}}(x, y) \in \{\text{true}, \text{false}\}$$
  Se l'algoritmo restituisce **`true`**, Bob è certo che la firma $y$ sul messaggio $x$ sia autentica e sia stata generata da Alice.
- *(Nota: Se Alice desidera sia firmare sia cifrare un messaggio $x$ per Bob, il metodo raccomandato dal libro è il **sign-then-encrypt**: Alice calcola prima la sua firma $y = \text{sig}_{\text{Alice}}(x)$ e poi cifra la coppia $(x, y)$ con la chiave pubblica di Bob, inviando $z = e_{\text{Bob}}(x, y)$)*.

---

### 1.2.3 Nonrepudiation (Non Ripudio)

Oltre al fatto che le firme digitali sono verificabili pubblicamente da chiunque, vi è una differenza concettuale tra un **MAC** e un **signature scheme**: la proprietà di **nonrepudiation** (non ripudio).

- **Perché un MAC NON fornisce nonrepudiation:**
  In un MAC, sia Alice sia Bob conoscono la medesima chiave segreta condivisa $K$. Pertanto, Bob è perfettamente in grado di calcolare da solo una coppia valida $(x, h_K(x))$ per qualsiasi messaggio $x$. Se sorge una disputa legale davanti a una terza parte imparziale (un giudice, **judge**):
  1. Bob non può dimostrare al giudice che è stata Alice a inviargli $(x, y)$, perché Bob stesso avrebbe potuto fabbricare quella coppia;
  2. Viceversa, se Alice ha davvero inviato $(x, y)$, può in seguito negare disonestamente (**repudiate**, ripudiare) di averlo mai mandato, sostenendo che sia stato Bob a crearlo.
- **Perché un Signature Scheme fornisce nonrepudiation:**
  In uno schema di firma digitale, **soltanto Alice** conosce la propria *private key* ($\text{sig}_{\text{Alice}}$), mentre Bob (e il giudice) conoscono unicamente la *public key* di verifica ($\text{ver}_{\text{Alice}}$). Bob non può creare una firma valida a nome di Alice; di conseguenza, se Bob mostra al giudice una coppia $(x, y)$ tale che $\text{ver}_{\text{Alice}}(x, y) = \text{true}$, il giudice ha la prova matematica che solo Alice può aver firmato $x$, e Alice non può negare (*repudiate*) di averlo firmato.

---

### 1.2.4 Certificates (Certificati Digitali)

Tutti i sistemi a chiave pubblica (sia per l'*encryption* sia per i *signature schemes*) si basano su un presupposto critico: quando Alice usa la chiave pubblica di Bob, come fa ad essere certa che quella chiave pubblica appartenga davvero a Bob e non a Oscar (che potrebbe essersi spacciato per Bob pubblicando la propria chiave pubblica)?

La soluzione standard consiste nell'utilizzo dei **certificates** (certificati digitali), emessi da una terza parte fidata chiamata **Certification Authority (CA)** (o **Trusted Authority, TA**):
1. La **CA** possiede una propria coppia di chiavi (privata e pubblica) per uno schema di firma digitale, e la *public key* della CA è nota e autenticata presso tutti gli utenti del sistema.
2. Dopo aver verificato l'identità di Bob, la CA crea un documento digitale contenente la stringa identificativa di Bob ($\text{ID}(\text{Bob})$) insieme alla chiave pubblica di Bob, e vi appone la **firma digitale della CA** (usando la *private key* della CA).
3. L'insieme dei dati di Bob e della firma della CA costituisce il **certificate** di Bob.
4. Chiunque (inclusa Alice) può verificare la firma della CA sul certificato di Bob utilizzando la *public key* della CA, ottenendo così la garanzia crittografica che la chiave pubblica contenuta nel certificato appartiene effettivamente a Bob.

---

### 1.2.5 Hash Functions (Funzioni di Hash)

Una **cryptographic hash function** (o **unkeyed hash function**, funzione di hash senza chiave) $h$ è una funzione pubblica che prende in input un messaggio $x$ di lunghezza arbitraria e produce in output una stringa binaria corta e di lunghezza fissa $y = h(x)$ (tipicamente da $160$ a $512$ bit), chiamata **message digest** (o **fingerprint**, impronta digitale del messaggio).

Affinché una funzione di hash sia sicura, deve soddisfare tre proprietà fondamentali:
1. **One-way (o Preimage resistant):** Dato un *message digest* $y$, deve essere computazionalmente infattibile risalire a un input $x$ tale che $h(x) = y$.
2. **Second preimage resistant:** Dato un messaggio $x$, deve essere computazionalmente infattibile trovare un secondo messaggio $x' \neq x$ tale che $h(x') = h(x)$.
3. **Collision resistant:** Deve essere computazionalmente infattibile trovare una qualsiasi coppia di messaggi distinti $x \neq x'$ che producano lo stesso *message digest*, ovvero tali che $h(x) = h(x')$ (una coppia del genere è chiamata **collision**, collisione).

- **Applicazioni principali:**
  - **All'interno dei Signature Schemes (Hash-then-sign):** Poiché gli schemi di firma digitale sono lenti e operano su blocchi di dimensione fissa, invece di firmare direttamente un messaggio lungo $x$, Alice calcola prima il breve *message digest* $z = h(x)$ e firma digitalmente soltanto $z$, calcolando $y = \text{sig}_{\text{Alice}}(h(x))$.
  - **Integrità di file e costruzione di MAC:** Le *hash functions* vengono usate per verificare l'integrità dei dati e, combinate opportunamente con una chiave segreta $K$, per costruire algoritmi MAC veloci e sicuri (come **HMAC**).

---

## 1.3 Cryptographic Protocols (Protocolli Crittografici)

Oltre agli strumenti crittografici di base (*primitives*), la crittografia si occupa della progettazione e dell'analisi dei **cryptographic protocols** (protocolli crittografici).

- Un **cryptographic protocol** è un algoritmo interattivo che coinvolge due o più parti (ad esempio Alice, Bob), le quali eseguono una sequenza di calcoli e si scambiano messaggi al fine di raggiungere uno specifico obiettivo di sicurezza in presenza di un avversario.
- Esempi fondamentali di protocolli crittografici trattati nel libro includono:
  - **Key distribution / Key agreement protocols:** Protocolli che permettono ad Alice e Bob di stabilire una nuova *session key* segreta condivisa comunicando su un canale aperto (come il protocollo di scambio chiavi di **Diffie-Hellman**).
  - **Identification / Entity authentication protocols:** Protocolli in cui Alice dimostra in tempo reale a Bob la propria identità (ad esempio dimostrando di possedere una chiave segreta o privata senza rivelarla).
  - **Secret sharing schemes:** Protocolli per distribuire un segreto tra più partecipanti in modo che solo determinati sottoinsiemi autorizzati possano ricostruirlo.

---

## 1.4 Security (Modelli di Attacco e Livelli di Sicurezza)

Il processo con cui l'avversario (Oscar) tenta di determinare la chiave segreta $K$, data una stringa di *ciphertext* $\mathbf{y}$, è chiamato **cryptanalysis** (crittoanalisi). Si osservi che se Oscar riesce a determinare la chiave $K$, può decifrare qualsiasi *ciphertext* $\mathbf{y}$ esattamente come farebbe Bob usando $d_K$; pertanto, determinare $K$ è almeno tanto difficile quanto determinare il *plaintext* $\mathbf{x}$ dato $\mathbf{y}$.

> [!important] Kerckhoffs' Principle (Principio di Kerckhoffs)
> Nel valutare la sicurezza di un crittosistema, si assume sempre che l'avversario (Oscar) conosca perfettamente l'intera struttura del crittosistema utilizzato (ovvero gli insiemi $\mathcal{P}, \mathcal{C}, \mathcal{K}$ e le famiglie di regole $\mathcal{E}, \mathcal{D}$).
> La sicurezza del crittosistema deve risiedere **esclusivamente nella segretezza della chiave $K$** (e mai nella presunta segretezza dell'algoritmo).

---

### 1.4.1 Attack Models (Modelli di Attacco)

Stinson elenca **quattro modelli di attacco** standard, ordinati dal più debole (più difficile per Oscar) al più potente (più favorevole a Oscar):

1. **Ciphertext-only attack (Attacco a solo testo cifrato):**
   L'avversario possiede unicamente una stringa di *ciphertext* $\mathbf{y}$ intercettata sul canale.
2. **Known-plaintext attack (Attacco a testo in chiaro noto):**
   L'avversario possiede una stringa di *plaintext* $\mathbf{x}$ e la corrispondente stringa di *ciphertext* $\mathbf{y}$ (cifrata con la chiave ignota $K$ che Oscar vuole scoprire).
3. **Chosen-plaintext attack (Attacco a testo in chiaro scelto):**
   L'avversario ha ottenuto accesso temporaneo all'apparato di cifratura (*encryption machinery*). Può quindi scegliere a proprio piacimento una stringa di *plaintext* $\mathbf{x}$ e costruire (ottenere dall'oracolo di cifratura) la corrispondente stringa di *ciphertext* $\mathbf{y}$.
   *(Nota: In un **public-key cryptosystem**, poiché la regola di cifratura $e_K$ è pubblica, l'avversario può sempre cifrare qualsiasi plaintext desideri; pertanto un sistema a chiave pubblica deve essere intrinsecamente sicuro almeno contro i chosen-plaintext attacks!)*.
4. **Chosen-ciphertext attack (Attacco a testo cifrato scelto):**
   L'avversario ha ottenuto accesso temporaneo all'apparato di decifratura (*decryption machinery*). Può quindi scegliere una stringa di *ciphertext* $\mathbf{y}$ e ottenere la corrispondente stringa di *plaintext* $\mathbf{x}$ (con l'obiettivo di dedurre la chiave $K$ o decifrare un diverso *ciphertext* bersaglio $\mathbf{y}^* \neq \mathbf{y}$).

---

### 1.4.2 Levels of Security (Livelli di Sicurezza)

Oltre a specificare il modello di attacco, Stinson distingue **tre concetti (livelli) fondamentali di sicurezza** in base alle risorse computazionali concesse all'avversario:

#### 1. Il Requisito Preliminare: Resistenza alla Exhaustive Key Search
- In un attacco di **exhaustive key search** (ricerca esaustiva della chiave, o *brute-force*), l'avversario prova ogni possibile regola di decifratura $d_K$ (per tutte le chiavi $K \in \mathcal{K}$) finché non ottiene una stringa di *plaintext* "dotata di senso" (*meaningful*).
- Affinché un crittosistema sia sicuro nella pratica, è **condizione necessaria ma NON sufficiente** che lo spazio delle chiavi $\mathcal{K}$ sia così grande da rendere computazionalmente infattibile una *exhaustive key search* (come mostra l'esempio del *Substitution Cipher* nel Capitolo 2, che possiede $26! \approx 4 \times 10^{26}$ chiavi ma viene violato istantaneamente tramite l'analisi delle frequenze).

#### 2. Unconditional Security (Sicurezza Incondizionata)
- Un crittosistema è **unconditionally secure** (incondizionatamente sicuro) se non può essere violato **nemmeno se l'avversario dispone di risorse computazionali infinite** (*infinite computational resources*).
- Ciò accade quando il *ciphertext* intercettato non contiene matematicamente informazioni sufficienti per determinare univocamente il *plaintext* (neppure provando tutte le chiavi possibili rimangono molteplici **spurious keys**, chiavi spurie plausibili).
- Il modello matematico formale della sicurezza incondizionata è la **perfect secrecy** (segretezza perfetta di Shannon, studiata nel Capitolo 3), il cui esempio canonico è il **One-time Pad**, il quale richiede tuttavia una chiave casuale lunga quanto l'intero messaggio.
- Nessun *public-key cryptosystem* può mai fornire *unconditional security* (poiché un avversario con potenza di calcolo infinita può cifrare tutti i possibili $x \in \mathcal{P}$ usando la chiave pubblica $e_K$ fino a trovare l'unico $x$ tale che $e_K(x) = y$).

#### 3. Computational Security (Sicurezza Computazionale)
- Poiché la sicurezza incondizionata richiede chiavi scomodamente lunghe, quasi tutti i crittosistemi usati nella pratica si basano sulla **computational security** (sicurezza computazionale).
- Un sistema è **computationally secure** se il miglior algoritmo noto per violarlo richiede una quantità di risorse computazionali (tempo di calcolo o memoria) talmente elevata da risultare **computationally infeasible** (computazionalmente infattibile) per qualsiasi avversario reale (ad esempio $2^{128}$ operazioni).

#### 4. Provable Security e Riduzioni (Sicurezza Dimostrabile)
- Un approccio rigoroso all'interno della *computational security* è la **provable security** (sicurezza dimostrabile): consiste nel fornire una dimostrazione matematica (**reduction**, riduzione) del fatto che violare un dato crittosistema è **almeno tanto difficile quanto risolvere un noto problema matematico ritenuto intrattabile** (come la fattorizzazione di grandi interi per RSA o il calcolo dei logaritmi discreti per ElGamal).
- In questo modo, finché il problema matematico sottostante rimane computazionalmente infattibile, il crittosistema è garantito essere sicuro sotto le ipotesi del modello considerato.

---

### Tabella di Sintesi dei Concetti del Capitolo 1

| **Obiettivo Crittografico**         | **Strumento Secret-key (Simmetrico)**                  | **Strumento Public-key (Asimmetrico)**                                  | **Senza Chiave (Unkeyed)**                      |
| :---------------------------------- | :----------------------------------------------------- | :---------------------------------------------------------------------- | :---------------------------------------------- |
| **Confidentiality (Secrecy)**       | Secret-key Cryptosystem (Block Cipher / Stream Cipher) | Public-key Cryptosystem (es. RSA, ElGamal)                              | —                                               |
| **Data Integrity & Authentication** | Message Authentication Code (**MAC**)                  | **Signature Scheme** (Firma Digitale)                                   | **Hash Function** (Message Digest, se protetto) |
| **Nonrepudiation**                  | ❌ Non garantito (chiave $K$ condivisa tra Alice e Bob) | ✅ Garantito da **Signature Scheme** (chiave privata nota solo ad Alice) | —                                               |
| **Autenticazione Chiavi Pubbliche** | —                                                      | **Certificate** firmato da una **CA**                                   | —                                               |

# Capitolo 2: Crittografia Classica e Crittoanalisi

Il Capitolo 2 introduce la definizione formale di crittosistema, gli strumenti essenziali di matematica discreta (aritmetica modulare e algebra lineare su anelli finiti), i cifrari storici e le tecniche matematico-statistiche per violarli (_crittoanalisi_).

  

## 2.0 Definizione Formale di Crittosistema

> [!abstract] Definizione 2.1: Crittosistema Un **crittosistema** è una 5-tupla $(\mathcal{P}, \mathcal{C}, \mathcal{K}, \mathcal{E}, \mathcal{D})$ che soddisfa le seguenti condizioni:
> 
>   
> 
> 1. $\mathcal{P}$ è un insieme finito di possibili **testi in chiaro** (_plaintexts_).
>     
>       
>     
> 2. $\mathcal{C}$ è un insieme finito di possibili **testi cifrati** (_ciphertexts_).
>     
>       
>     
> 3. $\mathcal{K}$, lo **spazio delle chiavi** (_keyspace_), è un insieme finito di possibili chiavi.
>     
>       
>     
> 4. Per ogni $K \in \mathcal{K}$, esiste una regola di cifratura $e_K \in \mathcal{E}$ e una corrispondente regola di decifratura $d_K \in \mathcal{D}$. Ogni $e_K : \mathcal{P} \to \mathcal{C}$ e $d_K : \mathcal{C} \to \mathcal{P}$ sono funzioni tali che:
>     
>       
>     
>     $$d_K(e_K(x)) = x \quad \forall x \in \mathcal{P}$$
>     

- **Osservazione sull'iniettività:** La proprietà 4 impone che, fissata $K$, la funzione $e_K$ debba essere **iniettiva** ($x_1 \neq x_2 \implies e_K(x_1) \neq e_K(x_2)$).
  Questo perchè altrimenti, se non lo fosse avremmo $x_1 \neq x_2 \implies e_K(x_1) = e_K(x_2)$, ma Bob non avrebbe modo di sapere se Alice ha inviato $x_1$ o $x_2$
    
      
    
- **Chiave Involutoria (Involutory Key):** Una chiave $K$ si dice _involutoria_ se la funzione di cifratura coincide esattamente con quella di decifratura, ovvero $e_K = d_K$.
    
      
    

## 2.1 Matematica Discreta per la Crittografia Classica

### A. Aritmetica Modulare e l'Anello $\mathbb{Z}_{26}$

1. **Operatore `mod`:** Dati un intero $a \in \mathbb{Z}$ e un intero positivo $m > 0$, $a \bmod m$ è il resto della divisione euclidea di $a$ per $m$, ovvero l'unico intero $r \in \{0, 1, \dots, m-1\}$ tale che $a = qm + r$. Formalmente:
    
      
    
    $$a \bmod m = a - \left\lfloor \frac{a}{m} \right\rfloor m$$
    
    - **Attenzione ai numeri negativi:** In crittografia il resto è sempre $\ge 0$. Se $a > 0$ e $a \not\equiv 0 \pmod m$, vale la regola rapida:
        
          
        
        $$(-a) \bmod m = m - (a \bmod m)$$
        
        (Esempio: $(-11) \bmod 26 = 26 - 11 = 15$).
        
          
        
2. **Congruenza Modulo $m$:** Si scrive $a \equiv b \pmod m$ se e solo se $a \bmod m = b \bmod m$, che equivale a dire che $m$ divide la differenza $(a - b)$.
    
      
    
3. **L'anello $\mathbb{Z}_m$ e la corrispondenza alfabetica ($\mathbb{Z}_{26}$):** L'insieme $\mathbb{Z}_m = \{0, 1, \dots, m-1\}$ dotato di addizione e moltiplicazione ridotte modulo $m$ forma un anello commutativo. Nei cifrari alfabetici inglesi si usa $\mathbb{Z}_{26}$ con la mappatura standard:
    
      
    

|**A**|**B**|**C**|**D**|**E**|**F**|**G**|**H**|**I**|**J**|**K**|**L**|**M**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0|1|2|3|4|5|6|7|8|9|10|11|12|

|**N**|**O**|**P**|**Q**|**R**|**S**|**T**|**U**|**V**|**W**|**X**|**Y**|**Z**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|13|14|15|16|17|18|19|20|21|22|23|24|25|

### B. Inverso Moltiplicativo e Funzione $\phi$ di Eulero

- **Definizione:** L'inverso moltiplicativo di $a \in \mathbb{Z}_m$, indicato con $a^{-1} \bmod m$, è quell'elemento (se esiste) tale che $a \cdot a^{-1} \equiv 1 \pmod m$.
    
      
    
- **Condizione di Esistenza (Teorema Fondamentale):** Un elemento $a \in \mathbb{Z}_m$ possiede inverso moltiplicativo modulo $m$ **se e solo se** $a$ e $m$ sono coprimi (primi tra loro):
    
      
    
    $$\gcd(a, m) = 1$$
    
- **Quanti sono gli elementi invertibili?** Il numero di elementi in $\mathbb{Z}_m$ coprimi con $m$ è dato dalla **Funzione $\phi$ di Eulero**: se $m = p_1^{e_1} p_2^{e_2} \dots p_k^{e_k}$, allora $\phi(m) = \prod_{i=1}^k (p_i^{e_i} - p_i^{e_i - 1})$. Per $m = 26 = 2 \times 13$, abbiamo $\phi(26) = (2-1)(13-1) = \mathbf{12}$ elementi invertibili (tutti i numeri dispari tranne il 13).
    
      
    
- **Tabella degli inversi moltiplicativi in $\mathbb{Z}_{26}$:**
    
      
    
      
    

|**a**|**1**|**3**|**5**|**7**|**9**|**11**|**15**|**17**|**19**|**21**|**23**|**25**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**$a^{-1} \bmod 26$**|1|9|21|15|3|19|7|23|11|5|17|25|

### C. Algebra Lineare su $\mathbb{Z}_{26}$ (Matrici, Determinante e Inversa)

1. **Prodotto tra Matrici:** Data una matrice $A = (a_{i,j})$ di dimensione $\ell \times m$ e una matrice $B = (b_{j,k})$ di dimensione $m \times n$, il prodotto $AB = (c_{i,k})$ è una matrice $\ell \times n$ i cui elementi si ottengono moltiplicando la riga $i$-esima di $A$ per la colonna $k$-esima di $B$ modulo 26:
    
      
    
    $$c_{i,k} = \left( \sum_{j=1}^m a_{i,j} b_{j,k} \right) \bmod 26$$
    
2. **Determinante e Condizione di Invertibilità:** Una matrice quadrata $K$ di dimensione $m \times m$ a coefficienti in $\mathbb{Z}_{26}$ ammette matrice inversa $K^{-1} \pmod{26}$ (tale che $K K^{-1} \equiv K^{-1} K \equiv I_m \pmod{26}$) **se e solo se il suo determinante è invertibile modulo 26**:
    
      
    
    $$\gcd(\det K, 26) = 1$$
    
3. **Calcolo della Matrice Inversa $K^{-1} \bmod 26$:**
    
      
    - **Caso generale ($m \times m$):**
        
          
        
        $$K^{-1} = (\det K)^{-1} \cdot K^* \bmod 26$$
        
        dove $(\det K)^{-1}$ è l'inverso moltiplicativo del determinante in $\mathbb{Z}_{26}$ e $K^* = \text{adj}(K)$ è la **matrice aggiunta**, ovvero la trasposta della matrice dei cofattori $C_{i,j} = (-1)^{i+j} \det(M_{i,j})$.
        
          
        
    - **Caso $2 \times 2$ (Corollario 2.4 - Formula Rapida):** Sia $K = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$. Il determinante è $\det K = (ad - bc) \bmod 26$. Se $\gcd(\det K, 26) = 1$, vale:
        
          
        
        $$K^{-1} = (ad - bc)^{-1} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} \bmod 26$$
        

## 2.2 Tutti i Crittosistemi Classici (con gli Esempi del Libro)

### 1. Shift Cipher (Cifrario a Scorrimento / di Cesare)

- **Definizione (Cryptosystem 2.1):** $\mathcal{P} = \mathcal{C} = \mathcal{K} = \mathbb{Z}_{26}$. Per una chiave $K \in \mathbb{Z}_{26}$:
    
      
    
    $$e_K(x) = (x + K) \bmod 26 \qquad d_K(y) = (y - K) \bmod 26$$
    
- **Meccanica e Spazio delle chiavi:** Trasla ciclicamente ogni lettera in avanti nell'alfabeto di $K$ posizioni (se $K=3$ si ha il cifrario di Cesare). $|\mathcal{K}| = 26$.
    
      
    

> [!example] Example 2.1 (Cifratura e Decifratura con lo Shift Cipher) Supponiamo che la chiave sia $K = 11$ e il testo in chiaro sia `wewillmeetatmidnight`.
> 
>   
> 
> 1. Convertiamo il plaintext in una sequenza di interi in $\mathbb{Z}_{26}$: `22 4 22 8 11 11 12 4 4 19 0 19 12 8 3 13 8 6 7 19`
>     
>       
>     
> 2. Sommiamo $11$ a ciascun valore riducendo modulo 26: `7 15 7 19 22 22 23 15 15 4 11 4 23 19 14 24 19 17 18 4`
>     
>       
>     
> 3. Riconvertiamo in caratteri alfabetici maiuscoli ottenendo il ciphertext: `HPHTWWXPPELEXTOYTRSE` Per decifrare, Bob converte il ciphertext in interi, sottrae $11$ modulo 26 e riconverte in lettere.
>     
>       
>     

> [!example] Example 2.2 (Attacco di Ricerca Esaustiva sullo Shift Cipher) Dato il testo cifrato `JBCRCLQRWCRVNBJENBWRWN`, proviamo in sequenza le chiavi di decifratura $d_0, d_1, d_2, \dots$ sottraendo $0, 1, 2, \dots$ modulo 26:
> 
>   
> 
> - $K = 0$: `jbcrclqrwcrvnbjenbwrwn`
>     
>       
>     
>       
>     
> - $K = 1$: `iabqbkpqvbqumaidmavqvm`
>     
>       
>     
>       
>     
> - $K = 2$: `hzapajopuaptlzhclzupul`
>     
>       
>     
>       
>     
> - $K = 3$: `gyzozinotzoskygbkytotk`
>     
>       
>     
>       
>     
> - $K = 4$: `fxynyhmnsynrjxfajxsnsj`
>     
>       
>     
>       
>     
> - $K = 5$: `ewxmxglmrxmqiweziwrmri`
>     
>       
>     
>       
>     
> - $K = 6$: `dvwlwfklqwlphvdyhvqlqh`
>     
>       
>     
>       
>     
> - $K = 7$: `cuvkvejkpvkogucxgupkpg`
>     
>       
>     
>       
>     
> - $K = 8$: `btujudijoujnftbwftojof`
>     
>       
>     
>       
>     
> - $K = 9$: `astitchintimesavesnine` ("a stitch in time saves nine"). Ci fermiamo: il testo in chiaro è stato individuato e la chiave è $K = 9$ (in media servono $26/2 = 13$ tentativi).
>     
>       
>     

### 2. Substitution Cipher (Cifrario a Sostituzione Monoalfabetica)

- **Definizione (Cryptosystem 2.2):** $\mathcal{P} = \mathcal{C} = \mathbb{Z}_{26}$. Lo spazio delle chiavi $\mathcal{K}$ è costituito da tutte le possibili **permutazioni** $\pi$ dei 26 caratteri alfabetici:
    
      
    
    $$e_\pi(x) = \pi(x) \qquad d_\pi(y) = \pi^{-1}(y)$$
    
- **Spazio delle chiavi:** $|\mathcal{K}| = 26! \approx 4.03 \times 10^{26}$. La ricerca esaustiva è totalmente infattibile.
    
      
    

> [!example] Esempio di Tabella di Sostituzione $\pi$ e $\pi^{-1}$ Una chiave $\pi$ viene specificata scrivendo una tabella di corrispondenza (in lettere o in numeri su $\mathbb{Z}_{26}$, come nell'Esercizio 2.29 dove $\pi(0)=23, \pi(1)=13, \pi(2)=24, \pi(3)=0, \dots$). Per cifrare si legge dalla prima riga alla seconda ($y = \pi(x)$); per decifrare si costruisce la tabella inversa $\pi^{-1}$ leggendo dalla seconda riga alla prima ($x = \pi^{-1}(y)$).
> 
>   

### 3. Affine Cipher (Cifrario Affine)

- **Definizione (Cryptosystem 2.3):** $\mathcal{P} = \mathcal{C} = \mathbb{Z}_{26}$ e $\mathcal{K} = \{(a, b) \in \mathbb{Z}_{26} \times \mathbb{Z}_{26} : \gcd(a, 26) = 1\}$.
    
      
    
    $$e_K(x) = (ax + b) \bmod 26 \qquad d_K(y) = a^{-1}(y - b) \bmod 26$$
    
- **Spazio delle chiavi:** Ci sono $\phi(26) = 12$ scelte valide per $a$ e $26$ scelte per $b$, quindi $|\mathcal{K}| = 12 \times 26 = \mathbf{312}$ chiavi totali.
    
      
    

> [!example] Example 2.3 (Cifratura e Decifratura con l'Affine Cipher) Sia la chiave $K = (7, 3)$ (valida perché $\gcd(7, 26) = 1$). Vogliamo cifrare il plaintext `hot`:
> 
>   
> 
> 1. Convertiamo `hot` nei tre interi in $\mathbb{Z}_{26}$: $7, 14, 19$.
>     
>       
>     
> 2. Applichiamo $e_K(x) = (7x + 3) \bmod 26$:
>     
>       
>     - $(7 \times 7 + 3) \bmod 26 = 52 \bmod 26 = 0$ (`A`)
>         
>           
>         
>     - $(7 \times 14 + 3) \bmod 26 = 101 \bmod 26 = 23$ (`X`)
>         
>           
>         
>     - $(7 \times 19 + 3) \bmod 26 = 136 \bmod 26 = 6$ (`G`)
>         
>           
>         
> 3. Il testo cifrato risultante è `AXG`.
>     
>       
>     
> 4. **Decifratura:** Poiché $7^{-1} \bmod 26 = 15$, la funzione di decifratura è $d_K(y) = 15(y - 3) \bmod 26 = (15y - 45) \bmod 26 = (15y + 7) \bmod 26$. Applicandola a $0, 23, 6$ si riottiene $7, 14, 19$ (`hot`).
>     
>       
>     

### 4. Vigenère Cipher (Cifrario Polialfabetico di Vigenère)

- **Definizione (Cryptosystem 2.4):** Fissato un intero $m \ge 1$ (lunghezza della parola chiave), $\mathcal{P} = \mathcal{C} = \mathcal{K} = (\mathbb{Z}_{26})^m$. Per una chiave $K = (k_1, k_2, \dots, k_m)$:
    
      
    
    $$e_K(x_1, x_2, \dots, x_m) = (x_1 + k_1, x_2 + k_2, \dots, x_m + k_m) \bmod 26$$
    
    $$d_K(y_1, y_2, \dots, y_m) = (y_1 - k_1, y_2 - k_2, \dots, y_m - k_m) \bmod 26$$
    
- **Spazio delle chiavi:** $|\mathcal{K}| = 26^m$ --> no ricerca esaustiva
- Questo cristtosistema è polialfabetico: uno stesso carattere alfabetico può essere mappato in più caratteri alfabetici diversi per via della keyword
    
      
    

> [!example] Example 2.4 (Cifratura e Decifratura con il Vigenère Cipher)
> 
> Supponiamo che la keyword sia `CIPHER` ($m = 6$), che corrisponde al vettore numerico $K = (2, 8, 15, 7, 4, 17)$, e che il plaintext sia `thiscryptosystemisnotsecure`.
> 
>   
> 
> 1. Dividiamo il plaintext in gruppi di $m = 6$ lettere convertite in numeri e sommiamo sotto ciascuno la chiave $K$ modulo 26:
>     
>       
>     - Plaintext: `19 7 8 18 2 17` | `24 15 19 14 18 24` | `18 19 4 12 8 18` | `13 14 19 18 4 2` | `20 17 4`
>         
>           
>         
>     - Keyword: `2 8 15 7 4 17` | `2 8 15 7 4 17` | `2 8 15 7 4 17` | `2 8 15 7 4 17` | `2 8 15`
>         
>           
>         
>     - Somma mod 26: `21 15 23 25 6 8` | `0 23 8 21 22 15` | `20 1 19 19 12 9` | `15 22 8 25 8 19` | `22 25 19`
>         
>           
>         
> 2. Convertendo in lettere maiuscole, il testo cifrato è:
>     
>     `VPXZGIAXIVWPUBTTMJPWIZITWZT`
>     
>     Per decifrare si sottrae ciclicamente $(2, 8, 15, 7, 4, 17)$ modulo 26.
>     
>       
>     

### 5. Hill Cipher (Cifrario di Hill)

- **Definizione (Cryptosystem 2.5):** Sia $m \ge 2$ un intero. $\mathcal{P} = \mathcal{C} = (\mathbb{Z}_{26})^m$ e $\mathcal{K} = \{\text{matrici invertibili } m \times m \text{ su } \mathbb{Z}_{26}\}$. Dati i vettori riga $x, y \in (\mathbb{Z}_{26})^m$:
    
      
    
    $$e_K(x) = xK \bmod 26 \qquad d_K(y) = yK^{-1} \bmod 26$$
    Questo crittosistema è polialfabetico

> [!example] Example 2.5 (Cifratura e Decifratura Hill Cipher con matrice $2 \times 2$) Supponiamo che la chiave sia $K = \begin{pmatrix} 11 & 8 \\ 3 & 7 \end{pmatrix}$.
> 
>   
> 
> 1. **Verifica di invertibilità e calcolo di $K^{-1}$:** $\det K = (11 \times 7 - 8 \times 3) \bmod 26 = (77 - 24) \bmod 26 = 53 \bmod 26 = 1$. Poiché $\gcd(1, 26) = 1$, $K$ è invertibile e $1^{-1} = 1$. Quindi:
>     
>       
>     
>     $$K^{-1} = \begin{pmatrix} 7 & -8 \\ -3 & 11 \end{pmatrix} \bmod 26 = \begin{pmatrix} 7 & 18 \\ 23 & 11 \end{pmatrix}$$
>     
>       
>     
> 2. **Cifratura di `july`:** Dividiamo in due blocchi di lunghezza 2: `ju` $= (9, 20)$ e `ly` $= (11, 24)$.
>     
>       
>     
>     $$(9, 20) \begin{pmatrix} 11 & 8 \\ 3 & 7 \end{pmatrix} = (99 + 60, 72 + 140) = (159, 212) \equiv (3, 4) \pmod{26}$$
>     
>       
>     
>     $$(11, 24) \begin{pmatrix} 11 & 8 \\ 3 & 7 \end{pmatrix} = (121 + 72, 88 + 168) = (193, 256) \equiv (11, 22) \pmod{26}$$
>     
>       
>     
>     Il testo cifrato corrispondente a $(3, 4)$ e $(11, 22)$ è `DELW`.
>     
>       
>     
> 3. **Decifratura:** Bob moltiplica per $K^{-1}$:
>     
>       
>     
>     $$(3, 4) \begin{pmatrix} 7 & 18 \\ 23 & 11 \end{pmatrix} \equiv (9, 20) \pmod{26} \quad \text{e} \quad (11, 22) \begin{pmatrix} 7 & 18 \\ 23 & 11 \end{pmatrix} \equiv (11, 24) \pmod{26}$$
>     
>       
>     

> [!example] Example 2.6 (Calcolo dell'inversa di una matrice $3 \times 3$ su $\mathbb{Z}_{26}$) Sia data la matrice chiave $3 \times 3$ con entrate in $\mathbb{Z}_{26}$:
> 
>   
> 
> $$K = \begin{pmatrix} 10 & 5 & 12 \\ 3 & 14 & 21 \\ 8 & 9 & 11 \end{pmatrix}$$
> 
>   
> 
> 4. **Determinante:** Calcolando il determinante e riducendo modulo 26 si ottiene $\det K = 7$. In $\mathbb{Z}_{26}$ l'inverso moltiplicativo è $7^{-1} \bmod 26 = 15$.
>     
>       
>     
> 5. **Matrice aggiunta $K^*$:** Calcolando i cofattori trasposti modulo 26 si ottiene:
>     
>       
>     
>     $$K^* = \begin{pmatrix} 17 & 1 & 15 \\ 5 & 14 & 8 \\ 19 & 2 & 21 \end{pmatrix}$$
>     
>       
>     
> 6. **Matrice inversa $K^{-1}$:** Moltiplicando $K^*$ per $15$ modulo 26:
>     
>       
>     
>     $$K^{-1} = 15 K^* \bmod 26 = \begin{pmatrix} 21 & 15 & 17 \\ 23 & 2 & 16 \\ 25 & 4 & 3 \end{pmatrix}$$
>     
>       
>     

### 6. Permutation Cipher (Cifrario a Permutazione / Trasposizione)

- **Definizione (Cryptosystem 2.6):** Sia $m \ge 2$. $\mathcal{P} = \mathcal{C} = (\mathbb{Z}_{26})^m$ e $\mathcal{K}$ consiste di tutte le permutazioni $\pi$ dell'insieme di indici $\{1, 2, \dots, m\}$.
    
      
    
    $$e_\pi(x_1, \dots, x_m) = (x_{\pi(1)}, \dots, x_{\pi(m)}) \qquad d_\pi(y_1, \dots, y_m) = (y_{\pi^{-1}(1)}, \dots, y_{\pi^{-1}(m)})$$
    
- **Il Permutation Cipher come caso speciale dell'Hill Cipher:** Data una permutazione $\pi$ di $\{1, \dots, m\}$, la matrice di permutazione associata $K_\pi = (k_{i,j})$ di dimensione $m \times m$ ha $k_{i,j} = 1$ se $i = \pi(j)$ e $0$ altrimenti, con inversa $K_\pi^{-1} = K_\pi^T$.
    
      
    

> [!example] Example 2.7 (Cifratura con il Permutation Cipher) Sia $m = 6$ e sia la chiave $\pi$ definita dalla permutazione: $\pi(1)=3, \pi(2)=5, \pi(3)=1, \pi(4)=6, \pi(5)=4, \pi(6)=2$. Dato il plaintext `shesellsseashellsbytheseashore`:
> 
>   
> 
> 1. Partizioniamo il plaintext in gruppi di 6 lettere: `shesel | lsseas | hellsb | ythese | ashore`
>     
>       
>     
> 2. Riorganizziamo le lettere di ciascun blocco secondo $\pi$ (la 1ª lettera va in posizione $\pi(1)=3$, la 3ª va in posizione $\pi(3)=1$, ecc.): `EESLSH | SALSES | LSHBLE | HSYEET | HRAEOS`
>     
>       
>     
> 3. Il testo cifrato è `EESLSHSALSESLSHBLEHSYEETHRAEOS`. Si decifra applicando la permutazione inversa $\pi^{-1}$.
>     
>       
>     

### 7. Stream Ciphers: Synchronous Stream Ciphers, Autokey Cipher e LFSR

#### A. Definizione di Synchronous Stream Cipher (Cifrario a Flusso Sincrono)

L'idea di base consiste nel generare un **keystream** $\mathbf{z} = z_1 z_2 \dots$ e utilizzarlo per cifrare una stringa di testo in chiaro $\mathbf{x} = x_1 x_2 \dots$ secondo la regola:

$$y_1 y_2 \dots = e_{z_1}(x_1) e_{z_2}(x_2) \dots$$

> [!abstract] Definition 2.6: Synchronous Stream Cipher Un **synchronous stream cipher** è una tupla $(\mathcal{P}, \mathcal{C}, \mathcal{K}, \mathcal{L}, \mathcal{E}, \mathcal{D})$, insieme a una funzione $g$, tale che siano soddisfatte le seguenti condizioni:
> 
> 1. $\mathcal{P}$ è un insieme finito di possibili **plaintexts** (testi in chiaro).
>     
> 2. $\mathcal{C}$ è un insieme finito di possibili **ciphertexts** (testi cifrati).
>     
> 3. $\mathcal{K}$, il **keyspace** (spazio delle chiavi), è un insieme finito di possibili chiavi.
>     
> 4. $\mathcal{L}$ è un insieme finito chiamato **keystream alphabet** (alfabeto del keystream).
>     
> 5. $g$ è il **keystream generator** (generatore del keystream). $g$ prende in input una chiave $K$ e genera una stringa infinita $z_1 z_2 \dots$ chiamata **keystream**, dove $z_i \in \mathcal{L}$ per ogni $i \ge 1$.
>     
> 6. Per ogni $z \in \mathcal{L}$, esiste una **encryption rule** (regola di cifratura) $e_z \in \mathcal{E}$ e una corrispondente **decryption rule** (regola di decifratura) $d_z \in \mathcal{D}$. $e_z : \mathcal{P} \to \mathcal{C}$ e $d_z : \mathcal{C} \to \mathcal{P}$ sono funzioni tali che $d_z(e_z(x)) = x$ per ogni elemento di testo in chiaro $x \in \mathcal{P}$.
>     

- **Differenza tra Stream Cipher Sincrono, Periodico e Non-sincrono:**
    
    - In un **synchronous stream cipher**, il keystream viene generato unicamente a partire dalla chiave $K$ ed è completamente indipendente dalla stringa di testo in chiaro.
        
    - Un cifrario a flusso si dice **periodic stream cipher** con **period** $d$ se il keystream ripete se stesso dopo $d$ caratteri, cioè se $z_{i+d} = z_i$ per ogni $i \ge 1$ (ad esempio, il _Vigenère Cipher_ con keyword di lunghezza $m$ può essere visto come un _periodic stream cipher_ con periodo $m$).
        
    - Un **non-synchronous stream cipher** è uno stream cipher in cui ciascun elemento del keystream $z_i$ dipende dai precedenti elementi del plaintext o del ciphertext ($x_1, \dots, x_{i-1}$ oppure $y_1, \dots, y_{i-1}$) oltre che dalla chiave $K$. Un esempio semplice è l'**Autokey Cipher** (_Cryptosystem 2.7_): $\mathcal{P} = \mathcal{C} = \mathcal{K} = \mathcal{L} = \mathbb{Z}_{26}$, con $z_1 = K$ e $z_i = x_{i-1}$ per ogni $i \ge 2$, dove $e_z(x) = (x + z) \bmod 26$ e $d_z(y) = (y - z) \bmod 26$.
        

> [!example] Example 2.9 (Cifratura e Decifratura con l'Autokey Cipher) Supponiamo che la chiave sia $K = 8$ e il plaintext sia `rendezvous`.
> 
> 1. Convertiamo `rendezvous` in una sequenza di interi in $\mathbb{Z}_{26}$: `17 4 13 3 4 25 21 14 20 18`.
>     
> 2. Il keystream ($z_1 = 8$, seguito dagli elementi del plaintext) è: `8 17 4 13 3 4 25 21 14 20`.
>     
> 3. Sommando gli elementi corrispondenti e riducendo modulo 26 otteniamo: `25 21 17 16 7 3 20 9 8 12` $\longrightarrow$ in forma alfabetica: `ZVRQHDUJIM`.
>     
> 4. **Decifratura:** Partendo da `25 21 17 16 7 3 20 9 8 12` e $K=8$:
>     
>     - $x_1 = d_8(25) = (25 - 8) \bmod 26 = 17$ (`r`)
>         
>     - $x_2 = d_{17}(21) = (21 - 17) \bmod 26 = 4$ (`e`)
>         
>     - $x_3 = d_4(17) = (17 - 4) \bmod 26 = 13$ (`n`), e così via.
>         

#### B. Generazione di un Keystream Sincrono su Alfabeti Binari ($\mathbb{Z}_2$) e LFSR

Gli stream ciphers sono spesso descritti in termini di **binary alphabets** (alfabeti binari), ovvero $\mathcal{P} = \mathcal{C} = \mathcal{L} = \mathbb{Z}_2$. In questo caso, le operazioni di cifratura e decifratura sono semplicemente l'addizione modulo 2:

$$e_z(x) = (x + z) \bmod 2 \qquad \text{e} \qquad d_z(y) = (y + z) \bmod 2$$

Se associamo `0` al valore booleano "false" e `1` a "true", l'addizione modulo 2 corrisponde all'operazione di **exclusive-or** (XOR, indicata con $\oplus$). Pertanto, la cifratura e la decifratura possono essere implementate in modo molto efficiente in hardware.

Vediamo come generare un keystream sincrono lavorando su alfabeti binari a partire da una chiave ridotta:

1. **Linear Recurrence (Ricorrenza Lineare) di grado $m$:** Supponiamo di partire da una **$m$-tupla binaria** $(k_1, \dots, k_m) \in (\mathbb{Z}_2)^m$ e poniamo i primi $m$ termini del keystream uguali a:
    
    $$z_i = k_i, \quad 1 \le i \le m$$
    
    Generiamo i termini successivi del keystream usando una **linear recurrence** (ricorrenza lineare) di **degree** (grado) $m$:
    
    $$z_{i+m} = \sum_{j=0}^{m-1} c_j z_{i+j} \bmod 2 \quad \forall i \ge 1$$
    
    dove $c_0, \dots, c_{m-1} \in \mathbb{Z}_2$ sono costanti specificate (**specified constants**).
    
    - **Perché si chiama così (_Remark_ del libro):** Questa ricorrenza si dice avere **degree $m$** (grado $m$) poiché ciascun termine dipende dai precedenti $m$ termini. Si chiama **linear recurrence** perché $z_{i+m}$ è una funzione lineare dei termini precedenti. Si noti che possiamo assumere $c_0 = 1$ senza perdita di generalità (_without loss of generality_), poiché altrimenti la ricorrenza sarebbe di grado al più $m - 1$.
        
2. **La Chiave $K$, l'Initialization Vector e il Periodo del Keystream:**
    
    - In questo schema, la chiave $K$ può essere vista come costituita dai $2m$ valori $(k_1, \dots, k_m, c_0, \dots, c_{m-1})$.
        
    - Il vettore iniziale $(k_1, \dots, k_m)$ è chiamato **initialization vector**.
        
    - Se $(k_1, \dots, k_m) = (0, \dots, 0)$, allora il keystream consiste interamente di `0`: questo va ovviamente evitato, poiché in tal caso il ciphertext risulterebbe identico al plaintext.
        
    - Tuttavia, se le costanti $c_0, \dots, c_{m-1}$ sono scelte in modo opportuno, allora qualsiasi altro **initialization vector** $(k_1, \dots, k_m) \neq (0, \dots, 0)$ darà origine a un **periodic keystream** avente **period** $2^m - 1$. In questo modo, una chiave "corta" può generare un keystream con un periodo lunghissimo (proprietà molto desiderabile, dato che un keystream con periodo corto è vulnerabile come nel caso del Vigenère Cipher). Qualsiasi altro _non-zero initialization vector_ produrrà semplicemente una **cyclic permutation** (permutazione ciclica) dello stesso keystream.
        
3. **Implementazione Hardware tramite Linear Feedback Shift Register (LFSR):** Un altro aspetto molto vantaggioso di questo metodo è che il keystream può essere prodotto in modo estremamente efficiente in hardware usando un **linear feedback shift register**, o **LFSR**:
    
    - Si utilizza uno **shift register** (registro a scorrimento) dotato di $m$ **stages** (stadi).
        
    - Il vettore $(k_1, \dots, k_m)$ viene utilizzato per inizializzare lo shift register.
        
    - Ad ogni **time unit** (unità di tempo), vengono eseguite concorrentemente le seguenti tre operazioni:
        
        1. $k_1$ viene prelevato (**tapped**) come successivo bit del keystream;
            
        2. $k_2, \dots, k_m$ vengono ciascuno fatti scorrere di uno stadio verso sinistra (**shifted one stage to the left**);
            
        3. il "nuovo" valore di $k_m$ viene calcolato come:
            
            $$\sum_{j=0}^{m-1} c_j k_{j+1} \bmod 2$$
            
            (questo è il **"linear feedback"**, ovvero la retroazione lineare).
            
    - In qualsiasi istante di tempo, lo shift register contiene $m$ elementi consecutivi del keystream, diciamo $z_i, \dots, z_{i+m-1}$. Dopo una _time unit_, lo shift register contiene $z_{i+1}, \dots, z_{i+m}$.
        
    - Si osservi che il **linear feedback** viene realizzato prelevando (_tapping_) determinati stadi del registro (esattamente quelli specificati dalle costanti $c_j$ che hanno valore `1`) e calcolando una somma modulo 2 (che equivale a un _exclusive-or_).
        

> [!example] Example 2.8 (Generazione del Keystream con un LFSR a 4 stages) Supponiamo che $m = 4$ e che il keystream sia generato usando la _linear recurrence_:
> 
> $$z_{i+4} = (z_i + z_{i+1}) \bmod 2, \quad i \ge 1$$
> 
> (Qui le costanti sono $c_0 = 1, c_1 = 1, c_2 = 0, c_3 = 0$; nell'LFSR della Figura 2.2 del libro vengono quindi prelevati gli stadi $k_1$ e $k_2$ per calcolare tramite somma modulo 2 il nuovo valore di $k_4$). Se il keystream viene inizializzato con qualsiasi vettore diverso da $(0, 0, 0, 0)$, otteniamo un keystream di **period** $2^4 - 1 = 15$. Ad esempio, partendo con $(z_1, z_2, z_3, z_4) = (1, 0, 0, 0)$, i bit successivi sono:
> 
> - $z_5 = (z_1 + z_2) \bmod 2 = (1 + 0) \bmod 2 = 1$ (lo shift register passa da `1000` a `0001`)
>     
> - $z_6 = (z_2 + z_3) \bmod 2 = (0 + 0) \bmod 2 = 0$ (lo shift register contiene `0010`)
>     
> - $z_7 = (z_3 + z_4) \bmod 2 = (0 + 0) \bmod 2 = 0$ (lo shift register contiene `0100`)
>     
> - $z_8 = (z_4 + z_5) \bmod 2 = (0 + 1) \bmod 2 = 1$ (lo shift register contiene `1001`)
>     
> 
> Continuando, il keystream prodotto è:
> 
> $$1 \ 0 \ 0 \ 0 \ 1 \ 0 \ 0 \ 1 \ 1 \ 0 \ 1 \ 0 \ 1 \ 1 \ 1 \ \dots$$
> 
> Qualsiasi altro _non-zero initialization vector_ darà origine a una _cyclic permutation_ (permutazione ciclica) di questo stesso keystream.

## 2.3 Crittoanalisi dei Cifrari Classici (con gli Esempi del Libro)

> [!tip] Fondamento Statistico (Analisi delle Frequenze in Inglese)
> 
>   
> 
> - **Gruppo 1 (Altissima frequenza):** `E` ($\approx 12.7\%$), seguita da `T, A, O, I, N, S, H, R` ($\approx 6\% - 9\%$).
>     
>       
>     
> - **Gruppo 2 (Media frequenza):** `D, L, C, U, M, W, F, G, Y, P, B` ($\approx 1.5\% - 4\%$).
>     
>       
>     
> - **Gruppo 3 (Bassa frequenza):** `V, K, J, X, Q, Z` ($< 1\%$).
>     
>       
>     
> - **Digrammi più comuni:** `TH, HE, IN, ER, AN, RE, ED, ON, ES, ST, EN, AT, TO, NT, HA, ND, OU`.
>     
>       
>     
> - **Trigrammi più comuni:** `THE, ING, AND, HER, ERE, ENT, THA, NTH, WAS, ETH, FOR, DTH`.
>     
>       
>     

### 1. Crittoanalisi dell'Affine Cipher (Ciphertext-Only)

Con l'analisi delle frequenze bastano **due sole corrispondenze** per risolvere un sistema lineare modulo 26 nelle incognite $(a, b)$.

  

> [!example] Example 2.10 (Crittoanalisi completa di un Affine Cipher)
> 
> Supponiamo di intercettare un testo cifrato di 57 caratteri (Tabella 2.3 del libro) in cui le lettere più frequenti sono: **`R` (8 occorrenze), `D` (7), `E, H, K` (5 ciascuna)**.
> 
>   
> 
> 1. **Primo tentativo:** Ipotizziamo che `R` ($17$) sia la cifratura di `e` ($4$) e `D` ($3$) sia la cifratura di `t` ($19$):
>     
>       
>     
>     $$\begin{cases} 4a + b \equiv 17 \pmod{26} \\ 19a + b \equiv 3 \pmod{26} \end{cases} \implies 15a \equiv -14 \equiv 12 \pmod{26}$$
>     
>     Moltiplicando per $15^{-1} \bmod 26 = 7$, otteniamo $a = (7 \times 12) \bmod 26 = 6$. Ma $\gcd(6, 26) = 2 \neq 1$: chiave **invalida**, scartiamo l'ipotesi.
>     
>       
>     
> 2. **Secondo tentativo:** Ipotizziamo $e_K(\text{e}) = \text{R}$ ($17$) e $e_K(\text{t}) = \text{E}$ ($4$):
>     
>       
>     
>     $$15a \equiv 4 - 17 \equiv -13 \equiv 13 \pmod{26} \implies a = 13 \quad (\gcd(13, 26) = 13 \neq 1, \text{ invalida}).$$
>     
> 3. **Terzo tentativo:** Ipotizziamo $e_K(\text{e}) = \text{R}$ ($17$) e $e_K(\text{t}) = \text{H}$ ($7$):
>     
>       
>     
>     $$15a \equiv 7 - 17 \equiv -10 \equiv 16 \pmod{26} \implies a = (7 \times 16) \bmod 26 = 8 \quad (\gcd(8, 26) = 2 \neq 1, \text{ invalida}).$$
>     
> 4. **Quarto tentativo (Successo):** Ipotizziamo $e_K(\text{e}) = \text{R}$ ($17$) e $e_K(\text{t}) = \text{K}$ ($10$):
>     
>       
>     
>     $$\begin{cases} 4a + b \equiv 17 \pmod{26} \\ 19a + b \equiv 10 \pmod{26} \end{cases} \implies 15a \equiv 10 - 17 \equiv -7 \equiv 19 \pmod{26}$$
>     
>     Moltiplicando per $15^{-1} = 7$: $a = (7 \times 19) \bmod 26 = 133 \bmod 26 = \mathbf{3}$ (valida perché $\gcd(3, 26) = 1$).
>     
>     Sostituendo nella prima equazione: $12 + b \equiv 17 \pmod{26} \implies b = \mathbf{5}$.
>     
>       
>     
> 5. **Decifratura:** Con $K = (3, 5)$ e $3^{-1} \bmod 26 = 9$, calcoliamo $d_K(y) = 9(y - 5) \bmod 26 = (9y - 19) \bmod 26$, ottenendo il plaintext inglese: `"algorithmsarequitegeneraldefinitionsofarithmeticprocesses"`.
>     
>       
>     

### 2. Crittoanalisi del Substitution Cipher (Ciphertext-Only)

Con $26!$ chiavi si procede per analisi statistica su lettere singole, digrammi, trigrammi e struttura vocalica/consonantica.

  

> [!example] Example 2.11 (Crittoanalisi di un Substitution Cipher) Dato il crittogramma di 4 righe (`YIFQFMZRWQFYVECFMDZPCVMRZWNMDZ...`):
> 
>   
> 
> 1. **Scoperta della `e`:** La lettera `Z` è nettamente la più frequente nel testo cifrato, quindi poniamo $d_K(\text{Z}) = \text{e}$.
>     
>       
>     
> 2. **Analisi dei digrammi con `Z`:** I digrammi `ZW`, `NZ`, `DZ`, `MZ` sono molto frequenti, e compare il trigramma `ZRW` seguito da `RW`. Poiché `nd` è un digramma molto comune e `end` è un trigramma frequente, ipotizziamo $d_K(\text{R}) = \text{n}$ e $d_K(\text{W}) = \text{d}$.
>     
>       
>     
> 3. **Scoperta di `h` e `a`:** Poiché `NZ` è comune mentre `ZN` non appare mai, e sappiamo che $d_K(\text{Z}) = \text{e}$, deduciamo $d_K(\text{N}) = \text{h}$ (formando `he`). Notando poi i pattern `RNM` (`nh-`) a inizio parola e `NMDZ` (`h--e`), la lettera `M` deve essere una vocale; confrontando i digrammi, poniamo $d_K(\text{M}) = \text{a}$ e $d_K(\text{D}) = \text{v}$ (ottenendo `have`).
>     
>       
>     
> 4. **Completamento con `i` e `o`:** Sostituendo $d_K(\text{C}) = \text{i}$ e poi $d_K(\text{Y}) = \text{o}$ (evitando sequenze impossibili di tre vocali come `aoi` da `CFM` o `CJM`), emergono frammenti trasparenti come `hs-r-riseasi-e-a-orationhadta-en--ace-hi-e`.
>     
>       
>     
> 5. **Decifratura completa:** _"Our friend from Paris examined his empty glass with surprise, as if evaporation had taken place while he wasn't looking. I poured some more wine and he settled back in his chair, face tilted up towards the sun."_.
>     
>       
>     

### 3. Crittoanalisi del Vigenère Cipher (Ciphertext-Only)

- **Fase 1A (Test di Kasiski):** Si cercano sottostringhe identiche di lunghezza $\ge 3$ con l'occorrenza più alta, si calcolano le distanze $\delta_i$ tra le loro posizioni e si trova $m = \gcd(\delta_1, \delta_2, \dots)$.
    
      
    
- **Fase 1B (Indice di Coincidenza $I_c$):**
    
      
    
    $$I_c(\mathbf{x}) = \frac{\sum_{i=0}^{25} f_i(f_i - 1)}{n(n - 1)}$$
    
    Vale $\approx \mathbf{0.065}$ per testo inglese/monoalfabetico e $\approx \mathbf{0.038}$ per testo casuale uniforme. Dividendo $\mathbf{y}$ in $m$ colonne $\mathbf{y}_1, \dots, \mathbf{y}_m$, l'$m$ corretto è quello per cui tutte le colonne hanno $I_c(\mathbf{y}_i) \approx 0.065$.
    
      
    
- **Fase 2 (Indice Mutuo di Coincidenza $M_g$):** Per ogni colonna $\mathbf{y}_i$ (di lunghezza $n'$) e scorrimento candidato $g \in \{0, \dots, 25\}$, si calcola:
    
      
    
    $$M_g(\mathbf{y}_i) = \sum_{j=0}^{25} \frac{p_j f_{(j+g) \bmod 26}}{n'}$$
    
    Il valore $g = k_i$ corretto è l'unico che produce un picco vicino a **$0.065$**.
    
      
    

> [!example] Example 2.12 (Attacco completo a Vigenère con Kasiski, $I_c$ e $M_g$)
> 
> Dato un testo cifrato $\mathbf{y}$ di $n = 439$ caratteri (`CHREEVOAHMAERATBIAXXWTNXBEEOPHBSBQMQEQERBW...`):
> 
>   
> 
> 1. **Test di Kasiski:** Il trigramma `CHR` appare 5 volte, iniziando alle posizioni **1, 166, 236, 276 e 286**. Le distanze dalla prima occorrenza sono $165, 235, 275, 285$. Il loro massimo comune divisore è $\gcd(165, 235, 275, 285) = \mathbf{5}$, suggerendo $m = 5$.
>     
>       
>     
> 2. **Conferma con l'Indice di Coincidenza ($I_c$):**
>     
>       
>     - Per $m = 1$: $I_c(\mathbf{y}) = 0.045$.
>         
>           
>         
>     - Per $m = 2$: i valori di $I_c$ delle 2 colonne sono $0.046, 0.041$.
>         
>           
>         
>     - Per $m = 3$: $0.043, 0.050, 0.047$.
>         
>           
>         
>     - Per $m = 4$: $0.042, 0.039, 0.046, 0.040$.
>         
>           
>         
>     - Per **$m = 5$**: i valori delle 5 colonne schizzano a **$0.063, 0.067, 0.069, 0.061, 0.072$** (tutti vicinissimi a $0.065$!), confermando con certezza che $m = 5$.
>         
>           
>         
> 3. **Ricerca della keyword con $M_g$:** Calcolando $M_g(\mathbf{y}_i)$ per le 5 colonne (Tabella 2.4 del libro), i picchi massimi ($\approx 0.065$) si trovano in corrispondenza degli scorrimenti:
>     
>       
>     - Colonna 1: $g = 9$ (`J`)
>         
>           
>         
>     - Colonna 2: $g = 0$ (`A`)
>         
>           
>         
>     - Colonna 3: $g = 13$ (`N`)
>         
>           
>         
>     - Colonna 4: $g = 4$ (`E`)
>         
>           
>         
>     - Colonna 5: $g = 19$ (`T`)
>         
>         La parola chiave segreta è **`JANET`** ($K = (9, 0, 13, 4, 19)$), che decifra il testo in: _"The almond tree was in tentative blossom..."_.
>         
>           
>         

### 4. Crittoanalisi dell'Hill Cipher (Known-Plaintext Attack)

Possedendo $m$ coppie di blocchi plaintext-ciphertext disposte come righe nelle matrici $X$ e $Y$ di dimensione $m \times m$, se $\gcd(\det X, 26) = 1$ si ricava $K = X^{-1} Y \bmod 26$.

  

> [!example] Example 2.13 (Known-Plaintext Attack sull'Hill Cipher) Supponiamo che il plaintext `friday` venga cifrato con un Hill Cipher ($m = 2$) producendo il ciphertext `PQCFKU`.
> 
>   
> 
> 1. Abbiamo 3 coppie di digrammi:
>     
>       
>     - `fr` $= (5, 17) \longrightarrow$ `PQ` $= (15, 16)$
>         
>           
>         
>     - `id` $= (8, 3) \longrightarrow$ `CF` $= (2, 5)$
>         
>           
>         
>     - `ay` $= (0, 24) \longrightarrow$ `KU` $= (10, 20)$
>         
>           
>         
> 2. Usiamo le prime due coppie per formare le matrici $2 \times 2$ $X$ e $Y$:
>     
>       
>     
>     $$X = \begin{pmatrix} 5 & 17 \\ 8 & 3 \end{pmatrix} \qquad Y = \begin{pmatrix} 15 & 16 \\ 2 & 5 \end{pmatrix} \qquad \text{con } Y = XK \bmod 26$$
>     
> 3. Calcoliamo l'inversa di $X$: $\det X = (5 \times 3 - 17 \times 8) \bmod 26 = (15 - 136) \bmod 26 = -121 \bmod 26 = 9$. Poiché $\gcd(9, 26) = 1$ e $9^{-1} \bmod 26 = 3$:
>     
>       
>     
>     $$X^{-1} = 3 \begin{pmatrix} 3 & -17 \\ -8 & 5 \end{pmatrix} \bmod 26 = 3 \begin{pmatrix} 3 & 9 \\ 18 & 5 \end{pmatrix} \bmod 26 = \begin{pmatrix} 9 & 1 \\ 2 & 15 \end{pmatrix}$$
>     
> 4. Ricaviamo la matrice chiave $K$:
>     
>       
>     
>     $$K = X^{-1} Y \bmod 26 = \begin{pmatrix} 9 & 1 \\ 2 & 15 \end{pmatrix} \begin{pmatrix} 15 & 16 \\ 2 & 5 \end{pmatrix} \bmod 26 = \begin{pmatrix} 137 & 149 \\ 60 & 107 \end{pmatrix} \bmod 26 = \begin{pmatrix} 7 & 19 \\ 8 & 3 \end{pmatrix}$$
>     
>     _(Verifica con la terza coppia: $(0, 24) \begin{pmatrix} 7 & 19 \\ 8 & 3 \end{pmatrix} \bmod 26 = (192, 72) \bmod 26 = (10, 20) =$ `KU`)._
>     
>       
>     

### 5. Crittoanalisi dell'LFSR Stream Cipher (Known-Plaintext Attack)

Dati $2m$ bit di plaintext e ciphertext, si ricavano i $2m$ bit di keystream $z_i = (x_i + y_i) \bmod 2$ e si risolve il sistema lineare su $\mathbb{Z}_2$ invertendo la matrice di stato $m \times m$:

  

$$(c_0, c_1, \dots, c_{m-1}) = (z_{m+1}, z_{m+2}, \dots, z_{2m}) \begin{pmatrix} z_1 & z_2 & \dots & z_m \\ z_2 & z_3 & \dots & z_{m+1} \\ \vdots & \vdots & \ddots & \vdots \\ z_m & z_{m+1} & \dots & z_{2m-1} \end{pmatrix}^{-1} \bmod 2$$

> [!example] Example 2.14 (Known-Plaintext Attack su un LFSR a 5 stadi) Supponiamo che Oscar intercetti la stringa cifrata di 15 bit `101101011110010` corrispondente alla stringa in chiaro `011001111111000`, sapendo che il keystream è stato generato da un LFSR a **$m = 5$ stadi**:
> 
>   
> 
> 1. **Estrazione del keystream (XOR tra plaintext e ciphertext):**
>     
>     `110100100001010`
>     
>       
>     
>       
>     
> 2. **Impostazione dell'equazione matriciale (usando i primi $2m = 10$ bit):**
>     
>       
>     
>     $$(0, 1, 0, 0, 0) = (c_0, c_1, c_2, c_3, c_4) \begin{pmatrix} 1 & 1 & 0 & 1 & 0 \\ 1 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 \\ 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 \end{pmatrix} \pmod 2$$
>     
> 3. **Inversione della matrice su $\mathbb{Z}_2$ e calcolo dei coefficienti:**
>     
>     La matrice inversa modulo 2 è:
>     
>       
>     
>     $$\begin{pmatrix} 0 & 1 & 0 & 0 & 1 \\ 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \\ 0 & 1 & 0 & 1 & 1 \\ 1 & 0 & 1 & 1 & 0 \end{pmatrix}$$
>     
>     Moltiplicando $(0, 1, 0, 0, 0)$ per questa inversa modulo 2 otteniamo la seconda riga dell'inversa:
>     
>       
>     
>     $$(c_0, c_1, c_2, c_3, c_4) = (1, 0, 0, 1, 0)$$
>     
> 4. **Ricostruzione della ricorrenza:** Poiché solo $c_0 = 1$ e $c_3 = 1$, la relazione di ricorrenza segreta dell'LFSR è:
>     
>       
>     
>     $$z_{i+5} = (z_i + z_{i+3}) \bmod 2$$
>     
>       
>     

## Tabella Riassuntiva dei Cifrari del Capitolo 2

|**Crittosistema**|**Tipo**|**Dimensione Spazio Chiavi ∣K∣**|**Condizione sulla Chiave**|**Attacco Principale**|
|---|---|---|---|---|
|**Shift Cipher**|Monoalfabetico (Sostituzione)|$26$|$K \in \mathbb{Z}_{26}$|Ricerca esaustiva (media 13 tentativi)|
|**Affine Cipher**|Monoalfabetico (Sostituzione)|$12 \times 26 = 312$|$\gcd(a, 26) = 1$|Analisi delle frequenze (2 lettere $\to$ sistema lineare)|
|**Substitution Cipher**|Monoalfabetico (Sostituzione)|$26! \approx 4.0 \times 10^{26}$|Permutazione $\pi$ di $\mathbb{Z}_{26}$|Analisi frequenze di lettere, digrammi e trigrammi|
|**Vigenère Cipher**|Polialfabetico (Periodico)|$26^m$|Parola di lunghezza $m$ in $(\mathbb{Z}_{26})^m$|Test di Kasiski / Indice di Coincidenza ($I_c$) + $M_g$|
|**Hill Cipher**|Poligrafico a Blocchi (Lineare)|Matrici invertibili $m \times m$ su $\mathbb{Z}_{26}$|$\gcd(\det K, 26) = 1$|Known-plaintext ($m$ blocchi $\to K = X^{-1}Y \bmod 26$)|
|**Permutation Cipher**|Trasposizione a Blocchi|$m!$|Permutazione $\pi$ di $\{1, \dots, m\}$|Caso speciale di Hill (Known-plaintext / Anagrammi)|
|**Autokey Cipher**|Stream Cipher Non-sincrono|$26$|$K \in \mathbb{Z}_{26}$, $z_i = x_{i-1}$|Ricerca esaustiva (solo 26 chiavi iniziali!)|
|**LFSR Stream Cipher**|Stream Cipher Sincrono ($\mathbb{Z}_2$)|$2^m - 1$ stati non nulli|Ricorrenza lineare di grado $m$|Known-plaintext ($2m$ bit $\to$ inversione matrice su $\mathbb{Z}_2$)|

Modifiche applicate al Capitolo 3 per allinearlo alla notazione, alla numerazione e alla struttura della 4ª edizione di Stinson & Paterson:

  

- **Uniformazione dei simboli delle variabili aleatorie:** Sostituita la notazione mista $\mathbf{P} / \mathbf{X}$ degli appunti precedenti con i simboli esatti del testo: variabili aleatorie in grassetto $\mathbf{X}, \mathbf{Y}, \mathbf{Z}, \mathbf{K}$ definite su insiemi finiti calligrafici $\mathcal{X}, \mathcal{Y}, \mathcal{Z}$ (e $\mathcal{P}, \mathcal{C}, \mathcal{K}$ nel crittosistema), con probabilità congiunta $\Pr[x, y]$ al posto di $\Pr[\mathbf{P}=x \land \mathbf{K}=K]$.
    
- **Numerazione fedele al libro (Sezioni 3.1–3.3):** Separata la **Sezione 3.2 (Elementary Probability Theory)** dalla **Sezione 3.3 (Perfect Secrecy)**, allineando tutte le etichette: **Definition 3.1**, **Example 3.1**, **Definition 3.2**, **Theorem 3.1** (Bayes), **Corollary 3.2**, **Example 3.2**, **Definition 3.3** (_Perfect Secrecy_), **Example 3.3** (che prima era numerato 3.1), **Theorem 3.3** (_Shift Cipher_), **Theorem 3.4** (_Shannon's Theorem_) e **Cryptosystem 3.1** (_One-time Pad_).
    
- **Inserimento di definizioni, corollari ed esempi mancanti:** Aggiunti la definizione formale di variabile aleatoria discreta e di evento (**Definition 3.1**), i due esempi sul lancio dei dadi (**Example 3.1** ed **Example 3.2**), **Theorem 3.1** e **Corollary 3.2** (che collega direttamente l'indipendenza alla segretezza perfetta), mantenendo intatti gli approfondimenti già presenti nei tuoi appunti (Quadrati Latini, Esercizio 3.4, esempio numerico del _One-time Pad_ e _Two-Time Pad_).
    

# Capitolo 3: Shannon's Theory, Perfect Secrecy, and the One-Time Pad

Il Capitolo 3 introduce le nozioni formali di sicurezza crittografica concentrandosi sulla **unconditional security** (sicurezza incondizionata), presentando il **One-time Pad** e i concetti matematici di probabilità discreta, teoria dell'informazione e **perfect secrecy** (segretezza perfetta) sviluppati da Claude Shannon.

  

## 3.1 Introduction (Introduzione)

- **Obiettivo del capitolo:** Valutare la sicurezza di un crittosistema assumendo che l'avversario (Oscar) disponga di **risorse computazionali illimitate** (_unconditional security_) e conduca un attacco _ciphertext-only_, osservando un singolo testo cifrato $y$ cifrato con una chiave $K$ utilizzata una sola volta.
    
- **Limite della sola sicurezza computazionale:** Molti cifrari (come il _Substitution Cipher_ con $26!$ chiavi) impediscono la ricerca esaustiva della chiave, ma vengono comunque violati perché la struttura statistica del testo cifrato rivela informazioni sul testo in chiaro.
    
- **L'approccio probabilistico di Shannon:** Per dimostrare matematicamente se un testo cifrato $y$ rivela o meno informazioni sul testo in chiaro $x$, si modellano la scelta del messaggio, della chiave e del testo cifrato come **variabili aleatorie discrete** governate da distribuzioni di probabilità.
    

## 3.2 Elementary Probability Theory (Teoria Elementare della Probabilità)

> [!abstract] Definition 3.1: Discrete Random Variable (Variabile Aleatoria Discreta)
> 
> Una **variabile aleatoria discreta** (_discrete random variable_) $\mathbf{X}$ consiste in un insieme finito $\mathcal{X}$ e in una **distribuzione di probabilità** definita su $\mathcal{X}$.
> 
> La probabilità che la variabile aleatoria $\mathbf{X}$ assuma il valore $x \in \mathcal{X}$ è denotata con $\Pr[\mathbf{X} = x]$ (spesso abbreviata in $\Pr[x]$ quando la variabile aleatoria è chiara dal contesto), e soddisfa le seguenti proprietà:
> 
>   
> 
> 1. $\Pr[\mathbf{X} = x] \ge 0$ per ogni $x \in \mathcal{X}$;
>     
> 2. $\sum_{x \in \mathcal{X}} \Pr[\mathbf{X} = x] = 1$.
>     
> 
> Un **evento** (_event_) $E$ è un sottoinsieme $E \subseteq \mathcal{X}$, e la sua probabilità è definita come:
> 
>   
> 
> $$\Pr[E] = \sum_{x \in E} \Pr[\mathbf{X} = x]$$

> [!example] Example 3.1 (Lancio casuale di una coppia di dadi)
> 
> Consideriamo il lancio casuale di una coppia di dadi non truccati. L'esperimento è modellato da una variabile aleatoria $\mathbf{Z}$ definita sull'insieme:
> 
>   
> 
> $$\mathcal{Z} = \{1, 2, 3, 4, 5, 6\} \times \{1, 2, 3, 4, 5, 6\}$$
> 
> in cui ciascuna delle $36$ coppie ordinate $(i, j) \in \mathcal{Z}$ ha la stessa probabilità uniforme:
> 
>   
> 
> $$\Pr[\mathbf{Z} = (i, j)] = \frac{1}{36} \quad \forall (i, j) \in \mathcal{Z}$$
> 
> Se definiamo la variabile aleatoria $\mathbf{X}$ sull'insieme $\mathcal{X} = \{2, 3, \dots, 12\}$ come la **somma** dei valori dei due dadi ($i + j$), la probabilità di ciascun valore $x \in \mathcal{X}$ corrisponde alla probabilità dell'evento $E_x = \{(i, j) \in \mathcal{Z} : i + j = x\}$:
> 
>   
> 
> |**x**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|
> |---|---|---|---|---|---|---|---|---|---|---|---|
> |**$\Pr[\mathbf{X} = x]$**|$\frac{1}{36}$|$\frac{2}{36}$|$\frac{3}{36}$|$\frac{4}{36}$|$\frac{5}{36}$|$\frac{6}{36}$|$\frac{5}{36}$|$\frac{4}{36}$|$\frac{3}{36}$|$\frac{2}{36}$|$\frac{1}{36}$|
> 
> Ad esempio, per l'evento $E_4 = \{(1, 3), (2, 2), (3, 1)\}$ vale $\Pr[\mathbf{X} = 4] = \frac{3}{36} = \frac{1}{12}$, mentre per $E_7$ vale $\Pr[\mathbf{X} = 7] = \frac{6}{36} = \frac{1}{6}$.
> 
>   

> [!abstract] Definition 3.2: Probabilità Congiunta, Condizionata e Indipendenza
> 
> Siano $\mathbf{X}$ e $\mathbf{Y}$ due variabili aleatorie definite rispettivamente sugli insiemi finiti $\mathcal{X}$ e $\mathcal{Y}$:
> 
>   
> 
> 1. La **probabilità congiunta** (_joint probability_) $\Pr[\mathbf{X} = x, \mathbf{Y} = y]$ (abbreviata in $\Pr[x, y]$) è la probabilità che $\mathbf{X}$ assuma il valore $x$ **e** $\mathbf{Y}$ assuma il valore $y$.
>     
> 2. La **probabilità condizionata** (_conditional probability_) $\Pr[\mathbf{X} = x \mid \mathbf{Y} = y]$ (abbreviata in $\Pr[x \mid y]$) denota la probabilità che $\mathbf{X}$ assuma il valore $x$ **dato che** $\mathbf{Y}$ assume il valore $y$. Per $\Pr[y] > 0$, essa soddisfa:
>     
>     $$\Pr[x \mid y] = \frac{\Pr[x, y]}{\Pr[y]} \quad \Longleftrightarrow \quad \Pr[x, y] = \Pr[y]\Pr[x \mid y] = \Pr[x]\Pr[y \mid x]$$
>     
> 3. Le variabili aleatorie $\mathbf{X}$ e $\mathbf{Y}$ si dicono **indipendenti** (_independent random variables_) se:
>     
>     $$\Pr[x, y] = \Pr[x]\Pr[y] \quad \forall x \in \mathcal{X}, \; \forall y \in \mathcal{Y}$$
>     

> [!important] Theorem 3.1: Bayes' Theorem (Teorema di Bayes)
> 
> Se $\Pr[y] > 0$, allora:
> 
>   
> 
> $$\Pr[x \mid y] = \frac{\Pr[x]\Pr[y \mid x]}{\Pr[y]}$$

> [!important] Corollary 3.2: Caratterizzazione dell'Indipendenza
> 
> Le variabili aleatorie $\mathbf{X}$ e $\mathbf{Y}$ sono **indipendenti** se e solo se:
> 
>   
> 
> $$\Pr[x \mid y] = \Pr[x] \quad \forall x \in \mathcal{X}, \; \forall y \in \mathcal{Y} \text{ (con } \Pr[y] > 0\text{)}$$

> [!example] Example 3.2 (Probabilità condizionata, Bayes e non-indipendenza sui dadi)
> 
> Consideriamo ancora il lancio casuale di una coppia di dadi. Sia $\mathbf{X}$ la variabile aleatoria su $\mathcal{X} = \{2, \dots, 12\}$ data dalla **somma** dei due dadi, e sia $\mathbf{Y}$ la variabile aleatoria su $\mathcal{Y} = \{1, 2, 3, 4, 5, 6\}$ data dal valore del **primo dado** (con $\Pr[\mathbf{Y} = y] = \frac{1}{6}$ per ogni $y \in \mathcal{Y}$).
> 
>   
> 
> 4. **Probabilità congiunta:** L'unico esito con somma $4$ e primo dado pari a $3$ è la coppia $(3, 1)$, quindi:
>     
>     $$\Pr[\mathbf{X} = 4, \mathbf{Y} = 3] = \frac{1}{36}$$
>     
> 5. **Verifica della non-indipendenza (tramite Corollary 3.2):** Poiché $\Pr[\mathbf{X} = 4] = \frac{3}{36} = \frac{1}{12}$, calcoliamo:
>     
>     $$\Pr[\mathbf{Y} = 3 \mid \mathbf{X} = 4] = \frac{\Pr[\mathbf{X} = 4, \mathbf{Y} = 3]}{\Pr[\mathbf{X} = 4]} = \frac{1/36}{3/36} = \frac{1}{3}$$
>     
>     Poiché $\Pr[\mathbf{Y} = 3 \mid \mathbf{X} = 4] = \frac{1}{3} \neq \frac{1}{6} = \Pr[\mathbf{Y} = 3]$, per il **Corollary 3.2** le variabili $\mathbf{X}$ e $\mathbf{Y}$ **non** sono indipendenti.
>     
> 6. **Applicazione di Bayes (Theorem 3.1):** Per determinare la probabilità che la somma sia $4$ sapendo che il primo dado ha dato $3$:
>     
>     $$\Pr[\mathbf{X} = 4 \mid \mathbf{Y} = 3] = \frac{\Pr[\mathbf{X} = 4]\Pr[\mathbf{Y} = 3 \mid \mathbf{X} = 4]}{\Pr[\mathbf{Y} = 3]} = \frac{(3/36)(1/3)}{1/6} = \frac{1/36}{1/6} = \frac{1}{6}$$
>     

## 3.3 Perfect Secrecy (Segretezza Perfetta)

### 3.3.1 Modello Probabilistico di un Crittosistema

Dato un crittosistema $(\mathcal{P}, \mathcal{C}, \mathcal{K}, \mathcal{E}, \mathcal{D})$:

  

1. **Variabili aleatorie $\mathbf{X}$, $\mathbf{K}$ e $\mathbf{Y}$:**
    
    - Sia $\mathbf{X}$ la variabile aleatoria sullo spazio dei testi in chiaro $\mathcal{P}$, con distribuzione di probabilità _a priori_ $\Pr[\mathbf{X} = x]$ nota a tutti (incluso Oscar).
        
    - Sia $\mathbf{K}$ la variabile aleatoria sullo spazio delle chiavi $\mathcal{K}$, scelta da Alice e Bob secondo la distribuzione $\Pr[\mathbf{K} = K]$.
        
    - **Ipotesi di indipendenza:** Si assume che la chiave $\mathbf{K}$ e il testo in chiaro $\mathbf{X}$ siano **variabili aleatorie indipendenti**, ovvero $\Pr[\mathbf{X} = x, \mathbf{K} = K] = \Pr[\mathbf{X} = x]\Pr[\mathbf{K} = K]$.
        
    - Le distribuzioni di $\mathbf{X}$ e $\mathbf{K}$ inducono una distribuzione di probabilità sulla variabile aleatoria $\mathbf{Y}$ definita sullo spazio dei testi cifrati $\mathcal{C}$.
        
2. **Distribuzione sul testo cifrato $\Pr[\mathbf{Y} = y]$:** Per ogni chiave $K \in \mathcal{K}$, definiamo l'insieme dei possibili testi cifrati generabili da $K$ come:
    
    $$C(K) = \{e_K(x) : x \in \mathcal{P}\}$$
    
    Allora, per ogni $y \in \mathcal{C}$, la probabilità di osservare il testo cifrato $y$ è:
    
    $$\Pr[\mathbf{Y} = y] = \sum_{\{K \in \mathcal{K} : y \in C(K)\}} \Pr[\mathbf{K} = K]\Pr[\mathbf{X} = d_K(y)]$$
    
3. **Probabilità condizionata $\Pr[\mathbf{Y} = y \mid \mathbf{X} = x]$:** Per ogni $x \in \mathcal{P}$ e $y \in \mathcal{C}$, la probabilità di ottenere il cifrato $y$ dato il messaggio $x$ è la somma delle probabilità di tutte le chiavi che mappano $x$ in $y$:
    
    $$\Pr[\mathbf{Y} = y \mid \mathbf{X} = x] = \sum_{\{K \in \mathcal{K} : e_K(x) = y\}} \Pr[\mathbf{K} = K]$$
    
4. **Probabilità a posteriori $\Pr[\mathbf{X} = x \mid \mathbf{Y} = y]$ (tramite Theorem 3.1):** Applicando il **Teorema di Bayes** (assumendo $\Pr[\mathbf{Y} = y] > 0$) si ottiene la probabilità _a posteriori_ che il messaggio inviato fosse $x$, dato il testo cifrato osservato $y$:
    
    $$\Pr[\mathbf{X} = x \mid \mathbf{Y} = y] = \frac{\Pr[\mathbf{X} = x]\Pr[\mathbf{Y} = y \mid \mathbf{X} = x]}{\Pr[\mathbf{Y} = y]} = \frac{\Pr[\mathbf{X} = x]\sum_{\{K \in \mathcal{K} : e_K(x) = y\}} \Pr[\mathbf{K} = K]}{\sum_{\{K \in \mathcal{K} : y \in C(K)\}} \Pr[\mathbf{K} = K]\Pr[\mathbf{X} = d_K(y)]}$$
    

### 3.3.2 Definizione di Segretezza Perfetta ed Esempio di Sistema Non Perfetto

> [!abstract] Definition 3.3: Perfect Secrecy (Segretezza Perfetta) Un crittosistema $(\mathcal{P}, \mathcal{C}, \mathcal{K}, \mathcal{E}, \mathcal{D})$ gode di **perfect secrecy** (segretezza perfetta) se, per ogni $x \in \mathcal{P}$ e per ogni $y \in \mathcal{C}$ (con $\Pr[\mathbf{Y} = y] > 0$), la probabilità _a posteriori_ che il testo in chiaro sia $x$ dato il testo cifrato $y$ è uguale alla probabilità _a priori_ che il testo in chiaro sia $x$:
> 
>   
> 
> $$\Pr[\mathbf{X} = x \mid \mathbf{Y} = y] = \Pr[\mathbf{X} = x]$$

- **Legame con il Corollary 3.2 e il Theorem 3.1:** Per il **Corollary 3.2**, un crittosistema ha segretezza perfetta se e solo se le variabili aleatorie $\mathbf{X}$ e $\mathbf{Y}$ sono **indipendenti**. Inoltre, per il **Theorem 3.1** (assumendo $\Pr[\mathbf{X} = x] > 0$ e $\Pr[\mathbf{Y} = y] > 0$), vale l'equivalenza:
    
    $$\Pr[\mathbf{X} = x \mid \mathbf{Y} = y] = \Pr[\mathbf{X} = x] \quad \Longleftrightarrow \quad \Pr[\mathbf{Y} = y \mid \mathbf{X} = x] = \Pr[\mathbf{Y} = y]$$
    
- **Indipendenza dalla distribuzione di $\mathbf{X}$ (Esercizio 3.6):** Poiché $\Pr[\mathbf{Y} = y \mid \mathbf{X} = x]$ dipende esclusivamente dalle regole di cifratura e dalla distribuzione delle chiavi $\Pr[\mathbf{K} = K]$, se un crittosistema gode di segretezza perfetta per una data distribuzione sui testi in chiaro, **mantiene la segretezza perfetta per qualunque distribuzione di probabilità su $\mathcal{P}$**.
    

> [!example] Example 3.3 (Calcolo di $\Pr[\mathbf{Y} = y]$ e delle probabilità a posteriori $\Pr[\mathbf{X} = x \mid \mathbf{Y} = y]$) Sia $\mathcal{P} = \{a, b\}$ con $\Pr[\mathbf{X} = a] = \frac{1}{4}$ e $\Pr[\mathbf{X} = b] = \frac{3}{4}$. Sia $\mathcal{K} = \{K_1, K_2, K_3\}$ con $\Pr[\mathbf{K} = K_1] = \frac{1}{2}$ e $\Pr[\mathbf{K} = K_2] = \Pr[\mathbf{K} = K_3] = \frac{1}{4}$. Sia $\mathcal{C} = \{1, 2, 3, 4\}$, con funzioni di cifratura specificate dalla seguente matrice di cifratura:
> 
>   
> 
> |**Chiave**|**a**|**b**|
> |---|---|---|
> |**$K_1$**|$1$|$2$|
> |**$K_2$**|$2$|$3$|
> |**$K_3$**|$3$|$4$|
> 
> 1. **Distribuzione di probabilità su $\mathcal{C}$ ($\Pr[\mathbf{Y} = y]$):**
>     
>     - $\Pr[\mathbf{Y} = 1] = \Pr[\mathbf{K} = K_1]\Pr[\mathbf{X} = a] = \frac{1}{2} \cdot \frac{1}{4} = \mathbf{\frac{1}{8}}$
>         
>     - $\Pr[\mathbf{Y} = 2] = \Pr[\mathbf{K} = K_1]\Pr[\mathbf{X} = b] + \Pr[\mathbf{K} = K_2]\Pr[\mathbf{X} = a] = \left(\frac{1}{2} \cdot \frac{3}{4}\right) + \left(\frac{1}{4} \cdot \frac{1}{4}\right) = \mathbf{\frac{7}{16}}$
>         
>     - $\Pr[\mathbf{Y} = 3] = \Pr[\mathbf{K} = K_2]\Pr[\mathbf{X} = b] + \Pr[\mathbf{K} = K_3]\Pr[\mathbf{X} = a] = \left(\frac{1}{4} \cdot \frac{3}{4}\right) + \left(\frac{1}{4} \cdot \frac{1}{4}\right) = \mathbf{\frac{1}{4}}$
>         
>     - $\Pr[\mathbf{Y} = 4] = \Pr[\mathbf{K} = K_3]\Pr[\mathbf{X} = b] = \frac{1}{4} \cdot \frac{3}{4} = \mathbf{\frac{3}{16}}$ _(Verifica: $\frac{1}{8} + \frac{7}{16} + \frac{1}{4} + \frac{3}{16} = 1$)._
>         
> 2. **Probabilità a posteriori $\Pr[\mathbf{X} = x \mid \mathbf{Y} = y]$ (via Theorem 3.1):**
>     
>     - Per $y = 1$: $\Pr[a \mid 1] = \mathbf{1}$ e $\Pr[b \mid 1] = \mathbf{0}$ (solo $a$ si cifra in $1$).
>         
>     - Per $y = 2$: $\Pr[a \mid 2] = \frac{(1/4)(1/4)}{7/16} = \mathbf{\frac{1}{7}}$ e $\Pr[b \mid 2] = \frac{(3/4)(1/2)}{7/16} = \mathbf{\frac{6}{7}}$.
>         
>     - Per $y = 3$: $\Pr[a \mid 3] = \frac{(1/4)(1/4)}{1/4} = \mathbf{\frac{1}{4}}$ e $\Pr[b \mid 3] = \frac{(3/4)(1/4)}{1/4} = \mathbf{\frac{3}{4}}$.
>         
>     - Per $y = 4$: $\Pr[a \mid 4] = \mathbf{0}$ e $\Pr[b \mid 4] = \mathbf{1}$ (solo $b$ si cifra in $4$).
>         
> 
> **Conclusione:** Il crittosistema **non** fornisce segretezza perfetta, perché sebbene $\Pr[a \mid 3] = \Pr[a] = \frac{1}{4}$, per $y \in \{1, 2, 4\}$ vale $\Pr[x \mid y] \neq \Pr[x]$ (e per $y=1$ o $y=4$ Oscar determina $x$ con certezza assoluta).
> 
>   

> [!important] Theorem 3.3: Segretezza Perfetta dello Shift Cipher
> Supponiamo che le $26$ chiavi dello **Shift Cipher** vengano scelte con probabilità uniforme $\Pr[\mathbf{K} = K] = \frac{1}{26}$ per ogni $K \in \mathbb{Z}_{26}$. Allora, per qualunque distribuzione di probabilità sui testi in chiaro $\mathbf{X}$ (su un singolo carattere in $\mathbb{Z}_{26}$), lo Shift Cipher fornisce **perfect secrecy**.

**Dimostrazione:**

1. **Calcolo della distribuzione di probabilità del testo cifrato $\Pr[\mathbf{Y} = y]$:**
   Ricordiamo che, per ogni chiave $K \in \mathbb{Z}_{26}$, vale $C(K) = \mathbb{Z}_{26}$ e la regola di decifratura è $d_K(y) = (y - K) \bmod 26$. Applicando la formula generale per $\Pr[\mathbf{Y} = y]$, per qualsiasi $y \in \mathbb{Z}_{26}$ otteniamo:
   $$\begin{aligned}
   \Pr[\mathbf{Y} = y] &= \sum_{K \in \mathbb{Z}_{26}} \Pr[\mathbf{K} = K]\Pr[\mathbf{X} = d_K(y)] \\
   &= \sum_{K \in \mathbb{Z}_{26}} \frac{1}{26}\Pr[\mathbf{X} = (y - K) \bmod 26] \\
   &= \frac{1}{26} \sum_{K \in \mathbb{Z}_{26}} \Pr[\mathbf{X} = (y - K) \bmod 26]
   \end{aligned}$$
   Fissato $y \in \mathbb{Z}_{26}$, al variare di $K$ su tutto $\mathbb{Z}_{26}$ i valori $(y - K) \bmod 26$ formano una permutazione di $\mathbb{Z}_{26}$. Pertanto:
   $$\sum_{K \in \mathbb{Z}_{26}} \Pr[\mathbf{X} = (y - K) \bmod 26] = \sum_{x \in \mathbb{Z}_{26}} \Pr[\mathbf{X} = x] = 1$$
   Di conseguenza:
   $$\Pr[\mathbf{Y} = y] = \frac{1}{26} \cdot 1 = \frac{1}{26} \quad \forall y \in \mathbb{Z}_{26}$$

2. **Calcolo della probabilità condizionata $\Pr[\mathbf{Y} = y \mid \mathbf{X} = x]$:**
   Per ogni $x, y \in \mathbb{Z}_{26}$, esiste un'unica chiave $K \in \mathbb{Z}_{26}$ tale che $e_K(x) = y$, ossia $K = (y - x) \bmod 26$. La sommatoria su $\{K \in \mathbb{Z}_{26} : e_K(x) = y\}$ si riduce quindi a un solo termine:
   $$\Pr[\mathbf{Y} = y \mid \mathbf{X} = x] = \Pr[\mathbf{K} = (y - x) \bmod 26] = \frac{1}{26} \quad \forall x, y \in \mathbb{Z}_{26}$$

3. **Applicazione del Theorem 3.1 (Teorema di Bayes):**
   Sostituendo i valori appena trovati nel Teorema di Bayes, per ogni $x, y \in \mathbb{Z}_{26}$ otteniamo:
   $$\Pr[\mathbf{X} = x \mid \mathbf{Y} = y] = \frac{\Pr[\mathbf{X} = x]\Pr[\mathbf{Y} = y \mid \mathbf{X} = x]}{\Pr[\mathbf{Y} = y]} = \frac{\Pr[\mathbf{X} = x] \cdot \frac{1}{26}}{\frac{1}{26}} = \Pr[\mathbf{X} = x]$$
   Poiché $\Pr[\mathbf{X} = x \mid \mathbf{Y} = y] = \Pr[\mathbf{X} = x]$ per ogni $x, y \in \mathbb{Z}_{26}$, lo Shift Cipher soddisfa la definizione di **perfect secrecy**. $\blacksquare$
- **Interpretazione operativa:** Se Oscar intercetta ad esempio $y = 10$ (`K`), provando tutte le $26$ chiavi equiprobabili ottiene come decifrature $d_K(10) = (10 - K) \bmod 26$ tutti e $26$ i caratteri dell'alfabeto, ciascuno con la propria probabilità _a priori_ $\Pr[\mathbf{X} = x]$. 
    

#### Disuguaglianza Fondamentale sulle Cardinalità ($\vert{}\mathcal{K}\vert{} \ge \vert{}\mathcal{C}\vert{} \ge \vert{}\mathcal{P}\vert{}$)

In qualsiasi crittosistema dotato di segretezza perfetta (assumendo $\Pr[\mathbf{Y} = y] > 0$ per ogni $y \in \mathcal{C}$):

  

1. **$\vert{}\mathcal{C}\vert{} \ge \vert{}\mathcal{P}\vert{}$:** Vale in ogni crittosistema perché ogni regola di cifratura $e_K : \mathcal{P} \to \mathcal{C}$ deve essere iniettiva.
    
2. **$\vert{}\mathcal{K}\vert{} \ge \vert{}\mathcal{C}\vert{}$:** Fissato un qualsiasi $x \in \mathcal{P}$, per ogni $y \in \mathcal{C}$ la segretezza perfetta richiede $\Pr[\mathbf{Y} = y \mid \mathbf{X} = x] = \Pr[\mathbf{Y} = y] > 0$, quindi deve esistere almeno una chiave $K \in \mathcal{K}$ tale che $e_K(x) = y$. Poiché ciascuna chiave associa a $x$ un solo valore $y$, servono almeno $\vert{}\mathcal{C}\vert{}$ chiavi distinte:
    
    $$\vert{}\mathcal{K}\vert{} \ge \vert{}\mathcal{C}\vert{} \ge \vert{}\mathcal{P}\vert{}$$
    

### 3.3.4 Il Teorema di Shannon e il One-Time Pad

> [!important] Theorem 3.4: Shannon's Theorem (Teorema di Shannon) Sia $(\mathcal{P}, \mathcal{C}, \mathcal{K}, \mathcal{E}, \mathcal{D})$ un crittosistema tale che $\vert{}\mathcal{K}\vert{} = \vert{}\mathcal{C}\vert{} = \vert{}\mathcal{P}\vert{}$. Allora il crittosistema fornisce **perfect secrecy** se e solo se sono soddisfatte entrambe le seguenti condizioni:
> 
>   
> 
> 1. Ogni chiave $K \in \mathcal{K}$ è scelta con la stessa probabilità uniforme:
>     
>     $$\Pr[\mathbf{K} = K] = \frac{1}{\vert{}\mathcal{K}\vert{}} \quad \forall K \in \mathcal{K}$$
>     
> 2. Per ogni $x \in \mathcal{P}$ e per ogni $y \in \mathcal{C}$, esiste un'**unica** chiave $K \in \mathcal{K}$ tale che $e_K(x) = y$.
>     

#### Dimostrazione completa del Theorem 3.4

- **($\Longrightarrow$ Supponiamo che il crittosistema fornisca perfect secrecy):**
    
    1. Fissato $x \in \mathcal{P}$, per ogni $y \in \mathcal{C}$ deve esistere almeno una chiave $K \in \mathcal{K}$ tale che $e_K(x) = y$ (altrimenti $\Pr[y \mid x] = 0 \neq \Pr[y]$). Poiché $|\mathcal{K}| = |\mathcal{C}|$, non possono esserci due chiavi distinte che mappano $x$ nello stesso $y$: esiste quindi un'**unica** chiave $K$ tale che $e_K(x) = y$ (**Condizione 2 dimostrata**).
        
    2. Poniamo $n = |\mathcal{K}|$, indichiamo $\mathcal{P} = \{x_i : 1 \le i \le n\}$ e fissiamo un elemento di testo cifrato $y \in \mathcal{C}$. Per la Condizione 2, possiamo etichettare le chiavi come $K_1, K_2, \dots, K_n$ in modo tale che $e_{K_i}(x_i) = y$ per $1 \le i \le n$.
        
    3. Per il **Theorem 3.1** (Bayes), per ogni $1 \le i \le n$ vale:
        
        $$\Pr[\mathbf{X} = x_i \mid \mathbf{Y} = y] = \frac{\Pr[\mathbf{X} = x_i]\Pr[\mathbf{Y} = y \mid \mathbf{X} = x_i]}{\Pr[\mathbf{Y} = y]} = \frac{\Pr[\mathbf{X} = x_i]\Pr[\mathbf{K} = K_i]}{\Pr[\mathbf{Y} = y]}$$
        
    4. Per ipotesi di segretezza perfetta, $\Pr[\mathbf{X} = x_i \mid \mathbf{Y} = y] = \Pr[\mathbf{X} = x_i]$; assumendo $\Pr[\mathbf{X} = x_i] > 0$ e dividendo entrambi i membri per $\Pr[\mathbf{X} = x_i]$, otteniamo $\Pr[\mathbf{K} = K_i] = \Pr[\mathbf{Y} = y]$ per ogni $1 \le i \le n$. Tutte le $n$ chiavi hanno dunque la stessa probabilità costante, che dovendo sommare a $1$ vale necessariamente $\Pr[\mathbf{K} = K_i] = \frac{1}{|\mathcal{K}|}$ (**Condizione 1 dimostrata**).
        
- **($\Longleftarrow$ Supponiamo che valgano le Condizioni 1 e 2):** Fissati $x \in \mathcal{P}$ e $y \in \mathcal{C}$, esiste un'unica chiave $K \in \mathcal{K}$ tale che $e_K(x) = y$, e tale chiave ha probabilità $\frac{1}{|\mathcal{K}|}$. Pertanto $\Pr[\mathbf{Y} = y \mid \mathbf{X} = x] = \frac{1}{|\mathcal{K}|}$. Ne segue che:
    
    $$\Pr[\mathbf{Y} = y] = \sum_{x \in \mathcal{P}} \Pr[\mathbf{X} = x]\Pr[\mathbf{Y} = y \mid \mathbf{X} = x] = \frac{1}{|\mathcal{K}|}\sum_{x \in \mathcal{P}} \Pr[\mathbf{X} = x] = \frac{1}{|\mathcal{K}|} = \Pr[\mathbf{Y} = y \mid \mathbf{X} = x]$$
    
    Applicando il **Theorem 3.1**, otteniamo $\Pr[\mathbf{X} = x \mid \mathbf{Y} = y] = \Pr[\mathbf{X} = x]$ per ogni $x \in \mathcal{P}, y \in \mathcal{C}$. $\blacksquare$
    

> [!example] Matrici di Cifratura Perfette: Quadrati Latini e Caso $|\mathcal{K}| > |\mathcal{C}| > |\mathcal{P}|$
> 
>   
> 
> 1. **Quadrato Latino ($\vert{}\mathcal{K}\vert{} = \vert{}\mathcal{C}\vert{} = \vert{}\mathcal{P}\vert{} = n$):** Per il **Theorem 3.4**, con chiavi equiprobabili $\Pr[\mathbf{K} = K_i] = \frac{1}{n}$, la matrice di cifratura fornisce segretezza perfetta se e solo se è un **Quadrato Latino** (_Latin square_), ossia ogni simbolo $y \in \mathcal{C}$ compare esattamente una volta in ogni riga (iniettività di $e_K$) e una volta in ogni colonna (unicità della chiave $K$ tale che $e_K(x) = y$).
>     
> 2. **Caso $|\mathcal{K}| > |\mathcal{C}| > |\mathcal{P}|$ (Esercizio 3.4):** Se $\mathcal{P} = \{a, b\}$, $\mathcal{C} = \{1, 2, 3, 4\}$ e $\mathcal{K} = \{K_1, \dots, K_6\}$ con righe $K_1:(1,2),\; K_2:(2,3),\; K_3:(3,4),\; K_4:(4,1),\; K_5:(1,3),\; K_6:(2,4)$, scegliendo probabilità anche non uniformi $\Pr[K_1]=\Pr[K_3]=p$, $\Pr[K_2]=\Pr[K_4]=q$, $\Pr[K_5]=\Pr[K_6]=r$ (con $2p + 2q + 2r = 1$), si ottiene comunque $\Pr[\mathbf{Y} = y \mid \mathbf{X} = a] = \Pr[\mathbf{Y} = y \mid \mathbf{X} = b]$ per ogni $y \in \mathcal{C}$. Questo mostra che l'equiprobabilità delle chiavi del Theorem 3.4 è necessaria solo quando $|\mathcal{K}| = |\mathcal{C}| = |\mathcal{P}|$.
>     

> [!abstract] Cryptosystem 3.1: One-time Pad
> Sia $n \ge 1$ un intero, e prendiamo $\mathcal{P} = \mathcal{C} = \mathcal{K} = (\mathbb{Z}_2)^n$. Per $K \in (\mathbb{Z}_2)^n$, definiamo $e_K(x)$ come la somma vettoriale modulo $2$ di $K$ e $x$ (o, equivalentemente, l'exclusive-or delle due bitstring associate). Quindi, se $x = (x_1, \dots, x_n)$ e $K = (K_1, \dots, K_n)$, allora
> $$e_K(x) = (x_1 + K_1, \dots, x_n + K_n) \bmod 2.$$
> La decifratura è identica alla cifratura. Se $y = (y_1, \dots, y_n)$, allora
> $$d_K(y) = (y_1 + K_1, \dots, y_n + K_n) \bmod 2.$$

> [!example] Esempio Numerico del One-time Pad e Vulnerabilità del Riutilizzo della Chiave (Two-Time Pad)
> 
>   
> 
> 1. **Cifratura e Decifratura ($n = 5$):** Dato $x = (1, 0, 1, 1, 0)$ e la chiave casuale $K = (0, 1, 1, 0, 1)$ (con $\Pr[\mathbf{K} = K] = 2^{-5} = \frac{1}{32}$):
>     
>     - **Cifratura:** $y = e_K(x) = x \oplus K = \mathbf{(1, 1, 0, 1, 1)}$.
>         
>     - **Decifratura:** $d_K(y) = y \oplus K = \mathbf{(1, 0, 1, 1, 0)} = x$.
>         
> 2. **Dimostrazione di Perfect Secrecy (via Theorem 3.4):** Poiché $|\mathcal{P}| = |\mathcal{C}| = |\mathcal{K}| = 2^n$, ogni chiave è scelta con probabilità uniforme $2^{-n}$ e, fissati $x, y \in (\mathbb{Z}_2)^n$, l'equazione $x \oplus K = y$ ammette l'unica soluzione $K = x \oplus y$, per il **Theorem 3.4** il _One-time Pad_ garantisce segretezza perfetta.
>     
> 3. **Attacco al riutilizzo della chiave (_Two-Time Pad_):** Se Alice cifra due messaggi distinti $x_1 = \texttt{10110}$ e $x_2 = \texttt{01100}$ con la medesima chiave $K = \texttt{01101}$, ottiene $y_1 = \texttt{11011}$ e $y_2 = \texttt{00001}$. Calcolando lo XOR dei due testi cifrati, Oscar elimina la chiave $K$:
>     
>     $$y_1 \oplus y_2 = (x_1 \oplus K) \oplus (x_2 \oplus K) = x_1 \oplus x_2 = \texttt{11010}$$
>     
>     ottenendo informazioni dirette sulla correlazione tra i due testi in chiaro (inoltre, in un attacco _known-plaintext_, conoscendo $x_1$ Oscar ricava subito $K = x_1 \oplus y_1$ e decifra $x_2$).
>     

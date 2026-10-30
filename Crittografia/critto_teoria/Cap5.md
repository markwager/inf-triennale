
# Capitolo 5: Funzioni di Hash e Autenticazione dei Messaggi



Nei capitoli precedenti abbiamo studiato i crittosistemi a chiave segreta (block ciphers e stream ciphers), il cui obiettivo è garantire la confidenzialità (_secrecy_). Tuttavia, la sola cifratura non protegge l'**integrità dei dati** (_data integrity_) né la **message authentication** (autenticazione dei messaggi) contro un avversario attivo.

  

Il **Capitolo 5** introduce le **hash functions** (Sezioni 5.1–5.4) e i **message authentication codes (MAC)** (Sezione 5.5), concludendo con l'**authenticated encryption** e il **Galois Counter Mode (GCM)** nella Sezione 5.5.3.
  

  

## 5.1 Hash Functions and Data Integrity (Funzioni di Hash e Integrità dei Dati)

  

  

Una **cryptographic hash function** può essere utilizzata per fornire garanzia di **data integrity**. Prende in input un messaggio di lunghezza arbitraria e produce in output un valore di lunghezza fissa (e ridotta) chiamato **message digest** (ad esempio di lunghezza compresa tra 160 e 512 bit).

  

Le funzioni di hash si dividono in due tipologie:

  

- **Keyed hash functions (Funzioni di hash con chiave):** Utilizzano una chiave segreta $K$; una _keyed hash function_ viene utilizzata come **message authentication code**, o **MAC**.
    
      
    
- **Unkeyed hash functions (Funzioni di hash senza chiave):** Non utilizzano alcuna chiave segreta. Quando nel seguito si usa il termine **hash function** senza ulteriori specificazioni, ci si riferisce sempre a una **unkeyed hash function**.
    
      
    

  

  

### 5.1.1 Definizione Formale di Hash Family

  
  

> [!abstract] Definition 5.1: Hash Family Una **hash family** è una 4-tupla $(\mathcal{X}, \mathcal{Y}, \mathcal{K}, \mathcal{H})$, dove sono soddisfatte le seguenti condizioni:
> 
>   
> 
> 1. $\mathcal{X}$ è un insieme di possibili **messages** (messaggi).
>     
>       
>     
> 2. $\mathcal{Y}$ è un insieme finito di possibili **message digests** (o **authentication tags**).
>     
>       
>     
> 3. $\mathcal{K}$, il **keyspace**, è un insieme finito di possibili **keys** (chiavi).
>     
>       
>     
> 4. Per ogni $K \in \mathcal{K}$, esiste una **hash function** $h_K \in \mathcal{H}$. Ciascuna $h_K : \mathcal{X} \to \mathcal{Y}$ è una funzione.
>     
>       
>     

- **Compression Function e Notazione $(N, M)$-hash family:**
    
      
    - $\mathcal{X}$ può essere un insieme finito oppure infinito; $\mathcal{Y}$ è sempre un insieme finito.
        
          
        
    - Se $\mathcal{X}$ è un insieme finito, allora una hash function è spesso chiamata una **compression function** (funzione di compressione), e assumiamo sempre che $\vert{}\mathcal{X}\vert{} \ge \vert{}\mathcal{Y}\vert{}$; in effetti, nella maggior parte dei casi pratici si richiede almeno $\vert{}\mathcal{X}\vert{} \ge 2\vert{}\mathcal{Y}\vert{}$.
        
          
        
    - Se $\vert{}\mathcal{X}\vert{} = N$ e $\vert{}\mathcal{Y}\vert{} = M$, la _hash family_ è detta una **$(N, M)$-hash family**.
        
          
        
    - Una **unkeyed hash function** è semplicemente una _hash family_ in cui esiste una sola chiave possibile, ovvero **$\vert{}\mathcal{K}\vert{} = 1$** (scriveremo in tal caso semplicemente $h : \mathcal{X} \to \mathcal{Y}$).
        
          
        

  

  

### 5.1.2 Come Verificare la Data Integrity (MAC vs Unkeyed Hash Function)

  

  

Supponiamo che Alice trasmetta un messaggio $x \in \mathcal{X}$ a Bob su un canale non sicuro e voglia permettere a Bob di verificare che $x$ non sia stato modificato:

  

1. **Con una Keyed Hash Function (MAC):**
    
      
    - Alice e Bob condividono una chiave segreta $K \in \mathcal{K}$.
        
          
        
    - Quando Alice trasmette $x$, calcola l'**authentication tag** (o message digest) $y = h_K(x)$ e invia la coppia $(x, y)$ sul canale.
        
          
        
    - Quando Bob riceve una coppia $(x, y)$, può verificare la validità del tag controllando se $y = h_K(x)$.
        
          
        
    - Se questa condizione è soddisfatta, Bob accetta $(x, y)$ come **valid** (valida); altrimenti la rifiuta come **invalid** (invalida).
        
          
        
    - Se un avversario (Oscar) sostituisce $x$ con $x'$ o modifica $y$ in $y'$ senza conoscere la chiave $K$, non sarà in grado di produrre una coppia valida $(x', y')$ tale che $y' = h_K(x')$.
        
          
        
2. **Con una Unkeyed Hash Function ($h : \mathcal{X} \to \mathcal{Y}$):**
    
      
    - Se non c'è una chiave segreta, perché un avversario non può semplicemente sostituire $x$ con un nuovo messaggio $x'$ e calcolare lui stesso il corrispondente message digest $y' = h(x')$ (dato che $h$ è pubblica)?
        
          
        
    - Effettivamente, se sia $x$ che $y = h(x)$ venissero trasmessi su un canale non protetto senza chiave, chiunque potrebbe sostituire $(x, y)$ con $(x', h(x'))$.
        
          
        
    - Pertanto, una **unkeyed hash function** viene utilizzata in scenari in cui il _message digest_ $y = h(x)$ è protetto in altro modo:
        
          
        - Ad esempio all'interno di un **signature scheme** (schema di firma digitale): Alice calcola il _message digest_ $y = h(x)$ e firma digitalmente soltanto $y$ con la sua chiave privata.
            
              
            
        - Oppure quando l'utente calcola $y = h(x)$ di un file e memorizza $y$ in un'area sicura per verificare in seguito che il file $x$ non sia stato alterato.
            
              
            
        - Oppure combinandola con una chiave segreta per costruire un MAC (come in **HMAC**, Sezione 5.5.1).
            
              
            

  

  

## 5.2 Security of Hash Functions (Sicurezza delle Funzioni di Hash)

  

  

Consideriamo una **unkeyed hash function** $h : \mathcal{X} \to \mathcal{Y}$. Tipicamente il dominio è $\mathcal{X} = \{0, 1\}^*$ (stringhe binarie di lunghezza arbitraria) e il codominio è $\mathcal{Y} = \{0, 1\}^m$ per un certo intero positivo $m$ (quindi $\vert{}\mathcal{Y}\vert{} = M = 2^m$).

  

Poiché $\vert{}\mathcal{X}\vert{} > \vert{}\mathcal{Y}\vert{}$, la funzione $h$ non può essere iniettiva: devono necessariamente esistere coppie di input distinti $x \neq x'$ tali che $h(x) = h(x')$. Una tale coppia è chiamata una **collision** (collisione). Affinché una funzione di hash sia sicura per gli usi crittografici, chiediamo che i seguenti **tre problemi** siano difficili da risolvere (computazionalmente infattibili):

  

  

  

### 1. The Three Hash Function Problems

  

  

> [!abstract] Problem 5.1: Preimage
> 
>   
> 
> - **Instance (Istanza):** Una hash function $h : \mathcal{X} \to \mathcal{Y}$ e un elemento $y \in \mathcal{Y}$.
>     
>       
>     
> - **Find (Trovare):** Un elemento $x \in \mathcal{X}$ tale che $h(x) = y$.
>     
>       
>     

- Dato un message digest $y$, un elemento $x$ tale che $h(x) = y$ è chiamato una **preimage** di $y$.
    
      
    
- Una funzione di hash per la quale il problema **Preimage** non può essere risolto efficientemente è spesso chiamata **one-way** (unidirezionale) oppure **preimage resistant**.
    
      
    

> [!abstract] Problem 5.2: Second Preimage
> 
>   
> 
> - **Instance (Istanza):** Una hash function $h : \mathcal{X} \to \mathcal{Y}$ e un elemento $x \in \mathcal{X}$.
>     
>       
>     
> - **Find (Trovare):** Un elemento $x' \in \mathcal{X}$ tale che $x' \neq x$ e $h(x') = h(x)$.
>     
>       
>     

- Una funzione di hash per la quale il problema **Second Preimage** non può essere risolto efficientemente è spesso chiamata **second preimage resistant**.
    
      
    

> [!abstract] Problem 5.3: Collision
> 
>   
> 
> - **Instance (Istanza):** Una hash function $h : \mathcal{X} \to \mathcal{Y}$.
>     
>       
>     
> - **Find (Trovare):** Due elementi $x, x' \in \mathcal{X}$ tali che $x' \neq x$ e $h(x') = h(x)$.
>     
>       
>     

- Una funzione di hash per la quale il problema **Collision** non può essere risolto efficientemente è spesso chiamata **collision resistant**.
    
      
    
- _(Nota applicativa sulle firme digitali):_ Se Alice firma un messaggio $x$ apponendo la sua firma digitale sul message digest $h(x)$, e Oscar riesce a risolvere **Second Preimage** trovando $x' \neq x$ con $h(x') = h(x)$, allora Oscar può spacciare la firma di Alice su $h(x)$ come una firma valida sul messaggio falso $x'$ (**forgery**). Inoltre, se Oscar riesce a risolvere **Collision** trovando in anticipo due messaggi $x \neq x'$ con $h(x) = h(x')$, può convincere Alice a firmare il messaggio $x$ (scelto da Oscar) e poi trasferire quella firma sul messaggio $x'$.
    
      
    

  

  

## 5.2.1 The Random Oracle Model (Il Modello dell'Oracolo Casuale)

  

  

Per analizzare la difficoltà intrinseca dei problemi **Preimage**, **Second Preimage** e **Collision** per una funzione di hash "ideale", la Sezione 5.2.1 introduce il **random oracle model** (dovuto a Bellare e Rogaway):

  

- Denotiamo con **$\mathcal{F}^{\mathcal{X}, \mathcal{Y}}$** l'insieme di tutte le funzioni da $\mathcal{X}$ a $\mathcal{Y}$. Se $\vert{}\mathcal{X}\vert{} = N$ e $\vert{}\mathcal{Y}\vert{} = M$, allora $\vert{}\mathcal{F}^{\mathcal{X}, \mathcal{Y}}\vert{} = M^N$.
    
      
    
- Nel **random oracle model**, si assume che una hash function $h \in \mathcal{F}^{\mathcal{X}, \mathcal{Y}}$ sia scelta **uniformemente a caso** (_chosen uniformly at random_), e che ci sia permesso accedere a $h$ **unicamente tramite un oracle** (oracolo):
    
      
    - Non ci viene data una formula o un algoritmo per calcolare i valori della funzione $h$.
        
          
        
    - Possiamo invece specificare un qualsiasi input $x \in \mathcal{X}$ e chiedere all'oracolo di fornirci il corrispondente output $y = h(x)$ (questa operazione è chiamata una **query** all'oracolo).
        
          
        

> [!important] Theorem 5.1: Independence Theorem Supponiamo che una hash function $h \in \mathcal{F}^{\mathcal{X}, \mathcal{Y}}$ sia scelta uniformemente a caso, e sia $\mathcal{X}_0 \subseteq \mathcal{X}$. Supponiamo che i valori $h(x)$ siano stati determinati (interrogando l'oracolo per $h$) se e solo se $x \in \mathcal{X}_0$. Allora:
> 
>   
> 
> $$\Pr[h(x) = y] = \frac{1}{M}$$
> 
> per tutti gli $x \in \mathcal{X} \setminus \mathcal{X}_0$ e tutti gli $y \in \mathcal{Y}$. Inoltre, le probabilità $\Pr[h(x) = y]$ sono **indipendenti** per tutti gli $x \in \mathcal{X} \setminus \mathcal{X}_0$.
> 
>   

- **Definizione di $(\varepsilon, Q)$-algorithm:** Nel _random oracle model_, misuriamo la complessità di un algoritmo contando il numero di **oracle queries** $Q$ che esso effettua. Un algoritmo randomizzato (**randomized algorithm**) che effettua al massimo $Q$ query all'oracolo e risolve un dato problema con probabilità di successo (**success probability**) almeno $\varepsilon$ viene chiamato un **$(\varepsilon, Q)$-algorithm**.
    
      
    

  

  

### Analisi di `Find-Preimage`, `Find-Second-Preimage` e `Find-Collision` nel ROM

  

  

  

  

#### 1. Algoritmo per `Preimage` (Algorithm 5.1)

  

  

> [!abstract] Algorithm 5.1: `Find-Preimage`$(h, y, Q)$
> 
>   
> 
> 1. Scegliere qualsiasi sottoinsieme $\mathcal{X}_0 \subseteq \mathcal{X}$ di cardinalità $\vert{}\mathcal{X}_0\vert{} = Q$.
>     
>       
>     
> 2. **for each** $x \in \mathcal{X}_0$ **do** $\quad$ **if** $h(x) = y$ **then** $\quad \quad$ **return** ($x$)
>     
>       
>     
> 3. **return** (_failure_)
>     
>       
>     

- **Teorema sulla probabilità di successo di `Find-Preimage`:** Per l'_Independence Theorem_ (Theorem 5.1), per ogni $x \in \mathcal{X}_0$ la probabilità che $h(x) = y$ è $1/M$, e questi eventi sono indipendenti per i $Q$ elementi distinti di $\mathcal{X}_0$. Pertanto la probabilità che nessun $x \in \mathcal{X}_0$ soddisfi $h(x) = y$ è $(1 - 1/M)^Q$. La probabilità di successo di `Find-Preimage` è quindi:
    
      
    
    $$\varepsilon = 1 - \left(1 - \frac{1}{M}\right)^Q$$
    
    Usando lo sviluppo binomiale al primo ordine (valido quando $Q$ è piccolo rispetto a $M$), si ottiene l'approssimazione $\varepsilon \approx \frac{Q}{M}$. Per avere una probabilità di successo costante (es. $\varepsilon = 1/2$), servono $Q = \Theta(M)$ query.
    
      
    

  

  

#### 2. Algoritmo per `Second Preimage` (Algorithm 5.2)

  

  

> [!abstract] Algorithm 5.2: `Find-Second-Preimage`$(h, x, Q)$
> 
>   
> 
> 1. Calcolare $y = h(x)$ _(1ª query all'oracolo)_.
>     
>       
>     
> 2. Scegliere qualsiasi sottoinsieme $\mathcal{X}_0 \subseteq \mathcal{X} \setminus \{x\}$ di cardinalità $\vert{}\mathcal{X}_0\vert{} = Q - 1$.
>     
>       
>     
> 3. **for each** $x_0 \in \mathcal{X}_0$ **do** $\quad$ **if** $h(x_0) = y$ **then** $\quad \quad$ **return** ($x_0$)
>     
>       
>     
> 4. **return** (_failure_)
>     
>       
>     

- **Probabilità di successo di `Find-Second-Preimage`:** Poiché l'algoritmo usa $1$ query per calcolare $y = h(x)$ e poi interroga l'oracolo su $Q - 1$ nuovi elementi distinti di $\mathcal{X} \setminus \{x\}$, la probabilità di successo con al massimo $Q$ query totali è esattamente:
    
      
    
    $$\varepsilon = 1 - \left(1 - \frac{1}{M}\right)^{Q - 1}$$
    
    Anche qui, per avere probabilità di successo costante, servono $Q = \Theta(M)$ query.
    
      
    

  

  

#### 3. Algoritmo per `Collision` (Algorithm 5.3) e Birthday Attack

  

  

> [!abstract] Algorithm 5.3: `Find-Collision`$(h, Q)$
> 
>   
> 
> 1. Scegliere qualsiasi sottoinsieme $\mathcal{X}_0 \subseteq \mathcal{X}$ di cardinalità $|\mathcal{X}_0| = Q$.
>     
>       
>     
> 2. **for each** $x \in \mathcal{X}_0$ **do** $\quad y_x \leftarrow h(x)$
>     
>       
>     
> 3. **if** $y_x = y_{x'}$ per qualche coppia $x \neq x'$ **then** $\quad$ **return** $(x, x')$
>     
>       
>     
> 4. **else** **return** (_failure_)
>     
>       
>     

- **Theorem 5.2 (Probabilità di successo di `Find-Collision` e Birthday Paradox):**
    
    Denotiamo gli elementi di $\mathcal{X}_0$ con $x_1, \dots, x_Q$. Sia $E_i$ l'evento che $y_{x_i} \notin \{y_{x_1}, \dots, y_{x_{i-1}}\}$.
    
      
    - $\Pr[E_1] = 1$.
        
          
        
    - Condizionatamente a $E_1 \land \dots \land E_{i-1}$ (cioè al fatto che i primi $i-1$ valori siano tutti distinti), per il Theorem 5.1 si ha $\Pr[E_i \mid E_1 \land \dots \land E_{i-1}] = \frac{M - (i - 1)}{M} = 1 - \frac{i - 1}{M}$.
        
          
        
    - Pertanto, la probabilità di non trovare alcuna collisione è $\prod_{i=1}^{Q-1} \left(1 - \frac{i}{M}\right)$, e la probabilità di successo $\varepsilon$ di `Find-Collision` è:
        
          
        
        $$\varepsilon = 1 - \prod_{i=1}^{Q-1} \left(1 - \frac{i}{M}\right)$$
        
    - Usando l'approssimazione $1 - t \approx e^{-t}$ per piccoli valori di $t$ e la somma $\sum_{i=1}^{Q-1} i = \frac{Q(Q-1)}{2}$, si ottiene:
        
          
        
        $$1 - \varepsilon \approx \prod_{i=1}^{Q-1} e^{-i/M} = e^{-\frac{Q(Q-1)}{2M}} \quad \Longrightarrow \quad \varepsilon \approx 1 - e^{-\frac{Q(Q-1)}{2M}}$$
        
    - Risolvendo rispetto a $Q$ (ed effettuando l'approssimazione $Q^2 - Q \approx Q^2$), troviamo il numero di query $Q$ necessarie per ottenere una probabilità di successo $\varepsilon$:
        
          
        
        $$Q \approx \sqrt{2M \ln\left(\frac{1}{1 - \varepsilon}\right)}$$
        
    - Prendendo $\varepsilon = \frac{1}{2}$, questa formula fornisce:
        
          
        
        $$Q \approx \sqrt{2 \ln 2 \cdot M} \approx 1.17 \sqrt{M}$$
        
- **Il Birthday Paradox e il Birthday Attack:**
    
      
    - Se $M = 365$ (giorni dell'anno) e $\varepsilon = 1/2$, la formula dà $Q \approx 1.17 \sqrt{365} \approx 22.3$ (per $Q = 23$ persone, la probabilità esatta di avere almeno due persone con lo stesso compleanno è $\varepsilon \approx 0.507$). Questo fenomeno è noto come **birthday paradox**.
        
          
        
    - Nel contesto delle funzioni di hash, l'Algorithm 5.3 è chiamato **birthday attack**. Se una funzione di hash ha un _message digest_ di $m$ bit ($M = 2^m$), il _birthday attack_ trova una collisione con probabilità $1/2$ utilizzando appena $\approx 2^{m/2}$ query ($Q = \Theta(\sqrt{M})$), motivo per cui il numero di bit $m$ dell'output di una hash function deve essere almeno il doppio rispetto alla lunghezza della chiave di un block cipher per garantire lo stesso livello di sicurezza contro attacchi di ricerca esaustiva.
        
          
        

  

  

## 5.2.2 Comparison of Security Criteria (Confronto tra i Criteri di Sicurezza)

  

  

Nella Sezione 5.2.2 Stinson confronta la difficoltà relativa di risolvere **Preimage**, **Second Preimage** e **Collision** per una generica funzione di hash (senza assumere il _random oracle model_), dimostrando due riduzioni tramite gli **Algorithm 5.4** e **Algorithm 5.5**.

  

  

  

### 1. Riduzione da `Collision` a `Second Preimage` (Algorithm 5.4 & Theorem 5.3)

  

  

Supponiamo di disporre di un algoritmo (visto come un oracolo o scatola nera) chiamato **`Find-Second-Preimage`** che risolve il problema **Second Preimage** per $h$. Allora possiamo risolvere il problema **Collision** come segue:

  

> [!abstract] Algorithm 5.4: `Collision-To-Second-Preimage`$(h)$ **External** `Find-Second-Preimage`
> 
>   
> 
> 1. Scegliere $x \in \mathcal{X}$ uniformemente a caso.
>     
>       
>     
> 2. **if** $\text{Find-Second-Preimage}(h, x)$ restituisce $x'$ **then** $\quad$ **return** $(x, x')$
>     
>       
>     
> 3. **else** $\quad$ **return** (_failure_)
>     
>       
>     

> [!important] Theorem 5.3 Supponiamo che $h : \mathcal{X} \to \mathcal{Y}$ sia una hash function e supponiamo che esista un $(\varepsilon, Q)$-algorithm `Find-Second-Preimage` che risolve il problema **Second Preimage** per $h$. Allora `Collision-To-Second-Preimage` è un $(\varepsilon, Q)$-algorithm che risolve il problema **Collision** per $h$.
> 
>   

  

  

### 2. Riduzione da `Collision` a `Preimage` (Algorithm 5.5 & Theorem 5.4)

  

  

Supponiamo ora di disporre di un algoritmo **`Find-Preimage`** che risolve il problema **Preimage** per una funzione di hash $h : \mathcal{X} \to \mathcal{Y}$ con $|\mathcal{X}|$ finito e $|\mathcal{X}| \ge 2|\mathcal{Y}|$:

  

> [!abstract] Algorithm 5.5: `Collision-To-Preimage`$(h)$ **External** `Find-Preimage`
> 
>   
> 
> 1. Scegliere $x \in \mathcal{X}$ uniformemente a caso.
>     
>       
>     
> 2. Calcolare $y = h(x)$.
>     
>       
>     
> 3. **if** $\text{Find-Preimage}(h, y)$ restituisce $x'$ **and** $x' \neq x$ **then** $\quad$ **return** $(x, x')$
>     
>       
>     
> 4. **else** $\quad$ **return** (_failure_)
>     
>       
>     

> [!important] Theorem 5.4 Supponiamo che $h : \mathcal{X} \to \mathcal{Y}$ sia una hash function in cui $|\mathcal{X}|$ e $|\mathcal{Y}|$ sono finiti e $|\mathcal{X}| \ge 2|\mathcal{Y}|$. Supponiamo che esista un $(1, Q)$-algorithm `Find-Preimage` che risolve il problema **Preimage** per $h$. Allora `Collision-To-Preimage` è un $(1/2, Q+1)$-algorithm che risolve il problema **Collision** per $h$.
> 
>   

- **Dimostrazione del Theorem 5.4 (come svolta nel libro):**
    
      
    1. Poniamo $|\mathcal{X}| = N$ e $|\mathcal{Y}| = M$, con $N \ge 2M$. Per ogni $y \in \mathcal{Y}$, definiamo $h^{-1}(y) = \{x \in \mathcal{X} : h(x) = y\}$ e poniamo $c_y = |h^{-1}(y)|$.
        
          
        
    2. Sia $\mathcal{Y}_0 = \{y \in \mathcal{Y} : c_y > 0\}$ l'insieme degli elementi di $\mathcal{Y}$ che hanno almeno una preimmagine (ovvero l'immagine di $h$). Chiaramente $|\mathcal{Y}_0| \le M$ e $\sum_{y \in \mathcal{Y}_0} c_y = N$.
        
          
        
    3. Quando $x \in \mathcal{X}$ viene scelto uniformemente a caso al passo 1 e si calcola $y = h(x)$, l'elemento $y$ appartiene a $\mathcal{Y}_0$, e poiché per ipotesi `Find-Preimage` è un $(1, Q)$-algorithm (ha probabilità di successo $1$ su ogni $y \in \mathcal{Y}_0$), `Find-Preimage`$(h, y)$ restituirà certamente un qualche elemento $x' \in h^{-1}(y)$.
        
          
        
    4. L'Algorithm 5.5 ha successo se e solo se $x' \neq x$. Anche se `Find-Preimage` è un algoritmo deterministico che per un dato $y$ restituisce sempre lo stesso identico elemento $x' \in h^{-1}(y)$, condizionatamente all'evento $h(x) = y$, l'elemento $x$ scelto al passo 1 può essere con uguale probabilità uno qualsiasi dei $c_y$ elementi in $h^{-1}(y)$. Pertanto:
        
          
        
        $$\Pr[x \neq x' \mid h(x) = y] = \frac{c_y - 1}{c_y}$$
        
    5. Poiché $\Pr[h(x) = y] = \frac{c_y}{N}$, calcoliamo la probabilità complessiva di successo sommando su tutti gli $y \in \mathcal{Y}_0$:
        
          
        
        $$\begin{aligned} \Pr[\text{success}] &= \sum_{y \in \mathcal{Y}_0} \Pr[h(x) = y] \cdot \Pr[x \neq x' \mid h(x) = y] \\ &= \sum_{y \in \mathcal{Y}_0} \frac{c_y}{N} \left(\frac{c_y - 1}{c_y}\right) \\ &= \frac{1}{N} \sum_{y \in \mathcal{Y}_0} (c_y - 1) \\ &= \frac{N - |\mathcal{Y}_0|}{N} \ge \frac{N - M}{N} = 1 - \frac{M}{N} \ge \frac{1}{2} \end{aligned}$$
        
        poiché $N \ge 2M$. Il numero totale di valutazioni di $h$ è $Q + 1$ (le $Q$ query di `Find-Preimage` più $1$ query per calcolare $y = h(x)$ al passo 2). $\blacksquare$
        
          
        

  

  

## 5.5.3 Authenticated Encryption (CCM e GCM)

  

  

In molte applicazioni si desidera garantire contemporaneamente la **confidentiality** (tramite encryption) e la **data integrity / authentication** (tramite un MAC). Un sistema che raggiunge entrambi gli obiettivi è chiamato **authenticated encryption**.

  

Stinson distingue due approcci generali per combinare cifratura e autenticazione:

  

1. **MAC-then-encrypt:** Si calcola prima un authentication tag (MAC) sul plaintext, e successivamente si cifrano insieme il plaintext e il tag. Un esempio di questo approccio è la modalità **CCM** (**Counter with Cipher Block Chaining-Message Authentication Code**), che combina la cifratura in **counter mode (CTR)** con l'autenticazione tramite **CBC-MAC**.
    
      
    
2. **Encrypt-then-MAC:** Si cifra prima il plaintext ottenendo il ciphertext, e successivamente si calcola un authentication tag (MAC) **sul ciphertext**. Un esempio fondamentale di questo approccio è la modalità **GCM** (**Galois Counter Mode**).
    
      
    

  

  

### Galois Counter Mode (GCM)

  

  

Il **Galois Counter Mode (GCM)** utilizza un metodo di tipo **encrypt-then-MAC**: il plaintext viene prima cifrato usando **AES in counter mode**, e poi viene calcolato un **MAC** sul ciphertext risultante. Inoltre, GCM consente di autenticare anche ulteriori **authenticated data** (dati autenticati che non vengono cifrati, ma che vengono inclusi nel calcolo dell'**authentication tag**).

  

Il calcolo del MAC in GCM si basa su moltiplicazioni per un elemento fisso $H$ all'interno del campo finito **$\mathbb{F}_{2^{128}}$**, definito tramite il polinomio irriducibile:

  

$$p(\alpha) = \alpha^{128} + \alpha^7 + \alpha^2 + \alpha + 1 \in \mathbb{Z}_2[\alpha]$$

Ecco la descrizione esatta dei passaggi di GCM (illustrati nella **Figure 5.3** del libro per un singolo blocco di _authenticated data_ `Auth data 1` e due blocchi di plaintext `Plaintext 1` e `Plaintext 2`):

  

1. **Inizializzazione di `Counter 0` e incremento dei contatori (`incr`):**
    
      
    - Si sceglie un **96-bit initialization vector (IV)**, il quale viene concatenato con **32 bit uguali a `0`** per formare un contatore iniziale di 128 bit chiamato **`Counter 0`**.
        
          
        
    - Il contatore viene poi incrementato di $1$ ad ogni passo (tramite la funzione **`incr`**, tutte le addizioni sono ridotte modulo $2^{32}$ sui 32 bit meno significativi, o come contatore binario) producendo **`Counter 1`**, **`Counter 2`**, ecc.
        
          
        
    - L'$IV$ deve essere cambiato ogni volta che viene eseguita una nuova cifratura.
        
          
        
2. **Cifratura dei blocchi di Plaintext in Counter Mode:**
    
      
    - I blocchi di plaintext da 128 bit (`Plaintext 1`, `Plaintext 2`, $\dots$) vengono cifrati in **counter mode** usando **AES** (con la chiave segreta $K$) applicato a `Counter 1`, `Counter 2`, $\dots$:
        
          
        
        $$\begin{aligned} \text{Ciphertext } 1 &= \text{Plaintext } 1 \oplus e_K(\text{Counter } 1) \\ \text{Ciphertext } 2 &= \text{Plaintext } 2 \oplus e_K(\text{Counter } 2) \end{aligned}$$
        
3. **Determinazione dell'elemento $H \in \mathbb{F}_{2^{128}}$:**
    
      
    - Il calcolo dell'**authentication tag** (`Auth tag`) richiede di effettuare moltiplicazioni nel campo finito $\mathbb{F}_{2^{128}} = \mathbb{Z}_2[\alpha]/(\alpha^{128} + \alpha^7 + \alpha^2 + \alpha + 1)$ per un particolare elemento fisso $H \in \mathbb{F}_{2^{128}}$ (operazione indicata nella Figure 5.3 con **`mult_H`**).
        
          
        
    - Come indicato nel libro, il valore di $H$ viene determinato cifrando `Counter 0` con AES.
        
          
        
4. **Catena di XOR ($\oplus$) e moltiplicazioni per $H$ (`mult_H`) per calcolare `Auth tag`:**
    
      
    - L'**authentication tag** (di lunghezza 128 bit) viene costruito processando in sequenza il blocco di dati autenticati (`Auth data 1`), i blocchi di testo cifrato (`Ciphertext 1`, `Ciphertext 2`) e il blocco delle lunghezze (`len(A) || len(C)`), alternando l'operazione di **exclusive-or ($\oplus$)** e la moltiplicazione per $H$ (**`mult_H`**) in $\mathbb{F}_{2^{128}}$:
        
          
        1. Si moltiplica `Auth data 1` per $H$ tramite `mult_H`;
            
              
            
        2. Si fa l'_exclusive-or_ ($\oplus$) del risultato con `Ciphertext 1` e si applica `mult_H`;
            
              
            
        3. Si fa l'_exclusive-or_ ($\oplus$) del risultato con `Ciphertext 2` e si applica `mult_H`;
            
              
            
        4. Si fa l'_exclusive-or_ ($\oplus$) del risultato con la stringa di 128 bit **`len(A) || len(C)`** (che rappresenta la concatenazione della lunghezza in bit degli _authenticated data_ $A$, su 64 bit, e della lunghezza in bit del _ciphertext_ $C$, su 64 bit) e si applica ancora `mult_H`;
            
              
            
        5. Infine, si effettua un ultimo **exclusive-or ($\oplus$)** con il blocco di 128 bit ottenuto cifrando **`Counter 0`** con AES ($e_K(\text{Counter } 0)$), ottenendo in output l'**`Auth tag`** finale.
            
              
            
5. **Decifratura e Verifica in GCM:**
    
      
    - Chi riceve il messaggio ricalcola l'**authentication tag** a partire da $IV$, dagli _authenticated data_ e dai blocchi di _ciphertext_ ricevuti (eseguendo esattamente la stessa catena di operazioni `mult_H` e $\oplus$), e verifica che coincida con l'`Auth tag` ricevuto prima di accettare i blocchi di plaintext decifrati tramite il _counter mode_.
        
          
        

Se vuoi che ti generi direttamente un file `.md` scaricabile con tutto questo contenuto aggiornato, dimmelo pure!
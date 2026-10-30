  

**6.1 Introduction to Public-key Cryptography (Introduzione alla Crittografia a Chiave Pubblica)**

  

Nel modello classico della crittografia che abbiamo studiato finora, Alice e Bob scelgono segretamente la chiave $K$. $K$ dà poi origine a una _encryption rule_ (regola di cifratura) $e_K$ e a una _decryption rule_ (regola di decifratura) $d_K$. Nei crittosistemi visti finora, $d_K$ è identica a $e_K$, oppure è facilmente derivabile da essa. Un crittosistema di questo tipo è noto come **secret-key cryptosystem** (crittosistema a chiave segreta) o, in alternativa, **symmetric-key cryptosystem** (crittosistema a chiave simmetrica). Di solito, in un tale crittosistema, la compromissione (_exposure_) sia di $e_K$ che di $d_K$ rende il sistema insicuro.

  

Uno svantaggio di un _secret-key cryptosystem_ è che richiede la comunicazione preventiva della chiave $K$ tra Alice e Bob, utilizzando un _secure channel_ (canale sicuro), prima che qualsiasi _ciphertext_ (testo cifrato) venga trasmesso. Nella pratica, ciò può essere molto difficile da realizzare. Ad esempio, supponiamo che Alice e Bob vivano molto lontani l'uno dall'altra e decidano di voler comunicare elettronicamente, tramite email. In una situazione come questa, Alice e Bob potrebbero non avere accesso a un canale sufficientemente sicuro.

  

L'idea alla base di un **public-key cryptosystem** (crittosistema a chiave pubblica) è che potrebbe essere possibile trovare un crittosistema in cui sia _computationally infeasible_ (computazionalmente infattibile) determinare $d_K$ a partire da $e_K$. Se così fosse, l'_encryption rule_ $e_K$ diverrebbe una **public key** (chiave pubblica), il cui valore potrebbe essere reso noto a tutti (da qui il termine _public-key system_). Il vantaggio di un _public-key system_ è che Alice (o chiunque altro) può inviare un messaggio cifrato a Bob (senza la comunicazione preventiva di una chiave segreta condivisa) utilizzando l'_encryption rule_ pubblica $e_K$. Bob sarà l'unica persona in grado di decifrare il _ciphertext_, utilizzando la _decryption rule_ $d_K$, che è chiamata **private key** (chiave privata).

  

Quando Alice vuole cifrare un messaggio da inviare a Bob, è fondamentale che la chiave di cifratura pubblica che Alice sta utilizzando sia effettivamente la chiave pubblica di Bob. Nella pratica, le chiavi pubbliche vengono autenticate tramite **certificates** (certificati).

  

Tra i _public-key cryptosystems_, i più importanti sono il **RSA Cryptosystem** (e le sue varianti), in cui la sicurezza è basata sulla difficoltà di fattorizzare numeri interi molto grandi; e l'**ElGamal Cryptosystem** (e varianti come gli _Elliptic Curve Cryptosystems_), in cui la sicurezza è basata sul problema del logaritmo discreto (_discrete logarithm problem_).

  

Tutti gli esempi noti di _public-key cryptosystems_ sicuri sono molto più lenti rispetto ai _secret-key cryptosystems_ comunemente usati come AES. Quindi, nella pratica, i _public-key cryptosystems_ non vengono quasi mai utilizzati per cifrare messaggi "lunghi"; il loro impiego principale risiede nella cifratura di chiavi brevi utilizzate nei _secret-key cryptosystems_. Potremmo cifrare i dati utilizzando AES e poi cifrare la chiave AES utilizzando un _public-key cryptosystem_. Questo processo è noto come **hybrid cryptography** (crittografia ibrida). Nel dettaglio, nella _hybrid cryptography_ viene utilizzato il seguente processo in due fasi:

  

1. Alice sceglie dapprima una chiave $L$ per un _secret-key cryptosystem_ e calcola $y = e_L(x)$.
    
      
    
2. Alice poi cifra $L$ usando la chiave pubblica di Bob, $e_{K_{\text{Bob}}}$, relativa a un _public-key cryptosystem_, ottenendo $z = e_{K_{\text{Bob}}}(L)$.
    
      
    

Il _ciphertext_ $y$ e la chiave cifrata $z$ verrebbero trasmessi entrambi a Bob. Quando Bob riceve $y$ e $z$, decifra il _ciphertext_ nel modo seguente:

  

1. Bob decifra dapprima $z$ utilizzando la sua _private key_ $d_{K_{\text{Bob}}}$, ottenendo $L = d_{K_{\text{Bob}}}(z)$.
    
      
    
2. Bob utilizza poi $L$ per decifrare $y$, ottenendo il _plaintext_ $x = d_L(y)$.
    
      
    

Un'osservazione molto importante è che un _public-key cryptosystem_ non può mai fornire **unconditional security** (sicurezza incondizionata). Questo perché un avversario (_opponent_), osservando un _ciphertext_ $y$, può cifrare a turno ogni possibile _plaintext_ utilizzando l'_encryption rule_ pubblica $e_K$ fino a trovare l'unico $x$ tale che $y = e_K(x)$. Questo $x$ è la decifratura di $y$. Di conseguenza, per i _public-key systems_ si studia la **computational security** (sicurezza computazionale).

  

Concettualmente è utile pensare a un _public-key system_ in termini di un'astrazione chiamata **trapdoor one-way function** (funzione one-way con trapdoor). Definiamo ora informalmente questa nozione.

  

La funzione di cifratura pubblica di Bob, $e_K$, dovrebbe essere facile da calcolare. Abbiamo appena notato che calcolare la funzione inversa (cioè decifrare) dovrebbe essere difficile (per chiunque tranne che per Bob). Si ricordi che una funzione facile da calcolare ma difficile da invertire è spesso chiamata **one-way function**. Nel contesto della cifratura, desideriamo che $e_K$ sia una _one-way function_ iniettiva (_injective_), affinché sia possibile eseguire la decifratura. Sfortunatamente, sebbene esistano molte funzioni iniettive che si ritiene siano _one-way_, al momento non esistono funzioni di cui si possa dimostrare matematicamente tale proprietà.

  

Ecco un esempio di una funzione che si ritiene sia _one-way_. Supponiamo che $n$ sia il prodotto di due grandi numeri primi $p$ e $q$, e sia $b$ un numero intero positivo. Definiamo allora $f: \mathbb{Z}_n \to \mathbb{Z}_n$ come:

  

$$f(x) = x^b \bmod n$$

(Se $\gcd(b, \phi(n)) = 1$, allora questa è a tutti gli effetti una funzione di cifratura RSA).

  

Se vogliamo costruire un _public-key cryptosystem_, non è sufficiente trovare una _one-way function_ iniettiva. Non vogliamo che $e_K$ sia _one-way_ dal punto di vista di Bob, perché egli ha bisogno di poter decifrare i messaggi che riceve in modo efficiente. Pertanto, è necessario che Bob possieda una **trapdoor** (scorciatoia segreta), che consiste in un'informazione segreta che permette di invertire facilmente $e_K$. In altre parole, Bob è in grado di decifrare in modo efficiente perché possiede una conoscenza segreta aggiuntiva, ovvero $K$, che gli fornisce la funzione di decifratura $d_K$. Diremo quindi che una funzione è una **trapdoor one-way function** se è una _one-way function_, ma diventa facile da invertire conoscendo una determinata _trapdoor_.

  

La _trapdoor_ è un metodo efficiente per calcolare l'esponente corretto $a$ (in funzione di $b$), che sfrutta la fattorizzazione di $n$.

  

È spesso conveniente specificare una famiglia di _trapdoor one-way functions_, diciamo $\mathcal{F}$. A quel punto, una funzione $f \in \mathcal{F}$ viene scelta a caso e usata come funzione di cifratura pubblica; la funzione inversa, $f^{-1}$, rappresenta la funzione di decifratura privata. Ciò è analogo a scegliere una chiave casuale da uno spazio delle chiavi specificato, come facevamo per i _secret-key cryptosystems_.
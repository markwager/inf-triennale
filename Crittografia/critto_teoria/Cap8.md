# Capitolo 8: Signature Schemes (Schemi di Firma)

### 8.1 Introduction (Introduzione)

Una firma manoscritta convenzionale apposta su un documento serve a identificare la persona che ne è responsabile.  Uno **signature scheme** è un metodo crittografico per firmare un messaggio in forma elettronica, consentendo così di trasmettere il messaggio firmato su una rete di computer.

  

#### 1. Differenze Fondamentali tra Firme Convenzionali e Firme Digitali

Esistono tre differenze sostanziali tra le firme cartacee tradizionali e le firme digitali:

  

1. **Legame tra firma e documento (_Binding_):**
    
      
    - In una firma convenzionale, la firma fa fisicamente parte del documento cartaceo che viene sottoscritto.
        
          
        
    - Una firma digitale, invece, non è fisicamente attaccata al messaggio: l'algoritmo di firma deve quindi "legare" (_bind_) matematicamente la firma allo specifico messaggio.
        
          
        
2. **Procedura di verifica (_Verification_):**
    
      
    - Una firma convenzionale viene verificata confrontandola visivamente con altre firme autentiche (un metodo poco sicuro, poiché è relativamente semplice falsificare la grafia altrui).
        
          
        
    - Le firme digitali vengono invece verificate mediante un **verification algorithm** (algoritmo di verifica) pubblicamente noto: di conseguenza, "chiunque" può verificare la validità di una firma digitale e l'impiego di uno schema sicuro previene la possibilità di falsificazioni (_forgeries_).
        
          
        
3. **Distinguibilità delle copie e prevenzione del riutilizzo (_Reusability_):**
    
      
    - Mentre la copia di un documento cartaceo firmato è solitamente distinguibile dall'originale, una "copia" di un messaggio digitale firmato è bit a bit **identica all'originale**.
        
          
        
    - Occorre quindi prestare attenzione a impedire il riutilizzo fraudolento di un messaggio digitale firmato: ad esempio, se Alice firma un messaggio digitale che autorizza Bob a prelevare $\$100$ dal suo conto bancario (come un assegno), vuole che Bob possa incassarlo una sola volta. Per questo motivo, il messaggio stesso deve contenere informazioni contestuali (come una data o un _timestamp_) che ne impediscano il riutilizzo.
        
          
        

#### 2. Componenti e Definizione Formale di uno Schema di Firma

Uno schema di firma si compone di due operazioni principali:

  

- **Signing algorithm ($\mathbf{sig}_K$):** Alice firma un messaggio $x$ utilizzando un algoritmo di firma privato $\mathbf{sig}_K$ (che dipende dalla sua chiave privata in $K$), producendo la firma $y = \mathbf{sig}_K(x)$.
    
      
    
- **Verification algorithm ($\mathbf{ver}_K$):** Chiunque riceva la coppia $(x, y)$, dove $x$ è il messaggio e $y$ è la presunta firma su $x$, può verificarla tramite l'algoritmo pubblico $\mathbf{ver}_K$ (che dipende dalla chiave pubblica in $K$), ottenendo in output $\mathit{true}$ oppure $\mathit{false}$ a seconda che $y$ sia o meno una firma valida per $x$.
    
      
    

> [!abstract] Definition 8.1: Signature Scheme (Schema di Firma) Un **signature scheme** è una quintupla $(\mathcal{P}, \mathcal{A}, \mathcal{K}, \mathcal{S}, \mathcal{V})$, in cui sono soddisfatte le seguenti condizioni:
> 
>   
> 
> 1. $\mathcal{P}$ è un insieme finito di possibili **messages** (messaggi);
>     
>       
>     
> 2. $\mathcal{A}$ è un insieme finito di possibili **signatures** (firme);
>     
>       
>     
> 3. $\mathcal{K}$, il **keyspace** (spazio delle chiavi), è un insieme finito di possibili **keys** (chiavi, intese come coppie di chiavi privata e pubblica);
>     
>       
>     
> 4. Per ciascun $K \in \mathcal{K}$, esiste un **signing algorithm** (algoritmo di firma) $\mathbf{sig}_K \in \mathcal{S}$ e un corrispondente **verification algorithm** (algoritmo di verifica) $\mathbf{ver}_K \in \mathcal{V}$. Ciascun $\mathbf{sig}_K : \mathcal{P} \to \mathcal{A}$ e $\mathbf{ver}_K : \mathcal{P} \times \mathcal{A} \to \{\mathit{true}, \mathit{false}\}$ sono funzioni$^a$ tali che la seguente equazione sia soddisfatta per ogni messaggio $x \in \mathcal{P}$ e per ogni firma $y \in \mathcal{A}$:
>     
>       
>     
>     $$\mathbf{ver}_K(x, y) = \begin{cases} \mathit{true} & \text{se } y = \mathbf{sig}_K(x) \\ \mathit{false} & \text{se } y \neq \mathbf{sig}_K(x). \end{cases}$$
>     
> 
> Una coppia $(x, y)$ con $x \in \mathcal{P}$ e $y \in \mathcal{A}$ è chiamata un **signed message** (messaggio firmato).
> 
>   
> 
> _$^a$Nota: In alcuni schemi di firma, l'algoritmo di firma $\mathbf{sig}_K$ è randomizzato (per cui possono esistere più firme valide $y$ associate allo stesso messaggio $x$)_.
> 
>   

#### 3. Requisiti Computazionali e Falsificazione (Forgery)

- **Calcolabilità in tempo polinomiale e visibilità:** Per ogni $K \in \mathcal{K}$, entrambe le funzioni $\mathbf{sig}_K$ e $\mathbf{ver}_K$ devono essere **polynomial-time functions** (funzioni calcolabili in tempo polinomiale). L'algoritmo di firma $\mathbf{sig}_K$ è mantenuto **privato** (noto solo ad Alice), mentre l'algoritmo di verifica $\mathbf{ver}_K$ è **pubblico**.
    
      
    
- **Infattibilità computazionale e Forgery (Falsificazione):**
    
      
    - Dato un messaggio $x \in \mathcal{P}$, deve essere computazionalmente infattibile per chiunque all'infuori di Alice calcolare una firma $y \in \mathcal{A}$ tale che $\mathbf{ver}_K(x, y) = \mathit{true}$.
        
          
        
    - Se un avversario Oscar riesce a calcolare una coppia $(x, y)$ tale che $\mathbf{ver}_K(x, y) = \mathit{true}$ per un messaggio $x$ che **non** è stato precedentemente firmato da Alice, allora la firma $y$ è chiamata una **forgery** (falsificazione). Informalmente, una _forged signature_ è una firma valida prodotta da chiunque non sia il legittimo firmatario Alice.






## Schema di firma di ElGamal

Serve a generare firme digitali.

Sia $p$ un numero primo tale che il problema del logaritmo discreto in $\mathbb{Z}_p$ sia intrattabile, e sia $\alpha \in \mathbb{Z}_p^*$ un elemento primitivo. Siano $\mathcal{P} = \mathbb{Z}_p^*$, $\mathcal{A} = \mathbb{Z}_p^* \times \mathbb{Z}_{p-1}$, e definiamo:

$$\mathcal{K} = \{(p, \alpha, a, \beta) : \beta \equiv \alpha^a \pmod{p}\}.$$

I valori $p$, $\alpha$ e $\beta$ costituiscono la chiave pubblica, mentre $a$ è la chiave privata.

Per $K = (p, \alpha, a, \beta)$ e per un numero casuale (segreto) $k \in \mathbb{Z}_{p-1}^*$, definiamo:

$$\mathbf{sig}_K(x, k) = (\gamma, \delta),$$

dove:

$$\gamma = \alpha^k \bmod p$$

e

$$\delta = (x - a\gamma)k^{-1} \bmod (p - 1).$$

Per $x, \gamma \in \mathbb{Z}_p^*$ e $\delta \in \mathbb{Z}_{p-1}$, definiamo:

$$\mathbf{ver}_K(x, (\gamma, \delta)) = \text{true} \iff \beta^\gamma \gamma^\delta \equiv \alpha^x \pmod{p}.$$


Lo Schema di Firma di ElGamal è randomizzato (si ricordi che anche il Crittosistema a Chiave Pubblica di ElGamal è randomizzato). Ciò significa che esistono molte firme valide per ogni dato messaggio, e l'algoritmo di verifica deve essere in grado di accettare come autentica ciascuna di queste firme valide.
Iniziamo con delle osservazioni. Una firma di ElGamal è composta da due componenti $\gamma$ e $\delta$.  $\gamma$ si ottiene elevando $\alpha$ a una potenza casuale modulo $p$; essa non dipende dal messaggio $x$ che viene firmato. La seconda componente, $\delta$, dipende invece sia dal messaggio $x$ sia dalla chiave privata $a$. La verifica della firma si effettua controllando che una determinata congruenza valga modulo $p$; ovviamente, tale congruenza non coinvolge la chiave privata.

Mostriamo ora che, se la firma è stata costruita correttamente, la verifica avrà successo. Ciò segue facilmente dalle seguenti congruenze:

$$\begin{aligned} \beta^\gamma \gamma^\delta &\equiv \alpha^{a\gamma} \alpha^{k\delta} \pmod{p} \\ &\equiv \alpha^x \pmod{p}, \end{aligned}$$

dove sfruttiamo il fatto che:

$$a\gamma + k\delta \equiv x \pmod{p - 1}.$$

In realtà, risulta meno misterioso partire dall'equazione di verifica e derivare poi la corrispondente funzione di firma. Supponiamo di iniziare dalla congruenza:

$$\alpha^x \equiv \beta^\gamma \gamma^\delta \pmod{p}. \qquad (8.1)$$

Effettuiamo quindi le sostituzioni:

$$\gamma \equiv \alpha^k \pmod{p} \qquad \text{e} \qquad \beta \equiv \alpha^a \pmod{p},$$

ma senza sostituire $\gamma$ nell'esponente della $(8.1)$. Otteniamo quanto segue:

$$\alpha^x \equiv \alpha^{a\gamma + k\delta} \pmod{p}.$$
Ora, $\alpha$ è un elemento primitivo modulo $p$; pertanto questa congruenza è vera se e solo se gli esponenti sono congrui modulo $p - 1$, ovvero se e solo se:

$$x \equiv a\gamma + k\delta \pmod{p - 1}.$$

Dati $x$, $a$, $\gamma$ e $k$, questa congruenza può essere risolta rispetto a $\delta$, ottenendo la formula utilizzata nella funzione di firma del _Cryptosystem 8.2_.

Alice calcola una firma utilizzando sia la chiave privata $a$, sia il numero casuale segreto $k$ (che viene usato per firmare un singolo messaggio, $x$). La verifica può invece essere eseguita utilizzando unicamente informazioni pubbliche.

Vediamo un piccolo esempio per illustrare i calcoli aritmetici.

**Example 8.1** Supponiamo di prendere $p = 467$, $\alpha = 2$, $a = 127$; allora:

$$\begin{aligned} \beta &= \alpha^a \bmod p \\ &= 2^{127} \bmod 467 \\ &= 132. \end{aligned}$$

Supponiamo che Alice voglia firmare il messaggio $x = 100$ e scelga il valore casuale $k = 213$ (si noti che $\gcd(213, 466) = 1$ e $213^{-1} \bmod 466 = 431$). Allora:

$$\gamma = 2^{213} \bmod 467 = 29$$

e

$$\delta = (100 - 127 \times 29)431 \bmod 466 = 51.$$

Chiunque può verificare la firma $(29, 51)$ controllando che:

$$132^{29} \cdot 29^{51} \equiv 189 \pmod{467}$$

e

$$2^{100} \equiv 189 \pmod{467}.$$

Pertanto, la firma è valida.


**8.3.1 Sicurezza dello Schema di Firma di ElGamal**

Esaminiamo la sicurezza dello Schema di Firma di ElGamal. Supponiamo che Oscar tenti di falsificare una firma per un messaggio $x$, senza conoscere $a$. Se Oscar sceglie un valore $\gamma$ e cerca poi di trovare il corrispondente $\delta$, deve calcolare il logaritmo discreto $\log_\gamma (\alpha^x \beta^{-\gamma})$. Se sceglie prima $\delta$ e cerca poi di trovare $\gamma$, sta tentando di "risolvere" l'equazione

  

$$\beta^\gamma \gamma^\delta \equiv \alpha^x \pmod{p}$$

nell'"incognita" $\gamma$. Si tratta di un problema per il quale non è nota alcuna soluzione fattibile; tuttavia, non sembra essere collegato ad alcun problema come il problema del Logaritmo Discreto. Rimane inoltre la possibilità che esista un qualche modo per calcolare $\gamma$ e $\delta$ simultaneamente in modo tale che $(\gamma, \delta)$ costituisca una firma. Nessuno ha scoperto un modo per farlo, ma viceversa nessuno ha dimostrato che non possa essere fatto.

  

Se Oscar sceglie $\gamma$ e $\delta$ e cerca poi di risolvere rispetto a $x$, si ritrova nuovamente di fronte a un'istanza del problema del Logaritmo Discreto, ovvero il calcolo di $\log_\alpha (\beta^\gamma \gamma^\delta)$. Pertanto, Oscar non può firmare un determinato messaggio $x$ utilizzando questo approccio.

  

Esiste tuttavia un metodo tramite il quale Oscar può firmare un messaggio casuale scegliendo $\gamma$, $\delta$ e $x$ simultaneamente. È quindi possibile una **falsificazione esistenziale** (mediante un **attacco a sola chiave** (_key-only attack_), assumendo che non venga utilizzata una funzione di hash. Descriviamo ora come procedere.

  

Supponiamo che $i$ e $j$ siano interi tali che $0 \le i \le p - 2$, $0 \le j \le p - 2$, e supponiamo di esprimere $\gamma$ nella forma $\gamma = \alpha^i \beta^j \bmod p$. Allora la condizione di verifica è:

  

$$\alpha^x \equiv \beta^\gamma (\alpha^i \beta^j)^\delta \pmod{p}.$$

Ciò è equivalente a:

  

$$\alpha^{x - i\delta} \equiv \beta^{\gamma + j\delta} \pmod{p}.$$

Quest'ultima congruenza risulterà soddisfatta se:

  

$$x - i\delta \equiv 0 \pmod{p - 1}$$

e

  

$$\gamma + j\delta \equiv 0 \pmod{p - 1}.$$

Dati $i$ e $j$, possiamo risolvere facilmente queste due congruenze modulo $p - 1$ rispetto a $\delta$ e $x$, purché $\gcd(j, p - 1) = 1$. Otteniamo quanto segue:

  

$$\begin{aligned} \gamma &= \alpha^i \beta^j \bmod p, \\ \delta &= -\gamma j^{-1} \bmod (p - 1), \quad \text{e} \\ x &= -\gamma i j^{-1} \bmod (p - 1). \end{aligned}$$

Per il modo in cui abbiamo costruito $(\gamma, \delta)$, è chiaro che essa è una firma valida per il messaggio $x$.

  

Illustriamo il procedimento con un esempio.

  

**Example 8.2** Come nell'esempio precedente, supponiamo che $p = 467$, $\alpha = 2$ e $\beta = 132$. Supponiamo che Oscar scelga $i = 99$ e $j = 179$; allora $j^{-1} \bmod (p - 1) = 151$. Egli calcolerà quanto segue:

  

$$\begin{aligned} \gamma &= 2^{99} \cdot 132^{179} \bmod 467 = 117 \\ \delta &= -117 \times 151 \bmod 466 = 41 \\ x &= 99 \times 41 \bmod 466 = 331. \end{aligned}$$

Allora $(117, 41)$ è una firma valida per il messaggio $331$, come si può verificare controllando che:

  

$$132^{117} \cdot 117^{41} \equiv 303 \pmod{467}$$

e

  

$$2^{331} \equiv 303 \pmod{467}.$$

Ecco un secondo tipo di falsificazione, in cui Oscar parte da un messaggio precedentemente firmato da Alice. Si tratta di una **falsificazione esistenziale** mediante un **attacco a messaggio noto** (_known message attack_). Supponiamo che $(\gamma, \delta)$ sia una firma valida per un messaggio $x$. Allora è possibile per Oscar firmare vari altri messaggi. Supponiamo che $h$, $i$ e $j$ siano interi, $0 \le h, i, j \le p - 2$, e $\gcd(h\gamma - j\delta, p - 1) = 1$. Calcoliamo quanto segue:

  

$$\begin{aligned} \lambda &= \gamma^h \alpha^i \beta^j \bmod p, \\ \mu &= \delta\lambda(h\gamma - j\delta)^{-1} \bmod (p - 1), \quad \text{e} \\ x' &= \lambda(hx + i\delta)(h\gamma - j\delta)^{-1} \bmod (p - 1). \end{aligned}$$

È quindi laborioso ma diretto verificare che la condizione di verifica

  

$$\beta^\lambda \lambda^\mu \equiv \alpha^{x'} \pmod{p}$$

è soddisfatta. Pertanto $(\lambda, \mu)$ è una firma valida per $x'$.

  

Entrambi questi metodi costituiscono falsificazioni esistenziali, ma non sembra che possano essere modificati per produrre **falsificazioni selettive** (_selective forgeries_). Di conseguenza, essi non sembrano rappresentare una minaccia per la sicurezza dello Schema di Firma di ElGamal, a condizione che venga utilizzata una funzione di hash sicura come descritto nella Sezione 8.2.1.

  

Menzioniamo anche un paio di modi in cui lo Schema di Firma di ElGamal può essere violato se viene utilizzato in modo incauto (si tratta di ulteriori esempi di _protocol failures_, introdotti negli Esercizi del Capitolo 6). In primo luogo, il valore casuale $k$ utilizzato nel calcolo di una firma non deve essere rivelato. Infatti, se $k$ è noto e $\gcd(\gamma, p - 1) = 1$, è molto semplice calcolare:

  

$$a = (x - k\delta)\gamma^{-1} \bmod (p - 1).$$

Una volta noto $a$, il sistema è completamente compromesso e Oscar può falsificare firme a piacimento.

  

Un altro uso improprio del sistema consiste nell'utilizzare lo stesso valore $k$ per firmare due messaggi diversi. Ciò comporterà la ripetizione del valore $\gamma$, e renderà inoltre facile per Oscar calcolare $a$ e quindi violare il sistema. Si può procedere come segue. Supponiamo che $(\gamma, \delta_1)$ sia una firma su $x_1$ e $(\gamma, \delta_2)$ sia una firma su $x_2$. Allora abbiamo:

  

$$\beta^\gamma \gamma^{\delta_1} \equiv \alpha^{x_1} \pmod{p}$$

e

  

$$\beta^\gamma \gamma^{\delta_2} \equiv \alpha^{x_2} \pmod{p}.$$

Dunque:

  

$$\alpha^{x_1 - x_2} \equiv \gamma^{\delta_1 - \delta_2} \pmod{p}.$$

Scrivendo $\gamma = \alpha^k$, otteniamo la seguente equazione nell'incognita $k$:

  

$$\alpha^{x_1 - x_2} \equiv \alpha^{k(\delta_1 - \delta_2)} \pmod{p},$$

che è equivalente a:

  

$$x_1 - x_2 \equiv k(\delta_1 - \delta_2) \pmod{p - 1}. \qquad (8.2)$$

Sia $d = \gcd(\delta_1 - \delta_2, p - 1)$. Se $d = 1$, allora possiamo risolvere immediatamente la $(8.2)$, ottenendo:

  

$$k = (x_1 - x_2)(\delta_1 - \delta_2)^{-1} \bmod (p - 1).$$

Tuttavia, anche se $d > 1$, potremmo comunque essere in grado di determinare $k$, purché $d$ non sia troppo grande. Poiché $d \mid (p - 1)$ e $d \mid (\delta_1 - \delta_2)$, ne segue che $d \mid (x_1 - x_2)$. Definiamo:

  

$$x' = \frac{x_1 - x_2}{d}, \qquad \delta' = \frac{\delta_1 - \delta_2}{d}, \qquad p' = \frac{p - 1}{d}.$$

Allora la congruenza $(8.2)$ diventa:

  

$$x' \equiv k\delta' \pmod{p'}.$$

Poiché $\gcd(\delta', p') = 1$, possiamo calcolare:

  

$$e = (\delta')^{-1} \bmod p'.$$

Il valore di $k$ risulta determinato modulo $p'$ come:

  

$$k = x'e \bmod p'.$$

Ciò fornisce $d$ valori candidati per $k$:

  

$$k = x'e + ip' \bmod (p - 1)$$

per qualche $i$, con $0 \le i \le d - 1$. Tra questi $d$ valori candidati, l'(unico) valore corretto può essere individuato verificando la condizione:

$$\gamma \equiv \alpha^k \pmod{p}.$$
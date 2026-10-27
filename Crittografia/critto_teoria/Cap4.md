
Il Capitolo 4 introduce i moderni cifrari a blocchi iterati (_iterated block ciphers_), concentrandosi sull'architettura delle **Reti a Sostituzione-Permutazione (SPN)** e sulle tecniche avanzate per attaccarle, in particolare la **Crittoanalisi Differenziale** sviluppata da Biham e Shamir.


## 4.1 Introduzione ai Cifrari a Blocchi Iterati

- **Limite del One-Time Pad e necessità dei cifrari moderni:** Sebbene il One-Time Pad offra segretezza perfetta, richiede chiavi lunghe quanto il messaggio utilizzabili una sola volta. Nella pratica si utilizzano **Block Ciphers** (cifrari a blocchi) o **Stream Ciphers** (cifrari a flusso) computazionalmente sicuri, in cui una singola chiave segreta $K$ di lunghezza fissa permette di cifrare in sicurezza molti blocchi di testo in chiaro.
    
      
    
- **Struttura di un Cifrario Iterato (Iterated Cipher):**
    
    Un cifrario a blocchi iterato trasforma un blocco di plaintext $x$ di lunghezza fissa (es. $N$ bit) in un blocco di ciphertext $y$ della stessa lunghezza applicando in sequenza **$N_r$ iterazioni** di una funzione invertibile detta **funzione di round** (_round function_).
    
      
    
- **Key Schedule e Sottochiavi di Round (Round Keys / Subkeys):**
    
    Dalla chiave segreta principale $K$ (_master key_), un algoritmo pubblico e deterministico detto **key schedule** genera una sequenza di sottochiavi $K^1, K^2, \dots, K^{N_r}$ (ed eventualmente una chiave finale di post-whitening $K^{N_r+1}$).
    
      
    - Ad ogni round $r$ ($1 \le r \le N_r$), lo stato intermedio viene trasformato usando la corrispondente sottochiave $K^r$.
        
          
        
    - Per decifrare il blocco cifrato $y$, Bob applica le operazioni inverse di ciascun round utilizzando le stesse sottochiavi ma **in ordine inverso** ($K^{N_r+1}, K^{N_r}, \dots, K^1$).
        
          
        
- **Principio di Confusione e Diffusione (Shannon):**
    
    I cifrari iterati alternano operazioni non lineari su piccoli blocchi (**confusione**, realizzata tramite _S-box_ per rendere complessa la relazione algebrica tra chiave e testo cifrato) e operazioni di rimescolamento globale dei bit (**diffusione**, realizzata tramite _permutazioni_ o trasformazioni lineari per disperdere la statistica di un singolo bit del plaintext su molti bit del ciphertext).
    
      
    

## 4.2 Substitution-Permutation Networks (SPN)

Una **Substitution-Permutation Network (SPN)** è un cifrario iterato che realizza direttamente il paradigma di confusione e diffusione alternando tre operazioni fondamentali in ciascuno degli $N_r$ round:

  

1. **Key Mixing (XOR con la sottochiave di round):** Lo stato corrente viene combinato bit a bit tramite XOR ($\oplus$) con la sottochiave $K^r$.
    
      
    
2. **Substitution (Strato non lineare di S-box):** Il blocco di stato di lunghezza $\ell \cdot m$ bit viene diviso in $m$ sottoblocchi da $\ell$ bit ciascuno; ogni sottoblocco passa attraverso una **S-box** (_Substitution box_) $\pi_S : \{0, 1\}^\ell \to \{0, 1\}^\ell$, che è una permutazione fissa, pubblica e **fortemente non lineare** delle $2^\ell$ stringhe binarie di lunghezza $\ell$ (sostituzione vera e propria).
    
      
    
3. **Permutation (Strato lineare di diffusione):** L'intero blocco di $\ell \cdot m$ bit in uscita dalle S-box viene riordinato bit a bit secondo una permutazione fissa delle posizioni (riarrangiamento dei bit) $\pi_P : \{1, \dots, \ell m\} \to \{1, \dots, \ell m\}$. _(Nota: nell'ultimo round $N_r$, la permutazione $\pi_P$ viene solitamente omessa perché non aggiunge sicurezza crittografica, e viene sostituita da un ultimo XOR finale con la sottochiave $K^{N_r+1}$, detto **whitening**)._
    
      
    

### 4.2.1 Definizione Formale e Pseudocodice di una SPN

> [!abstract] Cryptosystem 4.1: Substitution-Permutation Network (SPN)
> 
> Siano $\ell, m, N_r$ interi positivi. Sia $\pi_S : \{0, 1\}^\ell \to \{0, 1\}^\ell$ una permutazione (la S-box) e sia $\pi_P : \{1, \dots, \ell m\} \to \{1, \dots, \ell m\}$ una permutazione delle posizioni dei bit.
> 
> Sia $\mathcal{P} = \mathcal{C} = \{0, 1\}^{\ell m}$, e sia $\mathcal{K} \subseteq (\{0, 1\}^{\ell m})^{N_r + 1}$ l'insieme di tutte le possibili tuple di $(N_r + 1)$ sottochiavi $(K^1, K^2, \dots, K^{N_r+1})$ generabili dal key schedule a partire dalla chiave $K$.
> 
> Per cifrare un blocco di plaintext $x \in \{0, 1\}^{\ell m}$, si esegue il seguente algoritmo:
> 
>   

- **Notazione delle variabili interne al round $r$ ($1 \le r \le N_r$):**
    
      
    - $w^{r-1} = (w_1^{r-1}, \dots, w_{\ell m}^{r-1})$: stato di $\ell m$ bit in ingresso al round $r$ (con $w^0 = x$).
        
          
        
    - $u^r = w^{r-1} \oplus K^r$: blocco di $\ell m$ bit in **ingresso alle S-box** del round $r$ (dopo lo XOR con la sottochiave $K^r$). Si divide in $m$ sottostringhe da $\ell$ bit: $u^r = (u_{(1)}^r, u_{(2)}^r, \dots, u_{(m)}^r)$.
        
          
        
    - $v^r = (v_{(1)}^r, v_{(2)}^r, \dots, v_{(m)}^r)$: blocco di $\ell m$ bit in **uscita dalle S-box** del round $r$, dove ciascun blocco da $\ell$ bit è calcolato come $v_{(i)}^r = \pi_{S_i^r}(u_{(i)}^r)$ (la $i$-esima S-box del round $r$ è indicata con $S_i^r$).
        
          
        
    - $w^r$: per $1 \le r \le N_r - 1$, si ottiene applicando la permutazione $\pi_P$ ai bit di $v^r$: il bit in posizione $i$ di $v^r$ viene spostato nella posizione $\pi_P(i)$ di $w^r$.
        
          
        
    - **Ultimo round ($r = N_r$):** Dopo aver calcolato $u^{N_r} = w^{N_r - 1} \oplus K^{N_r}$ e $v^{N_r}$ tramite le S-box, **non** si applica $\pi_P$, ma si calcola direttamente il testo cifrato finale tramite l'ultimo XOR:
        
          
        
        $$y = v^{N_r} \oplus K^{N_r + 1}$$
        

### 4.2.2 L'SPN di Riferimento del Libro (Example 4.1)

Tutti gli attacchi di crittoanalisi lineare e differenziale del Capitolo 4 vengono illustrati su una specifica SPN didattica definita nell'**Example 4.1**.

  

> [!example] Example 4.1 (Parametri dell'SPN a 16 bit e 4 Round)
> 
> Consideriamo una SPN con i seguenti parametri:
> 
>   
> 
> - $\ell = 4$ (ciascuna S-box opera su 4 bit, ovvero una cifra esadecimale da `0`=`0000` a `F`=`1111`).
>     
>       
>     
> - $m = 4$ (ci sono 4 S-box affiancate per ogni round, quindi la dimensione del blocco è $\ell m = 16$ bit).
>     
>       
>     
> - $N_r = 4$ (il cifrario ha 4 round e utilizza 5 sottochiavi da 16 bit: $K^1, K^2, K^3, K^4, K^5$).
>     
>       
>     
> - **Key Schedule dell'Esempio:** La chiave principale $K$ è una stringa di 32 bit $(k_1, k_2, \dots, k_{32})$. Le 5 sottochiavi da 16 bit sono definite per scorrimento di 4 bit: $K^r = (k_{4r-3}, k_{4r-2}, \dots, k_{4r+12})$ per $1 \le r \le 5$.
>     
>       
>     
> - **S-box $\pi_S$:** Tutte le 16 S-box ($S_i^r$ per $1 \le i \le 4, 1 \le r \le 4$) usano la stessa identica permutazione esadecimale $\pi_S$:
>     
>       
>     
> 
> |**z**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**A**|**B**|**C**|**D**|**E**|**F**|
> |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
> |**$\pi_S(z)$**|`E`|`4`|`D`|`1`|`2`|`F`|`B`|`8`|`3`|`A`|`6`|`C`|`5`|`9`|`0`|`7`|
> 
> - **Permutazione dei bit $\pi_P$:** Mappa il bit $i$-esimo dell'uscita della S-box $j$-esima nel bit $j$-esimo dell'ingresso della S-box $i$-esima del round successivo:
>     
>       
>     
> 
> |**z**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**13**|**14**|**15**|**16**|
> |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
> |**$\pi_P(z)$**|1|5|9|13|2|6|10|14|3|7|11|15|4|8|12|16|
> 
> _(Osservazione: sia $\pi_P$ che la struttura generale sono simmetriche; per decifrare basta applicare l'inversa $\pi_S^{-1}$ e $\pi_P^{-1} = \pi_P$ con le chiavi in ordine inverso)._
> 
>   

![[Pasted image 20261018181904.png]]

## 4.4 Crittoanalisi Differenziale (Differential Cryptanalysis)

Sviluppata da Eli Biham e Adi Shamir (1990), la **Crittoanalisi Differenziale** è un attacco di tipo **chosen-plaintext** (testo in chiaro scelto) contro i cifrari a blocchi iterati.


### 4.4.1 Idea di Base e Invarianza dello XOR rispetto alla Chiave

Invece di studiare come un singolo input $x$ si trasforma in $y$ (come fa la crittoanalisi lineare), la crittoanalisi differenziale prende **coppie di testi in chiaro** $(x, x^*)$ che presentano una differenza XOR fissa e nota:

  

$$x' = x \oplus x^*$$

e analizza come questa differenza (detta **input XOR** o differenziale di input) si propaga attraverso i vari round del cifrario generando particolari differenze di output (**output XOR**).

  

- **Perché si usano le differenze XOR? (Il "Miracolo" dell'eliminazione delle sottochiavi):**
    
    Consideriamo lo step di Key Mixing in ingresso al round $r$, dove i due stati intermedi $w^{r-1}$ e $(w^{r-1})^*$ vengono sommati modulo 2 con la stessa sottochiave segreta $K^r$, producendo $u^r = w^{r-1} \oplus K^r$ e $(u^r)^* = (w^{r-1})^* \oplus K^r$. Calcoliamo la differenza XOR tra i due ingressi alle S-box:
    
      
    
    $$u'^r = u^r \oplus (u^r)^* = (w^{r-1} \oplus K^r) \oplus ((w^{r-1})^* \oplus K^r) = w^{r-1} \oplus (w^{r-1})^* \oplus (K^r \oplus K^r) = w'^{r-1}$$
    
    **La sottochiave $K^r$ sparisce completamente!** Lo XOR con la sottochiave non altera minimamente la differenza tra i due stati.
    
      
    
- **E la permutazione $\pi_P$?**
    
    Essendo un semplice riordino lineare dei fili, la permutazione $\pi_P$ si limita a spostare di posizione i bit del differenziale in modo completamente deterministico (con probabilità $1$):
    
      
    
    $$w'^r = \pi_P(v'^r)$$
    
- **Dove nasce l'incertezza probabilistica?**
    
    Le **S-box** sono l'unico componente non lineare del cifrario: per una S-box non vale $\pi_S(u \oplus u^*) = \pi_S(u) \oplus \pi_S(u^*)$. Tuttavia, la distribuzione delle differenze di output $v' = \pi_S(u) \oplus \pi_S(u^*)$ a fronte di una data differenza di input $u' = u \oplus u^*$ **non è uniforme**, ma presenta forti picchi statistici sfruttabili dall'attaccante!
    
      
    

### 4.4.2 Differenziali delle S-box, Tabella $N_D$ e Rapporto di Propagazione ($R_p$)

Analizziamo formalmente una singola S-box $\pi_S : \{0, 1\}^\ell \to \{0, 1\}^\ell$ (nel nostro esempio $\ell = 4$, quindi $2^\ell = 16$ possibili input).

  

> [!abstract] Definizione 4.3: Insieme $\Delta(x')$, Valori $N_D(x', y')$ e Rapporto di Propagazione $R_p(x', y')$ Siano $x', y' \in \{0, 1\}^\ell$ due stringhe binarie che rappresentano rispettivamente una differenza (XOR) di input e una differenza (XOR) di output per la S-box $\pi_S$.
> 
>   
> 
> 1. **Insieme delle coppie con differenza $x'$:** Definiamo $\Delta(x')$ come l'insieme di tutte le coppie ordinate $(x, x^*)$ aventi XOR pari a $x'$:
>     
>       
>     
>     $$\Delta(x') = \{(x, x^*) \in \{0, 1\}^\ell \times \{0, 1\}^\ell : x \oplus x^* = x'\} = \{(x, x \oplus x') : x \in \{0, 1\}^\ell\}$$
>     
>     Chiaramente $|\Delta(x')| = 2^\ell$ (perché per ciascuno dei $2^\ell$ valori di $x$, il compagno $x^* = x \oplus x'$ è univocamente determinato).
>     
>       
>     
> 1. **Contatore della Tabella di Distribuzione delle Differenze ($N_D$):** Si definisce $N_D(x', y')$ (i due input si chiamano **differenziali**) come il numero di coppie in $\Delta(x')$ la cui differenza in uscita dalla S-box è esattamente $y'$:
>     
>       
>     
>     $$N_D(x', y') = \left| \left\{ (x, x^*) \in \Delta(x') : \pi_S(x) \oplus \pi_S(x^*) = y' \right\} \right|$$
>     
> 2. **Rapporto di Propagazione (Propagation Ratio $R_p$):** È la probabilità che una coppia scelta casualmente con differenza di input $x'$ produca la differenza di output $y'$:
>     
>       
>     
>     $$R_p(x', y') = \frac{N_D(x', y')}{2^\ell}$$
>     

- **Proprietà matematiche della Difference Distribution Table (DDT):**
    
      
    1. **Prima riga ($x' = 0$):** Se $x' = 0000$, allora $x = x^*$ sempre, quindi $\pi_S(x) \oplus \pi_S(x^*) = 0000$ per tutti i $2^\ell$ input. Pertanto $N_D(0, 0) = 2^\ell$ (cioè $16$ per $\ell=4$) e $N_D(0, y') = 0$ per ogni $y' \neq 0$. (Una S-box con input XOR pari a `0000` si dice **passiva** o inattiva; se $x' \neq 0000$ la S-box si dice **attiva**).
        
          
        
    2. **Prima colonna ($y' = 0$):** Poiché $\pi_S$ è una biiezione (permutazione), due input diversi ($x' \neq 0$) non possono mai dare la stessa uscita ($y' = 0$). Quindi $N_D(x', 0) = 0$ per ogni $x' \neq 0$.
        
          
        
    3. **Tutti i valori sono pari:** Se la coppia $(x, x \oplus x')$ produce $y'$, anche la coppia simmetrica $(x \oplus x', x)$ produce lo stesso $y'$. Quindi ogni contatore $N_D(x', y')$ è sempre un numero pari ($0, 2, 4, 6, \dots, 2^\ell$).
        
          
        
    4. **Somma di riga e di colonna:** La somma dei valori su ogni riga (e su ogni colonna) è esattamente $2^\ell$ ($16$ nel caso $\ell=4$).
        
          
        

> [!example] Example 4.6 (Calcolo di $\Delta(x')$, di una riga di $N_D$ e Tabella Completa per la S-box $\pi_S$ dell'Example 4.1)
> 
> Consideriamo la S-box $\pi_S$ dell'Example 4.1 ($\ell = 4$) e fissiamo il differenziale di input $x' = 1011_2 = \text{B}_{16}$.
> 
>   
> 
> 3. **Calcolo per tutte le 16 coppie $(x, x \oplus \text{B})$:**
>     
>     Per ogni $x \in \{0, \dots, \text{F}\}$, calcoliamo $x^* = x \oplus \text{B}$, cerchiamo $y = \pi_S(x)$ e $y^* = \pi_S(x^*)$ nella tabella della S-box e calcoliamo lo XOR di uscita $y' = y \oplus y^*$:
>     
>       
>     - $x = 0 \implies x^* = \text{B} \implies y = \text{E}, \; y^* = \text{C} \implies y' = \text{E} \oplus \text{C} = \mathbf{2}$
>         
>           
>         
>     - $x = 1 \implies x^* = \text{A} \implies y = 4, \; y^* = 6 \implies y' = 4 \oplus 6 = \mathbf{2}$
>         
>           
>         
>     - $x = 2 \implies x^* = 9 \implies y = \text{D}, \; y^* = \text{A} \implies y' = \text{D} \oplus \text{A} = \mathbf{7}$
>         
>           
>         
>     - $x = 3 \implies x^* = 8 \implies y = 1, \; y^* = 3 \implies y' = 1 \oplus 3 = \mathbf{2}$
>         
>           
>         
>     - $x = 4 \implies x^* = \text{F} \implies y = 2, \; y^* = 7 \implies y' = 2 \oplus 7 = \mathbf{5}$
>         
>           
>         
>     - $x = 5 \implies x^* = \text{E} \implies y = \text{F}, \; y^* = 0 \implies y' = \text{F} \oplus 0 = \mathbf{\text{F}}$
>         
>           
>         
>     - $x = 6 \implies x^* = \text{D} \implies y = \text{B}, \; y^* = 9 \implies y' = \text{B} \oplus 9 = \mathbf{2}$
>         
>           
>         
>     - $x = 7 \implies x^* = \text{C} \implies y = 8, \; y^* = 5 \implies y' = 8 \oplus 5 = \mathbf{\text{D}}$
>         
>         _(Per $x = 8, \dots, \text{F}$ le coppie si ripetono simmetricamente raddoppiando i conteggi)._
>         
>           
>         
> 4. **Conteggio per la riga $x' = \text{B}$:**
>     
>     Il valore $y' = 2$ compare **$8$ volte** ($N_D(\text{B}, 2) = 8$, quindi rapporto di propagazione $R_p(1011, 0010) = 8/16 = \mathbf{1/2}$!), mentre $y' \in \{5, 7, \text{D}, \text{F}\}$ compaiono **$2$ volte ciascuno** ($N_D = 2$), e tutti gli altri $y'$ compaiono $0$ volte.
>     
>       
>     
> 
> **Tabella 4.6 del Libro – Tabella Completa $N_D(x', y')$ per la S-box dell'Example 4.1:**
> 
>   
> 
> |**x′↓ \ y′→**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**A**|**B**|**C**|**D**|**E**|**F**|
> |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
> |**0**|16|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
> |**1**|0|0|0|2|0|0|0|2|0|2|4|0|4|2|0|0|
> |**2**|0|0|0|2|0|6|2|2|0|2|0|0|0|0|2|0|
> |**3**|0|0|2|0|2|0|0|0|0|4|2|0|2|0|0|4|
> |**4**|0|0|0|2|0|0|**6**|0|0|2|0|4|2|0|0|0|
> |**5**|0|4|0|0|0|2|2|0|0|0|4|0|2|0|0|2|
> |**6**|0|0|0|4|0|4|0|0|0|0|0|0|2|2|2|2|
> |**7**|0|0|2|2|2|0|2|0|0|2|2|0|0|0|0|4|
> |**8**|0|0|0|0|0|0|2|2|0|0|0|4|0|4|2|2|
> |**9**|0|2|0|0|2|0|0|4|2|0|2|2|2|0|0|0|
> |**A**|0|2|2|0|0|0|0|0|6|0|0|2|0|0|4|0|
> |**B**|0|0|**8**|0|0|2|0|2|0|0|0|0|0|2|0|2|
> |**C**|0|2|0|0|2|2|2|0|0|0|0|2|0|6|0|0|
> |**D**|0|4|0|0|0|0|0|4|2|0|2|0|2|0|2|0|
> |**E**|0|0|2|4|2|0|0|0|6|0|0|0|0|0|2|0|
> |**F**|0|2|0|0|6|0|0|0|0|4|0|2|0|0|2|0|

### 4.4.3 Tracce Differenziali (Differential Trails) su Più Round

Per estendere l'analisi da una singola S-box all'intero cifrario (es. sui primi $N_r - 1$ round), **concateniamo le differenze di input e output delle S-box attive** (perchè sono le uniche che hanno un'influenza probabilistica) round dopo round in modo che **l'uscita permutata del round $r$**, cioè $w'^r = \pi_P(v'^r)$, **coincida esattamente con l'ingresso $u'^{r+1}$ del round $r+1$**. Questa **sequenza concatenata di differenziali** si chiama **traccia differenziale** (_differential trail_ o _characteristic_).

  

- **Assunzione di Indipendenza e Moltiplicazione dei Rapporti di Propagazione:** Assumendo che le differenze in ingresso alle varie S-box attive lungo la traccia si comportino come eventi statisticamente indipendenti (e fissando le sottochiavi), il **rapporto di propagazione complessivo $R_p$ di una traccia differenziale** su $N_r - 1$ round è dato dal **prodotto** dei rapporti di propagazione delle singole S-box attive coinvolte nella traccia:
    
      
    
    $$R_p = \prod_{\text{S-box attive } S_i^r} R_p(u'^r_{(i)}, v'^r_{(i)})$$
    
    _(Nota: per le S-box passive, dove $0000 \to 0000$, vale $R_p(0, 0) = 16/16 = 1$, quindi non influiscono sul prodotto e per massimizzare $R_p$ l'attaccante cerca tracce con il minor numero possibile di S-box attive!)_.
    
      
    

> [!example] Example 4.7 (Costruzione della Traccia Differenziale a 3 Round con $R_p = 27/1024$)
> 
> Costruiamo una traccia differenziale sui primi **3 round** dell'SPN dell'Example 4.1 che attiva in totale solo **4 S-box**: $S_3^1, S_4^1$ nel Round 1, $S_2^2$ nel Round 2, e $S_3^3$ nel Round 3 (Figura 4.5 del libro).
> 
>   
> 
> 1. **Scelta del Differenziale del Plaintext ($x'$):**
>     
>     Scegliamo coppie di testi in chiaro $(x, x^*)$ aventi differenza iniziale:
>     
>       
>     
>     $$x' = u'^1 = \texttt{0000 1011 0000 0000}_2 = \mathbf{\texttt{0B00}_{16}}$$
>     
>     _(Nota: nel libro viene mostrato come esempio principale sulla Figura 4.5 la traccia che attiva $S_2^1$ al Round 1, $S_3^2$ al Round 2, e $S_2^3, S_3^3$ al Round 3 a partire da $x' = \texttt{0B00}_{16}$. Vediamo tutti i passaggi esatti bit per bit di questa traccia del libro!)_
>     
>       
>     
> 2. **Round 1 (1 S-box attiva: $S_2^1$):**
>     
>       
>     - Input al Round 1: $u'^1 = \texttt{0000 1011 0000 0000}$. Solo $S_2^1$ è attiva con input $u'^1_{(2)} = \texttt{1011}_2 = \text{B}_{16}$.
>         
>           
>         
>     - Dalla Tabella 4.6 scegliamo la transizione più probabile per $S_2^1$:
>         
>           
>         
>         $$\text{B} \; (\texttt{1011}) \longrightarrow 2 \; (\texttt{0010}) \qquad \text{con } R_p = \frac{8}{16} = \mathbf{\frac{1}{2}}$$
>         
>     - L'uscita dalle S-box del Round 1 è quindi $v'^1 = \texttt{0000 0010 0000 0000}$ (solo il bit 7 è uguale a `1`).
>         
>           
>         
>     - Applichiamo la permutazione $\pi_P$: poiché $\pi_P(7) = 10$, il bit `1` in posizione 7 finisce in posizione **10**, che è il 2° bit della S-box $S_3^2$! Quindi:
>         
>           
>         
>         $$w'^1 = u'^2 = \texttt{0000 0000 0100 0000}_2 = \mathbf{\texttt{0040}_{16}}$$
>         
> 3. **Round 2 (1 S-box attiva: $S_3^2$):**
>     
>       
>     - Nel Round 2 si attiva **solo** $S_3^2$ con input $u'^2_{(3)} = \texttt{0100}_2 = 4_{16}$.
>         
>           
>         
>     - Dalla Tabella 4.6 scegliamo la transizione più probabile per l'input $4$:
>         
>           
>         
>         $$4 \; (\texttt{0100}) \longrightarrow 6 \; (\texttt{0110}) \qquad \text{con } R_p = \frac{6}{16} = \mathbf{\frac{3}{8}}$$
>         
>     - L'uscita dalle S-box del Round 2 è $v'^2 = \texttt{0000 0000 0110 0000}$ (bit attivi nelle posizioni **10** e **11**).
>         
>           
>         
>     - Applichiamo la permutazione $\pi_P$: abbiamo $\pi_P(10) = 6$ (2° bit di $S_2^3$) e $\pi_P(11) = 11$ (3° bit di $S_3^3$). Pertanto l'ingresso al Round 3 è:
>         
>           
>         
>         $$w'^2 = u'^3 = \texttt{0000 0100 0010 0000}_2 = \mathbf{\texttt{0420}_{16}}$$
>         
> 4. **Round 3 (2 S-box attive: $S_2^3$ e $S_3^3$):**
>     
>       
>     - In $S_2^3$ entra $u'^3_{(2)} = \texttt{0100}_2 = 4_{16}$. Dalla Tabella 4.6 scegliamo $4 \; (\texttt{0100}) \longrightarrow 6 \; (\texttt{0110})$ con $R_p = \frac{6}{16} = \mathbf{\frac{3}{8}}$.
>         
>           
>         
>     - In $S_3^3$ entra $u'^3_{(3)} = \texttt{0010}_2 = 2_{16}$. Dalla Tabella 4.6 scegliamo la transizione più probabile per l'input $2$:
>         
>           
>         
>         $$2 \; (\texttt{0010}) \longrightarrow 5 \; (\texttt{0101}) \qquad \text{con } R_p = \frac{6}{16} = \mathbf{\frac{3}{8}}$$
>         
>     - L'uscita dalle S-box del Round 3 è quindi:
>         
>           
>         
>         $$v'^3 = \texttt{0000 0110 0101 0000}_2 = \mathbf{\texttt{0650}_{16}}$$
>         
>         (I bit attivi sono nelle posizioni **6, 7, 10, 12**).
>         
>           
>         
>     - Applichiamo la permutazione $\pi_P$ del Round 3:
>         
>           
>         - $\pi_P(6) = 6$ (cade in $S_2^4$)
>             
>               
>             
>         - $\pi_P(7) = 10$ (cade in $S_3^4$)
>             
>               
>             
>         - $\pi_P(10) = 7$ (cade in $S_2^4$)
>             
>               
>             
>         - $\pi_P(12) = 15$ (cade in $S_4^4$)
>             
>             _(Anzi, controllando la tabella di $\pi_P$ dell'Example 4.1: $\pi_P(6)=6, \pi_P(7)=10, \pi_P(10)=7, \pi_P(12)=15$, ma attenendoci esattamente alla tabella di $\pi_P$: i bit in posizione 6, 7, 10, 12 sono le uscite e vanno nelle posizioni $\pi_P(6)=6, \pi_P(7)=10, \pi_P(10)=7, \pi_P(12)=15$; se invece leggiamo $\pi_P$ per colonne/righe come fa il libro dove $\pi_P(6)=6, \pi_P(7)=10, \pi_P(10)=7$, in particolare con la convenzione del libro i bit 6 e 10 finiscono in **6 e 7** cioè dentro $S_2^4$, e i bit 7 e 12 finiscono in **14 e 15** cioè dentro $S_4^4$!)_
>             
>               
>             
>     - Quindi il differenziale in ingresso all'ultimo round (Round 4) è:
>         
>           
>         
>         $$w'^3 = u'^4 = \texttt{0000 0110 0000 0110}_2 = \mathbf{\texttt{0606}_{16}}$$
>         
> 5. **Rapporto di Propagazione Totale della Traccia a 3 Round:**
>     
>     Moltiplicando le probabilità delle 4 S-box attive ($S_2^1, S_3^2, S_2^3, S_3^3$):
>     
>       
>     
>     $$R_p = \frac{1}{2} \times \frac{3}{8} \times \frac{3}{8} \times \frac{3}{8} = \mathbf{\frac{27}{1024}} \approx 0.02637$$
>     

### 4.4.4 L'Attacco Differenziale sull'Ultimo Round (Algorithm 4.3 & Example 4.8)

Come fa Oscar a sfruttare la traccia differenziale appena trovata ($x' = \texttt{0B00}_{16} \longrightarrow u'^4 = \texttt{0606}_{16}$ con probabilità $\epsilon = 27/1024$) per trovare i bit della sottochiave dell'ultimo round $K^5$?

  

- **Osservazione chiave sull'Ultimo Round (Round 4):** Quando una coppia $(x, x^*)$ segue correttamente la nostra traccia differenziale fino all'ingresso del Round 4 (una coppia del genere è chiamata **right pair**, _coppia giusta_), il differenziale in ingresso alle S-box del Round 4 è:
    
      
    
    $$u'^4 = (\texttt{0000}, \texttt{0110}, \texttt{0000}, \texttt{0110})$$
    
    Notiamo due cose fondamentali:
    
      
    1. Le S-box **$S_1^4$** e **$S_3^4$** hanno differenziale di ingresso pari a **`0000`** (sono **passive**!). Poiché dopo le S-box del Round 4 c'è solo lo XOR con $K^5$ (senza permutazione $\pi_P$), in una _right pair_ anche il differenziale del testo cifrato finale $y' = y \oplus y^* = v'^4$ **deve avere obbligatoriamente `0000` nel 1° e nel 3° blocco da 4 bit** ($y'_{(1)} = \texttt{0000}$ e $y'_{(3)} = \texttt{0000}$) (questa è un'oss. che abbiamo fatto quando abbiamo spiegato lo xor come primo passaggio per la crittazione).
        
          
        - _Vantaggio enorme (**Fase di Filtraggio**):_ Se Oscar vede una coppia di testi cifrati $(y, y^*)$ in cui $y'_{(1)} \neq \texttt{0000}$ oppure $y'_{(3)} \neq \texttt{0000}$, sa con certezza matematica che quella coppia **non** è una _right pair_ e la **scarta immediatamente** senza nemmeno fare calcoli!
            
              
            
    2. Le S-box attive nell'ultimo round sono solo due: **$S_2^4$** (con differenziale atteso $u'^4_{(2)} = \texttt{0110}$) e **$S_4^4$** (con differenziale atteso $u'^4_{(4)} = \texttt{0110}$).
        
          
        - Queste due S-box dipendono unicamente dagli **8 bit** della sottochiave finale $K^5$ che si trovano nei blocchi 2 e 4, indicati nel libro come **target partial subkey** $(K^5_{(2)}, K^5_{(4)})$.
            
              
            

#### Procedura di Decifratura Parziale e Conteggio

- Oscar genera $T$ coppie di testi in chiaro $(x, x^*)$ con $x \oplus x^* = \texttt{0B00}_{16}$ e ottiene i rispettivi testi cifrati $(y, y^*)$.
    
      
    
- Inizializza $2^8 = 256$ contatori $\text{Count}(L_1, L_2) = 0$ per tutte le $256$ possibili coppie di sottochiavi candidate a 4 bit $(L_1, L_2) \in \{0, 1\}^4 \times \{0, 1\}^4$ che ipotizzano i valori veri di $(K^5_{(2)}, K^5_{(4)})$.
    
      
    
- Per ogni coppia $(y, y^*)$ che **supera il filtraggio** ($y'_{(1)} = y'_{(3)} = \texttt{0000}$) e per ciascuna delle 256 chiavi candidate $(L_1, L_2)$, Oscar decifra parzialmente all'indietro attraverso l'ultimo round calcolando:
    
      
    
    $$v^4_{(2)} = y_{(2)} \oplus L_1, \qquad (v^4_{(2)})^* = y^*_{(2)} \oplus L_1$$
    
    $$u^4_{(2)} = \pi_S^{-1}(v^4_{(2)}), \qquad (u^4_{(2)})^* = \pi_S^{-1}((v^4_{(2)})^*), \qquad u'^4_{(2)} = u^4_{(2)} \oplus (u^4_{(2)})^*$$
    
    e analogamente per il 4° blocco usando $L_2$:
    
      
    
    $$v^4_{(4)} = y_{(4)} \oplus L_2, \qquad (v^4_{(4)})^* = y^*_{(4)} \oplus L_2$$
    
    $$u^4_{(4)} = \pi_S^{-1}(v^4_{(4)}), \qquad (u^4_{(4)})^* = \pi_S^{-1}((v^4_{(4)})^*), \qquad u'^4_{(4)} = u^4_{(4)} \oplus (u^4_{(4)})^*$$
    
- **Condizione di incremento del contatore:** Se per la chiave candidata $(L_1, L_2)$ risultano contemporaneamente verificati entrambi i differenziali attesi dalla traccia:
    
      
    
    $$u'^4_{(2)} = \texttt{0110} \quad \text{e} \quad u'^4_{(4)} = \texttt{0110}$$
    
    allora Oscar incrementa di 1 il contatore: $\text{Count}(L_1, L_2) \leftarrow \text{Count}(L_1, L_2) + 1$.
    
      
    

> [!abstract] Algorithm 4.3: DIFFERENTIAL ATTACK($\mathcal{T}, \pi_S, x', u'^4_{(2)}, u'^4_{(4)}$) **Input:** Un insieme $\mathcal{T}$ di $T$ coppie di plaintext-ciphertext $(x, y, x^*, y^*)$ tali che $x \oplus x^* = x' = \texttt{0B00}_{16}$; la S-box $\pi_S$; i differenziali target $u'^4_{(2)} = \texttt{0110}$ e $u'^4_{(4)} = \texttt{0110}$. **Output:** La sottochiave parziale a 8 bit $(K^5_{(2)}, K^5_{(4)})$.
> 
>   
> 
> 1. **for** $(L_1, L_2) \leftarrow (0, 0)$ **to** $(\text{F}, \text{F})$ **do**
>     
>     $\quad \text{Count}(L_1, L_2) \leftarrow 0$
>     
>       
>     
> 2. **for each** $(x, y, x^*, y^*) \in \mathcal{T}$ **do**
>     
>     $\quad$ **if** $(y_{(1)} = y^*_{(1)})$ **and** $(y_{(3)} = y^*_{(3)})$ **then** _(Fase di Filtraggio)_
>     
>       
>     
>       
>     
>     $\quad \quad$ **for** $(L_1, L_2) \leftarrow (0, 0)$ **to** $(\text{F}, \text{F})$ **do**
>     
>     $\quad \quad \quad v^4_{(2)} \leftarrow L_1 \oplus y_{(2)}$
>     
>     $\quad \quad \quad (v^4_{(2)})^* \leftarrow L_1 \oplus y^*_{(2)}$
>     
>     $\quad \quad \quad u^4_{(2)} \leftarrow \pi_S^{-1}(v^4_{(2)})$
>     
>     $\quad \quad \quad (u^4_{(2)})^* \leftarrow \pi_S^{-1}((v^4_{(2)})^*)$
>     
>     $\quad \quad \quad u'^4_{(2)} \leftarrow u^4_{(2)} \oplus (u^4_{(2)})^*$
>     
>     $\quad \quad \quad v^4_{(4)} \leftarrow L_2 \oplus y_{(4)}$
>     
>     $\quad \quad \quad (v^4_{(4)})^* \leftarrow L_2 \oplus y^*_{(4)}$
>     
>     $\quad \quad \quad u^4_{(4)} \leftarrow \pi_S^{-1}(v^4_{(4)})$
>     
>     $\quad \quad \quad (u^4_{(4)})^* \leftarrow \pi_S^{-1}((v^4_{(4)})^*)$
>     
>     $\quad \quad \quad u'^4_{(4)} \leftarrow u^4_{(4)} \oplus (u^4_{(4)})^*$
>     
>     $\quad \quad \quad$ **if** $(u'^4_{(2)} = \texttt{0110})$ **and** $(u'^4_{(4)} = \texttt{0110})$ **then**
>     
>     $\quad \quad \quad \quad \text{Count}(L_1, L_2) \leftarrow \text{Count}(L_1, L_2) + 1$
>     
>       
>     
> 3. $\text{max} \leftarrow -1$
>     
>       
>     
> 4. **for** $(L_1, L_2) \leftarrow (0, 0)$ **to** $(\text{F}, \text{F})$ **do**
>     
>     $\quad$ **if** $\text{Count}(L_1, L_2) > \text{max}$ **then**
>     
>     $\quad \quad \text{max} \leftarrow \text{Count}(L_1, L_2)$
>     
>     $\quad \quad \text{maxkey} \leftarrow (L_1, L_2)$
>     
>       
>     
> 5. **output** ($\text{maxkey}$)
>     
>       
>     

### 4.4.5 Perché l'Algoritmo Funziona e Quante Coppie Servono? (Example 4.8)

- **Perché la chiave vera $(K^5_{(2)}, K^5_{(4)})$ vince il conteggio?**
    
      
    - Quando l'algoritmo processa una **right pair** (cosa che accade con frequenza attesa $T \times R_p = \frac{27}{1024} T$) e testa la **chiave vera** $(L_1, L_2) = (K^5_{(2)}, K^5_{(4)})$, la decifratura parziale ricostruisce i veri stati intermedi del cifrario, i quali per definizione di _right pair_ hanno **sempre** differenziale $(\texttt{0110}, \texttt{0110})$ (oltre a superare sempre il filtraggio $y'_{(1)} = y'_{(3)} = \texttt{0000}$)! Pertanto, il contatore della chiave vera viene incrementato per tutte le _right pairs_, raggiungendo un valore atteso di **almeno $\frac{27}{1024} T \approx 0.0264 \, T$**.
        
          
        
    - Per una **chiave errata** $(L_1, L_2) \neq (K^5_{(2)}, K^5_{(4)})$ (o per le _wrong pairs_ sopravvissute per caso al filtraggio), i valori decifrati si comportano in modo pressoché uniforme e casuale, incrementando i contatori molto raramente (rumore di fondo bassissimo). Di conseguenza, il contatore $\text{Count}(L_1, L_2)$ con il valore **massimo assoluto** individua la vera sottochiave parziale.
        
          
        
- **Complessità Dati (Quante coppie $T$ servono?):**
    
    In generale, se una traccia differenziale su $N_r - 1$ round ha rapporto di propagazione $\epsilon = R_p$, il numero di coppie _chosen-plaintext_ necessarie per distinguere nettamente il picco della chiave vera dal rumore è:
    
      
    
    $$T \approx c \cdot \epsilon^{-1}$$
    
    dove $c$ è una piccola costante positiva.
    
      
    

> [!example] Example 4.8 (Risultati Sperimentali dell'Attacco Differenziale del Libro)
> 
> Applichiamo l'Algorithm 4.3 all'SPN dell'Example 4.1 usando la traccia dell'Example 4.7, dove $\epsilon = R_p = \frac{27}{1024} \approx 0.0264$ (quindi $\epsilon^{-1} = \frac{1024}{27} \approx 37.9$):
> 
>   
> 
> - Scegliendo ad esempio **$T = 5000$ coppie** di testi in chiaro (un multiplo abbondante di $38$), il valore atteso del contatore per la vera sottochiave $(K^5_{(2)}, K^5_{(4)}) = (\texttt{0110}, \texttt{1111}) = (6, \text{F})$ è:
>     
>       
>     
>     $$5000 \times \frac{27}{1024} \approx \mathbf{132}$$
>     
> - **Effetto del Filtraggio nella simulazione:** Su $5000$ coppie generate, grazie al controllo iniziale `if (y_(1) = y*_(1)) and (y_(3) = y*_(3))`, quasi tutte le _wrong pairs_ vengono scartate all'istante: rimangono tipicamente solo circa **150–200 coppie** su cui eseguire il ciclo interno delle 256 chiavi, rendendo l'attacco istantaneo!
>     
>       
>     
> - Al termine dell'esecuzione, il contatore massimo assoluto cade esattamente su $\text{maxkey} = (\texttt{0110}, \texttt{1111})$, svelando gli 8 bit di $K^5$ (gli altri 8 bit di $K^5$, cioè $K^5_{(1)}$ e $K^5_{(3)}$, possono poi essere trovati con un secondo attacco differenziale su un'altra traccia o per semplice ricerca esaustiva su $2^8 = 256$ possibilità).

### 4.4.6 Sunto Operativo della Crittoanalisi Differenziale: Fase Preliminare vs Fase di Attacco

Per comprendere appieno distinguiamo i **due momenti separati** in cui si articola la crittoanalisi differenziale su una SPN (fissando, come nel nostro caso di studio, $N_r = 4$ round):

#### 1. Fase Preliminare (Studio Offline della Traccia sui primi $N_r - 1 = 3$ Round)

Questa fase viene svolta a tavolino dal crittanalista **una sola volta prima dell'attacco**, senza bisogno di conoscere la chiave segreta (poiché nello XOR tra le coppie di stati intermedi le sottochiavi si annullano sempre: $K^r \oplus K^r = 0$). Consiste nell'effettuare tutti i calcoli di propagazione degli XOR attraverso i primi 3 round per ricavare **tre parametri fondamentali**:

  

1. **Scelta del differenziale iniziale ($x'$):** Si analizza la tabella di distribuzione delle differenze $N_D(a', b')$ e si individua la riga (escludendo la riga `0` banale che vale $16$) che contiene il **contatore più alto** (l'occorrenza massima nella tabella, es. $N_D(\text{B}, 2) = 8$ nell'esempio del libro), scegliendo al contempo una colonna di uscita con il minor numero possibile di bit uguali a `1` (es. `2` = `0010`). Si fissa così il differenziale del plaintext $x' = u'^1$ attivando una sola S-box nel Round 1 (es. $x' = \texttt{0B00}_{16}$).
    
      
    
2. **Determinazione dello stato finale della traccia ($w'^3 = u'^4$) e delle S-box attive nell'ultimo round:** Seguendo deterministicamente lo spostamento dei bit `1` attraverso la permutazione $\pi_P$ e scegliendo ad ogni round le uscite più probabili dalla tabella $N_D$ per le sole S-box attive, si calcolano gli stati differenziali intermedi dal Round 1 fino all'uscita del Round 3 ($w'^3$), che coincide esattamente con **l'ingresso alle S-box dell'ultimo round ($u'^4$)**.
    
      
    - Da $u'^4$ (es. $u'^4 = \texttt{0606}_{16} = \texttt{0000 0110 0000 0110}_2$) si vedono immediatamente quali sono le **S-box passive** (dove entra `0000`, utili per filtrare e scartare subito le coppie errate) e quali sono le **S-box attive dell'ultimo round** (dove entra una differenza non nulla, es. $S_2^4$ e $S_4^4$ con ingresso atteso `0110`).
        
          
        
    - È essenziale che il numero di S-box attive nell'ultimo round sia **piccolo** (es. solo 2 S-box su 4), così da dover indovinare solo i corrispondenti blocchetti della sottochiave finale $K^5$.
        
          
        
3. **Calcolo della probabilità della traccia ($R_p$) e del numero di coppie ($T$):** Moltiplicando i rapporti di propagazione $R_p = N_D / 16$ delle sole S-box attive attraversate nei primi 3 round, si ottiene la **probabilità complessiva della traccia** (es. $R_p = \frac{27}{1024} \approx 0.0264$). Questo valore ci dice esattamente **quante coppie di testi in chiaro $T$ dobbiamo generare casualmente** ($T \approx c / R_p$, es. $T = 5000$) affinché la traccia si verifichi un numero di volte sufficiente a staccare il rumore statistico.
    
      
#### 2. Fase Finale (Algoritmo di Attacco e Decifratura Parziale sull'Ultimo Round)

Una volta fissati $x'$, il differenziale atteso $u'^4$ e il numero di coppie $T$, non serve più ricalcolare gli stati dei primi tre round: entra in gioco l'**algoritmo di attacco vero e proprio** (il codice):

  

1. **Raccolta dati e Filtraggio:** Si generano casualmente $T$ testi in chiaro $x$, si calcolano i compagni $x^* = x \oplus x'$, si ottengono i rispettivi testi cifrati $(y, y^*)$ e si scartano subito tutte le coppie che non hanno differenza `0000` in corrispondenza delle S-box passive dell'ultimo round.
    
      
    
2. **I $2^8 = 256$ tentativi di Decifratura Parziale Inversa:** Poiché le S-box attive nell'ultimo round sono solo **due** (ciascuna da 4 bit), invece di fare forza bruta sui $2^{16} = 65.536$ valori dell'intera sottochiave $K^5$, l'algoritmo testa solo le **$2^8 = 256$ combinazioni possibili** per i due nibble di chiave $(L_1, L_2)$ collegati alle due S-box attive:
    
      
    - Per ogni coppia $(y, y^*)$ superstite e per ciascuna delle 256 ipotesi $(L_1, L_2)$, esegue una **decifratura parziale inversa** dell'ultimo round: fa lo **XOR** tra i blocchetti del testo cifrato e $(L_1, L_2)$ per rimuovere l'ultimo Key Mixing ($v^4 = y \oplus L$) e applica la **S-box inversa $\pi_S^{-1}$** per risalire a $u^4$ e $(u^4)^*$.
        
          
        
    - Calcola lo XOR $u'^4 = u^4 \oplus (u^4)^*$ e verifica se coincide con il valore atteso dalla fase preliminare (es. `0110` su entrambe le S-box attive): in caso affermativo, incrementa il contatore $\text{Count}[L_1, L_2]$.
        
          
        
3. **Individuazione dei bit veri della sottochiave:** Al termine del ciclo, la combinazione $(L_1, L_2)$ che ha accumulato il **conteggio massimo assoluto** (`maxkey`) corrisponde con altissima probabilità ai veri 8 bit della sottochiave finale $K^5$.

## 4.6 The Advanced Encryption Standard (AES)

Con l'obsolescenza del DES (dovuta alla chiave di soli 56 bit vulnerabile alla ricerca esaustiva), nel 1997 il NIST ha indetto un concorso pubblico internazionale per selezionare il nuovo standard crittografico (**AES**). Nel 2000 è stato scelto l'algoritmo **Rijndael**, progettato dai crittografi belgi **Joan Daemen e Vincent Rijmen**, diventato standard ufficiale nel 2001.

  

### 4.6.1 Parametri Fondamentali e Architettura Generale

**AES è un cifrario iterato con struttura SPN (Substitution-Permutation Network)**, in cui tutte le operazioni algebriche sono definite sui byte visti come elementi del campo finito di Galois **$\mathbb{F}_{2^8}$** ($GF(2^8)$).

  

- **Dimensione fissa del blocco:** $\mathbf{128 \text{ bit}}$ ($16$ byte).
    
      
    
- **Lunghezza della chiave ($K$) e Numero di Round ($N_r$):** AES supporta tre lunghezze di chiave, da cui dipende il numero di round $N_r$:
    
      
    

| **Versione** | **Lunghezza Chiave (bit / byte / word da 32 bit)** | **Dimensione Blocco** | **Numero di Round (Nr​)** | **Numero di Sottochiavi da 128 bit (Nr​+1)** |
| ------------ | -------------------------------------------------- | --------------------- | ------------------------- | -------------------------------------------- |
| **AES-128**  | $128$ bit ($16$ byte / $N_k = 4$ word)             | $128$ bit             | **$10$**                  | $11$ ($K^0, K^1, \dots, K^{10}$)             |
| **AES-192**  | $192$ bit ($24$ byte / $N_k = 6$ word)             | $128$ bit             | **$12$**                  | $13$ ($K^0, K^1, \dots, K^{12}$)             |
| **AES-256**  | $256$ bit ($32$ byte / $N_k = 8$ word)             | $128$ bit             | **$14$**                  | $15$ ($K^0, K^1, \dots, K^{14}$)             |

- **La Matrice di Stato (`State`):**
    
    Durante tutta la cifratura e decifratura, il blocco corrente di 128 bit ($16$ byte: $in_0, in_1, \dots, in_{15}$) viene rappresentato come una **matrice quadrata $4 \times 4$ di byte** chiamata **`State`**, riempita **colonna per colonna** (_column-major order_):
    
      
    
    $$\text{State} = \begin{pmatrix} s_{0,0} & s_{0,1} & s_{0,2} & s_{0,3} \\ s_{1,0} & s_{1,1} & s_{1,2} & s_{1,3} \\ s_{2,0} & s_{2,1} & s_{2,2} & s_{2,3} \\ s_{3,0} & s_{3,1} & s_{3,2} & s_{3,3} \end{pmatrix} = \begin{pmatrix} in_0 & in_4 & in_8 & in_{12} \\ in_1 & in_5 & in_9 & in_{13} \\ in_2 & in_6 & in_{10} & in_{14} \\ in_3 & in_7 & in_{11} & in_{15} \end{pmatrix}$$
    
    _(Ciascuna delle 4 colonne della matrice `State` contiene 4 byte, ovvero una **word** da 32 bit)._
    
      
    

### 4.6.2 La Matematica di AES: Il Campo Finito $\mathbb{F}_{2^8}$

Ogni singolo byte $b = (b_7 b_6 b_5 b_4 b_3 b_2 b_1 b_0)_2$ (scritto in esadecimale con due cifre, es. $\texttt{57}_{16} = \texttt{01010111}_2$) viene identificato con un polinomio di grado $\le 7$ in $\mathbb{Z}_2[x]$:

  

$$b_7 x^7 + b_6 x^6 + b_5 x^5 + b_4 x^4 + b_3 x^3 + b_2 x^2 + b_1 x + b_0$$

_(Ad esempio, il byte $\texttt{57}_{16} = \texttt{01010111}_2$ corrisponde al polinomio $x^6 + x^4 + x^2 + x + 1$)._

  

Il campo finito $\mathbb{F}_{2^8}$ di $256$ elementi utilizzato da AES è costruito come l'anello quoziente **$\mathbb{Z}_2[x]/(m(x))$**, dove il polinomio irriducibile di grado 8 scelto dallo standard è:

  

$$m(x) = x^8 + x^4 + x^3 + x + 1 \qquad (\text{in binario: } \texttt{100011011}_2, \text{ ovvero } x^8 \equiv x^4 + x^3 + x + 1 = \texttt{1B}_{16})$$

- **Addizione in $\mathbb{F}_{2^8}$:** Sommare due polinomi in $\mathbb{Z}_2[x]$ equivale a fare lo **XOR bit a bit** ($\oplus$) dei due byte (es. $\texttt{57} \oplus \texttt{83} = \texttt{D4}$).
    
      
    
- **Moltiplicazione in $\mathbb{F}_{2^8}$ (e l'operazione base `xtime`):**
    
    Moltiplicare due byte equivale a moltiplicare i rispettivi polinomi e ridurre il risultato **modulo $m(x)$**.
    
      
    - **Regola pratica (`xtime` - moltiplicazione per $x$, ovvero per $\texttt{02}_{16}$):**
        
        Dato un byte $b = (b_7 b_6 b_5 b_4 b_3 b_2 b_1 b_0)$, moltiplicarlo per $x$ dà $b_7 x^8 + b_6 x^7 + \dots + b_0 x$.
        
          
        1. Se il bit più significativo è **$b_7 = 0$**, il grado non raggiunge 8: basta fare uno **shift a sinistra di 1 bit** inserendo `0` a destra: $(b_6 b_5 b_4 b_3 b_2 b_1 b_0 0)_2$.
            
              
            
        2. Se il bit più significativo è **$b_7 = 1$**, compare il termine $x^8$, che modulo $m(x)$ va sostituito con $x^4 + x^3 + x + 1$ ($\texttt{00011011}_2 = \texttt{1B}_{16}$). Quindi si fa uno **shift a sinistra di 1 bit seguito dallo XOR con $\texttt{1B}_{16}$**:
            
              
            
            $$x \cdot b \pmod{m(x)} = \begin{cases} (b \ll 1) & \text{se } b_7 = 0 \\ (b \ll 1) \oplus \texttt{1B}_{16} & \text{se } b_7 = 1 \end{cases}$$
            

> [!example] Esempio di Moltiplicazione in $\mathbb{F}_{2^8}$ (dal Libro)
> 
> Calcoliamo il prodotto $\texttt{57}_{16} \bullet \texttt{13}_{16}$ in $\mathbb{F}_{2^8}$, dove $\texttt{57}_{16} = \texttt{01010111}_2$ e $\texttt{13}_{16} = \texttt{00010011}_2 = \texttt{01}_{16} \oplus \texttt{02}_{16} \oplus \texttt{10}_{16}$ (cioè $x^4 + x + 1$):
> 
>   
> 
> 1. Applichiamo ripetutamente la moltiplicazione per $\texttt{02}_{16}$ ($x$) a $\texttt{57}_{16}$:
>     
>       
>     - $\texttt{57} \bullet \texttt{02}$: poiché $b_7 = 0$ in $\texttt{01010111}$, shiftiamo a sinistra $\to \texttt{10101110}_2 = \mathbf{\texttt{AE}_{16}}$.
>         
>           
>         
>     - $\texttt{57} \bullet \texttt{04} = \texttt{AE} \bullet \texttt{02}$: poiché $b_7 = 1$ in $\texttt{10101110}$, shiftiamo a sinistra ($\texttt{01011100}$) e facciamo XOR con $\texttt{00011011}$ ($\texttt{1B}$) $\to \texttt{01000111}_2 = \mathbf{\texttt{47}_{16}}$.
>         
>           
>         
>     - $\texttt{57} \bullet \texttt{08} = \texttt{47} \bullet \texttt{02}$: poiché $b_7 = 0$ in $\texttt{01000111}$, shiftiamo a sinistra $\to \texttt{10001110}_2 = \mathbf{\texttt{8E}_{16}}$.
>         
>           
>         
>     - $\texttt{57} \bullet \texttt{10} = \texttt{8E} \bullet \texttt{02}$: poiché $b_7 = 1$ in $\texttt{10001110}$, shiftiamo a sinistra ($\texttt{00011100}$) e facciamo XOR con $\texttt{00011011}$ ($\texttt{1B}$) $\to \texttt{00000111}_2 = \mathbf{\texttt{07}_{16}}$.
>         
>           
>         
> 2. Sommiamo (XOR) i contributi per $\texttt{13}_{16} = \texttt{01} \oplus \texttt{02} \oplus \texttt{10}$:
>     
>       
>     
>     $$\texttt{57} \bullet \texttt{13} = (\texttt{57} \bullet \texttt{01}) \oplus (\texttt{57} \bullet \texttt{02}) \oplus (\texttt{57} \bullet \texttt{10}) = \texttt{57} \oplus \texttt{AE} \oplus \texttt{07} = \mathbf{\texttt{FE}_{16}}$$
>     

### 4.6.3 Struttura Globale e Le 4 Operazioni di Round di AES

L'algoritmo di cifratura AES procede come segue:

  

1. **Whitening Iniziale:** `AddRoundKey(State, K^0)` (XOR dello stato iniziale con la prima sottochiave $K^0$).
    
      
    
2. **Primi $N_r - 1$ Round ($r = 1, \dots, N_r - 1$):** Ogni round esegue in sequenza **4 operazioni**:
    
      
    - `SubBytes(State)` _(Sostituzione byte per byte tramite S-box)_
        
          
        
    - `ShiftRows(State)` _(Permutazione per scorrimento delle righe)_
        
          
        
    - `MixColumns(State)` _(Trasformazione lineare su $\mathbb{F}_{2^8}$ delle colonne per la diffusione)_
        
          
        
    - `AddRoundKey(State, K^r)` _(Key Mixing tramite XOR con la sottochiave $K^r$)_
        
          
        
3. **Ultimo Round ($r = N_r$):** Esegue solo **3 operazioni** (viene omesso `MixColumns`, esattamente come nell'SPN generale si omette l'ultima permutazione $\pi_P$):
    
      
    - `SubBytes(State)`
        
          
        
    - `ShiftRows(State)`
        
          
        
    - `AddRoundKey(State, K^{N_r})`
        
          
        

Analizziamo in dettaglio le quattro trasformazioni interne:

  

#### 1. `SubBytes` (La S-box di AES)

Applica la stessa identica **S-box $8 \times 8$** ($\pi_S : \{0, 1\}^8 \to \{0, 1\}^8$) a ciascuno dei 16 byte $s_{i,j}$ della matrice `State` in modo indipendente.

 La S-box di AES è definita matematicamente in **due passi** per massimizzare la resistenza alla crittoanalisi lineare e differenziale:

  

1. **Inversione nel campo finito $\mathbb{F}_{2^8}$ (Non-linearità):**
    
    Dato il byte di input $a \in \mathbb{F}_{2^8}$, si calcola:
    
      
    
    $$b = \begin{cases} 0 & \text{se } a = 0 \\ a^{-1} \bmod m(x) & \text{se } a \neq 0 \end{cases}$$
    
    dove $a^{-1}$ è l'inverso moltiplicativo nel campo $\mathbb{Z}_2[x]/(x^8 + x^4 + x^3 + x + 1)$.
    
      
    
2. **Trasformazione Affine su $\mathbb{Z}_2$ (per distruggere la struttura algebrica semplice di $a^{-1}$):**
    
    Considerato il byte $b = (b_7, \dots, b_0)^T \in (\mathbb{Z}_2)^8$ appena ottenuto, si calcola il byte finale $c = (c_7, \dots, c_0)^T$ applicando per ogni bit $0 \le i \le 7$:
    
      
    
    $$c_i = (b_i + b_{(i+4)\bmod 8} + b_{(i+5)\bmod 8} + b_{(i+6)\bmod 8} + b_{(i+7)\bmod 8} + d_i) \bmod 2$$
    
    dove $d = (d_7 \dots d_0)_2 = \texttt{01100011}_2 = \mathbf{\texttt{63}_{16}}$. In forma matriciale su $\mathbb{Z}_2$:
    
      
    
    $$\begin{pmatrix} c_0 \\ c_1 \\ c_2 \\ c_3 \\ c_4 \\ c_5 \\ c_6 \\ c_7 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 & 1 & 1 & 1 & 1 \\ 1 & 1 & 0 & 0 & 0 & 1 & 1 & 1 \\ 1 & 1 & 1 & 0 & 0 & 0 & 1 & 1 \\ 1 & 1 & 1 & 1 & 0 & 0 & 0 & 1 \\ 1 & 1 & 1 & 1 & 1 & 0 & 0 & 0 \\ 0 & 1 & 1 & 1 & 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 & 1 & 1 & 1 & 0 \\ 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} b_0 \\ b_1 \\ b_2 \\ b_3 \\ b_4 \\ b_5 \\ b_6 \\ b_7 \end{pmatrix} \oplus \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \\ 0 \\ 1 \\ 1 \\ 0 \end{pmatrix}$$
    
    _(Nota: se l'input è $a = \texttt{00}_{16}$, l'inverso è $b = \texttt{00}_{16}$ e l'uscita della S-box è $\pi_S(\texttt{00}) = \texttt{63}_{16}$)._
    
      
    

> [!example] Example 4.9 (Calcolo di `FieldInv` e `SubBytes` per il byte $\texttt{53}_{16}$)
> 
> Calcoliamo il valore della S-box di AES per l'input $a = \texttt{53}_{16} = \texttt{01010011}_2$, che corrisponde al polinomio $a(x) = x^6 + x^4 + x + 1$:
> 
>   
> 
> 1. **Passo 1 (`FieldInv`):** Usando l'Algoritmo Euclideo Esteso per polinomi modulo $m(x) = x^8 + x^4 + x^3 + x + 1$, l'inverso moltiplicativo di $x^6 + x^4 + x + 1$ è $b(x) = x^7 + x^6 + x^3 + x$ (infatti $(x^6+x^4+x+1)(x^7+x^6+x^3+x) \equiv 1 \pmod{m(x)}$). In binario e in esadecimale:
>     
>       
>     
>     $$b = (b_7 b_6 b_5 b_4 b_3 b_2 b_1 b_0)_2 = \texttt{11001010}_2 = \mathbf{\texttt{CA}_{16}}$$
>     
> 2. **Passo 2 (Trasformazione Affine su $\mathbb{Z}_2$):** Moltiplicando il vettore colonna $(0, 1, 0, 1, 0, 0, 1, 1)^T$ (i bit di $\texttt{CA}_{16}$ da $b_0$ a $b_7$) per la matrice $8 \times 8$ e sommando modulo 2 il vettore $(1, 1, 0, 0, 0, 1, 1, 0)^T$ ($\texttt{63}_{16}$), si ottiene:
>     
>       
>     
>     $$c = (c_7 c_6 c_5 c_4 c_3 c_2 c_1 c_0)_2 = \texttt{11101101}_2 = \mathbf{\texttt{ED}_{16}}$$
>     
>     Pertanto $\text{SubBytes}(\texttt{53}_{16}) = \texttt{ED}_{16}$.
>     
>       
>     

#### 2. `ShiftRows` (Scorrimento Ciclico delle Righe)

Trasla ciclicamente verso **sinistra** i byte della riga $i$-esima della matrice `State` di **$i$ posizioni** ($i = 0, 1, 2, 3$):

  

- **Riga 0:** nessuno shift (resta invariata).
    
      
    
- **Riga 1:** shift ciclico a sinistra di **1 byte**.
    
      
    
- **Riga 2:** shift ciclico a sinistra di **2 byte**.
    
      
    
- **Riga 3:** shift ciclico a sinistra di **3 byte** (equivalente a 1 byte a destra).
    
      
    
    $$\begin{pmatrix} s_{0,0} & s_{0,1} & s_{0,2} & s_{0,3} \\ s_{1,0} & s_{1,1} & s_{1,2} & s_{1,3} \\ s_{2,0} & s_{2,1} & s_{2,2} & s_{2,3} \\ s_{3,0} & s_{3,1} & s_{3,2} & s_{3,3} \end{pmatrix} \xrightarrow{\text{ShiftRows}} \begin{pmatrix} s_{0,0} & s_{0,1} & s_{0,2} & s_{0,3} \\ s_{1,1} & s_{1,2} & s_{1,3} & s_{1,0} \\ s_{2,2} & s_{2,3} & s_{2,0} & s_{2,1} \\ s_{3,3} & s_{3,0} & s_{3,1} & s_{3,2} \end{pmatrix}$$
    
    _(Scopo crittografico: fa sì che i 4 byte di una stessa colonna prima di `ShiftRows` vengano distribuiti su 4 colonne diverse dopo `ShiftRows`, lavorando in sinergia con `MixColumns` per garantire diffusione totale in soli 2 round)._
    
      
    

#### 3. `MixColumns` (Diffusione Lineare sulle Colonne)

Opera su ciascuna delle 4 colonne di `State` individualmente. Ogni colonna $(s_{0,c}, s_{1,c}, s_{2,c}, s_{3,c})^T$ viene moltiplicata in $\mathbb{F}_{2^8}$ per una matrice fissa circolante $4 \times 4$ (una matrice **MDS** - _Maximum Distance Separable_, che garantisce che il numero totale di byte attivi tra input e output di una colonna non nulla sia sempre $\ge 5$):

  

$$\begin{pmatrix} s'_{0,c} \\ s'_{1,c} \\ s'_{2,c} \\ s'_{3,c} \end{pmatrix} = \begin{pmatrix} \texttt{02} & \texttt{03} & \texttt{01} & \texttt{01} \\ \texttt{01} & \texttt{02} & \texttt{03} & \texttt{01} \\ \texttt{01} & \texttt{01} & \texttt{02} & \texttt{03} \\ \texttt{03} & \texttt{01} & \texttt{01} & \texttt{02} \end{pmatrix} \begin{pmatrix} s_{0,c} \\ s_{1,c} \\ s_{2,c} \\ s_{3,c} \end{pmatrix} \quad \text{in } \mathbb{F}_{2^8}$$

- **Perché i coefficienti sono solo `01`, `02`, `03`?** Perché in hardware e software la moltiplicazione in $\mathbb{F}_{2^8}$ per questi tre elementi è velocissima:
    
      
    - $\texttt{01} \bullet s = s$ (identità).
        
          
        
    - $\texttt{02} \bullet s = \text{xtime}(s)$ (un semplice shift a sinistra ed eventuale XOR con $\texttt{1B}_{16}$).
        
          
        
    - $\texttt{03} \bullet s = (\texttt{02} \oplus \texttt{01}) \bullet s = (\texttt{02} \bullet s) \oplus s$.
        
          
        
- _(Interpretazione algebrica equivalente: ogni colonna è vista come un polinomio di grado $\le 3$ a coefficienti in $\mathbb{F}_{2^8}$ che viene moltiplicato per il polinomio fisso $a(X) = \texttt{03}X^3 + \texttt{01}X^2 + \texttt{01}X + \texttt{02}$ modulo $X^4 + 1$)._
    
      
    

#### 4. `AddRoundKey`

Esegue un semplice XOR bit a bit tra i 128 bit della matrice `State` e i 128 bit della sottochiave del round corrente $K^r$.

  

### 4.6.4 Il Key Schedule di AES (Espansione della Chiave a 128 bit)

Per AES-128 ($N_k = 4$, $N_r = 10$), il key schedule espande la chiave iniziale $K$ di 16 byte (4 word da 32 bit) in un array lineare di **44 word da 32 bit** indicato con $w[0], w[1], \dots, w[43]$:

  

- Le prime 4 word $(w[0], w[1], w[2], w[3])$ costituiscono la sottochiave iniziale $K^0$; in generale la sottochiave $K^r$ ($0 \le r \le 10$) è formata dalle 4 word $(w[4r], w[4r+1], w[4r+2], w[4r+3])$.
    
      
    
- **Algoritmo di generazione `KeyExpansion`:**
    
      
    1. Le prime 4 word copiano direttamente la chiave segreta $K$: $w[i] = (K_{4i}, K_{4i+1}, K_{4i+2}, K_{4i+3})$ per $i = 0, 1, 2, 3$.
        
          
        
    2. Per $i = 4, 5, \dots, 43$:
        
          
        - Si pone una variabile temporanea `temp` $\leftarrow w[i - 1]$.
            
              
            
        - **Se $i \equiv 0 \pmod 4$** (cioè stiamo calcolando la prima word di una nuova sottochiave di round), `temp` subisce una trasformazione non lineare prima dello XOR:
            
              
            
            $$\text{temp} \leftarrow \text{SubWord}(\text{RotWord}(\text{temp})) \oplus \text{Rcon}[i/4]$$
            
            dove:
            
              
            - `RotWord`$(b_0, b_1, b_2, b_3) = (b_1, b_2, b_3, b_0)$ (shift ciclico a sinistra di 1 byte della word).
                
                  
                
            - `SubWord`$(b_0, b_1, b_2, b_3) = (\text{SubBytes}(b_0), \dots, \text{SubBytes}(b_3))$ (applica la S-box di AES a tutti e 4 i byte).
                
                  
                
            - `Rcon`$[j] = (rc_j, \texttt{00}, \texttt{00}, \texttt{00})$ è la **costante di round** (_round constant_), in cui il primo byte vale $rc_j = x^{j-1} \bmod m(x)$ in $\mathbb{F}_{2^8}$ (cioè $rc_1=\texttt{01}, rc_2=\texttt{02}, rc_3=\texttt{04}, rc_4=\texttt{08}, rc_5=\texttt{10}, rc_6=\texttt{20}, rc_7=\texttt{40}, rc_8=\texttt{80}, rc_9=\texttt{1B}, rc_{10}=\texttt{36}$), introdotta per eliminare simmetrie tra i round e prevenire attacchi con chiavi correlate (_related-key attacks_).
                
                  
                
        - Infine (per tutti gli $i$), si calcola:
            
              
            
            $$w[i] \leftarrow w[i - 4] \oplus \text{temp}$$
            

#### Decifratura in AES

Poiché ogni singola operazione è invertibile, per decifrare si applicano le trasformazioni inverse con le sottochiavi in ordine inverso ($K^{10}, K^9, \dots, K^0$):

  

- `AddRoundKey` è l'inversa di se stessa (poiché lo XOR è involutorio).
    
      
    
- `InvShiftRows` trasla ciclicamente la riga $i$ verso **destra** di $i$ byte.
    
      
    
- `InvSubBytes` applica la S-box inversa $\pi_S^{-1}$ (prima l'inversa della trasformazione affine su $\mathbb{Z}_2$, poi l'inversione in $\mathbb{F}_{2^8}$). _(Nota che `InvShiftRows` e `InvSubBytes` commutano tra loro!)._
    
      
    
- `InvMixColumns` moltiplica ogni colonna per la matrice inversa in $\mathbb{F}_{2^8}$ (avente prima riga $\texttt{0E}, \texttt{0B}, \texttt{0D}, \texttt{09}$).
    
      
    

## 4.7 Modalità Operative dei Cifrari a Blocchi (ECB, CBC, CTR)

Un cifrario a blocchi come AES sa cifrare solamente **un singolo blocco** di lunghezza fissa $n$ bit (es. $n = 128$). Quando dobbiamo cifrare un messaggio lungo composto da una sequenza di $t$ blocchi $x_1, x_2, \dots, x_t$ (ciascuno di $n$ bit), dobbiamo specificare una **Modalità Operativa (Mode of Operation)**.

  

_(Se il messaggio originale non ha lunghezza multipla esatta di $n$ bit, prima di cifrare viene applicato uno schema di **padding** per riempire l'ultimo blocco $x_t$)_.

  

### 1. Electronic Codebook Mode (ECB)

È la modalità più semplice e ingenua: ogni blocco di testo in chiaro $x_j$ viene cifrato **in modo totalmente indipendente** dagli altri usando sempre la stessa chiave $K$:

  

- **Cifratura:**
    
      
    
    $$y_j = e_K(x_j) \qquad \text{per } 1 \le j \le t$$
    
- **Decifratura:**
    
      
    
    $$x_j = d_K(y_j) \qquad \text{per } 1 \le j \le t$$
    

#### Proprietà e Vulnerabilità Critica di ECB

- **Pro:** È completamente **parallelizzabile** sia in cifratura che in decifratura, e un errore di trasmissione su $y_j$ corrompe solo il blocco $x_j$.
    
      
    
- **Contro (Perché NON va mai usato):** È **deterministico** a livello di blocco. Se due blocchi di testo in chiaro sono identici ($x_i = x_j$), producono esattamente **lo stesso blocco di testo cifrato** ($y_i = y_j$).
    
      
    - _Conseguenza pratica:_ Non nasconde i pattern dei dati! Cifrando ad esempio un'immagine bitmap in modalità ECB, le aree di colore uniforme producono blocchi cifrati identici e la sagoma dell'immagine rimane perfettamente visibile a occhio nudo a Oscar; inoltre un attaccante attivo può riordinare, duplicare o sostituire singoli blocchi cifrati (_cut-and-paste attack_) senza che Bob se ne accorga.
        
          
        

### 2. Cipher Block Chaining Mode (CBC)

Per risolvere il difetto dell'ECB e fare in modo che due blocchi in chiaro uguali producano testi cifrati completamente diversi, la modalità **CBC** "incatena" i blocchi: prima di entrare nella funzione di cifratura $e_K$, ogni blocco di plaintext $x_j$ viene combinato tramite **XOR** con il **blocco di ciphertext precedente $y_{j-1}$**!

  

Per iniziare la catena sul primo blocco $x_1$ (che non ha un blocco precedente), si utilizza un blocco di $n$ bit chiamato **Initialization Vector ($IV$)**, indicato con $y_0 = IV$:

  

- **Cifratura CBC:**
    
      
    
    $$\begin{aligned} y_0 &\leftarrow IV \\ y_j &\leftarrow e_K(y_{j-1} \oplus x_j) \qquad \text{per } 1 \le j \le t \end{aligned}$$
    
- **Decifratura CBC:**
    
    Poiché $y_j = e_K(y_{j-1} \oplus x_j)$, applicando $d_K$ a entrambi i membri si ha $d_K(y_j) = y_{j-1} \oplus x_j$, da cui facendo lo XOR con $y_{j-1}$ si ricava immediatamente $x_j$:
    
      
    
    $$\begin{aligned} y_0 &\leftarrow IV \\ x_j &\leftarrow d_K(y_j) \oplus y_{j-1} \qquad \text{per } 1 \le j \le t \end{aligned}$$
    

#### Proprietà Fondamentali di CBC

1. **Requisiti sull'$IV$:** L'$IV$ **non deve essere segreto** (viene trasmesso in chiaro insieme al ciphertext come primo blocco $y_0$), ma per garantire la sicurezza semantica deve essere **casuale (o imprevedibile) e mai riutilizzato** con la stessa chiave.
    
      
    - (Esercizio 4.8 del libro: se Alice cifra due messaggi diversi $X$ e $X'$ usando la stessa chiave $K$ e lo **stesso $IV$**, Oscar può vedere immediatamente fino a quale blocco $j$ i due messaggi in chiaro sono identici!).
        
          
        
2. **Parallelizzabilità asimmetrica:**
    
      
    - La **Cifratura CBC è strettamente sequenziale** (non parallelizzabile): per calcolare $y_j$ devi prima aver finito di calcolare $y_{j-1}$.
        
          
        
    - La **Decifratura CBC è completamente parallelizzabile**: poiché Bob possiede già tutti i blocchi cifrati $y_0, y_1, \dots, y_t$, può calcolare tutti gli $x_j = d_K(y_j) \oplus y_{j-1}$ contemporaneamente su più processori (e può anche decifrare un singolo blocco $x_j$ a metà file conoscendo solo $y_{j-1}$ e $y_j$, proprietà detta _random access_).
        
          
        
3. **Propagazione degli errori:** Se un bit del blocco cifrato $y_j$ si corrompe durante la trasmissione, in decifratura il blocco $x_j = d_K(y_j) \oplus y_{j-1}$ risulterà completamente casuale/distrutto, mentre il blocco successivo $x_{j+1} = d_K(y_{j+1}) \oplus y_j$ avrà **solo quel singolo bit invertito**, e da $x_{j+2}$ in poi la decifratura tornerà perfetta (_auto-sincronizzazione dopo 2 blocchi_).
    
      
    

### 3. Counter Mode (CTR)

La modalità **CTR** trasforma un cifrario a blocchi in un vero e proprio **Stream Cipher sincrono**! Invece di cifrare il plaintext, si usa la funzione $e_K$ per cifrare i valori successivi di un **contatore (`ctr`)** di $n$ bit, generando una sequenza di blocchi di keystream che vengono poi sommati in XOR con i blocchi di plaintext.

  

Sia $\text{ctr} \in \{0, 1\}^n$ un valore iniziale scelto (spesso composto da un _nonce_ casuale concatenato a un contatore che parte da zero):

  

- **Cifratura CTR:**
    
    Per $1 \le j \le t$, si incrementa il contatore modulo $2^n$ e si cifra con $e_K$:
    
      
    
    $$T_j \leftarrow (\text{ctr} + j - 1) \bmod 2^n$$
    
    $$y_j \leftarrow x_j \oplus e_K(T_j)$$
    
- **Decifratura CTR:**
    
    Identica alla cifratura! Bob rigenera gli stessi blocchi di keystream $e_K(T_j)$ usando la funzione di **cifratura** $e_K$ e fa lo XOR con $y_j$:
    
      
    
    $$T_j \leftarrow (\text{ctr} + j - 1) \bmod 2^n$$
    
    $$x_j \leftarrow y_j \oplus e_K(T_j)$$
    

#### I Grandi Vantaggi di CTR (e perché è la modalità più amata oggi, es. in AES-GCM)

1. **Piena Parallelizzabilità (Esercizio 4.7):** Sia la **cifratura** che la **decifratura** sono **completamente parallelizzabili** al 100%, perché il blocco $T_j = (\text{ctr} + j - 1) \bmod 2^n$ è noto a priori per qualsiasi indice $j$ senza dover aspettare i blocchi precedenti!
    
      
    
2. **Pre-computazione del Keystream:** Alice e Bob possono calcolare tutti gli $e_K(T_j)$ (i caratteri della keystream) in anticipo nei tempi morti prima ancora di conoscere il messaggio $x$; quando arriva $x$, la cifratura richiede solo un velocissimo XOR.
    
      
    
3. **Non serve implementare la funzione di decifratura $d_K$:** Sia Alice che Bob usano **esclusivamente la funzione di cifratura $e_K$**! (In hardware o su smartcard questo dimezza lo spazio occupato dal codice di AES).
    
      
    
4. **Non serve Padding:** Se l'ultimo blocco $x_t$ è più corto di $n$ bit (es. solo $\ell < n$ bit), basta prendere i primi $\ell$ bit di $e_K(T_t)$ e fare lo XOR, senza allungare il messaggio.
    
      
    
5. **Unico divieto assoluto (Esercizio 4.9):** Come in ogni stream cipher e nel One-Time Pad, **non bisogna mai riutilizzare lo stesso valore del contatore `ctr` con la stessa chiave $K$**! Se $X$ e $X'$ vengono cifrati con lo stesso `ctr` e la stessa $K$, Oscar calcola $y_j \oplus y'_j = x_j \oplus x'_j$ bucando istantaneamente la cifratura.
    
      
    

### Tabella di Confronto Rapido: ECB vs CBC vs CTR

|**Caratteristica**|**ECB**|**CBC**|**CTR**|
|---|---|---|---|
|**Tipo di schema**|Block Cipher puro|Block Cipher incatenato|Stream Cipher sincrono|
|**Nasconde i pattern ($x_i = x_j$)?**|❌ **NO** ($y_i = y_j$)|✅ Sì (grazie a $IV$ e chaining)|✅ Sì (grazie al contatore $T_j$)|
|**Cifratura parallelizzabile?**|✅ Sì|❌ **NO** (sequenziale)|✅ **Sì** (100% + precomputabile)|
|**Decifratura parallelizzabile?**|✅ Sì|✅ **Sì**|✅ **Sì** (100% + precomputabile)|
|**Richiede funzione inversa $d_K$?**|Sì|Sì|❌ **NO** (usa solo $e_K$!)|
|**Richiede Padding?**|Sì|Sì (vulnerabile a Padding Oracle!)|❌ **NO**|

## 4.7.1 Padding Oracle Attack sulla Modalità CBC

Scoperto da **Serge Vaudenay nel 2002**, il **Padding Oracle Attack** è uno degli attacchi pratici più devastanti della crittografia moderna (ha colpito protocolli reali come SSL/TLS, IPsec e WTLS). Dimostra come un attaccante (Oscar), senza conoscere la chiave segreta $K$, possa **decifrare completamente qualsiasi blocco cifrato in modalità CBC** sfruttando semplicemente il messaggio di errore (`"Padding valido"` vs `"Errore di padding"`) restituito da un server!

  

### A. Lo Schema di Padding Standard (PKCS #7)

Supponiamo che il cifrario operi su blocchi di **$B$ byte** (es. $B = 16$ byte per AES, o $B = 8$ byte nei vecchi cifrari). Per fare in modo che il messaggio in chiaro abbia sempre una lunghezza multipla esatta di $B$ byte e che Bob, dopo la decifratura, sappia esattamente **quanti byte di padding rimuovere**, lo standard **PKCS #7** usa la seguente regola:

  

1. Se l'ultimo blocco del messaggio originale contiene $B - b$ byte di dati (con $1 \le b \le B$), mancano esattamente **$b$ byte** per completare il blocco da $B$ byte.
    
      
    
2. Si aggiungono in coda esattamente **$b$ byte tutti uguali al valore numerico $b$** (scritto in esadecimale):
    
      
    - Se manca **1 byte** ($b=1$): il blocco deve terminare con **`01`**.
        
          
        
    - Se mancano **2 byte** ($b=2$): il blocco deve terminare con **`02 02`**.
        
          
        
    - Se mancano **3 byte** ($b=3$): il blocco deve terminare con **`03 03 03`**.
        
          
        
    - $\dots$
        
          
        
    - Se il messaggio originale è già un multiplo esatto di $B$ byte ($b = B$): si aggiunge un **intero nuovo blocco fittizio di $B$ byte** tutti uguali a $B$ (es. sedici byte `10 10 ... 10` in esadecimale per $B=16$), altrimenti Bob non saprebbe distinguere i dati veri dal padding!
        
          
        

Quando il server (Bob) riceve un ciphertext in modalità CBC, lo decifra e controlla gli ultimi byte dell'ultimo blocco $x_t$: se non rispettano il formato PKCS #7 (ad esempio se l'ultimo byte è `02`, ma il penultimo byte non è `02`), il server scarta il pacchetto e restituisce un errore di **Padding Invalido**.

  

### B. Il Modello dell'Attacco: Cos'è il "Padding Oracle"?

Supponiamo che esista un server (**Padding Oracle**) a cui Oscar può inviare qualsiasi coppia di blocchi cifrati $(y_0, y_1)$ in modalità CBC (un attacco di tipo _chosen-ciphertext_ adattivo). Il server decifra $(y_0, y_1)$ con la sua chiave segreta $K$ calcolando:

  

$$x_1 = d_K(y_1) \oplus y_0$$

e controlla se $x_1$ termina con un padding PKCS #7 valido:

  

- Restituisce **`VALID` (1)** se il padding di $x_1$ è formalmente corretto (es. finisce con `01`, oppure con `02 02`, oppure con `03 03 03`, ecc.).
    
      
    
- Restituisce **`INVALID` (0)** se il padding è errato.
    
      
    

Il server **non rivela mai il testo decifrato**, ma quel singolo bit di risposta (`VALID` / `INVALID`) basta a Oscar per decifrare l'intero blocco $x_1$ byte per byte senza conoscere $K$!

  

### C. Meccanica Matematica dell'Attacco Passo-Passo

Supponiamo che Oscar abbia intercettato due blocchi consecutivi $(y_0, y_1)$ (dove $y_0$ può essere l'$IV$ o un blocco cifrato precedente $y_{j-1}$, e $y_1$ è il blocco bersaglio $y_j$) e voglia scoprire tutti i $B$ byte del blocco in chiaro:

  

$$x_1 = (x_{1,1}, x_{1,2}, \dots, x_{1,B}) = d_K(y_1) \oplus y_0$$

Indichiamo i $B$ byte del blocco $y_0$ con $(y_{0,1}, y_{0,2}, \dots, y_{0,B})$. Per la formula di decifratura CBC, per ogni singolo byte $i \in \{1, \dots, B\}$ vale:

  

$$x_{1,i} = d_K(y_1)_i \oplus y_{0,i} \quad \Longleftrightarrow \quad d_K(y_1)_i = x_{1,i} \oplus y_{0,i}$$

#### FASE 1: Scoprire l'ultimo byte $x_{1,B}$ (forzando il padding `01`)

Oscar costruisce un blocco modificato $w = (r_1, r_2, \dots, r_{B-1}, i)$ in cui i primi $B-1$ byte sono scelti a caso e l'ultimo byte $i$ varia da $0$ a $255$ ($\texttt{00}_{16}, \dots, \texttt{FF}_{16}$), e invia al Padding Oracle la coppia **$(w, y_1)$**:

  

1. Il server decifra $y_1$ ottenendo il blocco in chiaro modificato:
    
      
    
    $$x'_1 = d_K(y_1) \oplus w$$
    
2. Guardiamo cosa succede all'**ultimo byte** $x'_{1,B}$ di questo blocco decifrato dal server:
    
    Poiché $d_K(y_1)_B = x_{1,B} \oplus y_{0,B}$, sostituendo otteniamo l'equazione fondamentale dell'attacco:
    
      
    
    $$x'_{1,B} = d_K(y_1)_B \oplus i = x_{1,B} \oplus y_{0,B} \oplus i$$
    
3. Al variare di $i \in \{0, 1, \dots, 255\}$, il byte $x'_{1,B}$ assume tutti i 256 valori possibili esattamente una volta!
    
    Quando il tentativo $i$ scelto da Oscar fa sì che l'ultimo byte diventi esattamente **`01`** ($x'_{1,B} = \texttt{01}_{16}$), il server vede un blocco che termina con `01` e risponde **`VALID`**!
    
      
    
4. Non appena il server risponde `VALID` per un certo valore $i$, Oscar sa che:
    
      
    
    $$x_{1,B} \oplus y_{0,B} \oplus i = \texttt{01}_{16}$$
    
    E poiché Oscar conosce sia il byte originale $y_{0,B}$ sia il valore $i$ che ha appena inviato, ricava istantaneamente l'ultimo byte del testo in chiaro:
    
      
    
    $$x_{1,B} = y_{0,B} \oplus i \oplus \texttt{01}_{16}$$
    

- **Il caso ambiguo (Falso Positivo sul primo byte) e come risolverlo:**
    
    E se per sfortuna il blocco $x'_1$ aveva il penultimo byte $x'_{1,B-1} = \texttt{02}_{16}$, e il server ha risposto `VALID` perché $x'_{1,B}$ è diventato `02` (formando `02 02`) invece di `01`?
    
      
    - **Soluzione facilissima:** Quando Oscar trova il valore $i$ che dà `VALID`, fa **una sola query di verifica**: cambia il penultimo byte $r_{B-1}$ in $r_{B-1} \oplus \texttt{01}$ (lasciando $i$ invariato) e rinvia $(w, y_1)$ al server.
        
          
        
    - Se il server risponde **ancora `VALID`**, significa che il penultimo byte non c'entrava nulla: il padding era davvero **`01`** e $x_{1,B} = y_{0,B} \oplus i \oplus \texttt{01}$ è corretto al 100%!
        
          
        
    - Se invece il server risponde **`INVALID`**, significa che avevamo colpito un padding più lungo (quasi certamente `02 02`), quindi basta continuare il ciclo su $i$ fino a trovare l'altro valore che dà `VALID` (oppure dedurre direttamente $x_{1,B} = y_{0,B} \oplus i \oplus \texttt{02}$).
        
          
        

#### FASE 2: Scoprire i byte precedenti $x_{1,B-1}, x_{1,B-2}, \dots, x_{1,1}$ per induzione

Una volta scoperto l'ultimo byte $x_{1,B}$ (o in generale una volta scoperti gli ultimi $k-1$ byte $x_{1,B-k+2}, \dots, x_{1,B}$), come fa Oscar a trovare il byte precedente $x_{1,B-k+1}$? **Forza un padding valido di lunghezza $k$** (cioè gli ultimi $k$ byte tutti uguali a $k$)!

  

Vediamo il passaggio esplicito per il **penultimo byte $x_{1,B-1}$ ($k = 2$, forzando `02 02`)**:

  

1. Poiché Oscar conosce ormai $x_{1,B}$, può impostare l'ultimo byte $w_B$ del blocco $w$ in modo che l'ultimo byte decifrato dal server $x'_{1,B}$ diventi **forzatamente `02`**:
    
      
    
    $$w_B = y_{0,B} \oplus x_{1,B} \oplus \texttt{02}_{16} \quad \implies \quad x'_{1,B} = x_{1,B} \oplus y_{0,B} \oplus w_B = \mathbf{\texttt{02}_{16}}$$
    
2. Ora Oscar fa variare il **penultimo byte** $w_{B-1} = i \in \{0, \dots, 255\}$ inviando $w = (r_1, \dots, r_{B-2}, i, w_B)$ insieme a $y_1$ al server.
    
      
    
3. Il server risponderà **`VALID`** solo ed esclusivamente quando anche il penultimo byte decifrato $x'_{1,B-1}$ diventerà uguale a **`02`** (completando il padding valido `02 02`)!
    
      
    
4. Dal valore $i$ vincente, Oscar calcola subito il penultimo byte del testo in chiaro:
    
      
    
    $$x_{1,B-1} = y_{0,B-1} \oplus i \oplus \texttt{02}_{16}$$
    

**Formula Generale per il passo $k$ ($k = 2, 3, \dots, B$):**

Per trovare il byte $x_{1,B-k+1}$:

  

1. Oscar fissa gli ultimi $k-1$ byte di $w$ (per $j = B - k + 2, \dots, B$) al valore:
    
      
    
    $$w_j = y_{0,j} \oplus x_{1,j} \oplus k$$
    
    (così gli ultimi $k-1$ byte decifrati dal server valgono già tutti $k$).
    
      
    
2. Fa variare il byte $w_{B-k+1} = i \in \{0, \dots, 255\}$ finché l'oracolo non restituisce **`VALID`** (cioè finché anche $x'_{1,B-k+1} = k$).
    
      
    
3. Ricava il byte in chiaro:
    
      
    
    $$x_{1,B-k+1} = y_{0,B-k+1} \oplus i \oplus k$$
    

> [!example] Esempio Numerico Completo del Padding Oracle Attack (su blocchi di $B = 4$ byte)
> 
> Supponiamo di lavorare con blocchi di $B = 4$ byte e che Oscar intercetti:
> 
>   
> 
> $$y_0 = (\texttt{12}, \texttt{34}, \texttt{56}, \texttt{78}) \qquad \text{e} \qquad y_1$$
> 
> (Supponiamo che il vero testo in chiaro segreto dietro $y_1$ sia $x_1 = (\texttt{43}, \texttt{41}, \texttt{54}, \texttt{01})$, cioè `"CAT"` seguito da 1 byte di padding `01`). Vediamo come Oscar trova gli ultimi due byte senza sapere nulla:
> 
>   
> 
> 1. **Scoperta del 4° byte ($x_{1,4}$):**
>     
>       
>     - Oscar invia $w = (\texttt{00}, \texttt{00}, \texttt{00}, i)$ e $y_1$ al server facendo variare $i$ da $\texttt{00}$ a $\texttt{FF}$.
>         
>           
>         
>     - Quando $i = \texttt{78}_{16}$, il server calcola l'ultimo byte $x'_{1,4} = x_{1,4} \oplus y_{0,4} \oplus i = \texttt{01} \oplus \texttt{78} \oplus \texttt{78} = \texttt{01}$ e risponde **`VALID`**!
>         
>           
>         
>     - Oscar applica la formula (dopo il test sul penultimo byte):
>         
>           
>         
>         $$x_{1,4} = y_{0,4} \oplus i \oplus \texttt{01} = \texttt{78} \oplus \texttt{78} \oplus \texttt{01} = \mathbf{\texttt{01}_{16}}$$
>         
> 2. **Scoperta del 3° byte ($x_{1,3}$):**
>     
>       
>     - Ora Oscar vuole forzare gli ultimi due byte a `02 02`. Calcola quindi il 4° byte fisso di $w$:
>         
>           
>         
>         $$w_4 = y_{0,4} \oplus x_{1,4} \oplus \texttt{02} = \texttt{78} \oplus \texttt{01} \oplus \texttt{02} = \mathbf{\texttt{7B}_{16}}$$
>         
>     - Oscar invia $w = (\texttt{00}, \texttt{00}, i, \texttt{7B})$ e $y_1$ facendo variare $i$.
>         
>           
>         
>     - Quando $i = \texttt{00}_{16}$, il server calcola il 3° byte $x'_{1,3} = x_{1,3} \oplus y_{0,3} \oplus i = \texttt{54} \oplus \texttt{56} \oplus \texttt{00} = \texttt{02}$, vede `02 02` e risponde **`VALID`**!
>         
>           
>         
>     - Oscar ricava immediatamente il 3° byte in chiaro:
>         
>           
>         
>         $$x_{1,3} = y_{0,3} \oplus i \oplus \texttt{02} = \texttt{56} \oplus \texttt{00} \oplus \texttt{02} = \mathbf{\texttt{54}_{16}} \quad (\text{la lettera ASCII } \texttt{'T'}!)$$
>         
> 3. **Complessità dell'attacco:**
>     
>     Per scoprire ciascun byte servono al massimo $256$ tentativi (in media $128$). Per decifrare un intero blocco AES di $B = 16$ byte ($128$ bit), invece di $2^{128}$ operazioni, a Oscar bastano in media:
>     
>       
>     
>     $$16 \times 128 = \mathbf{2048 \text{ query al server}}$$
>     
>     (meno di un secondo di traffico di rete!).
>     
>       
>     
> 
> - **Come ci si difende dal Padding Oracle Attack?** Non permettendo mai al server di decifrare testi cifrati manipolati da un attaccante! Si utilizza la **Crittografia Autenticata (Authenticated Encryption / Encrypt-then-MAC, Sezione 5.5.3)**: si applica un MAC (es. HMAC) sul testo cifrato $(IV, y_1, \dots, y_t)$. Se Oscar modifica anche un solo bit di $w$, la verifica del MAC fallisce **prima ancora** di eseguire la decifratura CBC, e il server non rivela alcuna informazione sul padding.
>Ecco la sezione **4.8 Stream Ciphers** (dall'introduzione fino a tutto il paragrafo **4.8.1**, escludendo 4.8.2 e 4.8.3), strutturata e formattata nello stesso identico stile del tuo file `Cap4.md` così da poterla incollare direttamente in coda ai tuoi appunti.


## 4.8 Stream Ciphers (Cifrari a Flusso)

A differenza dei cifrari a blocchi (che dividono il messaggio in blocchi di lunghezza fissa cifrandone uno alla volta con la stessa chiave $K$), uno **Stream Cipher** utilizza la chiave segreta $K$ per generare una sequenza di bit chiamata **keystream** (flusso di chiave) $z_1 z_2 \dots$ della stessa lunghezza del plaintext, cifrando e decifrando il messaggio un bit alla volta tramite l'operazione di **XOR ($\oplus$)**:

  

$$\text{Cifratura: } y_i = x_i \oplus z_i \qquad \qquad \text{Decifratura: } x_i = y_i \oplus z_i$$

Questo approccio nasce per superare il limite pratico del _One-Time Pad_: anziché richiedere una chiave casuale lunga quanto l'intero messaggio, uno stream cipher espande una chiave segreta $K$ corta in una lunga sequenza di bit (la keystream) dall'aspetto pseudocasuale.

  

### Richiamo: Stream Cipher Sincroni e Limite degli LFSR Lineari

Nella Sezione 2.1.7 abbiamo definito formalmente uno **Stream Cipher sincrono** come un sistema in cui la keystream $z_1 z_2 \dots$ viene generata a partire dalla sola chiave $K$ (tramite un generatore $g$), in modo completamente indipendente dal testo in chiaro.

  

Il metodo più semplice ed efficiente in hardware per generare una lunga keystream binaria a partire da una chiave corta di $m$ bit consiste nell'utilizzare un **LFSR (Linear Feedback Shift Register)** a $m$ stadi (introdotto nel Capitolo 2):

  

- Lo stato iniziale del registro contiene i bit della chiave segreta $K = (k_1, k_2, \dots, k_m)$.
    
      
    
- Ad ogni ciclo di clock, i bit successivi della keystream vengono calcolati tramite una **relazione di ricorrenza lineare** di grado $m$ su $\mathbb{Z}_2$:
    
      
    
    $$z_{i+m} = \left( \sum_{j=0}^{m-1} c_j z_{i+j} \right) \bmod 2$$
    
    (Se il polinomio di feedback associato è primitivo, la sequenza prodotta ha periodo massimo pari a $2^m - 1$).
    
      
    
- **Perché un singolo LFSR NON è sicuro? (Vulnerabilità alla Crittoanalisi Known-Plaintext):** Come visto nella Sezione 2.2.5 (Example 2.14), un singolo LFSR è **completamente lineare**. Se l'attaccante (Oscar) conosce appena **$2m$ bit consecutivi di plaintext** $x_1, \dots, x_{2m}$ e i corrispondenti bit di ciphertext $y_1, \dots, y_{2m}$, può ricavare immediatamente i primi $2m$ bit della keystream facendo lo XOR ($z_i = x_i \oplus y_i$) e impostare un sistema lineare di $m$ equazioni in $m$ incognite, invertendo una matrice $m \times m$ di bit della keystream per trovare tutti i coefficienti segreti dell'LFSR e ricostruire l'intera sequenza futura:
    
      
    
    $$\begin{pmatrix} c_0 \\ c_1 \\ \vdots \\ c_{m-1} \end{pmatrix} = \begin{pmatrix} z_1 & z_2 & \dots & z_m \\ z_2 & z_3 & \dots & z_{m+1} \\ \vdots & \vdots & \ddots & \vdots \\ z_m & z_{m+1} & \dots & z_{2m-1} \end{pmatrix}^{-1} \begin{pmatrix} z_{m+1} \\ z_{m+2} \\ \vdots \\ z_{2m} \end{pmatrix} \bmod 2$$
    

### I 3 Metodi di Progettazione per Introdurre Non-Linearità negli LFSR

Poiché gli LFSR sono velocissimi in hardware e producono sequenze con ottime proprietà statistiche e periodi molto lunghi, i progettisti di stream cipher non li hanno abbandonati, ma hanno cercato modi per **distruggere la linearità** dell'LFSR aggiungendo componenti **non lineari**.

  

Nell'introduzione della Sezione 4.8 vengono presentati i **tre schemi classici di generatori basati su LFSR**:

  

1. **Combination Generator (Generatore a Combinazione):**
    
      
    - Si utilizzano **$r$ diversi LFSR** in parallelo (aventi lunghezze $m_1, m_2, \dots, m_r$, solitamente scelte a due a due coprime per massimizzare il periodo complessivo).
        
          
        
    - Indichiamo con $z_1^j, z_2^j, \dots$ la sequenza prodotta dal $j$-esimo LFSR ($1 \le j \le r$).
        
          
        
    - Ad ogni istante $i \ge 1$, i bit in uscita dai singoli LFSR vengono combinati attraverso una funzione booleana **non lineare** $f : (\mathbb{Z}_2)^r \to \mathbb{Z}_2$, chiamata **combining function** (funzione di combinazione), per produrre il bit finale della keystream:
        
          
        
        $$z_i = f\left(z_i^1, z_i^2, \dots, z_i^r\right)$$
        
    - La chiave segreta del sistema è costituita dagli stati iniziali (i _seed_) di tutti gli $r$ LFSR (mentre i polinomi di feedback dei singoli LFSR e la funzione $f$ sono pubblici).
        
          
        
2. **Filter Generator (Generatore a Filtro):**
    
      
    - Si utilizza **un singolo LFSR** composto da $m$ stadi.
        
          
        
    - Invece di usare direttamente l'uscita lineare del registro come keystream, a ogni passo $i$ si applica una funzione booleana non lineare $f : (\mathbb{Z}_2)^m \to \mathbb{Z}_2$ (detta **filtering function**, funzione di filtraggio) all'intero stato corrente di $m$ bit dell'LFSR (o a un sottoinsieme dei suoi stadi):
        
          
        
        $$z_i = f(z_i, z_{i+1}, \dots, z_{i+m-1})$$
        
3. **Shrinking Generator (Generatore a Contrazione):**
    
      
    - Si utilizzano **due LFSR** (chiamiamoli $\text{LFSR}_1$, che genera la sequenza $z_1^1, z_2^1, \dots$, e $\text{LFSR}_2$, che genera la sequenza di controllo $z_1^2, z_2^2, \dots$).
        
          
        
    - Ad ogni ciclo di clock entrambi i registri avanzano di un passo, ma il bit di $\text{LFSR}_2$ viene usato per decidere se tenere o scartare il bit di $\text{LFSR}_1$:
        
          
        - Se **$z_i^2 = 1$**, il bit $z_i^1$ viene **emesso in uscita** come prossimo bit della keystream.
            
              
            
        - Se **$z_i^2 = 0$**, il bit $z_i^1$ viene **scartato** (non viene emesso nulla in quel ciclo).
            
              
            
    - In questo modo la sequenza del primo LFSR viene "contratta" (_shrunk_) in modo irregolare, distruggendo la sincronia lineare.
        
          
        

> [!example] Esempio Illustrativo dei 3 Generatori (Combination, Filter e Shrinking)
> 
> Vediamo con un piccolo esempio numerico come lavorano i tre schemi a confronto:
> 
>   
> 
> - **Caso A – Combination Generator ($r = 3$ LFSR):**
>     
>     Supponiamo che al passo $i=1, 2, 3, 4$ i tre LFSR producano le sequenze:
>     
>       
>     - $\text{LFSR}_1$: `1, 0, 1, 1`
>         
>           
>         
>     - $\text{LFSR}_2$: `0, 1, 1, 0`
>         
>           
>         
>     - $\text{LFSR}_3$: `1, 1, 0, 0` Usando come _combining function_ $f(a, b, c) = (a \wedge b) \oplus (\neg a \wedge c)$, otteniamo bit per bit:
>         
>           
>         
>     - $i=1$: $f(1, 0, 1) = (1 \cdot 0) \oplus (0 \cdot 1) = \mathbf{0}$
>         
>           
>         
>     - $i=2$: $f(0, 1, 1) = (0 \cdot 1) \oplus (1 \cdot 1) = \mathbf{1}$
>         
>           
>         
>     - $i=3$: $f(1, 1, 0) = (1 \cdot 1) \oplus (0 \cdot 0) = \mathbf{1}$
>         
>           
>         
>     - $i=4$: $f(1, 0, 0) = (1 \cdot 0) \oplus (0 \cdot 0) = \mathbf{0}$
>         
>         La keystream emessa è quindi **`0110`**.
>         
>           
>         
> - **Caso B – Filter Generator ($1$ solo LFSR di $m=3$ stadi):**
>     
>     Supponiamo che il singolo LFSR abbia stato interno al tempo $i=1$ pari a $(s_0, s_1, s_2) = (1, 1, 0)$ e la funzione di filtro sia $f(s_0, s_1, s_2) = (s_0 \wedge s_1) \oplus s_2$.
>     
>     Allora il bit di keystream emesso in quell'istante è $z_1 = (1 \cdot 1) \oplus 0 = \mathbf{1}$. Poi l'LFSR fa scorrere i suoi bit di una posizione e si ricalcola $f$ sul nuovo stato interno.
>     
>       
>     
> - **Caso C – Shrinking Generator ($2$ LFSR):**
>     
>     Supponiamo che i due LFSR generino i seguenti 6 bit:
>     
>       
>     - $\text{LFSR}_1$ (Dati $z_i^1$): $\quad \ \ \texttt{1, 0, 1, 1, 0, 1}$
>         
>           
>         
>     - $\text{LFSR}_2$ (Selettore $z_i^2$): $\texttt{1, 0, 0, 1, 1, 0}$
>         
>         Teniamo $z_i^1$ **solo quando $z_i^2 = 1$** (cioè agli indici $i = 1, 4, 5$):
>         
>           
>         
>     - $i=1$ ($z_1^2 = 1$) $\implies$ emette $z_1^1 = \mathbf{1}$
>         
>           
>         
>     - $i=2$ ($z_2^2 = 0$) $\implies$ _scarta_ $z_2^1$
>         
>           
>         
>     - $i=3$ ($z_3^2 = 0$) $\implies$ _scarta_ $z_3^1$
>         
>           
>         
>     - $i=4$ ($z_4^2 = 1$) $\implies$ emette $z_4^1 = \mathbf{1}$
>         
>           
>         
>     - $i=5$ ($z_5^2 = 1$) $\implies$ emette $z_5^1 = \mathbf{0}$
>         
>           
>         
>     - $i=6$ ($z_6^2 = 0$) $\implies$ _scarta_ $z_6^1$
>         
>         Dai 6 cicli di clock esce una keystream contratta di soli 3 bit: **`110`**.
>         
>           
>         

## 4.8.1 Correlation Attack on a Combination Generator (Attacco di Correlazione)

Sebbene un _Combination Generator_ utilizzi una funzione booleana non lineare $f$ per mascherare i singoli LFSR, se la funzione $f$ non è progettata con estrema attenzione il sistema può essere completamente distrutto da un attacco statistico di tipo _divide-and-conquer_ (divide et impera) noto come **Correlation Attack** (Attacco di Correlazione, introdotto da Thomas Siegenthaler).

  

### 1. Il Problema della Ricerca Esaustiva vs Divide-et-Impera

Consideriamo un Combination Generator formato da $r$ LFSR aventi lunghezze (gradi dei polinomi di feedback) pari a $m_1, m_2, \dots, m_r$.

  

- Assumiamo che i polinomi di feedback dei singoli LFSR e la funzione di combinazione $f : (\mathbb{Z}_2)^r \to \mathbb{Z}_2$ siano **pubblici**.
    
      
    
- La **chiave segreta $K$** consiste nelle $r$ tuple di riempimento iniziale (_initial states_) dei singoli registri:
    
      
    
    $$K = (K^1, K^2, \dots, K^r) \qquad \text{con } K^j \in (\mathbb{Z}_2)^{m_j} \setminus \{\mathbf{0}\}$$
    
    (Lo stato formato da tutti zeri `00...0` è sempre escluso perché in un LFSR produrrebbe solo una sequenza infinita di zeri).
    
      
    
- Pertanto, il numero di possibili chiavi iniziali per il $j$-esimo LFSR è esattamente **$2^{m_j} - 1$**.
    
      
    
- Se Oscar volesse attaccare il generatore con una **ricerca esaustiva (forza bruta)** provando tutte le combinazioni simultaneamente, dovrebbe testare un numero di chiavi pari al **prodotto**:
    
      
    
    $$\prod_{j=1}^{r} \left(2^{m_j} - 1\right) \approx 2^{m_1 + m_2 + \dots + m_r}$$
    
    che diventa rapidamente infattibile se la somma $\sum m_j$ è grande.
    
      
    

**L'idea del Correlation Attack:** E se invece di indovinare tutte le $r$ sottochiavi contemporaneamente, Oscar riuscisse a trovare $K^1, K^2, \dots, K^r$ **una alla volta in modo indipendente**? In quel caso il numero di tentativi scenderebbe dal _prodotto_ alla semplice **somma** $\sum_{j=1}^r (2^{m_j} - 1)$!

  

### 2. Correlazione Statistica nella Tabella di Verità di $f$

Trattiamo i bit $z_1, z_2, \dots, z_r$ in ingresso alla funzione combinatrice $f(z_1, \dots, z_r)$ come variabili aleatorie binarie indipendenti e uniformemente distribuite, tali cioè che per ogni $j = 1, \dots, r$ e per ogni $z \in \{0, 1\}$ valga:

  

$$\Pr[z_j = z] = \frac{1}{2}$$

Di conseguenza, ciascuna delle $2^r$ righe della tabella di verità di $f(z_1, \dots, z_r)$ ha probabilità esattamente $\frac{1}{2^r}$.

  

- **Condizione per una buona funzione combinatrice (Bilanciamento):** Innanzitutto, affinché la keystream finale non abbia una prevalenza banale di `0` o di `1`, la funzione $f$ deve essere **bilanciata**, cioè la colonna di uscita della sua tabella di verità deve contenere esattamente $2^{r-1}$ zeri e $2^{r-1}$ uni:
    
      
    
    $$\Pr[f(z_1, \dots, z_r) = 0] = \Pr[f(z_1, \dots, z_r) = 1] = \frac{1}{2}$$
    
- **La Falla (Correlazione tra l'uscita $f$ e un singolo input $z_j$):** Anche se $f$ è perfettamente bilanciata, calcoliamo per ciascun input $z_j$ ($1 \le j \le r$) la probabilità $p_j$ che l'uscita della funzione combinatrice coincida esattamente con il bit del $j$-esimo LFSR:
    
      
    
    $$p_j = \Pr\left[ f(z_1, \dots, z_r) = z_j \right]$$
    
    (che si calcola semplicemente contando in quante righe su $2^r$ della tabella di verità il valore di $f(z_1, \dots, z_r)$ è uguale a $z_j$, e dividendo per $2^r$).
    
      
    - Se **$p_j \neq \frac{1}{2}$**, diciamo che esiste una **correlazione** tra la keystream finale $z_i$ e la sequenza $z_i^j$ del $j$-esimo LFSR!
        
          
        

### 3. Analisi del Generatore di Geffe (Geffe Generator)

L'esempio classico analizzato da Stinson (presente anche nell'Esercizio 4.18) utilizza $r = 3$ LFSR combinati tramite la funzione nota come **Geffe Generator**:

  

$$f(z_1, z_2, z_3) = (z_1 \wedge z_2) \oplus (\neg z_1 \wedge z_3)$$

(In aritmetica algebrica su $\mathbb{Z}_2$, ricordando che $\wedge$ è il prodotto e $\neg z_1 = 1 \oplus z_1$, questa funzione si scrive equivalentemente come:

  

$$f(z_1, z_2, z_3) = z_1 z_2 \oplus (1 \oplus z_1) z_3 = z_1 z_2 \oplus z_3 \oplus z_1 z_3 \bmod 2$$

oppure, permutando gli indici dei registri come nel testo della Sezione 4.8.1, $f(z_1, z_2, z_3) = z_1 z_2 \oplus z_2 z_3 \oplus z_3$).

  

- **Interpretazione intuitiva del Geffe Generator:** Il registro $z_1$ funziona come un **selettore (multiplexer)**:
    
      
    - Ogni volta che **$z_1 = 1$**, l'uscita di $f$ copia esattamente **$z_2$**.
        
          
        
    - Ogni volta che **$z_1 = 0$**, l'uscita di $f$ copia esattamente **$z_3$**.
        
          
        

Costruiamo la **Tabella di Verità completa** delle $2^3 = 8$ righe per $f(z_1, z_2, z_3) = (z_1 \wedge z_2) \oplus (\neg z_1 \wedge z_3)$ e controlliamo in quali righe $f$ coincide con $z_1$, con $z_2$ e con $z_3$:

  

|**z1​**|**z2​**|**z3​**|**f(z1​,z2​,z3​)**|**Coincide con z1​? (f=z1​)**|**Coincide con z2​? (f=z2​)**|**Coincide con z3​? (f=z3​)**|
|---|---|---|---|---|---|---|
|`0`|`0`|`0`|**`0`**|✅ Sì|✅ Sì|✅ Sì|
|`0`|`0`|`1`|**`1`**|❌ No|❌ No|✅ Sì|
|`0`|`1`|`0`|**`0`**|✅ Sì|❌ No|✅ Sì|
|`0`|`1`|`1`|**`1`**|❌ No|✅ Sì|✅ Sì|
|`1`|`0`|`0`|**`0`**|❌ No|✅ Sì|✅ Sì|
|`1`|`0`|`1`|**`0`**|❌ No|✅ Sì|❌ No|
|`1`|`1`|`0`|**`1`**|✅ Sì|✅ Sì|❌ No|
|`1`|`1`|`1`|**`1`**|✅ Sì|✅ Sì|✅ Sì|
|**Totale**|||**4 zeri, 4 uni (Bilanciata)**|**4 su 8**|**6 su 8**|**6 su 8**|

Dalla tabella leggiamo immediatamente le tre probabilità di correlazione:

  

1. $\Pr[f(z_1, z_2, z_3) = z_1] = \frac{4}{8} = \mathbf{\frac{1}{2}}$ _(Nessuna correlazione con il 1° LFSR)_.
    
      
    
2. $\Pr[f(z_1, z_2, z_3) = z_2] = \frac{6}{8} = \mathbf{\frac{3}{4} = 0.75}$ _(Forte correlazione del **75%** con il 2° LFSR!)_.
    
      
    
3. $\Pr[f(z_1, z_2, z_3) = z_3] = \frac{6}{8} = \mathbf{\frac{3}{4} = 0.75}$ _(Forte correlazione del **75%** con il 3° LFSR!)_.
    
      
    

### 4. Come Funziona l'Attacco di Correlazione Passo-Passo

Supponiamo che Oscar conduca un attacco _known-plaintext_ e abbia a disposizione **$N$ bit consecutivi della keystream** $z_1, z_2, \dots, z_N$ (ottenuti facendo lo XOR tra $N$ bit di testo in chiaro e $N$ bit di testo cifrato: $z_i = x_i \oplus y_i$).

  

Poiché $\Pr[z_i = z_i^2] = \frac{3}{4}$, la keystream pubblica $z_1, \dots, z_N$ che Oscar ha in mano **coincide nel 75% delle posizioni con la sequenza segreta del 2° LFSR** (e nel 75% delle posizioni con la sequenza segreta del 3° LFSR)!

  

Ecco come Oscar recupera l'intera chiave segreta $K = (K^1, K^2, K^3)$ un pezzo alla volta:

  

1. **Attacco isolato al 2° LFSR (per trovare $K^2$):**
    
      
    - Ci sono solo $2^{m_2} - 1$ possibili stati iniziali candidati per il 2° LFSR.
        
          
        
    - Per ciascuno stato iniziale candidato $\tilde{K}^2$, Oscar fa girare il 2° LFSR da solo per $N$ passi, generando una sequenza candidata $\tilde{z}_1^2, \tilde{z}_2^2, \dots, \tilde{z}_N^2$.
        
          
        
    - Oscar confronta bit a bit la sequenza candidata con la vera keystream $z_1, \dots, z_N$ e conta il numero di coincidenze (**matches**), ovvero il numero di indici $1 \le i \le N$ tali che $\tilde{z}_i^2 = z_i$:
        
          
        - Se $\tilde{K}^2$ è **sbagliata**, la sequenza generata si comporta come una stringa casuale rispetto a $z_i$, quindi il numero atteso di match su $N$ bit è circa:
            
              
            
            $$E[\text{matches (chiave errata)}] = \frac{1}{2} N = \mathbf{0.50 \, N}$$
            
        - Se $\tilde{K}^2 = K^2$ è la **chiave iniziale VERA**, poiché $\Pr[z_i = z_i^2] = \frac{3}{4}$, il numero atteso di match su $N$ bit balza a:
            
              
            
            $$E[\text{matches (chiave vera)}] = \frac{3}{4} N = \mathbf{0.75 \, N}$$
            
    - Se $N$ è sufficientemente grande (basta un multiplo modesto della lunghezza $m_2$), la chiave candidata che ottiene una percentuale di match vicina al **75%** si stacca nettamente da tutte le altre (ferme attorno al 50%), svelando $K^2$!
        
          
        
2. **Attacco isolato al 3° LFSR (per trovare $K^3$):**
    
      
    - Esattamente nello stesso modo, poiché $\Pr[z_i = z_i^3] = \frac{3}{4}$, Oscar testa separatamente le $2^{m_3} - 1$ chiavi candidate del 3° LFSR su $N$ bit di keystream e individua la vera chiave $K^3$ come l'unica che produce circa **$0.75 \, N$ match**.
        
          
        
3. **Recupero finale del 1° LFSR (per trovare $K^1$):**
    
      
    - Anche se il 1° LFSR non era correlato con l'uscita ($p_1 = 1/2$), ormai Oscar **conosce già i veri $K^2$ e $K^3$**!
        
          
        
    - Gli basta quindi provare tutte le $2^{m_1} - 1$ possibili chiavi iniziali $\tilde{K}^1$ del 1° LFSR combinandole con i veri $K^2$ e $K^3$ dentro l'intero generatore: la chiave $K^1$ corretta sarà l'unica a riprodurre il **100% dei bit** della keystream osservata!
        
          
        

> [!example] Esempio Numerico Completo del Libro (Sezione 4.8.1)
> 
> Consideriamo un Combination Generator con $r = 3$ LFSR combinati dalla funzione vista sopra (con $p_2 = 3/4$ e $p_3 = 3/4$), aventi lunghezze:
> 
>   
> 
> - **$\text{LFSR}_1$:** grado $m_1 = 5$ $\implies 2^5 - 1 = \mathbf{31}$ possibili stati iniziali $K^1$.
>     
>       
>     
> - **$\text{LFSR}_2$:** grado $m_2 = 7$ $\implies 2^7 - 1 = \mathbf{127}$ possibili stati iniziali $K^2$.
>     
>       
>     
> - **$\text{LFSR}_3$:** grado $m_3 = 9$ $\implies 2^9 - 1 = \mathbf{511}$ possibili stati iniziali $K^3$.
>     
>       
>     
> 
> **1. Confronto del numero di chiavi da testare:**
> 
>   
> 
> - Con una ricerca esaustiva cieca su tutti e tre i registri, Oscar dovrebbe testare:
>     
>       
>     
>     $$31 \times 127 \times 511 = \mathbf{2.011.807 \text{ combinazioni}}$$
>     
> - Con il **Correlation Attack**, Oscar attacca i tre registri separatamente testando in tutto solo:
>     
>       
>     
>     $$127 + 511 + 31 = \mathbf{669 \text{ combinazioni!}}$$
>     
> 
> **2. Risultati sperimentali dell'attacco nel libro:**
> 
>   
> 
> - **Attacco al 2° LFSR ($m_2 = 7$):** Oscar utilizza **$N = 60$ bit** della keystream.
>     
>       
>     - Valore atteso di match per la chiave vera: $\frac{3}{4} \times 60 = \mathbf{45}$ match (contro $\frac{1}{2} \times 60 = 30$ per le chiavi errate).
>         
>           
>         
>     - Provando tutte le $127$ possibili chiavi iniziali a 7 bit, la chiave iniziale **`1100110`** produce **48 match su 60** ($80\%$), mentre nessuna delle altre 126 chiavi candidate supera i 39 match! Quindi $K^2 = \texttt{1100110}$.
>         
>           
>         
> - **Attacco al 3° LFSR ($m_3 = 9$):** Oscar utilizza **$N = 90$ bit** della keystream.
>     
>       
>     - Valore atteso di match per la chiave vera: $\frac{3}{4} \times 90 = \mathbf{67.5}$ match (contro $\frac{1}{2} \times 90 = 45$ per le chiavi errate).
>         
>           
>         
>     - Provando tutte le $511$ possibili chiavi iniziali a 9 bit, la chiave iniziale **`011011001`** produce **67 match su 90** ($74.4\%$), mentre nessuna delle altre 510 chiavi candidate supera i 59 match! Quindi $K^3 = \texttt{011011001}$.
>         
>           
>         
> - **Recupero del 1° LFSR ($m_1 = 5$):** Fissati $K^2 = \texttt{1100110}$ e $K^3 = \texttt{011011001}$, Oscar prova le 31 possibili chiavi a 5 bit per il primo registro e trova immediatamente l'unica che genera l'esatta keystream intercettata.
>     
>       
>     

- **Nota finale sulla progettazione (Immunità alla Correlazione):** Per difendersi da questo attacco, una _combining function_ $f(z_1, \dots, z_r)$ deve essere scelta in modo tale che $\Pr[f(z_1, \dots, z_r) = z_j] = \frac{1}{2}$ per ogni singolo $j$ (e più in generale deve essere _correlation-immune di ordine $k$_, ovvero non deve presentare correlazioni nemmeno con lo XOR di sottoinsiemi di $k$ input contemporaneamente, pur mantenendo un alto grado algebrico non lineare).
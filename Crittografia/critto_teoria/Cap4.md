
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

Sviluppata da Eli Biham e Adi Shamir (1990), la **Crittoanalisi Differenziale** è un attacco di tipo **chosen-plaintext** (a testo in chiaro scelto) applicato ai cifrari a blocchi iterati.

### 4.4.1 Definizione del Modello di Attacco (secondo Stinson) e Invarianza dello XOR

Nella crittoanalisi differenziale si assume che l'attaccante abbia un gran numero di tuple $(x, x^*, y, y^*)$, in cui il valore dello XOR tra i testi in chiaro $x' = x \oplus x^*$ è fisso e noto. Gli elementi di testo in chiaro ($x$ e $x^*$) vengono cifrati utilizzando la medesima chiave segreta $K$, producendo rispettivamente i testi cifrati $y$ e $y^*$.

Per ciascuna di queste tuple, l'attaccante procede come segue:
1. **Decifratura parziale dell'ultimo round:** Si inizia a decifrare a ritroso i testi cifrati $y$ e $y^*$ (limitatamente all'ultimo round del cifrario) provando tutte le possibili **chiavi candidate** (*candidate keys*) per le S-box attive dell'ultimo round.
2. **Verifica della differenza sullo stato intermedio e incremento dei contatori:** Per ciascuna chiave candidata, si calcolano i valori di determinati bit dello stato intermedio (l'ingresso $u^{N_r}$ alle S-box dell'ultimo round) e si verifica se il loro XOR ($u'^{N_r} = u^{N_r} \oplus (u^{N_r})^*$) coincide con un valore specifico, ovvero il valore più probabile previsto dalla traccia differenziale per il dato XOR di input $x'$. Ogni volta che tale condizione si verifica, si incrementa di $1$ un contatore associato a quella specifica chiave candidata.
3. **Individuazione della sottochiave corretta:** Al termine del processo su tutte le tuple, ci si aspetta che la chiave candidata che ha accumulato il conteggio di frequenza più elevato contenga i valori corretti per i bit della sottochiave dell'ultimo round.

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

Per estendere l'analisi da una singola S-box all'intero cifrario (es. sui primi $N_r - 1$ round), **concateniamo i rapporti di propagazione di modo che le differenze di input e output delle S-box attive** (perchè sono le uniche che hanno un'influenza probabilistica) round dopo round in modo che **l'uscita permutata del round $r$**, cioè $w'^r = \pi_P(v'^r)$, **coincida esattamente con l'ingresso $u'^{r+1}$ del round $r+1$**. Questa **sequenza concatenata di differenziali** si chiama **traccia differenziale** (_differential trail_ o _characteristic_).

  

- **Assunzione di Indipendenza e Moltiplicazione dei Rapporti di Propagazione:** Assumendo che le differenze in ingresso alle varie S-box attive lungo la traccia si comportino come eventi statisticamente indipendenti (e fissando le sottochiavi), il **rapporto di propagazione complessivo $R_p$ di una traccia differenziale** su $N_r - 1$ round è dato dal **prodotto** dei rapporti di propagazione delle singole S-box attive coinvolte nella traccia:
    
      
    
    $$R_p = \prod_{\text{S-box attive } S_i^r} R_p(u'^r_{(i)}, v'^r_{(i)})$$
    
    _(Nota: per le S-box passive, dove $0000 \to 0000$, vale $R_p(0, 0) = 16/16 = 1$, quindi non influiscono sul prodotto e per massimizzare $R_p$ l'attaccante cerca tracce con il minor numero possibile di S-box attive!)_.
    
      
    

> [!example] Example 4.7 (Costruzione della Traccia Differenziale a 3 Round con $R_p = 27/1024$)
> 
> Costruiamo la traccia differenziale sui primi **3 round** dell'SPN dell'Example 4.1 che attiva in totale solo **4 S-box**: **$S_2^1$** nel Round 1, **$S_3^2$** nel Round 2, e **$S_2^3, S_3^3$** nel Round 3:
> 
> 1. **Scelta del Differenziale del Plaintext ($x'$):**
>    Scegliamo coppie di testi in chiaro $(x, x^*)$ aventi differenza iniziale:
>    $$x' = u'^1 = \texttt{0000 1011 0000 0000}_2 = \mathbf{\texttt{0B00}_{16}}$$
>     
>    
>     
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

- **Pro:** È completamente **parallelizzabile** (cifratura e decifratura simultanea di più blocchi) sia in cifratura che in decifratura, e un errore di trasmissione su $y_j$ corrompe solo il blocco $x_j$.
    
      
    
- **Contro (Perché NON va mai usato):** Se due blocchi di testo in chiaro sono identici ($x_i = x_j$), producono esattamente **lo stesso blocco di testo cifrato** ($y_i = y_j$).
    
      
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

| **Caratteristica**                    | **ECB**                | **CBC**                            | **CTR**                          |     |     |
| ------------------------------------- | ---------------------- | ---------------------------------- | -------------------------------- | --- | --- |
| **Tipo di schema**                    | Block Cipher puro      | Block Cipher incatenato            | Stream Cipher sincrono           |     |     |
| **Nasconde i pattern ($x_i = x_j$)?** | ❌ **NO** ($y_i = y_j$) | ✅ Sì (grazie a $IV$ e chaining)    | ✅ Sì (grazie al contatore $T_j$) |     |     |
| **Cifratura parallelizzabile?**       | ✅ Sì                   | ❌ **NO** (sequenziale)             | ✅ **Sì** (100% + precomputabile) |     |     |
| **Decifratura parallelizzabile?**     | ✅ Sì                   | ✅ **Sì**                           | ✅ **Sì** (100% + precomputabile) |     |     |
| **Richiede funzione inversa $d_K$?**  | Sì                     | Sì                                 | ❌ **NO** (usa solo $e_K$!)       |     |     |
| **Richiede Padding?**                 | Sì                     | Sì (vulnerabile a Padding Oracle!) | ❌ **NO**                         |     |     |

## 4.7.1 Padding Oracle Attack sulla Modalità CBC

Scoperto da **Serge Vaudenay nel 2002**, il **Padding Oracle Attack** è uno degli attacchi pratici più devastanti della crittografia moderna. Dimostra come un attaccante (Oscar), senza conoscere la chiave segreta $K$, possa **decifrare completamente qualsiasi blocco cifrato in modalità CBC** sfruttando semplicemente il messaggio di errore (`"Padding valido"` vs `"Errore di padding"`) restituito da un server!

  

### A. Lo Schema di Padding Standard (PKCS #7)

Supponiamo che il cifrario operi su blocchi di **$B$ byte** (es. $B = 16$ byte per AES, o $B = 8$ byte nei vecchi cifrari). Per fare in modo che il messaggio in chiaro abbia sempre una lunghezza multipla esatta di $B$ byte e che Bob, dopo la decifratura, sappia esattamente **quanti byte di padding rimuovere**, lo standard **PKCS #7** usa la seguente regola:

  

1. Se l'ultimo blocco del messaggio originale contiene $B - b$ byte di dati (con $1 \le b \le B$), mancano esattamente **$b$ byte** per completare il blocco da $B$ byte.
    
      
    
2. Si aggiungono in coda esattamente **$b$ byte di valore $b$** (scritto in esadecimale):
    
      
    - Se manca **1 byte** ($b=1$): il blocco deve terminare con **`01`**.
        
          
        
    - Se mancano **2 byte** ($b=2$): il blocco deve terminare con **`02 02`**.
        
          
        
    - Se mancano **3 byte** ($b=3$): il blocco deve terminare con **`03 03 03`**.
        
          
        
    - $\dots$
        
          
        
    - Se il messaggio originale è già un multiplo esatto di $B$ byte ($b = B$): si aggiunge un **intero nuovo blocco fittizio di $B$ byte** tutti uguali a $B$ (es. sedici byte `10 10 ... 10` in esadecimale per $B=16$), altrimenti Bob non saprebbe distinguere i dati veri dal padding!
        
          
        

Quando il server (Bob) riceve un ciphertext in modalità CBC, lo decifra e controlla gli ultimi byte dell'ultimo blocco $x_t$: se non rispettano il formato PKCS #7 (ad esempio se l'ultimo byte è `02`, ma il penultimo byte non è `02`), il server scarta il pacchetto e restituisce un errore di **Padding Invalido**.

  

### B. Il Modello dell'Attacco: Cos'è il "Padding Oracle"?

Supponiamo che esista un oracolo (**Padding Oracle**) a cui Oscar può inviare qualsiasi coppia di blocchi cifrati $(y_0, y_1)$ in modalità CBC (un attacco di tipo _chosen-ciphertext_ adattivo). Oracolo decifra $(y_0, y_1)$ con la sua chiave segreta $K$ calcolando:

  

$$x_1 = d_K(y_1) \oplus y_0$$

e controlla se $x_1$ termina con un padding PKCS #7 valido:

  

- Restituisce **`VALID` (1)** se il padding di $x_1$ è formalmente corretto (es. finisce con `01`, oppure con `02 02`, oppure con `03 03 03`, ecc.).
    
      
    
- Restituisce **`INVALID` (0)** se il padding è errato.
    
      
    

L'oracolo **non rivela mai il testo decifrato**, ma quel singolo bit di risposta (`VALID` / `INVALID`) basta a Oscar per decifrare l'intero blocco $x_1$ byte per byte senza conoscere $K$!

  

### C. Meccanica Matematica dell'Attacco Passo-Passo

Supponiamo che Oscar abbia intercettato due blocchi consecutivi $(y_0, y_1)$ (dove $y_0$ può essere l'$IV$ o un blocco cifrato precedente $y_{j-1}$, e $y_1$ è il blocco bersaglio $y_j$) e voglia scoprire tutti i $B$ byte del blocco in chiaro:

  

$$x_1 = (x_{1,1}, x_{1,2}, \dots, x_{1,B}) = d_K(y_1) \oplus y_0$$

Indichiamo i $B$ byte del blocco $y_0$ con $(y_{0,1}, y_{0,2}, \dots, y_{0,B})$. Per la formula di decifratura CBC, per ogni singolo byte $i \in \{1, \dots, B\}$ vale:

  

$$x_{1,i} = d_K(y_1)_i \oplus y_{0,i} \quad \Longleftrightarrow \quad d_K(y_1)_i = x_{1,i} \oplus y_{0,i}$$

#### FASE 1: Scoprire l'ultimo byte $x_{1,B}$ (forzando il padding `01`)

Oscar costruisce un blocco modificato $w = (r_1, r_2, \dots, r_{B-1}, i)$ in cui i primi $B-1$ byte sono scelti a caso e l'ultimo byte $i$ varia da $0$ a $255$ ($\texttt{00}_{16}, \dots, \texttt{FF}_{16}$), e invia al Padding Oracle la coppia **$(w, y_1)$**:

  

1. Oracolo decifra $y_1$ ottenendo il blocco in chiaro modificato:
    
      
    
    $$x'_1 = d_K(y_1) \oplus w$$
    
1. Guardiamo cosa succede all'**ultimo byte** $x'_{1,B}$ di questo blocco decifrato dall'oracolo:
    
    Poiché $d_K(y_1)_B = x_{1,B} \oplus y_{0,B}$, sostituendo otteniamo l'equazione fondamentale dell'attacco:
    
      
    
    $$x'_{1,B} = d_K(y_1)_B \oplus i = x_{1,B} \oplus y_{0,B} \oplus i$$
    
2. Al variare di $i \in \{0, 1, \dots, 255\}$, il byte $x'_{1,B}$ assume tutti i 256 valori possibili esattamente una volta!
    
    Quando il tentativo $i$ scelto da Oscar fa sì che l'ultimo byte diventi esattamente **`01`** ($x'_{1,B} = \texttt{01}_{16}$), l'oracolo vede un blocco che termina con `01` e risponde **`VALID`**!
    
      
    
3. Non appena il server risponde `VALID` per un certo valore $i$, Oscar sa che:
    
      
    
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
    
    (così gli ultimi $k-1$ byte decifrati dall'oracolo valgono già tutti $k$).
    
      
    
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


Ecco la riscrittura completa della sezione **4.8 Stream Ciphers** e della sottosezione **4.8.1 Correlation Attack on a Combination Generator**, redatta seguendo **esclusivamente** la terminologia, le definizioni, i simboli ($L_1, L_2, L_3, L$, ecc.) e gli esempi (incluso l'**Example 4.5** con la **Table 4.6**) presenti nel libro di Stinson (_Cryptography: Theory and Practice_).

  

Sono stati rimossi tutti i termini esterni non usati in questa sezione dal libro (come _seed_, _Geffe generator_, _multiplexer_, _correlation-immune_, _ciclo di clock_, _polinomio primitivo_, ecc.).

  

  

  

## 4.8 Stream Ciphers

  

  

Abbiamo introdotto gli **stream ciphers** nella Sezione 2.1.7, dove abbiamo menzionato l'uso di un **linear feedback shift register (LFSR)** come possibile tecnica per generare un **keystream**. Tuttavia, un singolo LFSR non produce uno stream cipher sicuro, come mostrato nella Sezione 2.2.5 (poiché tutte le operazioni sono lineari, è vulnerabile a un **known-plaintext attack** risolvendo un sistema di equazioni lineari).

  

Nonostante ciò, l'idea di utilizzare gli LFSR per costruire stream ciphers rimane molto attraente grazie all'efficienza degli LFSR e al fatto che possono avere un **large period** (periodo molto lungo). Sono state quindi proposte varie tecniche per "combinare" gli LFSR in modo da ottenere uno stream cipher efficiente e sicuro. Invece di prendere direttamente l'output di un LFSR come keystream, si produce un keystream a partire da un certo numero (uno o più di uno) di LFSR utilizzando un'opportuna **boolean function** (funzione booleana) o qualche altro meccanismo.

  

Tre dei metodi più comuni per fare questo sono i seguenti:

  

- **combination generator**,
    
      
    
- **filter generator**, e
    
      
    
- **shrinking generator**.
    
      
    

Ecco le descrizioni di questi generatori così come presentate nel libro:

  

1. **Combination generator:** In un **combination generator**, abbiamo un certo numero, diciamo $r$, di LFSR. Supponiamo che il $j$-esimo LFSR generi il keystream $z_1^j, z_2^j, \dots$. L'idea di base è usare una **boolean function** $f : (\mathbb{Z}_2)^r \to \mathbb{Z}_2$ per combinare gli $r$ keystreams in un nuovo keystream $z_1 z_2 \dots$, tramite la regola:
    
      
    
    $$z_i = f(z_i^1, \dots, z_i^r), \qquad i = 1, 2, \dots$$
    
    La funzione $f$ è chiamata **combining function**. Si noti che è desiderabile che gli $r$ LFSR abbiano periodi che siano **pairwise relatively prime** (coprimi a due a due): questo assicurerà che l'input alla _combining function_ abbia il periodo più lungo possibile (ovvero, il prodotto dei periodi degli $r$ LFSR).
    
      
    
2. **Filter generator:** In un **filter generator**, utilizziamo un singolo LFSR, avente diciamo $m$ **stages** (stadi). Ma invece di prendere come bit del keystream i bit che vengono prodotti dall'LFSR, applichiamo una **boolean function** (avente $m$ input, chiamata in seguito anche **filtering function** o **filter function**) all'intero **state** (stato) di $m$ bit dell'LFSR. L'output della funzione booleana in qualsiasi istante dato costituisce un bit del keystream.
    
      
    
3. **Shrinking generator:** In uno **shrinking generator**, utilizziamo due LFSR. I bit del keystream sono ottenuti dal primo LFSR. Tuttavia, alcuni di questi bit vengono scartati (**discarded**), a seconda dell'output del secondo LFSR:
    
      
    - Se il secondo LFSR dà in output uno `0`, allora l'output del primo LFSR viene scartato (_discarded_);
        
          
        
    - Se il secondo LFSR dà in output un `1`, allora l'output del primo LFSR diventa il successivo bit del keystream.
        
          
        

  

  

## 4.8.1 Correlation Attack on a Combination Generator

  

  

In questa sezione descriviamo un attacco al **combination generator**, noto come **correlation attack**. Questo attacco può essere condotto quando esistono **correlations** (correlazioni) tra gli output degli LFSR (che sono gli input della _combining function_) e l'output della _combining function_.

  

### 1. Analisi della Combining Function e delle Correlazioni

Supponiamo di avere $r = 3$ LFSR e che la **combining function** sia:

  

$$f(z_1, z_2, z_3) = (z_1 \wedge z_2) \oplus (z_2 \wedge z_3) \oplus z_3$$

(dove $\wedge$ indica la congiunzione logica AND e $\oplus$ indica l'_exclusive-or_). La **truth table** (tabella di verità) per la funzione booleana $f$ è data da:

  

|**z1​**|**z2​**|**z3​**|**f(z1​,z2​,z3​)**|
|---|---|---|---|
|`0`|`0`|`0`|`0`|
|`0`|`0`|`1`|`1`|
|`0`|`1`|`0`|`0`|
|`0`|`1`|`1`|`0`|
|`1`|`0`|`0`|`0`|
|`1`|`0`|`1`|`1`|
|`1`|`1`|`0`|`1`|
|`1`|`1`|`1`|`1`|

Se trattiamo $z_1, z_2, z_3$ come **independent, uniformly distributed random binary variables** (variabili binarie aleatorie indipendenti e uniformemente distribuite, tali che $\Pr[z_j = 0] = \Pr[z_j = 1] = 1/2$ per $j = 1, 2, 3$), allora ciascuna delle 8 righe della tabella di verità si verifica con probabilità $1/8$, e anche l'output $z = f(z_1, z_2, z_3)$ assume i valori `0` e `1` con probabilità $1/2$.

  

Tuttavia, confrontando la colonna di output $z = f(z_1, z_2, z_3)$ con ciascuna delle colonne di input $z_1, z_2, z_3$ nelle 8 righe della tabella, osserviamo che per tutti e tre gli input vale:

  

$$\Pr[z = z_j] = \frac{3}{4}, \qquad \text{per } j = 1, 2, 3$$

(Infatti: $z = z_1$ in 6 righe su 8; $z = z_2$ in 6 righe su 8; $z = z_3$ in 6 righe su 8). È proprio possibile utilizzare questa **correlation** per cercare la **initial key** (chiave iniziale) per ciascuno dei tre LFSR.

  

### 2. Modello dell'Attacco: Brute Force Search vs Correlation Attack ("Divide-and-Conquer")

Per rendere preciso l'attacco, facciamo le seguenti assunzioni (come nel libro):

  

- I tre LFSR (ovvero le **linear recurrence relations**) sono noti.
    
      
    
- La **combining function** $f$ è nota.
    
      
    
- La **key** (chiave) consiste quindi negli **initial states** (stati iniziali, chiamati anche **initial keys** o **initial keystream bits**) dei tre LFSR componenti.
    
      
    
- Supponiamo che il $j$-esimo LFSR corrisponda a una _linear recurrence_ di **degree** $L_j$ (per $j = 1, 2, 3$). Allora la chiave per lo stream cipher risultante ha lunghezza totale:
    
      
    
    $$L = L_1 + L_2 + L_3$$
    

Come nella Sezione 2.2.5, consideriamo un **known plaintext attack**, il quale ci permette immediatamente di calcolare i **keystream bits**. L'obiettivo è determinare gli $L$ **initial keystream bits**:

  

1. **Confronto con la Brute Force Search:** A scopo di confronto, osserviamo che c'è sempre l'opzione di effettuare una **brute force search** per la chiave. Per ciascuna possibile **L-bit key**, possiamo generare un keystream usando i tre LFSR insieme alla _combining function_ data. Se il keystream generato è identico al keystream che abbiamo determinato dal _known plaintext attack_, allora possiamo essere certi di aver trovato la chiave corretta. Poiché si tratta di una _brute force search_, nel caso peggiore (_worst case_) potremmo dover considerare tutte le:
    
      
    
    $$2^L = 2^{L_1} \times 2^{L_2} \times 2^{L_3}$$
    
    chiavi (o sequenze) fino a trovare quella corretta. Se $L$ è sufficientemente grande, questo potrebbe non essere fattibile.
    
      
    
2. **Strategia del Correlation Attack ("Divide-and-Conquer"):** Sfruttando le correlazioni tra gli input di $f$ e il suo output, possiamo rendere la ricerca molto più efficiente. Le correlazioni ci permettono di cercare l'**initial state** di ciascun LFSR **separatamente** (per questo motivo ci si riferisce talvolta a questo metodo come a un **"divide-and-conquer" attack**):
    
      
    - Supponiamo di concentrarci sul primo LFSR e di tirare a indovinare (_guess_) un keystream iniziale consistente di $L_1$ bit.
        
          
        
    - Generiamo quindi una sequenza di bit usando questo LFSR e la confrontiamo con la sequenza degli **actual keystream bits** (i veri bit del keystream).
        
          
        
    - Se la **guessed initial key** (chiave iniziale ipotizzata) è **corretta**, allora ci aspettiamo che il **75%** dei bit generati dall'LFSR coincida (**agree**) con il keystream (poiché $\Pr[z = z_1] = 3/4$).
        
          
        
    - Se invece la **guessed initial key** è **errata**, allora ci aspettiamo che il **50%** dei bit generati dall'LFSR coincida con il keystream.
        
          
        
    - La strategia consiste quindi nel considerare tutte le $2^{L_1}$ possibili _initial keys_ (o più precisamente le $2^{L_1} - 1$ possibili _nonzero initial keys_) per questo LFSR e, per ciascuna _initial key_, generare un flusso di bit, tenendo traccia di quale flusso di bit corrisponde più da vicino (_most closely matches_) ai veri bit del keystream. Se disponiamo di un numero sufficiente di bit del keystream, possiamo essere molto fiduciosi che questa _initial key_ sia davvero quella corretta.
        
          
        
3. **Costo Computazionale dell'Attacco:** Effettuando una **exhaustive search** sui $2^{L_1}$ possibili stati iniziali, siamo in grado di determinare $L_1$ bit della chiave. Possiamo ripetere questo attacco per il secondo e per il terzo LFSR e ottenere così l'intera chiave di $L$ bit. Il calcolo totale richiesto da questo attacco può essere stimato in:
    
      
    
    $$2^{L_1} + 2^{L_2} + 2^{L_3}$$
    
    poiché gli attacchi sui tre LFSR vengono condotti separatamente. Questo valore è molto più piccolo rispetto al _brute force attack_ che richiede approssimativamente $2^L = 2^{L_1} \times 2^{L_2} \times 2^{L_3}$ sequenze da testare nel caso peggiore.
    
      
    - **Confronto concreto con parametri particolari:** Supponiamo $L_1 = 19, L_2 = 21$ e $L_3 = 23$. Allora la _brute force search_ richiede di testare $2^{63}$ possibili chiavi (un numero molto grande), mentre il _correlation attack_ testa solamente $2^{19} + 2^{21} + 2^{23} < 2^{24}$ chiavi, il che può essere fatto molto velocemente.
        
          
        

  

  

### 3. Esempio Pratico Completo dal Libro (Example 4.5)

  

  

> [!example] Example 4.5 (Correlation Attack su 3 LFSR con $L_1 = 5, L_2 = 7, L_3 = 9$) Supponiamo di avere tre LFSR, con $L_1 = 5, L_2 = 7$ e $L_3 = 9$ (quindi la chiave complessiva è una **21-bit key**, con $L = 5 + 7 + 9 = 21$). Questi LFSR implementano rispettivamente le seguenti **linear recurrence relations**:
> 
>   
> 
> $$\begin{aligned} > a_i &= a_{i-3} + a_{i-5} \\ > b_i &= b_{i-6} + b_{i-7} \\ > c_i &= c_{i-5} + c_{i-9} > \end{aligned}$$
> 
> dove tutta l'aritmetica è modulo 2. Supponiamo di aver ottenuto i seguenti **90 bit del keystream** da un _known plaintext attack_:
> 
>   
> 
> Plaintext
> 
> ```
> 011011001010000111101100000110
> 001111100101000111110100010111
> 001100110010100001001111000100
> ```
> 
> **Passo 1: Attacco al primo LFSR ($L_1 = 5$)** Iniziamo confrontando i primi **30 bit** del keystream con i 30 bit generati dal primo LFSR usando le $2^5 - 1 = 31$ possibili diverse **nonzero initial keys**. Per ciascuna _bitstring_ generata dall'LFSR, contiamo il **number of agreements** (numero di concordanze / **matches**) con il **true keystream** (vero keystream), ottenendo i dati presentati nella **Table 4.6** del libro:
> 
>   
> 
> **TABLE 4.6: Possible keystreams (per il 1° LFSR su 30 bit)**
> 
>   
> 
> |**Initial key (primi 5 bit)**|**Bitstring di 30 bit generata dal 1° LFSR**|**Agreements (su 30)**|
> |---|---|---|
> |`00001`|`000010010110011111000110111010`|15|
> |`00010`|`000100101100111110001101110101`|12|
> |`00011`|`000110111010100001001011001111`|15|
> |`00100`|`001001011001111100011011101010`|12|
> |`00101`|`001011001111100011011101010000`|19|
> |`00110`|`001101110101000010010110011111`|12|
> |`00111`|`001111100011011101010000100101`|15|
> |`01000`|`010000100101100111110001101110`|15|
> |`01001`|`010010110011111000110111010100`|12|
> |`01010`|`010100001001011001111100011011`|15|
> |`01011`|`010110011111000110111010100001`|16|
> |`01100`|`011001111100011011101010000100`|19|
> |**`01101`**|**`011011101010000100101100111110`**|**24**|
> |`01110`|`011101010000100101100111110001`|15|
> |`01111`|`011111000110111010100001001011`|16|
> |`10000`|`100001001011001111100011011101`|16|
> |`10001`|`100011011101010000100101100111`|15|
> |`10010`|`100101100111110001101110101000`|12|
> |`10011`|`100111110001101110101000010010`|15|
> |`10100`|`101000010010110011111000110111`|16|
> |`10101`|`101010000100101100111110001101`|15|
> |`10110`|`101100111110001101110101000010`|16|
> |`10111`|`101110101000010010110011111000`|11|
> |`11000`|`110001101110101000010010110011`|11|
> |`11001`|`110011111000110111010100001001`|16|
> |`11010`|`110101000010010110011111000110`|19|
> |`11011`|`110111010100001001011001111100`|12|
> |`11100`|`111000110111010100001001011001`|11|
> |`11101`|`111010100001001011001111100011`|16|
> |`11110`|`111100011011101010000100101100`|15|
> |`11111`|`111110001101110101000010010110`|16|
> 
> Per ciascuna riga della Table 4.6, i primi cinque bit costituiscono la **initial key** per l'LFSR. Osserviamo che la _initial key_ **`01101`** genera una _bitstring_ che concorda (_agrees_) con il keystream in **24 bit (su 30)**, mentre nessun'altra _initial key_ genera una _bitstring_ che concorda con il keystream in più di 19 bit. Pertanto sospettiamo fortemente che **`01101`** sia la _initial key_ per il primo LFSR.
> 
>   
> 
> **Passo 2: Attacco al secondo ($L_2 = 7$) e al terzo LFSR ($L_3 = 9$)** Possiamo ripetere questo processo per gli altri due LFSR. È consigliabile svolgere questi calcoli con più bit del keystream, poiché il numero di possibili _initial keys_ è maggiore (per la precisione, il numero di _nonzero initial keys_ è $2^7 - 1 = 127$ e $2^9 - 1 = 511$, rispettivamente, per gli ultimi due LFSR). Supponiamo di usare **60 keystream bits** per attaccare il secondo LFSR e **90 keystream bits** per attaccare il terzo LFSR:
> 
>   
> 
> - **Per il secondo LFSR:** la _initial key_ **`1100110`** produce **48 matches (su 60 bit)**, mentre nessun'altra possibile _initial key_ produce più di 39 matches.
>     
>       
>     
> - **Per il terzo LFSR:** osserviamo un tipo simile di "separazione" (_separation_). La _initial key_ **`011011001`** produce **67 matches (su 90 bit)**, ma nessun'altra possibile _initial key_ produce più di 59 matches.
>     
>       
>     
> 
> **Passo 3: Verifica finale della 21-bit key** Avendo identificato quelle che riteniamo essere le tre componenti della **21-bit key**, è una buona verifica controllare di avere davvero la chiave corretta. Ciò si fa facilmente usando il generatore per calcolare i bit del keystream e confrontandoli poi con i **true keystream bits** ottenuti dal _known plaintext attack_. Se abbiamo davvero la _21-bit key_ corretta, i due keystreams devono essere identici. In questo esempio, possiamo confermare che il keystream corretto si ottiene dalle tre _initial keys_ che abbiamo identificato (`01101`, `1100110`, `011011001`).
> 
>   

  

  

### 4. Numero di Keystream Bits Richiesti per il Successo dell'Attacco

  

  

Tecniche della teoria della probabilità possono essere utilizzate per predire quanti **keystream bits** sono richiesti affinché l'attacco abbia successo con alta probabilità. In generale, il numero di bit del keystream richiesti dipenderà dalla **correlation** (una correlazione più alta corrisponde a un minor numero di bit del keystream richiesti) e dal **degree of the recurrence relations** (ovvero il numero di _stages_ negli LFSR). LFSR più grandi richiederanno solitamente più bit del keystream.

  

È stato suggerito che un attacco su un LFSR avente $L_i$ _stages_ avrà successo se il numero di bit del keystream, $N$, è almeno:

  

$$N \ge \frac{L_i}{\left(p - \frac{1}{2}\right)^2}$$

dove $p$ è la **predicted correlation** (correlazione predetta). Si noti che l'Example 4.5 ha avuto successo anche con un numero inferiore di bit del keystream (infatti per $p = 3/4$, il denominatore vale $(3/4 - 1/2)^2 = 1/16$, per cui la formula suggerirebbe $N \ge 16 L_i$, ovvero $80, 112$ e $144$ bit rispettivamente per $L_1=5, L_2=7, L_3=9$, mentre nell'esempio sono bastati $30, 60$ e $90$ bit).

## Esercizio 3.4

> [!question] Testo dell'Esercizio 3.4 Sia $\mathcal{P} = \{a, b\}$, $\mathcal{K} = \{K_1, K_2, K_3, K_4, K_5\}$ e $\mathcal{C} = \{1, 2, 3, 4, 5\}$. Supponiamo che le funzioni di cifratura siano rappresentate dalla seguente matrice di cifratura:
> 
>   
> 
> |**Chiave**|**a**|**b**|
> |---|---|---|
> |**$K_1$**|$1$|$2$|
> |**$K_2$**|$2$|$3$|
> |**$K_3$**|$3$|$1$|
> |**$K_4$**|$4$|$5$|
> |**$K_5$**|$5$|$4$|
> 
> Scegliendo due numeri reali positivi $\alpha$ e $\beta$ tali che $\alpha + \beta = 1$, definiamo le probabilità delle chiavi come:
> 
>   
> 
> $$\Pr[K_1] = \Pr[K_2] = \Pr[K_3] = \frac{\alpha}{3} \qquad \text{e} \qquad \Pr[K_4] = \Pr[K_5] = \frac{\beta}{2}$$
> 
> Dimostrare che questo crittosistema raggiunge la **segretezza perfetta**.
> 
>   

### Svolgimento e Dimostrazione

Per dimostrare che il crittosistema gode di segretezza perfetta ($\Pr[x \mid y] = \Pr[x]$ per ogni $x \in \mathcal{P}$ e $y \in \mathcal{C}$), utilizziamo la condizione equivalente ricavata tramite il Teorema di Bayes (valida poiché $\alpha, \beta > 0$ garantisce $\Pr[y] > 0$ per ogni $y \in \mathcal{C}$):

  

$$\Pr[y \mid a] = \Pr[y \mid b] \quad \forall y \in \{1, 2, 3, 4, 5\}$$

Infatti, se $\Pr[y \mid a] = \Pr[y \mid b]$ per un dato $y$, allora per la legge della probabilità totale si ha:

  

$$\Pr[y] = \Pr[a]\Pr[y \mid a] + \Pr[b]\Pr[y \mid b] = \Pr[y \mid a](\Pr[a] + \Pr[b]) = \Pr[y \mid a] \cdot 1 = \Pr[y \mid a] = \Pr[y \mid b]$$

da cui segue immediatamente $\Pr[x \mid y] = \frac{\Pr[x]\Pr[y \mid x]}{\Pr[y]} = \Pr[x]$.

  

Calcoliamo dunque $\Pr[y \mid x] = \sum_{\{K : e_K(x) = y\}} \Pr[K]$ leggendo direttamente le colonne $a$ e $b$ della matrice di cifratura per ciascun testo cifrato $y \in \{1, 2, 3, 4, 5\}$:

  

1. **Per $y = 1$:**
    
      
    - Nella colonna di $a$, il simbolo $1$ compare solo nella riga $K_1$: $\Pr[1 \mid a] = \Pr[K_1] = \frac{\alpha}{3}$.
        
          
        
    - Nella colonna di $b$, il simbolo $1$ compare solo nella riga $K_3$: $\Pr[1 \mid b] = \Pr[K_3] = \frac{\alpha}{3}$.
        
          
        
    - Quindi $\Pr[1 \mid a] = \Pr[1 \mid b] = \Pr[1] = \mathbf{\frac{\alpha}{3}}$.
        
          
        
2. **Per $y = 2$:**
    
      
    - Nella colonna di $a$, il $2$ compare con $K_2$: $\Pr[2 \mid a] = \Pr[K_2] = \frac{\alpha}{3}$.
        
          
        
    - Nella colonna di $b$, il $2$ compare con $K_1$: $\Pr[2 \mid b] = \Pr[K_1] = \frac{\alpha}{3}$.
        
          
        
    - Quindi $\Pr[2 \mid a] = \Pr[2 \mid b] = \Pr[2] = \mathbf{\frac{\alpha}{3}}$.
        
          
        
3. **Per $y = 3$:**
    
      
    - Nella colonna di $a$, il $3$ compare con $K_3$: $\Pr[3 \mid a] = \Pr[K_3] = \frac{\alpha}{3}$.
        
          
        
    - Nella colonna di $b$, il $3$ compare con $K_2$: $\Pr[3 \mid b] = \Pr[K_2] = \frac{\alpha}{3}$.
        
          
        
    - Quindi $\Pr[3 \mid a] = \Pr[3 \mid b] = \Pr[3] = \mathbf{\frac{\alpha}{3}}$.
        
          
        
4. **Per $y = 4$:**
    
      
    - Nella colonna di $a$, il $4$ compare con $K_4$: $\Pr[4 \mid a] = \Pr[K_4] = \frac{\beta}{2}$.
        
          
        
    - Nella colonna di $b$, il $4$ compare con $K_5$: $\Pr[4 \mid b] = \Pr[K_5] = \frac{\beta}{2}$.
        
          
        
    - Quindi $\Pr[4 \mid a] = \Pr[4 \mid b] = \Pr[4] = \mathbf{\frac{\beta}{2}}$.
        
          
        
5. **Per $y = 5$:**
    
      
    - Nella colonna di $a$, il $5$ compare con $K_5$: $\Pr[5 \mid a] = \Pr[K_5] = \frac{\beta}{2}$.
        
          
        
    - Nella colonna di $b$, il $5$ compare con $K_4$: $\Pr[5 \mid b] = \Pr[K_4] = \frac{\beta}{2}$.
        
          
        
    - Quindi $\Pr[5 \mid a] = \Pr[5 \mid b] = \Pr[5] = \mathbf{\frac{\beta}{2}}$.
        
          
        

Poiché per ogni $y \in \mathcal{C}$ e per ogni $x \in \mathcal{P}$ vale $\Pr[y \mid x] = \Pr[y]$, il Teorema di Bayes restituisce $\Pr[x \mid y] = \Pr[x]$. Il crittosistema gode pertanto di **segretezza perfetta** (anche se le chiavi non sono equiprobabili, in quanto qui $\vert{}\mathcal{K}\vert{} = \vert{}\mathcal{C}\vert{} = 5 > \vert{}\mathcal{P}\vert{} = 2$). $\blacksquare$

  

## Esercizio 3.6

> [!question] Testo dell'Esercizio 3.6 Supponiamo che un crittosistema raggiunga la segretezza perfetta per una particolare distribuzione di probabilità sui testi in chiaro ($\mathcal{P}$). Dimostrare che la segretezza perfetta viene mantenuta per **qualsiasi** distribuzione di probabilità sui testi in chiaro.
> 
>   

### Svolgimento e Dimostrazione

1. **Ipotesi iniziale sulla distribuzione particolare $\Pr_1$:** Sia $\Pr_1[\mathbf{P} = x]$ (con $\Pr_1[x] > 0$ per ogni $x \in \mathcal{P}$) la particolare distribuzione di probabilità sui testi in chiaro per la quale il crittosistema raggiunge la segretezza perfetta, mantenendo fissa la distribuzione delle chiavi $\Pr[\mathbf{K} = K]$. Per definizione di segretezza perfetta e per l'equivalenza di Bayes vista nella Sezione 3.2:
    
      
    
    $$\Pr_1[x \mid y] = \Pr_1[x] \quad \forall x \in \mathcal{P}, y \in \mathcal{C} \quad \Longleftrightarrow \quad \Pr_1[y \mid x] = \Pr_1[y] \quad \forall x \in \mathcal{P}, y \in \mathcal{C}$$
    
    Questo significa che, fissato un qualsiasi testo cifrato $y \in \mathcal{C}$, la quantità $\Pr_1[y \mid x]$ ha lo **stesso valore costante** (che chiamiamo $c_y = \Pr_1[y]$) indipendentemente da quale elemento $x \in \mathcal{P}$ venga scelto:
    
      
    
    $$\Pr_1[y \mid x] = c_y \quad \forall x \in \mathcal{P}$$
    
2. **Indipendenza di $\Pr[y \mid x]$ dalla distribuzione del plaintext:**
    
    Osserviamo come è definita matematicamente la probabilità condizionata $\Pr[y \mid x]$:
    
      
    
    $$\Pr[y \mid x] = \sum_{\{K \in \mathcal{K} : e_K(x) = y\}} \Pr[\mathbf{K} = K]$$
    
    Questa somma dipende **esclusivamente** dalle funzioni di cifratura $e_K$ e dalla distribuzione di probabilità sulle chiavi $\Pr[\mathbf{K} = K]$, e **non dipende in alcun modo** dalla distribuzione di probabilità scelta su $\mathcal{P}$!
    
      
    
3. **Passaggio a una qualsiasi altra distribuzione $\Pr_2$ su $\mathcal{P}$:** Consideriamo ora un'arbitraria distribuzione di probabilità $\Pr_2[\mathbf{P} = x]$ definita su $\mathcal{P}$. Poiché $\Pr[y \mid x]$ non cambia al variare della distribuzione sul plaintext, per ogni $x \in \mathcal{P}$ e $y \in \mathcal{C}$ continua a valere:
    
      
    
    $$\Pr_2[y \mid x] = \Pr_1[y \mid x] = c_y$$
    
    Calcoliamo ora la nuova probabilità marginale $\Pr_2[y]$ del testo cifrato $y$ sotto la distribuzione $\Pr_2$:
    
      
    
    $$\Pr_2[y] = \sum_{x \in \mathcal{P}} \Pr_2[x] \Pr_2[y \mid x] = \sum_{x \in \mathcal{P}} \Pr_2[x] \cdot c_y = c_y \sum_{x \in \mathcal{P}} \Pr_2[x] = c_y \cdot 1 = c_y$$
    
    Di conseguenza, per ogni $x \in \mathcal{P}$ (con $\Pr_2[x] > 0$) e per ogni $y \in \mathcal{C}$, applicando il Teorema di Bayes sotto la distribuzione $\Pr_2$:
    
      
    
    $$\Pr_2[x \mid y] = \frac{\Pr_2[x] \Pr_2[y \mid x]}{\Pr_2[y]} = \frac{\Pr_2[x] \cdot c_y}{c_y} = \Pr_2[x]$$
    
    (E se per qualche $x_0 \in \mathcal{P}$ si ha $\Pr_2[x_0] = 0$, vale banalmente $\Pr_2[x_0 \mid y] = 0 = \Pr_2[x_0]$). Pertanto il crittosistema mantiene la segretezza perfetta per qualsiasi distribuzione di probabilità sui testi in chiaro. $\blacksquare$
    
      
    

## Esercizio 3.7

> [!question] Testo dell'Esercizio 3.7 Dimostrare che se un crittosistema gode di segretezza perfetta e vale $\vert{}\mathcal{K}\vert{} = \vert{}\mathcal{C}\vert{} = \vert{}\mathcal{P}\vert{}$, allora ogni testo cifrato è equiprobabile (cioè $\Pr[y] = \frac{1}{\vert{}\mathcal{C}\vert{}}$ per ogni $y \in \mathcal{C}$).
> 
>   

### Svolgimento e Dimostrazione

Sia $n = \vert{}\mathcal{K}\vert{} = \vert{}\mathcal{C}\vert{} = \vert{}\mathcal{P}\vert{}$. Poiché il crittosistema ha segretezza perfetta e soddisfa l'uguaglianza delle cardinalità $\vert{}\mathcal{K}\vert{} = \vert{}\mathcal{C}\vert{} = \vert{}\mathcal{P}\vert{}$, per il **Teorema di Shannon (Theorem 3.2)** valgono necessariamente le due proprietà seguenti:

  

1. Per ogni $x \in \mathcal{P}$ e per ogni $y \in \mathcal{C}$, esiste **un'unica** chiave $K \in \mathcal{K}$ tale che $e_K(x) = y$.
    
      
    
2. Tutte le chiavi sono scelte con uguale probabilità:
    
      
    
    $$\Pr[K] = \frac{1}{\vert{}\mathcal{K}\vert{}} = \frac{1}{\vert{}\mathcal{C}\vert{}} \quad \forall K \in \mathcal{K}$$
    

Fissiamo ora un generico elemento di testo cifrato $y \in \mathcal{C}$.

  

- Per ciascun testo in chiaro $x \in \mathcal{P}$, poiché esiste un'unica chiave $K$ che cifra $x$ in $y$ e tale chiave ha probabilità $\frac{1}{\vert{}\mathcal{C}\vert{}}$, la probabilità condizionata di ottenere $y$ dato $x$ vale:
    
      
    
    $$\Pr[y \mid x] = \frac{1}{\vert{}\mathcal{C}\vert{}}$$
    
- Calcoliamo la probabilità assoluta $\Pr[y]$ tramite il teorema della probabilità totale sommando su tutti i possibili testi in chiaro $x \in \mathcal{P}$:
    
      
    
    $$\Pr[y] = \sum_{x \in \mathcal{P}} \Pr[x] \Pr[y \mid x] = \sum_{x \in \mathcal{P}} \Pr[x] \frac{1}{\vert{}\mathcal{C}\vert{}} = \frac{1}{\vert{}\mathcal{C}\vert{}} \sum_{x \in \mathcal{P}} \Pr[x]$$
    
- Poiché la somma delle probabilità a priori di tutti i testi in chiaro vale $\sum_{x \in \mathcal{P}} \Pr[x] = 1$, otteniamo:
    
      
    
    $$\Pr[y] = \frac{1}{\vert{}\mathcal{C}\vert{}} \cdot 1 = \mathbf{\frac{1}{\vert{}\mathcal{C}\vert{}}} \quad \forall y \in \mathcal{C}$$
    
    Tutti i testi cifrati sono quindi equiprobabili (indipendentemente dalla distribuzione di probabilità del testo in chiaro!). $\blacksquare$
    
      
    

## Esercizio 4.16 (Punti a, b, c)

> [!question] Testo dell'Esercizio 4.16 Supponiamo che la S-box dell'Example 4.1 venga sostituita dalla S-box definita dalla seguente sostituzione $\pi_{S''}$:
> 
>   
> 
> |**z**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**A**|**B**|**C**|**D**|**E**|**F**|
> |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
> |**$\pi_{S''}(z)$**|`E`|`2`|`1`|`3`|`D`|`9`|`0`|`6`|`F`|`4`|`5`|`A`|`8`|`C`|`7`|`B`|
> 
> - **(a)** Calcolare la tabella dei valori $N_D$ (come definita nella Definition 4.3) per questa S-box.
>     
>       
>     
> - **(b)** Trovare una traccia differenziale (_differential trail_) che utilizzi quattro S-box attive, ovvero $S_1^1, S_4^1, S_4^2$ e $S_4^3$, avente rapporto di propagazione $27/2048$.
>     
>       
>     
> - **(c)** Descrivere un attacco differenziale, analogo all'Algorithm 4.3, che permetta di trovare 8 bit della sottochiave nell'ultimo round.
>     
>       
>     

### (a) Calcolo della Tabella di Distribuzione delle Differenze $N_D(x', y')$

Per la **Definition 4.3**, per ogni differenziale di input $x' \in \{0, \dots, \text{F}\}$ e di output $y' \in \{0, \dots, \text{F}\}$, il valore $N_D(x', y')$ è il numero di input $x \in \{0, \dots, \text{F}\}$ tali che $\pi_{S''}(x) \oplus \pi_{S''}(x \oplus x') = y'$.

  

Convertiamo prima $\pi_{S''}(z)$ in binario a 4 bit per eseguire gli XOR rapidamente:

  

- `0`$\to$`1110` (`E`), `1`$\to$`0010` (`2`), `2`$\to$`0001` (`1`), `3`$\to$`0011` (`3`), `4`$\to$`1101` (`D`), `5`$\to$`1001` (`9`), `6`$\to$`0000` (`0`), `7`$\to$`0110` (`6`), `8`$\to$`1111` (`F`), `9`$\to$`0100` (`4`), `A`$\to$`0101` (`5`), `B`$\to$`1010` (`A`), `C`$\to$`1000` (`8`), `D`$\to$`1100` (`C`), `E`$\to$`0111` (`7`), `F`$\to$`1011` (`B`).
    
      
    

Ecco la **Tabella completa dei valori $N_D(x', y')$** (righe = $x'$, colonne = $y'$):

  

|**x′↓ \ y′→**|**0**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**A**|**B**|**C**|**D**|**E**|**F**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**0**|16|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|**1**|0|0|2|0|**4**|0|2|0|0|0|0|2|**4**|0|0|2|
|**2**|0|2|0|0|0|0|0|2|0|0|2|0|0|2|2|6|
|**3**|0|2|0|4|0|2|0|0|0|2|0|4|0|2|0|0|
|**4**|0|4|2|2|0|2|0|2|2|0|0|2|0|0|0|0|
|**5**|0|0|0|4|0|0|0|4|0|0|0|0|2|2|2|2|
|**6**|0|0|0|0|2|0|2|0|2|0|2|0|2|2|2|2|
|**7**|0|0|4|2|2|0|0|0|4|2|0|0|0|0|2|0|
|**8**|0|2|0|0|2|4|2|2|0|2|0|0|0|2|0|0|
|**9**|0|**6**|0|0|0|0|2|0|0|0|2|4|0|2|0|0|
|**A**|0|0|2|0|0|0|0|2|4|0|4|2|0|0|2|0|
|**B**|0|0|0|0|2|2|2|2|0|0|0|0|4|0|4|0|
|**C**|0|0|2|0|0|2|4|0|2|0|0|0|2|2|2|0|
|**D**|0|0|2|2|2|0|2|0|0|2|6|0|0|0|0|0|
|**E**|0|0|2|2|0|0|0|0|2|6|0|0|0|0|0|4|
|**F**|0|0|0|0|2|4|0|2|0|2|0|2|2|2|0|0|

### (b) Ricerca della Traccia Differenziale con Rapporto di Propagazione $27/2048$

Vogliamo costruire una traccia differenziale sui primi 3 round che attivi esattamente le quattro S-box **$S_1^1, S_4^1, S_4^2, S_4^3$** con rapporto di propagazione complessivo $R_p = \frac{27}{2048}$.

  

1. **Analisi dei vincoli imposti dalla permutazione $\pi_P$:**
    
      
    - **Dal Round 1 al Round 2:** Nel Round 1 sono attive solo $S_1^1$ (bit 1–4) e $S_4^1$ (bit 13–16), mentre nel Round 2 deve attivarsi **esclusivamente** $S_4^2$ (che riceve i bit in posizione 13, 14, 15, 16). Guardando la permutazione $\pi_P$ dell'Example 4.1:
        
          
        - L'unico bit di $S_1^1$ che viene mappato dentro $S_4^2$ è il **bit 4**, poiché $\pi_P(4) = 13$ (questo perchè 13 è la posizione che accetta $S_4^2$) . Pertanto, l'uscita differenziale di $S_1^1$ deve essere obbligatoriamente (accendo solo il bit 4): 
            
              
            
            $$v'^1_{(1)} = \texttt{0001}_2 = \mathbf{1_{16}}$$
            
        - L'unico bit di $S_4^1$ che viene mappato dentro $S_4^2$ è il **bit 16**, poiché $\pi_P(16) = 16$. Pertanto, l'uscita differenziale di $S_4^1$ deve essere obbligatoriamente:
            
              
            
            $$v'^1_{(4)} = \texttt{0001}_2 = \mathbf{1_{16}}$$
            
        - Con $v'^1 = (\texttt{0001}, \texttt{0000}, \texttt{0000}, \texttt{0001})$, applicando $\pi_P$ i bit 4 e 16 finiscono nelle posizioni 13 e 16, dando come ingresso a $S_4^2$ nel Round 2 il differenziale:
            
              
            
            $$u'^2_{(4)} = \texttt{1001}_2 = \mathbf{9_{16}} \qquad (u'^2 = \texttt{0000 0000 0000 1001}_2 = \texttt{0009}_{16})$$
            
    - **Dal Round 2 al Round 3:** Nel Round 3 deve attivarsi **esclusivamente** $S_4^3$ (bit 13–16). L'unico bit in uscita da $S_4^2$ (posizioni 13–16) che $\pi_P$ mappa ancora dentro $S_4^3$ è il **bit 16** ($\pi_P(16) = 16$). Quindi l'uscita di $S_4^2$ deve essere obbligatoriamente:
        
          
        
        $$v'^2_{(4)} = \texttt{0001}_2 = \mathbf{1_{16}}$$
        
        Questo implica che nel Round 2 l'unica S-box attiva $S_4^2$ compie la transizione **$9 \longrightarrow 1$**, il cui rapporto di propagazione (dalla tabella al punto a) è:
        
          
        
        $$R_p(\texttt{1001}, \texttt{0001}) = \frac{N_D(9, 1)}{16} = \frac{6}{16} = \mathbf{\frac{3}{8}}$$
        
        Dopo $\pi_P$, l'ingresso a $S_4^3$ nel Round 3 è quindi:
        
        $$u'^3_{(4)} = \texttt{0001}_2 = \mathbf{1_{16}} \qquad (u'^3 = \texttt{0000 0000 0000 0001}_2 = \texttt{0001}_{16})$$
        
2. **Scelta degli input nel Round 1 e dell'output nel Round 3 per ottenere $R_p = 27/2048$:**
    
      
    - Per $S_1^1$ e $S_4^1$ (che devono entrambe avere output $y' = 1$), cerchiamo nella colonna $y' = 1$ della tabella $N_D$ il valore massimo: si trova in corrispondenza della riga **$x' = 9$** ($\texttt{1001}_2$), dove $N_D(9, 1) = 6$, cioè $R_p(\texttt{1001}, \texttt{0001}) = \frac{6}{16} = \mathbf{\frac{3}{8}}$.
        
          
        
    - Scegliamo quindi per entrambe le S-box del Round 1 l'input $u'^1_{(1)} = u'^1_{(4)} = \texttt{1001}_2 = 9_{16}$, ovvero il differenziale del plaintext:
        
          
        
        $$x' = u'^1 = \texttt{1001 0000 0000 1001}_2 = \mathbf{\texttt{9009}_{16}}$$
        
    - Finora il prodotto dei primi tre rapporti di propagazione è $\frac{3}{8} \times \frac{3}{8} \times \frac{3}{8} = \frac{27}{512}$.
        
          
        
    - Affinché il rapporto totale su 3 round sia $\frac{27}{2048}$, la quarta S-box attiva $S_4^3$ (che ha input $u'^3_{(4)} = 1$) deve avere rapporto di propagazione:
        
          
        
        $$R_p(S_4^3) = \frac{27/2048}{27/512} = \frac{512}{2048} = \mathbf{\frac{1}{4}} = \frac{4}{16}$$
        
    - Guardando la riga **$x' = 1$** della tabella $N_D$, vediamo che il valore $N_D(1, y') = 4$ si ottiene per due possibili output:
        
          
        - **Opzione 1:** $y' = 4_{16} = \texttt{0100}_2$ (che attiva solo il bit 14, mappato da $\pi_P$ in $\pi_P(14) = 8$, attivando una sola S-box nell'ultimo round, $S_2^4$).
            
              
            
        - **Opzione 2:** $y' = \text{C}_{16} = \texttt{1100}_2$ (che attiva due bit, 13 e 14, attivando **due S-box** nell'ultimo round e permettendo così di trovare **8 bit di sottochiave** come richiesto dal punto c!).
            
              
            
3. **Riepilogo Formale della Traccia Differenziale a 3 Round:**
    
      
    - **Input plaintext XOR:** $x' = u'^1 = \texttt{1001 0000 0000 1001}_2 = \texttt{9009}_{16}$
        
          
        
    - **Round 1 ($S_1^1, S_4^1$):**
        
          
        - $S_1^1 : \texttt{1001} \to \texttt{0001}$ con $R_p = 3/8$
            
              
            
        - $S_4^1 : \texttt{1001} \to \texttt{0001}$ con $R_p = 3/8$
            
              
            
        - Output Round 1: $v'^1 = \texttt{0001 0000 0000 0001} \xrightarrow{\pi_P} w'^1 = u'^2 = \texttt{0000 0000 0000 1001}$
            
              
            
    - **Round 2 ($S_4^2$):**
        
          
        - $S_4^2 : \texttt{1001} \to \texttt{0001}$ con $R_p = 3/8$
            
              
            
        - Output Round 2: $v'^2 = \texttt{0000 0000 0000 0001} \xrightarrow{\pi_P} w'^2 = u'^3 = \texttt{0000 0000 0000 0001}$
            
              
            
    - **Round 3 ($S_4^3$):**
        
          
        - $S_4^3 : \texttt{0001} \to \texttt{1100}$ ($\text{C}_{16}$) con $R_p = 4/16 = 1/4$
            
              
            
        - Output Round 3: $v'^3 = \texttt{0000 0000 0000 1100}$ (bit attivi in posizione **13** e **14**).
            
              
            
    - **Propagazione verso il Round 4:** Applicando $\pi_P$ a $v'^3$, poiché $\pi_P(13) = 4$ (4° bit di $S_1^4$) e $\pi_P(14) = 8$ (4° bit di $S_2^4$), l'input differenziale al Round 4 è:
        
          
        
        $$w'^3 = u'^4 = \texttt{0001 0001 0000 0000}_2 = \mathbf{\texttt{1100}_{16}}$$
        
    - **Rapporto di propagazione totale:**
        
          
        
        $$R_p = \frac{3}{8} \times \frac{3}{8} \times \frac{3}{8} \times \frac{1}{4} = \mathbf{\frac{27}{2048}}$$
        

### (c) Descrizione dell'Attacco Differenziale sull'Ultimo Round (Analogo ad Algorithm 4.3)

Dalla traccia trovata al punto (b), per ogni _right pair_ il differenziale in ingresso alle S-box dell'ultimo round (Round 4) è:

  

$$u'^4 = (\texttt{0001}, \texttt{0001}, \texttt{0000}, \texttt{0000})$$

- **S-box passive nel Round 4 (Filtraggio):** Le S-box **$S_3^4$** e **$S_4^4$** sono inattive ($u'^4_{(3)} = \texttt{0000}$ e $u'^4_{(4)} = \texttt{0000}$). Di conseguenza, ogni _right pair_ deve presentare $y_{(3)} = y^*_{(3)}$ e $y_{(4)} = y^*_{(4)}$ (gli ultimi 8 bit dei due testi cifrati devono coincidere).
    
      
    
- **S-box attive nel Round 4 (Target subkey bits):** Le S-box attive sono **$S_1^4$** (con differenziale atteso $u'^4_{(1)} = \texttt{0001}$) e **$S_2^4$** (con differenziale atteso $u'^4_{(2)} = \texttt{0001}$). L'attacco permette quindi di determinare gli **8 bit** della sottochiave finale $K^5$ corrispondenti ai primi due blocchi da 4 bit: **$(K^5_{(1)}, K^5_{(2)})$**.
    
      
    

#### Pseudocodice dell'Attacco Differenziale Modificato

> [!abstract] Algoritmo: DIFFERENTIAL ATTACK per l'Esercizio 4.16 **Input:** Un insieme $\mathcal{T}$ di $T$ coppie di plaintext-ciphertext $(x, y, x^*, y^*)$ aventi $x \oplus x^* = x' = \texttt{9009}_{16}$; la S-box $\pi_{S''}$; i differenziali target $u'^4_{(1)} = \texttt{0001}$ e $u'^4_{(2)} = \texttt{0001}$. **Output:** Gli 8 bit della sottochiave finale $(K^5_{(1)}, K^5_{(2)})$.
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
>     $\quad$ **if** $(y_{(3)} = y^*_{(3)})$ **and** $(y_{(4)} = y^*_{(4)})$ **then** _(Filtraggio sulle S-box passive $S_3^4, S_4^4$)_
>     
>     $\quad \quad$ **for** $(L_1, L_2) \leftarrow (0, 0)$ **to** $(\text{F}, \text{F})$ **do**
>     
>     $\quad \quad \quad v^4_{(1)} \leftarrow L_1 \oplus y_{(1)}$
>     
>     $\quad \quad \quad (v^4_{(1)})^* \leftarrow L_1 \oplus y^*_{(1)}$
>     
>     $\quad \quad \quad u^4_{(1)} \leftarrow \pi_{S''}^{-1}(v^4_{(1)})$
>     
>     $\quad \quad \quad (u^4_{(1)})^* \leftarrow \pi_{S''}^{-1}((v^4_{(1)})^*)$
>     
>     $\quad \quad \quad u'^4_{(1)} \leftarrow u^4_{(1)} \oplus (u^4_{(1)})^*$
>     
>     $\quad \quad \quad v^4_{(2)} \leftarrow L_2 \oplus y_{(2)}$
>     
>     $\quad \quad \quad (v^4_{(2)})^* \leftarrow L_2 \oplus y^*_{(2)}$
>     
>     $\quad \quad \quad u^4_{(2)} \leftarrow \pi_{S''}^{-1}(v^4_{(2)})$
>     
>     $\quad \quad \quad (u^4_{(2)})^* \leftarrow \pi_{S''}^{-1}((v^4_{(2)})^*)$
>     
>     $\quad \quad \quad u'^4_{(2)} \leftarrow u^4_{(2)} \oplus (u^4_{(2)})^*$
>     
>     $\quad \quad \quad$ **if** $(u'^4_{(1)} = \texttt{0001})$ **and** $(u'^4_{(2)} = \texttt{0001})$ **then**
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

- **Nota sul numero di coppie necessarie (Punto d del testo):** Poiché il rapporto di propagazione $\epsilon = 27/2048 \approx 0.0132$ è esattamente la metà rispetto a quello dell'Algorithm 4.3 ($27/1024$), servono circa il doppio delle coppie rispetto al caso precedente (circa $100 - 200$ coppie di testi in chiaro scelti sono già sufficienti nella pratica per far emergere la sottochiave corretta $(K^5_{(1)}, K^5_{(2)})$).

## Esercizio 4.8 (Modalità CBC)

> [!question] Testo dell'Esercizio 4.8 (Solo per CBC Mode)
> 
> Supponiamo che $x = x_1 x_2 \dots x_n$ e $x' = x'_1 x'_2 \dots x'_n$ siano due sequenze di $n$ blocchi di testo in chiaro. Supponiamo inoltre che $x_i = x'_i$ per $1 \le i \le j$, ma $x_{j+1} \neq x'_{j+1}$.
> 
> Sia $y = y_1 y_2 \dots y_n$ il testo cifrato ottenuto cifrando $x$ in modalità **CBC**, e sia $y' = y'_1 y'_2 \dots y'_n$ il testo cifrato ottenuto cifrando $x'$ nella stessa modalità **utilizzando la stessa chiave segreta $K$ e lo stesso vettore di inizializzazione ($IV$)**.
> 
> Quale informazione sui due testi in chiaro $x$ e $x'$ può dedurre un avversario (Oscar) osservando unicamente i due testi cifrati $y$ e $y'$?
> 
>   

### Svolgimento e Dimostrazione

1. **Richiamo delle equazioni di cifratura CBC:** In modalità CBC (Sezione 4.7), dato un vettore di inizializzazione $IV$ e una chiave segreta $K$, le due sequenze di testi cifrati $y$ e $y'$ vengono costruite ricorsivamente ponendo $y_0 = IV$ e $y'_0 = IV$, e calcolando per ogni blocco $i \ge 1$:
    
      
    
    $$y_i = e_K(y_{i-1} \oplus x_i) \qquad \text{e} \qquad y'_i = e_K(y'_{i-1} \oplus x'_i)$$
    
    dove $e_K$ è una **permutazione (biiezione)** sullo spazio dei blocchi (di conseguenza, per qualsiasi coppia di blocchi $A$ e $B$, vale l'equivalenza stretta: $e_K(A) = e_K(B) \iff A = B$).
    
      
    
2. **Analisi per i primi $j$ blocchi ($1 \le i \le j$):** Dimostriamo per induzione su $i \in \{1, \dots, j\}$ che i blocchi cifrati coincidono ($y_i = y'_i$):
    
      
    - **Caso base ($i = 1$):** Poiché viene riutilizzato lo stesso $IV$, si ha $y_0 = y'_0 = IV$. Inoltre, per ipotesi, $x_1 = x'_1$. Pertanto:
        
          
        
        $$y_1 = e_K(IV \oplus x_1) = e_K(IV \oplus x'_1) = y'_1$$
        
    - **Passo induttivo ($1 < i \le j$):** Supponiamo che valga $y_{i-1} = y'_{i-1}$. Poiché per ipotesi $x_i = x'_i$ per ogni $i \le j$, segue immediatamente che:
        
          
        
        $$y_i = e_K(y_{i-1} \oplus x_i) = e_K(y'_{i-1} \oplus x'_i) = y'_i$$
        
        Dunque, i primi $j$ blocchi dei due testi cifrati risultano **identici**:
        
          
        
        $$y_1 = y'_1, \quad y_2 = y'_2, \quad \dots, \quad y_j = y'_j$$
        
3. **Analisi per il blocco $(j + 1)$-esimo:** Consideriamo ora il blocco in posizione $j + 1$:
    
      
    
    $$y_{j+1} = e_K(y_j \oplus x_{j+1}) \qquad \text{e} \qquad y'_{j+1} = e_K(y'_j \oplus x'_{j+1})$$
    
    Dal passo precedente sappiamo che $y_j = y'_j$, mentre per ipotesi sappiamo che i due blocchi in chiaro sono diversi ($x_{j+1} \neq x'_{j+1}$). Poiché l'operazione di XOR con una costante fissata ($y_j$) è biiettiva, da $x_{j+1} \neq x'_{j+1}$ segue necessariamente che gli ingressi alla funzione di cifratura sono diversi:
    
      
    
    $$y_j \oplus x_{j+1} \neq y'_j \oplus x'_{j+1}$$
    
    E poiché $e_K$ è una biiezione (funzione iniettiva), input diversi producono obbligatoriamente output diversi:
    
      
    
    $$\mathbf{y_{j+1} \neq y'_{j+1}}$$
    
    _(Nota: per i blocchi successivi $i \ge j + 2$, poiché $y_{j+1}$ e $y'_{j+1}$ sono ormai completamente diversi e pseudocasuali, anche tutti i blocchi cifrati successivi $y_i$ e $y'_i$ appariranno diversi e scorrelati con altissima probabilità, a meno di una collisione fortuita $y_{i-1} \oplus y'_{i-1} = x_i \oplus x'_i$ che avviene con probabilità trascurabile $2^{-m}$)._
    
      
    
4. **Conclusione (Informazione appresa dall'avversario):** Confrontando blocco per blocco i due testi cifrati $y$ e $y'$ e osservando che $y_i = y'_i$ per $1 \le i \le j$ mentre $y_{j+1} \neq y'_{j+1}$, Oscar deduce con certezza matematica che **i due messaggi in chiaro $x$ e $x'$ hanno esattamente i primi $j$ blocchi identici** ($x_1 = x'_1, \dots, x_j = x'_j$) **e che differiscono per la prima volta nel blocco $(j + 1)$-esimo** ($x_{j+1} \neq x'_{j+1}$)._(Questo dimostra perché in modalità CBC è fondamentale cambiare sempre l'$IV$ ad ogni nuova cifratura effettuata con la stessa chiave $K$: riutilizzare lo stesso $IV$ rivela sempre la lunghezza del prefisso comune di due messaggi!)._ $\blacksquare$
    
      
    

## Esercizio 4.18 

> [!question] Testo dell'Esercizio 4.18
> 
> Supponiamo di costruire un _combination generator_ a partire da tre LFSR, utilizzando come funzione di combinazione (_combining function_):
> 
>   
> 
> $$f(z_1, z_2, z_3) = (z_1 \wedge z_2) \oplus (\neg z_1 \wedge z_3)$$
> 
> (questo generatore è noto come **Geffe generator**).
> 
>   
> 
> - **(a)** Calcolare la probabilità che $z_i = f(z_1, z_2, z_3)$, per $i = 1, 2, 3$, assumendo che $z_1, z_2$ e $z_3$ siano variabili aleatorie binarie indipendenti e uniformemente distribuite tali che $\Pr[z_i = 0] = \Pr[z_i = 1] = 1/2$ per $i = 1, 2, 3$.
>     
>       
>     
> - **(b)** Spiegare brevemente come questo generatore possa essere attaccato se una quantità sufficiente di bit della _keystream_ è nota all'avversario.
>     
>       
>     

### (a) Calcolo delle Probabilità di Correlazione $\Pr[f(z_1, z_2, z_3) = z_i]$

Poiché $z_1, z_2, z_3 \in \mathbb{Z}_2 = \{0, 1\}$ sono variabili aleatorie indipendenti con $\Pr[z_i = 0] = \Pr[z_i = 1] = \frac{1}{2}$, ciascuna delle $2^3 = 8$ possibili triple $(z_1, z_2, z_3) \in (\mathbb{Z}_2)^3$ è **equiprobabile** con probabilità esattamente pari a:

  

$$\Pr[(z_1, z_2, z_3)] = \frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} = \frac{1}{8}$$

Ricordando le definizioni delle operazioni booleane su $\{0, 1\}$:

  

- $a \wedge b = a \cdot b$ (AND logico: vale `1` solo se $a=1$ e $b=1$).
    
      
    
- $\neg a = 1 \oplus a$ (NOT logico: inverte il bit).
    
      
    
- $a \oplus b = (a + b) \bmod 2$ (XOR logico).
    
      
    

Notiamo che nella funzione di Geffe $f(z_1, z_2, z_3) = (z_1 \wedge z_2) \oplus (\neg z_1 \wedge z_3)$, la variabile $z_1$ agisce da selettore:

  

- Se **$z_1 = 0$**, allora $z_1 \wedge z_2 = 0$ e $\neg z_1 = 1$, quindi **$f(0, z_2, z_3) = z_3$**.
    
      
    
- Se **$z_1 = 1$**, allora $\neg z_1 \wedge z_3 = 0$ e $z_1 \wedge z_2 = z_2$, quindi **$f(1, z_2, z_3) = z_2$**.
    
      
    

Costruiamo la **Tabella di Verità completa** delle 8 configurazioni e verifichiamo in quali righe l'uscita $f = f(z_1, z_2, z_3)$ coincide rispettivamente con $z_1$, con $z_2$ e con $z_3$:

  

|**z1​**|**z2​**|**z3​**|**z1​∧z2​**|**¬z1​∧z3​**|**f(z1​,z2​,z3​)**|**f=z1​ ?**|**f=z2​ ?**|**f=z3​ ?**|
|---|---|---|---|---|---|---|---|---|
|`0`|`0`|`0`|`0`|`0`|**`0`**|✅ Sì (`0=0`)|✅ Sì (`0=0`)|✅ Sì (`0=0`)|
|`0`|`0`|`1`|`0`|`1`|**`1`**|❌ No (`1≠0`)|❌ No (`1≠0`)|✅ Sì (`1=1`)|
|`0`|`1`|`0`|`0`|`0`|**`0`**|✅ Sì (`0=0`)|❌ No (`0≠1`)|✅ Sì (`0=0`)|
|`0`|`1`|`1`|`0`|`1`|**`1`**|❌ No (`1≠0`)|✅ Sì (`1=1`)|✅ Sì (`1=1`)|
|`1`|`0`|`0`|`0`|`0`|**`0`**|❌ No (`0≠1`)|✅ Sì (`0=0`)|✅ Sì (`0=0`)|
|`1`|`0`|`1`|`0`|`0`|**`0`**|❌ No (`0≠1`)|✅ Sì (`0=0`)|❌ No (`0≠1`)|
|`1`|`1`|`0`|`1`|`0`|**`1`**|✅ Sì (`1=1`)|✅ Sì (`1=1`)|❌ No (`1≠0`)|
|`1`|`1`|`1`|`1`|`0`|**`1`**|✅ Sì (`1=1`)|✅ Sì (`1=1`)|✅ Sì (`1=1`)|
|**Conteggio**|||||**4 zeri, 4 uni**|**4 righe su 8**|**6 righe su 8**|**6 righe su 8**|

Contando il numero di righe favorevoli su $8$ otteniamo le tre probabilità richieste:

  

1. **Per $i = 1$ ($\text{LFSR}_1$):** $f(z_1, z_2, z_3) = z_1$ si verifica in $4$ righe su $8$:
    
      
    
    $$\Pr[z_1 = f(z_1, z_2, z_3)] = \frac{4}{8} = \mathbf{\frac{1}{2} = 0.50}$$
    
2. **Per $i = 2$ ($\text{LFSR}_2$):** $f(z_1, z_2, z_3) = z_2$ si verifica in $6$ righe su $8$ (tutte le $4$ righe in cui $z_1 = 1$, più le $2$ righe in cui $z_1 = 0$ e $z_2 = z_3$):
    
      
    
    $$\Pr[z_2 = f(z_1, z_2, z_3)] = \frac{6}{8} = \mathbf{\frac{3}{4} = 0.75}$$
    
3. **Per $i = 3$ ($\text{LFSR}_3$):** $f(z_1, z_2, z_3) = z_3$ si verifica in $6$ righe su $8$ (tutte le $4$ righe in cui $z_1 = 0$, più le $2$ righe in cui $z_1 = 1$ e $z_3 = z_2$):
    
      
    
    $$\Pr[z_3 = f(z_1, z_2, z_3)] = \frac{6}{8} = \mathbf{\frac{3}{4} = 0.75}$$
    

### (b) Descrizione dell'Attacco al Generatore (Correlation Attack)

Siano $L_1, L_2, L_3$ le lunghezze (note) dei tre LFSR, e sia $K = (K^1, K^2, K^3)$ la chiave segreta del generatore, costituita dagli stati iniziali non nulli dei tre registri (ci sono rispettivamente $2^{L_1}-1$, $2^{L_2}-1$ e $2^{L_3}-1$ possibili chiavi iniziali per i tre LFSR). Supponiamo che l'avversario (Oscar), tramite un attacco _known-plaintext_ ($z_j = x_j \oplus y_j$), conosca una sequenza sufficientemente lunga di **$N$ bit consecutivi della vera keystream** $z_1, z_2, \dots, z_N$.

  

Dai calcoli del punto (a) sappiamo che la keystream finale $z_j$ presenta una **forte correlazione statistica del 75%** sia con la sequenza generata dal 2° LFSR ($p_2 = 3/4$) sia con quella generata dal 3° LFSR ($p_3 = 3/4$). Oscar può quindi applicare un **Correlation Attack (Attacco di Correlazione di Siegenthaler, Sezione 4.8.1)** di tipo _divide-et-impera_ per trovare $K^2, K^3$ e $K^1$ **separatamente**, procedendo in tre passi:

  

1. **Passo 1 – Recupero dello stato iniziale $K^2$ del 2° LFSR:**
    
      
    - Per ciascuno dei $2^{L_2} - 1$ possibili stati iniziali candidati $\tilde{K}^2 \in (\mathbb{Z}_2)^{L_2} \setminus \{\mathbf{0}\}$, Oscar simula il funzionamento del solo $\text{LFSR}_2$ per $N$ cicli, generando i primi $N$ bit della sequenza candidata $\tilde{z}_1^2, \tilde{z}_2^2, \dots, \tilde{z}_N^2$.
        
          
        
    - Confronta questa sequenza bit a bit con i veri $N$ bit della keystream $z_1, \dots, z_N$ e conta il numero di coincidenze (_matches_):
        
          
        
        $$M(\tilde{K}^2) = \left\vert{} \left\{ 1 \le j \le N : \tilde{z}_j^2 = z_j \right\} \right\vert{}$$
        
    - **Distinzione statistica:**
        
          
        - Per qualsiasi stato iniziale **errato** ($\tilde{K}^2 \neq K^2$), la sequenza $\tilde{z}_j^2$ è statisticamente indipendente da $z_j$, quindi il numero atteso di coincidenze è circa la metà dei bit: $E[M] \approx \mathbf{\frac{1}{2} N = 0.50 \, N}$.
            
              
            
        - Per lo stato iniziale **corretto** ($\tilde{K}^2 = K^2$), poiché $\Pr[z_j^2 = z_j] = \frac{3}{4}$, il numero atteso di coincidenze sale a **$E[M] = \mathbf{\frac{3}{4} N = 0.75 \, N}$**.
            
              
            
    - Selezionando l'ipotesi $\tilde{K}^2$ che massimizza il numero di match (avvicinandosi a $\frac{3}{4} N$), Oscar identifica univocamente la vera sottochiave **$K^2$** dopo soli $2^{L_2} - 1$ tentativi.
        
          
        
2. **Passo 2 – Recupero dello stato iniziale $K^3$ del 3° LFSR:**
    
      
    - Poiché anche per il 3° LFSR vale $\Pr[z_j^3 = z_j] = \frac{3}{4}$, Oscar ripete esattamente la stessa procedura in modo indipendente sul 3° registro: testa tutti i $2^{L_3} - 1$ possibili stati iniziali $\tilde{K}^3$, genera $N$ bit per ciascuno e individua la vera sottochiave **$K^3$** come l'unica che produce circa **$\frac{3}{4} N$ coincidenze** con la keystream $z_1, \dots, z_N$ (contro $\frac{1}{2} N$ delle chiavi errate).
        
          
        
3. **Passo 3 – Recupero dello stato iniziale $K^1$ del 1° LFSR:**
    
      
    - Sebbene il 1° LFSR non possa essere attaccato direttamente da solo perché non è correlato con la keystream ($\Pr[z_j^1 = z_j] = \frac{1}{2}$), a questo punto Oscar **conosce già i veri stati iniziali $K^2$ e $K^3$** (e quindi conosce le intere sequenze vere $z_j^2$ e $z_j^3$)!
        
          
        
    - A Oscar basta quindi testare tutte le $2^{L_1} - 1$ possibili chiavi iniziali $\tilde{K}^1$ del 1° LFSR inserendole nel generatore completo insieme ai già noti $K^2$ e $K^3$: la chiave corretta **$K^1$** sarà l'unica a generare una keystream che coincide al **100%** con tutti gli $N$ bit osservati $z_1, \dots, z_N$. _(In alternativa, per tutti gli istanti $j$ in cui $z_j^2 \neq z_j^3$, il valore di $z_j^1$ si legge persino direttamente senza fare tentativi, poiché quando $z_j^2 \neq z_j^3$ vale $z_j = z_j^2 \implies z_j^1 = 1$ e $z_j = z_j^3 \implies z_j^1 = 0$!)._
        
          
        

- **Vantaggio Computazionale Complessivo:** Invece di effettuare una ricerca esaustiva su $\approx 2^{L_1 + L_2 + L_3}$ chiavi (prodotto degli spazi delle chiavi), l'attacco di correlazione recupera l'intera chiave segreta $K = (K^1, K^2, K^3)$ effettuando solamente:
    
      
    
    $$(2^{L_1} - 1) + (2^{L_2} - 1) + (2^{L_3} - 1) \approx \mathbf{2^{L_1} + 2^{L_2} + 2^{L_3}}$$
    
    test complessivi, demolendo completamente la sicurezza del generatore. $\blacksquare$
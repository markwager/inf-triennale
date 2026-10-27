# Appendice A: Teoria dei Numeri e Concetti Algebrici per la Crittografia

## A.1 Aritmetica Modulare

- **Definizione A.1.1 (Congruenze):** Siano $a$ e $b$ numeri interi e $m$ un intero positivo. Diciamo che $a \equiv b \pmod m$ se $m$ divide la differenza $b - a$. L'espressione $a \equiv b \pmod m$ è chiamata **congruenza** e si legge "$a$ è congruo a $b$ modulo $m$". Il numero $m$ è chiamato **modulo**.
    
      
    
- **Definizione A.1.2 (Riduzione Modulare):** Dividendo $a$ e $b$ per $m$ otteniamo quozienti e resti interi: $a = q_1m + r_1$ e $b = q_2m + r_2$, con $0 \le r_1 \le m - 1$ e $0 \le r_2 \le m - 1$. Allora $a \equiv b \pmod m$ se e solo se $r_1 = r_2$. Utilizziamo la notazione $a \bmod m$ per indicare il resto $r_1$ quando $a$ è diviso per $m$. Sostituire $a$ con $a \bmod m$ si definisce **riduzione modulare** ($a$ è ridotto modulo $m$).
    
      
    

> [!example] Esempio A.1.3 (Calcolo di riduzioni modulari e numeri negativi)
> 
> Valutiamo $a \bmod m$ sia con numeri positivi che negativi (ad esempio con modulo $m = 26$):
> 
>   
> 
> - **Caso positivo:** Per $a = 101$ e $m = 26$, dividendo otteniamo $101 = 3 \times 26 + 23$ (dove $0 \le 23 < 26$). Pertanto $101 \bmod 26 = 23$.
>     
>       
>     
> - **Caso negativo:** Per $a = -19$ e $m = 26$, poiché il resto $r_1$ deve soddisfare $0 \le r_1 \le 25$, scriviamo $-19 = (-1) \times 26 + 7$ (oppure usiamo la proprietà $(-a) \bmod m = m - (a \bmod m) = 26 - 19 = 7$). Pertanto $(-19) \bmod 26 = 7$.
>     
>       
>     

## A.2 Gruppi

- **Definizione A.2.1 (Gruppo e Gruppo Abeliano):** Un **gruppo** $(G, \cdot)$ è un insieme $G$ dotato di un'operazione binaria $\cdot$ che soddisfa quattro proprietà (vale anche per l'addizione):
    
      
    1. **Chiusura:** Per ogni $a, b \in G$, si ha $a \cdot b \in G$.
        
          
        
    2. **Associatività:** Per ogni $a, b, c \in G$, vale $(a \cdot b) \cdot c = a \cdot (b \cdot c)$.
        
          
        
    3. **Elemento neutro (identità):** Esiste un elemento $e \in G$ tale che $e \cdot a = a \cdot e = a$ per ogni $a \in G$.
        
          
        
    4. **Elemento inverso:** Per ogni $a \in G$, esiste un elemento $a^{-1} \in G$ tale che $a \cdot a^{-1} = a^{-1} \cdot a = e$. Se inoltre l'operazione è commutativa ($a \cdot b = b \cdot a$ per ogni $a, b \in G$), il gruppo si dice **abeliano** (o commutativo).
        
          
        

> [!example] Esempio A.2.2 (Gruppo Additivo e Gruppo Moltiplicativo)
> 
>   
> 
> - **Gruppo additivo $(\mathbb{Z}_{26}, +)$:** L'insieme $\{0, 1, \dots, 25\}$ con l'addizione modulo $26$ forma un gruppo abeliano finito di ordine $26$: l'elemento neutro è $0$ e l'inverso additivo di ogni $a \in \mathbb{Z}_{26}$ è $(-a) \bmod 26 = (26 - a) \bmod 26$ (usato nel _Shift Cipher_ per decifrare tramite $d_K(y) = (y - K) \bmod 26$).
>     
>       
>     
> - **Gruppo moltiplicativo $(\mathbb{Z}_{26}^*, \cdot)$:** L'insieme degli elementi invertibili modulo $26$, ovvero $\{a \in \mathbb{Z}_{26} : \gcd(a, 26) = 1\} = \{1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25\}$, forma un gruppo abeliano di $12$ elementi rispetto alla moltiplicazione modulo $26$, con elemento neutro $1$ (ad esempio, l'inverso di $7$ è $7^{-1} \bmod 26 = 15$, poiché $7 \times 15 = 105 = 4 \times 26 + 1 \equiv 1 \pmod{26}$).
>     
>       
>     

## A.3 Anelli, Classi di Resto e Omomorfismi

_(Sintesi integrata da Stinson, Appendice A.3, e Lidl & Niederreiter, Cap. 1, §2)_

  

### 1. Definizioni Fondamentali sugli Anelli

- **Definizione A.3.1 (Anello - Ring):** Un anello $R = (X, +, \cdot)$ è un insieme $X$ dotato di due operazioni binarie, addizione ($+$) e moltiplicazione ($\cdot$), tali che:
    
      
    1. $(X, +)$ è un **gruppo abeliano** (chiusura, associatività, elemento neutro $0$, inverso additivo $-a$ e commutatività $a+b = b+a$).
        
          
        
    2. La moltiplicazione $\cdot$ è chiusa e **associativa**: $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ per ogni $a,b,c \in X$.
        
          
        
    3. Valgono le **leggi distributive** del prodotto rispetto alla somma: $a \cdot (b + c) = a \cdot b + a \cdot c$ e $(a + b) \cdot c = a \cdot c + b \cdot c$.
        
          
        
- **Definizione A.3.2 (Tipi speciali di Anelli):**
    
      
    - **Anello Commutativo:** Un anello in cui anche la moltiplicazione è commutativa ($a \cdot b = b \cdot a$).
        
          
        
    - **Anello con Identità (o Unitario):** Un anello che possiede un elemento neutro moltiplicativo $1 \neq 0$ tale che $1 \cdot a = a \cdot 1 = a$.
        
          
        

> [!example] Esempio A.3.3 (Anelli Commutativi e Non Commutativi in Crittografia)
> 
>   
> 
> - **Anello commutativo con identità:** $(\mathbb{Z}_{26}, +, \cdot)$ è un anello commutativo con identità $1$.
>     
>       
>     
> - **Anello NON commutativo con identità:** L'insieme delle matrici quadrate $2 \times 2$ a coefficienti in $\mathbb{Z}_{26}$ (alla base dell'_Hill Cipher_) forma un anello con identità $I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, ma la moltiplicazione righe per colonne tra matrici non è commutativa ($AB \neq BA$).
>     
>       
>     

### 2. Sottoanelli, Ideali e Anelli delle Classi di Resto (Anelli Quoziente)

- **Definizione A.3.3 (Sottoanello - Subring):** Un sottoinsieme non vuoto $S \subseteq R$ è un **sottoanello** di $R$ se è chiuso rispetto alla sottrazione e alla moltiplicazione ($a - b \in S$ e $a \cdot b \in S$ per ogni $a,b \in S$).
    
      
    
- **Definizione A.3.4 (Ideale - Ideal):** Un sottoinsieme non vuoto $J \subseteq R$ è un **ideale** di $R$ se è un sottoanello e "assorbe" la moltiplicazione per qualsiasi elemento dell'anello esterno $R$: per ogni $a \in J$ e per ogni $r \in R$, si ha $ar \in J$ e $ra \in J$.
    
      
    
- **Definizione A.3.5 (Ideale Principale):** Un ideale $J$ di un anello commutativo con identità $R$ è detto **principale** se esiste un elemento $a \in R$ tale che $J$ coincida con l'insieme di tutti i multipli di $a$:
    
      
    
    $$J = (a) = \langle a \rangle = \{r \cdot a : r \in R\}$$
    
    - _Esempio 1 (Negli interi $\mathbb{Z}$):_ Fissato $n = 5$, l'ideale principale dei multipli di $5$ è $5\mathbb{Z} = (5) = \{\dots, -10, -5, 0, 5, 10, \dots\}$. (Nota che qualsiasi numero intero $r \in \mathbb{Z}$ moltiplicato per un multiplo di $5$ dà ancora un multiplo di $5$).
        
          
        
    - _Esempio 2 (Nei polinomi $\mathbb{Z}_2[x]$):_ L'ideale principale generato da $f(x) = x^2 + x + 1$ è l'insieme $(x^2 + x + 1) = \{g(x)(x^2 + x + 1) : g(x) \in \mathbb{Z}_2[x]\}$ di tutti i polinomi divisibili esattamente per $x^2 + x + 1$.
        
          
        
- **Definizione A.3.6 (Classi di Resto - Residue Classes):** Sia $J$ un ideale di $R$. Due elementi $a, b \in R$ sono congrui modulo $J$, scritto $a \equiv b \pmod J$, se la loro differenza appartiene all'ideale ($a - b \in J$). La **classe di resto** di $a$ modulo $J$ è l'insieme:
    
      
    
    $$a + J = [a]_J = [a] = \{a + c : c \in J\}$$
    
- **Teorema A.3.7 (Anello Quoziente):** L'insieme di tutte le classi di resto distinte $R/J$ forma un anello (chiamato **anello delle classi di resto** o **anello quoziente**) rispetto alle operazioni:
    
      
    
    $$[a] + [b] = (a + J) + (b + J) = (a + b) + J = [a + b]$$
    
    $$[a] \cdot [b] = (a + J) \cdot (b + J) = (a \cdot b) + J = [a \cdot b]$$
    
    L'elemento neutro additivo (lo zero di $R/J$) è l'ideale stesso $[0] = 0 + J = J$ (tutti i multipli che stanno in $J$ vengono "schiacciati a zero" nella classe $[0]$).
    
      
    

> [!example] Esempio A.3.8 (Costruzione esplicita delle Classi di Resto in $\mathbb{Z}/(5) = \mathbb{Z}_5$) Prendiamo l'anello $R = \mathbb{Z}$ e l'ideale principale $J = (5) = 5\mathbb{Z}$. Tutto l'insieme infinito $\mathbb{Z}$ si suddivide esattamente in $5$ classi di resto ("scatole") disgiunte, a seconda del resto della divisione per $5$:
> 
>   
> 
> - $[0] = 0 + (5) = \{\dots, -10, -5, \mathbf{0}, 5, 10, 15, \dots\}$ _(lo zero dell'anello quoziente, che coincide con l'ideale $(5)$)_
>     
>       
>     
>       
>     
> - $[1] = 1 + (5) = \{\dots, -9, -4, \mathbf{1}, 6, 11, 16, \dots\}$
>     
>       
>     
>       
>     
> - $[2] = 2 + (5) = \{\dots, -8, -3, \mathbf{2}, 7, 12, 17, \dots\}$
>     
>       
>     
>       
>     
> - $[3] = 3 + (5) = \{\dots, -7, -2, \mathbf{3}, 8, 13, 18, \dots\}$
>     
>       
>     
>       
>     
> - $[4] = 4 + (5) = \{\dots, -6, -1, \mathbf{4}, 9, 14, 19, \dots\}$
>     
>       
>     
>       
>     
> 
> In $\mathbb{Z}/(5) = \mathbb{Z}_5$, sommare $[3] + [4]$ equivale a prendere $[3 + 4] = [7] = [2 + 5] = [2]$.
> 
>   

### 3. Omomorfismi, Isomorfismi e Induzione di Struttura

- **Definizione A.3.8 (Omomorfismo di Anelli):** Una funzione $\phi : R_1 \to R_2$ tra due anelli è un **omomorfismo** se preserva le operazioni di somma e prodotto per ogni $a, b \in R_1$:
    
      
    
    $$\phi(a + b) = \phi(a) + \phi(b) \qquad \text{e} \qquad \phi(a \cdot b) = \phi(a) \cdot \phi(b)$$
    
- **Definizione A.3.9 (Nucleo / Kernel):** Il **Kernel** di un omomorfismo $\phi : R_1 \to R_2$ è il sottoinsieme degli elementi di $R_1$ che vengono mappati nello zero di $R_2$:
    
      
    
    $$\ker(\phi) = \{a \in R_1 : \phi(a) = 0_{R_2}\}$$
    
    _Proprietà fondamentale:_ Il $\ker(\phi)$ è sempre un **ideale** di $R_1$, e $\phi$ è iniettivo se e solo se $\ker(\phi) = \{0_{R_1}\}$.
    
      
    
- **Definizione A.3.10 (Isomorfismo):** Un omomorfismo biunivoco (iniettivo e suriettivo) si chiama **isomorfismo** ($R_1 \cong R_2$), a indicare che i due anelli hanno esattamente la stessa struttura algebrica (cambiano solo i nomi degli elementi).
    
      
    
- **Teorema A.3.11 (Teorema Fondamentale dell'Omomorfismo):** Se $\phi : R_1 \to R_2$ è un omomorfismo di anelli, allora l'anello quoziente delle classi di resto $R_1 / \ker(\phi)$ è isomorfo all'immagine $\text{Im}(\phi) = \phi(R_1)$:
    
      
    
    $$R_1 / \ker(\phi) \cong \phi(R_1)$$
    

> [!example] Esempio A.3.12 (Omomorfismo di riduzione e Kernel su interi e polinomi)
> 
>   
> 
> 1. **Sugli interi:** Sia $\phi : \mathbb{Z} \to \mathbb{Z}_5$ la funzione $\phi(a) = a \bmod 5$. È un omomorfismo suriettivo perché $(a+b)\bmod 5 = (a\bmod 5 + b\bmod 5)\bmod 5$ e $(ab)\bmod 5 = ((a\bmod 5)(b\bmod 5))\bmod 5$. Il suo Kernel è l'insieme degli interi che hanno resto $0$ modulo $5$, cioè l'ideale principale $\ker(\phi) = 5\mathbb{Z} = (5)$. Per il Teorema A.3.11 otteniamo subito $\mathbb{Z}/(5) \cong \mathbb{Z}_5$ (dove ogni classe di resto $[a] \in \mathbb{Z}/(5)$ corrisponde al resto $a \in \mathbb{Z}_5$).
>     
>       
>     
> 2. **Sui polinomi (Valutazione in un punto):** Sia $\phi : \mathbb{Z}_2[x] \to \mathbb{Z}_2$ la mappa che valuta ogni polinomio in $x = 1$, cioè $\phi(g(x)) = g(1) \bmod 2$. È un omomorfismo di anelli il cui Kernel $\ker(\phi) = \{g(x) \in \mathbb{Z}_2[x] : g(1) = 0\}$ coincide con l'ideale principale $(x + 1)$ di tutti i polinomi divisibili per $x + 1$ (cioè tutti i polinomi con un numero pari di termini non nulli, come $x^2 + 1$ o $x^3 + x$).
>     
>       
>     

- **Principio di Induzione della Struttura tramite Biiezione:** Sia $(R, +, \cdot)$ un anello e $S$ un insieme qualsiasi legato a $R$ da una funzione biunivoca $\psi : R \to S$. Possiamo trasferire le operazioni di $R$ su $S$ definendo per ogni $x, y \in S$:
    
      
    
    $$x \oplus y = \psi(\psi^{-1}(x) + \psi^{-1}(y)) \qquad \text{e} \qquad x \odot y = \psi(\psi^{-1}(x) \cdot \psi^{-1}(y))$$
    
    In questo modo $(S, \oplus, \odot)$ diventa automaticamente un anello isomorfo a $R$.
    
      
    - _Esempio pratico in Crittografia (AES e rappresentazione binaria):_ Prendiamo l'anello quoziente delle classi di resto $R = \mathbb{Z}_2[x]/(x^2 + x + 1) = \{[0], [1], [x], [x+1]\}$ e l'insieme delle coppie di bit $S = (\mathbb{Z}_2)^2 = \{00, 01, 10, 11\}$. Usando la biiezione $\psi([ax + b]) = (a, b)_2$ (cioè $[0] \leftrightarrow 00$, $[1] \leftrightarrow 01$, $[x] \leftrightarrow 10$, $[x+1] \leftrightarrow 11$), induciamo su $S$ il prodotto di $\mathbb{F}_4$: ad esempio, per moltiplicare le stringhe di bit $10 \odot 11$, passiamo alle classi di resto $[x] \cdot [x+1] = [x^2 + x] = [1]$ (poiché $x^2 + x + 1 \in (x^2 + x + 1) = [0]$), e torniamo ai bit ottenendo $10 \odot 11 = 01$.
        
          
        

## A.4 Campi (Fields) e Polinomi su Campi

_(Sintesi integrata da Stinson, Appendice A.4, e Lidl & Niederreiter, Cap. 1, §3 e §4)_

  

### 1. Definizione di Campo e Campi Finiti $\mathbb{Z}_n$

- **Definizione A.4.1 (Campo):** Un anello $R = (X, \cdot, +)$ è un **campo** se è un anello commutativo con identità ($1 \neq 0$) in cui **ogni elemento diverso da zero possiede un inverso moltiplicativo** (cioè $R \setminus \{0\}$ forma un gruppo abeliano rispetto alla moltiplicazione).
    
      
    
- **Teorema (Example A.4.2 Stinson / Theorem 1.38 L&N):** L'anello delle classi di resto $(\mathbb{Z}_n, \cdot, +) = \mathbb{Z}/(n)$ è un campo finito **se e solo se** $n$ è un numero primo.
    
      
    - **Dimostrazione:**
        
          
        1. **($\Leftarrow$ Se $n$ è primo):** Per ogni classe di resto non nulla $[b] \in \{[1], \dots, [n-1]\}$, poiché $1 \le b < n$ e $n$ è primo, vale $\gcd(b, n) = 1$. Per l'identità di Bézout esistono interi $s, t$ tali che $sb + tn = 1 (= \gcd(b, n))$. Passando alle classi di resto modulo l'ideale principale $(n)$ (dove $[tn] = [0]$), si ha $[s] \cdot [b] + [tn] = [1] \implies [s] \cdot [b] = [1]$, quindi esiste la classe inversa $[b]^{-1} = [s \bmod n]$ calcolabile con l'Algoritmo Euclideo Esteso. Dunque $\mathbb{Z}/(n) = \mathbb{Z}_n$ è un campo.
            
              
            
        2. **($\Rightarrow$ Se $\mathbb{Z}_n$ è un campo, $n$ è primo - Remark A.4.4):** Per contrapposizione, se $n$ non è primo, ammette una fattorizzazione $n = n_1 n_2$ con $1 < n_1, n_2 < n$. Allora le classi di resto $[n_1] \neq [0]$ e $[n_2] \neq [0]$ in $\mathbb{Z}_n$, ma il loro prodotto appartiene all'ideale $(n)$: $[n_1] \cdot [n_2] = [n_1 n_2] = [n] = [0]$ (sono divisori dello zero). Supponendo per assurdo che $[n_1]$ abbia una classe inversa $[r] \in \mathbb{Z}_n$ tale che $[r] \cdot [n_1] = [1]$, moltiplicando per $[n_2]$ si ha da un lato $([r] \cdot [n_1]) \cdot [n_2] = [1] \cdot [n_2] = [n_2] \neq [0]$, e dall'altro $[r] \cdot ([n_1] \cdot [n_2]) = [r] \cdot [0] = [0]$, ottenendo l'assurdo $[n_2] = [0]$. Pertanto $[n_1]$ non è invertibile e $\mathbb{Z}_n$ non è un campo. $\blacksquare$
            
              
            
- **Remark A.4.3:** Gli inversi moltiplicativi modulo un primo $p$ si calcolano con l'**Algoritmo Euclideo Esteso**.
    
      
    - _Esempio in $\mathbb{Z}_7 = \mathbb{Z}/(7)$:_ Poiché $7$ è primo, $\mathbb{Z}_7$ è un campo. Calcoliamo $[3]^{-1}$ in $\mathbb{Z}/(7)$: dividendo $7 = 2 \times 3 + 1 \implies 1 = 1 \times 7 + (-2) \times 3$. Passando alle classi di resto modulo l'ideale $(7)$ (dove $[7] = [0]$), abbiamo $[1] = [7] + [-2] \cdot [3] = [-2] \cdot [3] = [5] \cdot [3]$. Quindi $[3]^{-1} = [5]$ (infatti $[3] \cdot [5] = [15] = [1 + 2 \times 7] = [1]$).
        
          
        
- **Remark:** Il prodotto diretto tra due campi $A \times B$ non è mai un campo a causa della presenza dei divisori dello zero $(1,0)$ e $(0,1)$, per i quali $(1,0) \cdot (0,1) = (0,0)$.
    
      
    

### 2. Teoria dei Polinomi su un Campo $F[x]$ (da Lidl & Niederreiter, Cap. 1, §3)

Prima di costruire i campi finiti di ordine $p^k$, elenchiamo le definizioni e i teoremi fondamentali sull'anello dei polinomi $F[x]$ a coefficienti in un campo $F$ (come $\mathbb{Z}_p$):

  

- **Definizione (Grado e Polinomio Monico):** Dato un polinomio non nullo $f(x) = a_n x^n + a_{n-1}x^{n-1} + \dots + a_1 x + a_0 \in F[x]$ con $a_n \neq 0$, l'intero $n = \deg(f)$ è chiamato **grado** di $f(x)$, mentre $a_n$ è detto **coefficiente direttivo** (_leading coefficient_). Se $a_n = 1$, il polinomio $f(x)$ si dice **monico**. Per due polinomi non nulli $f, g \in F[x]$ vale sempre:
    
      
    
    $$\deg(f + g) \le \max(\deg(f), \deg(g)) \qquad \text{e} \qquad \deg(f \cdot g) = \deg(f) + \deg(g)$$
    
- **Teorema 1.48 L&N (Algoritmo di Divisione Euclidea per Polinomi):** Sia $g(x) \neq 0$ un polinomio in $F[x]$. Allora per ogni polinomio $f(x) \in F[x]$ esistono e sono **unici** due polinomi $q(x), r(x) \in F[x]$ (detti _quoziente_ e _resto_) tali che:
    
      
    
    $$f(x) = q(x)g(x) + r(x) \qquad \text{con } \deg(r) < \deg(g) \text{ oppure } r(x) = 0$$
    

> [!example] Esempio di Divisione Polinomiale in $\mathbb{Z}_2[x]$ Dividiamo $f(x) = x^4 + x^3 + x + 1$ per $g(x) = x^2 + x + 1$ nell'anello $\mathbb{Z}_2[x]$ (ricordando che in $\mathbb{Z}_2$ somma e sottrazione coincidono):
> 
>   
> 
> 1. Dividiamo i termini di grado massimo: $x^4 / x^2 = x^2$. Moltiplichiamo $x^2(x^2 + x + 1) = x^4 + x^3 + x^2$ e sommiamo a $f(x)$:
>     
>       
>     
>     $$(x^4 + x^3 + x + 1) + (x^4 + x^3 + x^2) = x^2 + x + 1$$
>     
> 2. Dividiamo ancora per $g(x)$: $(x^2 + x + 1) / (x^2 + x + 1) = 1$ con resto $0$!
>     
>     Quindi il quoziente è $q(x) = x^2 + 1$ e il resto è $r(x) = 0$ (ovvero $x^4 + x^3 + x + 1 = (x^2 + 1)(x^2 + x + 1) \in (x^2 + x + 1)$, per cui nella classe di resto modulo $(x^2+x+1)$ vale $[x^4 + x^3 + x + 1] = [0]$).
>     
>       
>     
> 
> Se invece dividiamo $h(x) = x^3 + x$ per $g(x) = x^2 + x + 1$:
> 
>   
> 
> - $x^3 + x = x(x^2 + x + 1) + (x^2) = (x + 1)(x^2 + x + 1) + (\mathbf{x + 1})$, quindi $q(x) = x + 1$ e resto $r(x) = x + 1$ (di grado $1 < 2$). Nelle classi di resto modulo l'ideale $(x^2 + x + 1)$ ciò equivale a scrivere **$[x^3 + x] = [x + 1]$**.
>     
>       
>     

- **Teorema 1.52 L&N ($F[x]$ è un Anello a Ideali Principali - PID):** Ogni ideale $J$ dell'anello dei polinomi $F[x]$ è **principale**, cioè $J = (g(x))$ per un opportuno polinomio generatore $g(x) \in F[x]$ (che è unico se scelto monico).
    
      
    
- **Definizione 1.54 e Teorema 1.55 L&N (Massimo Comune Divisore e Identità di Bézout per Polinomi):** Dati due polinomi non entrambi nulli $f(x), g(x) \in F[x]$, il loro **massimo comune divisore** $\gcd(f(x), g(x))$ è l'unico polinomio **monico** $d(x)$ di grado massimo che divide sia $f(x)$ che $g(x)$. Esso può essere calcolato tramite l'**Algoritmo Euclideo per Polinomi** (divisioni successive dei resti) ed è sempre esprimibile come combinazione lineare polinomiale (**Identità di Bézout**): esistono due polinomi $s(x), t(x) \in F[x]$ tali che:
    
      
    
    $$d(x) = \gcd(f(x), g(x)) = s(x)f(x) + t(x)g(x)$$
    
    Se $\gcd(f(x), g(x)) = 1$, i due polinomi si dicono **coprimi** (o relativamente primi).
    
      
    
- **Definizione 1.57 L&N (Polinomio Irriducibile):** Un polinomio $f(x) \in F[x]$ di grado $\ge 1$ è detto **irriducibile** in $F[x]$ se non può essere scritto come prodotto $f(x) = f_1(x)f_2(x)$ con $f_1, f_2 \in F[x]$ entrambi di grado strettamente positivo ($1 \le \deg(f_i) < \deg(f)$). (Per i polinomi i polinomi irriducibili svolgono esattamente lo stesso ruolo che i numeri primi svolgono per i numeri interi: il **Teorema 1.59 L&N** di Fattorizzazione Unica garantisce che ogni polinomio monico in $F[x]$ si scompone in modo unico nel prodotto di polinomi irriducibili monici).
    
      
    
- **Teorema 1.62 e Corollario 1.64 L&N (Teorema di Ruffini e Test di Irriducibilità per gradi 2 e 3):**
    
      
    1. Un elemento $a \in F$ è una **radice** (o zero) del polinomio $f(x) \in F[x]$ (cioè $f(a) = 0$) **se e solo se** il binomio di primo grado $(x - a)$ divide $f(x)$ in $F[x]$.
        
          
        
    2. **Criterio pratico per gradi $2$ e $3$:** Un polinomio $f(x) \in F[x]$ di grado $2$ oppure $3$ è **irriducibile** in $F[x]$ **se e solo se non possiede radici in $F$** (cioè $f(a) \neq 0$ per tutti gli elementi $a \in F$). _(Infatti, se un polinomio di grado 2 o 3 si fattorizzasse in gradi minori, almeno uno dei fattori dovrebbe avere grado 1, cioè essere della forma $x - a$, dandogli una radice $a \in F$!)._
        
          
        

> [!example] Esempio A.4.5 (Test di Irriducibilità in $\mathbb{Z}_2[x]$ fino al grado 4) Applichiamo il Corollario 1.64 ai polinomi su $\mathbb{Z}_2 = \{0, 1\}$:
> 
>   
> 
> - **Grado 2:**
>     
>       
>     - $f_1(x) = x^2 + 1$: valutiamo in $x=1 \implies f_1(1) = 1 + 1 = 0 \pmod 2$. Ha radice $1$, quindi è divisibile per $x - 1 \equiv x + 1$: infatti $x^2 + 1 = (x+1)(x+1)$ (**riducibile**).
>         
>           
>         
>     - $f_2(x) = x^2 + x$: ha radice $0$ ($f_2(0)=0$) e $1$ ($f_2(1)=0$), infatti $x^2 + x = x(x+1)$ (**riducibile**).
>         
>           
>         
>     - $f_3(x) = x^2 + x + 1$: $f_3(0) = 1 \neq 0$ e $f_3(1) = 1 + 1 + 1 = 1 \neq 0$. Non ha radici in $\mathbb{Z}_2$ ed è di grado 2 $\implies$ **irriducibile**!
>         
>           
>         
> - **Grado 3:**
>     
>       
>     - Un polinomio di grado 3 in $\mathbb{Z}_2[x]$ senza radici in $\{0, 1\}$ deve avere termine noto $1$ (altrimenti $0$ è radice) e un numero dispari di termini non nulli (altrimenti $1$ è radice). Gli unici due polinomi di grado 3 con queste proprietà sono **$x^3 + x + 1$** e **$x^3 + x^2 + 1$**: poiché hanno grado 3 e nessuna radice in $\mathbb{Z}_2$, sono **entrambi irriducibili**!
>         
>           
>         
> - **Attenzione al Grado $\ge 4$:** Per grado $\ge 4$, non avere radici è necessario ma _non sufficiente_! Ad esempio, il polinomio di grado 4 $h(x) = x^4 + x^2 + 1$ non ha radici in $\mathbb{Z}_2$ ($h(0)=1, h(1)=1$), ma è **riducibile** perché è il quadrato dell'irriducibile di grado 2:
>     
>       
>     
>     $$(x^2 + x + 1)(x^2 + x + 1) = x^4 + x^2 + 1 \pmod 2$$
>     
>     Invece $x^4 + x + 1$, $x^4 + x^3 + 1$ e $x^4 + x^3 + x^2 + x + 1$ non hanno radici e non sono divisibili per $x^2+x+1$, quindi sono **irriducibili** di grado 4.
>     
>       
>     

- **Teorema:** Su qualsiasi campo finito $F$ e per ogni intero $k \ge 1$, esiste sempre almeno un polinomio irriducibile di grado $k$ in $F[x]$.
    
      
    

### 3. Costruzione di Campi Finiti (Campi di Galois) e Dimostrazioni Complete

- **Teorema (Esistenza e Unicità dei Campi Finiti):** Esiste un campo finito di ordine $q$ **se e solo se** $q = p^k$, dove $p$ è un numero primo e $k \ge 1$ è un intero positivo. Inoltre, tutti i campi finiti di ordine $q = p^k$ sono isomorfi tra loro.
    
      
    - **Dimostrazione (Necessaria, Sufficiente e Unicità):**
        
          
        1. **Condizione Necessaria ($\Rightarrow$ Se $F$ è un campo finito di ordine $q$, allora $q = p^k$ con $p$ primo e $k \ge 1$ — Lemma 2.1 e Teorema 2.2 L&N):** Sia $F$ un campo finito con $q$ elementi. Poiché $F$ è finito, la sua caratteristica deve essere un numero finito $p \ge 2$ (il più piccolo intero positivo tale che sommando $p$ copie dell'identità $[1]$ si ottenga $[0]$).
            
              
            - **Passo 1a ($p$ deve essere primo):** Se per assurdo $p$ fosse composto ($p = ab$ con $1 < a, b < p$), allora nel campo avremmo $([a] \cdot [1])([b] \cdot [1]) = [ab] \cdot [1] = [p] \cdot [1] = [0]$. Poiché in un campo non esistono divisori dello zero, dovrebbe essere $[a] = [0]$ oppure $[b] = [0]$, contraddicendo la minimalità di $p$. Dunque la caratteristica $p$ è necessariamente un **numero primo**.
                
                  
                
            - **Passo 1b ($F$ come spazio vettoriale su $\mathbb{Z}_p$):** Le classi di resto multiple dell'identità $\{[0], [1], [2], \dots, [p-1]\} \subseteq F$ formano il _sottocampo primo_ isomorfo a $\mathbb{Z}_p = \mathbb{Z}/(p)$ (che ha $p$ classi di resto). Ogni campo finito $F$ può essere visto come uno **spazio vettoriale di dimensione finita** $k \ge 1$ sopra il suo sottocampo primo $\mathbb{Z}_p$. Sia $\{b_1, b_2, \dots, b_k\}$ una base di $F$ su $\mathbb{Z}_p$. Per definizione di base, ogni elemento $x \in F$ si scrive in modo unico come combinazione lineare dei $k$ vettori della base con coefficienti scalari $[a_i] \in \mathbb{Z}_p$:
                
                  
                
                $$x = [a_1] b_1 + [a_2] b_2 + \dots + [a_k] b_k \qquad \text{con } [a_i] \in \mathbb{Z}_p$$
                
                Poiché ciascuno dei $k$ coefficienti $[a_1], \dots, [a_k]$ può assumere indipendentemente esattamente $p$ classi di resto distinte in $\mathbb{Z}_p$, il numero totale di elementi di $F$ è necessariamente:
                
                  
                
                $$q = |F| = \underbrace{p \times p \times \dots \times p}_{k \text{ volte}} = p^k$$
                
        2. **Condizione Sufficiente ($\Leftarrow$ Se $q = p^k$ con $p$ primo e $k \ge 1$, allora esiste un campo finito di ordine $q$):**
            
              
            - **Approccio 1 (Costruttivo via Polinomi Irriducibili — Stinson, Teorema A.4.11):** Poiché per ogni primo $p$ e per ogni intero $k \ge 1$ esiste sempre almeno un polinomio irriducibile $f(x) \in \mathbb{Z}_p[x]$ di grado $k$, l'anello quoziente delle classi di resto $\mathbb{Z}_p[x]/(f(x))$ modulo l'ideale principale $(f(x))$ costituisce un campo finito avente esattamente $p^k = q$ classi di resto $[r(x)]$. _(Se $k=1$, il campo è semplicemente $\mathbb{Z}/(p) = \mathbb{Z}_p$)_.
                
                  
                
            - **Approccio 2 (Algebrico via Campo di Spezzamento — Teorema 2.5 L&N):** Consideriamo il polinomio $g(x) = x^q - x \in \mathbb{Z}_p[x]$ (con $q = p^k$) e sia $F$ il suo campo di spezzamento (_splitting field_) su $\mathbb{Z}_p$. La derivata formale di $g(x)$ in caratteristica $p$ è $g'(x) = q x^{q-1} - 1 = [p^k] x^{q-1} - [1] = [0] - [1] = [-1] \neq [0]$; poiché $g'(x)$ non ha radici comuni con $g(x)$, il polinomio $x^q - x$ ha esattamente $q$ radici tutte distinte in $F$. L'insieme di tutte queste $q$ radici, $S = \{a \in F : a^q - a = 0\} = \{a \in F : a^q = a\}$, forma già da solo un campo: contiene $0$ e $1$, ed essendo in caratteristica $p$ vale $(a \pm b)^q = a^q \pm b^q = a \pm b$ e $(ab^{-1})^q = a^q(b^q)^{-1} = ab^{-1}$ (quindi $S$ è chiuso rispetto a somma, sottrazione, prodotto e inverso). Pertanto $S = F$ è un campo finito con esattamente $q = p^k$ elementi.
                
                  
                
        3. **Unicità a meno di Isomorfismo (Teorema A.4.17 Stinson / Lemma 2.3 e Teorema 2.5 L&N):** Sia $F$ un qualsiasi campo finito di ordine $q = p^k$. Il gruppo moltiplicativo degli elementi non nulli $F^* = F \setminus \{0\}$ è un gruppo finito di ordine $q - 1$. Per il Teorema di Lagrange, ogni elemento non nullo $a \in F^*$ soddisfa $a^{q-1} = 1$. Moltiplicando entrambi i membri per $a$, otteniamo che tutti i $q$ elementi di $F$ (incluso $a = 0$) soddisfano l'equazione:
            
              
            
            $$a^q = a \quad \Longleftrightarrow \quad a^q - a = 0$$
            
            Di conseguenza, in qualsiasi campo finito $F$ di ordine $q$, il polinomio $x^q - x$ si fattorizza completamente come prodotto dei fattori lineari di tutti i suoi elementi:
            
              
            
            $$x^q - x = \prod_{a \in F} (x - a)$$
            
            Pertanto, qualunque campo finito di ordine $q = p^k$ è un campo di spezzamento dello stesso identico polinomio $x^q - x$ sul campo primo $\mathbb{Z}_p$. Poiché per un teorema fondamentale dell'algebra dei campi due campi di spezzamento dello stesso polinomio sullo stesso campo base sono sempre **isomorfi**, segue che tutti i campi finiti di ordine $q = p^k$ sono isomorfi tra loro. $\blacksquare$
            
              
            
- **Definizione (Caratteristica):** Il più piccolo intero positivo $p$ tale che sommando $p$ volte la classe identità $[1]$ si ottenga la classe zero $[0]$ ($[1] + [1] + \dots + [1] = [0]$) è chiamato **caratteristica** del campo. Ogni campo finito di ordine $q = p^k$ ha caratteristica prima $p$.
    
      
    
- **Teorema (Costruzione di Campi Finiti tramite Anello Quoziente — Teorema 1.61 L&N / A.4.11 Stinson):** Sia $p$ un numero primo e $k \ge 1$ un intero. Se $f(x) \in \mathbb{Z}_p[x]$ è un polinomio **irriducibile** di grado $k$, allora l'anello quoziente delle classi di resto modulo l'ideale principale $(f(x))$:
    
      
    
    $$F = \mathbb{Z}_p[x] / (f(x))$$
    
    è un **campo finito di ordine $p^k$**, i cui elementi sono le classi di resto $[r(x)] = r(x) + (f(x))$ rappresentate univocamente da tutti i polinomi $r(x)$ di grado $< k$ a coefficienti in $\mathbb{Z}_p$. _(Equivalenza fondamentale tra Ideale e Classe di Resto: l'ideale principale $(f(x))$ coincide con la classe di resto nulla $[0] = [f(x)]$; pertanto per ogni polinomio $g(x) \in (f(x))$ multiplo di $f(x)$ vale $[g(x)] = [0])$_.
    
      
    - **Dimostrazione (in 2 Parti):**
        
          
        1. **Parte 1 – Cardinalità dell'anello quoziente ($\vert{}F\vert{} = p^k$):** Per il Teorema A.3.7, gli elementi di $F = \mathbb{Z}_p[x]/(f(x))$ sono le classi di resto $[a(x)] = a(x) + (f(x))$. Per il Teorema 1.48 (Divisione Euclidea per polinomi), dividendo qualsiasi polinomio $a(x) \in \mathbb{Z}_p[x]$ per il polinomio $f(x)$ di grado $k$, esistono e sono unici il quoziente $q(x)$ e il resto $r(x)$ tali che:
            
              
            
            $$a(x) = q(x)f(x) + r(x) \qquad \text{con } \deg(r) < k \text{ oppure } r(x) = 0$$
            
            Poiché la differenza $a(x) - r(x) = q(x)f(x)$ è un multiplo di $f(x)$, essa appartiene all'ideale principale $(f(x))$. Per definizione di classe di resto (Def. A.3.6), ciò equivale esattamente a dire che $a(x)$ e $r(x)$ generano la **stessa classe di resto**:
            
              
            
            $$[a(x)] = [q(x)f(x) + r(x)] = \underbrace{[q(x)f(x)]}_{= [0]} + [r(x)] = [r(x)]$$
            
            Ogni classe di resto $[a(x)] \in F$ ha dunque un unico rappresentante canonico $[r(x)]$ di grado strettamente minore di $k$:
            
              
            
            $$[r(x)] = [r_{k-1}x^{k-1} + r_{k-2}x^{k-2} + \dots + r_1 x + r_0]$$
            
            _(Due resti distinti $r(x) \neq r_1(x)$ di grado $< k$ non possono mai appartenere alla stessa classe di resto, perché se fosse $[r(x)] = [r_1(x)]$, allora $r(x) - r_1(x)$ dovrebbe appartenere all'ideale $(f(x))$, ovvero essere divisibile per $f(x)$, il che è impossibile poiché $\deg(r - r_1) < k = \deg(f)$)_. Poiché ciascuno dei $k$ coefficienti $(r_{k-1}, \dots, r_0)$ appartiene a $\mathbb{Z}_p$ e può essere scelto indipendentemente in $p$ modi diversi ($0, 1, \dots, p-1$), il numero totale di classi di resto $[r(x)]$ distinte in $F$ è esattamente:
            
              
            
            $$\underbrace{p \times p \times \dots \times p}_{k \text{ volte}} = p^k$$
            
        2. **Parte 2 – Esistenza dell'inverso moltiplicativo per ogni classe di resto non nulla:**
            
            Poiché $\mathbb{Z}_p[x]$ è un anello commutativo con identità $1$, anche l'anello quoziente $F = \mathbb{Z}_p[x]/(f(x))$ è un anello commutativo con identità $[1]$. Per dimostrare che $F$ è un campo, dobbiamo provare che ogni classe di resto non nulla $[a(x)] \neq [0]$ (rappresentata da un polinomio non nullo $a(x) \in \mathbb{Z}_p[x]$ con $0 \le \deg(a) < k$) possiede una classe inversa $[a(x)]^{-1} \in F$ tale che $[a(x)] \cdot [a(x)]^{-1} = [1]$.
            
            Consideriamo il massimo comune divisore $d(x) = \gcd(a(x), f(x))$ in $\mathbb{Z}_p[x]$:
            
              
            - Per ipotesi **$f(x)$ è irriducibile** di grado $k$, quindi i suoi unici divisori monici in $\mathbb{Z}_p[x]$ sono il polinomio costante $1$ e $f(x)$ stesso (a meno di una costante).
                
                  
                
            - Poiché $a(x) \neq 0$ ha grado $\deg(a) < k = \deg(f)$, il polinomio $f(x)$ di grado $k$ **non può dividere** $a(x)$.
                
                  
                
            - Pertanto l'unico divisore monico comune a $a(x)$ e $f(x)$ è $1$:
                
                  
                
                $$\gcd(a(x), f(x)) = 1$$
                
                Per il Teorema 1.55 (Identità di Bézout per polinomi), esistono due polinomi $s(x), t(x) \in \mathbb{Z}_p[x]$ tali che:
                
                  
                
                $$s(x)f(x) + t(x)a(x) = 1$$
                
                Passando alle classi di resto modulo l'ideale $(f(x))$, applichiamo le operazioni dell'anello quoziente (Teorema A.3.7):
                
                  
                
                $$[s(x)f(x) + t(x)a(x)] = [1] \implies [s(x)f(x)] + [t(x)] \cdot [a(x)] = [1]$$
                
                Poiché $s(x)f(x)$ è un multiplo di $f(x)$, appartiene all'ideale $(f(x)) = [0]$, quindi la sua classe di resto è nulla ($[s(x)f(x)] = [0]$) e l'equazione si riduce a:
                
                  
                
                $$[t(x)] \cdot [a(x)] = [1]$$
                
                Dunque la classe di resto $[t(x) \bmod f(x)]$ è l'**inverso moltiplicativo** $[a(x)]^{-1}$ di $[a(x)]$ in $F$. Ogni classe di resto non nulla di $F$ è invertibile, perciò $\mathbb{Z}_p[x]/(f(x))$ è un campo finito di ordine $p^k$. $\blacksquare$
                
                  
                

> [!example] Esempio A.4.6 (Tabelle complete di Addizione e Moltiplicazione delle Classi di Resto di $\mathbb{F}_4$) Costruiamo il campo di $4$ elementi $\mathbb{F}_4 = \mathbb{Z}_2[x]/(x^2 + x + 1)$ modulo l'ideale principale $J = (x^2 + x + 1)$. Le $4$ classi di resto distinte (i polinomi resto di grado $< 2$) sono:
> 
>   
> 
> $$\mathbb{F}_4 = \{[0], [1], [x], [x+1]\}$$
> 
> Poiché il generatore dell'ideale appartiene alla classe zero, vale $[x^2 + x + 1] = [0]$, da cui la regola di sostituzione nelle classi di resto (ricordando che in $\mathbb{Z}_2$ vale $[-1] = [1]$):
> 
>   
> 
> $$[x^2] = [x + 1]$$
> 
> **Tabella dell'Addizione $+$ tra classi di resto ($[a(x)] + [b(x)] = [a(x) + b(x)]$, XOR dei coefficienti):**
> 
>   
> 
>   
> 
> |**+**|**[0]**|**[1]**|**[x]**|**[x+1]**|
> |---|---|---|---|---|
> |**$[0]$**|$[0]$|$[1]$|$[x]$|$[x+1]$|
> |**$[1]$**|$[1]$|$[0]$|$[x+1]$|$[x]$|
> |**$[x]$**|$[x]$|$[x+1]$|$[0]$|$[1]$|
> |**$[x+1]$**|$[x+1]$|$[x]$|$[1]$|$[0]$|
> 
> **Tabella della Moltiplicazione $\cdot$ tra classi di resto ($[a(x)] \cdot [b(x)] = [a(x)b(x) \bmod (x^2 + x + 1)]$):**
> 
>   
> 
>   
> 
> - $[x] \cdot [x] = [x^2] = [x + 1]$
>     
>       
>     
>       
>     
> - $[x] \cdot [x + 1] = [x^2 + x] = [(x + 1) + x] = [2x + 1] = [1]$
>     
>       
>     
>       
>     
> - $[x + 1] \cdot [x + 1] = [x^2 + 2x + 1] = [x^2 + 1] = [(x + 1) + 1] = [x]$
>     
>       
>     
>       
>     
> 
> |**⋅**|**[0]**|**[1]**|**[x]**|**[x+1]**|
> |---|---|---|---|---|
> |**$[0]$**|$[0]$|$[0]$|$[0]$|$[0]$|
> |**$[1]$**|$[0]$|$[1]$|$[x]$|$[x+1]$|
> |**$[x]$**|$[0]$|$[x]$|$[x+1]$|$[1]$|
> |**$[x+1]$**|$[0]$|$[x+1]$|$[1]$|$[x]$|
> 
> _(Osserva che nella tabella di moltiplicazione ogni classe di resto non nulla contiene la classe identità $[1]$ sulla propria riga: $[1]^{-1} = [1]$, $[x]^{-1} = [x+1]$ e $[x+1]^{-1} = [x]$!)_.
> 
>   

### 4. Inversi Moltiplicativi per Classi di Resto di Polinomi (Algoritmo Euclideo Esteso)

- **Remark A.4.13:** Gli inversi moltiplicativi $[a(x)]^{-1}$ in un campo finito $\mathbb{Z}_p[x]/(f(x))$ si calcolano con l'**Algoritmo Euclideo Esteso per Polinomi**, calcolando una sequenza di resti $r_i(x)$, quozienti $q_i(x)$ e coefficienti di Bézout $s_i(x), t_i(x)$ tali che $s_i(x)f(x) + t_i(x)a(x) = r_i(x)$, fino a ottenere l'ultimo resto non nullo $r_k(x) = 1$. Dall'identità finale $s_k(x)f(x) + t_k(x)a(x) = 1$, passando alle classi di resto modulo l'ideale $(f(x))$ il termine multiplo appartiene a $(f(x)) = [0]$ ($[s_k(x)f(x)] = [0]$), da cui:
    
      
    
    $$[t_k(x)] \cdot [a(x)] = [1] \implies [a(x)]^{-1} = [t_k(x) \bmod f(x)]$$
    

> [!example] Esempio A.4.14 (Svolgimento Passo-Passo dell'Algoritmo Euclideo Esteso in $\mathbb{F}_{16}$) Calcoliamo la classe di resto inversa $[x^3 + x]^{-1}$ nel campo finito $\mathbb{F}_{16} = \mathbb{Z}_2[x]/(x^4 + x + 1)$, dove l'ideale principale è generato dal polinomio irriducibile $f(x) = x^4 + x + 1$ (quindi $[x^4 + x + 1] = [0]$ e in $\mathbb{Z}_2$ vale $- = +$):
> 
>   
> 
> - **Inizializzazione:**
>     
>       
>     - $r_0(x) = x^4 + x + 1$, $\quad t_0(x) = 0$
>         
>           
>         
>     - $r_1(x) = x^3 + x$, $\quad t_1(x) = 1$
>         
>           
>         
> - **Passo 1:** Dividiamo $r_0(x)$ per $r_1(x)$:
>     
>       
>     
>     $$x^4 + x + 1 = \underbrace{x}_{q_1(x)} \cdot (x^3 + x) + \underbrace{(x^2 + x + 1)}_{r_2(x)}$$
>     
>     Aggiorniamo $t_2(x) = t_0(x) + q_1(x)t_1(x) = 0 + x \cdot 1 = \mathbf{x}$.
>     
>       
>     
> - **Passo 2 (Calcolo esatto in $\mathbb{Z}_2[x]$):** Dividendo $r_1(x) = x^3 + x$ per $r_2(x) = x^2 + x + 1$, poiché $(x+1)(x^2+x+1) = x^3 + 1$, si ha:
>     
>       
>     
>     $$x^3 + x = \underbrace{(x + 1)}_{q_2(x)} \cdot (x^2 + x + 1) + \underbrace{(x + 1)}_{r_3(x)}$$
>     
>     Aggiorniamo $t_3(x) = t_1(x) + q_2(x)t_2(x) = 1 + (x + 1)x = \mathbf{x^2 + x + 1}$.
>     
>       
>     
> - **Passo 3:** Dividiamo $r_2(x) = x^2 + x + 1$ per $r_3(x) = x + 1$:
>     
>       
>     
>     $$x^2 + x + 1 = \underbrace{x}_{q_3(x)} \cdot (x + 1) + \underbrace{1}_{r_4(x)}$$
>     
>     Siamo arrivati al resto $r_4(x) = 1$! Calcoliamo $t_4(x)$:
>     
>       
>     
>     $$t_4(x) = t_2(x) + q_3(x)t_3(x) = x + x(x^2 + x + 1) = x + x^3 + x^2 + x = \mathbf{x^3 + x^2}$$
>     
> 
> Otteniamo esattamente l'identità di Bézout del libro in $\mathbb{Z}_2[x]$:
> 
>   
> 
> $$(x^2 + x + 1)(x^4 + x + 1) + (x^3 + x^2)(x^3 + x) = 1$$
> 
> Passando alle classi di resto nell'anello quoziente $\mathbb{Z}_2[x]/(x^4 + x + 1)$, poiché il primo addendo appartiene all'ideale principale $(x^4 + x + 1)$, la sua classe di resto è $[0]$:
> 
>   
> 
> $$\underbrace{[(x^2 + x + 1)(x^4 + x + 1)]}_{= [0]} + [x^3 + x^2] \cdot [x^3 + x] = [1] \implies [x^3 + x^2] \cdot [x^3 + x] = [1]$$
> 
> Pertanto in $\mathbb{Z}_2[x]/(x^4 + x + 1)$ l'inverso della classe $[x^3 + x]$ è **$[x^3 + x]^{-1} = [x^3 + x^2]$**.
> 
>   

### 5. Isomorfismi tra Campi Finiti ed Elementi Primitivi

- **Remark (Isomorfismo Additivo):** Per ogni polinomio $f(x) \in \mathbb{Z}_p[x]$ di grado $k$, il gruppo additivo delle classi di resto $(\mathbb{Z}_p[x]/(f(x)), +)$ è isomorfo allo spazio vettoriale $(\mathbb{Z}_p)^k$ tramite la biiezione $[a_{k-1}x^{k-1} + \dots + a_0] \leftrightarrow (a_{k-1}, \dots, a_0)$.
    
      
    
- **Teorema (Unicità):** Tutti i campi finiti dello stesso ordine $q = p^k$ sono **isomorfi** tra loro e si denotano con **$\mathbb{F}_q$** (o $GF(q)$).
    
      
    
- **Teorema (Ciclicità del Gruppo Moltiplicativo):** Il gruppo moltiplicativo delle classi di resto non nulle $(\mathbb{F}_q \setminus \{[0]\}, \cdot)$ è sempre un **gruppo ciclico** di ordine $q - 1$.
    
      
    
- **Definizione (Elemento Primitivo):** Una classe di resto $\alpha = [g(x)]$ che genera il gruppo moltiplicativo $(\mathbb{F}_q \setminus \{[0]\}, \cdot)$ (tale cioè che le sue potenze $\alpha^0, \alpha^1, \dots, \alpha^{q-2}$ generino tutte le $q-1$ classi di resto non nulle di $\mathbb{F}_q$) si chiama **elemento primitivo** di $\mathbb{F}_q$.
    
      
    

> [!example] Esempio A.4.15 (Elementi Primitivi e Isomorfismo esplicito tra le Classi di Resto di $\mathbb{F}_8$)
> 
>   
> 
> 1. **Potenze della Classe Primitiva $[x]$ in $\mathbb{F}_8$:** Consideriamo $\mathbb{F}_8 = \mathbb{Z}_2[x]/(x^3 + x + 1)$, costruito modulo l'ideale principale $(x^3 + x + 1)$. Il gruppo moltiplicativo $(\mathbb{F}_8 \setminus \{[0]\}, \cdot)$ ha ordine $8 - 1 = 7$ (che è un numero primo, quindi ogni classe di resto diversa da $[0]$ e $[1]$ ha ordine $7$ ed è primitiva!). Poiché il generatore dell'ideale appartiene alla classe zero ($[x^3 + x + 1] = [0]$), vale la relazione tra classi di resto **$[x^3] = [x + 1]$**. Prendendo $\alpha = [x]$ e calcolando le sue potenze $[x]^i = [x^i]$, otteniamo tutte le $7$ classi di resto non nulle del campo:
>     
>       
>     - $[x]^0 = [1]$
>         
>           
>         
>           
>         
>     - $[x]^1 = [x]$
>         
>           
>         
>           
>         
>     - $[x]^2 = [x^2]$
>         
>           
>         
>           
>         
>     - $[x]^3 = [x^3] = [x + 1]$
>         
>           
>         
>           
>         
>     - $[x]^4 = [x] \cdot [x + 1] = [x^2 + x]$
>         
>           
>         
>           
>         
>     - $[x]^5 = [x] \cdot [x^2 + x] = [x^3 + x^2] = [x + 1 + x^2] = [x^2 + x + 1]$
>         
>           
>         
>           
>         
>     - $[x]^6 = [x] \cdot [x^2 + x + 1] = [x^3 + x^2 + x] = [x + 1 + x^2 + x] = [x^2 + 2x + 1] = [x^2 + 1]$
>         
>           
>         
>           
>         
>     - _(Verifica di chiusura del ciclo: $[x]^7 = [x] \cdot [x^2 + 1] = [x^3 + x] = [x + 1 + x] = [1] = [x]^0$)_. _(Nota pratica: questa tabella delle potenze rende immediato il calcolo degli inversi e dei prodotti tra classi! Ad esempio, poiché $[x]^7 = [1]$, l'inverso della classe $[x^2 + x + 1] = [x]^5$ è semplicemente $[x]^{7-5} = [x]^2 = [x^2]$!)._
>         
>           
>         
> 2. **Costruzione dell'Isomorfismo tra i due campi quoziente $\mathbb{F}_8$:** Se costruiamo $\mathbb{F}_8$ usando l'ideale generato dall'altro polinomio irriducibile di grado 3, $R_2 = \mathbb{Z}_2[y]/(y^3 + y^2 + 1)$ (dove $[y^3 + y^2 + 1]_2 = [0]_2$), si verifica facilmente che la classe di resto $[y + 1]_2 \in R_2$ soddisfa:
>     
>       
>     
>     $$[y + 1]^3_2 + [y + 1]_2 + [1]_2 = [y^3 + y^2 + y + 1]_2 + [y + 1]_2 + [1]_2 = [y^3 + y^2 + 1]_2 = [0]_2$$
>     
>     Ovvero la classe di resto $[y + 1]_2$ in $R_2$ soddisfa la stessa identica equazione algebrica ($[x]^3_1 + [x]_1 + [1]_1 = [0]_1$) della classe $[x]_1$ in $R_1 = \mathbb{Z}_2[x]/(x^3 + x + 1)$! Pertanto la mappa $\phi : R_1 \to R_2$ che sostituisce la classe $[x]_1 \mapsto [y + 1]_2$ (cioè $\phi([a(x)]_1) = [a(y + 1)]_2$) è un **isomorfismo di campi** esplicito tra le due costruzioni di $\mathbb{F}_8$.
>
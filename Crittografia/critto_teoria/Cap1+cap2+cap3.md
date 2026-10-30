

# Capitolo 1: Introduzione alla Crittografia

Il Capitolo 1 fornisce una panoramica ad alto livello degli obiettivi fondamentali della crittografia moderna (confidenzialità, integrità dei dati, autenticazione e non ripudio) e degli strumenti matematici e protocollari usati per raggiungerli.

  

## 1.1 Crittosistemi e Strumenti Crittografici di Base

### 1.1.1 Crittosistemi a Chiave Segreta (Simmetrica)

- **Come funzionano:** Due parti (Alice e Bob) scelgono e condividono in anticipo una chiave segreta $K$ attraverso un canale sicuro (ad esempio incontrandosi di persona).
    
      
    
- **Cifratura e Decifratura:** Quando Alice vuole inviare un messaggio in chiaro (_plaintext_) $x$ a Bob su un canale insicuro osservato dall'avversario Oscar, applica la regola di cifratura $y = e_K(x)$ ottenendo il testo cifrato (_ciphertext_) $y$. Bob riceve $y$ e recupera $x$ tramite la funzione di decifratura $x = d_K(y)$.
    
      
    
- **Caratteristica critica:** Nei sistemi a chiave segreta (o _simmetrica_), la regola di decifratura $d_K$ è uguale a $e_K$ oppure è facilmente derivabile da essa. Di conseguenza, l'esposizione di una qualsiasi delle due rende l'intero sistema insicuro.
    
      
    

### 1.1.2 Crittosistemi a Chiave Pubblica (Asimmetrica)

- **Il problema dello scambio chiavi:** La crittografia a chiave pubblica (come l'RSA, inventato da Rivest, Shamir e Adleman) elimina la necessità che Alice e Bob debbano concordare preventivamente una chiave segreta condivisa.
    
      
    
- **Doppia chiave:** Bob genera una coppia di chiavi: una **chiave pubblica** (usata da chiunque per cifrare i messaggi destinati a lui tramite $e_K$) e una **chiave privata** (tenuta segreta da Bob e usata per decifrare tramite $d_K$).
    
      
    
- **Il problema dell'autenticità:** Sebbene non serva un canale segreto per scambiare la chiave pubblica, è necessario garantirne l'autenticità (evitare che Oscar sostituisca la chiave pubblica di Bob con la propria), problema risolto tipicamente tramite i **certificati**.
    
      
    

### 1.1.3 Cifrari a Blocchi (Block Ciphers) e Cifrari a Flusso (Stream Ciphers)

I cifrari simmetrici si dividono in due grandi famiglie architetturali:

  

- **Block Ciphers (Cifrari a blocchi):** Dividono il testo in chiaro in blocchi di lunghezza fissa (es. 128 bit) e cifrano ciascun blocco separatamente usando sempre la stessa chiave $K$.
    
      
    
- **Stream Ciphers (Cifrari a flusso):** Generano una sequenza continua di elementi detta _keystream_ ($z_1, z_2, \dots$) a partire dalla chiave $K$ e cifrano il testo in chiaro un carattere (o un bit) alla volta man mano che fluisce.
    
      
    

### 1.1.4 Crittografia Ibrida (Hybrid Cryptography)

- I sistemi a chiave pubblica sono matematicamente pesanti e molto più lenti dei cifrari a chiave segreta.
    
      
    
- Nella pratica si usa la **crittografia ibrida**: si utilizza un protocollo a chiave pubblica all'inizio della comunicazione esclusivamente per scambiarsi una _chiave di sessione_ temporanea, dopodiché si passa a un cifrario simmetrico veloce (a blocchi o a flusso) per cifrare il traffico dati vero e proprio.
    
      
    

## 1.2 Integrità del Messaggio e Autenticazione

Cifrare un messaggio garantisce la _confidenzialità_ (Oscar non può leggerlo), ma non impedisce a un attaccante attivo di modificare i bit in transito o di fingersi Alice. Servono quindi strumenti per l'**integrità** e l'**autenticazione**.

  

- **1.2.1 Message Authentication Codes (MAC):** Strumento simmetrico in cui Alice e Bob condividono una chiave segreta $K$. Alice calcola un tag di autenticazione funzione del messaggio e della chiave e lo invia insieme al messaggio; Bob ricalcola il tag con la stessa chiave per verificare che il messaggio provenga da Alice e non sia stato alterato.
    
      
    
- **1.2.2 Signature Schemes (Schemi di Firma Digitale):** Strumento asimmetrico per l'integrità e l'autenticazione. Alice firma il messaggio usando la propria _chiave privata_, producendo una firma digitale che chiunque può verificare applicando la _chiave pubblica_ di Alice.
    
      
    
- **1.2.3 Nonrepudiation (Non ripudio):** Proprietà fondamentale delle firme digitali. Con un MAC, poiché sia Alice che Bob possiedono la stessa chiave segreta, Bob potrebbe generare da solo un messaggio valido e accusare Alice di averlo mandato (un giudice terzo non potrebbe stabilire chi dei due ha ragione). Con una firma digitale, invece, solo Alice possiede la chiave privata: Alice non può negare (_ripudiare_) di aver firmato un documento valido.
    
      
    
- **1.2.4 Certificates (Certificati Digitali):** Per evitare che Oscar pubblichi la propria chiave pubblica spacciandola per quella di Bob, un'autorità fidata detta **Certification Authority (CA)** firma digitalmente un documento (il _certificato_) che lega in modo indissolubile l'identità di Bob alla sua chiave pubblica.
    
      
    
- **1.2.5 Hash Functions (Funzioni di Hash):** Funzioni matematiche pubbliche (senza chiave) che prendono un input di lunghezza arbitraria e restituiscono un'impronta digitale (_digest_) di lunghezza fissa e ridotta. Sono progettate per essere non invertibili (_one-way_) e prive di collisioni trovabili (impossibile trovare due messaggi diversi con lo stesso hash), e vengono usate costantemente all'interno di MAC e firme digitali.
    
      
    

## 1.3 Modelli di Attacco e Livelli di Sicurezza

> [!important] Principio di Kerckhoffs Nel valutare la sicurezza di un crittosistema si assume sempre che l'avversario (Oscar) conosca perfettamente l'algoritmo di cifratura e decifratura. La sicurezza deve dipendere **esclusivamente** dalla segretezza della chiave $K$.
> 
>   

### Classificazione degli Attacchi (in ordine crescente di potenza dell'avversario)

1. **Ciphertext-only attack (Solo testo cifrato):** Oscar possiede unicamente una o più stringhe di testo cifrato $\mathbf{y}$ intercettate sul canale.
    
      
    
2. **Known-plaintext attack (Testo in chiaro noto):** Oscar possiede una o più coppie di testo in chiaro e relativo testo cifrato $(\mathbf{x}, \mathbf{y})$ cifrate con la stessa chiave.
    
      
    
3. **Chosen-plaintext attack (Testo in chiaro scelto):** Oscar ha accesso temporaneo alla macchina di cifratura: può scegliere dei testi in chiaro $\mathbf{x}$ a suo piacimento e ottenere i corrispondenti testi cifrati $\mathbf{y}$.
    
      
    
4. **Chosen-ciphertext attack (Testo cifrato scelto):** Oscar può scegliere dei testi cifrati $\mathbf{y}$ e ottenere i corrispondenti testi in chiaro decifrati $\mathbf{x}$.
    
      
    

### Livelli di Sicurezza

- **Sicurezza contro la Ricerca Esaustiva (Brute Force):** Un attacco di ricerca esaustiva prova tutte le possibili regole di decifratura $d_K$ finché non appare un testo in chiaro sensato. Una condizione **necessaria ma non sufficiente** affinché un crittosistema sia sicuro è che lo spazio delle chiavi $\mathcal{K}$ sia così vasto da rendere computazionalmente infattibile provarle tutte.
    
      
    
- **Unconditional Security (Sicurezza Incondizionata):** Il crittosistema è matematicamente inviolabile anche se Oscar dispone di potenza di calcolo **infinita**, perché il testo cifrato non contiene informazioni sufficienti a determinare univocamente il testo in chiaro (es. _One-Time Pad_).
    
      
    
- **Computational Security (Sicurezza Computazionale):** Il sistema è violabile in linea di principio, ma richiede una quantità di operazioni talmente elevata da risultare irrealizzabile con le risorse computazionali disponibili in un tempo ragionevole.
    
      
    

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

- **Osservazione sull'iniettività:** La proprietà 4 impone che, fissata $K$, la funzione $e_K$ debba essere **iniettiva** (due messaggi diversi non possono mai cifrarsi nello stesso identico testo cifrato, altrimenti Bob non saprebbe come decifrare univocamente).
    
      
    
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
    
- **Spazio delle chiavi:** $|\mathcal{K}| = 26^m$.
    
      
    

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
    
    - In questo schema, la chiave $K$ può essere vista come costituita dai $2m$ valori $(k_1, \dots, k_m, c_0, \dots, c_{m-1})$ (oppure, se la relazione di ricorrenza è pubblica/nota e fissata in hardware, la chiave segreta consiste nella sola $m$-tupla iniziale $(k_1, \dots, k_m)$).
        
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

Con $26!$ chiavi si procede per deduzione statistica su lettere singole, digrammi, trigrammi e struttura vocalica/consonantica.

  

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

- **Fase 1A (Test di Kasiski):** Si cercano sottostringhe identiche di lunghezza $\ge 3$, si calcolano le distanze $\delta_i$ tra le loro posizioni e si trova $m = \gcd(\delta_1, \delta_2, \dots)$.
    
      
    
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

# Capitolo 3: La Teoria di Shannon, la Segretezza Perfetta e il One-Time Pad

Il Capitolo 3 introduce le nozioni formali di sicurezza crittografica concentrandosi sulla **sicurezza incondizionata** (_unconditional security_), sul **One-Time Pad** e sui concetti matematici di probabilità, teoria dell'informazione e **segretezza perfetta** (_perfect secrecy_) sviluppati da Claude Shannon (1949).

  

## 3.1 Introduzione

- **Obiettivo del capitolo:** Valutare la sicurezza di un crittosistema assumendo che l'avversario (Oscar) disponga di **potenza computazionale illimitata** (_unconditional security_) e conduca un attacco _ciphertext-only_ (osservando un singolo testo cifrato $y$ cifrato con una chiave $K$ usata una sola volta).
    
      
    
- **Perché la sicurezza computazionale non basta da sola:** Molti cifrari (come il Substitution Cipher con $26!$ chiavi) impediscono la ricerca esaustiva della chiave, ma crollano comunque perché la struttura statistica del testo cifrato rivela informazioni sul testo in chiaro.
    
      
    
- **L'approccio probabilistico di Shannon:** Per dimostrare matematicamente se un testo cifrato $y$ tradisce o meno informazioni sul testo in chiaro $x$, dobbiamo modellare la scelta del messaggio e la scelta della chiave come **variabili aleatorie discrete** governate da distribuzioni di probabilità.
    
      
    

## 3.2 Segretezza Perfetta (Perfect Secrecy)

### 3.2.1 Richiami di Probabilità Discreta e Variabili Aleatorie

Per studiare la segretezza perfetta servono quattro strumenti fondamentali del calcolo delle probabilità:

  

1. **Variabili Aleatorie del Crittosistema:**
    
      
    - Sia $\mathbf{P}$ la variabile aleatoria sul testo in chiaro $\mathcal{P}$, con distribuzione di probabilità _a priori_ nota a tutti (incluso Oscar): $\Pr[\mathbf{P} = x]$ (abbreviata in $\Pr[x]$), dove $\sum_{x \in \mathcal{P}} \Pr[x] = 1$.
        
          
        
    - Sia $\mathbf{K}$ la variabile aleatoria sulla chiave $\mathcal{K}$, scelta da Alice e Bob secondo la distribuzione $\Pr[\mathbf{K} = K]$ (abbreviata in $\Pr[K]$), dove $\sum_{K \in \mathcal{K}} \Pr[K] = 1$.
        
          
        
    - **Ipotesi di indipendenza:** La chiave $K$ e il messaggio $x$ vengono scelti in modo **statisticamente indipendente**: $\Pr[\mathbf{P} = x \land \mathbf{K} = K] = \Pr[x] \cdot \Pr[K]$.
        
          
        
2. **Distribuzione di Probabilità sul Testo Cifrato ($\mathcal{C}$):**
    
      
    - **Insieme dei testi cifrati generabili da $K$:** Fissata una chiave $K$, definiamo $C(K) = \{e_K(x) : x \in \mathcal{P}\}$.
        
          
        
    - **Probabilità condizionata $\Pr[y \mid x]$ (di ottenere il cifrato $y$ dato il messaggio $x$):** È la somma delle probabilità di tutte le chiavi $K$ che trasformano esattamente $x$ in $y$:
        
          
        
        $$\Pr[y \mid x] = \sum_{\{K \in \mathcal{K} : x = d_K(y)\}} \Pr[K] = \sum_{\{K \in \mathcal{K} : e_K(x) = y\}} \Pr[K]$$
        
    - **Probabilità assoluta $\Pr[y]$ (Teorema della Probabilità Totale):** La probabilità complessiva di osservare il testo cifrato $y$ sul canale è la media pesata su tutti i possibili testi in chiaro $x$:
        
          
        
        $$\Pr[y] = \sum_{x \in \mathcal{P}} \Pr[x] \Pr[y \mid x] = \sum_{\{K : y \in C(K)\}} \Pr[K] \Pr[d_K(y)]$$
        
3. **Probabilità a Posteriori $\Pr[x \mid y]$ e Teorema di Bayes:** Quando Oscar intercetta $y$, vuole calcolare la probabilità condizionata **a posteriori** $\Pr[x \mid y]$ che il messaggio originale spedito da Alice fosse $x$. Per il **Teorema di Bayes** (assumendo $\Pr[y] > 0$):
    
      
    
    $$\Pr[x \mid y] = \frac{\Pr[x] \Pr[y \mid x]}{\Pr[y]} = \frac{\Pr[x] \sum_{\{K : x = d_K(y)\}} \Pr[K]}{\sum_{\{K : y \in C(K)\}} \Pr[K] \Pr[d_K(y)]}$$
    

> [!example] Example 3.1 (Calcolo di $\Pr[y]$, $\Pr[y \mid x]$ e delle Probabilità a Posteriori $\Pr[x \mid y]$)
> 
> Sia $\mathcal{P} = \{a, b\}$ con probabilità a priori $\Pr[a] = 1/4$ e $\Pr[b] = 3/4$.
> 
> Sia $\mathcal{K} = \{K_1, K_2, K_3\}$ con $\Pr[K_1] = 1/2$ e $\Pr[K_2] = \Pr[K_3] = 1/4$.
> 
> Sia $\mathcal{C} = \{1, 2, 3, 4\}$, e siano le funzioni di cifratura definite dalla seguente **matrice di cifratura**:
> 
>   
> 
> |**Chiave**|**a**|**b**|
> |---|---|---|
> |**$K_1$**|$1$|$2$|
> |**$K_2$**|$2$|$3$|
> |**$K_3$**|$3$|$4$|
> 
> 1. **Calcolo delle probabilità dei testi cifrati $\Pr[y]$:**
>     
>       
>     - $\Pr[1] = \Pr[K_1]\Pr[a] = \frac{1}{2} \times \frac{1}{4} = \mathbf{\frac{1}{8}}$
>         
>           
>         
>     - $\Pr[2] = \Pr[K_1]\Pr[b] + \Pr[K_2]\Pr[a] = \left(\frac{1}{2} \times \frac{3}{4}\right) + \left(\frac{1}{4} \times \frac{1}{4}\right) = \frac{3}{8} + \frac{1}{16} = \mathbf{\frac{7}{16}}$
>         
>           
>         
>     - $\Pr[3] = \Pr[K_2]\Pr[b] + \Pr[K_3]\Pr[a] = \left(\frac{1}{4} \times \frac{3}{4}\right) + \left(\frac{1}{4} \times \frac{1}{4}\right) = \frac{3}{16} + \frac{1}{16} = \mathbf{\frac{1}{4}}$
>         
>           
>         
>     - $\Pr[4] = \Pr[K_3]\Pr[b] = \frac{1}{4} \times \frac{3}{4} = \mathbf{\frac{3}{16}}$
>         
>         _(Verifica: $\frac{1}{8} + \frac{7}{16} + \frac{1}{4} + \frac{3}{16} = 1$)._
>         
>           
>         
> 2. **Calcolo delle probabilità a posteriori $\Pr[x \mid y]$ tramite il Teorema di Bayes:**
>     
>       
>     - Se Oscar intercetta $y = 1$: $\Pr[a \mid 1] = 1$ e $\Pr[b \mid 1] = 0$ (perché solo $a$ può cifrarsi in $1$!).
>         
>           
>         
>     - Se Oscar intercetta $y = 2$: $\Pr[a \mid 2] = \frac{\Pr[a]\Pr[2 \mid a]}{\Pr[2]} = \frac{(1/4)(1/4)}{7/16} = \mathbf{\frac{1}{7}}$, mentre $\Pr[b \mid 2] = \mathbf{\frac{6}{7}}$.
>         
>           
>         
>     - Se Oscar intercetta $y = 3$: $\Pr[a \mid 3] = \frac{(1/4)(1/4)}{1/4} = \mathbf{\frac{1}{4}}$, mentre $\Pr[b \mid 3] = \mathbf{\frac{3}{4}}$.
>         
>           
>         
>     - Se Oscar intercetta $y = 4$: $\Pr[a \mid 4] = 0$ e $\Pr[b \mid 4] = 1$ (perché solo $b$ può cifrarsi in $4$!).
>         
>           
>         
> 
> **Conclusione sull'Esempio 3.1:** Questo crittosistema **NON** ha segretezza perfetta! Sebbene per $y = 3$ valga $\Pr[a \mid 3] = 1/4 = \Pr[a]$, per $y = 1, 2, 4$ le probabilità a posteriori cambiano drasticamente (addirittura con $y=1$ o $y=4$ Oscar scopre con certezza assoluta il messaggio).
> 
>   

### 3.2.2 Definizione Formale di Segretezza Perfetta e Lemmi Equivalenti

> [!abstract] Definizione 3.1: Segretezza Perfetta (Perfect Secrecy) Un crittosistema $(\mathcal{P}, \mathcal{C}, \mathcal{K}, \mathcal{E}, \mathcal{D})$ gode di **segretezza perfetta** se, per ogni elemento di testo in chiaro $x \in \mathcal{P}$ e per ogni elemento di testo cifrato $y \in \mathcal{C}$ (con $\Pr[y] > 0$), la probabilità _a posteriori_ che il testo in chiaro sia $x$, dato che è stato osservato il testo cifrato $y$, è identica alla probabilità _a priori_ che il testo in chiaro sia $x$:
> 
>   
> 
> $$\Pr[x \mid y] = \Pr[x]$$

#### Condizione Equivalente (tramite il Teorema di Bayes)

- Considerando gli $x \in \mathcal{P}$ con $\Pr[x] > 0$ e gli $y \in \mathcal{C}$ con $\Pr[y] > 0$, applicando il Teorema di Bayes $\Pr[x \mid y] = \frac{\Pr[y \mid x]\Pr[x]}{\Pr[y]}$ e dividendo per $\Pr[x] > 0$, si ottiene:
    
      
    
    $$\Pr[x \mid y] = \Pr[x] \quad \forall x \in \mathcal{P}, y \in \mathcal{C} \quad \Longleftrightarrow \quad \Pr[y \mid x] = \Pr[y] \quad \forall x \in \mathcal{P}, y \in \mathcal{C}$$
    
- **Proprietà cruciale (Esercizio 3.6):** Poiché $\Pr[y \mid x]$ dipende esclusivamente dall'algoritmo e dalla distribuzione delle chiavi $\Pr[K]$, se un crittosistema raggiunge la segretezza perfetta per una particolare distribuzione di probabilità sui testi in chiaro, **mantiene la segretezza perfetta per qualsiasi distribuzione di probabilità sui testi in chiaro**.
    
      
    

### 3.2.3 Disuguaglianza Fondamentale sulle Cardinalità ($\vert{}\mathcal{K}\vert{} \ge \vert{}\mathcal{C}\vert{} \ge \vert{}\mathcal{P}\vert{}$)

Supponiamo che un crittosistema $(\mathcal{P}, \mathcal{C}, \mathcal{K}, \mathcal{E}, \mathcal{D})$ abbia segretezza perfetta:

  

1. **Perché $\vert{}\mathcal{C}\vert{} \ge \vert{}\mathcal{P}\vert{}$ (vale in ogni crittosistema):** Ogni funzione di cifratura $e_K : \mathcal{P} \to \mathcal{C}$ deve essere **iniettiva** affinché la decifratura $d_K(e_K(x)) = x$ sia univoca.
    
      
    
2. **Perché $\vert{}\mathcal{K}\vert{} \ge \vert{}\mathcal{C}\vert{}$ (necessario per la segretezza perfetta):** Fissiamo un qualsiasi $x \in \mathcal{P}$. Per ogni $y \in \mathcal{C}$, la condizione di segretezza perfetta impone $\Pr[y \mid x] = \Pr[y] > 0$, quindi deve esistere **almeno una chiave** $K \in \mathcal{K}$ tale che $e_K(x) = y$. Poiché una singola chiave applicata a $x$ produce un solo $y$, servono almeno $\vert{}\mathcal{C}\vert{}$ chiavi distinte:
    
      
    
    $$\vert{}\mathcal{K}\vert{} \ge \vert{}\mathcal{C}\vert{} \ge \vert{}\mathcal{P}\vert{}$$
    

> [!example] Example 3.2 / Theorem 3.1 (Segretezza Perfetta dello Shift Cipher su 1 carattere) Lo Shift Cipher modulo 26 fornisce **segretezza perfetta** quando una chiave $K \in \mathbb{Z}_{26}$ scelta con probabilità uniforme ($\Pr[K] = 1/26$) viene usata per cifrare **un singolo carattere** $x \in \mathbb{Z}_{26}$.
> 
>   
> 
> - **Dimostrazione:** Per ogni $x, y \in \mathbb{Z}_{26}$, l'equazione $(x + K) \equiv y \pmod{26}$ ammette l'unica soluzione $K = (y - x) \bmod 26$. Pertanto:
>     
>       
>     
>     $$\Pr[y \mid x] = \Pr[K = (y - x) \bmod 26] = \frac{1}{26}$$
>     
>       
>     
>     Calcoliamo la probabilità marginale $\Pr[y]$ per qualsiasi $y \in \mathbb{Z}_{26}$:
>     
>       
>     
>     $$\Pr[y] = \sum_{x \in \mathbb{Z}_{26}} \Pr[x] \Pr[y \mid x] = \frac{1}{26} \sum_{x \in \mathbb{Z}_{26}} \Pr[x] = \frac{1}{26} \times 1 = \frac{1}{26}$$
>     
>       
>     
>     Allora, per il Teorema di Bayes:
>     
>       
>     
>     $$\Pr[x \mid y] = \frac{\Pr[x]\Pr[y \mid x]}{\Pr[y]} = \frac{\Pr[x](1/26)}{1/26} = \Pr[x]$$
>     
> - **Cosa succede se Oscar intercetta ad esempio $y = 10$ (`K`)?** Provando tutte le 26 chiavi equiprobabili $K \in \{0, \dots, 25\}$, Oscar ottiene come possibili decifrature $d_K(10) = (10 - K) \bmod 26$ **tutti e 26 i caratteri in chiaro dell'alfabeto**, ciascuno con la sua esatta probabilità a priori $\Pr[x]$. Non può scartare né preferire alcuna chiave o messaggio!
>     
>       
>     
> - **Nota per i cifrari generali:** Per lo stesso principio, il _Substitution Cipher_ è perfettamente sicuro se cifra 1 sola lettera (con $\Pr[\pi] = 1/26!$) e il _Vigenère Cipher_ con keyword di lunghezza $m$ è perfettamente sicuro se cifra un solo blocco di $m$ lettere (con $\Pr[K] = 1/26^m$).
>     
>       
>     

## 3.3 Il Teorema di Shannon e il One-Time Pad

### 3.3.1 Il Teorema di Caratterizzazione di Shannon (Caso $\vert{}\mathcal{K}\vert{} = \vert{}\mathcal{C}\vert{} = \vert{}\mathcal{P}\vert{}$)

> [!important] Teorema 3.2: Teorema di Shannon Sia $(\mathcal{P}, \mathcal{C}, \mathcal{K}, \mathcal{E}, \mathcal{D})$ un crittosistema in cui $\vert{}\mathcal{K}\vert{} = \vert{}\mathcal{C}\vert{} = \vert{}\mathcal{P}\vert{}$. Allora il crittosistema fornisce **segretezza perfetta** se e solo se sono verificate entrambe le seguenti condizioni:
> 
>   
> 
> 1. **Unicità della chiave ponte:** Per ogni $x \in \mathcal{P}$ e per ogni $y \in \mathcal{C}$, esiste **un'unica** chiave $K \in \mathcal{K}$ tale che $e_K(x) = y$.
>     
>       
>     
> 2. **Equiprobabilità delle chiavi:** Ogni chiave $K \in \mathcal{K}$ viene scelta con la stessa identica probabilità uniforme:
>     
>       
>     
>     $$\Pr[K] = \frac{1}{\vert{}\mathcal{K}\vert{}} \quad \forall K \in \mathcal{K}$$
>     

#### Dimostrazione completa del Teorema di Shannon

- **($\Longrightarrow$ Supponiamo che il sistema abbia segretezza perfetta):**
    
      
    1. Fissato $x \in \mathcal{P}$, per ogni $y \in \mathcal{C}$ deve esistere almeno una chiave $K$ tale che $e_K(x) = y$. Poiché $\vert{}\mathcal{K}\vert{} = \vert{}\mathcal{C}\vert{}$, la mappa $K \mapsto e_K(x)$ è biiettiva: esiste _esattamente una_ chiave $K_i$ tale che $e_{K_i}(x_i) = y$ (**Condizione 1 dimostrata**).
        
          
        
    2. Rinominando le $n = \vert{}\mathcal{K}\vert{}$ chiavi in modo che $e_{K_i}(x_i) = y$ per $1 \le i \le n$, per il Teorema di Bayes abbiamo $\Pr[x_i \mid y] = \frac{\Pr[x_i]\Pr[y \mid x_i]}{\Pr[y]} = \frac{\Pr[x_i]\Pr[K_i]}{\Pr[y]}$.
        
          
        
    3. Poiché vale la segretezza perfetta ($\Pr[x_i \mid y] = \Pr[x_i]$), dividendo per $\Pr[x_i]$ otteniamo $\Pr[K_i] = \Pr[y]$ per ogni $1 \le i \le n$. Tutte le chiavi hanno quindi la stessa probabilità costante $\Pr[y]$, che dovendo sommare a $1$ vale necessariamente $\Pr[K_i] = 1/\vert{}\mathcal{K}\vert{}$ (**Condizione 2 dimostrata**).
        
          
        
- **($\Longleftarrow$ Supponiamo che valgano le Condizioni 1 e 2):** Per ogni $x \in \mathcal{P}$ e $y \in \mathcal{C}$ esiste un'unica chiave $K$ tale che $e_K(x) = y$, con $\Pr[K] = 1/\vert{}\mathcal{K}\vert{}$, quindi $\Pr[y \mid x] = 1/\vert{}\mathcal{K}\vert{}$. Allora $\Pr[y] = \sum_{x \in \mathcal{P}} \Pr[x] \frac{1}{\vert{}\mathcal{K}\vert{}} = \frac{1}{\vert{}\mathcal{K}\vert{}} = \Pr[y \mid x]$, che per Bayes equivale a $\Pr[x \mid y] = \Pr[x]$. $\blacksquare$
    
      
    

> [!example] Esempio di Matrice di Cifratura con Segretezza Perfetta (Quadrati Latini e Caso $\vert{}\mathcal{K}\vert{} > \vert{}\mathcal{C}\vert{} > \vert{}\mathcal{P}\vert{}$)
> 
>   
> 
> 1. **Caso $\vert{}\mathcal{K}\vert{} = \vert{}\mathcal{C}\vert{} = \vert{}\mathcal{P}\vert{} = 4$ (Quadrato Latino):** Se $\mathcal{P} = \mathcal{C} = \{1, 2, 3, 4\}$ e $\mathcal{K} = \{K_1, K_2, K_3, K_4\}$ con $\Pr[K_i] = 1/4$, una matrice di cifratura dà segretezza perfetta se e solo se è un **Quadrato Latino** (ogni simbolo di $\mathcal{C}$ compare esattamente una volta in ogni riga e una volta in ogni colonna). (Attenzione alla Tabella dell'Esercizio 5.15 vista nel libro: lì compare una matrice $6 \times 4$ in cui i simboli $\{1, 2, 3\}$ compaiono esattamente 2 volte per colonna, usata per costruire famiglie di hash fortemente universali).
>     
>       
>     
> 2. **Caso generale con cardinalità diverse (Esercizio 3.4 del libro):** Sia $\mathcal{P} = \{a, b\}$, $\mathcal{C} = \{1, 2, 3, 4\}$ e $\mathcal{K} = \{K_1, K_2, K_3, K_4, K_5, K_6\}$ ($\vert{}\mathcal{K}\vert{} = 6 > \vert{}\mathcal{C}\vert{} = 4 > \vert{}\mathcal{P}\vert{} = 2$). Se la matrice di cifratura ha righe:
>     
>     $K_1: (1, 2), \; K_2: (2, 3), \; K_3: (3, 4), \; K_4: (4, 1), \; K_5: (1, 3), \; K_6: (2, 4)$
>     
>     allora scegliendo probabilità non uniformi per le chiavi (es. $\Pr[K_1]=\Pr[K_3]=p$, $\Pr[K_2]=\Pr[K_4]=q$, $\Pr[K_5]=\Pr[K_6]=r$ con $2p+2q+2r=1$), si ottiene comunque $\Pr[y \mid a] = \Pr[y \mid b]$ per ogni $y \in \{1, 2, 3, 4\}$, realizzando la segretezza perfetta anche con chiavi non equiprobabili perché $\vert{}\mathcal{K}\vert{} > \vert{}\mathcal{C}\vert{}$.
>     
>       
>     

### 3.3.2 Il One-Time Pad (Cifrario di Vernam)

> [!abstract] Cryptosystem 3.1: One-Time Pad Sia $n \ge 1$ un intero positivo. Si definisce $\mathcal{P} = \mathcal{C} = \mathcal{K} = (\mathbb{Z}_2)^n$ (tutte le stringhe binarie di lunghezza $n$). Per una chiave $K = (K_1, \dots, K_n) \in (\mathbb{Z}_2)^n$ scelta con probabilità uniforme $\Pr[K] = 2^{-n}$, la cifratura e la decifratura per ogni $x = (x_1, \dots, x_n), y = (y_1, \dots, y_n) \in (\mathbb{Z}_2)^n$ sono definite dalla somma vettoriale modulo 2 (**XOR bit a bit**, $\oplus$):
> 
>   
> 
> $$e_K(x) = (x_1 + K_1, \dots, x_n + K_n) \bmod 2 = x \oplus K$$
> 
>   
> 
> $$d_K(y) = (y_1 + K_1, \dots, y_n + K_n) \bmod 2 = y \oplus K$$
> 
>   

> [!example] Esempio Numerico del One-Time Pad e Attacco al Riutilizzo della Chiave
> 
>   
> 
> 1. **Cifratura e Decifratura ($n = 5$):**
>     
>       
>     - Sia il plaintext $x = (1, 0, 1, 1, 0)$ e la chiave casuale estratta $K = (0, 1, 1, 0, 1)$ (con $\Pr[K] = 1/2^5 = 1/32$).
>         
>           
>         
>     - **Cifratura:** $y = x \oplus K = (1+0, 0+1, 1+1, 1+0, 0+1) \bmod 2 = \mathbf{(1, 1, 0, 1, 1)}$.
>         
>           
>         
>     - **Decifratura:** Bob calcola $y \oplus K = (1+0, 1+1, 0+1, 1+0, 1+1) \bmod 2 = \mathbf{(1, 0, 1, 1, 0)} = x$.
>         
>           
>         
> 2. **Dimostrazione di Segretezza Perfetta tramite il Teorema di Shannon:**
>     
>       
>     - $\vert{}\mathcal{P}\vert{} = \vert{}\mathcal{C}\vert{} = \vert{}\mathcal{K}\vert{} = 2^n$.
>         
>           
>         
>     - Ogni chiave ha probabilità $\Pr[K] = 2^{-n}$.
>         
>           
>         
>     - Fissati $x$ e $y$, l'equazione $x \oplus K = y$ ha **un'unica soluzione** $K = x \oplus y$. Per il Teorema 3.2, il One-Time Pad ha segretezza perfetta.
>         
>           
>         
> 3. **Esempio di vulnerabilità se la chiave viene usata due volte (Two-Time Pad):** Se Alice cifra due messaggi $x_1 = \texttt{10110}$ e $x_2 = \texttt{01100}$ con la **stessa chiave** $K = \texttt{01101}$, ottiene $y_1 = \texttt{11011}$ e $y_2 = \texttt{00001}$. Oscar intercetta $y_1, y_2$ e calcola:
>     
>       
>     
>     $$y_1 \oplus y_2 = \texttt{11011} \oplus \texttt{00001} = \texttt{11010} = x_1 \oplus x_2$$
>     
>       
>     
>     La chiave $K$ è sparita del tutto e Oscar conosce esattamente in quali bit i due messaggi in chiaro coincidono (dove c'è `0`) e in quali differiscono (dove c'è `1`)!
>
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
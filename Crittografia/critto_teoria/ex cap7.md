# Soluzione Dettagliata degli Esercizi 7.4 e 7.5 (Capitolo 7)

## Esercizio 7.4

> Supponiamo che $p$ sia un numero primo dispari (*odd prime*) e $k$ sia un intero positivo. Il gruppo moltiplicativo $\mathbb{Z}_{p^k}^*$ ha ordine $p^{k-1}(p - 1)$, ed è noto essere ciclico. Un generatore per questo gruppo è chiamato un **primitive element modulo** $p^k$ (o **primitive root modulo** $p^k$).
>
> * **(a)** Supponiamo che $\alpha$ sia un *primitive element* modulo $p$. Dimostrare che almeno uno tra $\alpha$ oppure $\alpha + p$ è un *primitive element* modulo $p^2$.
>
> * **(b)** Descrivere come verificare in modo efficiente che $3$ è una *primitive root* modulo $29$ e modulo $29^2$. *(Nota: Si può dimostrare che se* $\alpha$ *è una primitive root modulo* $p$ *e modulo* $p^2$*, allora è una primitive root modulo* $p^k$ *per tutti gli interi positivi* $k$*. Pertanto, ne segue che* $3$ *è una primitive root modulo* $29^k$ *per tutti gli interi positivi* $k$*).*
>
> * **(c)** Trovare un intero $\alpha$ che sia una *primitive root* modulo $29$ ma **non** una *primitive root* modulo $29^2$.
>
> * **(d)** Utilizzare il `POHLIG-HELLMAN ALGORITHM` per calcolare il logaritmo discreto di $3344$ in base $3$ nel gruppo moltiplicativo $\mathbb{Z}_{24389}^*$.

### Soluzione del Punto (a) – Dimostrazione Formale

> Dimostrazione che almeno uno tra $\alpha$ e $\alpha + p$ è un elemento primitivo modulo $p^2$
> Sia $\alpha \in \mathbb{Z}_p^*$ un **primitive element** modulo $p$. Per definizione (Parte I, Sezione A.2.3), l'ordine di $\alpha$ nel gruppo moltiplicativo $\mathbb{Z}_p^*$ è uguale a:
> 
>
> $$
> \vert{}\mathbb{Z}_p^*\vert{} = \phi(p) = p - 1
> $$
>
> 
> Consideriamo ora il gruppo moltiplicativo $\mathbb{Z}_{p^2}^*$, il quale è ciclico e ha ordine:
> 
>
> $$
> \vert{}\mathbb{Z}_{p^2}^*\vert{} = \phi(p^2) = p(p - 1)
> $$
>
> 
> Poiché $\alpha$ è un elemento primitivo modulo $p$, si ha $\gcd(\alpha, p) = 1$, e di conseguenza $\gcd(\alpha, p^2) = 1$ e $\gcd(\alpha + p, p^2) = 1$; pertanto sia $\alpha$ sia $\alpha + p$ appartengono a $\mathbb{Z}_{p^2}^*$.
>
> **Passo 1: Caratterizzazione dei possibili ordini in** $\mathbb{Z}_{p^2}^*$
> Sia $\beta \in \{\alpha, \alpha + p\}$ e sia $d$ l'**order** di $\beta$ in $\mathbb{Z}_{p^2}^*$ (ovvero il più piccolo intero positivo $d$ tale che $\beta^d \equiv 1 \pmod{p^2}$).
>
> 1. Per il **Lagrange's Theorem**, l'ordine $d$ di $\beta$ deve dividere l'ordine del gruppo $\vert{}\mathbb{Z}_{p^2}^*\vert{} = p(p - 1)$, ovvero:
>    
>
>    $$
>    d \mid p(p - 1)
>    $$
>
> 2. D'altra parte, poiché $\beta \equiv \alpha \pmod p$ e $\beta^d \equiv 1 \pmod{p^2}$, riducendo la congruenza modulo $p$ si ottiene:
>    
>
>    $$
>    \alpha^d \equiv \beta^d \equiv 1 \pmod p
>    $$
>
>    
>    Per le proprietà algebriche dell'ordine di un elemento (Parte I, Sezione A.2.4, Proprietà 2), poiché $\alpha$ ha ordine $p - 1$ modulo $p$, segue che:
>    
>
>    $$
>    (p - 1) \mid d
>    $$
>
> Combinando le due condizioni $(p - 1) \mid d$ e $d \mid p(p - 1)$, ed essendo $p$ un numero primo, gli unici due valori possibili per l'ordine $d$ di $\beta$ in $\mathbb{Z}_{p^2}^*$ sono:
> 
>
> $$
> d = p - 1 \qquad \text{oppure} \qquad d = p(p - 1)
> $$
>
> **Passo 2: Analisi dei due casi per** $\alpha$ **e** $\alpha + p$
>
> * **Caso 1:** Se l'ordine di $\alpha$ modulo $p^2$ è $d = p(p - 1)$, allora $\alpha$ genera l'intero gruppo $\mathbb{Z}_{p^2}^*$ ed è già un **primitive element** modulo $p^2$. La tesi è quindi verificata.
>
> * **Caso 2:** Supponiamo invece che $\alpha$ **non** sia un elemento primitivo modulo $p^2$. Allora il suo ordine modulo $p^2$ deve necessariamente essere $d = p - 1$, il che significa che:
>   
>
>   $$
>   \alpha^{p-1} \equiv 1 \pmod{p^2}
>   $$
>
>   
>   Esaminiamo in questo caso l'elemento $\alpha + p$ ed eleviamolo alla potenza $p - 1$ applicando lo sviluppo del binomio di Newton:
>   
>
>   $$
>   (\alpha + p)^{p-1} = \alpha^{p-1} + \binom{p-1}{1}\alpha^{p-2}p + \binom{p-1}{2}\alpha^{p-3}p^2 + \dots + p^{p-1}
>   $$
>
>   
>   Riducendo modulo $p^2$, tutti i termini della sommatoria che contengono una potenza $p^j$ con $j \ge 2$ sono multipli di $p^2$ e quindi congrui a $0 \pmod{p^2}$. Rimangono soltanto i primi due termini:
>   
>
>   $$
>   (\alpha + p)^{p-1} \equiv \alpha^{p-1} + (p - 1)p\alpha^{p-2} \pmod{p^2}
>   $$
>
>   
>   Sfruttando l'ipotesi del Caso 2 ($\alpha^{p-1} \equiv 1 \pmod{p^2}$) e osservando che $(p - 1)p = p^2 - p \equiv -p \pmod{p^2}$, otteniamo:
>   
>
>   $$
>   (\alpha + p)^{p-1} \equiv 1 - p\alpha^{p-2} \pmod{p^2}
>   $$
>
>   
>   Affinché $(\alpha + p)^{p-1}$ sia congruo a $1 \pmod{p^2}$, dovrebbe valere:
>   
>
>   $$
>   p\alpha^{p-2} \equiv 0 \pmod{p^2} \iff \alpha^{p-2} \equiv 0 \pmod p \iff p \mid \alpha
>   $$
>
>   
>   Ma ciò è impossibile perché $\alpha \in \mathbb{Z}_p^*$, quindi $\gcd(\alpha, p) = 1$ (ovvero $p \nmid \alpha$). Pertanto:
>   
>
>   $$
>   (\alpha + p)^{p-1} \not\equiv 1 \pmod{p^2}
>   $$
>
>   
>   Poiché l'ordine di $\alpha + p$ modulo $p^2$ può essere solo $p - 1$ oppure $p(p - 1)$, ed essendo $(\alpha + p)^{p-1} \not\equiv 1 \pmod{p^2}$, l'ordine di $\alpha + p$ non può essere $p - 1$. Di conseguenza, l'ordine di $\alpha + p$ modulo $p^2$ è necessariamente $p(p - 1)$, ovvero $\alpha + p$ è un **primitive element** modulo $p^2$. $\blacksquare$

### Soluzione del Punto (b) – Verifica Efficiente per $\alpha = 3$ modulo $29$ e $29^2$

Per verificare in modo efficiente che un elemento $\alpha$ appartiene ai generatori di un gruppo ciclico finito $G$ di ordine $n$ senza calcolare tutte le $n$ potenze, utilizziamo il criterio basato sui fattori primi di $n$ (Parte I, Sezione A.2.4):

$$
\alpha \text{ ha ordine } n \iff \alpha^{n/q} \not\equiv 1 \quad \text{per ogni fattore primo } q \text{ che divide } n
$$

1. **Verifica che** $3$ **è una *primitive root* modulo** $p = 29$**:**
   L'ordine di $\mathbb{Z}_{29}^*$ è:
   

   $$
   n_1 = p - 1 = 28 = 2^2 \times 7^1
   $$

   
   I fattori primi distinti di $n_1 = 28$ sono $q_1 = 2$ e $q_2 = 7$. Dobbiamo quindi verificare unicamente che $3^{28/2} \not\equiv 1 \pmod{29}$ e $3^{28/7} \not\equiv 1 \pmod{29}$:

   * Per $q_1 = 2$ ($n_1 / 2 = 14$):
     

     $$
     3^{14} \bmod 29 = (3^3)^4 \times 3^2 \bmod 29 = (-2)^4 \times 9 \bmod 29 = 16 \times 9 \bmod 29 = 144 \bmod 29 = 28 \equiv -1 \not\equiv 1 \pmod{29}
     $$

   * Per $q_2 = 7$ ($n_1 / 7 = 4$):
     

     $$
     3^4 \bmod 29 = 81 \bmod 29 = 23 \not\equiv 1 \pmod{29}
     $$

     
     Poiché entrambi i test danno un risultato diverso da $1$, l'elemento $3$ ha ordine $28$ ed è una **primitive root modulo** $29$.

2. **Verifica che** $3$ **è una *primitive root* modulo** $p^2 = 29^2 = 841$**:**
   Il gruppo $\mathbb{Z}_{29^2}^*$ ha ordine:
   

   $$
   n_2 = 29(29 - 1) = 29 \times 28 = 812 = 2^2 \times 7^1 \times 29^1
   $$

   
   Come dimostrato nel **Punto (a)**, poiché sappiamo già che $3$ è una *primitive root* modulo $29$, il suo ordine modulo $29^2$ può essere solamente $28$ oppure $812$. Pertanto, **basta eseguire un unico test**, verificando che $3^{28} \not\equiv 1 \pmod{29^2}$ tramite `SQUARE-AND-MULTIPLY` modulo $841$:
   

   $$
   \begin{aligned} 3^2 \bmod 841 &= 9 \\ 3^4 \bmod 841 &= 81 \\ 3^7 \bmod 841 &= 3^4 \times 3^2 \times 3^1 \bmod 841 = 81 \times 27 \bmod 841 = 2187 \bmod 841 = 505 \\ 3^{14} \bmod 841 &= 505^2 \bmod 841 = 255025 \bmod 841 = 192 \\ 3^{28} \bmod 841 &= 192^2 \bmod 841 = 36864 \bmod 841 = \mathbf{436} \not\equiv 1 \pmod{841} \end{aligned}
   $$

   
   Poiché $3^{28} \equiv 436 \not\equiv 1 \pmod{841}$, l'ordine di $3$ in $\mathbb{Z}_{841}^*$ è $812$. Di conseguenza, $3$ è una **primitive root modulo** $29^2$ (e dunque anche modulo $29^k$ per ogni $k \ge 1$).

### Soluzione del Punto (c) – Costruzione di $\alpha$ primitivo mod $29$ ma non mod $29^2$

Cerchiamo un intero $\alpha$ che sia una *primitive root* modulo $29$, ma il cui ordine modulo $29^2 = 841$ sia $28$ invece di $812$, ovvero tale che:

$$
\alpha^{28} \equiv 1 \pmod{841}
$$

Possiamo determinarlo in due modi equivalenti:

* **Metodo 1 (Costruzione algebrica a partire da** $\alpha_0 = 3$**):**
  Qualsiasi numero della forma $\alpha = 3 + 29k$ (con $k \in \mathbb{Z}_{29}$) soddisfa $\alpha \equiv 3 \pmod{29}$, ed è quindi automaticamente una *primitive root* modulo $29$. Sviluppando $(\alpha)^{28} = (3 + 29k)^{28}$ modulo $29^2 = 841$ come nel Punto (a):
  

  $$
  (3 + 29k)^{28} \equiv 3^{28} + 28 \times 29k \times 3^{27} \equiv 3^{28} - 29k \times 3^{27} \pmod{841}
  $$

  
  Dal Punto (b) sappiamo che $3^{28} \bmod 841 = 436 = 1 + 15 \times 29$. Sostituendo:
  

  $$
  (3 + 29k)^{28} \equiv 1 + 29\left(15 - k \times 3^{27}\right) \pmod{841}
  $$

  
  Affinché valga $(3 + 29k)^{28} \equiv 1 \pmod{841}$, il termine tra parentesi deve essere divisibile per $29$:
  

  $$
  k \times 3^{27} \equiv 15 \pmod{29}
  $$

  
  Poiché per il Teorema di Fermat $3^{28} \equiv 1 \pmod{29}$, moltiplicando entrambi i membri per $3$ otteniamo:
  

  $$
  k \equiv 15 \times 3 \equiv 45 \equiv 16 \pmod{29}
  $$

  
  Scegliendo $k = 16$, otteniamo:
  

  $$
  \alpha = 3 + 16 \times 29 = \mathbf{467}
  $$

  
  Infatti $467 \equiv 3 \pmod{29}$ (quindi è primitivo modulo $29$), ma $467^{28} \bmod 841 = 1$.

* **Metodo 2 (L'esempio positivo più piccolo,** $\alpha = 14$**):**
  Se cerchiamo un valore $\alpha < 29$, basta considerare l'elemento $\alpha = 3^{29} \bmod 841$. Poiché $\gcd(29, 28) = 1$ e $3^{29} \equiv 3^1 \equiv 3 \pmod{29}$ no, ma testando i generatori di $\mathbb{Z}_{29}^*$ (oppure prendendo una qualsiasi radice primitiva $\alpha_0 \in \mathbb{Z}_{29}^*$ elevata alla potenza $29$ modulo $841$), troviamo che per $\alpha = \mathbf{14}$:

  * Modulo $29$: $14^{14} \bmod 29 = 28 \not\equiv 1$ e $14^4 \bmod 29 = 20 \not\equiv 1 \implies \mathbf{14}$ **è una primitive root modulo** $29$.

  * Modulo $29^2 = 841$:
    

    $$
    14^{28} \bmod 841 = \mathbf{1}
    $$

    
    Quindi $\mathbf{14}$ ha ordine $28$ in $\mathbb{Z}_{841}^*$ e **non è una primitive root modulo** $29^2$.
    *(Tutti i* $12$ *valori in \$\\mathbb{Z}\_{841}^*\$ che soddisfano la richiesta sono: $\{14, 60, 137, 221, 374, 416, 425, 467, 620, 704, 781, 827\}$).\*

### Soluzione del Punto (d) – Calcolo di $\log_3 3344$ in $\mathbb{Z}_{24389}^*$ con Pohlig-Hellman

Osserviamo innanzitutto che il modulo del gruppo è una potenza di $29$:

$$
24389 = 29^3
$$


Dal **Punto (b)** sappiamo che $\alpha = 3$ è una *primitive root* modulo $29^3 = 24389$. Pertanto il gruppo moltiplicativo $G = \mathbb{Z}_{24389}^*$ è generato da $\alpha = 3$ e l'ordine $n$ di $\alpha$ è:

$$
n = \vert{}\mathbb{Z}_{29^3}^*\vert{} = 29^2(29 - 1) = 841 \times 28 = \mathbf{23548}
$$


La fattorizzazione in numeri primi di $n$ è:

$$
n = 23548 = 2^2 \times 7^1 \times 29^2
$$


Vogliamo determinare $a = \log_3 3344 \bmod 23548$ (con $\beta = 3344$). Applichiamo il `POHLIG-HELLMAN ALGORITHM` (**Algorithm 7.3**) per ciascuno dei tre fattori primi $q \in \{2, 7, 29\}$ (ricordando che l'inverso di $\alpha = 3$ modulo $24389$ è $\alpha^{-1} = 3^{-1} \bmod 24389 = 16260$, poiché $3 \times 16260 = 48780 = 2 \times 24389 + 2$, anzi $3 \times 8130 = 24390 \equiv 1 \pmod{24389}$, quindi $\alpha^{-1} = 8130$).

#### 1. Fattore $q = 2, \; c = 2$ (Calcolo di $a \bmod 4$)

Poniamo $a \bmod 4 = a_0 + 2a_1$ con $a_0, a_1 \in \{0, 1\}$. L'elemento di ordine $2$ è:

$$
\gamma = \alpha^{n/2} \bmod 24389 = 3^{11774} \bmod 24389 = 24388 \equiv -1
$$


Le potenze di $\gamma$ sono $\gamma^0 = 1$ e $\gamma^1 = 24388$.

* **Iterazione** $j = 0$**:**

  * $\beta_0 = \beta = 3344$

  * $\delta = \beta_0^{n/2^1} \bmod 24389 = 3344^{11774} \bmod 24389 = 1 = \gamma^0 \implies \mathbf{a_0 = 0}$

  * $\beta_1 = \beta_0 \alpha^{-a_0 \cdot 2^0} \bmod 24389 = 3344 \times 3^0 = 3344$

* **Iterazione** $j = 1$**:**

  * $\delta = \beta_1^{n/2^2} \bmod 24389 = 3344^{5887} \bmod 24389 = 24388 = \gamma^1 \implies \mathbf{a_1 = 1}$

Ricomponendo in base $2$:

$$
a \equiv a_0 + a_1 \cdot 2 = 0 + 1 \cdot 2 = \mathbf{2 \pmod 4}
$$

#### 2. Fattore $q = 7, \; c = 1$ (Calcolo di $a \bmod 7$)

Poniamo $a \bmod 7 = a_0$ con $a_0 \in \{0, \dots, 6\}$. L'elemento di ordine $7$ è:

$$
\gamma = \alpha^{n/7} \bmod 24389 = 3^{3364} \bmod 24389 = 18068
$$


Calcoliamo le potenze $\gamma^i \bmod 24389$ per $i = 0, 1, 2, \dots$:

* $\gamma^0 = 1$

* $\gamma^1 = 18068$

* $\gamma^2 = 18068^2 \bmod 24389 = 4850$

* **Iterazione** $j = 0$**:**

  * $\beta_0 = 3344$

  * $\delta = \beta_0^{n/7} \bmod 24389 = 3344^{3364} \bmod 24389 = 4850 = \gamma^2 \implies \mathbf{a_0 = 2}$

Pertanto:

$$
a \equiv \mathbf{2 \pmod 7}
$$

#### 3. Fattore $q = 29, \; c = 2$ (Calcolo di $a \bmod 29^2 = 841$)

Poniamo $a \bmod 841 = a_0 + 29a_1$ con $a_0, a_1 \in \{0, \dots, 28\}$. L'elemento di ordine $29$ è:

$$
\gamma = \alpha^{n/29} \bmod 24389 = 3^{812} \bmod 24389 = 12616
$$

* **Iterazione** $j = 0$**:**

  * $\beta_0 = 3344$

  * $\delta = \beta_0^{n/29} \bmod 24389 = 3344^{812} \bmod 24389 = 11775$

  * Confrontando $\delta = 11775$ con le potenze $\gamma^i \bmod 24389$, si trova $\gamma^{28} \bmod 24389 = 11775 \implies \mathbf{a_0 = 28}$.

  * Aggiorniamo $\beta_1$:
    

    $$
    \beta_1 = \beta_0 \alpha^{-28 \cdot 29^0} \bmod 24389 = 3344 \times (8130)^{28} \bmod 24389 = 6998
    $$

* **Iterazione** $j = 1$**:**

  * $\delta = \beta_1^{n/29^2} \bmod 24389 = 6998^{28} \bmod 24389 = 3365$

  * Confrontando $\delta = 3365$ con le potenze $\gamma^i \bmod 24389$, si trova $\gamma^8 \bmod 24389 = 3365 \implies \mathbf{a_1 = 8}$.

Ricomponendo in base $29$:

$$
a \equiv a_0 + 29a_1 = 28 + 29 \times 8 = 28 + 232 = \mathbf{260 \pmod{841}}
$$

#### 4. Ricomposizione Finale tramite il Chinese Remainder Theorem (Theorem A.3.20)

Dobbiamo risolvere il sistema di congruenze rispetto ai moduli coprimi $m_1 = 4, \; m_2 = 7, \; m_3 = 841$ (con prodotto $M = n = 23548$):

$$
\begin{cases} a \equiv 2 \pmod 4 \\ a \equiv 2 \pmod 7 \\ a \equiv 260 \pmod{841} \end{cases}
$$

Applicando la formula esplicita del **Theorem A.3.20**:

1. **Per** $i = 1$ **(**$m_1 = 4, \; a_1 = 2$**):**
   

   $$
   M_1 = \frac{23548}{4} = 5887 \implies y_1 = 5887^{-1} \bmod 4 = 3^{-1} \bmod 4 = 3
   $$

2. **Per** $i = 2$ **(**$m_2 = 7, \; a_2 = 2$**):**
   

   $$
   M_2 = \frac{23548}{7} = 3364 \implies y_2 = 3364^{-1} \bmod 7 = 4^{-1} \bmod 7 = 2
   $$

3. **Per** $i = 3$ **(**$m_3 = 841, \; a_3 = 260$**):**
   

   $$
   M_3 = \frac{23548}{841} = 28 \implies y_3 = 28^{-1} \bmod 841 = 811 \quad (\text{poiché } 28 \times 811 = 22708 = 27 \times 841 + 1)
   $$

Calcoliamo la combinazione lineare modulo $23548$:

$$
\begin{aligned} a &= (a_1 M_1 y_1 + a_2 M_2 y_2 + a_3 M_3 y_3) \bmod 23548 \\ &= (2 \times 5887 \times 3 + 2 \times 3364 \times 2 + 260 \times 28 \times 811) \bmod 23548 \\ &= (35322 + 13456 + 5904080) \bmod 23548 \\ &= 5952858 \bmod 23548 = \mathbf{18762} \end{aligned}
$$

*(Nota rapida: Poiché le prime due congruenze hanno lo stesso resto* $a \equiv 2 \pmod 4$ *e* $a \equiv 2 \pmod 7$*, esse equivalgono immediatamente ad* $a \equiv 2 \pmod{28}$*; combinandola con* $a \equiv 260 \pmod{841}$ *si ottiene lo stesso risultato).*

> \[!example\] Risultato Finale Esercizio 7.4(d)
> 
>
> $$
> \log_3 3344 = \mathbf{18762} \quad \text{in } \mathbb{Z}_{24389}^*
> $$
>
> 
> *(Verifica:* $3^{18762} \bmod 24389 = 3344$*).*

## Esercizio 7.5

> \[!abstract\] Testo dell'Esercizio 7.5
> Implementare il `POHLIG-HELLMAN ALGORITHM` per trovare i logaritmi discreti in $\mathbb{Z}_p$, dove $p$ è primo e $\alpha$ è un *primitive element*. Utilizzare il programma per trovare:
>
> 1. $\log_5 8563$ in $\mathbb{Z}_{28703}$
>
> 2. $\log_{10} 12611$ in $\mathbb{Z}_{31153}$

### 1. Implementazione in Python del Pohlig-Hellman Algorithm

L'implementazione seguente traduce fedelmente l'**Algorithm 7.3** (`POHLIG-HELLMAN`), includendo l'ottimizzazione $O(c\sqrt{q})$ discussa alla fine della Sezione 7.2.3 tramite lo `SHANKS' ALGORITHM` (**Algorithm 7.1**, *Baby-step Giant-step*) per risolvere ciascun sottoproblema $\delta = (\alpha^{n/q})^i \pmod p$ di ordine $q$, e il **Chinese Remainder Theorem** (**Theorem A.3.20**) con l'`EXTENDED EUCLIDEAN ALGORITHM` (**Algorithm 6.2**) per ricomporre l'esponente finale $a \bmod (p - 1)$.

```
import math
from typing import Dict, List, Tuple


def factorize(n: int) -> Dict[int, int]:
    """
    Scompone l'ordine n = prod(p_i^{c_i}) nei suoi fattori primi distinti.
    Restituisce un dizionario {p_i: c_i}.
    """
    factors: Dict[int, int] = {}
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors[d] = factors.get(d, 0) + 1
            temp //= d
        d += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    return factors


def extended_euclidean(a: int, b: int) -> Tuple[int, int, int]:
    """
    Algorithm 6.2: EXTENDED EUCLIDEAN ALGORITHM(a, b).
    Restituisce (r, s, t) tali che r = gcd(a, b) e s*a + t*b = r.
    """
    a0, b0 = a, b
    t0, t = 0, 1
    s0, s = 1, 0
    q = a0 // b0
    r = a0 - q * b0
    while r > 0:
        temp = t0 - q * t
        t0, t = t, temp
        temp = s0 - q * s
        s0, s = s, temp
        a0, b0 = b0, r
        q = a0 // b0
        r = a0 - q * b0
    r = b0
    return r, s, t


def mod_inverse(b: int, m: int) -> int:
    """Calcola b^{-1} mod m usando l'Extended Euclidean Algorithm."""
    r, _, t = extended_euclidean(m, b % m)
    if r != 1:
        raise ValueError(f"L'inverso di {b} mod {m} non esiste (gcd = {r}).")
    return t % m


def shanks_discrete_log(mod_group: int, q: int, gamma: int, delta: int) -> int:
    """
    Algorithm 7.1: SHANKS(G, q, gamma, delta) in tempo e spazio O(sqrt(q)).
    Risolve gamma^i = delta (mod mod_group) dove gamma = alpha^{n/q} ha ordine q.
    """
    m = math.isqrt(q)
    if m * m < q:
        m += 1

    # Passo 2-3: Tabella L1 delle coppie (gamma^{m*j} mod p : j)
    gamma_m = pow(gamma, m, mod_group)
    L1: Dict[int, int] = {}
    curr = 1
    for j in range(m):
        if curr not in L1:
            L1[curr] = j
        curr = (curr * gamma_m) % mod_group

    # Passo 4-6: Cerca collisione con delta * gamma^{-i} mod p (L2)
    gamma_inv = mod_inverse(gamma, mod_group)
    curr = delta % mod_group
    for i in range(m):
        if curr in L1:
            j = L1[curr]
            return (m * j + i) % q
        curr = (curr * gamma_inv) % mod_group

    raise ValueError("Logaritmo discreto non trovato nel sottogruppo.")


def pohlig_hellman_prime_power(
    mod_group: int, n: int, alpha: int, beta: int, q: int, c: int
) -> Tuple[List[int], int]:
    """
    Algorithm 7.3: POHLIG-HELLMAN(G, n, alpha, beta, q, c).
    Calcola la rappresentazione in base q (a_0, ..., a_{c-1}) di x = log_alpha(beta) mod q^c.
    """
    j = 0
    beta_j = beta % mod_group
    a_digits: List[int] = []

    # L'elemento gamma = alpha^{n/q} ha ordine esatto q
    gamma = pow(alpha, n // q, mod_group)
    alpha_inv = mod_inverse(alpha, mod_group)

    while j <= c - 1:
        # delta <- beta_j^{n / q^{j+1}} mod p
        exp = n // (q ** (j + 1))
        delta = pow(beta_j, exp, mod_group)

        # Trova i tale che delta = alpha^{i*n/q} = gamma^i (in tempo O(sqrt(q)))
        a_j = shanks_discrete_log(mod_group, q, gamma, delta)
        a_digits.append(a_j)

        # beta_{j+1} <- beta_j * alpha^{-a_j * q^j} mod p
        shift_exp = a_j * (q ** j)
        beta_j = (beta_j * pow(alpha_inv, shift_exp, mod_group)) % mod_group
        j += 1

    x_mod_qc = sum(a_digits[i] * (q ** i) for i in range(c))
    return a_digits, x_mod_qc


def chinese_remainder_theorem(remainders: List[int], moduli: List[int]) -> int:
    """
    Theorem A.3.20: Chinese Remainder Theorem.
    Risolve il sistema x = a_i (mod m_i) restituendo l'unica soluzione modulo M.
    """
    M = math.prod(moduli)
    x = 0
    for a_i, m_i in zip(remainders, moduli):
        M_i = M // m_i
        y_i = mod_inverse(M_i, m_i)
        x = (x + a_i * M_i * y_i) % M
    return x


def pohlig_hellman(mod_group: int, n: int, alpha: int, beta: int) -> int:
    """
    Algoritmo completo di Pohlig-Hellman:
    1. Fattorizza l'ordine n = prod(p_i^{c_i})
    2. Esegue Algorithm 7.3 per ogni potenza di primo p_i^{c_i}
    3. Ricompone a = log_alpha(beta) mod n tramite il Teorema Cinese del Resto.
    """
    prime_factors = factorize(n)
    remainders: List[int] = []
    moduli: List[int] = []

    for q, c in sorted(prime_factors.items()):
        _, x_val = pohlig_hellman_prime_power(mod_group, n, alpha, beta, q, c)
        remainders.append(x_val)
        moduli.append(q ** c)

    return chinese_remainder_theorem(remainders, moduli)


if __name__ == "__main__":
    # Verifica Esercizio 7.4(d): log_3(3344) in Z_{24389}^*
    M_74 = 24389
    n_74 = (29 ** 2) * (29 - 1)
    ans_74 = pohlig_hellman(M_74, n_74, 3, 3344)
    print(f"[7.4(d)] log_3(3344) in Z_24389^* = {ans_74} (Verifica: {pow(3, ans_74, M_74) == 3344})")

    # Esercizio 7.5 - Istanza 1: log_5(8563) in Z_{28703}
    p1, alpha1, beta1 = 28703, 5, 8563
    ans_75_1 = pohlig_hellman(p1, p1 - 1, alpha1, beta1)
    print(f"[7.5(1)] log_5(8563) in Z_28703   = {ans_75_1} (Verifica: {pow(alpha1, ans_75_1, p1) == beta1})")

    # Esercizio 7.5 - Istanza 2: log_10(12611) in Z_{31153}
    p2, alpha2, beta2 = 31153, 10, 12611
    ans_75_2 = pohlig_hellman(p2, p2 - 1, alpha2, beta2)
    print(f"[7.5(2)] log_10(12611) in Z_31153 = {ans_75_2} (Verifica: {pow(alpha2, ans_75_2, p2) == beta2})")

```

### 2. Svolgimento Dettagliato – Istanza 1: $\log_5 8563$ in $\mathbb{Z}_{28703}$

* **Parametri dell'istanza:**
  Il modulo $p = 28703$ è primo e $\alpha = 5$ è un **primitive element** modulo $28703$. L'ordine di $\alpha$ in $\mathbb{Z}_{28703}^*$ è:
  

  $$
  n = p - 1 = 28702
  $$

  
  Scomponendo $n = 28702$ in fattori primi otteniamo:
  

  $$
  n = 28702 = 2^1 \times 113^1 \times 127^1
  $$

  
  Vogliamo calcolare $a = \log_5 8563 \bmod 28702$ (con $\beta = 8563$). Poiché tutti gli esponenti nella fattorizzazione di $n$ valgono $c_i = 1$, l'**Algorithm 7.3** esegue una sola iterazione ($j = 0$) per ciascuno dei tre primi.

1. **Fattore** $q = 2, \; c = 1$ **(Calcolo di** $a \bmod 2$**):**

   * $\gamma = \alpha^{n/2} \bmod 28703 = 5^{14351} \bmod 28703 = 28702 \equiv -1$

   * $\delta = \beta_0^{n/2} \bmod 28703 = 8563^{14351} \bmod 28703 = 28702 = \gamma^1 \implies \mathbf{a_0 = 1}$

   * Pertanto:
     

     $$
     a \equiv \mathbf{1 \pmod 2}
     $$

2. **Fattore** $q = 113, \; c = 1$ **(Calcolo di** $a \bmod 113$**):**

   * $\gamma = \alpha^{n/113} \bmod 28703 = 5^{254} \bmod 28703 = 18611$

   * $\delta = \beta_0^{n/113} \bmod 28703 = 8563^{254} \bmod 28703 = 24021$

   * Risolvendo $18611^i \equiv 24021 \pmod{28703}$, si ottiene $\mathbf{a_0 = 67}$.

   * Pertanto:
     

     $$
     a \equiv \mathbf{67 \pmod{113}}
     $$

3. **Fattore** $q = 127, \; c = 1$ **(Calcolo di** $a \bmod 127$**):**

   * $\gamma = \alpha^{n/127} \bmod 28703 = 5^{226} \bmod 28703 = 19749$

   * $\delta = \beta_0^{n/127} \bmod 28703 = 8563^{226} \bmod 28703 = 7538$

   * Risolvendo $19749^i \equiv 7538 \pmod{28703}$, si ottiene $\mathbf{a_0 = 99}$.

   * Pertanto:
     

     $$
     a \equiv \mathbf{99 \pmod{127}}
     $$

4. **Ricomposizione con il Chinese Remainder Theorem (Theorem A.3.20):**
   Risolviamo il sistema modulo $M = n = 28702$:
   

   $$
   \begin{cases} a \equiv 1 \pmod 2 \\ a \equiv 67 \pmod{113} \\ a \equiv 99 \pmod{127} \end{cases}
   $$

   
   Calcoliamo i coefficienti $M_i = M / m_i$ e gli inversi $y_i = M_i^{-1} \bmod m_i$:

   * **Per** $i = 1$ **(**$m_1 = 2, \; a_1 = 1$**):**
     

     $$
     M_1 = \frac{28702}{2} = 14351 \implies y_1 = 14351^{-1} \bmod 2 = 1^{-1} \bmod 2 = 1
     $$

   * **Per** $i = 2$ **(**$m_2 = 113, \; a_2 = 67$**):**
     

     $$
     M_2 = \frac{28702}{113} = 254 \implies y_2 = 254^{-1} \bmod 113 = 28^{-1} \bmod 113 = 109
     $$

   * **Per** $i = 3$ **(**$m_3 = 127, \; a_3 = 99$**):**
     

     $$
     M_3 = \frac{28702}{127} = 226 \implies y_3 = 226^{-1} \bmod 127 = 99^{-1} \bmod 127 = 68
     $$

   Combinando i termini modulo $28702$:
   

   $$
   \begin{aligned} a &= (1 \times 14351 \times 1 + 67 \times 254 \times 109 + 99 \times 226 \times 68) \bmod 28702 \\ &= (14351 + 1854962 + 1521432) \bmod 28702 \\ &= 3390745 \bmod 28702 = \mathbf{3909} \end{aligned}
   $$

> \[!example\] Risultato Finale (Istanza 1)
> 
>
> $$
> \log_5 8563 = \mathbf{3909} \quad \text{in } \mathbb{Z}_{28703}
> $$
>
> 
> *(Verifica:* $5^{3909} \bmod 28703 = 8563$*).*

### 3. Svolgimento Dettagliato – Istanza 2: $\log_{10} 12611$ in $\mathbb{Z}_{31153}$

* **Parametri dell'istanza:**
  Il modulo $p = 31153$ è primo e $\alpha = 10$ è un **primitive element** modulo $31153$. L'ordine di $\alpha$ in $\mathbb{Z}_{31153}^*$ è:
  

  $$
  n = p - 1 = 31152
  $$

  
  La fattorizzazione in numeri primi di $n = 31152$ è:
  

  $$
  n = 31152 = 2^4 \times 3^1 \times 11^1 \times 59^1
  $$

  
  Vogliamo determinare $a = \log_{10} 12611 \bmod 31152$ (con $\beta = 12611$). L'inverso moltiplicativo della base $\alpha = 10$ modulo $31153$ è:
  

  $$
  \alpha^{-1} = 10^{-1} \bmod 31153 = 28038 \quad (\text{poiché } 10 \times 28038 = 280380 = 9 \times 31153 + 3 \dots \text{ anzi } 10 \times 28038 = 280380 = 9 \times 31153 + 3? \text{ Verifica: } 9 \times 31153 = 280377 \implies \alpha^{-1} = 31153 - 3115 = \mathbf{28038}? \text{ No: } 3 \times 31153 + 1 = 93460 \implies \alpha^{-1} = \mathbf{9346})
  $$

  
  Infatti $10 \times 9346 = 93460 = 3 \times 31153 + 1 \equiv 1 \pmod{31153}$.

#### 1. Fattore $q = 2, \; c = 4$ (Calcolo di $a \bmod 16$)

Esprimiamo $a \bmod 16 = a_0 + 2a_1 + 4a_2 + 8a_3$ con $a_j \in \{0, 1\}$. L'elemento di ordine $2$ è:

$$
\gamma = \alpha^{n/2} \bmod 31153 = 10^{15576} \bmod 31153 = 31152 \equiv -1
$$


Le potenze di $\gamma$ sono $\gamma^0 = 1$ e $\gamma^1 = 31152$.

* **Iterazione** $j = 0$**:**

  * $\beta_0 = 12611$

  * $\delta = \beta_0^{31152/2} \bmod 31153 = 12611^{15576} \bmod 31153 = 1 = \gamma^0 \implies \mathbf{a_0 = 0}$

  * $\beta_1 = \beta_0 \alpha^{-0} = 12611$

* **Iterazione** $j = 1$**:**

  * $\delta = \beta_1^{31152/4} \bmod 31153 = 12611^{7788} \bmod 31153 = 31152 = \gamma^1 \implies \mathbf{a_1 = 1}$

  * $\beta_2 = \beta_1 \alpha^{-1 \cdot 2^1} \bmod 31153 = 12611 \times (9346)^2 \bmod 31153 = 4176$

* **Iterazione** $j = 2$**:**

  * $\delta = \beta_2^{31152/8} \bmod 31153 = 4176^{3894} \bmod 31153 = 31152 = \gamma^1 \implies \mathbf{a_2 = 1}$

  * $\beta_3 = \beta_2 \alpha^{-1 \cdot 2^2} \bmod 31153 = 4176 \times (9346)^4 \bmod 31153 = 6879$

* **Iterazione** $j = 3$**:**

  * $\delta = \beta_3^{31152/16} \bmod 31153 = 6879^{1947} \bmod 31153 = 31152 = \gamma^1 \implies \mathbf{a_3 = 1}$

Ricomponendo in base $2$:

$$
a \equiv 0 + 1 \cdot 2 + 1 \cdot 4 + 1 \cdot 8 = \mathbf{14 \pmod{16}}
$$

#### 2. Fattore $q = 3, \; c = 1$ (Calcolo di $a \bmod 3$)

* $\gamma = \alpha^{n/3} \bmod 31153 = 10^{10384} \bmod 31153 = 30976$

* $\delta = \beta_0^{n/3} \bmod 31153 = 12611^{10384} \bmod 31153 = 176$

* Calcolando le potenze di $\gamma$: $\gamma^0 = 1, \; \gamma^1 = 30976, \; \gamma^2 = 30976^2 \bmod 31153 = 176 = \delta \implies \mathbf{a_0 = 2}$.

* Pertanto:
  

  $$
  a \equiv \mathbf{2 \pmod 3}
  $$

#### 3. Fattore $q = 11, \; c = 1$ (Calcolo di $a \bmod 11$)

* $\gamma = \alpha^{n/11} \bmod 31153 = 10^{2832} \bmod 31153 = 2059$

* $\delta = \beta_0^{n/11} \bmod 31153 = 12611^{2832} \bmod 31153 = 30256$

* Confrontando con le potenze di $\gamma$, si trova $\gamma^8 \bmod 31153 = 2059^8 \bmod 31153 = 30256 = \delta \implies \mathbf{a_0 = 8}$.

* Pertanto:
  

  $$
  a \equiv \mathbf{8 \pmod{11}}
  $$

#### 4. Fattore $q = 59, \; c = 1$ (Calcolo di $a \bmod 59$)

* $\gamma = \alpha^{n/59} \bmod 31153 = 10^{528} \bmod 31153 = 19789$

* $\delta = \beta_0^{n/59} \bmod 31153 = 12611^{528} \bmod 31153 = 2816$

* Risolvendo $19789^i \equiv 2816 \pmod{31153}$, si trova $\gamma^{51} \bmod 31153 = 2816 = \delta \implies \mathbf{a_0 = 51}$.

* Pertanto:
  

  $$
  a \equiv \mathbf{51 \pmod{59}}
  $$

#### 5. Ricomposizione con il Chinese Remainder Theorem (Theorem A.3.20)

Risolviamo il sistema di quattro congruenze modulo $M = n = 31152$:

$$
\begin{cases}
a \equiv 14 \pmod{16} \\
a \equiv 2 \pmod 3 \\
a \equiv 8 \pmod{11} \\
a \equiv 51 \pmod{59}
\end{cases}
$$

Calcoliamo $M_i = M / m_i$ e gli inversi $y_i = M_i^{-1} \bmod m_i$:

* **Per** $i = 1$ **(**$m_1 = 16, \; a_1 = 14$**):**
  

  $$
  M_1 = \frac{31152}{16} = 1947 \implies y_1 = 1947^{-1} \bmod 16 = 11^{-1} \bmod 16 = 3
  $$

* **Per** $i = 2$ **(**$m_2 = 3, \; a_2 = 2$**):**
  

  $$
  M_2 = \frac{31152}{3} = 10384 \implies y_2 = 10384^{-1} \bmod 3 = 1^{-1} \bmod 3 = 1
  $$

* **Per** $i = 3$ **(**$m_3 = 11, \; a_3 = 8$**):**
  

  $$
  M_3 = \frac{31152}{11} = 2832 \implies y_3 = 2832^{-1} \bmod 11 = 5^{-1} \bmod 11 = 9
  $$

* **Per** $i = 4$ **(**$m_4 = 59, \; a_4 = 51$**):**
  

  $$
  M_4 = \frac{31152}{59} = 528 \implies y_4 = 528^{-1} \bmod 59 = 56^{-1} \bmod 59 = 39
  $$

Calcoliamo la combinazione lineare modulo $31152$:

$$
\begin{aligned}
a &= (14 \times 1947 \times 3 + 2 \times 10384 \times 1 + 8 \times 2832 \times 9 + 51 \times 528 \times 39) \bmod 31152 \\
&= (81774 + 20768 + 203904 + 1050192) \bmod 31152 \\
&= 1356638 \bmod 31152 = \mathbf{17102}
\end{aligned}
$$

> \[!example\] Risultato Finale (Istanza 2)
> 
>
> $$
> \log_{10} 12611 = \mathbf{17102} \quad \text{in } \mathbb{Z}_{31153}
> $$
>
> 
> *(Verifica:* $10^{17102} \bmod 31153 = 12611$*).*




## Esercizio 7.3

> [!abstract] Testo dell'Esercizio 7.3 L'intero $p = 458009$ è primo e $\alpha = 2$ ha ordine $n = 57251$ in $\mathbb{Z}_p^*$. Utilizzare il `POLLARD RHO ALGORITHM` per calcolare il logaritmo discreto in $\mathbb{Z}_p^*$ di $\beta = 56851$ in base $\alpha$. Prendere il valore iniziale $x_0 = 1$ e definire la partizione $(S_1, S_2, S_3)$ come nell'**Example 7.3**. Trovare il più piccolo intero $i$ tale che $x_i = x_{2i}$, e quindi calcolare il logaritmo discreto desiderato.
> 
>   

### 1. Impostazione Teorica (Sezione 7.2.2, Algorithm 7.2)

Nel gruppo moltiplicativo $G = \mathbb{Z}_{458009}^*$, l'elemento $\alpha = 2$ genera un sottogruppo ciclico $\langle \alpha \rangle$ di ordine $n = 57251$ (che è un numero primo, dato che $p - 1 = 458008 = 8 \times 57251$). Tutte le moltiplicazioni tra elementi del gruppo ($x_i \in \langle \alpha \rangle$) vengono eseguite **modulo $p = 458009$**, mentre tutte le operazioni sugli esponenti ($a_i, b_i \in \mathbb{Z}_n$) vengono ridotte **modulo $n = 57251$**.

  

1. **Partizione del gruppo $(S_1, S_2, S_3)$:** Come nell'**Example 7.3**, partizioniamo $\mathbb{Z}_{458009}^*$ in tre sottoinsiemi in base al resto modulo $3$ (osservando che $1 \in S_1$ e quindi $1 \notin S_2$, evitando cicli banali su $(1, 0, 0)$):
    
      
    
    $$\begin{aligned} S_1 &= \{ x \in \mathbb{Z}_{458009}^* : x \equiv 1 \pmod 3 \} \\ S_2 &= \{ x \in \mathbb{Z}_{458009}^* : x \equiv 0 \pmod 3 \} \\ S_3 &= \{ x \in \mathbb{Z}_{458009}^* : x \equiv 2 \pmod 3 \} \end{aligned}$$
    
2. **Funzione iterativa $f$ e proprietà invariante:** Partendo dalla tripla iniziale $(x_0, a_0, b_0) = (1, 0, 0)$, definiamo per ogni $i \ge 1$ la sequenza $(x_i, a_i, b_i) = f(x_{i-1}, a_{i-1}, b_{i-1})$ tramite la funzione:
    
      
    
    $$f(x, a, b) = \begin{cases} (\beta x \bmod p, \; a, \; (b + 1) \bmod n) & \text{se } x \in S_1 \quad (x \equiv 1 \pmod 3) \\ (x^2 \bmod p, \; 2a \bmod n, \; 2b \bmod n) & \text{se } x \in S_2 \quad (x \equiv 0 \pmod 3) \\ (\alpha x \bmod p, \; (a + 1) \bmod n, \; b) & \text{se } x \in S_3 \quad (x \equiv 2 \pmod 3) \end{cases}$$
    
    Ad ogni passo è preservata la **proprietà invariante**:
    
      
    
    $$x_i \equiv \alpha^{a_i} \beta^{b_i} \pmod p$$
    
3. **Condizione di collisione ($x_i = x_{2i}$) ed equazione risolutiva:** Quando si individua il più piccolo indice $i \ge 1$ tale che $x_i = x_{2i}$, posto $c = \log_\alpha \beta$, vale:
    
      
    
    $$\alpha^{a_{2i}} \beta^{b_{2i}} \equiv \alpha^{a_i} \beta^{b_i} \pmod p \iff \alpha^{a_{2i} + c b_{2i}} \equiv \alpha^{a_i + c b_i} \pmod p$$
    
    Poiché $\alpha$ ha ordine $n = 57251$, gli esponenti sono congrui modulo $n$:
    
      
    
    $$c(b_{2i} - b_i) \equiv a_i - a_{2i} \pmod n$$
    
    Se $\gcd(b_{2i} - b_i, n) = 1$, l'unica soluzione modulo $n$ è data da:
    
      
    
    $$c = (a_i - a_{2i})(b_{2i} - b_i)^{-1} \bmod n$$
    

### 2. Implementazione in Python dell'Algorithm 7.2

Python

```
from typing import Tuple

def f_step(x: int, a: int, b: int, p: int, n: int, alpha: int, beta: int) -> Tuple[int, int, int]:
    """Procedura f(x, a, b) dell'Algorithm 7.2 con partizione basata su x mod 3."""
    rem = x % 3
    if rem == 1:      # x in S_1
        return (beta * x) % p, a, (b + 1) % n
    elif rem == 0:    # x in S_2
        return (x * x) % p, (2 * a) % n, (2 * b) % n
    else:             # x in S_3 (rem == 2)
        return (alpha * x) % p, (a + 1) % n, b

def pollard_rho_dlog(p: int, n: int, alpha: int, beta: int) -> None:
    """Algorithm 7.2: POLLARD RHO DISCRETE LOG ALGORITHM(G, n, alpha, beta)."""
    # Inizializzazione i = 0: (x_0, a_0, b_0) = (1, 0, 0)
    x_i, a_i, b_i = 1, 0, 0
    x_2i, a_2i, b_2i = 1, 0, 0
    
    i = 0
    while True:
        i += 1
        # Passo singolo (tartaruga): (x_i, a_i, b_i)
        x_i, a_i, b_i = f_step(x_i, a_i, b_i, p, n, alpha, beta)
        # Passo doppio (lepre): (x_{2i}, a_{2i}, b_{2i})
        x_2i, a_2i, b_2i = f_step(x_2i, a_2i, b_2i, p, n, alpha, beta)
        x_2i, a_2i, b_2i = f_step(x_2i, a_2i, b_2i, p, n, alpha, beta)
        
        if x_i == x_2i:
            break

    diff_a = (a_i - a_2i) % n
    diff_b = (b_2i - b_i) % n
    inv_diff_b = pow(diff_b, -1, n)
    c = (diff_a * inv_diff_b) % n

    print(f"Collisione trovata a i = {i}:")
    print(f"  (x_{i}, a_{i}, b_{i})   = ({x_i}, {a_i}, {b_i})")
    print(f"  (x_{2*i}, a_{2*i}, b_{2*i}) = ({x_2i}, {a_2i}, {b_2i})")
    print(f"Logaritmo discreto c = {c} (Verifica: {pow(alpha, c, p) == beta})")

if __name__ == "__main__":
    pollard_rho_dlog(p=458009, n=57251, alpha=2, beta=56851)
```

### 3. Svolgimento Numerico e Calcolo del Logaritmo Discreto

1. **Primi passi dell'iterazione e individuazione della collisione:** Partendo da $(x_0, a_0, b_0) = (1, 0, 0)$:
    
      
    
    - Poiché $1 \equiv 1 \pmod 3 \implies 1 \in S_1$, per $i = 1$ abbiamo $(x_1, a_1, b_1) = (56851 \times 1 \bmod 458009, \; 0, \; 1) = (56851, 0, 1)$.
        
          
        
    - Poiché $56851 \equiv 1 \pmod 3 \implies 56851 \in S_1$, per $i = 2$ abbiamo $(x_2, a_2, b_2) = (56851^2 \bmod 458009, \; 0, \; 2) = (324697, 0, 2)$.
        
          
        
    
    Proseguendo iterativamente, riportiamo i primi passi e il punto di collisione:
    
      
    
    |**i**|**(xi​,ai​,bi​)**|**(x2i​,a2i​,b2i​)**|
    |---|---|---|
    |$1$|$(56851, \; 0, \; 1)$|$(324697, \; 0, \; 2)$|
    |$2$|$(324697, \; 0, \; 2)$|$(424840, \; 1, \; 3)$|
    |$3$|$(212420, \; 0, \; 3)$|$(232522, \; 2, \; 8)$|
    |$4$|$(424840, \; 1, \; 3)$|$(295215, \; 4, \; 18)$|
    |$5$|$(390243, \; 1, \; 4)$|$(212527, \; 16, \; 72)$|
    |$\vdots$|$\vdots$|$\vdots$|
    |**$444$**|**$(339768, \; 22811, \; 35067)$**|**$(339768, \; 37251, \; 5360)$**|
    
    Il più piccolo intero positivo $i$ per cui $x_i = x_{2i}$ è quindi:
    
      
    
    $$\mathbf{i = 444} \qquad (\text{con } x_{444} = x_{888} = \mathbf{339768})$$
    
2. **Risoluzione della congruenza lineare modulo $n = 57251$:** Sostituendo i valori $(a_{444}, b_{444}) = (22811, 35067)$ e $(a_{888}, b_{888}) = (37251, 5360)$ nell'equazione $c(b_{2i} - b_i) \equiv a_i - a_{2i} \pmod n$:
    
      
    - Differenza dei coefficienti $b$:
        
          
        
        $$b_{888} - b_{444} \bmod 57251 = (5360 - 35067) \bmod 57251 = -29707 \bmod 57251 = \mathbf{27544}$$
        
    - Differenza dei coefficienti $a$:
        
          
        
        $$a_{444} - a_{888} \bmod 57251 = (22811 - 37251) \bmod 57251 = -14440 \bmod 57251 = \mathbf{42811}$$
        
    - Calcolo dell'inverso moltiplicativo $27544^{-1} \bmod 57251$ tramite l'`EXTENDED EUCLIDEAN ALGORITHM` (**Algorithm 6.2**):
        
          
        
        $$\begin{aligned} 57251 &= 2 \times 27544 + 2163 \\ 27544 &= 12 \times 2163 + 1588 \\ 2163 &= 1 \times 1588 + 575 \\ 1588 &= 2 \times 575 + 438 \\ 575 &= 1 \times 438 + 137 \\ 438 &= 3 \times 137 + 27 \\ 137 &= 5 \times 27 + 2 \\ 27 &= 13 \times 2 + 1 \end{aligned}$$
        
        Poiché $\gcd(27544, 57251) = 1$, risalendo i coefficienti $t_j$ si ottiene:
        
          
        
        $$27544^{-1} \bmod 57251 = \mathbf{27580} \qquad (\text{infatti } 27544 \times 27580 = 759663520 = 13269 \times 57251 + 1)$$
        
    - Calcolo di $c = \log_2 56851$:
        
          
        
        $$c = (42811 \times 27580) \bmod 57251 = 1180727380 \bmod 57251 = \mathbf{40007}$$
        

> [!example] Risultato Finale Esercizio 7.3
> 
>   
> 
> - Primo indice di collisione: $\mathbf{i = 444}$ ($x_{444} = x_{888} = 339768$)
>     
>       
>     
> - Logaritmo discreto:
>     
>       
>     
>     $$\log_2 56851 = \mathbf{40007} \quad \text{in } \mathbb{Z}_{458009}^*$$
>     
>     _(Verifica: $2^{40007} \bmod 458009 = 56851$)._
>     
>       
>     

## Esercizio 7.6

> [!abstract] Testo dell'Esercizio 7.6
> 
> Sia $p = 227$. L'elemento $\alpha = 2$ è primitivo in $\mathbb{Z}_p^*$.
> 
>   
> 
> - **(a)** Calcolare $\alpha^{32}, \alpha^{40}, \alpha^{59}$ e $\alpha^{156}$ modulo $p$, e fattorizzarli sulla _factor base_ $\mathcal{B} = \{2, 3, 5, 7, 11\}$.
>     
>       
>     
> - **(b)** Utilizzando il fatto che $\log_2 2 = 1$, calcolare $\log_2 3, \log_2 5, \log_2 7$ e $\log_2 11$ dalle fattorizzazioni ottenute al punto precedente (tutti i logaritmi sono logaritmi discreti in $\mathbb{Z}_p^*$ in base $\alpha = 2$).
>     
>       
>     
> - **(c)** Supponiamo ora di voler calcolare $\log_2 173$. Moltiplicare $173$ per il valore "casuale" $2^{177} \bmod p$. Fattorizzare il risultato sulla _factor base_, e procedere a calcolare $\log_2 173$ utilizzando i logaritmi dei numeri nella _factor base_ calcolati in precedenza.
>     
>       
>     

### Soluzione del Punto (a) – Esponenziazioni Modulari e Fattorizzazione su $\mathcal{B}$

Lavoriamo nel gruppo moltiplicativo $\mathbb{Z}_{227}^*$ (con $p = 227$ primo). Poiché $\alpha = 2$ è un **primitive element** modulo $227$, il suo ordine è $n = \vert{}\mathbb{Z}_{227}^*\vert{} = p - 1 = 226$. La _factor base_ fissata è:

  

$$\mathcal{B} = \{2, 3, 5, 7, 11\}$$

Calcoliamo preliminarmente le potenze successive di $2$ per raddoppiamento (_squaring_) modulo $227$:

  

$$\begin{aligned} 2^8 \bmod 227 &= 256 \bmod 227 = 29 \\ 2^{16} \bmod 227 &= 29^2 \bmod 227 = 841 \bmod 227 = 160 \\ 2^{32} \bmod 227 &= 160^2 \bmod 227 = 25600 \bmod 227 = 176 \equiv -51 \pmod{227} \\ 2^{64} \bmod 227 &= (-51)^2 \bmod 227 = 2601 \bmod 227 = 104 \\ 2^{128} \bmod 227 &= 104^2 \bmod 227 = 10816 \bmod 227 = 147 \end{aligned}$$

Calcoliamo ora le quattro potenze richieste e fattorizziamo ciascun resto intero sui primi di $\mathcal{B}$:

  

1. **Per $x_1 = 32$:**
    
      
    
    $$2^{32} \bmod 227 = \mathbf{176} = 16 \times 11 = \mathbf{2^4 \times 11^1}$$
    
2. **Per $x_2 = 40$ ($40 = 32 + 8$):**
    
      
    
    $$2^{40} \bmod 227 = (2^{32} \times 2^8) \bmod 227 = (176 \times 29) \bmod 227 = 5104 \bmod 227 = \mathbf{110} = \mathbf{2^1 \times 5^1 \times 11^1}$$
    
3. **Per $x_3 = 59$ ($59 = 40 + 16 + 3$):**
    
      
    
    $$2^{59} \bmod 227 = (2^{40} \times 2^{16} \times 2^3) \bmod 227 = (110 \times 160 \times 8) \bmod 227 = (121 \times 8) \bmod 227 = 968 \bmod 227 = \mathbf{60} = \mathbf{2^2 \times 3^1 \times 5^1}$$
    
4. **Per $x_4 = 156$ ($156 = 128 + 16 + 8 + 4$):**
    
      
    
    $$2^{156} \bmod 227 = (2^{128} \times 2^{16} \times 2^8 \times 2^4) \bmod 227 = (147 \times 160 \times 29 \times 16) \bmod 227 = \mathbf{28} = \mathbf{2^2 \times 7^1}$$
    

### Soluzione del Punto (b) – Calcolo dei Logaritmi della Factor Base ($\bmod 226$)

Come illustrato nella Sezione 7.2.4, ciascuna congruenza moltiplicativa della forma $\alpha^{x_j} \equiv \prod_{i=1}^B p_i^{a_{ij}} \pmod p$ si traduce, applicando il logaritmo in base $\alpha = 2$ a entrambi i membri, nella congruenza lineare equivalente modulo $p - 1 = 226$:

  

$$x_j \equiv \sum_{i=1}^B a_{ij} \log_2 p_i \pmod{226}$$

Dalle quattro fattorizzazioni del **Punto (a)** otteniamo il seguente sistema di congruenze lineari modulo $226$:

  

$$\begin{cases} 4 \log_2 2 + \log_2 11 \equiv 32 \pmod{226} & (1) \\ \log_2 2 + \log_2 5 + \log_2 11 \equiv 40 \pmod{226} & (2) \\ 2 \log_2 2 + \log_2 3 + \log_2 5 \equiv 59 \pmod{226} & (3) \\ 2 \log_2 2 + \log_2 7 \equiv 156 \pmod{226} & (4) \end{cases}$$

Poiché sappiamo che $\mathbf{\log_2 2 = 1}$, il sistema è già in forma triangolare e possiamo ricavare direttamente tutte le incognite per sostituzione successiva modulo $226$:

  

1. **Calcolo di $\log_2 11$ dalla congruenza $(1)$:**
    
      
    
    $$\log_2 11 \equiv (32 - 4 \log_2 2) \bmod 226 = (32 - 4 \times 1) \bmod 226 = \mathbf{28}$$
    
2. **Calcolo di $\log_2 5$ dalla congruenza $(2)$ (sostituendo $\log_2 2 = 1$ e $\log_2 11 = 28$):**
    
      
    
    $$\log_2 5 \equiv (40 - \log_2 2 - \log_2 11) \bmod 226 = (40 - 1 - 28) \bmod 226 = \mathbf{11}$$
    
3. **Calcolo di $\log_2 3$ dalla congruenza $(3)$ (sostituendo $\log_2 2 = 1$ e $\log_2 5 = 11$):**
    
      
    
    $$\log_2 3 \equiv (59 - 2 \log_2 2 - \log_2 5) \bmod 226 = (59 - 2 \times 1 - 11) \bmod 226 = \mathbf{46}$$
    
4. **Calcolo di $\log_2 7$ dalla congruenza $(4)$ (sostituendo $\log_2 2 = 1$):**
    
      
    
    $$\log_2 7 \equiv (156 - 2 \log_2 2) \bmod 226 = (156 - 2 \times 1) \bmod 226 = \mathbf{154}$$
    

> [!example] Logaritmi Discreti della Factor Base $\mathcal{B}$ in $\mathbb{Z}_{227}^*$
> 
>   
> 
> $$\log_2 2 = \mathbf{1}, \qquad \log_2 3 = \mathbf{46}, \qquad \log_2 5 = \mathbf{11}, \qquad \log_2 7 = \mathbf{154}, \qquad \log_2 11 = \mathbf{28}$$

### Soluzione del Punto (c) – Calcolo Individuale di $\log_2 173$

Vogliamo determinare $\log_2 \beta$ per $\beta = 173$ applicando il secondo passo dell'`INDEX CALCULUS ALGORITHM` con l'esponente casuale fornito $s = 177$:

  

1. **Calcolo di $\gamma = \beta \alpha^s \bmod p$:** Osservando che $177 = 156 + 16 + 4 + 1$, calcoliamo prima $2^{177} \bmod 227$:
    
      
    
    $$2^{177} \bmod 227 = (2^{156} \times 2^{16} \times 2^4 \times 2^1) \bmod 227 = (28 \times 160 \times 16 \times 2) \bmod 227 = 143360 \bmod 227 = 96$$
    
    Moltiplichiamo ora per $\beta = 173$ modulo $227$:
    
      
    
    $$\gamma = 173 \times 2^{177} \bmod 227 = (173 \times 96) \bmod 227 = 16608 \bmod 227 = \mathbf{168}$$
    
2. **Fattorizzazione di $\gamma = 168$ sulla _factor base_ $\mathcal{B} = \{2, 3, 5, 7, 11\}$:**
    
      
    
    $$168 = 8 \times 21 = \mathbf{2^3 \times 3^1 \times 7^1}$$
    
    Poiché $168$ si fattorizza completamente su $\mathcal{B}$, otteniamo la congruenza moltiplicativa:
    
      
    
    $$173 \times 2^{177} \equiv 2^3 \times 3^1 \times 7^1 \pmod{227}$$
    
3. **Passaggio agli esponenti modulo $p - 1 = 226$ e risoluzione per $\log_2 173$:** Prendendo il logaritmo discreto in base $2$ di entrambi i membri:
    
      
    
    $$\log_2 173 + 177 \equiv 3 \log_2 2 + 1 \log_2 3 + 1 \log_2 7 \pmod{226}$$
    
    Sostituendo i valori noti della _factor base_ ($\log_2 2 = 1$, $\log_2 3 = 46$, $\log_2 7 = 154$) e sottraendo $s = 177$:
    
      
    
    $$\begin{aligned} \log_2 173 &= (3 \log_2 2 + \log_2 3 + \log_2 7 - 177) \bmod 226 \\ &= (3 \times 1 + 46 + 154 - 177) \bmod 226 \\ &= (203 - 177) \bmod 226 \\ &= \mathbf{26} \end{aligned}$$
    

> [!example] Risultato Finale Esercizio 7.6(c)
> 
>   
> 
> $$\log_2 173 = \mathbf{26} \quad \text{in } \mathbb{Z}_{227}^*$$
> 
> _(Verifica: $2^{26} \bmod 227 = (2^{16} \times 2^8 \times 2^2) \bmod 227 = (160 \times 29 \times 4) \bmod 227 = 18560 \bmod 227 = 173$)._
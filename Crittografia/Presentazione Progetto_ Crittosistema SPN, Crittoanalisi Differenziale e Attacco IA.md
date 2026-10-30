

# Presentazione Progetto: Crittosistema SPN, Crittoanalisi Differenziale e Attacco IA

## Indice della Presentazione
**Introduzione: I Cifrari Iterati**
0. **Definizione Formale di Substitution-Permutation Network**
1. **Architettura del Crittosistema SPN**
2. **Fase 1: Implementazione in Python di Cifratura e Decifratura**
3. **Fase 2: Crittoanalisi Differenziale dal Libro**
4. **Fase 3: Attacco tramite Modello IA "Stupido"**

---

## Introduzione: I Cifrari Iterati

La quasi totalità dei cifrari a blocchi moderni è progettata secondo il paradigma del **cifrario iterato** (*iterated cipher*):

1. **Key Schedule e Sottochiavi di Round:**
   A partire da una chiave segreta iniziale $K$, un algoritmo detto **key schedule** genera una sequenza di $N$ sottochiavi (*round keys* o *subkeys*) denotate con $(K^1, K^2, \dots, K^N)$.

2. **Funzione di Round $g$ e Cifratura Iterata:**
   La cifratura trasforma un blocco di *plaintext* $x$ in un blocco di *ciphertext* $y$ attraverso **$N$ iterazioni successive** (chiamate **round**) di una stessa funzione, detta **funzione di round** (*round function*) $$g_K: \mathcal{W} \to \mathcal{W}$$
   Indicato lo stato iniziale con $w^0 = x$, ad ogni round $r$ ($1 \le r \le N$) lo stato corrente $w^{r-1}$ viene combinato con la sottochiave $K^r$ tramite la funzione $g$ per produrre lo stato successivo $w^r$:
   $$\begin{aligned} w^0 &= x \\ w^1 &= g(w^0, K^1) \\ w^2 &= g(w^1, K^2) \\ &\;\;\vdots \\ w^{N-1} &= g(w^{N-2}, K^{N-1}) \\ y = w^N &= g(w^{N-1}, K^N) \end{aligned}$$

3. **Corettezza:**
   La correttezza è data del crittosistema è data dall'**iniettività** di g.
   Equivale quindi a dire che esiste una funzione inversa $g^{-1}$ tale che, per ogni stato $w$ e sottochiave $K^r$:
   $$g^{-1}\big(g(w, K^r), K^r\big) = w$$
   Per decifrare il testo cifrato $y = w^N$ e ricostruire il testo in chiaro $x = w^0$, il destinatario applica iterativamente la funzione inversa $g^{-1}$ utilizzando le stesse sottochiavi di round, ma in **ordine inverso** ($K^N, K^{N-1}, \dots, K^1$):
   $$\begin{aligned} w^{N-1} &= g^{-1}(y, K^N) \\ w^{N-2} &= g^{-1}(w^{N-1}, K^{N-1}) \\ &\;\;\vdots \\ x = w^0 &= g^{-1}(w^1, K^1) \end{aligned}$$
   Se si verificasse la condizione $g(x_1, K^r) = g(x_2, K^r) = y$ partendo da due stati originali diversi ($x_1 \neq x_2$), l'inversione di $y$ restituirebbe contemporaneamente due candidati ugualmente validi ($x_1$ e $x_2$)
4. **Principi di Confusione e Diffusione:**
   Una singola funzione di round $g$, presa da sola, può anche essere crittograficamente debole o semplice da implementare, ma la sua **composizione ripetuta per $N$ round** produce una funzione complessiva complessa, realizzando i due principi cardine enunciati da Claude Shannon:
   * **Confusione:** mediante sostituzioni sul testo cifrato.
   * **Diffusione:** riarrangiare la posizione di ogni bit del testo in chiaro su molti bit del testo cifrato mediante permutazioni.

---

## 0. Definizione Formale di Substitution-Permutation Network (SPN)

Una **Substitution-Permutation Network (SPN)** è un particolare tipo di cifrario iterato costruito a partire da operazioni 2 operazioni principali: sostituzione (confusione) e permutazione (diffusione).

### 0.1 Componenti Matematiche e Notazione dei Blocchi
Siano $\ell, m \in \mathbb{P}$ due interi positivi. Sia il testo in chiaro (*plaintext*) che il testo cifrato (*ciphertext*) sono vettori binari di lunghezza $\ell m$ (ovvero $\ell m$ rappresenta la dimensione del blocco del cifrario).
Una rete SPN è costruita a partire da due componenti fondamentali, denotate con $\pi_S$ e $\pi_P$ entrambe biietive:
1. **La S-box ($\pi_S$):**
   $$\pi_S : \{0, 1\}^\ell \to \{0, 1\}^\ell$$
   è una permutazione delle $2^\ell$ stringhe binarie di lunghezza $\ell$ (la lettera *"S"* indica *"Substitution"*). Essa sostituisce un blocco di $\ell$ bit con un diverso blocco di $\ell$ bit.
2. **La Permutazione ($\pi_P$):**
   $$\pi_P : \{1, \dots, \ell m\} \to \{1, \dots, \ell m\}$$
   è una permutazione degli indici interi $\{1, \dots, \ell m\}$ (la lettera *"P"* indica *"Permutation"*). Essa rimescola i $\ell m$ bit dell'intero stato cambiandone l'ordine posizionale.

Data una stringa binaria di $\ell m$ bit $x = (x_1, \dots, x_{\ell m}) \in \{0, 1\}^{\ell m}$, possiamo considerare $x$ come la concatenazione di $m$ sottostringhe di lunghezza $\ell$ bit ciascuna, denotate con $x^{\langle 1 \rangle}, \dots, x^{\langle m \rangle}$:
$$x = x^{\langle 1 \rangle} \parallel \dots \parallel x^{\langle m \rangle}$$

---

### 0.2 Definizione Formale

> Siano $\ell, m, N$ interi positivi, sia $\pi_S : \{0, 1\}^\ell \to \{0, 1\}^\ell$ una permutazione e sia $\pi_P : \{1, \dots, \ell m\} \to \{1, \dots, \ell m\}$ una permutazione.
> * **Spazio dei Plaintext e dei Ciphertext:** $\mathcal{P} = \mathcal{C} = \{0, 1\}^{\ell m}$.
> * **Spazio delle Sottochiavi (*Key Schedule*):** $\mathcal{K} \subseteq \left(\{0, 1\}^{\ell m}\right)^{N+1}$ consiste di tutte le possibili sequenze di $N+1$ sottochiavi di round $(K^1, \dots, K^{N+1})$ derivabili da una chiave iniziale maestra $K$ tramite l'algoritmo di *key scheduling*.
> * **Funzione di Cifratura:** Per una data *key schedule* $(K^1, \dots, K^{N+1})$, il testo in chiaro $x \in \mathcal{P}$ viene cifrato in $N$ round mediante l'**Algorithm 4.1**.

---

### 0.3 Dinamica dei Round, Variabili Intermedie e *Whitening*
Il cifrario SPN opera su **$N$ round** successivi:
* **Round $1 \le r \le N-1$:** In ciascun round standard si eseguono tre passaggi in sequenza:
  1. **Round Key Mixing:** Lo stato corrente $w^{r-1}$ (con $w^0 = x$) viene combinato tramite XOR bit a bit con la sottochiave di round $K^r$, producendo l'ingresso alle S-box:
     $$u^r = w^{r-1} \oplus K^r$$
  2. **Sostituzione ($m$ S-box in parallelo):** Su ciascuno degli $m$ sottoblocchi di $\ell$ bit di $u^r$ viene applicata la S-box $\pi_S$, ottenendo l'uscita delle S-box $v^r$:
     $$v^{r\langle i \rangle} = \pi_S\left(u^{r\langle i \rangle}\right) \quad \text{per } 1 \le i \le m$$
  3. **Permutazione:** All'uscita $v^r = (v^r_1, \dots, v^r_{\ell m})$ viene applicata la permutazione $\pi_P$ per produrre $w^r = (w^r_1, \dots, w^r_{\ell m})$, dove $w^r_{\pi_P(i)} = v^r_i$.
* **Ultimo Round ($r = N$) e Invertibilità:** Nell'ultimo round si calcolano $u^N = w^{N-1} \oplus K^N$ e $v^N = \pi_S(u^N)$, ma **la permutazione $\pi_P$ non viene applicata**. Questo perchè inserendo una nuova permutazione non avrebbe senso in quanto si è nell'ultimo round, e inoltre si ha una simmetria per la **decifratura**, semplicemente invertendo l'ordine (e applicando $\pi_P^{-1}$ alle chiavi intermedie) della *key schedule* e sostituendo le S-box $\pi_S$ con le loro inverse $\pi_S^{-1}$.
* **Whitening:** La primissima operazione ($x \oplus K^1$) e l'ultimissima operazione ($y = v^N \oplus K^{N+1}$) dell'SPN consistono in uno XOR diretto con una sottochiave. Questa tecnica prende il nome di **whitening** e serve a impedire a un attaccante privo della chiave di calcolare anche solo il primo livello di S-box in ingresso o l'ultimo livello di S-box a ritroso dal testo cifrato.

### 0.4 Processo di Decifratura (Operazione Inversa dell'SPN)

Per decifrare un blocco di testo cifrato $y \in \{0, 1\}^{\ell m}$ e ricostruire univocamente il testo in chiaro originale $x = w^0$, il destinatario deve invertire ciascuna delle trasformazioni applicate in fase di cifratura, procedendo **a ritroso dall'ultimo round $r = N$ fino al primo round $r = 1$** e utilizzando le sottochiavi della *key schedule* in **ordine inverso** ($K^{N+1}, K^N, \dots, K^1$).


---

#### Sequenza Passo-Passo dell'Algoritmo di Decifratura

Dato il testo cifrato $y \in \{0, 1\}^{\ell m}$ e la sequenza di sottochiavi $(K^1, \dots, K^{N+1})$, la decifratura procede attraverso le seguenti fasi:

* **Inversione dell'Ultimo Round ($r = N$):**
Poiché in fase di cifratura nell'ultimo round non è stata applicata la permutazione $\pi_P$ ma il *whitening* finale, le prime tre operazioni inverse sono:


1. **Rimozione del Whitening finale ($K^{N+1}$):** Si combina il testo cifrato $y$ in XOR con l'ultima sottochiave $K^{N+1}$ per riottenere l'uscita delle S-box dell'ultimo round:



$$v^N = y \oplus K^{N+1}$$


2. **Sostituzione Inversa ($m$ S-box inverse $\pi_S^{-1}$ in parallelo):** Su ciascuno degli $m$ sottoblocchi di $\ell$ bit di $v^N$ si applica la S-box inversa $\pi_S^{-1}$, risalendo all'ingresso delle S-box dell'ultimo round:



$$u^{N\langle i \rangle} = \pi_S^{-1}\left(v^{N\langle i \rangle}\right) \quad \text{per } 1 \le i \le m$$


3. **Rimozione della Sottochiave $K^N$:** Si effettua lo XOR tra $u^N$ e la sottochiave $K^N$, ottenendo lo stato d'uscita del penultimo round $w^{N-1}$:



$$w^{N-1} = u^N \oplus K^N$$




* **Inversione dei Round Standard ($r = N-1, N-2, \dots, 1$):**
Per ciascun round $r$ che scende da $N-1$ fino a $1$, partendo dallo stato $w^r$ appena ricostruito, si invertono nell'ordine la permutazione, le S-box e il *key mixing*:


1. **Permutazione Inversa ($\pi_P^{-1}$):** Si riordinano i bit dello stato $w^r = (w^r_1, \dots, w^r_{\ell m})$ applicando $\pi_P^{-1}$, riottenendo l'uscita delle S-box del round $r$:



$$v^r_i = w^r_{\pi_P(i)} \quad \text{per } 1 \le i \le \ell m \qquad \Big(\text{ovvero } v^r = \pi_P^{-1}(w^r)\Big)$$


2. **Sostituzione Inversa ($\pi_S^{-1}$):** Si applica $\pi_S^{-1}$ a ciascuno degli $m$ sottoblocchi da $\ell$ bit di $v^r$, risalendo a $u^r$:



$$u^{r\langle i \rangle} = \pi_S^{-1}\left(v^{r\langle i \rangle}\right) \quad \text{per } 1 \le i \le m$$


3. **Rimozione della Sottochiave di Round ($K^r$):** Si esegue lo XOR con la sottochiave $K^r$ per ottenere lo stato del round precedente $w^{r-1}$:



$$w^{r-1} = u^r \oplus K^r$$




* **Output Finale ($r = 1$):**
Al termine dell'iterazione $r = 1$, dopo aver rimosso il *whitening* iniziale tramite l'ultimo XOR $w^0 = u^1 \oplus K^1$, lo stato finale $w^0$ coincide esattamente con il blocco di testo in chiaro originario:



$$x = w^0$$

---

## 1. Architettura del Crittosistema SPN (Parametri Specifici)

Il crittosistema analizzato nel nostro progetto istanzia il *Cryptosystem 4.1* su $N = 4$ round, con blocchi di lunghezza $\ell \cdot m = 16$ bit ($\ell = 4$ bit per S-box, $m = 4$ S-box affiancate per round).

### 1.1 Sostituzione $\pi_{S'}$ (specifica dell'Esercizio 4.16)
Adottiamo la sostituzione $\pi_{S'} : \{0,1\}^4 \to \{0,1\}^4$ definita nell'Esercizio 4.16, insieme alla sua inversa $(\pi_{S'})^{-1}$ necessaria per la decifratura e per l'attacco:

| $z$ (Input Hex) | `0` | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `A` | `B` | `C` | `D` | `E` | `F` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$\pi_{S'}(z)$ (Output)** | `E` | `2` | `1` | `3` | `D` | `9` | `0` | `6` | `F` | `4` | `5` | `A` | `8` | `C` | `7` | `B` |
| **$(\pi_{S'})^{-1}(z)$ (Inversa)** | `6` | `2` | `1` | `3` | `9` | `A` | `7` | `E` | `C` | `5` | `B` | `F` | `D` | `4` | `0` | `8` |

### 1.2 Permutazione $\pi_P$ (specifica dell'Esempio 4.1)
La permutazione dei $16$ bit $\pi_P : \{1, \dots, 16\} \to \{1, \dots, 16\}$ sposta il bit $j$-esimo della S-box $i$-esima nella posizione $i$-esima della S-box $j$-esima:

| $i$ | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| **$\pi_P(i)$** | `1` | `5` | `9` | `13` | `2` | `6` | `10` | `14` | `3` | `7` | `11` | `15` | `4` | `8` | `12` | `16` |

*(Nota: Poiché $\pi_P$ è simmetrica, coincide con la propria inversa: $\pi_P^{-1} = \pi_P$)*.

### 1.3 Key Schedule (Esempio 4.1)
Dalla chiave principale random $K$ a $32$ bit si estraggono $N+1 = 5$ sottochiavi di round $K^1, \dots, K^5$ da $16$ bit ciascuna, traslando una finestra di $16$ bit di $4$ posizioni alla volta ($K^r$ consiste dei bit da $4r-3$ a $4r+12$ di $K$).

---

## 2. Fase 1: Implementazione in Python (Cifratura e Decifratura)

Il codice seguente traduce fedelmente lo pseudocodice dell'**Algorithm 4.1** dello Stinson:
* Nei round $r = 1, \dots, N-1$ si eseguono: *Round Key Mixing* ($u^r = w^{r-1} \oplus K^r$), *S-box* ($v^r = \pi_{S'}(u^r)$) e *Permutazione* ($w^r = \pi_P(v^r)$).
* Nell'ultimo round ($r = N = 4$) la permutazione $\pi_P$ **viene omessa** e si applica il *whitening* finale ($y = v^4 \oplus K^5$).
* La **decifratura** inverte l'ordine delle operazioni e delle sottochiavi, usando $(\pi_{S'})^{-1}$ e $\pi_P^{-1}$.

```python
import random

# S-box
PI_S = [0xE, 0x2, 0x1, 0x3, 0xD, 0x9, 0x0, 0x6, 
        0xF, 0x4, 0x5, 0xA, 0x8, 0xC, 0x7, 0xB]

# Calcoliamo automaticamente la S-box inversa
PI_S_INV = [0] * 16
for indice, valore in enumerate(PI_S):
    PI_S_INV[valore] = indice

# P-box (Permutation-box): indica dove deve finire ciascun bit.
PI_P = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]


def get_round_keys(master_key_32bit):
    """
    Prende la chiave principale da 32 bit e ritaglia 5 sottochiavi da 16 bit.
    Ogni sottochiave si ottiene spostando una 'finestra' di 4 bit verso destra.
    """
    round_keys = []
    for r in range(1, 6): # r va da 1 a 5
        shift = 32 - (16 + 4 * (r - 1)) # calcola la finestra di lettura
        k_r = (master_key_32bit >> shift) & 0xFFFF # esegue shifting verso dx ed isola i bit 
        round_keys.append(k_r)
    return round_keys


def apply_sbox_layer(state_16bit, sbox):
    """
    Prende i 16 bit di stato, li divide in 4 blocchetti da 4 bit ciascuno,
    e passa ciascun blocchetto dentro la S-box.
    """
    output = 0
    for i in range(4):
        shift = (3 - i) * 4 # finestra per leggere il blocco giusto
        nibble = (state_16bit >> shift) & 0xF # shifta e poi isola i 4 bit
        output |= (sbox[nibble] << shift) # usa come indice nibble per cercare l'output giusto e poi shifta per farli concatenare con l'output
    return output # restituisce tutti e 4 i blocchi dopo l'S-box


def apply_permutation(state_16bit, perm):
    """
    Legge i 16 bit uno ad uno e li sposta nella nuova posizione 
    indicata dalla lista 'perm'.
    """
    output = 0
    for i in range(16):
        bit = (state_16bit >> (15 - i)) & 1 # isola il bit in pos i 
        dest_pos = perm[i] # nuova pos dove mettere il bit i
        output |= (bit << (15 - dest_pos)) # bit i messo nella pos giusta
    return output # restituisce tutti e 4 i blocchi dopo la permutazione


def spn_encrypt(x, round_keys, N=4):
    """
    Cifratura: prende il testo in chiaro 'x' e lo trasforma in testo cifrato.
    """
    w = x  # Stato iniziale
    
    # Primi N-1 round (in questo caso i round 1, 2 e 3)
    for r in range(1, N):
        u = w ^ round_keys[r - 1]
        v = apply_sbox_layer(u, PI_S)
        w = apply_permutation(v, PI_P)
    
    # Ultimo round (round 4): identico ai precedenti ma SENZA la permutazione
    u_N = w ^ round_keys[N - 1]
    v_N = apply_sbox_layer(u_N, PI_S)
    
    # Whitening finale: un ultimo XOR con la chiave finale
    y = v_N ^ round_keys[N]
    
    return y


def spn_decrypt(y, round_keys, N=4):
    """
    Decifratura: fa esattamente i passi della cifratura ma al contrario,
    usando la S-box inversa.
    """
    # Rimuove l'ultimo step di Whitening
    v_N = y ^ round_keys[N]
    
    # Inverte la S-box dell'ultimo round
    u_N = apply_sbox_layer(v_N, PI_S_INV)
    
    # Rimuove la chiave del round 4
    w = u_N ^ round_keys[N - 1]
    
    # Esegue i round precedenti al contrario (dal 3 fino all'1)
    for r in range(N - 1, 0, -1):
        v = apply_permutation(w, PI_P)
        u = apply_sbox_layer(v, PI_S_INV)
        w = u ^ round_keys[r - 1]
    
    return w


# ==============================================================================
# TEST DEL CODICE CON VALORI CASUALI
# ==============================================================================
print("=== TEST SPN CON VALORI RANDOMICI ===")

# Genera una chiave maestra casuale da 32 bit 
K_master = random.randint(0, 0xFFFFFFFF)

# Genera un messaggio in chiaro casuale da 16 bit
x_plain = random.randint(0, 0xFFFF)

# Calcola le 5 sottochiavi
keys = get_round_keys(K_master)

# Cifra e poi decifra il messaggio
y_cipher = spn_encrypt(x_plain, keys)
x_dec    = spn_decrypt(y_cipher, keys)

# Prepara le stringhe in binario e in esadecimale
k_bin = format(K_master, '032b')
k_hex = format(K_master, '08X')

x_plain_bin = format(x_plain, '016b')
x_plain_hex = format(x_plain, '04X')

y_cipher_bin = format(y_cipher, '016b')
y_cipher_hex = format(y_cipher, '04X')

x_dec_bin = format(x_dec, '016b')
x_dec_hex = format(x_dec, '04X')

# Stampa i risultati unendo i pezzi
print("Chiave Master generata : " + k_bin + " (Hex: " + k_hex + ")")
print("Plaintext originale    : " + x_plain_bin + " (Hex: " + x_plain_hex + ")")
print("Ciphertext (cifrato)   : " + y_cipher_bin + " (Hex: " + y_cipher_hex + ")")
print("Plaintext decifrato    : " + x_dec_bin + " (Hex: " + x_dec_hex + ")")

# Controllo di sicurezza con un classico if
if x_plain == x_dec:
    print("\nVerifica superata: La decifratura ha ripristinato il messaggio originale senza errori!")
else:
    print("\nErrore: la decifratura non coincide!")


```

---

## 3. Fase 2: Crittoanalisi Differenziale (Risoluzione Esercizio 4.16)

La crittoanalisi differenziale è un *chosen-plaintext attack* (attacco a testo in chiaro scelto) che analizza come specifiche differenze nei dati in ingresso si propaghino attraverso i round di un cifrario. 

L'obiettivo dell'Esercizio 4.16 è sfruttare questa propagazione per recuperare parte dell'ultima sottochiave. L'attaccante raccoglie e analizza un gran numero di tuple $(x, x^*, y, y^*)$, in cui $(x, x^*)$ sono coppie di testi in chiaro appositamente scelte affinché la loro differenza XOR assuma un valore fisso e noto (in questo caso specifico $x' = x \oplus x^* = \texttt{0x9009}$) e $(y, y^*)$ sono i rispettivi testi cifrati.

### 3.1 Costruzione della Difference Distribution Table ($N_D$) per l'Esercizio 4.16

Per studiare le transizioni differenziali, si costruisce la *Difference Distribution Table* (DDT) della S-box.

**Insieme $\Delta(x')$:** Dato un input differenziale $x' \in \{0,1\}^4$, l'insieme delle coppie ordinate che generano tale differenza è:
$$\Delta(x') = \{(x, x \oplus x') : x \in \{0,1\}^4\}$$
Tale insieme ha sempre cardinalità $|\Delta(x')| = 16$.

**Funzione $N_D(x', y')$:** Per la S-box $\pi_{S'}$, la DDT conta quante coppie in $\Delta(x')$ producono una specifica differenza di uscita $y'$:
$$N_D(x', y') = \left| \left\{ (x, x^*) \in \Delta(x') : \pi_{S'}(x) \oplus \pi_{S'}(x^*) = y' \right\} \right|$$

**Proprietà applicative della DDT:**
*   **S-box passiva:** Se $x' = 0$, l'ingresso non cambia, quindi l'uscita non cambia. Vale $N_D(0,0) = 16$ e $N_D(0, y') = 0$ per ogni $y' \neq 0$. Una S-box che riceve differenza zero si dice passiva e propaga differenza zero con probabilità $1$.
*   **Parità:** Tutti i valori $N_D(x', y')$ sono pari, poiché se la coppia $(x, x^*)$ produce $y'$, lo fa anche la coppia simmetrica $(x^*, x)$.
*   **Somma costante:** La somma dei valori su ogni riga è pari a $16$.
*   **Invarianza di sottochiave:** Il calcolo prescinde dalle sottochiavi di round $K^r$, in quanto l'operazione di XOR con la chiave si annulla calcolando la differenza: $(x \oplus K^r) \oplus (x^* \oplus K^r) = x \oplus x^* = x'$.

**Tabella $N_D$ per la S-box dell'Esercizio 4.16:**

| $x' \setminus y'$ | `0` | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `A` | `B` | `C` | `D` | `E` | `F` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`0`** | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **`1`** | 0 | 0 | 2 | 0 | **4** | 0 | 2 | 0 | 0 | 0 | 0 | 2 | **4** | 0 | 0 | 2 |
| **`2`** | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 2 | 2 | 6 |
| **`3`** | 0 | 2 | 0 | 4 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 4 | 0 | 2 | 0 | 0 |
| **`4`** | 0 | 4 | 2 | 2 | 0 | 2 | 0 | 2 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 |
| **`5`** | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 2 | 2 | 2 | 2 |
| **`6`** | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 2 | 0 | 2 | 0 | 2 | 2 | 2 | 2 |
| **`7`** | 0 | 0 | 4 | 2 | 2 | 0 | 0 | 0 | 4 | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| **`8`** | 0 | 2 | 0 | 0 | 2 | 4 | 2 | 2 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| **`9`** | 0 | **6** | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 4 | 0 | 2 | 0 | 0 |
| **`A`** | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 4 | 0 | 4 | 2 | 0 | 0 | 2 | 0 |
| **`B`** | 0 | 0 | 0 | 0 | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 4 | 0 | 4 | 0 |
| **`C`** | 0 | 0 | 2 | 0 | 0 | 2 | 4 | 0 | 2 | 0 | 0 | 0 | 2 | 2 | 2 | 0 |
| **`D`** | 0 | 0 | 2 | 2 | 2 | 0 | 2 | 0 | 0 | 2 | 6 | 0 | 0 | 0 | 0 | 0 |
| **`E`** | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 2 | 6 | 0 | 0 | 0 | 0 | 0 | 4 |
| **`F`** | 0 | 0 | 0 | 0 | 2 | 4 | 0 | 2 | 0 | 2 | 0 | 2 | 2 | 2 | 0 | 0 |

### 3.2 La Traccia Differenziale

L'obiettivo è individuare un percorso differenziale attraverso la rete SPN calcolando il rapporto di propagazione ($R_p$) per la traccia innescata dall'input $x' = \texttt{0x9009}$. Costruiamo la traccia sui primi 3 round che attiva in totale 4 S-box ($S_1^1$ e $S_4^1$ nel Round 1, $S_4^2$ nel Round 2, e $S_4^3$ nel Round 3):

*   **Round 1 (2 S-box attive: $S_1^1$ e $S_4^1$):**
    *   Input al Round 1: $\Delta u^1 = \texttt{0x9009} = \texttt{1001 0000 0000 1001}_2$. Le S-box attive sono $S_1^1$ e $S_4^1$, entrambe con input $\Delta u^1_{(1)} = \Delta u^1_{(4)} = \texttt{1001}_2 = 9_{16}$.
    *   Sfruttiamo la transizione $9 \to 1$ ($N_D = 6$). La probabilità per ciascuna S-box è $R_p = 6/16 = 3/8$.
    *   L'uscita dello strato di sostituzione è $\Delta v^1 = \texttt{0x1001} = \texttt{0001 0000 0000 0001}_2$.
    *   Dopo la permutazione della P-box ($\pi_P$), i bit in posizione 4 e 16 vengono mappati rispettivamente in posizione 13 e 16. La differenza diventa $\Delta w^1 = \Delta u^2 = \texttt{0x0009} = \texttt{0000 0000 0000 1001}_2$.
        $$p_1 = \frac{3}{8} \cdot \frac{3}{8} = \frac{9}{64}$$
*   **Round 2 (1 S-box attiva: $S_4^2$):**
    *   L'ingresso $\Delta u^2 = \texttt{0x0009}$ attiva unicamente $S_4^2$ con input $\Delta u^2_{(4)} = \texttt{1001}_2 = 9_{16}$.
    *   Sfruttiamo ancora la transizione $9 \to 1$ (probabilità $R_p = 3/8$).
    *   L'uscita è $\Delta v^2 = \texttt{0x0001} = \texttt{0000 0000 0000 0001}_2$.
    *   La P-box mappa il bit in posizione 16 nuovamente in posizione 16, mantenendo la differenza $\Delta w^2 = \Delta u^3 = \texttt{0x0001}$.
        $$p_2 = \frac{3}{8}$$
*   **Round 3 (1 S-box attiva: $S_4^3$):**
    *   L'ingresso $\Delta u^3 = \texttt{0x0001}$ attiva unicamente $S_4^3$ con input $\Delta u^3_{(4)} = \texttt{0001}_2 = 1_{16}$.
    *   Sfruttiamo la transizione $1 \to \text{C}$ ($N_D = 4$, probabilità $R_p = 4/16 = 1/4$).
    *   L'uscita dell'S-box è $\Delta v^3 = \texttt{0x000C} = \texttt{0000 0000 0000 1100}_2$ (bit attivi in posizione 13 e 14).
    *   Applichiamo la permutazione $\pi_P$: $\pi_P(13) = 4$ e $\pi_P(14) = 8$. Il differenziale in ingresso al Round 4 è pari a $\Delta w^3 = \Delta u^4 = \texttt{0x1100} = \texttt{0001 0001 0000 0000}_2$.
        $$p_3 = \frac{1}{4}$$

Il rapporto di propagazione totale per questa traccia a 3 round è il prodotto delle probabilità delle singole S-box attive:
$$R_p = \frac{9}{64} \times \frac{3}{8} \times \frac{1}{4} = \frac{27}{2048} \approx 0.01318$$

### 3.3 Recupero parziale della sottochiave ($K^5$)

La traccia differenziale ha rivelato che, per una coppia giusta (*right pair*), la differenza in ingresso al quarto round è $\Delta u^4 = \texttt{0x1100}$. Questo indica che le S-box attive nel Round 4 sono esclusivamente $S_1^4$ e $S_2^4$ (i due *nibble* più significativi), mentre $S_3^4$ e $S_4^4$ sono passive. L'attacco sfrutta questa asimmetria per estrarre gli 8 bit corrispondenti della sottochiave $K^5$, testando i candidati $L_1$ e $L_2$.

#### Procedura di Decifratura Parziale e Conteggio

*   Oscar genera $T$ tuple di testi in chiaro $(x, x^*)$ con $x \oplus x^* = \texttt{0x9009}$ e ottiene i rispettivi testi cifrati $(y, y^*)$.
*   Inizializza $2^8 = 256$ contatori $\text{Count}(L_1, L_2) = 0$ per tutte le 256 possibili coppie di sottochiavi candidate a 4 bit $(L_1, L_2) \in \{0, 1\}^4 \times \{0, 1\}^4$ che ipotizzano i valori veri di $(K^5_{(1)}, K^5_{(2)})$.
*   Per ogni coppia $(y, y^*)$ che supera il filtraggio ($\Delta y_{(3)} = \Delta y_{(4)} = \texttt{0000}$) e per ciascuna delle 256 chiavi candidate $(L_1, L_2)$, Oscar decifra parzialmente all'indietro attraverso l'ultimo round calcolando:
    $$v^4_{(1)} = y_{(1)} \oplus L_1, \qquad (v^4_{(1)})^* = y^*_{(1)} \oplus L_1$$
    $$u^4_{(1)} = \pi_{S'}^{-1}(v^4_{(1)}), \qquad (u^4_{(1)})^* = \pi_{S'}^{-1}((v^4_{(1)})^*), \qquad \Delta u^4_{(1)} = u^4_{(1)} \oplus (u^4_{(1)})^*$$
    e analogamente per il 2° blocco usando $L_2$:
    $$v^4_{(2)} = y_{(2)} \oplus L_2, \qquad (v^4_{(2)})^* = y^*_{(2)} \oplus L_2$$
    $$u^4_{(2)} = \pi_{S'}^{-1}(v^4_{(2)}), \qquad (u^4_{(2)})^* = \pi_{S'}^{-1}((v^4_{(2)})^*), \qquad \Delta u^4_{(2)} = u^4_{(2)} \oplus (u^4_{(2)})^*$$
*   **Condizione di incremento del contatore:** Se per la chiave candidata $(L_1, L_2)$ risultano contemporaneamente verificati entrambi i differenziali attesi dalla traccia:
    $$\Delta u^4_{(1)} = \texttt{0001} \quad \text{e} \quad \Delta u^4_{(2)} = \texttt{0001}$$
    allora Oscar incrementa di 1 il contatore: $\text{Count}(L_1, L_2) \leftarrow \text{Count}(L_1, L_2) + 1$. A fine ciclo, la sottochiave con il contatore massimo corrisponde con altissima probabilità ai veri 8 bit di $K^5$.

### 3.4 Codice Python dell'Attacco Differenziale (Algorithm 4.3)

Testiamo le $256$ combinazioni per indovinare gli 8 bit delle due S-box attive nell'ultimo round:

```python
import random

# COSTANTI E IMPOSTAZIONI BASE
SBOX = [0xE, 2, 1, 3, 0xD, 9, 0, 6, 0xF, 4, 5, 0xA, 8, 0xC, 7, 0xB]
SBOX_INV = [SBOX.index(i) for i in range(16)]

PERM = [None, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]
PERM_INV = [0] * 17 
for i in range(1, 17):
    PERM_INV[PERM[i]] = i

NR = 4 

def sub(x, box):
    return sum(box[(x >> (4 * i)) & 0xF] << (4 * i) for i in range(4))

def permute(x, table):
    y = 0
    for i in range(1, 17):
        if (x >> (16 - i)) & 1:
            y |= 1 << (16 - table[i])
    return y

def encrypt(p, keys):
    x = p
    for r in range(NR - 1):
        x = permute(sub(x ^ keys[r], SBOX), PERM)
    x = sub(x ^ keys[NR - 1], SBOX) ^ keys[NR]
    return x

def decrypt(c, keys):
    x = sub(c ^ keys[NR], SBOX_INV) ^ keys[NR - 1]
    for r in range(NR - 2, -1, -1):
        x = sub(permute(x, PERM_INV), SBOX_INV) ^ keys[r]
    return x

def key_from_hex(text):
    t = text.strip().lower()
    if t.startswith("0x"):
        t = t[2:]
    t = t.replace(" ", "").replace("-", "").replace("_", "")
    if len(t) != 20:
        raise ValueError("Servono 20 cifre esadecimali (80 bit). Ne hai inserite: " + str(len(t)))
    try:
        k = int(t, 16)
    except ValueError:
        raise ValueError("La chiave puo contenere solo cifre 0-9 e lettere a-f.")
    return [(k >> (16 * (4 - i))) & 0xFFFF for i in range(5)]

def encrypt_message(msg, keys):
    b = msg.encode()
    if len(b) % 2: 
        b += b"\x00"
    return [encrypt((b[i] << 8) | b[i + 1], keys) for i in range(0, len(b), 2)]

def decrypt_message(blocks, keys):
    out = bytearray()
    for c in blocks:
        p = decrypt(c, keys)
        out += bytes([p >> 8, p & 0xFF])
    return out.rstrip(b"\x00").decode(errors="replace")


# CRITTOANALISI DIFFERENZIALE DINAMICA (CON BINARI E ESADECIMALI)

def punto_a_ddt():
    print("\n--- PUNTO A: CALCOLO DDT ---")
    ddt = [[0] * 16 for _ in range(16)]
    for dx in range(16):
        for x in range(16):
            dy = SBOX[x] ^ SBOX[x ^ dx]
            ddt[dx][dy] += 1
    
    intestazione_colonne = " ".join(format(i, "04b") for i in range(16))
    print("x'\\y'       | " + intestazione_colonne)
    print("-" * 85)
    for dx, riga in enumerate(ddt):
        valori = " ".join(format(v, "4d") for v in riga)
        print("  " + format(dx, "X") + " (" + format(dx, "04b") + ") | " + valori)
    return ddt


def punto_b_traccia(ddt):
    print("\n--- PUNTO B: CALCOLO DELLA TRACCIA DIFFERENZIALE ---")
    x_prime = 0x9009
    print("Input iniziale differenziale x primo: 0x" + format(x_prime, "04X") + " (" + format(x_prime, "016b") + ")")
    
    stato_corrente = x_prime
    prob_totale = 1.0
    numeratore_totale = 1
    denominatore_totale = 1
    
    for round_num in range(1, 4):
        print("\nRound " + str(round_num) + ":")
        stato_dopo_sbox = 0
        
        for sbox_idx in range(4):
            shift = 12 - 4 * sbox_idx
            nibble_in = (stato_corrente >> shift) & 0xF
            
            if nibble_in == 0:
                print("  S-box " + str(sbox_idx + 1) + ": PASSIVA (Input 0x0 (0000), Output 0x0 (0000))")
            else:
                massimo = max(ddt[nibble_in])
                possibili_uscite = [i for i, val in enumerate(ddt[nibble_in]) if val == massimo]
                nibble_out = possibili_uscite[-1]
                casi = ddt[nibble_in][nibble_out]
                
                stato_dopo_sbox |= (nibble_out << shift)
                prob_totale *= (casi / 16.0)
                numeratore_totale *= casi
                denominatore_totale *= 16
                
                print("  S-box " + str(sbox_idx + 1) + ": ATTIVA (Input 0x" + format(nibble_in, "X") + " (" + format(nibble_in, "04b") + ")" + 
                      ", Output 0x" + format(nibble_out, "X") + " (" + format(nibble_out, "04b") + "), casi " + str(casi) + " su 16)")
        
        print("  Stato intermedio prima della permutazione: 0x" + format(stato_dopo_sbox, "04X") + " (" + format(stato_dopo_sbox, "016b") + ")")
        stato_corrente = permute(stato_dopo_sbox, PERM)
        print("  Stato intermedio dopo la permutazione: 0x" + format(stato_corrente, "04X") + " (" + format(stato_corrente, "016b") + ")")
        
    print("\nStato finale (differenza in ingresso all'ultimo round): 0x" + format(stato_corrente, "04X") + " (" + format(stato_corrente, "016b") + ")")
    print("Probabilita totale della traccia (R_p): " + str(numeratore_totale) + " su " + str(denominatore_totale) + " (ovvero " + str(prob_totale) + ")")
    
    return prob_totale


def punto_c_attacco(probabilita_traccia):
    print("\n--- PUNTO C: ATTACCO DIFFERENZIALE ---")
    chiave_str = input("Inserisci una chiave maestra a 80 bit per simulare l'attacco (es. 0x1234567890ABCDEF1234): ")
    try:
        chiavi = key_from_hex(chiave_str)
    except ValueError as e:
        print("Errore: " + str(e))
        return

    C_COSTANTE = 6
    numero_coppie = int(C_COSTANTE * (1.0 / probabilita_traccia))
    
    print("Costante c scelta: " + str(C_COSTANTE))
    print("Calcolo coppie teoriche (T = c * 1/R_p): " + str(C_COSTANTE) + " * (1 / " + str(probabilita_traccia) + ") = " + str(numero_coppie))
    print("Generazione interna di " + str(numero_coppie) + " coppie di testi in chiaro con differenza 0x9009 (1001000000001001)...")
    
    coppie = []
    for i in range(numero_coppie):
        x = random.randrange(0x10000)
        x_star = x ^ 0x9009
        y = encrypt(x, chiavi)
        y_star = encrypt(x_star, chiavi)
        coppie.append((x, x_star, y, y_star))
        
    conteggi = [[0] * 16 for j in range(16)]
    filtrate = 0

    for (x, x_star, y, y_star) in coppie:
        if (y & 0x00FF) != (y_star & 0x00FF):
            continue
        filtrate += 1

        y1 = (y >> 12) & 0xF
        y1_star = (y_star >> 12) & 0xF
        y2 = (y >> 8) & 0xF
        y2_star = (y_star >> 8) & 0xF

        for L1 in range(16):
            u4_1_diff = SBOX_INV[y1 ^ L1] ^ SBOX_INV[y1_star ^ L1]
            if u4_1_diff == 0x1:
                for L2 in range(16):
                    u4_2_diff = SBOX_INV[y2 ^ L2] ^ SBOX_INV[y2_star ^ L2]
                    if u4_2_diff == 0x1:
                        conteggi[L1][L2] += 1

    classifica = sorted(
        ((conteggi[l1][l2], l1, l2) for l1 in range(16) for l2 in range(16)),
        reverse=True
    )
    
    hits, l1, l2 = classifica[0]
    sottochiave_trovata = (l1 << 4) | l2
    print("Coppie totali testate: " + str(numero_coppie) + " (sopravvissute al filtro: " + str(filtrate) + ")")
    print("La sottochiave vincente per i primi 8 bit di K^5 e 0x" + format(sottochiave_trovata, "02X") + 
          " (" + format(sottochiave_trovata, "08b") + ") con " + str(hits) + " hit")
    
    chiave_vera_k5 = chiavi[4]
    veri_8bit = (chiave_vera_k5 >> 8) & 0xFF
    print("Confronto: i veri 8 bit di K^5 inseriti sono 0x" + format(veri_8bit, "02X") + 
          " (" + format(veri_8bit, "08b") + ")")
    
    if sottochiave_trovata == veri_8bit:
        print("Risultato: Attacco Differenziale Riuscito.")
    else:
        print("Risultato: Attacco Fallito.")


# MENU INTERATTIVO PRINCIPALE

def main():
    while True:
        print("\n==================================================")
        print("  CRITTOGRAFIA SPN - MENU PRINCIPALE")
        print("==================================================")
        print("1. Cifra un messaggio")
        print("2. Decifra un messaggio")
        print("3. Esegui Crittoanalisi (Es. 4.16 - Punti a, b, c)")
        print("0. Esci")
        
        scelta = input("Scegli un'opzione: ")
        
        if scelta == "0":
            print("Chiusura del programma.")
            break
            
        elif scelta == "1":
            print("\n--- CIFRATURA ---")
            chiave_str = input("Inserisci la chiave maestra a 80 bit (es. 0x1234567890ABCDEF1234): ")
            try:
                chiavi = key_from_hex(chiave_str)
                messaggio = input("Inserisci il messaggio in chiaro da cifrare: ")
                blocchi_cifrati = encrypt_message(messaggio, chiavi)
                esadecimale = "".join(format(b, "04X") for b in blocchi_cifrati)
                binario = "".join(format(b, "016b") for b in blocchi_cifrati)
                print("Messaggio cifrato in esadecimale: " + esadecimale)
                print("Messaggio cifrato in binario: " + binario)
            except ValueError as e:
                print("Errore: " + str(e))
                
        elif scelta == "2":
            print("\n--- DECIFRATURA ---")
            chiave_str = input("Inserisci la chiave maestra a 80 bit (es. 0x1234567890ABCDEF1234): ")
            try:
                chiavi = key_from_hex(chiave_str)
                cifrato_str = input("Inserisci il testo cifrato in esadecimale: ")
                cifrato_str = cifrato_str.replace(" ", "").replace("\n", "")
                
                if len(cifrato_str) % 4 != 0:
                    print("Errore: La stringa esadecimale deve avere una lunghezza multipla di 4.")
                    continue
                    
                blocchi_cifrati = [int(cifrato_str[i:i+4], 16) for i in range(0, len(cifrato_str), 4)]
                binario = "".join(format(b, "016b") for b in blocchi_cifrati)
                print("Testo cifrato inserito in binario: " + binario)
                
                msg_decifrato = decrypt_message(blocchi_cifrati, chiavi)
                print("Messaggio decifrato: " + msg_decifrato)
            except ValueError as e:
                print("Errore: " + str(e))
                
        elif scelta == "3":
            tabella = punto_a_ddt()
            prob = punto_b_traccia(tabella)
            punto_c_attacco(prob)
            
        else:
            print("Opzione non valida. Riprova.")

main()
```

---

## 4. Fase 3: Attacco Differenziale
cose da aggiungere / modificare : 
- dire che ollama si collega o meno ad internet 
- fornirgli solo il chipertext
- osservare se vale la pena (fissando l ed m=4) mettere nella key schedule come input una chiave da 80 bit (16*5), di modo da non avere una finestra eventuale da shiftare per ottenere le sottochiavi: se K è da 80 bit, basta prelevare 5 blocchi fissi da 16 bit in successione 

- motivare perché prendo $\pi_p$ (in teoria me lo richiede l'esercizio 4.16)

### 1. Definizione dettagliata del Test 
#### A. Cosa stiamo testando esattamente?

L'obiettivo di questa fase non consiste nell'eseguire verifiche empiriche o implementative in prima persona, bensì nel sottoporre a uno stress-test analitico il modello di IA (Ollama), valutandone le capacità di ragionamento crittografico, di code review e di diagnostica. Nello specifico, l'oggetto del test sull'IA comprende:

- **La capacità di diagnosi dei fallimenti:**  
  verificare se il modello sa individuare e spiegare con precisione le cause di un insuccesso crittografico. L'analisi valuta la sua competenza nel riconoscere due scenari critici:
  - **Insufficienza dei campioni:** quando il numero di campioni disponibili è inadeguato, sia perché troppo ridotto sia perché non ottimale rispetto alle esigenze dell'analisi, compromettendo l'affidabilità dei risultati e aumentando il rischio che il modello individui una sottochiave sulla base di risultati casuali.
  - **Incoerenza dei dati:** quando la presenza di dati incongruenti altera i risultati dell'analisi, inducendo il modello a identificare erroneamente una sottochiave come corretta.

- **Il comportamento di fronte a modifiche strutturali:**  
  valutare come l'IA reagisce e si adatta quando il codice viene alterato nei suoi parametri costitutivi, attraverso variazioni del numero di round \(N\), modifiche all'algoritmo di *Key Schedule* o alterazioni della traccia differenziale.

- **L'efficacia come "avversario" o revisore:**  
  testare la capacità del modello di individuare anomalie logiche e difetti implementativi nella decifratura parziale dell'ultimo round e nella gestione delle funzioni inverse, verificando se le sue osservazioni siano coerenti con il funzionamento algebrico e statistico del cifrario SPN.

#### B. Lo strumento di analisi

L'analisi viene condotta utilizzando Ollama in ambiente locale, attraverso l'esecuzione di modelli linguistici avanzati open-weight, come Llama 3. Questa configurazione permette di operare in un ambiente controllato, senza dipendere da API esterne per l'elaborazione delle richieste. In questo modo, è possibile sottoporre il modello a una serie di prove analitiche mantenendo il controllo sull'ambiente di esecuzione.

#### C. La motivazione metodologica (Perché questa scelta)

- **Valutazione del ragionamento logico e della comprensione dei principi crittografici:**  
  i modelli linguistici possono riconoscere strutture di codice e implementazioni standard già presenti nei dati utilizzati durante il loro addestramento. L'introduzione di modifiche mirate al codice permette quindi di verificare se il modello sia in grado di adattare le proprie analisi a configurazioni diverse da quelle standard, applicando correttamente i principi algebrici e statistici alla base dell'attacco.

- **Diagnosi dei fallimenti di natura probabilistica:**  
  poiché l'attacco differenziale si basa sull'analisi statistica delle distribuzioni di probabilità, la sua efficacia dipende anche dalla quantità e dalla coerenza dei campioni utilizzati. La scelta di esaminare scenari di fallimento differenti permette di valutare se il modello sappia interpretare correttamente i limiti dell'analisi statistica e distinguere le diverse cause di un risultato inattendibile.


---------------

### 2. Conoscenze a Disposizione dell'IA
Prima di definire nel dettaglio le informazioni a disposizione dell'attaccante, è necessario chiarire quale materiale viene fornito al modello di IA. Affinché Ollama possa analizzare correttamente il funzionamento dell'attacco e individuare le possibili cause di successo o fallimento, è importante mettergli a disposizione sia il codice che implementa il cifrario SPN, sia quello che realizza la procedura di crittoanalisi.

Fornire esclusivamente il codice del cifrario, contenente la definizione delle S-box e le funzioni di cifratura e decifratura, non sarebbe sufficiente, poiché il modello non disporrebbe della logica necessaria per analizzare il comportamento dell'attacco, i risultati statistici e i contatori utilizzati per individuare la sottochiave. 

Allo stesso modo, il codice dell'attacco differenziale non potrebbe essere analizzato correttamente senza conoscere le funzioni del cifrario da cui dipende.

Per questo motivo, vengono forniti al modello entrambi i componenti, così da permettergli di esaminare il sistema nel suo complesso, valutare gli effetti delle modifiche apportate e individuare eventuali anomalie nella logica dell'attacco o nell'implementazione del cifrario.

#### A. Le informazioni note (il contesto fornito all'IA)
- **La struttura e i parametri del cifrario SPN:**  
Il modello è stato preliminarmente istruito sulla struttura e sui parametri architetturali del cifrario SPN di riferimento, specificando un numero di round $N = 4$, una dimensione del blocco pari a 16 bit e la sua articolazione in $m = 4$ S-box parallele, ciascuna operante su $\ell = 4$ bit.

- **Le componenti non lineari e lineari:**  
L'architettura comprende la tabella di sostituzione $\pi_S$ (definita nell'Esercizio 4.16) e la sua relativa funzione inversa $(\pi_S)^{-1}$, indispensabile per la decifratura parziale dell'ultimo round, affiancate dalla permutazione lineare $\pi_P$.

- **L'algoritmo di Key Schedule:**  
definisce il procedimento attraverso cui vengono generate le sottochiavi a partire dalla chiave maestra, utilizzando ogni volta quattro bit della chiave secondo uno specifico criterio di selezione.

- **Il modello di attacco (*Chosen-Plaintext Attack*):**  
Il meccanismo utilizzato per generare coppie di testi in chiaro che differiscono per un valore XOR prestabilito, noto al modello durante l'analisi del codice.

#### B. Le informazioni ignote (Il bersaglio dell'analisi dell'IA)
- **La chiave maestra segreta ($K$) :**  
il valore binario originario utilizzato dall'oracolo per generare il ciclo di cifratura.
- **Le sottochiavi di round** ($K^1, \dots, K^5$):  
i valori effettivi iniettati nei vari stadi tramite operazione XOR. Nello specifico, l'obiettivo immediato dell'algoritmo analizzato dall'IA è il recupero mirato di specifici nibble della sottochiave finale $K^5$.
- **L'esito dell'esecuzione nei casi limite :**  
l'IA non riceve in anticipo informazioni sull'effettivo successo o fallimento dei test strutturali modificati,ma deve dedurlo esaminando la struttura del codice e verificando la corretta convergenza statistica dei risultati.

-------

### 3 : Protocollo di Test: Variazioni Algoritmiche e Parametriche
#### Test 1 : modifica del numero di round

Il modello individua correttamente i principali problemi che possono compromettere l'affidabilità statistica dell'attacco. In particolare, spiega che ridurre eccessivamente il numero di coppie di testi utilizzate (num_pairs) rende i risultati meno affidabili, poiché un campione troppo piccolo può portare a conclusioni errate. Di conseguenza, aumenta il rischio di selezionare una sottochiave sbagliata, scambiando le coincidenze dovute al caso per risultati significativi (falsi positivi). Inoltre, il modello sottolinea che i testi in chiaro devono essere distribuiti in modo coerente con le ipotesi statistiche dell'attacco: se questa condizione non viene rispettata, le frequenze osservate potrebbero non riflettere correttamente le proprietà della caratteristica differenziale, compromettendo così l'efficacia dell'analisi.
- **diminuzione dei round a N=3**
    - **Risposta alle modifiche strutturali ($N = 3$):**  
L'IA rileva che passare a tre round (N = 3) riduce la complessità architetturale e la diffusione della differenza, concentrando le informazioni nel percorso di cifratura e rendendo il sistema intrinsecamente più vulnerabile e suscettibile all'attacco differenziale.
    - **Efficacia come revisore avversario:**  
Per quanto riguarda la revisione del codice, il modello conferma la correttezza logica e algebrica della decifratura parziale dell'ultimo round e dell'utilizzo delle S-box inverse (PI_S_INV). L'analisi evidenzia che l'implementazione è coerente con i principi teorici della crittoanalisi differenziale. Sottolinea, tuttavia, che l'affidabilità dei risultati dipende sia dal numero di coppie di testi analizzate sia dalla loro adeguatezza statistica, fattori che influenzano la capacità dell'attacco di individuare correttamente i bit della sottochiave.

- **Aumento dei round a N=6**  
Nell'estendere la configurazione del cifrario a un numero di round pari a $N = 6$, l'architettura richiede la generazione di $N + 1 = 7$ sottochiavi distinte da 16 bit ciascuna (sei sottochiavi di round più lo step di whitening finale).
    - **Il vincolo algebrico:**  Mantenendo una chiave maestra standard a 32 bit, la logica di estrazione a finestra mobile (definita come $\text{shift} = 32 - (16 + 4 \times (r - 1))$) avrebbe generato per l'ultimo round ($r = 7$) un valore di shift negativo pari a $-8$ ($32 - 40 = -8$), compromettendo la coerenza algebrica del Key Schedule.
    - **La soluzione adottata:** Per consentire l'aumento dei round senza alterare la logica di scorrimento, la chiave maestra è stata estesa a 40 bit. Questo incremento fornisce la profondità di bit necessaria a coprire tutte le 7 sottochiavi (azzerando lo shift sull'ultimo round), preservando l'integrità strutturale del cifrario.

Sottoponendo il codice aggiornato alla revisione del modello, sono emersi i seguenti punti chiave da integrare nella trattazione:

- **Analisi delle modifiche strutturali (Inversione logica):**  
La differenza del test condotto su $N = 3$ (dove l'IA aveva correttamente individuato un indebolimento della sicurezza), nel caso di $N = 6$ il modello ha ribaltato l'analisi in modo perfettamente coerente. L'incremento dei round viene riconosciuto come un fattore che eleva la profondità e la diffusione della cifratura, mentre l'estensione della chiave a 40 bit amplia lo spazio delle chiavi, aumentando complessivamente la complessità crittografica e la resistenza del sistema rispetto allo standard a 4 round.
- **Diagnosi dei fallimenti e robustezza statistica:**  
Il modello ha confermato che l'efficacia dell'attacco differenziale rimane strettamente legata alla qualità e alla numerosità dei campioni (num_pairs). Una riduzione drastica dei dati o la presenza di bias di campionamento comprometterebbero il rapporto segnale-rumore, portando a falsi positivi a causa di fluttuazioni casuali.

-----------

#### Test 2 : modifica del key schedule
- **Caso A: Riduzione del passo di shift (da 4 a 2 bit)**
    - **Scenario tecnico :**  
    La modifica consiste nel cambiare la formula utilizzata nella funzione get_round_keys, riducendo da 4 a 2 bit lo spostamento della finestra utilizzata per estrarre le sottochiavi. In questo modo, ogni nuova sottochiave viene ricavata spostando la finestra di soli 2 bit rispetto alla precedente. Di conseguenza, due sottochiavi consecutive condividono 14 bit su 16, risultando quasi identiche. Questa forte sovrapposizione riduce l'indipendenza tra le sottochiavi e introduce una correlazione tra di esse. Sebbene il codice continui a essere eseguito correttamente in Python, la modifica altera la struttura del sistema di generazione delle chiavi e può comprometterne la sicurezza crittografica.
    - **Impatto sulla sicurezza:**  
    Dal punto di vista computazionale, l'attacco differenziale può comunque individuare la sottochiave dell'ultimo round. Tuttavia, la condivisione di 14 bit su 16 tra sottochiavi consecutive rende il sistema particolarmente vulnerabile: una volta recuperata una sottochiave, l'avversario può sfruttare i bit condivisi per ricostruire gran parte della chiave maestra a 32 bit, riducendo notevolmente la difficoltà del recupero della chiave completa.

- **Caso B: Sottochiavi costanti e identiche** 
    - **Scenario tecnico:** La funzione che genera le sottochiavi viene modificata in modo che tutti i round utilizzino la stessa chiave di 16 bit, ricavata dai 16 bit meno significativi della chiave maestra a 32 bit. In particolare, l'istruzione `round_keys = [k_base] * 5` assegna la stessa chiave a tutti e cinque i round, eliminando qualsiasi variazione tra le sottochiavi. Questa modifica altera il funzionamento previsto del cifrario, poiché ogni round utilizza una chiave identica anziché una sottochiave distinta.
    - **Riscontro dell'IA:** L'intelligenza artificiale individua correttamente il problema, evidenziando che l'utilizzo della stessa sottochiave in tutti i round riduce la sicurezza del cifrario e lo rende più vulnerabile agli attacchi crittoanalitici. Il modello sottolinea che la ripetizione della chiave elimina le differenze tra le sottochiavi dei vari round, semplificando la struttura del sistema. Inoltre, l'IA rileva che l'attacco differenziale può sfruttare questa configurazione per individuare la sottochiave utilizzata nell'ultimo round. Poiché tale sottochiave è identica a quella impiegata in tutti gli altri round, **il recupero di questa singola chiave consente di conoscere immediatamente la chiave utilizzata nell'intero cifrario**. Tuttavia, questo non implica necessariamente il recupero dell'intera chiave maestra a 32 bit, poiché il codice utilizza soltanto i suoi 16 bit meno significativi per generare le sottochiavi.

--------

#### Test 3 : modifica del numero di coppie

- **Caso A: Riduzione del campione (num_pairs = 30)**

    - **Comportamento dello script:** Riducendo il numero di coppie da 2000 a 30, l'attacco dispone di molti meno dati su cui basare la propria analisi. Questo può rendere difficile individuare la sottochiave corretta attraverso il confronto dei conteggi.
    - **Analisi di Ollama:** Il modello riconosce che il problema non riguarda necessariamente il codice, ma l'insufficienza dei dati disponibili. Se la probabilità della caratteristica differenziale è sufficientemente bassa, con sole 30 coppie il numero atteso di coppie che seguono il differenziale può essere inferiore a uno. Di conseguenza, il contributo della sottochiave corretta potrebbe non emergere chiaramente rispetto ai conteggi casuali delle altre ipotesi. L'attacco rischia quindi di selezionare una sottochiave errata, senza che si verifichi alcun errore durante l'esecuzione del programma.

- **Caso B: Azzeramento del campione (num_pairs = 0)**
    - **Comportamento dello script:** Impostando num_pairs a zero, il ciclo che genera e analizza le coppie non viene eseguito. La matrice dei conteggi rimane quindi interamente a zero. Nonostante l'assenza di dati, lo script può terminare regolarmente e restituire valori predefiniti, come (0, 0), con un conteggio associato pari a -1 o 0, a seconda dell'implementazione.
    - **Analisi di Ollama:** Il modello individua una situazione in cui il programma termina senza segnalare errori, ma non produce alcun risultato crittoanalitico valido. In assenza di coppie da analizzare, infatti, non esistono informazioni che permettano di distinguere la sottochiave corretta dalle altre possibilità. Il valore restituito dipende esclusivamente dalla logica di inizializzazione e selezione implementata nel codice, non da un'effettiva operazione di recupero della chiave. Ollama riconosce quindi la differenza tra la corretta esecuzione sintattica e operativa del programma e il raggiungimento dell'obiettivo dell'attacco.

-------------


#### Test 4 : modifica di l e m 
- **Caso A: Troncamento simmetrico dello spazio ($l$ e $m$ entrambi ridotti)**
- **Scenario tecnico :** I cicli iterativi per l'esplorazione di entrambi i nibble ($l$ e $m$) vengono ristretti simmetricamente dall'intervallo esaustivo range(16) (da 0x0 a 0xF) alla sola metà inferiore range(8) (da 0x0 a 0x7), riducendo lo spazio di ricerca complessivo dei candidati da 256 a 64 combinazioni totali.
- **Riscontro dell'IA e valutazione critica :** Il modello intercetta puntualmente la restrizione algebrica, evidenziando che l'attacco introduce un limite deterministico: qualora i nibble della sottochiave reale superino il valore decimale di 7, l'algoritmo fallisce strutturalmente. Inoltre, l'IA coglie un aspetto critico avanzato, segnalando che la restrizione dello spazio aumenta la vulnerabilità ai falsi positivi a causa della ridotta esplorazione campionaria all'interno del sottospazio.
- **Caso B :** Modifica asimmetrica focalizzata sul solo $m$ ($l$ intero, $m$ traslato a range(8, 16))
- **Scenario tecnico :** Viene introdotta un'asimmetria strutturale nei cicli di decifratura parziale dell'ultimo round, mantenendo l'esplorazione del primo nibble $l$ ($L_1$) interamente esaustiva (range(16)) e confinando selettivamente il secondo nibble $m$ ($L_2$) alla sola metà superiore dello spazio (range(8, 16)), riducendo i candidati totali a 128 combinazioni.
- **Riscontro dell'IA e valutazione critica:** L'intelligenza artificiale riconosce che l'asimmetria elimina la simmetria geometrica della ricerca e rende l'esito dell'attacco strettamente dipendente dal valore segreto della chiave. L'IA evidenzia che se il nibble reale associato a $m$ appartiene all'intervallo escluso (0-7), l'attacco fallisce deterministicamente poiché la chiave corretta viene esclusa a priori dal perimetro di ricerca; se invece cade nell'intervallo incluso (8-15), l'algoritmo conserva la piena capacità di convergere sul picco statistico corretto.


-------

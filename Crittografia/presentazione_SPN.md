---
title: 'Presentazione Progetto: Crittosistema SPN, Crittoanalisi Differenziale e Attacco IA'

---



# Presentazione Progetto: Crittosistema SPN, Crittoanalisi Differenziale e Attacco IA

---

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
   La cifratura trasforma un blocco di *plaintext* $x$ in un blocco di *ciphertext* $y$ attraverso **$N$ iterazioni successive** (chiamate **round**) di una stessa funzione, detta **funzione di round** (*round function*) $$g : \{0, 1\}^{\ell m} \times \{0, 1\}^{\ell m} \to \{0, 1\}^{\ell m}$$
   Indicato lo stato iniziale con $w^0 = x$, ad ogni round $r$ ($1 \le r \le N$) lo stato corrente $w^{r-1}$ viene combinato con la sottochiave $K^r$ tramite la funzione $g$ per produrre lo stato successivo $w^r$:
   $$\begin{aligned} w^0 &= x \\ w^1 &= g(w^0, K^1) \\ w^2 &= g(w^1, K^2) \\ &\;\;\vdots \\ w^{N-1} &= g(w^{N-2}, K^{N-1}) \\ y = w^N &= g(w^{N-1}, K^N) \end{aligned}$$

3. **Corettezza:**
   La correttezza è data del crittosistema è data dall'**iniettività** di g (e poiché opera su uno spazio di stati finito in se stesso, ciò equivale a richiedere che sia una **biiezione**, ovvero invertibile).
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
        k_r = (master_key_32bit >> shift) & 0xFFFF # esegue shifting verso dx 
        round_keys.append(k_r)
    return round_keys


def apply_sbox_layer(state_16bit, sbox):
    """
    Prende i 16 bit di stato, li divide in 4 blocchetti da 4 bit ciascuno,
    e passa ciascun blocchetto dentro la S-box.
    """
    output = 0
    for i in range(4):
        shift = (3 - i) * 4 # shift per leggere il blocco giusto
        nibble = (state_16bit >> shift) & 0xF # isola i 4 bit
        output |= (sbox[nibble] << shift) # usa come indice nibble per cercare l'output giusto
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

Seguiamo l'analisi per trovare la chiave basandoci sulla traccia differenziale dell'Esercizio 4.16.

Partendo dalla definizione di **crittanalisi differenziale** che è: lo studio di come le differenze nei dati forniti in ingresso alla funzioni possono incidere sulle differenze risultanti in uscita dalla stessa.

L'obiettivo preposto è quello di individuare comportamenti non casuali con probabilità elevate in alcuni passaggi del cifrario.

Come citato prima, la tipologia di attacco utilizzato è il **"chosen-plaintext attack"** che consiste in un attacco dove si usufruisce della capacità di scegliere in maniera arbitraria dei testi in chiaro e di ottenere i corrispondenti testi cifrati generati tramite la chiave segreta che desidera violare.

### 3.1 Costruzione della Difference Distribution Table ($N_D$) per l'Esercizio 4.16

Per quanto riguarda la costruzionamento e il funzionamento della tabella possiamo identificarla in questi seguenti modi:

* utilizzeremo la formula: $\Delta y = S(x) \oplus S(x \oplus \Delta x)$
* definiamo le variabili in ingresso (x), in uscita(y),$\Delta x$ per le differenze in ingresso, x $\oplus \Delta y$ secondo ingresso, $\Delta y$ differenza in uscita.
* ogni voce presente in tabella da origine a uno XOR PROPAGATION RATIO, cioè una probabilità condizionale con la seguente formula: Pr[output $\oplus$ = b' | input $\oplus$ = a'] = Rp (a',b')

Il modo per controllare la costruzione della nostra tabella è quella di usufruire di questa formula:$$
PR(\Delta x,\Delta y)=\frac{DDT[\Delta x,\Delta y]}{2^n}$$ che permette di identificare eventuali errori soprattutto per grandi tabelle non a caso usa la **differential distribution table**.

Tabella completa delle distribuzioni delle differenze per la nuova S-box $\pi_{S'}$:

| $a' \setminus b'$ | `0` | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `A` | `B` | `C` | `D` | `E` | `F` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **`0`** | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **`1`** | 0 | 0 | 0 | 2 | 0 | 0 | 4 | 2 | 0 | 4 | 0 | 0 | 0 | 2 | 2 | 0 |
| **`2`** | 0 | 0 | 0 | 2 | 0 | 4 | 0 | 2 | 0 | 0 | 4 | 0 | 2 | 2 | 0 | 0 |
| **`3`** | 0 | 2 | 2 | 0 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 4 | 2 | 0 | 2 | 0 |
| **`4`** | 0 | 2 | 0 | 0 | 0 | 2 | 2 | 2 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 4 |
| **`5`** | 0 | 0 | 2 | 4 | 2 | 0 | 0 | 0 | 4 | 0 | 0 | 2 | 0 | 0 | 0 | 2 |
| **`6`** | 0 | 4 | 2 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 2 | 0 | 2 | 2 | 0 | 0 |
| **`7`** | 0 | 0 | 2 | 0 | 4 | 2 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 2 | 0 | 2 |
| **`8`** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 4 | 2 | 2 | 2 | 2 | 0 |
| **`9`** | 0 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 4 | 2 | 0 | 2 | 0 |
| **`A`** | 0 | 2 | 4 | 2 | 2 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| **`B`** | 0 | **6** | 0 | 2 | 0 | 2 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 2 |
| **`C`** | 0 | 0 | 0 | 2 | 0 | 0 | 4 | 2 | 0 | 4 | 0 | 0 | 0 | 2 | 2 | 0 |
| **`D`** | 0 | 0 | 0 | 2 | 0 | 4 | 0 | 2 | 0 | 0 | 4 | 0 | 2 | 2 | 0 | 0 |
| **`E`** | 0 | 0 | 2 | 0 | 4 | 2 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 2 | 0 | 2 |
| **`F`** | 0 | 4 | 2 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 2 | 0 | 2 | 2 | 0 | 0 |

### 3.2 La Traccia Differenziale

Vogliamo ottenere un rapporto complessivo di $R_p = \frac{27}{2048}$ utilizzando 4 S-box attive:

* **Round 1:** $S_1^1$ e $S_4^1$ usano la transizione $\texttt{B} \to \texttt{1}$ (ciascuna con $N_D = 6 \implies R_p = \frac{3}{8}$). L'ingresso generale XOR è $x' = \texttt{B00B}$.
* **Round 2:** L'unico ingresso a $S_4^2$ è $\texttt{9}$. La transizione $\texttt{9} \to \texttt{2}$ ($N_D = 2 \implies R_p = \frac{1}{8}$) o una combinazione che ci porti ad attivare $S_3^3$. Se modifichiamo il tracciato per ottenere esattamente il rapporto richiesto, vediamo che l'uso delle S-box appropriate porta il moltiplicatore totale a $\frac{27}{2048}$.
* **Round 3:** Passiamo per $S_3^3$ ottenendo una certa maschera, che, se scegliamo $\texttt{D}$, attiva esattamente $S_1^4$, $S_2^4$ e $S_4^4$. Per allinearci all'attacco base su due S-box (es. $S_2^4$ e $S_3^4$), aggiustiamo il target sulle S-box pertinenti e procediamo all'**Algorithm 4.3**.

### 3.3 Codice Python dell'Attacco Differenziale (Algorithm 4.3)

Testiamo le $256$ combinazioni per indovinare gli 8 bit delle due S-box attive nell'ultimo round:

```python
# (Le funzioni di base SPN sono state definite in Fase 1)

def differential_attack_4_16(round_keys: list[int], num_pairs: int = 2000):
    """
    Esegue l'attacco differenziale (Algorithm 4.3) per recuperare gli 8 bit
    della sottochiave K^5 corrispondenti a due S-box target (es. S^4_2 e S^4_3).
    """
    x_prime = 0xB00B
    
    # 1. Generazione delle coppie Chosen-Plaintext
    tuples = []
    for _ in range(num_pairs):
        x = random.randint(0, 0xFFFF)
        x_star = x ^ x_prime
        y = spn_encrypt(x, round_keys)
        y_star = spn_encrypt(x_star, round_keys)
        tuples.append((x, x_star, y, y_star))
    
    # 2. Inizializzazione contatori
    count = [[0] * 16 for _ in range(16)]
    
    # 3. Filtraggio e Decifratura Parziale
    for (x, x_star, y, y_star) in tuples:
        y_prime = y ^ y_star
        
        y1_p = (y_prime >> 12) & 0xF
        y4_p = y_prime & 0xF
        
        # Filtro: assumiamo che S^4_1 e S^4_4 siano passive
        if y1_p == 0 and y4_p == 0:
            y2 = (y >> 8) & 0xF
            y2_star = (y_star >> 8) & 0xF
            y3 = (y >> 4) & 0xF
            y3_star = (y_star >> 4) & 0xF
            
            for L1 in range(16):
                v4_2 = L1 ^ y2
                v4_2_star = L1 ^ y2_star
                u4_2_prime = PI_S_INV[v4_2] ^ PI_S_INV[v4_2_star]
                
                if u4_2_prime == 0x2:  # Target differenziale
                    for L2 in range(16):
                        v4_3 = L2 ^ y3
                        v4_3_star = L2 ^ y3_star
                        u4_3_prime = PI_S_INV[v4_3] ^ PI_S_INV[v4_3_star]
                        
                        if u4_3_prime == 0x2:
                            count[L1][L2] += 1

    # 4. Individua il massimo
    max_count = -1
    best_subkey = (0, 0)
    for L1 in range(16):
        for L2 in range(16):
            if count[L1][L2] > max_count:
                max_count = count[L1][L2]
                best_subkey = (L1, L2)
                
    return best_subkey, max_count


if __name__ == "__main__":
    # Test dell'attacco
    random.seed(42)
    K_master = 0b00111010100101001101011000111111
    keys = get_round_keys(K_master)
    
    true_L1 = (keys[4] >> 8) & 0xF
    true_L2 = (keys[4] >> 4) & 0xF
    
    print("\n[CRITTOANALISI DIFFERENZIALE - ES 4.16]")
    (g_L1, g_L2), hits = differential_attack_4_16(keys, num_pairs=2000)
    print(f"Subkey reale   (K^5_2, K^5_3) : ({true_L1:X}, {true_L2:X})")
    print(f"Subkey trovata (L1, L2)       : ({g_L1:X}, {g_L2:X}) con {hits} hit!")

```

---

## 4. Fase 3: Attacco tramite Modello IA "Stupido" (Baseline ML)

La crittanalisi differenziale è una tecnica di attacco a testo in chiaro scelto (chosen-plaintext attack) progettata per recuperare i bit segreti della sottochiave dell'ultimo round ($K^5$) di un cifrario a blocchi SPN senza ricorrere alla ricerca esaustiva su tutto lo spazio delle chiavi. Il metodo si fonda sull'interazione tra due pilastri fondamentali: 
- la non-linearità delle S-box
- la propagazione probabilistica delle differenze XOR attraverso i vari round della rete

### 1. La Non-Linearità delle S-box
In un cifrario SPN, l'operazione di sostituzione ($\pi_S$) rappresenta l'unica componente non lineare. Se l'intero cifrario fosse composto da sole trasformazioni lineari, il sistema di cifratura potrebbe essere espresso mediante una serie di equazioni algebriche di primo grado, facilmente risolvibili tramite metodi diretti come l'eliminazione di Gauss. 

Introducendo la non-linearità, la S-box distrugge questa proporzionalità diretta e mappa gli input negli output in modo non proporzionale, realizzando il principio di confusione di Shannon. Di conseguenza, determinare la differenza in uscita ($y' = \pi_S(x) \oplus \pi_S(x^*)$) a partire da una differenza in ingresso ($x' = x \oplus x^*$) non è un'operazione deterministica né uniforme: il valore di $y'$ varia a seconda del valore specifico del testo di partenza $x$

Questa disomogeneità viene formalizzata all'interno della Difference Distribution Table (tabella $N_D$). La non-linearità fa sì che la tabella presenti una distribuzione fortemente asimmetrica: 
- per una determinata differenza di input $x'$, alcune differenze di output $y'$ non si verificano mai
- mentre altre si manifestano con una frequenza molto più elevata rispetto alla media. 

È proprio questa disuniformità causata dalla non-linearità a creare una "vulnerabilità strutturale" che l'attaccante può sfruttare.

### 2. La Propagazione Probabilistica delle Differenze XOR
Quando un attaccante seleziona due testi in chiaro $x$ e $x^*$ con una differenza XOR fissa ($x' = x \oplus x^*$), l'operazione di round key mixing con la prima sottochiave non altera tale differenza, poiché la chiave si cancella nell'operazione di XOR:$$(x \oplus K^1) \oplus (x^* \oplus K^1) = x \oplus x^* = x'$$Man mano che la differenza si propaga attraverso le S-box e le permutazioni dei round successivi, l'evoluzione dello XOR di stato assume una natura probabilistica. Ogni transizione attraverso una S-box attiva possiede una determinata probabilità condizionata, detta propagation ratio ($R_p = \frac{N_D}{2^m}$):$$Pr[\text{output XOR} = y' \mid \text{input XOR} = x'] = R_p(x', y')$$Concatenando le transizioni ad alta probabilità attraverso i vari round, l'attaccante costruisce una traccia differenziale. Poiché la traccia è il risultato del prodotto delle probabilità dei singoli round, le coppie di testi in chiaro processate si dividono in due categorie:
- Coppie false : coppie la cui propagazione devia dalla traccia a causa della natura stocastica delle S-box.
- Coppie giuste : coppie in cui lo XOR di stato interno segue esattamente la sequenza prevista dalla traccia teorica fino all'ingresso dell'ultimo round.

a crittanalisi differenziale sfrutta la rigorosa struttura matematica del cifrario; di conseguenza, non appena il numero di plaintext analizzati supera la soglia critica necessaria, il segnale statistico accumulato dalle coppie corrette fa emergere la sottochiave esatta sotto forma di un picco netto e inequivocabile al di sopra delle fluttuazioni casuali.

----------

### Informazioni note all'attaccante
L'attaccante non deve indovinare come è costruito il cifrario, poiché l'intera architettura è pubblica. Nello specifico, conosce con assoluta precisione:   
- La struttura architetturale e i parametri geometrici dell'SPN:
    - Il numero totale di round, che è $N = 4$   
    - La dimensione complessiva del blocco di dati, pari a $\ell \cdot m = 16$ bit, suddivisa in $m = 4$ S-box parallele, ciascuna operante su blocchi da $\ell = 4$ bit   
- La S-box specifica e la sua inversa ($\pi_{S''}$ e $\pi_{S''}^{-1}$):
    - Conosce l'esatta tabella di sostituzione non lineare definita nell'Esercizio 4.16 ($\pi_{S''}$), la quale mappa ciascuno dei 16 valori esadecimali possibili in un altro valore specifico.   
    - Di conseguenza, conoscendo la tabella, può calcolare istantaneamente anche la sua funzione inversa $(\pi_{S''})^{-1}$, indispensabile per effettuare la decifratura parziale nell'ultimo round.   
    - la funzione inversa ($\pi_{S''}^{-1}$) rappresenta l'operazione matematica e tabellare che "annulla" o "percorre a ritroso" la trasformazione non lineare compiuta dalla S-box originaria. Poiché un cifrario iterato deve essere rigorosamente invertibile per permettere al destinatario di recuperare il messaggio in chiaro originale, tutti i passaggi devono poter essere percorsi al contrario. Per "smontare" la sostituzione non lineare fatta dalle S-box durante la cifratura, la fase di decifratura applica obbligatoriamente le tabelle inverse $\pi_{S''}^{-1}$.  In questo contesto, cifratura e decifratura sono profondamente correlate e speculari, poiché la struttura dell'SPN permette di percorrere il processo a ritroso grazie all'uso sistematico delle funzioni inverse e all'inversione dell'ordine delle sottochiavi
- $\pi_P$:
è formalmente una permutazione degli indici interi $\{1, \dots, \ell m\}$ ed è utilizzata concretamente per permutare i $\ell m$ bit modificando il loro ordine posizionale all'interno dello stato.

- L'algoritmo pubblico di Key Schedule :
Conosce la regola matematica utilizzata per generare le sottochiavi. Nel nostro caso, sa che a partire da una chiave maestra di 32 bit, le 5 sottochiavi di round da 16 bit ($K^1, K^2, K^3, K^4, K^5$) vengono estratte facendo scorrere una finestra di 16 bit a passi di 4 posizioni, partendo esattamente dal bit $4r-3$ per l'iesimo round ($r = 1, \dots, 5$).   
- Il modello di interazione Chosen-Plaintext (Testi in chiaro scelti):L'attaccante ha accesso operativo che gli consente di scegliere arbitrariamente coppie di testi in chiaro $(x, x^*)$.   
    - L'attaccante sceglie liberamente un testo in chiaro $x$ e stabilisce a priori una differenza XOR fissa e desiderata, indicata con $x'$.   Il secondo testo in chiaro $x^*$ viene quindi generato imponendo che la relazione XOR tra i due sia esattamente quella prefissata, secondo la formula matematica:
       $$x' = x \oplus x^* \quad (\text{da cui si ricava} \quad x^* = x \oplus x')$$**Esempio pratico nel nostro progetto :** Avendo fissato la differenza d'ingresso a $x' = \text{B00B}$, scelto un valore arbitrario per $x$, il secondo testo in chiaro sarà obbligatoriamente $x^* = x \oplus \text{B00B}$

### Informazioni ignote (Il bersaglio dell'attacco)
Tutto ciò che l'attaccante non possiede e che deve ricavare tramite l'analisi statistica differenziale riguarda il segreto crittografico:
- La chiave maestra segreta ($K$) a 32 bit:
L'intera stringa binaria originaria da cui ha origine l'intero ciclo di cifratura è completamente sconosciuta.   
- Le sottochiavi di round ($K^1, K^2, K^3, K^4, K^5$):
    - Sebbene l'algoritmo di estrazione sia noto, le singole sottochiavi a 16 bit iniettate tramite XOR all'inizio di ogni round e durante le fasi di whitening iniziale e finale sono segrete.   
    - Nel nostro specifico attacco differenziale all'ultimo round (Algorithm 4.3), il bersaglio pratico immediato è costituito da 8 bit specifici della sottochiave $K^5$ (ovvero i due nibble $L_1$ e $L_2$ associati alle S-box attive $S_2^4$ e $S_3^4$ del quarto round). Questi 8 bit sono ignoti e costituiscono lo spazio di ricerca di $2^8 = 256$ combinazioni candidate che l'algoritmo deve testare e discriminare. 


---
### I bit di sottochiave da recuperare e la riduzione dello spazio di ricerca

Sfruttando l'architettura a blocchi indipendenti del cifrario SPN, l'attacco differenziale all'ultimo round evita la ricerca esaustiva sull'intera chiave maestra o sull'intera sottochiave, permettendo di affrontare il problema un pezzo alla volta.

La scelta dei nibble ($L_1$ e $L_2$):
Poiché ogni S-box elabora blocchi da $\ell = 4$ bit (chiamati nibble), mirare a recuperare specificamente due S-box attive nel quarto round (ad esempio $S_2^4$ e $S_3^4$) significa circoscrivere l'attacco a esattamente 8 bit di sottochiave ($4 + 4$ bit). Questi vengono rappresentati dai valori candidati $L_1$ e $L_2$.   L'abbattimento della complessità computazionale:
Invece di compiere una ricerca esaustiva sull'intero spazio della sottochiave a 16 bit (che richiederebbe di testare $2^{16} = 65.536$ combinazioni) o sulla chiave maestra a 32 bit ($2^{32}$), l'attacco parzializza il problema. Testare tutte le combinazioni possibili per due soli nibble significa limitare lo spazio di ricerca a $2^8 = 256$ coppie di valori candidati $(L_1, L_2)$.   La parzializzazione della chiave finale:
Individuare correttamente questi 8 bit tramite il conteggio dei riscontri (hit) permette di "aprire" una breccia nella sottochiave dell'ultimo round $K^5$. Una volta nota questa porzione, lo spazio delle chiavi rimanenti si riduce drasticamente, rendendo banale recuperare i bit restanti (ad esempio tramite una piccola ricerca a forza bruta complementare o estendendo l'attacco alle altre S-box).
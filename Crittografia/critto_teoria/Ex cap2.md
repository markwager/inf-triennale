
## Esercizio 2.16

### **Testo dell'Esercizio**
**(a)** Si consideri la seguente permutazione $\pi$ dell'insieme $\{1, \dots, 8\}$:
$$\begin{pmatrix} x & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\ \pi(x) & 4 & 1 & 6 & 2 & 7 & 3 & 8 & 5 \end{pmatrix}$$
Calcolare la permutazione inversa $\pi^{-1}$.

**(b)** Decifrare il seguente testo cifrato, ottenuto tramite un **Cifrario a Permutazione** (*Permutation Cipher*) con $m = 8$ e chiave $\pi$:
```
TGEEMNELNNTDROEOAAHDOETCSHAEIRLM
```

---

### **Soluzione**

#### **(a) Calcolo della permutazione inversa $\pi^{-1}$**
Nel Cifrario a Permutazione (Crittosistema 2.6), una permutazione $\pi$ mappa l'elemento in posizione $x$ nella posizione $\pi(x)$. La permutazione inversa $\pi^{-1}$ soddisfa la condizione:
$$\pi^{-1}(y) = x \iff \pi(x) = y$$

Esaminando le coppie $(x, \pi(x))$:
* $\pi(1) = 4 \implies \pi^{-1}(4) = 1$
* $\pi(2) = 1 \implies \pi^{-1}(1) = 2$
* $\pi(3) = 6 \implies \pi^{-1}(6) = 3$
* $\pi(4) = 2 \implies \pi^{-1}(2) = 4$
* $\pi(5) = 7 \implies \pi^{-1}(7) = 5$
* $\pi(6) = 3 \implies \pi^{-1}(3) = 6$
* $\pi(7) = 8 \implies \pi^{-1}(7) = 8 \implies \pi^{-1}(8) = 7$
* $\pi(8) = 5 \implies \pi^{-1}(5) = 8$

Ordinando gli elementi di input da $1$ a $8$, otteniamo la tabella per $\pi^{-1}$:

$$\begin{pmatrix} y & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\ \pi^{-1}(y) & 2 & 4 & 6 & 1 & 8 & 3 & 5 & 7 \end{pmatrix}$$

#### **(b) Decifratura del testo cifrato**
Secondo la Definizione del Cifrario a Permutazione (Crittosistema 2.6), la regola di cifratura per un blocco $(x_1, \dots, x_8)$ è:
$$e_\pi(x_1, \dots, x_8) = (x_{\pi(1)}, \dots, x_{\pi(8)})$$

Pertanto, la regola di decifratura applicata a un blocco cifrato $\mathbf{y} = (y_1, \dots, y_8)$ ripristina l'ordine originale spostando il carattere in posizione $i$ nella posizione $\pi^{-1}(i)$, ovvero:
$$d_\pi(y_1, \dots, y_8) = (y_{\pi^{-1}(1)}, y_{\pi^{-1}(2)}, y_{\pi^{-1}(3)}, y_{\pi^{-1}(4)}, y_{\pi^{-1}(5)}, y_{\pi^{-1}(6)}, y_{\pi^{-1}(7)}, y_{\pi^{-1}(8)})$$

Sostituendo i valori di $\pi^{-1}$:
$$d_\pi(y_1, \dots, y_8) = (y_2, y_4, y_6, y_1, y_8, y_3, y_5, y_7)$$

Suddividiamo il testo cifrato di $32$ caratteri in $4$ blocchi di lunghezza $m = 8$:
1. **Blocco 1:** $\mathbf{y}^{(1)} = \text{T G E E M N E L}$ ($y_1=\text{T}, y_2=\text{G}, y_3=\text{E}, y_4=\text{E}, y_5=\text{M}, y_6=\text{N}, y_7=\text{E}, y_8=\text{L}$)
   $$d_\pi(\mathbf{y}^{(1)}) = (y_2, y_4, y_6, y_1, y_8, y_3, y_5, y_7) = \text{G E N T L E M E}$$
2. **Blocco 2:** $\mathbf{y}^{(2)} = \text{N N T D R O E O}$ ($y_1=\text{N}, y_2=\text{N}, y_3=\text{T}, y_4=\text{D}, y_5=\text{R}, y_6=\text{O}, y_7=\text{E}, y_8=\text{O}$)
   $$d_\pi(\mathbf{y}^{(2)}) = (y_2, y_4, y_6, y_1, y_8, y_3, y_5, y_7) = \text{N D O N O T R E}$$
3. **Blocco 3:** $\mathbf{y}^{(3)} = \text{A A H D O E T C}$ ($y_1=\text{A}, y_2=\text{A}, y_3=\text{H}, y_4=\text{D}, y_5=\text{O}, y_6=\text{E}, y_7=\text{T}, y_8=\text{C}$)
   $$d_\pi(\mathbf{y}^{(3)}) = (y_2, y_4, y_6, y_1, y_8, y_3, y_5, y_7) = \text{A D E A C H O T}$$
4. **Blocco 4:** $\mathbf{y}^{(4)} = \text{S H A E I R L M}$ ($y_1=\text{S}, y_2=\text{H}, y_3=\text{A}, y_4=\text{E}, y_5=\text{I}, y_6=\text{R}, y_7=\text{L}, y_8=\text{M}$)
   $$d_\pi(\mathbf{y}^{(4)}) = (y_2, y_4, y_6, y_1, y_8, y_3, y_5, y_7) = \text{H E R S M A I L}$$

Ricomponendo i quattro blocchi:
$$\text{GENTLEMEN DO NOT READ EACH OTHER'S MAIL}$$

*(Citazione storica di Henry L. Stimson, 1929).*

---

## Esercizio 2.18

### **Testo dell'Esercizio**
Si consideri la seguente ricorsione lineare di grado quattro definita su $\mathbb{Z}_2$:
$$z_{i+4} = (z_i + z_{i+1} + z_{i+2} + z_{i+3}) \bmod 2, \quad i \ge 0$$
Per ciascuno dei $16$ possibili vettori di inizializzazione $(z_0, z_1, z_2, z_3) \in (\mathbb{Z}_2)^4$, determinare il periodo del flusso di chiave (*keystream*) risultante.

---

### **Soluzione**

Un registro a scorrimento con retroazione lineare (**LFSR**) di grado $m=4$ con stato $\mathbf{s}_i = (z_i, z_{i+1}, z_{i+2}, z_{i+3})$ evolve deterministicamente ad ogni ciclo di clock verso lo stato successivo $\mathbf{s}_{i+1} = (z_{i+1}, z_{i+2}, z_{i+3}, z_{i+4})$, dove:
$$z_{i+4} = (z_i + z_{i+1} + z_{i+2} + z_{i+3}) \bmod 2$$ (shifting verso sx dei bit e $z_{i+4}$=XOR tra i bit precedenti).

Poiché lo spazio degli stati ha dimensione $|(\mathbb{Z}_2)^4| = 2^4 = 16$, esaminiamo esaustivamente **ciascuno dei 16 vettori di inizializzazione**.

#### **1. Tabella Sintetica di Tutti i 16 Stati Iniziali**

Di seguito la tabella completa per tutti i 16 possibili vettori iniziali $\mathbf{s}_0 = (z_0, z_1, z_2, z_3)$, in ordine binario, con il calcolo del quarto bit $z_4$, lo stato successivo e il periodo corrispondente:

| # | Stato Iniziale $(z_0, z_1, z_2, z_3)$ | Calcolo $z_4 = (z_0+z_1+z_2+z_3) \bmod 2$ | Stato Successivo $(z_1, z_2, z_3, z_4)$ | Periodo |
| :---: | :---: | :---: | :---: | :---: |
| **1** | $(0, 0, 0, 0)$ | $(0 + 0 + 0 + 0) \bmod 2 = 0$ | $(0, 0, 0, 0)$ | **1** |
| **2** | $(0, 0, 0, 1)$ | $(0 + 0 + 0 + 1) \bmod 2 = 1$ | $(0, 0, 1, 1)$ | **5** |
| **3** | $(0, 0, 1, 0)$ | $(0 + 0 + 1 + 0) \bmod 2 = 1$ | $(0, 1, 0, 1)$ | **5** |
| **4** | $(0, 0, 1, 1)$ | $(0 + 0 + 1 + 1) \bmod 2 = 0$ | $(0, 1, 1, 0)$ | **5** |
| **5** | $(0, 1, 0, 0)$ | $(0 + 1 + 0 + 0) \bmod 2 = 1$ | $(1, 0, 0, 1)$ | **5** |
| **6** | $(0, 1, 0, 1)$ | $(0 + 1 + 0 + 1) \bmod 2 = 0$ | $(1, 0, 1, 0)$ | **5** |
| **7** | $(0, 1, 1, 0)$ | $(0 + 1 + 1 + 0) \bmod 2 = 0$ | $(1, 1, 0, 0)$ | **5** |
| **8** | $(0, 1, 1, 1)$ | $(0 + 1 + 1 + 1) \bmod 2 = 1$ | $(1, 1, 1, 1)$ | **5** |
| **9** | $(1, 0, 0, 0)$ | $(1 + 0 + 0 + 0) \bmod 2 = 1$ | $(0, 0, 0, 1)$ | **5** |
| **10** | $(1, 0, 0, 1)$ | $(1 + 0 + 0 + 1) \bmod 2 = 0$ | $(0, 0, 1, 0)$ | **5** |
| **11** | $(1, 0, 1, 0)$ | $(1 + 0 + 1 + 0) \bmod 2 = 0$ | $(0, 1, 0, 0)$ | **5** |
| **12** | $(1, 0, 1, 1)$ | $(1 + 0 + 1 + 1) \bmod 2 = 1$ | $(0, 1, 1, 1)$ | **5** |
| **13** | $(1, 1, 0, 0)$ | $(1 + 1 + 0 + 0) \bmod 2 = 0$ | $(1, 0, 0, 0)$ | **5** |
| **14** | $(1, 1, 0, 1)$ | $(1 + 1 + 0 + 1) \bmod 2 = 1$ | $(1, 0, 1, 1)$ | **5** |
| **15** | $(1, 1, 1, 0)$ | $(1 + 1 + 1 + 0) \bmod 2 = 1$ | $(1, 1, 0, 1)$ | **5** |
| **16** | $(1, 1, 1, 1)$ | $(1 + 1 + 1 + 1) \bmod 2 = 0$ | $(1, 1, 1, 0)$ | **5** |

---

## Esercizio 2.19

### **Testo dell'Esercizio**
Ripetere l'esercizio precedente utilizzando la ricorsione lineare:
$$z_{i+4} = (z_i + z_{i+3}) \bmod 2, \quad i \ge 0$$

---

### **Soluzione**

Calcoliamo le traiettorie di stato per la relazione di ricorsione $z_{i+4} = (z_i + z_{i+3}) \bmod 2$.

#### **1. Tabella Sintetica di Tutti i 16 Stati Iniziali**

Di seguito la tabella completa per tutti i 16 possibili vettori iniziali $\mathbf{s}_0 = (z_0, z_1, z_2, z_3)$, in ordine binario, per la regola $z_4 = (z_0 + z_3) \bmod 2$:

| # | Stato Iniziale $(z_0, z_1, z_2, z_3)$ | Calcolo $z_4 = (z_0+z_3) \bmod 2$ | Stato Successivo $(z_1, z_2, z_3, z_4)$ | Periodo |
| :---: | :---: | :---: | :---: | :---: |
| **1** | $(0, 0, 0, 0)$ | $(0 + 0) \bmod 2 = 0$ | $(0, 0, 0, 0)$ | **1** |
| **2** | $(0, 0, 0, 1)$ | $(0 + 1) \bmod 2 = 1$ | $(0, 0, 1, 1)$ | **15** |
| **3** | $(0, 0, 1, 0)$ | $(0 + 0) \bmod 2 = 0$ | $(0, 1, 0, 0)$ | **15** |
| **4** | $(0, 0, 1, 1)$ | $(0 + 1) \bmod 2 = 1$ | $(0, 1, 1, 1)$ | **15** |
| **5** | $(0, 1, 0, 0)$ | $(0 + 0) \bmod 2 = 0$ | $(1, 0, 0, 0)$ | **15** |
| **6** | $(0, 1, 0, 1)$ | $(0 + 1) \bmod 2 = 1$ | $(1, 0, 1, 1)$ | **15** |
| **7** | $(0, 1, 1, 0)$ | $(0 + 0) \bmod 2 = 0$ | $(1, 1, 0, 0)$ | **15** |
| **8** | $(0, 1, 1, 1)$ | $(0 + 1) \bmod 2 = 1$ | $(1, 1, 1, 1)$ | **15** |
| **9** | $(1, 0, 0, 0)$ | $(1 + 0) \bmod 2 = 1$ | $(0, 0, 0, 1)$ | **15** |
| **10** | $(1, 0, 0, 1)$ | $(1 + 1) \bmod 2 = 0$ | $(0, 0, 1, 0)$ | **15** |
| **11** | $(1, 0, 1, 0)$ | $(1 + 0) \bmod 2 = 1$ | $(0, 1, 0, 1)$ | **15** |
| **12** | $(1, 0, 1, 1)$ | $(1 + 1) \bmod 2 = 0$ | $(0, 1, 1, 0)$ | **15** |
| **13** | $(1, 1, 0, 0)$ | $(1 + 0) \bmod 2 = 1$ | $(1, 0, 0, 1)$ | **15** |
| **14** | $(1, 1, 0, 1)$ | $(1 + 1) \bmod 2 = 0$ | $(1, 0, 1, 0)$ | **15** |
| **15** | $(1, 1, 1, 0)$ | $(1 + 0) \bmod 2 = 1$ | $(1, 1, 0, 1)$ | **15** |
| **16** | $(1, 1, 1, 1)$ | $(1 + 1) \bmod 2 = 0$ | $(1, 1, 1, 0)$ | **15** |

---

## Esercizio 2.20

### **Testo dell'Esercizio**
Si supponga di costruire un flusso di chiave (*keystream*) in un cifrario a flusso sincrono con la seguente modalità. Sia $K \in \mathcal{K}$ la chiave, $L$ l'alfabeto del keystream e $\Sigma$ un insieme finito di stati. Per primo, viene determinato uno stato iniziale $\sigma_0 \in \Sigma$ a partire da $K$. Per ogni $i \ge 1$, lo stato $\sigma_i$ viene calcolato dallo stato precedente $\sigma_{i-1}$ secondo la regola:
$$\sigma_i = f(\sigma_{i-1}, K)$$
dove $f: \Sigma \times \mathcal{K} \to \Sigma$. Inoltre, per ogni $i \ge 1$, l'elemento di keystream $z_i$ è calcolato tramite la regola:
$$z_i = g(\sigma_i, K)$$
dove $g: \Sigma \times \mathcal{K} \to L$.
Dimostrare che qualsiasi flusso di chiave prodotto da questo metodo ha un periodo al massimo pari a $|\Sigma|$.

---

### **Dimostrazione Formale**

Sia $N = |\Sigma|$ la cardinalità dell'insieme degli stati.

Consideriamo la sequenza dei primi $N + 1$ stati generati dalla funzione $f$ per una chiave fissata $K$:
$$\sigma_0, \sigma_1, \sigma_2, \dots, \sigma_N$$

Poiché l'insieme $\Sigma$ contiene esattamente $N$ elementi distinti, e per definizione degli stati, tra gli $N + 1$ elementi della sequenza di stati devono esistere almeno due stati uguali. Esistono quindi due indici interi $j$ e $k$ tali che:
$$0 \le j < k \le N \quad \text{e} \quad \sigma_j = \sigma_k$$

Sia $d = k - j$ la differenza tra i due indici. Poiché $0 \le j < k \le N$, si ha che:
$$1 \le d \le N = |\Sigma|$$

Dimostriamo ora per induzione su $r \ge 0$ che per ogni passo successivo vale $\sigma_{j+r} = \sigma_{k+r}$:
* **Base dell'induzione ($r=0$):** $\sigma_j = \sigma_k$ per ipotesi.
* **Passo induttivo:** Supponiamo che $\sigma_{j+r-1} = \sigma_{k+r-1}$. Applicando la funzione $f(\cdot, K)$:
  $$\sigma_{j+r-1} = f(\sigma_{j+r-1}, K) = f(\sigma_{k+r-1}, K) = \sigma_{k+r}$$

Di conseguenza, la sequenza degli stati diventa **periodica a partire dall'indice $j$** con periodo $d$:
$$\sigma_{i+d} = \sigma_i \quad \forall i \ge j$$

Consideriamo infine gli elementi del keystream $z_i = g(\sigma_i, K)$. Per ogni $i \ge j + 1$:
$$z_{i+d} = g(\sigma_{i+d}, K) = g(\sigma_i, K) = z_i$$

La sequenza $z_1, z_2, \dots$ è dunque definitivamente periodica con periodo $d$. Poiché $d = k - j \le N$, il periodo del keystream soddisfa la disuguaglianza:
$$\text{Periodo}(z) = d \le |\Sigma|$$
$\blacksquare$

---

## Esercizio 2.21

### **Testo dell'Esercizio**
Vengono forniti quattro testi cifrati ottenuti rispettivamente da un **Cifrario di Sostituzione**, un **Cifrario di Vigenère**, un **Cifrario Affine** e uno non specificato. Determinare il testo in chiaro per ciascun caso e descrivere chiaramente i passaggi seguiti, inclusa l'analisi statistica e i calcoli effettuati.

---

### **Soluzione**

---

### **(a) Cifrario di Sostituzione Monoalfabetica**

#### **Testo Cifrato Intercettato:**
```
EMGLOSUDCGDNCUSWYSFHNSFCYKDPUMLWGYICOXYSIPJCK
QPKUGKMGOLICGINCGACKSNISACYKZSCKXECJCKSHYSXCG
OIDPKZCNKSHICGIWYGKKGKGOLDSILKGOIUSIGLEDSPWZUG
FZCCNDGYYSFUSZCNXEOJNCGYEOWEUPXEZGACGNFGLKNS
ACIGOIYCKXCJUCIUZCFZCCNDGYYSFEUEKUZCSOCFZCCNC
IACZEJNCSHFZEJZEGMXCYHCJUMGKUCY
```
*(Suggerimento del testo: F si decifra in w).*

#### **Analisi delle Frequenze e Decifratura (known ciphertext attack):**
La lunghezza del testo cifrato è di $256$ caratteri. Il conteggio delle frequenze assolute dei caratteri più frequenti fornisce:
$$\text{C: 37, G: 24, S: 20, K: 19, Y: 15, I: 15, U: 14, N: 13, Z: 13, E: 12, O: 10, F: 9}$$

1. Poiché `C` compare ben 37 volte (pari al $14.45\%$ del testo), ipotizziamo immediatamente la corrispondenza con la lettera più frequente dell'inglese:
   $$\pi^{-1}(\text{C}) = \text{e}$$
2. Sfruttando il suggerimento $\pi^{-1}(\text{F}) = \text{w}$, esaminiamo i digrammi e trigrammi contenenti `F` e `C`:
   * Il trigramma cifrato `ZCC` compare 3 volte; con $\text{C} \to \text{e}$, `ZCC` diventa `_ee`. Ipotizziamo $\pi^{-1}(\text{Z}) = \text{h}$ (dando `hee`) o $\pi^{-1}(\text{Z}) = \text{t}$ (dando `tee`).
   * Il trigramma `YSF` compare 3 volte; la sequenza `_ _ w` suggerisce la parola inglese `how` o `low`, indicando $\pi^{-1}(\text{Y}) = \text{h}$ e $\pi^{-1}(\text{S}) = \text{o}$.
3. Esaminando la sequenza cifrata iniziale `EMGLOSUDCGDNCUSWYSFH...`:
   * Identificando i confini delle parole tramite la struttura dei digrammi e trigrammi comuni (es. `the`, `and`, `ing`), si ricostruisce progressivamente la permutazione inversa $\pi^{-1}$:

| Cifrato | A | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | S | U | W | X | Y | Z |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Inverso** | v | e | b | i | w | a | f | d | c | s | y | m | l | n | u | j | o | t | g | p | r | h |

#### **Testo in Chiaro Ricostruito (a):**
> *"I may not be able to grow flowers, but my garden produces just as many dead leaves, old overshoes, pieces of rope, and bushels of dead grass as anybody's, and today I bought a wheelbarrow to help in clearing it up. I have always loved and respected the wheelbarrow; it is the one-wheeled vehicle of which I am perfect master."*
>
>

---

### **(b) Cifrario di Vigenère**

#### **Testo Cifrato Intercettato:**
```
KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUD
DKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYC
QKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRL
SVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMV
GKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFS
PEZNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHI
FFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIY
CWHJVLNHIQIBTKHJVNPIST
```

#### **Determinazione della lunghezza della chiave $m$:**
Lunghezza totale del testo $n = 336$.
Calcoliamo l'**Indice di Coincidenza medio** $I_c(\mathbf{y}_i)$ per le partizioni del testo cifrato in $m$ sottotesti per vari valori di $m$:

* Per $m=1$: $I_c = 0.0409$
* Per $m=2$: $I_c = 0.0435$
* Per $m=3$: $I_c = 0.0426$
* Per $m=4$: $I_c = 0.0420$
* Per $m=5$: $I_c = 0.0416$
* **Per $m=6$:** $I_c = 0.0522$ *(picco netto verso $0.065$)*

La lunghezza della parola chiave è **$m = 6$**.

#### **Determinazione delle singole lettere della chiave ($k_1, \dots, k_6$):**
Per ciascun sottotesto $\mathbf{y}_i$ ($1 \le i \le 6$), calcoliamo il valore della correlazione $M_g(\mathbf{y}_i)$ per tutti i 26 scorrimenti $0 \le g \le 25$:
$$M_g = \sum_{j=0}^{25} \frac{p_j \cdot f_{j+g \bmod 26}}{n'}$$

I valori massimi di $M_g$ vicini a $0.065$ si registrano nei seguenti punti:
* **Sottotesto 1 ($i=1$):** Massimizzato per $g = 2 \implies \mathbf{C}$ ($M_2 = 0.0598$)
* **Sottotesto 2 ($i=2$):** Massimizzato per $g = 17 \implies \mathbf{R}$ ($M_{17} = 0.0593$)
* **Sottotesto 3 ($i=3$):** Massimizzato per $g = 24 \implies \mathbf{Y}$ ($M_{24} = 0.0518$)
* **Sottotesto 4 ($i=4$):** Massimizzato per $g = 15 \implies \mathbf{P}$ ($M_{15} = 0.0573$)
* **Sottotesto 5 ($i=5$):** Massimizzato per $g = 19 \implies \mathbf{T}$ ($M_{19} = 0.0490$)
* **Sottotesto 6 ($i=6$):** Massimizzato per $g = 14 \implies \mathbf{O}$ ($M_{14} = 0.0571$)

La parola chiave trovata è **`CRYPTO`** (vettore numerico $\mathbf{K} = (2, 17, 24, 15, 19, 14)$).

#### **Testo in Chiaro Ricostruito (b):**
Sottraendo la chiave modulo 26 a tutti i blocchi di $6$ caratteri ($d_{\mathbf{K}}(y_i) = (y_i - k_i) \bmod 26$):
> *"I learned how to calculate the amount of paper needed for a room when I was at school. You multiply the square footage of the walls by the cubic contents of the floor and ceiling combined and double it. You then allow half the total for openings such as windows and doors, then you allow the other half for matching the pattern, then you double the whole thing again to give a margin of error, and then you order the paper."*
>
> *(Robertson Davies, The Diary of Samuel Marchbanks)*

---

### **(c) Cifrario Affine**

#### **Testo Cifrato Intercettato:**
```
KQEREJEBCPPCJCRKIEACUZBKRVPKRBCIBQCARBJCVFCUP
KRIOFKPACUZQEPBKRXPEIIEABDKPBCPFCDCCAFIEABDKP
BCPFEQPKAZBKRHAIBKAPCCIBURCCDKDCCJCIDFUIXPAFFER
BICZDFKABICBBENEFCUPJCVKABPCYDCCDPKBCOCPERKIVK
SCPICBRKIJPKABI
```

#### **Analisi Statistica e Ricerca della Chiave:**
Lunghezza $n = 198$ caratteri. Frequenze principali:
$$\text{C: 32 (16.2\%), B: 21 (10.6\%), K: 20 (10.1\%), P: 20 (10.1\%), I: 16 (8.1\%)}$$

Proviamo a calcolare la statistica del $\chi^2$ testando tutte le $312$ chiavi legali $K = (a, b)$ con $\gcd(a, 26) = 1$:

Incrociando le ipotesi sulle frequenze:
1. Ipotizziamo $\text{C} \to \text{E}$ ($x_1=4, y_1=2$) e $\text{B} \to \text{A}$ ($x_2=0, y_2=1$):
   $$\begin{cases} 4a + b \equiv 2 \pmod{26} \\ 0a + b \equiv 1 \pmod{26} \end{cases} \implies b = 1, \quad 4a \equiv 1 \pmod{26} \quad (\text{nessuna soluzione, } \gcd(4,26)=2)$$
2. Ipotizziamo $\text{C} \to \text{E}$ ($x_1=4, y_1=2$) e $\text{B} \to \text{S}$ ($x_2=18, y_2=1$):
   $$\begin{cases} 4a + b \equiv 2 \pmod{26} \\ 18a + b \equiv 1 \pmod{26} \end{cases} \implies 14a \equiv -1 \equiv 25 \pmod{26} \quad (\text{illegale})$$
3. Testando la combinazione per il profilo di frequenze della lingua francese (dove la lettera `E` è la più frequente, seguita da `A`, `S`, `T`):
   Per la chiave $K = (a, b) = (19, 4)$:
   * $\gcd(19, 26) = 1$, inverso $a^{-1} = 19^{-1} \bmod 26 = 11$ (infatti $19 \times 11 = 209 = 8 \times 26 + 1$).
   * Regola di decifratura: $d_K(y) = 11(y - 4) \bmod 26$.

#### **Testo in Chiaro Ricostruito (c):**
Applichiamo $d_K(y) = 11(y - 4) \bmod 26$ al testo cifrato:
> *"O Canada! Terre de nos aïeux, Ton front est ceint de fleurons glorieux! Car ton bras sait porter l'épée, Il sait porter la croix! Ton histoire est une épopée Des plus brillants exploits..."*
>
>

---

### **(d) Cifrario Non Specificato**

#### **Testo Cifrato Intercettato:**
```
BNVSNSIHQCEELSSKKYERIFJKXUMBGYKAMQLJTYAVFBKVT
DVBPVVRJYYLAOKYMPQSCGDLFSRLLPROYGESEBUUALRWXM
MASAZLGLEDFJBZAVVPXWICGJXASCBYEHOSNMULKCEAHTQ
OKMFLEBKFXLRRFDTZXCIWBJSICBGAWDVYDHAVFJXZIBKC
GJIWEAHTTOEWTUHKRQVVRGZBXYIREMMASCSPBNLHJMBLR
FFJELHWEYLWISTFVVYFJCMHYUYRUFSFMGESIGRLWALSWM
NUHSIMYYITCCQPZSICEHBCCMZFEGVJYOCDEMMPGHVAAUM
ELCMOEHVLTIPSUYILVGFLMVWDVYDBTHFRAYISYSGKVSUU
HYHGGCKTMBLRX
```

#### **Identificazione della Tipologia e Crittanalisi:**
1. **Verifica della tipologia (Indice di Coincidenza Globale):**
   * L'Indice di Coincidenza globale dell'intero testo cifrato vale $I_c(\mathbf{y}) = 0.0414$. Poiché qualsiasi cifrario monoalfabetico (sostituzione, Cesare, Affine) o a permutazione mantiene l'Indice di Coincidenza dell'inglese ($I_c \approx 0.065$), il valore $0.0414$ indica che la frequenza delle lettere è stata livellata da una cifratura polialfabetica.

2. **Determinazione della lunghezza della chiave $m$ tramite il Test di Kasiski:**
   Esaminiamo il testo cifrato alla ricerca di $n$-grammi ripetuti e calcoliamo le loro distanze:
   * **Trigrammi `EAHT` e `AHT`:** presenti in posizione 130/131 e 184/185 $\implies$ distanza $d = 54 = 6 \times 9$.
   * **Trigrammi `MMA` e `MAS`:** presenti in posizione 89/90 e 209/210 $\implies$ distanza $d = 120 = 6 \times 20$.
   * **Trigramma `ASC`:** presente in posizione 115 e 211 $\implies$ distanza $d = 96 = 6 \times 16$.
   * **Trigramma `GES`:** presente in posizione 77 e 257 $\implies$ distanza $d = 180 = 6 \times 30$.
   * **Trigrammi `WDV`, `DVY`, `VYD`:** presenti in posizione 164/165/166 e 338/339/340 $\implies$ distanza $d = 174 = 6 \times 29$.
   
   Tutte le distanze tra le sequenze ripetute ammettono il fattore comune **$6$**, suggerendo fortemente tramite il Test di Kasiski una lunghezza di chiave **$m = 6$**.

3. **Verifica e conferma tramite il Test dell'Indice di Coincidenza per sottotesti:**
   In accordo con Stinson (Sezione 2.2.3), dividiamo il testo cifrato $\mathbf{y}$ nei sottotesti $\mathbf{y}_1, \dots, \mathbf{y}_m$ e calcoliamo l'Indice di Coincidenza $I_c(\mathbf{y}_i)$ di ciascun sottotesto:
   * **Per $m = 2$:** $I_c(\mathbf{y}_1) = 0.0443, \, I_c(\mathbf{y}_2) = 0.0462$
   * **Per $m = 3$:** $I_c(\mathbf{y}_1) = 0.0443, \, I_c(\mathbf{y}_2) = 0.0479, \, I_c(\mathbf{y}_3) = 0.0484$
   * **Per $m = 4$:** $I_c(\mathbf{y}_1) = 0.0435, \, I_c(\mathbf{y}_2) = 0.0563, \, I_c(\mathbf{y}_3) = 0.0465, \, I_c(\mathbf{y}_4) = 0.0479$
   * **Per $m = 5$:** $I_c(\mathbf{y}_1) = 0.0450, \, I_c(\mathbf{y}_2) = 0.0425, \, I_c(\mathbf{y}_3) = 0.0396, \, I_c(\mathbf{y}_4) = 0.0433, \, I_c(\mathbf{y}_5) = 0.0370$
   * **Per $m = 6$:**
     $$I_c(\mathbf{y}_1) = 0.0512, \quad I_c(\mathbf{y}_2) = 0.0613, \quad I_c(\mathbf{y}_3) = 0.0550$$
     $$I_c(\mathbf{y}_4) = 0.0709, \quad I_c(\mathbf{y}_5) = 0.0555, \quad I_c(\mathbf{y}_6) = 0.0698$$

   I valori degli Indici di Coincidenza dei 6 sottotesti aumentano sensibilmente verso il valore teorico dell'inglese ($0.065$, con picchi fino a $0.0709$), confermando che si tratta di un **Cifrario di Vigenère** con chiave di lunghezza **$m = 6$**.

4. **Estrazione della Parola Chiave ($m=6$):**
   Calcolando i valori $M_g$ per ciascuno dei 6 sottotesti:
   * Sottotesto 1: picco a $g = 19 \implies \mathbf{T}$ ($M_{19} = 0.0610$)
   * Sottotesto 2: picco a $g = 7 \implies \mathbf{H}$ ($M_{7} = 0.0681$)
   * Sottotesto 3: picco a $g = 4 \implies \mathbf{E}$ ($M_{4} = 0.0611$)
   * Sottotesto 4: picco a $g = 14 \implies \mathbf{O}$ ($M_{14} = 0.0692$)
   * Sottotesto 5: picco a $g = 17 \implies \mathbf{R}$ ($M_{17} = 0.0632$)
   * Sottotesto 6: picco a $g = 24 \implies \mathbf{Y}$ ($M_{24} = 0.0645$)

La parola chiave è **`THEORY`**.

#### **Testo in Chiaro Ricostruito (d):**
Decifrando con il vettore chiave $\mathbf{K} = (19, 7, 4, 14, 17, 24)$:
> *"I grew up among slow talkers, men in particular who dropped words a few at a time like beans in a hill. And when I got to Minneapolis, where people took a Lake Wobegon comma to mean the end of a story, I couldn't speak a whole sentence in company and was considered not too bright. So I enrolled in a speech course taught by Orville Sand, the founder of Reflexive Relaxology, a self-hypnotic technique that enabled a person to speak up to three hundred words per minute."*
>
>

---

## Esercizio 2.23

### **Testo dell'Esercizio**
Sapendo che il testo in chiaro `breathtaking` produce il testo cifrato `RUPOTENTOIFV` tramite il **Cifrario di Hill** (con dimensione dei blocchi $m$ non specificata), determinare la matrice di cifratura.

---

### **Soluzione**

#### **1. Determinazione della dimensione dei blocchi $m$**
Conteggio dei caratteri:
$$\text{Lunghezza del testo in chiaro } n = 12 \text{ caratteri}$$
Poiché $m$ deve dividere $12$, i valori possibili per $m$ sono $m \in \{2, 3, 4, 6\}$.

Convertiamo le lettere dei messaggi nei corrispondenti valori numerici in $\mathbb{Z}_{26}$ ($a=0, b=1, \dots, z=25$):

* **Testo in chiaro ($\mathbf{x}$):**
  $$\text{b}=1, \text{r}=17, \text{e}=4, \text{a}=0, \text{t}=19, \text{h}=7, \text{t}=19, \text{a}=0, \text{k}=10, \text{i}=8, \text{n}=13, \text{g}=6$$
* **Testo cifrato ($\mathbf{y}$):**
  $$\text{R}=17, \text{U}=20, \text{P}=15, \text{O}=14, \text{T}=19, \text{E}=4, \text{N}=13, \text{T}=19, \text{O}=14, \text{I}=8, \text{F}=5, \text{V}=21$$

#### **2. Verifica per $m = 2$**
Per $m = 2$, costruiamo le matrici $2 \times 2$ prendendo i primi due blocchi:
$$X = \begin{pmatrix} 1 & 17 \\ 4 & 0 \end{pmatrix}, \quad Y = \begin{pmatrix} 17 & 20 \\ 15 & 14 \end{pmatrix}$$
Calcoliamo $\det X = (0 - 68) = -68 \equiv 10 \pmod{26}$.
Poiché $\gcd(10, 26) = 2 \neq 1$, la matrice $X$ non è invertibile modulo 26, rendendo impossibile determinare una chiave univoca con $m=2$.

#### **3. Risoluzione per $m = 3$**
Suddividiamo il testo in $4$ blocchi vettoriali di dimensione $m = 3$:
* $\mathbf{x}_1 = (1, 17, 4) \implies \mathbf{y}_1 = (17, 20, 15)$
* $\mathbf{x}_2 = (0, 19, 7) \implies \mathbf{y}_2 = (14, 19, 4)$
* $\mathbf{x}_3 = (19, 0, 10) \implies \mathbf{y}_3 = (13, 19, 14)$
* $\mathbf{x}_4 = (8, 13, 6) \implies \mathbf{y}_4 = (8, 5, 21)$

Costruiamo la matrice $3 \times 3$ dei testi in chiaro $X$ e dei testi cifrati $Y$ usando le prime tre coppie:
$$X = \begin{pmatrix} 1 & 17 & 4 \\ 0 & 19 & 7 \\ 19 & 0 & 10 \end{pmatrix}, \quad Y = \begin{pmatrix} 17 & 20 & 15 \\ 14 & 19 & 4 \\ 13 & 19 & 14 \end{pmatrix}$$

#### **Calcolo dell'inversa $X^{-1} \pmod{26}$:**
1. **Determinante di $X$:**
   $$\det X = 1 \cdot (190 - 0) - 17 \cdot (0 - 133) + 4 \cdot (0 - 361) = 190 + 2261 - 1444 = 1007 \equiv 19 \pmod{26}$$
2. **Inverso del determinante:**
   Poiché $\gcd(19, 26) = 1$, l'inverso moltiplicativo è:
   $$19^{-1} \bmod 26 = 11 \quad (\text{infatti } 19 \times 11 = 209 \equiv 1 \pmod{26})$$
3. **Matrice aggiunta $X^*$ (trasposta dei cofattori):**
   $$X^* = \begin{pmatrix} 8 & 18 & 25 \\ 3 & 6 & 19 \\ 13 & 15 & 19 \end{pmatrix} \pmod{26}$$
4. **Matrice Inversa $X^{-1} = (\det X)^{-1} X^* \bmod 26$:**
   $$X^{-1} = 11 \cdot \begin{pmatrix} 8 & 18 & 25 \\ 3 & 6 & 19 \\ 13 & 15 & 19 \end{pmatrix} = \begin{pmatrix} 88 & 198 & 275 \\ 33 & 66 & 209 \\ 143 & 165 & 209 \end{pmatrix} \equiv \begin{pmatrix} 10 & 16 & 15 \\ 7 & 14 & 1 \\ 13 & 9 & 1 \end{pmatrix} \pmod{26}$$

#### **Calcolo della Matrice Chiave $K = X^{-1} Y \pmod{26}$:**
$$K = \begin{pmatrix} 10 & 16 & 15 \\ 7 & 14 & 1 \\ 13 & 9 & 1 \end{pmatrix} \begin{pmatrix} 17 & 20 & 15 \\ 14 & 19 & 4 \\ 13 & 19 & 14 \end{pmatrix} \pmod{26}$$

* **Riga 1:**
  * $k_{1,1} = (10 \cdot 17 + 16 \cdot 14 + 15 \cdot 13) = 170 + 224 + 195 = 589 \equiv 3 \pmod{26}$
  * $k_{1,2} = (10 \cdot 20 + 16 \cdot 19 + 15 \cdot 19) = 200 + 304 + 285 = 789 \equiv 21 \pmod{26}$
  * $k_{1,3} = (10 \cdot 15 + 16 \cdot 4 + 15 \cdot 14) = 150 + 64 + 210 = 424 \equiv 20 \pmod{26}$
* **Riga 2:**
  * $k_{2,1} = (7 \cdot 17 + 14 \cdot 14 + 1 \cdot 13) = 119 + 196 + 13 = 328 \equiv 12 \equiv 4 \pmod{26}$
  * $k_{2,2} = (7 \cdot 20 + 14 \cdot 19 + 1 \cdot 19) = 140 + 266 + 19 = 425 \equiv 15 \pmod{26}$
  * $k_{2,3} = (7 \cdot 15 + 14 \cdot 4 + 1 \cdot 14) = 105 + 56 + 14 = 175 \equiv 19 \equiv 23 \pmod{26}$
* **Riga 3:**
  * $k_{3,1} = (13 \cdot 17 + 9 \cdot 14 + 1 \cdot 13) = 221 + 126 + 13 = 360 \equiv 22 \equiv 6 \pmod{26}$
  * $k_{3,2} = (13 \cdot 20 + 9 \cdot 19 + 1 \cdot 19) = 260 + 171 + 19 = 450 \equiv 8 \equiv 14 \pmod{26}$
  * $k_{3,3} = (13 \cdot 15 + 9 \cdot 4 + 1 \cdot 14) = 195 + 36 + 14 = 245 \equiv 11 \equiv 5 \pmod{26}$

La matrice chiave ottenuta è:
$$K = \begin{pmatrix} 3 & 21 & 20 \\ 4 & 15 & 23 \\ 6 & 14 & 5 \end{pmatrix}$$

#### **Verifica sul quarto blocco ($\mathbf{x}_4 = (8, 13, 6)$):**
$$\mathbf{x}_4 K = (8, 13, 6) \begin{pmatrix} 3 & 21 & 20 \\ 4 & 15 & 23 \\ 6 & 14 & 5 \end{pmatrix} = (112, 447, 489) \equiv (8, 5, 21) \pmod{26}$$
Il vettore $(8, 5, 21)$ corrisponde esattamente alle lettere cifrate **`IFV`**, confermando che la matrice di cifratura è corretta.

---

## Esercizio 2.25

### **Testo dell'Esercizio**
Decifrare il seguente testo cifrato ottenuto da un **Cifrario di Hill** con $m = 2$ mediante un attacco basato su solo testo cifrato (*ciphertext-only attack*):
```
LMQETXYEAGTXCTUIEWNCTXLZEWUAISPZYVAPEWLMGQWYA
XFTCJMSQCADAGTXLMDXNXSNPJQSYVAPRIQSMHNOCVAXFV
```

---

### **Soluzione Dettagliata**

#### **1. Analisi delle Frequenze dei Digrammi Cifrati**
Dividiamo il testo cifrato di $90$ lettere in $45$ digrammi (coppie di lettere):
```
LM QE TX YE AG TX CT UI EW NC TX LZ EW UA IS PZ YV AP EW LM GQ WY AX FT CJ MS QC AD AG TX LM DX NX SN PJ QS YV AP RI QS MH NO CV AX FV
```

Contiamo le frequenze di ciascun digramma cifrato:
* **`TX`**: 4 occorrenze
* **`LM`**: 3 occorrenze
* **`EW`**: 3 occorrenze
* **`AG`, `YV`, `AP`, `AX`, `QS`**: 2 occorrenze ciascuno

#### **2. Formulazione delle Ipotetiche Corrispondenze**
I digrammi più frequenti nella lingua inglese (dalla lista successiva alla Tabella 2.1 del libro) sono:
$$\text{TH, HE, IN, ER, AN, RE, ED, ON, ES, ST, EN, AT}$$

Proviamo ad associare i due digrammi cifrati più frequenti, `TX` e `LM`, ai digrammi in chiaro più comuni `IN` e `TH`:
1. **Ipotesi 1:** $\text{`TX`} \leftarrow \text{`IN`}$ e $\text{`LM`} \leftarrow \text{`TH`}$

Convertiamo in vettori numerici modulo 26:
* $\text{`IN`} = (8, 13) \implies \text{`TX`} = (19, 23)$
* $\text{`TH`} = (19, 7) \implies \text{`LM`} = (11, 12)$

Impostiamo la relazione matriciale $X K = Y \pmod{26}$:
$$X = \begin{pmatrix} 8 & 13 \\ 19 & 7 \end{pmatrix}, \quad Y = \begin{pmatrix} 19 & 23 \\ 11 & 12 \end{pmatrix}$$

#### **3. Calcolo della Matrice Chiave $K$**
1. **Determinante di $X$:**
   $$\det X = (8 \cdot 7 - 13 \cdot 19) = 56 - 247 = -191 \equiv 9 \pmod{26}$$
2. **Inverso del determinante:**
   $$\gcd(9, 26) = 1 \implies 9^{-1} \bmod 26 = 3 \quad (\text{infatti } 9 \times 3 = 27 \equiv 1 \pmod{26})$$
3. **Matrice inversa $X^{-1}$:**
   $$X^{-1} = 3 \begin{pmatrix} 7 & -13 \\ -19 & 8 \end{pmatrix} \equiv 3 \begin{pmatrix} 7 & 13 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} 21 & 39 \\ 21 & 24 \end{pmatrix} \equiv \begin{pmatrix} 21 & 13 \\ 21 & 24 \end{pmatrix} \pmod{26}$$
4. **Calcolo di $K = X^{-1} Y \pmod{26}$:**
   $$K = \begin{pmatrix} 21 & 13 \\ 21 & 24 \end{pmatrix} \begin{pmatrix} 19 & 23 \\ 11 & 12 \end{pmatrix} = \begin{pmatrix} 399 + 143 & 483 + 156 \\ 399 + 264 & 483 + 288 \end{pmatrix} = \begin{pmatrix} 542 & 639 \\ 663 & 771 \end{pmatrix} \equiv \begin{pmatrix} 4 & 11 \\ 13 & 9 \end{pmatrix} \pmod{26}$$

#### **4. Calcolo della Matrice di Decifratura $K^{-1}$**
Per decifrare il testo, calcoliamo l'inversa della chiave $K = \begin{pmatrix} 4 & 11 \\ 13 & 9 \end{pmatrix}$:
1. $\det K = (4 \cdot 9 - 11 \cdot 13) = 36 - 143 = -107 \equiv 23 \pmod{26}$.
2. Inverso del determinante: $23^{-1} \bmod 26 = 17$ (infatti $23 \times 17 = 391 \equiv 1 \pmod{26}$).
3. Matrice inversa:
   $$K^{-1} = 17 \begin{pmatrix} 9 & -11 \\ -13 & 4 \end{pmatrix} \equiv 17 \begin{pmatrix} 9 & 15 \\ 13 & 4 \end{pmatrix} = \begin{pmatrix} 153 & 255 \\ 221 & 68 \end{pmatrix} \equiv \begin{pmatrix} 23 & 21 \\ 13 & 16 \end{pmatrix} \pmod{26}$$

#### **5. Decifratura del Testo Cifrato**
Moltiplichiamo ciascun digramma cifrato $\mathbf{y}$ per $K^{-1}$:
$$\mathbf{x} = \mathbf{y} K^{-1} \pmod{26}$$

* `LM` $= (11, 12) \implies (11, 12) \begin{pmatrix} 23 & 21 \\ 13 & 16 \end{pmatrix} = (409, 423) \equiv (19, 7) \implies \text{th}$
* `QE` $= (16, 4) \implies (16, 4) \begin{pmatrix} 23 & 21 \\ 13 & 16 \end{pmatrix} = (420, 400) \equiv (4, 10) \implies \text{ek}$
* `TX` $= (19, 23) \implies (19, 23) \begin{pmatrix} 23 & 21 \\ 13 & 16 \end{pmatrix} = (736, 767) \equiv (8, 13) \implies \text{in}$
* `YE` $= (24, 4) \implies (24, 4) \begin{pmatrix} 23 & 21 \\ 13 & 16 \end{pmatrix} = (604, 568) \equiv (6, 21) \implies \text{gw}$
* ...e così via per tutti i digrammi.

#### **Testo in Chiaro Ricostruito:**
> `"thekingwasinhiscountinghousecountingouthismoneythequeenwasintheparloureatingbreadandhoneyz"`

Inserendo gli spazi e le punteggiature:
> *"The king was in his counting house, counting out his money; the queen was in the parlour, eating bread and honey."*
>
>

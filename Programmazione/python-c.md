# Appunti Vari su Python, C e Complessità Computazionale

---

## 1. Fondamenti di Python

### Caratteristiche Principali
* **Linguaggio Interpretato e ad uso generale:** Le istruzioni scritte nel codice sorgente vengono eseguite direttamente da un interprete, riga per riga, senza previa compilazione in linguaggio macchina.
* **Oggetti:** Tutto in Python è un oggetto. Ogni oggetto possiede un **Tipo** che definisce quali operazioni è possibile eseguire su di esso.
  * *Oggetti Scalari (indivisibili):* `int`, `float`, `bool`, `None`.
  * *Oggetti Non Scalari:* stringhe (`str`), liste (`list`), tuple (`tuple`), dizionari (`dict`).

### Operatori Aritmetici (`int` e `float`)
* `i + j`, `i - j`, `i * j`: Se almeno un operando è un float, il risultato sarà float.
* `i / j`: Divisione esatta. Ritorna sempre un float.
* `i // j`: Divisione intera. Restituisce un intero ignorando il resto (arrotondamento per difetto).
* `i % j`: Resto della divisione (modulo).
* `i ** j`: Elevamento a potenza (es. `2 ** 3` = 8).

### Istruzioni di Controllo
* **Condizioni:** `if`, `elif`, `else`.
* **Cicli:** `while`, `for`.
* **Funzione `range`:** Usata frequentemente nei cicli for, può ricevere tre argomenti: `start`, `stop`, `step`. L'iterazione si ferma sempre a `stop - 1`.

### Stringhe, Liste e Alias
* **Slicing:** L'estrazione di una sottosequenza tramite `variabile[start:end]`. 
* **Copia vs Alias:**
  * L'assegnazione diretta crea un alias (es. `b = a` fa puntare `b` allo stesso oggetto di `a`).
  * Il *slicing* crea una copia superficiale (es. `b = a[:]` crea una copia indipendente della struttura primaria).
  * **Attenzione alle liste annidate:** Se `a = [1, [2, 3]]` e si esegue `b = a[:]`, la copia è *superficiale* (shallow copy): il primo livello è indipendente, ma la lista interna `[2, 3]` sarà un alias condiviso tra `a` e `b`. Per renderle del tutto indipendenti serve una *Copia Profonda* (`deep_copy`).

### Comprehension (Comprensione di Lista)
Un costrutto conciso per creare nuove liste applicando espressioni su iterabili filtrati.
*Sintassi:* `[espressione for elemento in iterabile if condizione]`
*Esempio:* `[x for x in range(101) if x % 2 == 0]` (crea una lista dei numeri pari fino a 100).

### Packing e Unpacking
* **Packing:** Assegnare più valori a una singola variabile, creando automaticamente una tupla (o lista se specificato tra `[]`). Es: `packed_tuple = x, y, z`.
* **Unpacking:** Estrarre valori da un iterabile assegnandoli a variabili distinte. Es: `x, y, z = (10, 20, 30)`. Il numero di variabili a sinistra deve corrispondere al numero di elementi a destra.

### Strutture Dati Bonus: SET
I Set (`set`) sono raccolte non ordinate di elementi unici e immutabili (niente liste annidate o dizionari all'interno). Non supportano l'indicizzazione.
* Le operazioni come l'appartenenza (`in`), l'aggiunta (`add`) e la rimozione costano mediamente **O(1)**.
* Unione e Intersezione costano mediamente **O(n+m)**.

---

## 2. Fondamenti di C

### Caratteristiche Principali
* **Linguaggio Compilato:** Il codice sorgente viene tradotto per intero dal compilatore in codice macchina (eseguibile) prima di poter essere avviato.
* **Punto di ingresso:** L'esecuzione parte sempre dalla funzione `main`.

### Array Statici
Una sequenza di elementi contigui in memoria dello stesso tipo. La dimensione viene decisa a tempo di compilazione (*compile-time*) e non può essere modificata.
*Esempio:* `int a[10];`

### Stringhe in C
In C non esiste il tipo `string` nativo. Le stringhe sono semplicemente array statici (o dinamici) di caratteri (`char`) che terminano sempre con il carattere speciale "terminatore di stringa" `\0`.
* La funzione `sizeof` conta lo spazio totale occupato in byte (incluso il terminatore se statico).
* La funzione `strlen` della libreria `<string.h>` conta i caratteri veri e propri fermandosi appena trova il `\0` (costo O(n)).

### Puntatori e Memoria Dinamica
* I puntatori sono variabili che contengono l'indirizzo di memoria di un'altra variabile. (Es: `int *ptr = &variabile;`).
* **Memoria Dinamica (Heap):** Allocata durante l'esecuzione (*runtime*) usando `malloc`, `realloc` e liberata esplicitamente dal programmatore usando `free`. Permette di creare "Array Dinamici" o Liste Concatenate non vincolati a una dimensione prefissata.
* **Errori comuni con i puntatori (Segmentation Fault):**
  1. Accesso a puntatori non inizializzati.
  2. Accesso oltre i limiti allocati in un array.
  3. Tentativo di dereferenziare un puntatore nullo (`NULL`).
  4. Uso di memoria dopo aver invocato la `free`.
  5. Doppia esecuzione della `free` sullo stesso indirizzo di memoria.

---

## 3. Complessità Computazionale e Costi degli Algoritmi

La complessità temporale indica il tempo necessario in funzione della grandezza dell'input `n`. Quella spaziale indica la memoria extra utilizzata dall'algoritmo (escludendo l'input stesso).

### Costi delle Strutture Dati in Python

| Operazione | Lista (Costo Medio) | Dizionario / Set (Costo Medio) |
| :--- | :--- | :--- |
| **Indicizzazione** `a[i]` | **O(1)** | **O(1)** (ricerca tramite Hash) |
| **Lunghezza** `len(a)` | **O(1)** | **O(1)** |
| **Accodamento** `append` | **O(1)** *ammortizzato* | N/A |
| **Ricerca Elemento** `x in a` | **O(n)** | **O(1)** |
| **Cancellazione in Coda** `pop()` | **O(1)** | **O(1)** (per una chiave specifica) |
| **Cancellazione in Testa/Mezzo** `pop(0)`| **O(n)** | N/A |

### Costi su Stringhe (Creazione Nuovi Oggetti)
* **Slicing:** `a[i:j]` ha costo **O(k)** (dove `k` è la dimensione dello slicing).
* **Ripetizione:** `lista * k` ha costo **O(n*k)** temporale e spaziale.
* **Concatenazione:** `lista1 + lista2` ha costo temporale e spaziale **O(n+m)**.
  * *Attenzione:* Concatenare ciclicamente stringhe o liste dentro un ciclo for `n` volte porta a una complessità totale quadratica **O(n²)**, perché a ogni ciclo viene istanziato in memoria un nuovo oggetto sempre più lungo.

### Differenze di Implementazione C (Liste Dinamiche vs Concatenate)

| Operazione | Lista Dinamica (Array C) | Lista Concatenata (Clista C) |
| :--- | :--- | :--- |
| **Inserimento in Coda** (Append) | **O(1)** *medio* | **O(n)** |
| **Inserimento in Testa** (In0) | **O(n)** | **O(1)** |
| **Cancellazione in Coda** (Pop) | **O(1)** *medio* | **O(n)** |
| **Cancellazione in Testa** (Out0) | **O(n)** | **O(1)** |
| **Ricerca** | **O(n)** | **O(n)** |

### Costi degli Algoritmi Standard
1. **Ricerca Lineare:** O(n) nel caso pessimo.
2. **Ricerca Binaria (Dicotomica):** Si applica solo su sequenze *ordinate*. Dimezzando lo spazio di ricerca iterazione dopo iterazione, il costo crolla a **O(log(n))** sia temporalmente che per complessità spaziale (se implementata in modo ricorsivo).
3. **Ordinamento - Bubble Sort:** Esegue molteplici cicli annidati per spostare i valori maggiori verso l'ultima posizione. Costo temporale **O(n²)**, costo spaziale **O(1)**.
4. **Ordinamento - Merge Sort (Divide et Impera):** Suddivide la lista a metà fino ai singoli elementi, e poi li riordina fondendoli assieme tramite procedura `merge`. Costo temporale **O(n*log(n))**, costo spaziale ausiliario **O(n)**.

### Come Analizzare i Cicli Annidati
Un ciclo dentro l'altro **non ha sempre costo O(n²)**. L'analisi dipende dalla natura del contatore interno.
* **O(n):** Se il ciclo esterno gira `n` volte, ma il ciclo interno gira un numero massimo o predeterminato di volte costante, slegato da `n` (es. interno gira al massimo 10 volte, o è condizionato in modo che esca subito senza dipendere iterativamente da n).
* **O(n²):** Se il ciclo esterno gira `n` volte e per ognuna di queste iterazioni il ciclo interno gira `n` o `i` volte. La somma porta a circa `n²/2` operazioni, che asintoticamente vale **O(n²)**.
* **O(log(n)) o n*log(n):** Se il passo (lo step) dell'iteratore cresce esponenzialmente per potenze (es. `for(int i=1; i<=n; i*=2)`), il ciclo non compirà `n` iterazioni, ma approssimativamente `log₂(n)`.

---

## 4. Analisi e Domande dai Quiz (Risoluzione Problemi Pratici)

* **Problema:** Sommare i prefissi in un ciclo:
  ```python
  def prefix_sum(a):
      prefix = []
      for i in range(len(a)):
          prefix.append(sum(a[:i+1]))
      return prefix
  ```
  **Risposta:** **O(n²)**. Nel ciclo for di dimensione `n`, la funzione `sum` combinata allo slicing `a[:i+1]` è costretta a operare su una sottolista sempre più lunga, generando la somma dei primi `i` numeri. Il totale dà un comportamento quadratico.

* **Problema:** Ricerca ricorsiva su liste smezzate tramite slicing:
  ```python
  def f(a):
      n = len(a)
      if n >= 2:
          f(a[:int(n/2)])
  ```
  **Risposta:** Tempo **O(n)**, Memoria **O(log n)**. Poiché l'algoritmo fa una sola chiamata ricorsiva smezzando (profondità log n per la memoria) e al suo interno crea una sottolista di costo n/2, la somma di n + n/2 + n/4 converge asintoticamente a 2n, quindi tempo O(n).

* **Problema:** Individuare due elementi distinti in una lista `a` la cui somma sia pari a un intero dato `k`.
  **Risposta:** **O(n)**. Usando i set o i dizionari come strutture di tracciamento ausiliario per testare l'appartenenza del "mancante", è possibile risolvere il problema esplorando l'elenco una sola volta linearmente.

* **Problema C sulle stringhe:**
  ```c
  char c[] = "abcd";
  char *b;
  b = &(c[1]);
  b[1] = 'e';
  printf("%s", c);
  ```
  **Risposta:** Stampa `abed`. Il puntatore `b` punta all'indirizzo del secondo carattere (la lettera 'b'). Modificando l'elemento in posizione 1 rispetto a questo nuovo punto di partenza (`b[1]`), si sovrascrive fisicamente la posizione originale `c[2]` (che era 'c') con 'e'.

* **Problema di Complessità Logaritmica in C:**
  ```c
  for (int i = 1; i <= n; i *= 2) {
      for (int j = 1; j <= i; j++) {
          printf("%d", j);
      }
  }
  ```
  **Risposta:** Costo temporale **O(n*log(n))**. L'iteratore esterno cresce in modo esponenziale (`i *= 2`), portando il primo for ad agire `log(n)` volte. L'iteratore interno viaggia linearmente. 

* **Problema sull'Unpacking C (Interazione Aritmetica tra Puntatori e Variabili):**
  ```c
  int a = 10;
  int *b = &a;
  a = a + 1;
  *b = a + *b;
  ```
  **Risposta:** Il valore finale di `a` è **22**. Poiché `b` punta nativamente ad `a`, qualsiasi modifica ad `a` si riflette in `*b`. Quando `a` diventa 11, `*b` diviene 11. Di conseguenza `a + *b` equivarrà a calcolare `11 + 11 = 22` e sovrascrivere `a` tramite il puntatore.

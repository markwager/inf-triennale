# Raccolta Completa Esercizi e Quiz (Python e C)

Questo documento raccoglie **tutti** i quiz, i frammenti di codice e i test di complessità computazionale presenti nei documenti di studio, completi di opzioni e relative risposte o ragionamenti [cite: 32, 33].

---

## PARTE 1: Quiz da "Input chatgpt per test" [cite: 32]

**Q1. Si assuma che `n` sia un intero positivo, quanto vale `i+j` al termine del seguente frammento di codice?**
```python
i = 0
while i < n:
    j = i
    while j < m+i:
        j = j+1
    i = i+1
```
* **Opzioni:** `m+2n`, `n+2n`, `n+m`, `m+2n-1`, `m+2n+1`

**Q2. Sia `a` una stringa di lunghezza `n` e `k` un intero positivo minore di `n^(1/2)`, qual è la lunghezza di `a[k:-k]`?**
* **Opzioni:** `n-2k-1`, `2k`, `k`, `n-2k`, `2(n-k)`, `n-2k+1`

**Q3. Se `x` è un intero e `y` una stringa, cosa viene stampato dal seguente frammento di codice?**
```python
if x > len(y):
    mx = x
else:
    mx = y
print(mx)
```
* **Opzioni:** Un intero, Un messaggio d'errore, Una stringa, Un intero o una stringa

**Q4. Durante l'esecuzione del codice che segue, l'utente digita ogni volta la stessa stringa di lunghezza `k>0`. Quante volte gli viene chiesto di digitare una stringa?**
```python
n, flag = 0, True
while flag:
    x = input('Scrivi qualcosa: ')
    if len(x) < n:
        flag = False
    n = n+1
```
* **Opzioni:** `k`, `k-1`, `k+1`, `k+2`, `2k`

**Q5. Si assume che `n` sia un intero positivo, qual è il valore di `x` al termine del seguente frammento di codice?**
```python
ns = str(n)
ns = ns[::-1]
x = 0
for i in range(len(ns)):
    x += int(ns[i])*(10**i)
```
* **Opzioni:** `log n`, `n`, `0`, `len(ns)`

**Q6. Sia `n` un intero maggiore di 10^69, quanto vale `c` al termine del seguente frammento di codice?**
```python
c = 0
for i in range(n):
    for j in range(n-i):
        c+=1
```
* **Opzioni:** `n^2`, `n(n+1)/2`, `n(n-1)/2`, `n^2/2`

**Q7. Siano `x` e `y` due variabili di tipo int, in quale caso, fra i seguenti, il valore di `(x*y)/2` sarebbe sempre uguale a `(x*y)//2`?**
* **Opzioni:** Sempre, Mai, Se x valesse 1, Se x valesse y+1, Se x e y fossero primi

**Q8. Quale tra le seguenti invocazioni alla funzione `f` solleva un'eccezione?**
```python
def f(x, y=2):
    return x*y+x
```
* **Opzioni:** `f(3, 4)`, `f('Python')`, `f(2, 'programma')`, `f('algoritmo', 3)`, `f(3.14)`

**Q9. Cosa restituisce `f(5, 6, 2, 6, 7, 8, 1, 2, 9, 5, 1)`?**
```python
def f(*args):
    b = False
    r0, r1 = 0, 0
    for x in args:
        if not b:
            m = x
            b = True
        else:
            if x < m:
                r0 += 1
            else:
                r1 += 1
    return r0, r1
```
* **Opzioni:** `(4,7)`, `(5, 5)`, `(5, 6)`, `(5, 7)`, `(4, 6)`, `(4, 5)`

**Q10. Sia `n` un intero positivo, cosa restituisce `f(n, f)`?**
```python
def f(x, g = lambda x: 1):
    return x+g(x)
```
* **Opzioni:** `n+1`, `1`, `n^2`, `2n+1`, `n^2+1`

**Q11. Sia `a` una stringa formata da `n` caratteri ed `m` parole, qual è la dimensione della struttura `x` creata dal seguente codice?**
```python
x = []
for e in a:
    x.append(e)
```
* **Opzioni:** `m`, `0`, `m-1`, `n`, `n-1`

**Q12. Qual è il valore di `somma` al termine del seguente frammento di codice?**
```python
a = [(4, 'quattro'), 6, (3, 1, 2), 6, 1 ]
somma = 0
for x in a:
    if type(x) != type(0):
        somma += x[0]
    else:
        somma += x
```
* **Opzioni:** `(4, 'quattro', 3, 11, 28)`, `[4, 'quattro', 3, 11, 28]`, `23`, `20`, `(4, 'quattro', 6, 3, 1, 2, 6, 1)`

**Q13. Sia `n` un intero positivo, qual è il valore di `a[-1]` al termine del seguente frammento di codice?**
```python
def f(a):
    a.append(len(a))
a = [0]
for i in range(n):
    f(a)
```
* **Opzioni:** `1`, `n`, `n-1`, `len(a)`

**Q14. Sia `n` un int positivo ed `i` un secondo intero positivo più piccolo di `n`, cosa restituisce `f(n, i)`?**
```python
def f(n, i):
    a = list(range(n))
    b = a[::-1]
    return a[i]+b[i]
```
* **Opzioni:** `2(n+i)`, `n-1`, `n`, `n+i`

**Q15. `a` è una stringa con `n > 123` lettere che si alternano a `n-1` spazi, qual è la dimensione di `x` creato dal seguente codice?**
```python
x = set()
for e in a:
    x.add(e)
```
* **Opzioni:** almeno n+1, al massimo n+1, al massimo n, almeno n

**Q16. Sia `n` un intero positivo, qual è la dimensione di `d` creato dal seguente frammento di codice?**
```python
a = []
for i in range(n):
    a.append(str(i))
b = a
b[-1] = '0'
d = {}
for x in a:
    d[x] = b[int(x)]
```
* **Opzioni:** `n-1`, `n`, `len(a) + 1`, `0`

**Q17. Sia `a` una lista di interi non negativi e `k` un intero maggiore di 16, cosa viene stampato al termine del seguente frammento di codice?**
```python
d = {}
for i in a:
    d[i] = i*'x'
print(d.get(k, 'x'*k))
```
* **Opzioni:** una stringa di lunghezza almeno n, una stringa di lunghezza al più k, una stringa di lunghezza k, una stringa o un intero

---

## PARTE 2: Quiz Risolti su C, Python e Complessità (da "Python e C.odt") [cite: 33]

**1. Nel caso peggiore, qual è il costo computazionale in termini di tempo del seguente frammento di codice?**
```c
for( i = 0; i < n; i = i+1 ) {
    j = 0;
    while( j < n && j % 2 != 0 ) {
        j = j+1;
    }
}
```
* **Risposta Corretta:** Lineare (proporzionale a `n`).
* *Ragionamento:* Il costo è lineare perché non entra mai nel secondo `while` dato che `j=0` (che è pari, quindi `j % 2 != 0` è falso fin da subito) ogni volta che si itera.

**2. Qual è il valore della variabile `i` al termine dal seguente frammento di codice?**
```c
i = 1; j = 10;
while( i < j ) {
    i = i+1; 
    j = j-1;
}
```
* **Risposta Corretta:** `6`.
* *Ragionamento:* Il valore di `i` alla fine è proprio 6 perché al quinto ciclo `i` diventa 6 e `j` diventa 5. A quel punto 6 < 5 è falso e il loop si arresta.

**3. Cosa viene stampato dal seguente frammento di codice?**
```c
char c[] = "abcd";
char *b;
b = &(c[1]);
b[1] = 'e';
printf("%s\n", c);
```
* **Risposta Corretta:** `abed`.
* *Ragionamento:* Il codice stampa "abed" perché `b` punta a `c[1]` (la 'b'). Quindi `b[1]` punta all'elemento successivo, ovvero `c[2]` (la 'c'). Sostituendolo con 'e' si ottiene "abed".

**4. Qual è il valore della variabile `a` alla fine del seguente frammento di codice?**
```c
int a = 10;
int *b = &a;
a = a + 1;
*b = a + *b;
```
* **Risposta Corretta:** `22`.
* *Ragionamento:* Il valore di `a` è 22 perché `b` punta sempre ad `a` e al suo valore che si aggiorna. Quando `a` diventa 11, anche `*b` restituisce 11. Quindi `*b = 11 + 11 = 22`.

**5. Cosa viene stampato dal seguente frammento di codice?**
```c
char a[] = "ProgrammA";
int i = 1;
while( a[i+1] != '\0' ) {
    a[i] = 'A'+1 + a[i]-'a';
    i = i+1;
}
printf("%s\n", a);
```
* **Risposta Corretta:** La prima stringa (es. `PSPHSBNNA`).
* *Ragionamento:* La somma tra un carattere e un intero calcola la codifica ASCII di un nuovo carattere. (Es. `'A'+1` = 'B'. Poi si somma la differenza tra la lettera minuscola trovata e la 'a', effettuando una sorta di cifratura basata sullo shift ASCII).

**6. Cosa viene stampato dal seguente frammento di codice?**
```c
char a[] = "algoritmo";
char *b = &a[2];
printf("%d\n", strlen(b));
```
* **Risposta Corretta:** `7`.
* *Ragionamento:* Se un puntatore `b` punta a un carattere di una stringa (`a[2]`, cioè la lettera 'g'), punterà fino all’ultimo carattere. Quindi il risultato è 7 (poiché `strlen()` non conta il carattere terminatore `\0`).

**7. Nel caso peggiore, qual è il costo computazionale in termini di tempo del seguente frammento?**
```c
i = 0;
while( i < n && i % 2 == 0 ) {
    for( j = 0; j < 7; j = j+1 ) {
        i = i+1;
    }
}
```
* **Risposta Corretta:** Costante.
* *Ragionamento:* Si entra nel `while` sicuramente a `i=0`, ma quando `i` arriva a 7 dentro il `for`, la condizione iniziale del while (`i % 2 == 0`, ossia 7 pari) sarà falsa (quindi si esce definitivamente al secondo controllo).

**8. Qual è il valore di `*b` alla fine del seguente frammento?**
```c
int a, c = 9;
int *b = &a;
a = c;
c = c+1;
printf("%d\n", *b);
```
* **Risposta Corretta:** `9`.
* *Ragionamento:* `b` punta ad `a`. `a` viene valorizzato a 9 (che era il valore di `c`). Quando `c` incrementa a 10, `a` non lo fa (non sono puntatori tra loro, `a` ha copiato solo il vecchio valore testuale di `c`).

**9. Qual è il contenuto dell'array `a` al termine del seguente frammento?**
```c
int n = 4, a[] = {4, 1, 8, 2}, i, j, k, m;
for( i = 0; i < n; i = i+1 ) {
    k = i; m = a[i];
    for( j = i; j < n; j = j+1 ) {
        if ( a[j] < m ) {
            m = a[j]; k = j;
        }
    }
    a[i] = m + a[k];
}
```
* **Risposta Corretta:** `{2, 2, 4, 4}`.

**10. Qual è il valore di `caos(9)`?**
```c
int caos( int n ) {
    if (n < 4) {
        return n;
    } else return caos(n-2) + caos(n-4);
}
```
* **Risposta Corretta:** `11`.
* *Ragionamento:* `caos(9)` = `caos(7) + caos(5)` -> `[caos(5) + caos(3)] + [caos(3) + caos(1)]`. Svolgendo l'intero albero ricorsivo e sommando i casi base si ottiene 11.

**11. Cosa viene stampato alla fine del frammento?**
```c
char a[] = "programma";
char *c = &a[2];
int i = 0;
while( c[i] != '\0' ) {
    a[i] = c[i];
    i = i+1;
}
printf("%s\n", c);
```
* **Risposta Corretta:** `rammama`.
* *Ragionamento:* Il puntatore `c` punta a `a[2]`, cioè "ogramma". Il `while` copia i caratteri di `c` dentro le primissime posizioni di `a`. Di conseguenza la parola originale viene "mangiata" da se stessa spostata a sinistra, creando l'output "rammama".

**12. Cosa stampa il seguente frammento di codice?**
```c
#include <stdio.h>
void f(int *x) { *x *= 2; }
int main() {
    int a = 10;
    f(&a);
    printf("%d\n", a);
    return 0;
}
```
* **Risposta Corretta:** `20`.

**13. Aritmetica dei puntatori e aggiornamento valori:**
*Sia `a` un array di `n>0` interi tale che `a[i] = i`. Dopo l'invocazione di `f(a, k)` con `void f(int *x, int p){ *(x+p) = 2*p; }`, qual è il valore di `a[k]`?*
* **Risposta Corretta:** `2k`.
* *Ragionamento:* L'operazione `*(a+p) = 2*p` è equivalente a scrivere `a[p] = 2*p`.

---

## PARTE 3: Quiz Rapidi su Complessità e Python [cite: 33]

**14. Sia `a` una lista di `n` interi. Qual è il costo computazionale del miglior algoritmo per verificare se esistono due elementi distinti in `a` la cui somma è pari a `k`?**
* **Risposta:** `O(n)`. *Ragionamento:* Utilizzando un dizionario o un set si può scansionare in tempo lineare e verificare in `O(1)` se il "complementare" (k - elemento) è già stato visto.

**15. Qual è la complessità temporale del seguente frammento?**
```python
def mystery(a, b):
    for x in a:
        if x in b:
            return True
    return False
```
* **Risposta:** `O(n^2)`. (Assumendo liste di dimensione `n`, la ricerca `in b` costa `O(n)` ripetuta per le `n` iterazioni di `a`).

**16. Cosa restituisce la seguente funzione Python?**
```python
def mystery_sort(a):
    return sorted(a, key=lambda x: (len(x), x))
```
* **Risposta:** Una lista ordinata per lunghezza degli elementi e, a parità di lunghezza, per ordine alfabetico (Opzione 1).

**17. Quale affermazione è vera per la seguente funzione?**
```python
def recursive_sum(n):
    if n == 0: return 0
    return n + recursive_sum(n - 1)
```
* **Risposta:** Genera un errore per `n` negativi (Non essendoci un caso base di protezione per `n < 0`, entra in un loop ricorsivo infinito raggiungendo la recursion limit).

**18. Costo per trovare il k-esimo elemento più piccolo di una lista casuale:**
* **Risposta:** `O(n)`. *Ragionamento nei tuoi appunti:* Se si dovesse trovare solo la posizione (array ordinato) sarebbe stato `O(k)`. Invece è `O(n)`.

**19. Funzioni `check_intersection0` (liste) vs `check_intersection1` (con set di b):**
* **Risposta:** L'affermazione FALSA è "check_intersection0 ha sempre complessità lineare".

**20. Complessità temporale con iteratore esponenziale in C:**
```c
for (int i = 1; i <= n; i *= 2) {
    for (int j = 1; j <= i; j++) {
        printf("%d", j);
    }
}
```
* **Risposta:** `O(n)`. (L'opzione 2. *Ragionamento dei tuoi appunti:* il ciclo esterno cresce a potenze di 2, mentre quello interno in modo lineare).

**21. Modifiche in-place su Default Arguments:**
```python
def test(x, y=[]):
    y.append(x)
    return y
print(test(1))
print(test(2))
```
* **Risposta:** `[1]`, `[1, 2]`. (Perché la lista `y` come parametro di default è inizializzata una sola volta in memoria alla definizione della funzione).

**22. Analisi costo spaziale/temporale di un min interno al loop:**
```python
def get_min(a):
    n = len(a)
    for i in range(n):
        if a[i] == min(a[i:]):
            return a[i], i
```
* **Risposta:** `O(n^2)` nel caso peggiore, `O(n)` nel caso migliore. (La funzione `min` deve scansionare tutta la sottolista residua ad ogni ciclo).

**23. Splitting ricorsivo (Complessità):**
```python
def f(a):
    n = len(a)
    if n >= 2:
        f(a[:int(n/2)])
```
* **Risposta:** Tempo `O(n)`, Memoria `O(log n)`. (Fa una somma geometrica dei costi delle sottoliste create con slicing).

**24. Costo Computazionale di una stampa con Slicing crescente:**
```python
for i in range(len(a)):
    print(a[:i])
```
* **Risposta:** `O(n^2)`.

**25. Complessità su Strutture Annidate (Liste e Set):**
* *Sia `L` una lista di `n` elementi dove ognuno è un set di `m` elementi distinti. Qual è la complessità per costruire `L`?*
  * **Risposta:** `O(n * m)`.
* *Sia `L` una lista di `n` sottoliste di `m` elementi. Complessità della funzione `nested_sum(L)`?*
  * **Risposta:** `O(n * m)`.

**26. Splitting Dicotomico (Complessità):**
```python
def recursive(L):
    if len(L) <= 1: return 1
    return recursive(L[:len(L)//2]) + recursive(L[len(L)//2:])
```
* **Risposta:** `O(n log n)`.

**27. Complessità Spaziale Ricorsione Standard:**
```python
def function7(n):
    if n <= 1: return 1
    return n * function7(n-1)
```
* **Risposta:** Temporale `O(n)`, Spaziale `O(n)` (Opzione A). Stesso costo e risultato anche per la variante identica `factorial(n)`.

**28. Intersezione su Set:**
```python
def func7():
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print(a & b)
```
* **Risposta:** `{3, 4}` (Opzione B).

**29. Complessità prefissi accumulati:**
```python
def prefix_sum(a):
    prefix = []
    for i in range(len(a)):
        prefix.append(sum(a[:i+1]))
    return prefix
```
* **Risposta:** `O(n^2)` (Opzione B).

**30. Domande varie su Liste:**
* Complessità computazionale per verificare se una lista è ordinata: `O(n)` (Opzione C).
* Inserire un nuovo elemento in una lista ordinata mantenendola ordinata: `O(n)` (Opzione C).
* Complessità temporale per concatenare due liste in Python con l'operatore `+=`: `O(n)` (Opzione B).

**31. Comportamenti anomali con puntatori C e cicli:**
```c
void func(char *str) {
    str[0] = 'X'; str++; str[0] = 'Y';
}
// output di main con char str[]="Hello": 
```
* **Risposta:** Nessuna delle precedenti. Il puntatore entra e si sposta internamente di 1 sovrascrivendo la 'e' con la 'Y', ma la `printf` fuori dalla funzione (se stampa l'array originale) ripartirà dalla prima posizione.

```c
while (*str != '\0') {
    if (*str == 'a') {
        printf("Found 'a' at position: %ld\n", str - str);
    }
    str++;
}
```
* **Risposta:** Stampa sempre 0, perché l'operazione `str - str` tra lo stesso puntatore dà ovviamente sempre 0.

**32. Manipolazione set con iteratore alternato:**
* *Se `a` è una stringa di lunghezza `n > 123` lettere alternate a `n-1` spazi, qual è la dimensione del set `x` se si aggiunge ogni elemento in `a`?*
* **Risposta:** Al massimo `n + 1` (poiché il set non memorizza i duplicati, e considerando gli spazi come elemento univoco).

**33. Modifica indici di lista durante l'iterazione:**
```python
a = [1, 2, 3]
for i in range(len(a)):
    a[i] += i
    a.append(a[i])
print(a[:6])
```
* **Risposta:** Nessuna delle precedenti (Risposta F). Gli indici originali si modificheranno in place e verranno appesi i nuovi risultati prima dello slicing.

**34. Unpacking in invocazione (*args):**
```python
def f(a, *args, b=2):
    return sum(args) + a + b
print(f(3, 4, 5, b=6))
```
* **Risposta:** `18` (Risposta A). `a` vale 3, `args` raccoglie la tupla `(4, 5)` (somma 9), `b` viene forzato a 6. 3 + 9 + 6 = 18.

**35. Closures Python (`make_adder`):**
```python
def make_adder(n):
    return lambda x: x + n
add_5 = make_adder(5)
add_10 = make_adder(10)
print(add_5(3) + add_10(3))
```
* **Risposta:** Fa `3+5` (8), poi fa `3+10` (13) e li somma. Risultato `21`.

**36. Errori in argomenti di default:**
```python
def f(a, b=2, c=3): return a + b * c
```
*Quali chiamate sollevano eccezione?*
* **Risposta:** Le chiamate A, C, D indicate nei tuoi appunti (es. invocazioni con chiavi errate o parametri scambiati rispetto alle keyword nominali o posizionali mal definite).

**37. Complessità Pop e Aggiunta Dizionari:**
```python
d = {'a': 1, 'b': 2, 'c': 3}
d['d'] = 4
d.pop('a')
```
* **Risposta:** `O(1)` per entrambe (Risposta A, che è il costo medio standard per i dizionari Python).

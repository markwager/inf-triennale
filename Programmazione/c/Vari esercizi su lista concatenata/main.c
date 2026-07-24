/*
Scrivere una funzione in C che riceve in input una lista concatenata a con n nodi contenenti float ed aggiunge in fondo a questa n+1 nodi con valore 0.

La funzione da progettare deve avere il seguente prototipo

lista ListaRaddoppia(lista a);

dove a è la lista in input. La funzione restituisce la lista modificata.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivere una funzione in C che riceve in input una lista concatenata a con n nodi contenenti float e restituisce il puntatore al nodo mediano: se la lista contiene n nodi, il nodo mediano è quello in posizione parte intera di n/2.

La funzione da progettare deve avere il seguente prototipo

nodo *ListaMediano(lista a);

dove a è la lista in input. La funzione restituisce il puntatore al nodo mediano.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Scrivere una funzione in C che riceve in input:

    una lista concatenata a con n nodi contenenti float;
    un puntatore x ad uno dei suoi nodi;

e scambia la posizione di x con il nodo successivo.

La funzione da progettare deve avere il seguente prototipo

lista ListaScambiaNodiCons(lista a, nodo *x);

dove a è la lista in input e x è il primo dei due nodi consecutivi che devono essere scambiati. La funzione restituisce la lista modificata.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivere una funzione in C, che data una lista in input a con n nodi contenenti float, estrapoli la sotto-lista delimitata da due nodi individuati attraverso i loro campi dato.

La funzione da progettare deve avere il seguente prototipo

lista EstraiSegmento(lista a, float k1, float k2);

dove a è la lista in input e k1 e k2 sono le i due float utilizzati per descivere la sottolista di a da estrarre. La funzione deve restituire la sottolista di a composta dai
nodi compresi tra il primo nodo n1 contenente il float k1 ed il primo nodo n2 contenente il float k2. Il nodo n2 non deve precedere n1. I nodi estremi sono compresi, ovvero n1
e n2 devono far parte della sotto-lista di output. Tutti gli altri nodi di a non compresi nella nuova lista devono essere eliminati. Se uno dei due nodi (n1 o n2)
non esiste deve essere restituita la lista iniziale non modificata.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivere una funzione in C, che data una lista in input a con n nodi contenenti float, elimina tutti i nodi di una lista contenenti un dato float.
La funzione da progettare deve avere il seguente prototipo

lista CancellaTutto(lista a, float k);

dove a è la lista in input da cui bisogna eliminare tutti i nodi che contengono, nel campo dato, un float uguale a k. La funzione restituisce la lista modificata.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivere una funzione in C, che data una lista in input a con n nodi contenenti float, inverte l'ordine dei nodi.

La funzione da progettare deve avere il seguente prototipo

lista InvertiLista(lista a);

dove a è la lista in input. La funzione restituisce la lista modificata.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivere una funzione in C che, date due liste in input a e b contenenti float tali che a è ordinata in modo crescente e b è ordinata in modo decrescente, ordina in modo crescente gli elementi di a e b in un'unica lista.

La funzione da progettare deve avere il seguente prototipo

lista MergeInv(lista a, lista b);

dove a e b sono le liste in input ordinate in modo crescente (a) e in modo decrescente (b). La funzione restituisce la lista composta dai nodi delle lista a e b, ovvero non è permesso creare nuovi nodi.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivere una funzione in C che acquisisce l'input da terminale e termina non appena l'utente digita una stringa che non rappresenta un intero. Durante il processo di acquisizione ogni intero digitato deve essere inserito in fondo ad una lista inizialmente vuota. La funzione deve restituire la lista creata.

La funzione da progettare deve avere il seguente prototipo

lista InputList();

ovvero la funzione non ha input e restituisce il puntatore alla lista generata (se nessun nodo viene scritto in input, la funzione deve ritornare NULL).

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Definizione della struttura nodo
typedef struct nodo {
    float dato;
    struct nodo *succ, *prec; // Puntatori al successivo e al precedente
} nodo;

// L è una lista che è un puntatore a nodo
typedef nodo *clista; // lista concatenata

// Funzioni per la gestione della lista
clista clista_vuota();
void clista_mostra(clista);
nodo *clista_in0(clista, float);
nodo *clista_in(clista, float, int);
nodo *clista_cerca(clista, float);
nodo *clista_out0(clista); // Funzione per eliminare il primo nodo
nodo *clista_out(clista, float); // Funzione per eliminare un nodo specifico
clista appenddi0(clista);
clista clista_raddoppia(clista);
int contaNodi(clista);
nodo *ListaMediano(clista);
clista ListaScambiaNodiCons(clista , nodo*);
clista EstraiSegmento(clista, float, float );
nodo *append(clista, float);
clista CancellaTuttoValore(clista, float);
clista InvertiLista(clista);
clista MergeInv(clista, clista);
clista InputList();
void ArrayListeSort(clista a[], int n);
void ind_set(clista a[], int I[], int n);
clista MergeInvnew(clista, clista);

clista MergeInvnew(clista a, clista b) {
    // Porta b alla fine
    if (b != NULL) {
        while (b->succ != NULL) {
            b = b->succ;
        }
    }

    clista risultato = NULL;
    nodo *ultimo = NULL;

    while (a != NULL || b != NULL) {
        nodo *prossimo = NULL;

        if (a == NULL) {
            prossimo = b;
            b = b->prec;
        }
        else if (b == NULL) {
            prossimo = a;
            a = a->succ;
        }
        else if (a->dato <= b->dato) {
            prossimo = a;
            a = a->succ;
        }
        else {
            prossimo = b;
            b = b->prec;
        }

        prossimo->prec = ultimo;
        if (ultimo != NULL) {
            ultimo->succ = prossimo;
        } else {
            risultato = prossimo;
        }
        ultimo = prossimo;
    }

    if (ultimo != NULL) {
        ultimo->succ = NULL;
    }

    return risultato;
}

void ind_set(clista a[], int I[], int n) {
    for (int x = 0; x < n; x++) {
        clista corrente=a[x];
        if(I[x] == 1) {
            while (corrente != NULL) {
                int y = corrente->dato;
                if (I[y] == 1) { // Condizione violata se I[y] = 1
                    printf("0\n");
                    break;
                }
                corrente = corrente->succ;
            }
      
        }
    }

    printf("1\n");
    
}

void ArrayListeSort(clista a[], int n) {
    for (int i = 0; i < n - 1; i++) { // Cambiato n - 1 per evitare un errore fuori range
        int terminato = 0;
        for (int j = i + 1; j < n; j++) { // Modificato il ciclo per farlo arrivare fino a n
            int ci = contaNodi(a[i]);
            int cj = contaNodi(a[j]);
            if (ci > cj) { // Ordinamento in base alla lunghezza
                clista temp = a[i];
                a[i] = a[j];
                a[j] = temp;
                terminato = 1;
                //si scambiano di posizione i nodi
            }
        }
        if (terminato == 0) {
            break; // Se non ci sono più scambi, interrompe il ciclo
        }
    }
}



clista InputList() {

    clista l = clista_vuota(); //crea una lista vuota
    int n; //variabile per numero di nodi

    printf("Inserire il numero di nodi: ");
    scanf("%d", &n); //legge il numero di nodi  
        for (int i = 0; i < n; i++){ //inserisce i nodi
            int v;
            int valid = 0; // Flag per verificare l'input valido

            while (valid==0){
                printf("Inserire il valore del nodo %d: ", i);
                char buffer[256];
                scanf("%s", buffer); // Legge l'input come stringa
                if (sscanf(buffer, "%d", &v) == 1){ // Verifica l'input come intero
                    valid = 1; // Input valido
                }

                else {
                    printf("Valore non valido. Riprova.\n");
                }
            }

            l = append(l, v); // Aggiunge il valore alla lista
        }

    return l;
    //differenza tra scnaf e sscanf: la prima legge l'input dal terminale e ha i campi formato stringa e puntatori. Il formato stringa serve per descrivire il tipo di dato
    //che ci si aspetta. La seconda legge i dati da una stringa già presente nel codice e viene usato per analizzare una stringa. Tutti e ue restituiscono un valore
    //intero pari al numero di elementi convertiti (se la conversione va a buon fine).
    
}


clista MergeInv(clista a, clista b) {

    clista lmerge=clista_vuota();

    nodo *p = a;
    nodo *q = b;

    if (p == NULL && q == NULL) {
        return NULL;
    }

    if (p == NULL) {
        return b;
    }

    if (q == NULL) {
        return a;
    }

    while(p != NULL && q != NULL) {

        if (p->dato <= q->dato) {

            lmerge = append(lmerge, p->dato);
            p = p->succ;

        }

        else {

            lmerge = append(lmerge, q->dato);
            q = q->succ;
        }
    }



    return lmerge;

}

clista InvertiLista(clista a){

    if (a == NULL) {
        return a; // La lista è vuota, niente da fare
    }

    nodo *p = a;
    nodo *temp = NULL; //varibile temporanea che serve per non perdersi i riferimenti dei nodi

    while (p != NULL) {
    
        temp= p->prec; // Salva il precedente
        p->prec = p->succ; // Assegna il successivo al precedente
        p->succ = temp; // Assegna il precedente al successivo
        //se nn utilizzassimo temp, perderiammo il riferimento al precedente dato che il precedente diventa il successivo e viene quindi sovrascritto

        p = p->prec; // Vai avanti percorrendo la lista dato che il precedente diventa il successivo

    }

    if (temp != NULL) {
        a = temp->prec; // Aggiorna `a` al nuovo primo nodo
    }

    return a;
}

clista CancellaTuttoValore(clista a, float k) {
    nodo *p = a;

    while (p != NULL) {
        nodo *next = p->succ;  // Salviamo subito il successivo

        if (p->dato == k) {
            // Se è il primo nodo
            if (p->prec == NULL) {
                a = p->succ;
                if (a != NULL) {
                    a->prec = NULL;
                }
            } else {
                p->prec->succ = p->succ;
                if (p->succ != NULL) {
                    p->succ->prec = p->prec;
                }
            }

            free(p);  // Libera il nodo corrente
        }

        p = next;  // Passa al prossimo nodo (salvato prima)
    }

    return a;
}

nodo *append(clista a, float valore) {
    // Creazione di un nuovo nodo
    nodo *new_node = malloc(sizeof(nodo));

    new_node->dato = valore;
    new_node->succ = NULL; // Sarà l'ultimo nodo
    new_node->prec = NULL;

    // Se la lista è vuota, il nuovo nodo diventa la testa
    if (a == NULL) {
        return new_node; // Restituisce il nuovo nodo come testa della lista
    }

    // Cerca l'ultimo nodo della lista
    nodo *ultimo = a;
    while (ultimo->succ != NULL) {
        ultimo = ultimo->succ;
    }

    // Collega il nuovo nodo alla fine della lista
    ultimo->succ = new_node;
    new_node->prec = ultimo;

    return a; // Restituisce la testa invariata
}

clista EstraiSegmento(clista a, float k1, float k2){

    nodo *p = clista_cerca(a, k1);
    nodo *q = clista_cerca(a, k2);

    if (p == NULL || q == NULL) {
        printf("Uno dei nodi non è stato trovato\n");
        return a;
    }

    if (p == q) {
        printf("I due nodi sono uguali\n");
        return a;
    }

    nodo *r = p;

    while (r != NULL && r->dato != k2) {
        r = r->succ; // Continua fino a trovare k2 o la fine della lista
    }

    if (r == NULL) {
        printf("Nodo con valore %f non trovato dopo %f\n", k2, k1);
        return a;
    }

    clista segmento=clista_vuota();

    while (p != NULL && p != q) {
        segmento = append(segmento, p->dato);
        p = p->succ;
    }

    if (p == q) {
        segmento = append(segmento, p->dato);
    }
    
    return segmento;
}

clista ListaScambiaNodiCons(clista a, nodo *x){

if (x == NULL || x->succ == NULL) {
        return a; // Non ci sono nodi successivi da scambiare
    }

    nodo *y = x->succ; // Nodo successivo a x

    // Aggiornamento dei puntatori
    x->succ = y->succ; // x ora punta al successivo del successore
    if (y->succ != NULL) {
        y->succ->prec = x; // Se esiste, il successivo di y punta a x
    }

    y->prec = x->prec; // y ora punta al precedente di x
    if (x->prec != NULL) {
        x->prec->succ = y; // Se esiste, il precedente di x punta a y
    }

    y->succ = x; // y punta a x
    x->prec = y; // x punta a y come precedente

    // Se x era la testa della lista, aggiornare a
    if (a == x) {
        a = y;
    }

    return a; 
    
}

nodo *ListaMediano(clista a){
    int n_nodi=contaNodi(a);
    int pos=n_nodi/2;
    nodo *p=a;
    for(int i=0;i<pos;i++){
        p=p->succ;
    }
    return p;
}

clista clista_raddoppia(clista a){
    int i=0;
    int n_nodi=contaNodi(a);
    while(i<n_nodi){
        a=appenddi0(a);
        i++;
    }
    return a;
}

int contaNodi(clista a) {
    int count = 0; // Contatore dei nodi
    nodo *p = a;   // Puntatore al nodo corrente

    while (p != NULL) {
        count++;   // Incrementa il contatore
        p = p->succ; // Vai al nodo successivo
    }

    return count; // Restituisce il numero di nodi
}


clista appenddi0(clista a){

    nodo *new_node = malloc(sizeof(nodo));

    nodo *p = a;

    if (a == NULL) {
    nodo *new_node = malloc(sizeof(nodo));
    new_node->dato = 0;
    new_node->succ = NULL;
    new_node->prec = NULL;
    return new_node;
}

    while (p->succ != NULL) { // Fino a che non raggiungo la fine della lista
        p = p->succ;
    }

    new_node->succ=NULL;
    new_node->dato = 0;
    new_node->prec=p;
    p->succ = new_node;

    return a;

}


// Funzione per eliminare un nodo specifico
nodo *clista_out(clista a, float k) {
    nodo *p = clista_cerca(a, k); // Cerca il nodo e mi ritorna l'indirizzo di p
    if (p == NULL) {
        return a; // Nodo non trovato
    }

    nodo *q = p->prec; // Nodo precedente al nodo da eliminare (quindi trovato)

    if (q == NULL) { // se q = NULL, allora il nodo da eliminare era la testa (perchè non c'è nulla)
        return clista_out0(a); //elimina il primo nodo (cioè quello dalla testa)
    }

    // Collegamento del nodo precedente al successivo
    q->succ = p->succ;
    if (p->succ != NULL) {
        p->succ->prec = q;
    }

    free(p); // Liberazione del nodo trovato
    return a;
}

nodo *clista_in(clista a, float k, int pos){

    nodo *new_node = malloc(sizeof(nodo));

    if (pos == 0 || a == NULL) { //se la lista è vuota oppure la posizione che ho inserito è 0
        // Inserimento in testa
        return clista_in0(a, k);
        } //in realtà non servirebbe la condizione se a==NULL per via della funzione clista_in0 

    nodo *p = a; //salvo l'indirizzo del primo nodo 
    int current_pos = 0;

    while (p->succ != NULL && current_pos < pos-1) { 
        p = p->succ;
        current_pos++;
    }
    //faccio una ricerca per posizione shiftando i nodi con il puntatore succ. Vado avanti con la ricerca fintanto che il puntatore succ che viene incrementato è diverso da NULL ecc...

    new_node->dato = k; //assegno il valore k al nuovo nodo
    new_node->succ = p->succ; // assegno a succ del nuovo nodo il succ del precedente perchè p->succ si è fermato al nodo prima del nodo da inserire
    new_node->prec = p;

    if (p->succ != NULL) {
        p->succ->prec = new_node; //aggiorna campo prec di nodo successivo
    }
    p->succ = new_node;

    return a;

    }

// Funzione per eliminare il primo nodo
nodo *clista_out0(clista a) {
    if (a == NULL) {
        return NULL; // Lista già vuota
    }

    nodo *p = a;    // Salviamo il nodo da scollegare
    a = a->succ;    // Spostiamo la testa della lista
    if (a != NULL) {
        a->prec = NULL; // Scollegamento del nodo
    }

    free(p); // Liberazione del nodo
    return a;
}

// Funzione per cercare un nodo
nodo *clista_cerca(clista a, float k) {
    nodo *p = a;
    while (p != NULL && p->dato != k) {
        p = p->succ;
    }
    return p; // Restituisce NULL se non trovato
}

// Funzione per inserire un nodo in testa
nodo *clista_in0(clista a, float v) {
    nodo *p = malloc(sizeof(nodo));
    if (p == NULL) {
        return NULL; // Restituisce NULL in caso di errore di allocazione
    }
    p->dato = v;
    p->succ = a;
    p->prec = NULL; // Il primo nodo non ha un precedente
    if (a != NULL) { 
        a->prec = p; // Collegamento della lista alla testa
    }
    return p;
}

// Creazione di una lista vuota
clista clista_vuota() {
    return NULL;
}

// Mostra il contenuto della lista
void clista_mostra(clista a) {
    nodo *p = a;
    printf("Contenuto della lista -->");
    while (p != NULL) { // Fino a che non raggiungo la fine della lista
        printf(" %5.2f,", p->dato);
        p = p->succ;
    }
    printf("\n");
}

int main() {
    clista L = clista_vuota();

    // Inserimento iniziale
    for (int i = 0; i < 10; i++) {
        L = clista_in0(L, i);
    }
    clista_mostra(L);

    // Eliminazione di tutti i nodi

    // Reinserimento e test di eliminazione
   
    L = clista_out(L, 5);
    clista_mostra(L);

    L = clista_out(L, 9);
    clista_mostra(L);

    L=clista_in(L, 97, 3); 
    clista_mostra(L);

    L=clista_in(L, 97, 9); 
    clista_mostra(L);

    L=appenddi0(L);
    clista_mostra(L);

    int value=contaNodi(L);
    printf("Il numero di nodi e': %d", value);

    L=clista_raddoppia(L);
    clista_mostra(L);

    nodo *x=clista_cerca(L, 97);
    printf("Il valore di x è: %f\n", x->dato);

    nodo *p=ListaMediano(L);
    printf("Il valore del nodo mediano è: %f\n", p->dato);

    nodo *y = clista_cerca(L, 7);
    L=ListaScambiaNodiCons(L, y);
    clista_mostra(L);

    L=CancellaTuttoValore(L,0);
    clista_mostra(L);

    L=InvertiLista(L);
    clista_mostra(L);

    clista Lnew1 = clista_vuota();

    // Inserimento iniziale
    for (int i = 0; i < 10; i++) {
        Lnew1 = append(Lnew1, i);
    }
    clista_mostra(Lnew1);
    
    clista Lnew2 = clista_vuota();

    // Inserimento iniziale
    for (int i = 0; i < 10; i++) {
        Lnew2 = clista_in0(Lnew2, i);
    }
    clista_mostra(Lnew2);

    clista Lnew3 = MergeInv(Lnew1, Lnew2);
    clista_mostra(Lnew3);

    clista lista=InputList();
    clista_mostra(lista);

    int n = 3; // Numero di liste nell'array
    clista liste[n]; // Array di liste

    // Inizializza tutte le liste a NULL
    for (int i = 0; i < n; i++) {
        liste[i] = NULL;
    }

    // Riempire le liste con valori
    liste[0] = append(liste[0], 10.5);
    liste[0] = append(liste[0], 20.3);
    liste[0] = append(liste[0], 30.1);

    liste[1] = append(liste[1], 40.2);
    liste[1] = append(liste[1], 50.6);

    liste[2] = append(liste[2], 60.8);

    // Stampare tutte le liste prima dell'ordinamento
    printf("Liste prima dell'ordinamento:\n");
    for (int i = 0; i < n; i++) {
        printf("Lista %d: ", i);
        clista_mostra(liste[i]);
    }

    // Ordinare le liste in base alla lunghezza
    ArrayListeSort(liste, n);

    // Stampare tutte le liste dopo l'ordinamento
    printf("\nListe dopo l'ordinamento:\n");
    for (int i = 0; i < n; i++) {
        printf("Lista %d: ", i);
        clista_mostra(liste[i]);
    }

    int k = 4; // Numero di liste nell'array
    clista Liste[k]; // Array di liste

    // Inizializza tutte le liste a NULL
    for (int pos = 0; pos < k; pos++) {
        Liste[pos] = NULL;
    }

    // Riempire le liste con valori
    Liste[0] = append(Liste[0], 2);
    Liste[0] = append(Liste[0], 3);

    Liste[1] = append(Liste[1], 3);
    Liste[1] = append(Liste[1], 50.6);

    Liste[2] = append(Liste[2], 1);
    Liste[2] = append(Liste[2], 3);
    Liste[2] = append(Liste[2], 0);

    Liste[3] = append(Liste[3], 2);

    int I[]={1,1,0,0};

    ind_set(Liste,I,k);

    // Stampare tutte le liste dopo l'ordinamento
    printf("\nListe di indset:\n");
    for (int pos = 0; pos < k; pos++) {
        printf("Lista %d: ", pos);
        clista_mostra(Liste[pos]);
    }

    ind_set(Liste,I,k);



}

/*

append:	O(n)
EstraiSegmento:	O(n+m)
ListaScambiaNodiCons: O(1)
ListaMediano: O(n)
clista_raddoppia: O(n2)
contaNodi: O(n)
appenddi0: O(n)
clista_out: O(n)
clista_in: O(n)
clista_out0: O(1)
clista_cerca: O(n)
clista_in0: O(1)
clista_vuota: O(1)
clista_mostra: O(n)
CancellaTuttoValore: O(n)
InvertiLista: O(n)
MergeInv: O(n)
InputList: O(n**2)
ArrayListeSort: O(n**2)

*/
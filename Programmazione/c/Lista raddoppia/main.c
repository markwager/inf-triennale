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

*/

#include <stdio.h>
#include <stdlib.h>

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
    p->dato = v;
    p->succ = a;
    p->prec = NULL; //perchè il primo nodo non ha un precedente
    if (a != NULL) { 
        a->prec = p; // Collegamento della lista alla testa di essa
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

    float k1=97;
    float k2=3;
    L=EstraiSegmento(L, k1, k2);
    clista_mostra(L);
    
    

}
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
        fprintf(stderr, "Errore di allocazione della memoria\n");
        exit(1);
    }
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

}
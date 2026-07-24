//progettare una struttura dati tipo coda che consenta le seguenti operazioni su insiemi di stringhe:
//- init coda vuota
//- inserimento di una stringa
//- lettura/stampa della stringa più vecchia della struttura
//- cancellazione della stringa più anziana

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Struttura del nodo
typedef struct nodo {
    char *dato;
    struct nodo *succ;
} nodo;

// Struttura della coda
typedef struct {
    nodo *head;
    nodo *tail;
} coda;

// Funzioni per la gestione della coda
coda* init_coda();
void append(coda*, const char*);
char* outold(coda*);
char* cerca(coda*);
void mostra_coda(coda*);
int is_empty(coda*);
void free_coda(coda*);

int main() {
    coda *coda = init_coda();

    // Inserimento di stringhe
    append(coda, "Stringa 1");
    append(coda, "Stringa 2");
    append(coda, "Stringa 3");

    // Mostra il contenuto della coda
    printf("Coda iniziale:\n");
    mostra_coda(coda);

    // Lettura della stringa più vecchia
    printf("\nStringa più vecchia: %s\n", cerca(coda));

    // Rimuovi la stringa più vecchia
    printf("\nRimuovi la stringa più vecchia: %s\n", outold(coda));
    printf("Coda dopo dequeue:\n");
    mostra_coda(coda);

    // Altre operazioni
    append(coda, "Stringa 4");
    printf("\nCoda dopo un altro enqueue:\n");
    mostra_coda(coda);

    // Svuota la coda
    while (!is_empty(coda)) {
        printf("Rimuovi: %s\n", outold(coda));
    }
    printf("Coda vuota!\n");

    // Libera la memoria della coda
    free_coda(coda);
}

// Inizializza una coda vuota
coda* init_coda() {
    coda *q = malloc(sizeof(coda));
    q->head = NULL;
    q->tail = NULL;
    return q;
}

// Inserisce una stringa nella coda
void append(coda *q, const char *str) {
    nodo *new_node = malloc(sizeof(nodo)); //crea un nuovo nodo
    new_node->dato = malloc(strlen(str) + 1); // Alloca memoria per la stringa
    strcpy(new_node->dato, str); // Copia la stringa
    new_node->succ = NULL; //ora il nodo non ha un nodo successivo perchè è già l'ultimo

    if (q->tail == NULL) { // Coda vuota
        q->head = new_node;
        q->tail = new_node;
    }
    else { //se non è vuota
        q->tail->succ = new_node; //indica il nodo successivo alla coda attuale=il nuovo nodo
        //quindi il penultimo nodo punta all'ultimo
        q->tail = new_node; //aggiorna il puntatore alla coda (perchè prima puntava al penultimo)
    }
}

// Rimuove la stringa più vecchia dalla coda
char* outold(coda *q) {
    if (q->head == NULL) { // Coda vuota, si potrebbe anche usare q->tail == NULL
        return NULL;
    }

    nodo *old_head = q->head; // Nodo da rimuovere è uguala alla testa
    char *result = old_head->dato; // Stringa da restituire

    q->head = old_head->succ; // La testa punta al nodo successivo della vecchia testa
    if (q->head == NULL) { //se la testa era l'ultimo nodo della coda allora la coda diventa vuota
        q->tail = NULL;
    }

    free(old_head);
    return result;
}

// Legge la stringa più vecchia senza rimuoverla
char* cerca(coda *q) {
    if (q->head == NULL) { // Coda vuota
        return NULL;
    }
    return q->head->dato; // Restituisce la stringa della testa
}

// Mostra il contenuto della coda
void mostra_coda(coda *q) {
    nodo *current = q->head;
    printf("Contenuto della coda: ");
    while (current != NULL){
        printf("\"%s\" -> ", current->dato);
        current = current->succ;
    }
    printf("NULL\n");
}

// Controlla se la coda è vuota
int is_empty(coda *q) {
    return q->head == NULL;
}

// Libera tutta la memoria della coda
void free_coda(coda *q) {
    while (!is_empty(q)) {
        char *str = outold(q);
        free(str); // Libera la stringa
    }
    free(q); // Libera la struttura coda
}

/*

append:	Inserisce un elemento	O(1)
outold:	Rimuove l'elemento più vecchio	O(1)
cerca:	Restituisce il primo elemento	O(1)
is_empty:	Controlla se la coda è vuota	O(1)
free_coda:	Libera la memoria della coda	O(n)
mostra_coda:	Mostra il contenuto della coda	O(n)

*/
/*
La funzione deve ricevere in input due puntatori a vettori v1 e v2, calcolare la loro somma (coordinata per coordinata) e restituire un puntatore al nuovo vettore risultato.
*/

#include <stdlib.h> // Necessario per malloc e free
#include <stdio.h> // Necessario per printf

struct vector {
    float x, y, z;
};
typedef struct vector vector;

vector *add_vectors(vector *v1, vector *v2);

vector *add_vectors(vector *v1,vector *v2){
    vector *a=malloc(sizeof(vector));
    a->x = v1->x + v2->x;
    a->y = v1->y + v2->y;
    a->z = v1->z + v2->z;
    return a;
}

int main() {
    vector *v1 = malloc(sizeof(vector));
    vector *v2 = malloc(sizeof(vector));
    v1->x = 1; v1->y = 2; v1->z = 3;
    v2->x = 4; v2->y = 5; v2->z = 6;

    // Somma i due vettori
    vector *v3 = add_vectors(v1, v2);

    // Stampa il risultato
    printf("Risultato: %f %f %f\n", v3->x, v3->y, v3->z);

}

/*
se devi restituire un puntatore con struct di una funzione allora serve la malloc
se hai solo una struct come funzione allora non serve la malloc
se hai delle malloc nella struct devi usare malloc per quelle

Se ci sono due puntatori all'interno di una struct, ma il prototipo della funzione non deve restituire un puntatore, si può agire in due modi principali:

    Modificare i valori dei puntatori della struct tramite riferimento: La funzione riceve un puntatore alla struct e modifica i valori a cui puntano i suoi membri senza
    restituire nulla.

    Restituire una struttura per valore: La funzione restituisce una copia della struct con i puntatori già inizializzati e gestiti internamente, evitando l'uso esplicito di
    puntatori come risultato.

    Esempio del primo caso: #include <stdio.h>

    #include <stdlib.h>

    struct Rectangle {
        int *width;
        int *height;
    };

    // Prototipo della funzione: non restituisce nulla
    void set_rectangle(struct Rectangle *r, int w, int h) {
        // Allocazione dinamica per i membri della struttura
        r->width = malloc(sizeof(int));
        r->height = malloc(sizeof(int));
        if (r->width == NULL || r->height == NULL) {
            printf("Errore nell'allocazione della memoria\n");
            exit(1);
        }
        *r->width = w;  // Assegna il valore al puntatore width
        *r->height = h; // Assegna il valore al puntatore height
    }

    void free_rectangle(struct Rectangle *r) {
        free(r->width);  // Libera la memoria allocata per width
        free(r->height); // Libera la memoria allocata per height
    }

    int main() {
        struct Rectangle rect;
        set_rectangle(&rect, 10, 20);

        printf("Larghezza: %d, Altezza: %d\n", *rect.width, *rect.height);

        free_rectangle(&rect);  // Libera la memoria allocata
        return 0;
    }

    Esempio secondo caso:

    #include <stdio.h>
    #include <stdlib.h>

    struct Rectangle {
        int *width;
        int *height;
    };

    // Prototipo della funzione: restituisce una struttura per valore
    struct Rectangle create_rectangle(int w, int h) {
        struct Rectangle r;
        // Allocazione dinamica per i membri della struttura
        r.width = malloc(sizeof(int));
        r.height = malloc(sizeof(int));
        if (r.width == NULL || r.height == NULL) {
            printf("Errore nell'allocazione della memoria\n");
            exit(1);
        }
        *r.width = w;  // Assegna il valore al puntatore width
        *r.height = h; // Assegna il valore al puntatore height
        return r;      // Restituisce la struttura per valore
    }

    void free_rectangle(struct Rectangle *r) {
        free(r->width);  // Libera la memoria allocata per width
        free(r->height); // Libera la memoria allocata per height
    }

    int main() {
        struct Rectangle rect = create_rectangle(10, 20);

        printf("Larghezza: %d, Altezza: %d\n", *rect.width, *rect.height);

        free_rectangle(&rect);  // Libera la memoria allocata
        return 0;
    }

    se non ci sono puntatori nella struct, la funzione non deve restituire un puntatore ma ce ne è uno come argomento nella funzione non si usa malloc


*/
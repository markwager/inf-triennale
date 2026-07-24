#include <stdio.h>
#include <stdlib.h>

struct int_array {
    int dim;  // Dimensione dell'array di posizioni
    int *v;   // Array delle posizioni
};

typedef struct int_array int_array;

int_array pos_max(float *a, int n) {
    int_array result;
    result.v = malloc(n * sizeof(int));  // Allocazione dinamica dell'array per le posizioni
    result.dim = 0;  // Inizialmente non ci sono posizioni

    // Troviamo il massimo nell'array
    float max_value = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] > max_value) {
            max_value = a[i];
        }
    }

    // Troviamo tutte le posizioni che contengono il massimo
    for (int i = 0; i < n; i++) {
        if (a[i] == max_value) {
            result.v[result.dim] = i;  // Aggiungiamo la posizione all'array
            result.dim++;  // Incrementiamo la dimensione
        }
    }

    // Riassegniamo la memoria per la dimensione effettiva dell'array
    result.v = (int *)realloc(result.v, result.dim * sizeof(int));

    return result;  // Restituiamo l'array con le posizioni
}

int main() {
    float a[] = {1.5, 2.3, 3.4, 2.3, 3.4, 0.9};  // Esempio di array
    int n = sizeof(a) / sizeof(a[0]);

    int_array result = pos_max(a, n);

    // Stampa dei risultati
    printf("Posizioni dei massimi: ");
    for (int i = 0; i < result.dim; i++) {
        printf("%d ", result.v[i]);
    }
    printf("\n");

    // Libera la memoria allocata
    free(result.v);

    return 0;
}
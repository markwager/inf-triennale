#include <stdio.h>
#include <stdlib.h>

// Funzione per eseguire il merge di due array ordinati
int* merge(int* a, int size_a, int* b, int size_b, int* size_result) {
    int* result = (int*)malloc((size_a + size_b) * sizeof(int)); // Array di output
    int i = 0, j = 0, k = 0;

    // Fase 1: Confronta gli elementi delle due liste e aggiungi il più piccolo
    while (i < size_a && j < size_b) {
        if (a[i] <= b[j]) {
            result[k] = a[i];
            i++;
        }

        else {
            result[k] = b[j];
            j++;
        }

        k++;
    }

    // Fase 2: Aggiungi gli elementi rimanenti della prima lista (se ci sono)
    while (i < size_a) {
        result[k] = a[i];
        i++;
        k++;
    }

    // Fase 3: Aggiungi gli elementi rimanenti della seconda lista (se ci sono)
    while (j < size_b) {
        result[k] = b[j];
        j++;
        k++;
    }

    *size_result = k; // Imposta la dimensione dell'array risultato
    return result;
}

int main() {
    // Esempio di utilizzo
    int a[] = {1, 3, 5, 7};
    int b[] = {2, 4, 6, 8};
    int size_a = sizeof(a) / sizeof(int);
    int size_b = sizeof(b) / sizeof(int);

    int size_result;
    int* result = merge(a, size_a, b, size_b, &size_result);

    printf("Array fuso:\n");
    for (int i = 0; i < size_result; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");

    free(result); // Libera la memoria allocata
    return 0;
}
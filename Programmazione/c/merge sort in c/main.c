#include <stdio.h>
#include <stdlib.h>

// Funzione per eseguire il merge di due array ordinati
int* merge(int* a, int size_a, int* b, int size_b, int* size_result) {
    int* result = (int*)malloc((size_a + size_b) * sizeof(int)); // Array di output
    int i = 0, j = 0, k = 0;

    // Fase 1: Confronta gli elementi delle due liste e aggiungi il più piccolo
    while (i < size_a && j < size_b) {
        if (a[i] <= b[j]) {
            result[k++] = a[i++];
        } else {
            result[k++] = b[j++];
        }
    }

    // Fase 2: Aggiungi gli elementi rimanenti della prima lista (se ci sono)
    while (i < size_a) {
        result[k++] = a[i++];
    }

    // Fase 3: Aggiungi gli elementi rimanenti della seconda lista (se ci sono)
    while (j < size_b) {
        result[k++] = b[j++];
    }

    *size_result = k; // Imposta la dimensione dell'array risultato
    return result;
}

// Funzione ricorsiva per il Merge Sort
void mergeSort(int* array, int size) {
    if (size < 2) {
        return; // Base della ricorsione: array di un elemento
    }

    int mid = size / 2;
    
    // Divide l'array in due sotto-array
    int* left = (int*)malloc(mid * sizeof(int));
    int* right = (int*)malloc((size - mid) * sizeof(int));

    for (int i = 0; i < mid; i++) {
        left[i] = array[i];
    }
    for (int i = mid; i < size; i++) {
        right[i - mid] = array[i];
    }

    // Ordina ricorsivamente le due metà
    mergeSort(left, mid);
    mergeSort(right, size - mid);

    // Fonde le due metà ordinate
    int size_result;
    int* merged = merge(left, mid, right, size - mid, &size_result);

    // Copia l'array ordinato nel buffer originale
    for (int i = 0; i < size; i++) {
        array[i] = merged[i];
    }

    // Libera la memoria allocata
    free(left);
    free(right);
    free(merged);
}

int main() {
    // Esempio di utilizzo
    int array[] = {38, 27, 43, 3, 9, 82, 10};
    int size = sizeof(array) / sizeof(array[0]);

    printf("Array originale:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    // Ordina l'array con il Merge Sort
    mergeSort(array, size);

    printf("Array ordinato:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    return 0;
}

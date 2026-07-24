#include <stdio.h>

// Funzione per eseguire la ricerca binaria
int binarySearch(int* array, int size, int target) {
    int left = 0, right = size - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2; // Calcolo del punto centrale

        if (array[mid] == target) {
            return mid; // Elemento trovato
        } else if (array[mid] < target) {
            left = mid + 1; // Cerca nella metà destra
        } else {
            right = mid - 1; // Cerca nella metà sinistra
        }
    }

    return -1; // Elemento non trovato
}

int main() {
    // Esempio di utilizzo
    int array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}; // Array ordinato
    int size = sizeof(array) / sizeof(array[0]);
    int target = 5;

    printf("Array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    // Esegui la ricerca binaria
    int result = binarySearch(array, size, target);

    if (result != -1) {
        printf("Elemento %d trovato all'indice %d.\n", target, result);
    } else {
        printf("Elemento %d non trovato nell'array.\n", target);
    }

    return 0;
}

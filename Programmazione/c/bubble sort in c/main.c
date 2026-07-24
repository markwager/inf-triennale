
#include <stdio.h>

// Funzione per eseguire il Bubble Sort ottimizzato
void bubbleSort(int* array, int size) {
    int swapped;

    for (int i = 0; i < size - 1; i++) {
        swapped = 0; // Indica se ci sono stati scambi

        for (int j = 0; j < size - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                // Scambia gli elementi
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
                swapped = 1; // Registra che è avvenuto uno scambio
            }
        }

        // Se non ci sono stati scambi, l'array è già ordinato
        if (swapped == 0) {
            break;
        }
    }
}

int main() {
    // Esempio di utilizzo
    int array[] = {1, 2, 3, 4, 5, 6}; // Già ordinato
    int size = sizeof(array) / sizeof(array[0]);

    printf("Array originale:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    // Ordina l'array con il Bubble Sort
    bubbleSort(array, size);

    printf("Array ordinato:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    return 0;
}

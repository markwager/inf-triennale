#include <stdio.h>
#include <string.h>

void centering(int *a, int r, int c) {
    // Itera sulle righe
    for (int i = 0; i < r; i++) {
        int count_ones = 0;

        // Conta il numero di `1` nella riga i
        for (int j = 0; j < c; j++) {
            if (a[i * c + j] == 1) {
                count_ones++;
            }
        }

        // Riempi la riga con `0`
        for (int j = 0; j < c; j++) {
            a[i * c + j] = 0; //indice_riga*n_colonne+indice_colonna
        }

        // Calcola l'inizio della sequenza di `1` centrata
        int start_index = (c - count_ones) / 2;

        // Inserisci gli `1` al centro
        for (int j = 0; j < count_ones; j++) {
            a[i * c + start_index + j] = 1;
        }
    }
}


int main() {
    int a[] = {
        1, 1, 0, 0, 0,
        1, 0, 0, 0, 0,
        1, 1, 1, 0, 0,
        1, 1, 0, 0, 0,
        1, 1, 1, 1, 1,
        1, 1, 1, 1, 1
    };

    int r = 6;
    int c = 5;

    centering(a, r, c);

    printf("\nMatrix after centering:\n");
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            printf("%d ", a[i * c + j]);
        }
        printf("\n");
    }

}
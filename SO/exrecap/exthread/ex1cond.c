#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

#define N 11

int count = 0;
int buffer[N];
int inizializzata[N] = {0}; // Array di supporto per contare le celle UNICHE
int termina = 0;

pthread_mutex_t mutex;
pthread_cond_t condc;

void *task1(void *arg) {
    while (1) {
        pthread_mutex_lock(&mutex);
        if (termina) {
            pthread_mutex_unlock(&mutex);
            break;
        }

        int index = rand() % N;
        buffer[index] = 1;

        // Incrementiamo count solo se la cella era vuota
        if (inizializzata[index] == 0) {
            inizializzata[index] = 1;
            count++;
            pthread_cond_signal(&condc); // Sveglia T3 se stava aspettando
        }

        printf("[T1] Scritto +1 in %d. Celle totali: %d\n", index, count);
        pthread_mutex_unlock(&mutex);
        sleep(rand() % 3);
    }
    return NULL;
}

void *task2(void *arg) {
    while (1) {
        pthread_mutex_lock(&mutex);
        if (termina) {
            pthread_mutex_unlock(&mutex);
            break;
        }

        int index = rand() % N;
        buffer[index] = -1;

        if (inizializzata[index] == 0) {
            inizializzata[index] = 1;
            count++;
            pthread_cond_signal(&condc);
        }

        printf("[T2] Scritto -1 in %d. Celle totali: %d\n", index, count);
        pthread_mutex_unlock(&mutex);
        sleep(rand() % 3);
    }
    return NULL;
}

void *task3(void *arg) {
    pthread_mutex_lock(&mutex);
    
    // USIAMO IL WHILE: T3 dorme finché count non arriva a N
    while (count < N) {
        printf("[T3] Buffer incompleto (%d/%d), vado a dormire...\n", count, N);
        pthread_cond_wait(&condc, &mutex);
    }

    // Se arriviamo qui, il buffer è pieno!
    int pos = 0, neg = 0;
    for (int i = 0; i < N; i++) {
        if (buffer[i] == 1) pos++;
        else if (buffer[i] == -1) neg++;
    }

    printf("\n--- RISULTATO FINALE ---\n");
    printf("Positivi: %d, Negativi: %d\n", pos, neg);
    printf(pos > neg ? "Vince T1!\n" : "Vince T2 (o pareggio)!\n");

    // Diciamo agli altri di chiudere
    termina = 1;
    pthread_mutex_unlock(&mutex);
    
    return NULL;
}

int main() {
    srand(time(NULL));
    pthread_t th1, th2, th3;

    pthread_create(&th1, NULL, task1, NULL);
    pthread_create(&th2, NULL, task2, NULL);
    pthread_create(&th3, NULL, task3, NULL);

    // Aspettiamo che T3 finisca i calcoli
    pthread_join(th3, NULL);
    
    // Aspettiamo che T1 e T2 vedano 'termina=1' e escano
    pthread_join(th1, NULL);
    pthread_join(th2, NULL);

    printf("Tutti i thread terminati correttamente.\n");
   
    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&condc);

}

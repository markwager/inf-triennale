#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

#define N 11

int buffer[N];
pthread_t th1, th2, th3;
pthread_mutex_t mutex;
int finito = 0;

void *task1(void *arg) {
    while (1) {
        pthread_mutex_lock(&mutex); // Aggiunta la &
        if (finito) {
            pthread_mutex_unlock(&mutex);
            pthread_exit(NULL); // Aggiunto per uscire davvero
        }

        int index = rand() % N;
        buffer[index] = 1;
        pthread_mutex_unlock(&mutex);
        sleep(rand() % 4);
    }
}

void *task2(void *arg) {
    while (1) {
        pthread_mutex_lock(&mutex);
        if (finito) {
            pthread_mutex_unlock(&mutex);
            pthread_exit(NULL);
        }

        int index = rand() % N;
        buffer[index] = -1;
        pthread_mutex_unlock(&mutex);
        sleep(rand() % 4);
    }
}

void *task3(void *arg) {
    while (1) {
        int occup = 0; // Inizializzato a 0
        int pos = 0;   // Inizializzato a 0
        int neg = 0;   // Inizializzato a 0
        
        pthread_mutex_lock(&mutex);
        
        for (int i = 0; i < N; i++) {
            if (buffer[i] != 0) {
                occup++;
            }
        }

        if (occup == N) {
            for (int i = 0; i < N; i++) {
                if (buffer[i] == 1) pos++;
                else neg++;
            }
            
            if (pos > neg) printf("Vincono gli 1 (%d contro %d)\n", pos, neg);
            else printf("Vincono i -1 (%d contro %d)\n", neg, pos);
            
            finito = 1;
            pthread_mutex_unlock(&mutex);
            pthread_exit(NULL); // Corretta sintassi
        }
        
        pthread_mutex_unlock(&mutex);
        sleep(1); // Una piccola pausa per non saturare la CPU
    }
}

int main() {
    srand(time(NULL));

    // Corretto il ; nel ciclo for
    for (int i = 0; i < N; i++) {
        buffer[i] = 0;
    }

    pthread_mutex_init(&mutex, NULL);

    pthread_create(&th1, NULL, task1, NULL);
    pthread_create(&th2, NULL, task2, NULL);
    pthread_create(&th3, NULL, task3, NULL);

    pthread_join(th1, NULL);
    pthread_join(th2, NULL);
    pthread_join(th3, NULL);

    pthread_mutex_destroy(&mutex); // Aggiunta & se necessario (dipende dalla firma ma di solito si passa l'indirizzo)
}

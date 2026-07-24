#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>

#define N 10

int buff1[N] = {0};
int buff2[N] = {0};
int finito = 0; // Flag per fermare i thread

pthread_mutex_t mutex;

void *task1(void *arg) {
    while (1) {
        pthread_mutex_lock(&mutex);
        if (finito) { 
            pthread_mutex_unlock(&mutex); 
            break; 
        }
        
        // Scrive un numero tra 1 e 150 in una posizione casuale
        int num = (rand() % 150) + 1;
        int index = rand() % N;
        buff1[index] = num;
        
        pthread_mutex_unlock(&mutex);
        sleep(3); 
    }
    pthread_exit(NULL);
}

void *task2(void *arg) {
    while (1) {
        pthread_mutex_lock(&mutex);
        if (finito) { 
            pthread_mutex_unlock(&mutex); 
            break; 
        }
        
        // Scrive un numero tra 150 e 300 in una posizione casuale
        int num = (rand() % 151) + 150;
        int index = rand() % N;
        buff2[index] = num;
        
        pthread_mutex_unlock(&mutex);
        sleep(3);
    }
    pthread_exit(NULL);
}

void *task3(void *arg) {
    while (1) {
        pthread_mutex_lock(&mutex);
        
        // 1. Controllo se entrambi gli array sono pieni (nessuno zero presente)
        int pronti = 1; 
        for (int i = 0; i < N; i++) {
            if (buff1[i] == 0 || buff2[i] == 0) {
                pronti = 0; 
                break;
            }
        }

        if (pronti) {
            // 2. Calcolo Max e Min per ogni array
            int maxA = buff1[0], minA = buff1[0];
            int maxB = buff2[0], minB = buff2[0];

            for (int i = 0; i < N; i++) {
                if (buff1[i] > maxA) maxA = buff1[i];
                if (buff1[i] < minA) minA = buff1[i];
                if (buff2[i] > maxB) maxB = buff2[i];
                if (buff2[i] < minB) minB = buff2[i];
            }

            // 3. Calcolo Max e Min Assoluti con if/else classici
            int maxAbs, minAbs;

            if (maxA > maxB) {
                maxAbs = maxA;
            } else {
                maxAbs = maxB;
            }

            if (minA < minB) {
                minAbs = minA;
            } else {
                minAbs = minB;
            }

            // 4. Stampa Risultati
            printf("--- ELABORAZIONE COMPLETATA ---\n");
            printf("Array A: Max = %d, Min = %d\n", maxA, minA);
            printf("Array B: Max = %d, Min = %d\n", maxB, minB);
            printf("RISULTATI FINALI:\n");
            printf("Max{max(A), max(B)} = %d\n", maxAbs);
            printf("Min{min(A), min(B)} = %d\n", minAbs);

            finito = 1; // Comunica agli altri thread di uscire
            pthread_mutex_unlock(&mutex);
            break; 
        }
        
        pthread_mutex_unlock(&mutex);
        usleep(100000);
    }
	pthread_exit(NULL);
}

int main() {
    srand(time(NULL));
    pthread_t th1, th2, th3;

    // Creazione dei thread
    pthread_create(&th1, NULL, task1, NULL);
    pthread_create(&th2, NULL, task2, NULL);
    pthread_create(&th3, NULL, task3, NULL);

    // Attesa fine dei thread
    pthread_join(th1, NULL);
    pthread_join(th2, NULL);
    pthread_join(th3, NULL);

    printf("\nProgramma terminato correttamente.\n");
}

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <semaphore.h>

#define N 11

// Variabili per gli ID dei thread
pthread_t th1, th2, th3; 
int buffer[N];
sem_t mutex; // Ho usato il nome 'mutex' coerentemente

void down(sem_t *sem) { sem_wait(sem); }
void up(sem_t *sem) { sem_post(sem); }

void *task1(void *arg) {
    while(1) {
        down(&mutex);
        int index = rand() % N;
        buffer[index] = 1;
        printf("T1: inserito 1 in [%d]\n", index);
        up(&mutex);
        sleep(rand() % 4);
    }
}

void *task2(void *arg) {
    while(1) {
        down(&mutex);
        int index = rand() % N;
        buffer[index] = -1;
        printf("T2: inserito -1 in [%d]\n", index);
        up(&mutex);
        sleep(rand() % 4);
    }
}

void *task3(void *arg) {
    while(1) {
        down(&mutex);
        // CORREZIONE: Inizializza sempre a 0 dentro il loop!
        int count_pos = 0, count_neg = 0, occup = 0;
        
        for(int i = 0; i < N; i++) {
            if(buffer[i] != 0) {
                occup++;
                if(buffer[i] == 1) count_pos++;
                else count_neg++;
            }
        }

        printf("T3 Check: occupati %d, pos %d, neg %d\n", occup, count_pos, count_neg);

        if(occup == N && count_pos > count_neg) {
            printf("\n--- CONDIZIONE OK! TERMINO ---\n");
            pthread_cancel(th1);
            pthread_cancel(th2);
            up(&mutex); // Rilascia SEMPRE prima di uscire
            pthread_exit(NULL);
        }
        
        up(&mutex);
        sleep(rand() % 4);
    }
}

int main() {
    srand(time(NULL));
    sem_init(&mutex, 0, 1);

    for(int i = 0; i < N; i++) buffer[i] = 0;

    // Passiamo le funzioni rinominate
    pthread_create(&th1, NULL, task1, NULL);
    pthread_create(&th2, NULL, task2, NULL);
    pthread_create(&th3, NULL, task3, NULL);

    pthread_join(th1, NULL);
    pthread_join(th2, NULL);
    pthread_join(th3, NULL);

    printf("Fine del programma.\n");
    sem_destroy(&mutex);
}

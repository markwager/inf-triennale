#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

#define N 11

// Variabili globali condivise
pthread_mutex_t mutex;
int buffer[N];
int fine_esecuzione = 0; // Flag per terminare tutti i thread

// Thread per scrivere +1
void *task1(void *arg){
    while(1){
        pthread_mutex_lock(&mutex);
        
        // Se il flag di fine è attivo, rilascio ed esco
        if (fine_esecuzione) {
            pthread_mutex_unlock(&mutex);
            break; 
        }

        int index = rand() % N;
        buffer[index] = 1;
        // printf("T1: Scritto +1 in pos %d\n", index); // Debug opzionale

        pthread_mutex_unlock(&mutex);
        sleep(rand() % 4); // Sleep 0-3 secondi
    }
    pthread_exit(NULL);
}

// Thread per scrivere -1
void *task2(void *arg){
    while(1){
        pthread_mutex_lock(&mutex);

        if (fine_esecuzione) {
            pthread_mutex_unlock(&mutex);
            break;
        }

        int index = rand() % N;
        buffer[index] = -1;
        // printf("T2: Scritto -1 in pos %d\n", index); // Debug opzionale

        pthread_mutex_unlock(&mutex);
        sleep(rand() % 4);
    }
    pthread_exit(NULL);
}

// Thread di controllo (Monitor)
void *task3(void *arg){
    while(1){
        pthread_mutex_lock(&mutex);

        int cpos = 0;
        int cneg = 0;
        int celle_piene = 0;

        // Scansione del buffer
        for(int i=0; i<N; i++){
            if(buffer[i] != 0){
                celle_piene++;
                if(buffer[i] == 1){
                    cpos++;
                } else {
                    cneg++;
                }
            }
        }

        // Controllo se TUTTE le celle sono inizializzate
        if(celle_piene == N){
            printf("\n--- BUFFER COMPLETO ---\n");
            printf("Positivi (+1): %d\n", cpos);
            printf("Negativi (-1): %d\n", cneg);

            if(cpos > cneg){
                printf("RISULTATO: Il numero di 1 è MAGGIORE di -1\n");
            } else if (cneg > cpos) {
                printf("RISULTATO: Il numero di 1 è MINORE di -1\n");
            } else {
                printf("RISULTATO: Pareggio\n");
            }

            fine_esecuzione = 1; // Segnalo agli altri di fermarsi
            pthread_mutex_unlock(&mutex); // IMPORTANTE: Rilasciare prima di uscire
            break; // Esco dal ciclo while
        }

        pthread_mutex_unlock(&mutex);
        sleep(rand() % 4);
    }
    pthread_exit(NULL);
}

int main(){
    pthread_t th1, th2, th3;

    srand(time(NULL));

    // 1. Inizializzo il Mutex
    pthread_mutex_init(&mutex, NULL);

    // 2. Inizializzo il buffer PRIMA di creare i thread
    for(int i=0; i<N; i++){
        buffer[i] = 0;
    }

    printf("Avvio dei thread...\n");

    // 3. Creo i thread
    if (pthread_create(&th1, NULL, task1, NULL) != 0) perror("Errore create th1");
    if (pthread_create(&th2, NULL, task2, NULL) != 0) perror("Errore create th2");
    if (pthread_create(&th3, NULL, task3, NULL) != 0) perror("Errore create th3");

    // 4. Attendo la fine dei thread
    pthread_join(th1, NULL);
    pthread_join(th2, NULL);
    pthread_join(th3, NULL);

    printf("Tutti i thread terminati. Programma concluso.\n");

    pthread_mutex_destroy(&mutex);
}

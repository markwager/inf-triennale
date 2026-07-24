#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h> // Necessario per inizializzare rand()

#define NUMBER_OF_THREADS 10

void *print_hello_world(void *tid) {
    // Cast del puntatore void* di nuovo a long/int per la stampa
    long thread_id = (long)tid; 
    
    int r = rand() % 5; 
    sleep(r); 
    
    printf("Ciao mondo dal thread %ld (ho dormito %d secondi)\n", thread_id, r);
    
    pthread_exit(NULL);
}

int main() {
    pthread_t threads[NUMBER_OF_THREADS];
    int status;
    long i; // Usiamo long per evitare problemi di dimensione con i puntatori

    // Inizializza il generatore di numeri casuali con l'ora corrente
    srand(time(NULL));

    for(i = 0; i < NUMBER_OF_THREADS; i++) {
        // Passiamo 'i' come (void *)i. Questo è un trucco comune per passare piccoli interi.
        status = pthread_create(&threads[i], NULL, print_hello_world, (void *)i);

        if(status == 0) {
            printf("Sistema: Thread %ld creato con successo\n", i);
        } else {
            printf("Errore: Impossibile creare il thread %ld\n", i);
            exit(-1);
        }
    }

    for(i = 0; i < NUMBER_OF_THREADS; i++) {
        status = pthread_join(threads[i], NULL);
        
        if(status == 0) {
            printf("Sistema: Thread %ld terminato\n", i);
        } else {
            printf("Errore nel join del thread %ld\n", i);
        }
    }

    return 0;
}

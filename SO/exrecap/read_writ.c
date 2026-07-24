#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <semaphore.h>

#define TRUE 1
#define NUM_READERS 3

sem_t mutex; 
sem_t db;
int rc = 0; 

void down(sem_t *sem) { sem_wait(sem); }
void up(sem_t *sem) { sem_post(sem); }

void read_database() {
    printf("Lettore sta leggendo...\n");
    sleep(1); 
}

void write_database() {
    printf("Scrittore sta scrivendo!!!\n");
    sleep(1);
}

void use_data_read() { sleep(1); }
void think_up_data() { sleep(1); }

// Corretto: void invece di oid
void *reader(void *arg) {
    while(TRUE) {
        down(&mutex);
        rc++;
        if(rc == 1) down(&db);
        up(&mutex);

        read_database();

        down(&mutex);
        rc--;
        if(rc == 0) up(&db);
        up(&mutex);

        use_data_read();
    }
    return NULL;
}

void *writer(void *arg) {
    while(TRUE) {
        think_up_data();
        down(&db); 
        write_database();
        up(&db); 
    }
    return NULL;
}

int main() {
    pthread_t readers_t[NUM_READERS], writer_thread; // Cambiato nome array per chiarezza
    sem_init(&mutex, 0, 1);
    sem_init(&db, 0, 1);

    // Creazione dei lettori: passiamo la funzione 'reader'
    for(int i = 0; i < NUM_READERS; i++) {
        pthread_create(&readers_t[i], NULL, reader, NULL);
    }

    // Creazione dello scrittore: usiamo la variabile corretta 'writer_thread'
    pthread_create(&writer_thread, NULL, writer, NULL);

    // Join dei thread
    for(int i = 0; i < NUM_READERS; i++) {
        pthread_join(readers_t[i], NULL);
    }
    pthread_join(writer_thread, NULL);

    sem_destroy(&mutex);
    sem_destroy(&db);
}

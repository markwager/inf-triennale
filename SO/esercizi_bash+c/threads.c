#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define NUMBER_OF_THREADS 10 //numeor costante di thread che devo creare

//ciò che ogni thread deve fare
void *print_hello_world(void *tid){
    int id = (long)tid;   // ricava l'indice
    int r = rand() % 5;
    sleep(r);
    printf("Hello from thread %d\n", id);
    pthread_exit(NULL); //termina il thread e restituisce NULL
}

int main(int argc, char *argv[]) {
    pthread_t threads[NUMBER_OF_THREADS]; //creo array di thread
    int status, i;

    for(i = 0; i < NUMBER_OF_THREADS; i++) {
        status = pthread_create(&threads[i], NULL,
                                print_hello_world, (void *)(long)i); //crea thread con funzione
				//di avvio print_hello_world. Mi ritorna 0 se thread è stato 
				//creato con successo

        if(status == 0) {
            printf("Thread %d creato con status %d\n", i, status);
        }
	
	 else {
            printf("Errore creando thread %d\n", i);
            exit(-1);
        }
    }
	//ciclo che attende che tutti i thread terminino
    for(i = 0; i < NUMBER_OF_THREADS; i++){
        status = pthread_join(threads[i], NULL); //aspetta che un thread specifico esca

        if(status == 0){
            printf("Thread %d terminato con status %d\n", i, status);
        } else {
            printf("Errore join thread %d\n", i);
            exit(-1);
        }
    }

    return 0;
}

/*
questo programma crea 10 thread con un for che vengono inizializati con funzione print hello world
e poi terminano sempre con un ciclo for
*/

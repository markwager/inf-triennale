#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <semaphore.h>

#define N 10 //numero di posti nel buffer
#define TRUE 1

sem_t mutex; //gestisce accesso regione critica
sem_t empty; //conta posti vuoti
sem_t full; //conta posti occupati

int buffer[N]; //buffer condiviso tra peoduttore e consumatore
int in=0; //indice buffer

//primitive down e up per il semaforo
void down(sem_t *sem){
	sem_wait(sem); //controlla se sem>0
	//se sì, lo decrementa e il thread passa
	//se no, il thread si blocca in attesa
}

void up(sem_t *sem){
	sem_post(sem); //incrementa il val di un semaforo e se c'è un thread bloccato
			//ne risveglia uno
}

//funzione per inserire un elemento in buffer
void insert_item(){
	int item=rand()%100;
	printf("\nInserisco elemento %d in posizione %d\n", item, (in+1));
	buffer[in]=item;
	in++;
}

void remove_item(){
	printf("%i", in);
	int item=buffer[in-1];
	printf("\nPrelevo %d da posizione %d\n", item, in);
	in--;
}

void print_buffer(){
	for(int i=0; i<in; i++){
		printf("%d ", buffer[i]);
	}
	printf("\n");
}

//attività dei due thread
void *producer(void *arg){
	while(TRUE){
		down(&empty); //posto vuoto in meno
		down(&mutex); //entra nella regione critica

		insert_item(); //inserisce elemento nel buffer
		print_buffer(); //stampa il contenuto del buffer

		up(&mutex); //esce dalla regione critica
		up(&full); //segnala che c'è un posto pieno in più nel buffer
	}
}

void *consumer(void *arg){
	while(TRUE){
		down(&full); //c'è un posto pieno in meno
		down(&mutex); //entra nella regione critica

		remove_item(); 
		print_buffer();

		up(&mutex); //esci dal mutex
		up(&empty); //c'è un posto vuoto in più
	}
}

int main(){

	pthread_t prod, cons; //dichiarazione dei thread
	
	//inizializzazione dei semafori
	sem_init(&mutex, 0, 1); //il primo numero (lo 0) riguarda i thread, il secondo è il valore con cui viene
	//inizializzato il mutex 
	sem_init(&empty, 0, N); //same
	sem_init(&full, 0, 0); //same
	
	//creazione dei thread
	pthread_create(&prod, NULL, producer, NULL); //scrive id in prod e ha la routine produce
	pthread_create(&cons, NULL, consumer, NULL); //scrive id in cons e ha la routine consumer
	
	//attesa della terminazione dei thread
	pthread_join(prod, NULL);
	pthread_join(cons, NULL);
	
	//distribuzione dei semafori
	sem_destroy(&mutex);
	sem_destroy(&empty);
	sem_destroy(&full);
}

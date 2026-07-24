#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <semaphore.h>

#define N 10 //numero di posti nel buffer
#define TRUE 1

//dichiaraz dei semafori
sem_t mutex;
sem_t empty;
sem_t full;

int buffer[N]; //buffer condiviso tra prod e cons
int in=0; //indice dove inserire il prossimo elemento nel buffer

void down(sem_t *sem){
	sem_wait(sem);
}

void up(sem_t *sem){
	sem_post(sem);
}

//inserimento elemento
void insert_item(){
	int item=rand()%100;
	printf("\nInserisco %d in posizione %d\n", item, (in+1));
	buffer[in]=item;
	in++;
}

//rimozione elemento
void remove_item(){
	printf("%d", in);
	int item=buffer[in-1];
	printf("\nPrelevo %d da posizione %d\n", item, in);
	in--;
}

void print_buffer(){
	for(int i=0; i<in; i++){
		printf("%d", buffer[i]);

	}
	printf("\n");
}

void *producer(void *arg){
	while(TRUE){
		down(&empty); //attende finchè ci sono posti vuoti nel buffer
		down(&mutex); //entra nella regione critica

		insert_item(); //inserisce un element nel buffer
		print_buffer(); //stampa il conteuto del buffer

		up(&mutex); //esce dalla regione critica
		up(&full); //segnala che c'è un posto pieno in +
	}
}

void *consumer(void *arg){
	while(TRUE){
		down(&full);
		down(&mutex);
		
		remove_item();
		print_buffer();
		
		up(&mutex);
		up(&empty);
	}
}

int main(){
	pthread_t prod, cons; //dichiarazione dei thread
	
	//inizializzazione dei semafori
	sem_init(&mutex, 0, 1); //il secondo campo indica chi può vedere e usare questo semaforo
	//0=codiviso solo tra thread dello stesso processo
	sem_init(&empty, 0, N); //il terzo campo è il val inziale del semaforo
	sem_init(&full, 0, 0);
	
	//creazione dei thread con associata la loro funzione
	pthread_create(&prod, NULL, producer, NULL);
	pthread_create(&cons, NULL, consumer, NULL);
	
	//attesa della terminazione dei thread
	pthread_join(prod, NULL);
	pthread_join(cons, NULL);

	//distruzione dei semafori
	sem_destroy(&mutex);
	sem_destroy(&empty);
	sem_destroy(&full);
	
}

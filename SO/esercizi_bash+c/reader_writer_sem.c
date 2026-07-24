#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <semaphore.h>

#define TRUE 1
#define NUM_READERS 3

sem_t mutex; //semaforo per accesso esclusivo ad rc
sem_t db; //semaforo accesso esclusivo al database
int rc=0; //numero di processi che leggono o vogliono leggere

void down(sem_t *sem){
	sem_wait(sem);
}

void up(sem_t *sem){
	sem_post(sem);
}

void read_database(){
	printf("Leggendo dal database...\n");
	sleep(1);
}

void write_database(){
	printf("Scrivendo dal database...\n");
	sleep(1);
}

void use_data_read(){
	printf("Utilizzando i dati letti...\n");
	sleep(1);
}

void think_up_data(){
	printf("Pensando ai dati da scrivere...\n");
	sleep(1);
}

void *reader(void *arg){
	while(TRUE){
		down(&mutex); //accesso ad rc
		rc++;

		if(rc==1){ //se è il primo lettore, blocca accesso al db
			down(&db);
		}
		
		up(&mutex); //rilascia accesso esclusivo ad rc
		read_database();//legge dal database
		down(&mutex);//ottiene accesso esclusivo ad rc
		rc--;

		if(rc==0){
			up(&db);
		}
		
		up(&mutex);
		use_data_read();
	}
}

void *writer(void *arg){
	while(TRUE){
		think_up_data(); //simulazione di elaboraz. scrittura dati
		down(&db); //ottiene accesso esclusivo al database
		write_database(); //scrive nel database
		up(&db);
	}
}

int main(){
	pthread_t readers[NUM_READERS], writer_thread;
	sem_init(&mutex, 0, 1);
	sem_init(&db, 0, 1);

	//creazione degli n lettori
	for(int i=0; i<NUM_READERS; i++){
		pthread_create(&readers[i], NULL, reader, NULL);
	}
	
	pthread_create(&writer_thread, NULL, writer, NULL);

	//join dei lettori
	for(int i=0; i<NUM_READERS; i++){
		pthread_join(&readers[i], NULL);
	}

	pthread_join(writer_thread, NULL);
	
	sem_destroy(&mutex);
	sem_destroy(&db);

}

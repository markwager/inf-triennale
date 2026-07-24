#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

#define MAX 10 //quantità di numeri da produrre

pthread_mutex_t the_mutex;
pthread_cond_t condc, condp;
//variabili condizionali + semaforo

int buffer=0; //buffer usato tra produttore e consumatore

void *producer(void *ptr){
	int i;
	for(i=1; i<=MAX; i++){
		pthread_mutex_lock(&the_mutex);
		while (buffer != 0) {
            		pthread_cond_wait(&condp, &the_mutex);
        	}
		
		buffer = i;  /* Inserisce l'elemento nel buffer */
        	printf("Producing:\t%d\n", i);
        	sleep(rand()%2);
        	pthread_cond_signal(&condc);  /* Sveglia il consumatore */
        	pthread_mutex_unlock(&the_mutex);  /* Rilascia l'accesso al buffer */		
	}
	pthread_exit(0);
}
	
void *consumer(void *ptr){
	int i;
	for(i=1; i<=MAX; i++){
		pthread_mutex_lock(&the_mutex);
		
		while(buffer==0){
			pthread_cond_wait(&condc, &the_mutex);
		}
		 printf("Consuming:\t%d\n", i);
        	buffer = 0;  /* Preleva un elemento dal buffer e lo reinizializza */
        	sleep(rand()%2);
        	pthread_cond_signal(&condp);  /* Sveglia il produttore */
        	pthread_mutex_unlock(&the_mutex);  /* Rilascia l'accesso al buffer */


	}
	pthread_exit(0);
}

int main(){
	pthread_t pro, con;
	
	//inizializzazione di mutex e var cond
	pthread_mutex_init(&the_mutex, NULL);
	pthread_cond_init(&condc, NULL);
	pthread_cond_init(&condp, NULL);

	//creazione dei threads
	 pthread_create(&con, NULL, consumer, NULL);
   	 pthread_create(&pro, NULL, producer, NULL);

    	/* Attesa che i threads completino l'esecuzione */
    	pthread_join(pro, NULL);
    	pthread_join(con, NULL);

    	/* Pulizia e distruzione di mutex e variabili condizionali */
    	pthread_cond_destroy(&condc);
    	pthread_cond_destroy(&condp);
    	pthread_mutex_destroy(&the_mutex);

}

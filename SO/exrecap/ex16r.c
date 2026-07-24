#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <time.h>

#define READERS 5
#define N 10

pthread_t wr;
pthread_t rd[READERS];
sem_t mutex; //semaforo per accesso esclusivo a rc
sem_t arr; //sem per accesso escusivo ad array
int rc=0;
int buffer[N];

void down(sem_t *sem){
	sem_wait(sem);
}

void up(sem_t *sem){
	sem_post(sem);
}

void *writer(void *arg){
	while(1){
	down(&arr);
	for(int i=0; i<N; i+=2){
		int num=((rand()%25)*2)+1;
		buffer[i]=num;
		printf("Inserito num %d in pos pari\n", i);
	}
	
	for(int i=1; i<N; i+=2){
                int num=50+(rand()%25)*2;
                buffer[i]=num;
		printf("Inserito num %d in pos dispari\n", i);
        }

	up(&arr);
	sleep(2);
	}
}

void *readers(void *arg){
	while(1){
		down(&mutex);
		rc++;
		if(rc==1){
			down(&arr);
		}
		up(&mutex);
		for(int i=0; i<N; i++){
			printf("Letta coppia %d,%d\n", buffer[i], buffer[i+1]);
		}
		down(&mutex);
		rc--;
		if(rc==0){
			up(&arr);
		}

		up(&mutex);
		sleep(2);
	}
}


int main(){

srand(time(NULL));
sem_init(&mutex, 0, 1);
sem_init(&arr, 0, 1);

for(int i=0; i<READERS; i++){
	pthread_create(&rd[i], NULL, &readers, NULL);
}

pthread_create(&wr, NULL, &writer, NULL);

for(int i=0; i<READERS; i++){
        pthread_join(rd[i], NULL);
}

pthread_join(wr, NULL);

sem_destroy(&mutex);
sem_destroy(&arr);

}

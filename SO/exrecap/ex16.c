#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>
#include <time.h>

#define NUM_READERS 5
#define N 10

sem_t mutex; //semaforo per l'accesso esclusivo a rc
sem_t arr; //semaforo per l'accesso esclusivo all'array
pthread_t writer;
pthread_t readers[NUM_READERS];
int rc=0;
int buffer[N];

void down(sem_t *sem){
	sem_wait(sem);
}

void up(sem_t *sem){
	sem_post(sem);
}

void *rd(void *arg){
	while(1){
		down(&mutex);
		rc++;
		if(rc==1){
			down(&arr);
		}
		up(&mutex);
		for(int i=0; i<N; i++){
			printf("Leggo l'elemento %d\n", buffer[i]);
		}
		down(&mutex);
		rc--;
		if(rc==0){
                        up(&arr);
                }
		up(&mutex);
		usleep(300000);
	}
}

void *wr(void *arg){
	while(1){
		down(&arr);
		int num1=(rand()%25)*2+1;
		for(int i=0; i<N; i+=2){
			buffer[i]=num1;
		}

		int num2=50+((rand()%26)*2);
		for(int i=1; i<N; i+=2){
			buffer[i]=num2;
		}
		up(&arr);
	}
}


int main(){

srand(time(NULL));
sem_init(&mutex, 0, 1);
sem_init(&arr, 0, 1);
int status;

for(int i=0; i<NUM_READERS; i++){
	pthread_create(&readers[i], NULL, &rd, NULL);
}

pthread_create(&writer, NULL, &wr, NULL);

for(int i=0; i<NUM_READERS; i++){
        pthread_join(readers[i], NULL);
}

pthread_join(writer, NULL);

sem_destroy(&mutex);
sem_destroy(&arr);

}

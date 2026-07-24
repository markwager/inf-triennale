#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore>
#include <time.h>

#define N 10

sem_t mutex;
sem_t full;
sem_t empty;

pthread_t prod;
pthread_t cons;

void *down(sem_t *sem){
	sem_wait(sem);
}

void *up(sem_t *sem){
	sem_post(sem);
}

void *produttore(void *arg){
	while(1){
		down(&empty);
		down(&mutex);
		int num1=rand()%101;
		for(int i=0; i<N; i+=2){
			buffer[i]=num1;
		}
		int num2=100+(rand()%101);
                for(int i=1; i<N; i+=2){
                        buffer[i]=num1;
                }
		up(&mutex);
		up(&full);
		sleep(2);
	}
}

void *consumatore(void *arg){
        while(1){
                down(&full);
                down(&mutex);
		int somma=0
                for(int i=0; i<N; i++){
                        somma=buffer[i]+buffer[i+1];
                }
                up(&mutex);
                up(&full);
                sleep(2);
        }
}


int main(){

sem_init(&mutex, 0, 1);
sem_init(&full, 0, 0);
sem_init(&empty, 0, N);

pthread_create(&prod, NULL, produttore, NULL);
pthread_create(&cons, NULL, consumatore, NULL);

for(i=0; i<N; i++){
	buffer[i]=0;
}


pthread_join(prod, NULL);
pthread_join(cons, NULL);

sem_destroy(&mutex);
sem_destroy(&full);
sem_destroy(&empty);

}

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>
#include <time.h>

#define N 10

pthread_t prod;
pthread_t cons;
sem_t mutex;
sem_t empty;
sem_t full;
int buffer[N];

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
                        buffer[i]=num2;
                }
		up(&mutex);
		up(&full);
	}
}


void *consumatore(void *arg){
        while(1){
		int coppia;
                down(&full);
                down(&mutex);
                for(int i=0; i<N-1; i++){
                        coppia=buffer[i]+buffer[i+1];
                }
		printf("La somma è %d\n", coppia);
                up(&mutex);
                up(&empty);
        }
}


int main(){
srand(time(NULL));

sem_init(&mutex, 0, 1);
sem_init(&full, 0, 0);
sem_init(&empty, 0, N);

pthread_create(&prod, NULL, produttore, NULL);
pthread_create(&cons, NULL, consumatore, NULL);

for(int i=0; i<N; i++){

        buffer[i]=-1;
}

pthread_join(prod, NULL);
pthread_join(cons, NULL);

sem_destroy(&mutex);
sem_destroy(&full);
sem_destroy(&empty);

}

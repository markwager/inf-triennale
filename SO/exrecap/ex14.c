 #include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <semaphore.h>

#define N 10

sem_t mutex;
sem_t empty;
sem_t full;

int buffer[N];

void down(sem_t *sem){
        sem_wait(sem);
}


void up(sem_t *sem){
        sem_post(sem);
}


void producer(void *arg){

        while(1){
                down(&empty);
                down(&mutex);
                int num=(rand()%100)*2;
                for(int i=0; i<N; i+=2){
                        buffer[i]=num;
                }
                up(&muetx);
                up(&full);
        }
}


void consumer(void *arg){
        while(1){
                down(&full);
                down(&mutex);
                int num=((rand()%101)+100)*3;
                for(int i=1; i<N; i+=2){
                        buffer[i]=num;
                }
                up(&mutex);
                up(&empty);
        }
}

int main(){

pthread_t prod, cons;
sem_init(&mutex, 0, 1);
sem_init(&empty, 0, N);
sem_init(&full, 0, 0);

pthread_create(&prod, NULL, producer, NULL);
pthread_create(&cons, NULL, consumer, NULL);

for(int i=0; i<N; i++){
        buffer[i]=-1;
}

pthread_join(prod, NULL);
pthread_join(cons, NULL);

sem_destroy(&mutex);
sem_destroy(&empty);
sem_destroy(&full);


}

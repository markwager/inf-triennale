#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <sys/wait.h>
#include <pthread.h>
#include <semaphore.h>

#define N 10

pthread_t th1, th2, th3;
sem_t mutex, sem_pari, sem_dispari;
int finito=0;

void down(sem_t *sem){
	sem_wait(sem);
}

void up(sem_t *sem){
	sem_post(sem);
}

void *task1(void *arg){
	while(finito!=1){
		down(&mutex);
		int num=rand()%101;
		for(int i=0; i<N; i+=2){
			buffer[i]=num;
		}
		up(&mutex);
		up(&sem_pari);
	}
	pthread_exit(NULL);
}

void *task2(void *arg){
        while(finito!=1){
                down(&mutex);
                int num=100+(rand()%101);
                for(int i=1; i<N; i+=2){
                        buffer[i]=num;
                }
                up(&mutex);
                up(&sem_dispari);
        }
        pthread_exit(NULL);
}

void *task3(void *arg){
        while(1){
                down(&sem_pari);
                down(&sem_dispari);
		down(&mutex);
                buffer[0]=buffer[0];
		buffer[1]=buffer[0]+buffer[1];
		buffer[2]=buffer[1]+buffer[2];
		finito=1;
                up(&mutex);
        }
        pthread_exit(NULL);
}


int main(){
srand(time(NULL));

for(int i=0; i<N; i++){
	buffer[i]=-1;
}

sem_init(&mutex, 0, 1);
sem_init(&full, 0, 0);
sem_init(&empty, 0, N);

pthread_create(&th1, NULL, task1, NULL);
pthread_create(&th2, NULL, task2, NULL);
pthread_create(&th3, NULL, task3, NULL);

pthread_join(th1, NULL);
pthread_join(th2, NULL);
pthread_join(th3, NULL);

sem_destroy(&mutex, NULL);
sem_destroy(&full, NULL);
sem_destroy(&empty, NULL);

}

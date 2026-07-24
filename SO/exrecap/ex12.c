#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>
#include <semaphore.h>
#include <pthread.h>

#define N 10
int buffer[N];
sem_t mutex;
pthread_t th1, th2, th3;

void down(sem_t *sem){
	sem_wait(sem);
}

void up(sem_t *sem){
	sem_post(sem);
}

void *task1(void *arg){
	while(1){
		down(&mutex);
		for(int i=0; i<N; i+=2){
			if(buffer[i]!=-1){
				int num=rand()%101;
				buffer[i]=num;
				printf("Ho inserito nel buffer %d\n", buffer[i]);
			}
		}
		up(&mutex);
	}
}

void *task2(void *arg){
        while(1){
                down(&mutex);
                for(int i=1; i<N; i+=2){
                        if(buffer[i]!=-1){
                                int num=(rand()%101)+100;
                                buffer[i]=num;
                                printf("Ho inserito nel buffer %d\n", buffer[i]);
                        }
                }
                up(&mutex);
        }
}

void *task3(void *arg){
        while(1){
                down(&mutex);
                for(int i=1; i<N; i++){
                        buffer[i]+=buffer[i-1];
                        printf("Ho modificato gli elementi nel buffer %d\n", buffer[i]);
                }
                up(&mutex);
		exit(0);
        }
}

int main(){

srand(time(NULL));
sem_init(&mutex, 0 , 1);
for(int i = 0; i < N; i++) buffer[i] = -1;
pthread_create(&th1, NULL, task1, NULL);
pthread_create(&th2, NULL, task2, NULL);
pthread_create(&th3, NULL, task3, NULL);

pthread_join(th1, NULL);
pthread_join(th2, NULL);
pthread_join(th3, NULL);

sem_destroy(&mutex);

}

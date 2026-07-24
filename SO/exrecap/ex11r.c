#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <semaphore.h>
#include <pthread.h>
#include <stdlib.h>

#define N 11

int buffer[N];

pthread_t th1;
pthread_t th2;
pthread_t th3;

sem_t mutex;

void down(sem_t *sem){
	sem_wait(sem);
}

void up(sem_t *sem){
	sem_post(sem);
}

void *task1(void *arg){
	while(1){
		down(&mutex);
		int index=rand()%N;
		buffer[index]=1;
		printf("Scrivo 1\n");
		up(&mutex);
		sleep(rand()%4);
	}
}

void *task2(void *arg){
	while(1){
		down(&mutex);
                int index=rand()%N;
                buffer[index]=-1;
		printf("Scrivo -1\n");
                up(&mutex);
		sleep(rand()%4);
	}
}

void *task3(void *arg){
	while(1){
		int occup=0;
		int c_pos=0;
		int c_neg=0;
		down(&mutex);
		for(int i=0; i<N; i++){
			if(buffer[i]!=0){
				occup++;

				if(buffer[i]==1){
                                	c_pos++;
                        	}

				if(buffer[i]==-1){
                               		c_neg++;
                        	}
			}
		}

		if(occup==N){
			if(c_pos>c_neg){
				printf("Gli 1 sono di più dei -1: cancello i thread\n");
				pthread_cancel(th1);
				pthread_cancel(th2);
				up(&mutex);
				return NULL;
			}
		}
		up(&mutex);
		sleep(rand()%4);
	}
}



int main(){

srand(time(NULL));
    for(int i = 0; i < N; i++) buffer[i] = 0;
sem_init(&mutex, 0, 1);
pthread_create(&th1, NULL, task1, NULL);
pthread_create(&th2, NULL, task2, NULL);
pthread_create(&th3, NULL, task3, NULL);

pthread_join(th1, NULL);
pthread_join(th2, NULL);
pthread_join(th3, NULL);

sem_destroy(&mutex);

}

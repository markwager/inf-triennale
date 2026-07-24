#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>

#define N 10
int buffer[N]
pthread_t th1;
pthread_t th2;
pthread_t th3;
pthread_mutex_t mutex;
int finito=0;

void *task1(void *arg){
	while(1){
		pthread_mutex_lock(&mutex);
		if(finito){
			pthread_mutex_unlock(&mutex);
			pthread_exit(NULL);
		}
		for(int i=0; i<N; i+=2){
			buffer[i]=rand()%101;
		}
		pthread_mutex_unlock(&mutex);
	}
	pthread_exit(NULL);
}

void *task2(void *arg){
        while(1){
                pthread_mutex_lock(&mutex);
                if(finito){
                        pthread_mutex_unlock(&mutex);
                        pthread_exit(NULL);
                }
                for(int i=1; i<N; i+=2){
                        buffer[i]=100+(rand()%101);
                }
                pthread_mutex_unlock(&mutex);
        }
        pthread_exit(NULL);
}

void *task3(void *arg){
        while(1){
                pthread_mutex_lock(&mutex);
		if (buffer[0] != -1 && buffer[1] != -1 && buffer[2] != -1) {
                	buffer[0]=buffer[0];
			buffer[1]=buffer[1]+buffer[0];
			buffer[2]=buffer[1]+buffer[2];
			finito=1;
			pthread_mutex_unlock(&mutex);
			pthread_exit(NULL);
		}
        }
        pthread_mutex_unlock(&mutex);
}


int main(){

srand(time(NULL));

for(int i=0; i<N; i++){
	buffer[i]=-1;
}

pthread_mutex_init(&mutex, NULL);
pthread_create(&th1, NULL, task1, NULL);
pthread_create(&th2, NULL, task2, NULL);
pthread_create(&th3, NULL, task3, NULL);

pthread_join(th1, NULL);
pthread_join(th2, NULL);
pthread_join(th3, NULL);

pthread_mutex_destroy(&mutex);

}

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>

#define N 10

pthread_t th1;
pthread_t th2;
pthread_t th3;
int num1, num2;

pthread_mutex_t mutex;

int buffer[N];

void *task1(void *arg){
	while(1){
		pthread_mutex_lock(&mutex);
		num1=rand()%101;
		for(int i=0; i<N; i+=2){
printf("sono t1 sto stampando %d in posizione %d\n", num1, i);
			buffer[i]=num1;
		}
		pthread_mutex_unlock(&mutex);
		sleep(3);
	}
	pthread_exit(NULL);
}

void *task2(void *arg){
        while(1){
                pthread_mutex_lock(&mutex);
                num2=100+(rand()%101);
                for(int i=1; i<N; i+=2){
printf("sono t2 sto stampando %d in posizione %d\n", num2, i);
                        buffer[i]=num2;
                }
                pthread_mutex_unlock(&mutex);
		sleep(3);
        }
        pthread_exit(NULL);
}


void *task3(void *arg){
        while(1){
                pthread_mutex_lock(&mutex);
                buffer[0]=buffer[0];
		buffer[1]=buffer[1]+buffer[0];
		buffer[2]=buffer[2]+buffer[1];
                pthread_mutex_unlock(&mutex);
		sleep(3);
        }
        pthread_exit(NULL);
}




int main(){

srand(time(NULL));
pthread_mutex_init(&mutex, NULL);

pthread_create(&th1, NULL, task1, NULL);
pthread_create(&th2, NULL, task2, NULL);
pthread_create(&th3, NULL, task3, NULL);

for(int i=0; i<N; i++){
	buffer[i]=-1;
}


pthread_join(th1, NULL);
pthread_join(th2, NULL);
pthread_join(th3, NULL);

pthread_mutex_destroy(&mutex);

}

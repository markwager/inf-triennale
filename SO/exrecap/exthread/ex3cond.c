#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>

#define N 10

pthread_t th1, th2, th3;
pthread_mutex_t mutex;
pthread_cond_t condc;
int buff1[N];
int buff2[N];
int count1=0;
int count2=0;
int pos, neg;
int min1=buff1[0];
int min2=buff2[0];
int mass1=buff1[0];
int mass2=buff2[0];
int mins, maxs;

void *task1(void *arg){
	while(1){
		pthread_mutex_lock(&mutex);
		int num=(rand()%151)+1;
		int index=rand()%N;
		buffer[index]=num;
		count1++;
		pthread_cond_signal(&condc);
		pthread_mutex_unlock(&mutex);
	}
	pthread_exit(NULL);
}

void *task2(void *arg){
        while(1){
                pthread_mutex_lock(&mutex);
                int num=(rand()%151)+150;
                int index=rand()%N;
                buffer[index]=num;
		count2++;
                pthread_cond_signal(&condc);
                pthread_mutex_unlock(&mutex);
        }
        pthread_exit(NULL);

}

void *task3(void *arg){
        while(1){
                pthread_mutex_lock(&mutex);
                if(count1<N && count2<N){
			pthread_cond_wait(&condc, &mutex);
		}
		for(int i=0; i<N; i++){
			if(buff1[i]<min1){
				min1=buff1[i];
			}
			if(buff2[i]<min2){
                                min2=buff2[i];
                        }
			if(buff1[i]>max1){
                                max1=buff1[i];
                        }
                        if(buff2[i]>max2){
                                max2=buff2[i];
                        }
		}

		if(max1>max2){
			maxs=max1;
		}
		if(max2>max1){
                        maxs=max2;
                }

		if(min1<min2){
                        mins=min1;
                }
                if(min2<min1){
                        mins=min2;
                }

                pthread_mutex_unlock(&mutex);
        }
        pthread_exit(NULL);

}


int main(){
srand(time(NULL));

for(int i=0; i<N; i++){
	buff1[i]=0;
}

for(int i=0; i<N; i++){
        buff2[i]=0;
}

pthread_mutex_init(&mutex);
pthread_create(&th1, NULL, task1, NULL);
pthread_create(&th2, NULL, task2, NULL);
pthread_create(&th3, NULL, task3, NULL);

pthread_join(th1, NULL);
pthread_join(th2, NULL);
pthread_join(th3, NULL);

pthread_mutex_destroy(&mutex);

}

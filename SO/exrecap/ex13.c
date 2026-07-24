#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>
#include <time.h>

#define N 10
sem_t mutex;
pthread_t th1, th2, th3;
int buff1[N];
int buff2[N];
int max1=0;
int min1=1000;
int max2=0;
int min2=1000;
int maxf, minf;

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
		if(buff1[index]==0){
			int num=(rand()%150)+1;
			buff1[index]=num;
		}
		up(&mutex);
	}
}

void *task2(void *arg){
        while(1){
                down(&mutex);
                int index=rand()%N;
		if(buff2[index]==0){
                	int num=(rand()%151)+150;
                	buff2[index]=num;
		}
		up(&mutex);
        }
}

void *task3(void *arg){
        while(1){
                down(&mutex);
                for(int i=0; i<N; i++){
			if(buff1[i]!=0 && buff2[i]!=0){
				if(buff1[i]>max1){
					max1=buff1[i];
				}
				
				if(buff1[i]<min1){
                                        min1=buff1[i];
                                }

				if(buff2[i]>max2){
                                        max2=buff2[i];
                                }

                                if(buff2[i]<min2){
                                        min2=buff2[i];
                                }
			}
		}
		if(max1>max2){
			maxf=max1;
		}
		
		if(max1<max2){
			maxf=max2;
		}
		
		if(min1<min2){
                        minf=min1;
                }
                
                if(min1>min2){
                        minf=min2;
                }

		up(&mutex);
        }
}




int main(){
srand(time(NULL));
sem_init(&mutex, 0 ,1);

for(int i=0; i<N; i++){
	buff1[i]=0;
	buff2[i]=0;
}

pthread_create(&th1, NULL, task1, NULL);
pthread_create(&th2, NULL, task2, NULL);
pthread_create(&th3, NULL, task3, NULL);

pthread_join(th1, NULL);
pthread_join(th2, NULL);
pthread_join(th3, NULL);

sem_destroy(&mutex);

}

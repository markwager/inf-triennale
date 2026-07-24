#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>
#include <ctype.h>
#include <string.h>

#define N 10

char stringa[N]="ciaosonval";
int i=0;
sem_t mutex;

void down(sem_t *sem){
	sem_wait(sem);
}

void up(sem_t *sem){
	sem_post(sem);
}

void *print_task(void *arg){
	while(1){
		down(&mutex);
		printf("Stampo il carattere %c\n", toupper(stringa[i]));
		i=(i+1)%(N);
		up(&mutex);
	}
}

int main(){

sem_init(&mutex, 0, 1);

pthread_t threads[N/2];

for(int i=0; i<N/2; i++){
	int status=pthread_create(&threads[i], NULL, print_task, NULL);
}
for(int i=0; i<N/2; i++){
	pthread_join(threads[i], NULL);
}

sem_destroy(&mutex);


}

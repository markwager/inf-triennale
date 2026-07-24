#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <ctype.h>
#include <string.h>

#define N 4
char *parola="sos";
pthread_t th[N/2];
pthread_mutex_t mutex;
int i=0;

void *task(void *arg){
	pthread_mutex_lock(&mutex);
	if(i<strlen(parola)){
	printf("La lettera è %c\n", toupper(parola[i]));
	i++;
	}
	pthread_mutex_unlock(&mutex);
	pthread_exit(NULL);
}


int main(){

pthread_mutex_init(&mutex, NULL);

for(int i=0; i<(N/2); i++){
	pthread_create(&th[i], NULL, task, NULL);
}

for(int i=0; i<(N/2); i++){
        pthread_join(th[i], NULL);
}

pthread_mutex_destroy(&mutex);

}

#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

void alarm_handler(int);

void alarm_handler(int signal){
	printf("In signal handler: caught signal %d che è %s\n", signal, strsignal(signal));
	exit(0);
}

int main(int argc, char *argv[]){
	signal(SIGALRM, alarm_handler); //sigalrm è un segnale che notifica a un processo lo scadere di un timer
	alarm(1); //timer di 1 sec

	while(1){
		printf("I am running!\n");
	}
}

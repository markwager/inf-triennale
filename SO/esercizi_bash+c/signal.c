#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>

void sigHandler(int signum){
	printf("Il segnale di interrupt %d ricevuto è %s\n", signum, strsignal(signum));
	exit(signum); //comunica che il programma è stato interroro per il segnale
}

int main(){

signal(SIGINT, sigHandler);

while(1){
	printf("Buonanotte...ZzzzZ...");
	sleep(1);
}

}

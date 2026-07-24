#include <stdio.h>
#include <unistd.h>
#include <stdlib.h> //exit
#include <signal.h> //per i diversi segnali
#include <string.h> //strsignal

void signalHandler(int signum){
	printf("Segnale di interrupt %d ricevuto che è %s\n", signum, strsignal(signum));
	//converte un numero di segnale in una descrizione testuale leggibile dall'uomo
	exit(signum);
}

int main(){
	signal(SIGINT, signalHandler); //ctrl-c

	while(1){
		printf("Vado a dormì\n");
		sleep(1);
	}

}

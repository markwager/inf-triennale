#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>

void alarm_handler(int signum){
	printf("Ho ricevuto %d che è %s\n", signum, strsignal(signum));
	exit(0);
}

int main(){
	signal(SIGALRM, alarm_handler);

	while(1){
		printf("Sono in esecuzione");
	}
}

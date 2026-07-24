#include <stdio.h>
#include <unistd.h> //per fork, exec, sleep
#include <sys/wait.h>

int main(){

	int pid, child_status;
	char *args[]={"/bin/ls", "-l", NULL}; //argomenti da passare al programma
	if(fork()==0){
		execv(args[0],args); //fornisce percorso completo di ls (programma)
					//e a destra ci sono gli argomenti
	}

	else{
		wait(&child_status);

	}



}

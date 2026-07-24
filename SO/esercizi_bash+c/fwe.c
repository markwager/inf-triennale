#include <stdio.h>
#include <unistd.h> //serve per fork, exec (e altri), sleep, write, read, pipe, close, dup
#include <stdlib.h> //serve per exit
#include <sys/wait.h>

int main(int argc, char *argv[]){
		
	int status;
	pid_t pid;
		
	pid=fork();
	if(pid==0){
		execvp(argv[1],&argv[1]);
	        exit(1);
	}
		
	else if(pid>0){
		wait(&status); //processo padre è bloccato fintanto che non
				//finisce il figlio
	}
		
	else{
		return -1;
	}
}

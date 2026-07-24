#include <stdio.h> 
#include <stdlib.h> //exit
#include <unistd.h>  //fork, execv, pipe
#include <sys/wait.h> //wait, waitpid

int main(){
	int pid, child_status;
	pid=fork();
	if(pid==0){
		printf("frocio, so er fijo\n");
	}

	else{
		wait(&child_status);
		printf("stronzo, so er genitore\n");
	}

}

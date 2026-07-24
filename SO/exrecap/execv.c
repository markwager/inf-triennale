#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){

	int pid, child_status;
	pid=fork();
	char *args[]={"/bin/ls", "-l", NULL};

	if(pid==0){
		execv(args[0], args);
	}

	else{
		wait(&child_status);
	}
}

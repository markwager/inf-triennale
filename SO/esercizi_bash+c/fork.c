#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

#define STDIN 0
#define STDOUT 1
#define PIPE_RD 0
#define PIPE_WR 1

void fork1();
void fork2();

void fork1(){

int pid, child_status;
if((pid=fork())==0){
	printf("Sono il bimbo e vedo il pid %d\n", pid);
}

else{
	wait(&child_status);
	printf("So er genitore, vedo il pid del bimbo %d e lo status suo %d", pid, child_status);
}

}

void fork2(){

pid_t catpid, sortpid; //questi sono i pid dei due processi figli
int fd[2]; //descrittori di file: lettura[0] e scrittura[1]
pipe(fd); //crea una pipe con i due descrittori

catpid=fork();

if(catpid==0){
close(fd[PIPE_RD]);
close(fd[STDOUT]);

dup(fd[PIPE_WR]);
execl("/bin/cat", "cat", "names.txt", NULL);

}

sortpid=fork();

if(sortpid==0){
close(fd[PIPE_WR]);
close(fd[STDIN]);

dup(fd[PIPE_RD]);
execl("/usr/bin/sort", "sort", NULL);

}

//qui entra in gioco il processo genitore:
close(fd[PIPE_WR]);
close(fd[PIPE_RD]);

waitpid(catpid, NULL, 0);
waitpid(sortpid, NULL, 0);

}


int main(){

fork1();
fork2();

}

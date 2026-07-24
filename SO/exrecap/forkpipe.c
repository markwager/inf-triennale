#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

#define STDIN 0
#define STDOUT 1
#define PIPE_RD 0 //lato lettura pipe
#define PIPE_WR 1 //lato scrittura pipe

int main(){

pid_t cat_pid, sort_pid;
int fd[2]; //descrittori di file per la pipe: fd[0] per leggere e fd[1] per scrivere
pipe(fd); //creazione pipe

cat_pid=fork();
if(cat_pid==0){
close(fd[PIPE_RD]); //chiude estremità di lettura di pipe
close(STDOUT); //chiude output standard
dup(fd[PIPE_WR]);
execl("/bin/cat", "cat", "forkpipe.c", NULL); //percorso completo, nome del programma, 
					//argomenti sucessivi, NULL
}

sort_pid=fork();
if(sort_pid==0){
close(fd[PIPE_WR]);
close(STDIN);
dup(fd[PIPE_RD]);
execl("/usr/bin/sort", "sort", NULL);
}

//il processo genitore chiude le estremità della pipe
close(fd[PIPE_RD]);
close(fd[PIPE_WR]);

waitpid(cat_pid, NULL, 0);
waitpid(sort_pid, NULL, 0);

}

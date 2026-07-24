#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/wait.h>

#define STDIN 0
#define STDOUT 1

#define PIPE_RD 0
#define PIPE_WR 1


void outfile();
void pipex();

void outinfile(){

int file_fd=open("output.txt", O_WRONLY | O_CREAT, 0644);
dup2(file_fd, STDOUT_FILENO);
printf("Questo va in output.txt\n");
close(file_fd);
//mette printf in file invece che su terminale (STDOUT)
}

void pipex(){

    pid_t cat_pid, sort_pid;
    int fd[2];
    pipe(fd);

    cat_pid = fork();
    if (cat_pid == 0) {
        close(fd[PIPE_RD]);
        close(STDOUT);
        dup(fd[PIPE_WR]);
        execl("/bin/cat", "cat", "parole.txt", NULL); //duplica questo fd e lo reindirizza alfd chiuso più vicino STDWR (=dup2(PIPE_WR,STDOUT))
    }

    sort_pid = fork();
    if(sort_pid==0){
        close(fd[PIPE_WR]);
        close(STDIN);
        dup(fd[PIPE_RD]); //duplica questo fd e lo reindirizza alfd chiuso più vicino STDIN (=dup2(PIPE_RD,STDIN))
        execl("/usr/bin/sort", "sort", NULL);
    }

    close(fd[PIPE_RD]);
    close(fd[PIPE_WR]);

    /* wait for children to finish */
    waitpid(cat_pid, NULL, 0);
    waitpid(sort_pid, NULL, 0);
    //così il padre raccoglie lo stato dei figli
    //se non usassimo waitpid si creerebbero se processi zombie: stanno ancora nella tabella dei processi

    //questo codice esegue cat parole.txt | sort
}

/*
non possiamo saltare i due close di pipe dei due if perchè:
1)altrimenti il processo figlio di scrittura rimarrebbe bloccato
2)al processo figlio di lettura non arriverebbe mai l'EOF per fare la lettura
3)si chiude inoltre il primo fd di pipe (lettura) per evitare eventuali letture accidentali
4)si chiudono gli fd originali (in tutti e due gli if) affinchè si possa garantire la lettura/scrittura nella pipe
5)dopo fork, il padre dovrebbe chiudere entrambe le estremità della pipe
*/

int main(){

outinfile();
pipex();

}

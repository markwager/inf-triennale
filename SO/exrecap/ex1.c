#include <stdio.h>
#include <stdlib.h> //exit, malloc, free
#include <unistd.h> //pipe, fork, write, close, read
#include <signal.h>
#include <sys/wait.h>
#include <time.h> //rand e srand

#define PIPE_RD 0
#define PIPE_WR 1

int main(){
srand(time(NULL));
int n1, n2, somma=0;
pid_t p1,p2;
int fd1[2];
int fd2[2];
pipe(fd1);
pipe(fd2);

p1=fork();
if(p1==0){
	close(fd1[PIPE_RD]);
	close(fd2[PIPE_RD]);
	while(1){
		n1=rand()%100;
		if(n1%2>0){
			write(fd1[PIPE_WR], &n1, sizeof(int));
		}
		sleep(5);
	}
	exit(0);
}


p2=fork();
if(p2==0){
        close(fd2[PIPE_RD]);
	close(fd1[PIPE_RD]);
        while(1){
                n2=rand()%100;
                if(n2%2==0){
                        write(fd2[PIPE_WR], &n2, sizeof(int));
                }
		sleep(5);
        }
	exit(0);
}

close(fd1[PIPE_WR]);
close(fd2[PIPE_WR]);

while(1){
	read(fd1[PIPE_RD], &n1, sizeof(int));
	read(fd2[PIPE_RD], &n2, sizeof(int));
	somma=n1+n2;
	printf("P1: %d, P2: %d | Somma: %d\n", n1, n2, somma);
	if(somma==190){
		break;
	}
}

kill(p1, SIGTERM);
kill(p2, SIGTERM);
waitpid(p1, NULL, 0);
waitpid(p2, NULL, 0);

printf("Processi terminati.\n");

}
	

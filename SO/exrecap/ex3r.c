#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <time.h>
#include <signal.h>

#define PIPE_RD 0
#define PIPE_WR 1

int main(){

srand(time(NULL));
pid_t p1;
pid_t p2;
int fd1[2], fd2[2];
pipe(fd1);
pipe(fd2);

p1=fork();
if(p1<0){
	printf("Errore processo p1\n");
}
if(p1==0){
	close(fd1[PIPE_RD]);
	close(fd2[PIPE_WR]);
	close(fd2[PIPE_RD]);
	while(1){
		int num=rand()%100;
		if(num%2==0){
			write(fd1[PIPE_WR], &num, sizeof(int));
		}
	}
	exit(0);
}

p2=fork();
if(p2<0){
        printf("Errore processo p2");
}
if(p2==0){
        close(fd2[PIPE_RD]);
        close(fd1[PIPE_WR]);
        close(fd1[PIPE_RD]);
	while(1){
        	int num=rand()%100;
        	if(num%2!=0){
                	write(fd2[PIPE_WR], &num, sizeof(int));
        	}
	}
	exit(0);
}

close(fd1[PIPE_WR]);
close(fd2[PIPE_WR]);

int n1, n2;
int somma=0;

while(1){

	read(fd1[PIPE_RD], &n1, sizeof(int));
	read(fd2[PIPE_RD], &n2, sizeof(int));
	somma=n1+n2;
	printf("P1: %d, P2: %d | Somma: %d\n", n1, n2, somma);
	if(somma>190){
		break;
	}
}

kill(p1, SIGINT);
kill(p2, SIGINT);

waitpid(p1, NULL, 0);
waitpid(p2, NULL, 0);


}

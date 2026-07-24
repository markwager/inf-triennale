#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <time.h>

#define PIPE_RD 0
#define PIPE_WR 1

int main(){

int fd1[2];
int fd2[2];
pipe(fd1);
pipe(fd2);

srand(time(NULL));

pid_t proc1;
proc1=fork();

if(proc1==0){
	close(fd2[PIPE_RD]);
	close(fd2[PIPE_WR]);
	close(fd1[PIPE_RD]);
	while(1){
		int n=rand()%101;
		sleep(1);
		if(n%2==1){
			write(fd1[PIPE_WR], &n, sizeof(int));
		}
	}
}

pid_t proc2;
proc2=fork();

if(proc2==0){
	close(fd1[PIPE_RD]);
	close(fd1[PIPE_WR]);
	close(fd2[PIPE_RD]);
	while(1){
		int n=rand()%101;
		sleep(1);
		if(n%2==0){
			write(fd2[PIPE_WR], &n, sizeof(int));
		}
	}

}

close(fd1[PIPE_WR]);
close(fd2[PIPE_WR]);
int disp;
int pari;

while(1){

	read(fd1[PIPE_RD], &disp, sizeof(int));
	read(fd2[PIPE_RD], &pari, sizeof(int));
	int somma=disp+pari;
	printf("Somma %d+%d=%d\n", disp, pari, somma);

	if((somma)>100){
		printf("So arrivato\n");
		kill(proc1, SIGTERM);
		kill(proc2, SIGTERM);

		waitpid(proc1, NULL, 0);
		waitpid(proc2, NULL, 0);
		break;
	}

}

}

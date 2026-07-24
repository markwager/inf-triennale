#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include <sys/wait.h>


#define PIPE_RD 0
#define PIPE_WR 1


int main(){

srand(time(NULL));
int fd1[2], fd2[2];
pid_t p1,p2;
pipe(fd1);
pipe(fd2);

p1=fork();
if(p1==0){
	close(fd1[PIPE_RD]);
        close(fd2[PIPE_WR]);
        close(fd2[PIPE_RD]);

	while(1){
		int num=rand()%51;
		if(num%2==0){
			write(fd1[PIPE_WR], &num, sizeof(int));
		}
	}
	exit(0);
}

p2=fork();
if(p2==0){

	close(fd2[PIPE_RD]);
	close(fd1[PIPE_WR]);
	close(fd1[PIPE_RD]);
        while(1){
                int num=(rand()%51+100);
                if(num%3==0){
                        write(fd2[PIPE_WR], &num, sizeof(int));
                }
        }
	exit(0);
}

close(fd1[PIPE_WR]);
close(fd2[PIPE_WR]);

int num1=0;
int num2=0;

while(1){
	read(fd1[PIPE_RD], &num1, sizeof(int));
	read(fd2[PIPE_RD], &num2, sizeof(int));
	printf("Ho ricevuto da processo p1 con pid %d il num1 %d\n", p1, num1);
	printf("Ho ricevuto da processo p2 con pid %d il num2 %d\n", p2, num2);
	if(num1+num2>190){
		break;
	}

}

kill(p1, SIGTERM);
kill(p2, SIGTERM);

waitpid(p1, NULL, 0);
waitpid(p2, NULL, 0);

}

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>

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
if(p1==0){
	close(fd1[PIPE_RD]);
	close(fd2[PIPE_WR]);
	close(fd2[PIPE_RD]);
	while(1){
		int num=rand()%101;
		if(num%2==0){
			write(fd1[PIPE_WR], &num, sizeof(int));
			printf("P1 scrive %d\n", num);
		}
		sleep(2);
	}
	exit(0);
}



p2=fork();
if(p2==0){
        close(fd2[PIPE_RD]);
        close(fd1[PIPE_WR]);
        close(fd1[PIPE_RD]);
        while(1){
                int num=rand()%101;
                if(num%2!=0){
                        write(fd2[PIPE_WR], &num, sizeof(int));
                        printf("P2 scrive %d\n", num);
                }
                sleep(2);
        }
        exit(0);
}

close(fd1[PIPE_WR]);
close(fd2[PIPE_WR]);

int num1, num2;
while(1){
	read(fd1[PIPE_RD], &num1, sizeof(int));
	read(fd2[PIPE_RD], &num2, sizeof(int));
	if(num1+num2>190){
		break;
	}
}


waitpid(p1, NULL, 0);
waitpid(p2, NULL, 0);

}

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <time.h>

#define PIPE_RD 0
#define PIPE_WR 1

int main(){

srand(time(NULL));
pid_t p1,p2;
int fd1[2], fd2[2];
pipe(fd1);
pipe(fd2);

p1=fork();
if(p1==0){
	close(fd1[PIPE_RD]);
	close(fd2[PIPE_RD]);
	close(fd2[PIPE_WR]);
	while(1){
		int n1=rand()%50;
		if(n1%3==0){
			write(fd1[PIPE_WR], &n1, sizeof(n1));
		}
	}
	exit(0);
}

p2=fork();
if(p2==0){
        close(fd2[PIPE_RD]);
        close(fd1[PIPE_RD]);
        close(fd1[PIPE_WR]);
        while(1){
                int n2=(rand()%51)+100;
                if(n2%2==0){
                        write(fd2[PIPE_WR], &n2, sizeof(n2));
                }
        }
        exit(0);
}

close(fd1[PIPE_WR]);
close(fd2[PIPE_WR]);
int res1, res2, tot;
while(1){
	read(fd1[PIPE_RD], &res1, sizeof(res1));
	read(fd2[PIPE_RD], &res2, sizeof(res2));
	tot=res1+res2;
	printf("P1: %d, P2: %d | Somma: %d\n", res1, res2, tot);
	if(tot>130){
		break;
	}

}


kill(p1, SIGTERM);
kill(p2, SIGTERM);

waitpid(p1, NULL, 0);
waitpid(p2, NULL, 0);

}

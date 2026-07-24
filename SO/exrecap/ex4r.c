#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include <sys/wait.h>

#define PIPE_RD 0
#define PIPE_WR 1

int main(){

srand(time(NULL));
pid_t p1, p2;
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
		write(fd1[PIPE_WR], &num, sizeof(int));
		sleep(2);
	}
	exit(0);
}

p2=fork();
if(p2==0){
        close(fd2[PIPE_WR]);
        close(fd1[PIPE_WR]);
        close(fd1[PIPE_RD]);
        while(1){
		int num;
                read(fd2[PIPE_RD], &num, sizeof(int));
		printf("Il numero inviato dal padre è %d\n", num);
        }
        exit(0);
}

close(fd1[PIPE_WR]);
int numero;

while(1){
	read(fd1[PIPE_RD], &numero, sizeof(int));
	int n=(rand()%101)*numero;
	write(fd2[PIPE_WR], &n, sizeof(int));
	sleep(2);
}


waitpid(p1, NULL, 0);
waitpid(p2, NULL, 0);

}





#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <signal.h>
#include <time.h>

#define PIPE_RD 0
#define PIPE_WR 1

void sigint_handler(int signum){
        printf("Disabilitazione interrotta\n");
}

int main(){

srand(time(NULL));
int fd=open("dati.txt", O_RDONLY);
pid_t p1;
int fd1[2];
int fd2[2];
pipe(fd1);
pipe(fd2);
int x=lseek(fd, 0, SEEK_END);

p1=fork();
if(p1==0){
	close(fd1[PIPE_WR]);
	close(fd2[PIPE_RD]);
	while(1){
		int numpadre;
		read(fd1[PIPE_RD], &numpadre, sizeof(int));
		int numerobello=((rand()%6)+1)+numpadre;
		write(fd2[PIPE_WR], &numerobello, sizeof(int));
	}
	exit(0);
}


signal(SIGINT, sigint_handler);
close(fd1[PIPE_RD]);
close(fd2[PIPE_WR]);
while(1){
        int num=1+(rand()%11);
        int numfin=num-x;
        write(fd1[PIPE_WR], &numfin, sizeof(int));
        int nump1;
        read(fd2[PIPE_RD], &nump1, sizeof(int));
        printf("Padre - pid %d: valore corrente=%d\n", p1, x);
        if(nump1<=0){
                kill(p1, SIGTERM);
                break;
        }
        x+=nump1;
}

wait(NULL);

}

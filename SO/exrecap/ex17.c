#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include <sys/wait.h>
#include <signal.h>
#include <fcntl.h>

#define PIPE_RD 0
#define PIPE_WR 1

void sigint_handler(int signum){
	printf("Interruzione disabilitata\n");
}

int main(){
signal(SIGINT, sigint_handler);
srand(time(NULL));
int fd=open("numeri.txt", O_CREAT | O_TRUNC | O_WRONLY, 0644);
pid_t p1;
pid_t p2;
int fd1[2];
int fd2[2];
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
                write(fd2[PIPE_WR], &num, sizeof(int));
        }
        exit(0);
}

close(fd1[PIPE_WR]);
close(fd2[PIPE_WR]);

int num1, num2;
while(1){
	read(fd1[PIPE_RD], &num1, sizeof(int));
	read(fd2[PIPE_RD], &num2, sizeof(int));
	dprintf(fd, "%d\n", num1+num2);
	printf("La somma tra i numeri di P1 e P2 è %d\n", num1+num2);
	if (num1+num2 == 100) {
            printf("Somma 100 raggiunta. Termino.\n");
            break; // Esce dal ciclo while
        } else {
            // Se non è 100, il padre aspetta 2 secondi prima di leggere ancora
            // Nota: i dati si accumuleranno nella pipe, che è ok.
            sleep(2);
        }

}

lseek(fd, 0, SEEK_SET);

close(fd);

kill(p1, SIGTERM);
kill(p2, SIGTERM);

waitpid(p1, NULL, 0);
waitpid(p2, NULL, 0);

}

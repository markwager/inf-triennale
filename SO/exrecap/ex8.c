#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <sys/wait.h>

#define PIPE_RD 0
#define PIPE_WR 1

int main(){

srand(time(NULL));
pid_t pson;
int fd1[2], fd2[2];
pipe(fd1);
pipe(fd2);
int numson;
int quad;

pson=fork();
if(pson==0){
	close(fd2[PIPE_RD]);
	while(1){
		read(fd1[PIPE_RD], &numson, sizeof(numson));
		quad=numson*numson;
		printf("Il figlio invia %d\n", quad);
		write(fd2[PIPE_WR], &quad, sizeof(quad));
	}
	exit(0);
}

close(fd1[PIPE_RD]);
close(fd2[PIPE_WR]);

int num;
int rid;
for(int i=0; i<8; i++){
	num = rand() % 100;
        write(fd1[PIPE_WR], &num, sizeof(num));
        printf("Padre invia: %d\n", num);

        // Ora il padre sa che riceverà SEMPRE una risposta
        read(fd2[PIPE_RD], &rid, sizeof(rid));
        
        if (rid % 2 == 0) {
            printf("Il padre legge un quadrato PARI: %d\n", rid);
        } else {
            printf("Il padre legge un quadrato DISPARI: %d (scartato)\n", rid);
        }
}


kill(pson, SIGTERM);
waitpid(pson, NULL, 0);


}

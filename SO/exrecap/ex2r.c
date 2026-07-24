#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>
#include <fcntl.h>
#include <signal.h>

#define PIPE_RD 0
#define PIPE_WR 1

int count(char *buffer, int size, char *parola){
	
	int count=0;
	for(int i=0; i<size-strlen(parola); i++){
		if(strncmp(&buffer[i], parola, size)==0){
			count++;
		}

	}
	return count;
}


int main(){

char vally[]="vally";
int fd=open("testo.txt", O_RDONLY);
int tot=lseek(fd, 0, SEEK_END);
int meta=tot/2;
lseek(fd, 0, SEEK_SET);

pid_t p1, p2;
int fd1[2];
int fd2[2];
pipe(fd1);
pipe(fd2);

p1=fork();
if(p1==0){
	close(fd1[PIPE_RD]);
	close(fd2[PIPE_WR]);
	close(fd2[PIPE_RD]);
	char *buffer1=malloc(meta);
	read(fd, buffer1, meta);
	int conta=count(buffer1, meta, vally);
	write(fd1[PIPE_WR], &conta, sizeof(int));
	free(buffer1);
	exit(0);
}

int resto=tot-meta;
lseek(fd, meta, SEEK_SET);

p2=fork();
if(p2==0){
	close(fd2[PIPE_RD]);
	close(fd1[PIPE_WR]);
	close(fd1[PIPE_RD]);
	char *buffer2=malloc(resto);
	read(fd, buffer2, resto);
	int conta=count(buffer2, resto, vally);
	write(fd2[PIPE_WR], &conta, sizeof(int));
	free(buffer2);
	exit(0);
}

close(fd1[PIPE_WR]);
close(fd2[PIPE_WR]);

int n1, n2;

read(fd1[PIPE_RD], &n1, sizeof(int));
read(fd2[PIPE_RD], &n2, sizeof(int));
printf("La somma è %d\n", n1+n2);


close(fd);

//kill(p1, SIGINT);
//kill(p2, SIGINT); nn serve pk c'è già exit

waitpid(p1, NULL, 0);
waitpid(p2, NULL, 0);

}

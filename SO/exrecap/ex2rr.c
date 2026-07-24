#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <string.h>

#define PIPE_RD 0
#define PIPE_WR 1

int counter(char *parola, int size, char *buffer){
	int count=0;
	for(int i=0; i<size-strlen(parola); i++){
		if(strncmp(&buffer[i], parola, strlen(parola))==0){
			count++;
		}
	}
	return count;
}

int main(){

int fd=open("testo.txt", O_RDONLY);
pid_t p1;
pid_t p2;
int fd1[2], fd2[2];
pipe(fd1);
pipe(fd2);
int dim=lseek(fd, 0, SEEK_END);
int meta=dim/2;
char *parola="vally";

p1=fork();
if(p1==0){
	close(fd1[PIPE_RD]);
	close(fd2[PIPE_WR]);
	close(fd2[PIPE_RD]);
	lseek(fd, 0, SEEK_SET);
	char *buff=malloc(meta);
	read(fd, buff, meta);
	int num=counter(parola, meta, buff);
	write(fd1[PIPE_WR], &num, sizeof(int));
	free(buff);
	exit(0);
}

int resto=dim-meta;
p2=fork();
if(p2==0){
        close(fd2[PIPE_RD]);
        close(fd1[PIPE_WR]);
        close(fd1[PIPE_RD]);
        lseek(fd, resto, SEEK_SET);
        char *buff=malloc(resto);
        read(fd, buff, resto);
        int num=counter(parola, resto, buff);
        write(fd2[PIPE_WR], &num, sizeof(int));
        free(buff);
        exit(0);
}

close(fd1[PIPE_WR]);
close(fd2[PIPE_WR]);

int num1, num2;

read(fd1[PIPE_RD], &num1, sizeof(int));
read(fd2[PIPE_RD], &num2, sizeof(int));

int tot=num1+num2;
printf("Le occorrenze sono %d\n", tot);

close(fd);

kill(p1, SIGTERM);
kill(p2, SIGTERM);

waitpid(p1, NULL, 0);
waitpid(p2, NULL, 0);
}

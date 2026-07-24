#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <signal.h>

#define PIPE_RD 0
#define PIPE_WR 1

int main(){

int fd=open("testo.txt", O_RDONLY);
int fd1[2], fd2[2];
pipe(fd1);
pipe(fd2);

pid_t p1, p2;
int tot=lseek(fd, 0, SEEK_END);
int meta=tot/2;
int resto=tot-meta;

p1=fork();
if(p1==0){
	close(fd1[PIPE_RD]);
	close(fd2[PIPE_WR]);
	close(fd2[PIPE_RD]);
	lseek(fd, 0, SEEK_SET);
	char *buffer=malloc(meta);
	read(fd, buffer, meta);
	write(fd1[PIPE_WR], buffer, meta);
	free(buffer);
	exit(0);
}


p2=fork();
if(p2==0){
	close(fd2[PIPE_RD]);
        close(fd1[PIPE_WR]);
        close(fd1[PIPE_RD]);
	lseek(fd, meta, SEEK_SET);
        char *buffer=malloc(resto);
        read(fd, buffer, resto);
        write(fd2[PIPE_WR], buffer, resto);
        free(buffer);
	exit(0);
}

close(fd1[PIPE_WR]);
close(fd2[PIPE_WR]);

char *b1=malloc(meta);
char *b2=malloc(resto);
read(fd1[PIPE_RD], b1, meta);
read(fd2[PIPE_RD], b2, resto);

b1[meta+1]='\0';
b2[resto+1]='\0';

printf("Il figlio p1 con pid %d scrive: %s\n", p1, b1);
printf("Il figlio p2 con pid %d scrive: %s\n", p2, b2);

free(b1);
free(b2);
close(fd);

kill(p1, SIGINT);
kill(p2, SIGINT);

waitpid(p1, NULL, 0);
waitpid(p2, NULL, 0);
}


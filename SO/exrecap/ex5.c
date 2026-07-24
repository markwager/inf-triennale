#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>

#define PIPE_RD 0
#define PIPE_WR 1

int main(){

int fd1[2], fd2[2];
pid_t p1, p2;
pipe(fd1);
pipe(fd2);

int fd=open("testo.txt", O_RDONLY);
int dim_tot=lseek(fd, 0, SEEK_END);
int meta=dim_tot/2;
int resto=dim_tot-meta;

p1=fork();
if(p1==0){
	lseek(fd, 0, SEEK_SET);
	close(fd1[PIPE_RD]);
	close(fd2[PIPE_WR]);
	close(fd2[PIPE_RD]);
	char *buffer=malloc(meta*sizeof(char));
	read(fd, buffer, meta);
	write(fd1[PIPE_WR], buffer, meta);
	free(buffer);
	exit(0);
}

p2=fork();
if(p2==0){
	int resto=dim_tot-meta;
        close(fd1[PIPE_RD]);
        close(fd1[PIPE_WR]);
        close(fd2[PIPE_RD]);
	char *buffer=malloc(resto*sizeof(char));
	lseek(fd, meta, SEEK_SET);
        read(fd, buffer, resto);
        write(fd2[PIPE_WR], buffer, resto);
        free(buffer);
	exit(0);
}

close(fd1[PIPE_WR]);
close(fd2[PIPE_WR]);

char *b1=malloc(meta+1);
char *b2=malloc(resto+1);

read(fd1[PIPE_RD], b1, meta);
b1[meta]='\0';
read(fd2[PIPE_RD], b2, resto);
b2[resto]='\0';

printf("Il figlio p1 con pid %d scrive: %s\n", p1, b1);
printf("Il figlio p2 con pid %d scrive: %s\n", p2, b2);

free(b1);
free(b2);
close(fd);

waitpid(p1, NULL, 0);
waitpid(p2, NULL, 0);

}

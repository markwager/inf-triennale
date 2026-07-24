#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

#define PIPE_RD 0
#define PIPE_WR 1

int occorrenze(char *parola, int size, char *buffer){
	int count=0;
	for(int i=0; i<size-strlen(parola), i++){
		if(strncmp(&buffer[i],parola,len)==0){
			count++;
		}
	}
	return count;
}


int main(){

int fd=open("testo.txt", O_RDONLY);
pid_t p1, p2;
int fd1[2], fd2[2];
pipe(fd1);
pipe(fd2);
int dim=lseek(fd, 0, SEEK_END);
int meta=dim/2;
char *parola="valerio"

p1=fork()
if(p1==0){
	close(fd1[PIPE_RD]);
	close(fd2[PIPE_WR]);
	close(fd2[PIPE_RD]);
	lseek(fd, 0, SEEK_SET);
	char *buffer=malloc(meta);
	read(fd, buffer, meta);
	int conta=occorrenze(parola, meta, buffer);
	write(fd1[PIPE_WR], &conta, sizeof(int));
	sleep(2);
	exit(0);
}

int resto=tot-meta;

p2=fork()
if(p2==0){
        close(fd2[PIPE_RD]);
        close(fd1[PIPE_WR]);
        close(fd1[PIPE_RD]);
	lseek(fd, resto, SEEK_SET);
        char *buffer=malloc(meta);
        read(fd, buffer, meta);
        int conta=occorrenze(parola, meta, buffer);
        write(fd2[PIPE_WR], &conta, sizeof(int));
        sleep(2);
        exit(0);
}

close(fd1[PIPE_WR]);
close(fd2[PIPE_WR]);

int num1, num2;
read(fd1[PIPE_RD], &num1, sizeof(int));
read(fd2[PIPE_RD], &num2, sizeof(int));

printf("La somma tra le occorrenze è %d\n", num1+num2);

}

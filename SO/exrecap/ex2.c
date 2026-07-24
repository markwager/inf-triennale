#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <string.h>

#define PIPE_RD 0
#define PIPE_WR 1

int count(char *buffer, int size, char *parola){
	int count=0;
	int len=strlen(parola);
	for(int i=0; i<=size-len; i++){
		if(strncmp(&buffer[i], parola, len)==0){
			count++;
		}
	}
	return count;
}

int main(){

int fd=open("testo.txt", O_RDONLY);
char *parola="vally";
int fd1[2], fd2[2];
pipe(fd1), pipe(fd2);
pid_t p1, p2;

int dim_tot=lseek(fd, 0, SEEK_END); //numero di byte per lo spostamento, da dove inizia il calcolo
int meta=dim_tot/2;

p1=fork();
if(p1==0){
	close(fd1[PIPE_RD]);
	close(fd2[PIPE_RD]);
	close(fd2[PIPE_WR]);
	char *buffer=malloc(meta*sizeof(char));
	lseek(fd, 0, SEEK_SET); //parte dall'inizio del file
	read(fd, buffer, meta);
	int conta=count(buffer, meta, parola);
	write(fd1[PIPE_WR], &conta, sizeof(int));
	free(buffer);
	exit(0);
}

p2=fork();
if(p2==0){
	close(fd2[PIPE_RD]);
	close(fd1[PIPE_WR]);
	close(fd1[PIPE_RD]);
	int resto=dim_tot-meta;
	char *buffer=malloc(resto*sizeof(char));
	lseek(fd, meta, SEEK_SET);
	read(fd, buffer, resto);
	int conta=count(buffer, resto, parola);
	write(fd2[PIPE_WR], &conta, sizeof(int));
	free(buffer);
	exit(0);
}

close(fd1[PIPE_WR]);
close(fd2[PIPE_WR]);

int res1, res2;
read(fd1[PIPE_RD], &res1, sizeof(int));
read(fd2[PIPE_RD], &res2, sizeof(int));

printf("Risultato Figlio 1: %d\n", res1);
printf("Risultato Figlio 2: %d\n", res2);
printf("Totale occorrenze della parola '%s': %d\n", parola, res1 + res2);

close(fd);
waitpid(p1, NULL, 0);
waitpid(p2, NULL, 0); // Aspetta la fine dei figli


}


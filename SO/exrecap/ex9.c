#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>

#define  PIPE_WR 1
#define PIPE_RD 0

int main(){

pid_t p1, p2;
int n1[]={21, 4, 2, 3, 2, 1};
int n2[]={43, 32, 7, 8, 9, 10};
int fd1[2], fd2[2];
pipe(fd1);
pipe(fd2);

p1=fork();
if(p1==0){
	close(fd1[PIPE_RD]);
	close(fd2[PIPE_WR]);
	close(fd2[PIPE_RD]);
	for(int i=0; i<6; i++){
		if(i%2==0){
			write(fd1[PIPE_WR], &n1[i], sizeof(int));
		}
	}
	exit(0);
}

p2=fork();
if(p2==0){
        close(fd2[PIPE_RD]);
        close(fd1[PIPE_WR]);
        close(fd1[PIPE_RD]);
        for(int i=0; i<6; i++){
                if(i%2!=0){
                        write(fd2[PIPE_WR], &n2[i], sizeof(int));
                }
        }
        exit(0);
}


close(fd1[PIPE_WR]);
close(fd2[PIPE_WR]);
int *res;
res=malloc(sizeof(int)*6);

for(int i=0; i<6; i++){
	
	if(i%2==0){
		read(fd1[PIPE_RD], &res[i], sizeof(int));
	}

	else{
		read(fd2[PIPE_RD], &res[i], sizeof(int));
	}
}

kill(p1, SIGTERM);
kill(p2, SIGTERM);

waitpid(p1, NULL, 0);
waitpid(p2, NULL, 0);

int max=res[0];
int min=res[0];

for(int i=0; i<6; i++){

	printf("%d ", res[i]);
	if(res[i]>max){
		max=res[i];
	}
	if(res[i]<min){
		min=res[i];
	}

}

printf("\n");
printf("Il minimo è %d\n", min);
printf("Il massimo è %d\n", max);
free(res);
}

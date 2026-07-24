#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

#define PIPE_RD 0
#define PIPE_WR 1

int main(){

int matr_a[3][3]={{12,5,4},{2,10,6},{4,3,2}};
int matr_b[3][3]={{5,7,9},{11,33,20},{25,42,1}};
int res[3][3];
pid_t p1, p2;
int fd1[2], fd2[2];
pipe(fd1);
pipe(fd2);

p1=fork();
if(p1==0){
	close(fd1[PIPE_RD]);
	close(fd2[PIPE_WR]);
	close(fd2[PIPE_RD]);
	int colonna[3];
	for(int j=0; j<3; j++){
		colonna[j]=0;
		for(int i=0; i<3; i++){
			colonna[j]+=matr_a[j][i]*matr_b[i][0];
		}
	}
	write(fd1[PIPE_WR], colonna, sizeof(colonna));
	exit(0);
}

p2=fork();
if(p2==0){
        close(fd2[PIPE_RD]);
        close(fd1[PIPE_WR]);
        close(fd1[PIPE_RD]);
        int colonna[3];
        for(int j=0; j<3; j++){
                colonna[j]=0;
                for(int i=0; i<3; i++){
                        colonna[j]+=matr_a[j][i]*matr_b[i][1];
                }
        }
	write(fd2[PIPE_WR], colonna, sizeof(colonna));
        exit(0);
}

close(fd1[PIPE_WR]);
close(fd2[PIPE_WR]);

int col1[3];
int col2[3];

read(fd1[PIPE_RD], col1, sizeof(col1));
read(fd2[PIPE_RD], col2, sizeof(col2));

for(int j=0; j<3; j++){
	res[j][2]=0;
	for(int i=0; i<3; i++){
		res[j][2]+=matr_a[j][i]*matr_b[i][2];
	}

}

 for(int i=0; i<3; i++){
        res[i][0]=col1[i];
        res[i][1]=col2[i];
    }

    printf("Risultato Moltiplicazione Parallela:\n");
    for(int j=0; j<3; j++){
	for(int i=0; i<3; i++){
		printf("%d\t", res[j][i]);
	}
	printf("\n");
    }

    waitpid(p1, NULL, 0);
    waitpid(p2, NULL, 0);

}

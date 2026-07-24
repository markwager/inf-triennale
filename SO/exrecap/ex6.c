#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

#define PIPE_RD 0
#define PIPE_WR 1

void stampa_m(int m[3][3]){
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){ // Corretto: j < 3
            printf("%d\t", m[i][j]); // Corretto: m[i][j]
        }
        printf("\n");
    }
}

int main(){
    int matr_a[3][3]={{12,5,4},{2,10,6},{4,3,2}};
    int matr_b[3][3]={{5,7,9},{11,33,20},{25,42,1}};
    int res[3][3];

    pid_t p1, p2;
    int fd1[2], fd2[2];
    pipe(fd1);
    pipe(fd2);
    int i; 

    p1=fork();
    if(p1==0){
        close(fd1[PIPE_RD]);
        close(fd2[PIPE_WR]);
        close(fd2[PIPE_RD]);
        int colonna[3];
        for(i=0; i<3; i++){
            colonna[i]=0;
            for(int k=0; k<3; k++){
                colonna[i]+=matr_a[i][k]*matr_b[k][0];
            }
        } 
        write(fd1[PIPE_WR], colonna, sizeof(colonna));
        exit(0);
    }

    p2=fork();
    if(p2==0){
        close(fd1[PIPE_RD]);
        close(fd1[PIPE_WR]);
        close(fd2[PIPE_RD]);
        int colonna[3];
        for(i=0; i<3; i++){
            colonna[i]=0;
            for(int k=0; k<3; k++){
                colonna[i]+=matr_a[i][k]*matr_b[k][1];
            }
        }
        write(fd2[PIPE_WR], colonna, sizeof(colonna));
        exit(0);
    }

    // Processo Padre
    close(fd1[PIPE_WR]);
    close(fd2[PIPE_WR]);

    for(i=0; i<3; i++){
        res[i][2]=0;
        for(int k=0; k<3; k++){
            res[i][2]+=matr_a[i][k]*matr_b[k][2];
        }
    }

    int col0[3], col1[3];
    // Sintassi corretta per la read
    read(fd1[PIPE_RD], col0, sizeof(col0));
    read(fd2[PIPE_RD], col1, sizeof(col1));

    for(int i=0; i<3; i++){
        res[i][0]=col0[i];
        res[i][1]=col1[i];
    }

    printf("Risultato Moltiplicazione Parallela:\n");
    stampa_m(res);

    waitpid(p1, NULL, 0);
    waitpid(p2, NULL, 0);
}

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <time.h>

#define PIPE_RD 0
#define PIPE_WR 1

int main() {
    srand(time(NULL));
    pid_t p1, p2;
    int fd1[2], fd2[2];
    int n1, n2;

    pipe(fd1);
    pipe(fd2);

    p1 = fork();
    if (p1 == 0) {
        close(fd1[PIPE_RD]); 
        close(fd2[PIPE_RD]);
        close(fd2[PIPE_WR]); 

        while (1) {
            n1 = rand() % 100;
            write(fd1[PIPE_WR], &n1, sizeof(int));
        }
        exit(0);
    }

    p2 = fork();
    if (p2 == 0) {
       
        close(fd1[PIPE_RD]); // P2 doesn't touch pipe 1
        close(fd1[PIPE_WR]);
        close(fd2[PIPE_WR]); // P2 only reads from pipe 2
        while (1) {
            read(fd2[PIPE_RD], &n2, sizeof(int));
                printf("Il numero letto da p2 è %d\n", n2);
                sleep(1); // Wait as per original requirement
        }
        exit(0);
    }

    // --- PARENT PROCESS (Processor) ---
    close(fd1[PIPE_WR]);
    close(fd2[PIPE_RD]);

    while (1) {
            read(fd1[PIPE_RD], &n1, sizeof(int));
            n2 = n1 * (rand() % 10);
            write(fd2[PIPE_WR], &n2, sizeof(int));
    }

    waitpid(p1,NULL,0);
    waitpid(p2,NULL,0);
}

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <signal.h>

#define PIPE_RD 0
#define PIPE_WR 1

int main(){

int fd=open("minchia.txt",  O_RDWR | O_TRUNC | O_CREAT, 0644);
pid_t p1, p2;
int fd1[2], fd2[2];
pipe(fd1);
pipe(fd2);

p1=fork();
if(p1==0){
	close(fd1[PIPE_RD]);
	close(fd2[PIPE_WR]);
	close(fd2[PIPE_RD]);
	for(int i=0; i<10; i+=2){
		dprintf(fd, "%d\n", i);
	}
	write(fd, "fatto p1\n", 10);
	exit(0);
}

p2=fork();
if(p2==0){
        close(fd2[PIPE_RD]);
        close(fd1[PIPE_WR]);
        close(fd1[PIPE_RD]);
        for(int i=1; i<10; i+=2){
                dprintf(fd, "%d\n", i);
        }
	write(fd, "fatto p2\n", 10);
        exit(0);
}

close(fd1[PIPE_WR]);
close(fd2[PIPE_WR]);

waitpid(p1, NULL, 0);
waitpid(p2, NULL, 0);

lseek(fd, 0, SEEK_SET);

char buffer[1];

while(read(fd, buffer, sizeof(char))>0){
	putchar(buffer[0]);
}

close(fd);

}

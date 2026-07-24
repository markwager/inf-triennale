#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <sys/wait.h>

#define PIPE_RD 0
#define PIPE_WR 1


int main(){

int fd=open("testo.txt", O_CREATE | O_RWONLY | O_TRUNC, 0644);
pid_t p1;
pid_t p2;

p1=fork()
if(p1==fork){
	while(1){
		for(int i=0; i<10; i+=2){
			dprintf(fd, "Scrivo il numero pari: %d\n", i);
		}
		sleep(2);
	}
	exit(0);
}

p2=fork()
if(p2==fork){
        while(1){
                for(int i=1; i<10; i+=2){
                        dprintf(fd, "Scrivo il numero dispari: %d\n", i);
                }
                sleep(2);
        }
	exit(0);
}

lseek(fd, 0, SEEK_SET);
char buffer[1];
while(read(fd, buffer, sizeof(char)>0)){
	putchar(buffer[0]);
}


waitpid(p1, NULL, 0);
waitpid(p2, NULL, 0);

close(fd);

}

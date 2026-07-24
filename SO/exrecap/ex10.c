#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>
#include <fcntl.h>

#define PIPE_WR 1
#define PIPE_RD 0

int main(){

srand(time(NULL));
pid_t p1, p2;
int fd=open("minchia.txt", O_RDWR | O_CREAT | O_TRUNC, NULL); //lettura/scrittura
//creazione se non c'è e se esiste il suo contenuto viene eliminato

p1=fork();
if(p1==0){
	for(int z=0; z<10; z++){
		int i=(rand()%100)*2;
		dprintf(fd, "%d\n", i);
	}
exit(0);

}

p2=fork();
if(p2==0){
        for(int z=0; z<10; z++){
		int j=(rand()%100)*2+1;
                dprintf(fd, "%d\n", j);
                
        }
exit(0);

}


waitpid(p1, NULL, 0);
waitpid(p2, NULL, 0);
lseek(fd, 0, SEEK_SET);

char buffer[1];
while(read(fd, buffer, sizeof(char))>0){
	putchar(buffer[0]);
}

close(fd);


}

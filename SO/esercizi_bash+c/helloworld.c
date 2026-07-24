#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>
#define STDOUT 1

void hello1();
void hello2();
void hello3();

void hello1(){
printf("Hello World!\n");
} //stampa sullo standard output (terminale)

void hello2(){
char msg[]="Hello World!!\n";
write(STDOUT, msg, sizeof(msg)); //dentro c'è fd, buffer e size del messaggio
}

void hello3(){
char msg[]="Hello World!!!\n";
int nr=SYS_write;
syscall(nr, STDOUT, msg, sizeof(msg)); //numero di chiamata di write, messaggio e sua size
}

int main(){
hello1();
hello2();
hello3();
}

/*
questo programma fa vedere come viene implementata in realtà printf()
*/

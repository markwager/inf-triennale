#include <stdlib.h> // Necessario per malloc e free
#include <stdio.h> // Necessario per printf
#include <string.h>

char *prefix(char*, int);

char *prefix(char *s, int n) {
    char *p = malloc(n+1);
    for (int i = 0; i < n; i++) {
        p[i] = s[i];
    }

    if(n > strlen(s)){
        int x = strlen(s);
        for(int j=0;j<x;j++){
            p[j] = s[j];
            
        }
    }

    p[n] = '\0';
    return p;

}

int main() {
    char s[] = "ciao";
    printf("%s\n",prefix(s, 5));
}
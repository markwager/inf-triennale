#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *sottostr(char *a, int n, int i, int j);

char *sottostr(char *a, int n, int i, int j){

    int k=0;

    char *p=malloc(n*sizeof(char)); //crea un array di char

    for (i; i < j; i++) {
        p[k] = a[i];
        k++;
    }

    return p;

}

int main()
{

    char a[]="programmazione dei calcolatori";
    int n=strlen(a)+1;
    int i=4;
    int j=18;
    char *result = sottostr(a, n, i, j);
    printf("%s\n", result);

}

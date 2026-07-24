#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *copia_array_di_str_conc(char *, int, char *, int);

int *copia_array_di_str_conc(char *a, int n, char *b, int m){

    int i=0;
    int j=0;

    char *c=malloc((n+m+1)*sizeof(char));

    for (i; i < n+m+1; i++) {
        if(a[i]<=b[i]){

            strcpy(c, a); // copio a in c
            strcpy(c+n, b); // copio b in c 

        }

        else if(a[i]>b[i]){

            strcpy(c, b);
            strcpy(c+m, a);

        }

    }


    return c;

}


int main()
{
    char a[]="prolog";
    char b[]="programmazione";
    int n=strlen(a);
    int m=strlen(b);
    //restituiscono il num di elementi
    int *w=copia_array_di_str_conc(a, n, b, m);
    printf("%s\n", w);

}


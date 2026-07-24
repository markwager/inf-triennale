#include <stdlib.h> // Necessario per malloc e free
#include <stdio.h> // Necessario per printf
#include <string.h>

char *str_cat0(char*, int, char*);

char *str_cat0(char *a, int n, char *b){

    int j=0;

    for(j; j<strlen(b);j++){
        a[n + j] = b[j];
    }

    return a;
}

int main0(){

    char *a = "ciao";
    char *b = "mondo";
    int n=strlen(a);
    char *c = str_cat0(a, n, b);
    printf("%s\n", c);

}

/*  
Questa è una possibile soluzione, altrimenti c'è questa soluzione:
*/

char *str_cat(char*, int, char*);

char *str_cat(char *a, int n, char *b){

    int j=0;

    for(j; j<strlen(b);j++){
        a[n + j] = b[j];
    }

    return a;
}

char *str_cat(char *a, int n, char *b){
    int size = n + strlen(b) + 1;

    // Ridimensiona l'array a per contenere b
    a = realloc(a, size * sizeof(char));

    // Copia b in a a partire dall'indice n
    for (int j = 0; j < strlen(b); j++) {
        a[n + j] = b[j];
    }

    // Aggiungi il terminatore nullo
    a[n + strlen(b)] = '\0';

    return a;
}

/**
 * This function tests the function str_cat.
 */
int main(){

    char *a = malloc((strlen("ciao") + 1) * sizeof(char));
    strcpy(a, "ciao");
    char *b = "mondo";
    int n=strlen(a);
    char *c = str_cat(a, n, b);
    printf("%s\n", c);

}

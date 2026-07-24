#include <stdio.h>
#include <stdlib.h>

//l'array e una sequenza di elementi di uno stesso tipo. Possiamo solo definirlo e modificare gli elementi


int main()
{

    int a[10]; //un array di 10 elementi int indefinito
    int b[5]={0,1,5,1,2,4}; //array di 6 interi definiti
    int c[]={4,1,4}; //stessa cosa di quello sopra
    int d[101]={0,1,2}; //definisco esplicitamente i primi 3 elementi, da d[3] in poi gli elementi sono 0

    int i=0;

    while(i=0){
        printf("%d\n", d[i]); //legge l'array
        i++;
    }

    for(i=0; i<10; i++){
        printf("%d\n",d[i]); //legge l'array (come il blocco di prima)

    }

    d[9]=10; //modifica array

}

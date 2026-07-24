/*
si scriva una funzione in c che abbia il seguente prototipo: 
int *x_arry(int *a, int na, int *b, int nb);
na è la lunghezza dell'array a
nb la lunghezza dell'array b

la funzione restituisce una matrice m con na righe e nb colonne tale che in riga i e colonna j ci sia il valore a[i]*b[j]. La matrice di output deve essere rappresentata con
un array di dimensione na*nb

*/

#include <stdio.h>
#include <stdlib.h>

int *x_array(int *a, int na, int *b, int nb){
    int *matrix=malloc(na*nb*sizeof(int));
    for(int i=0; i<na; i++){
        for(int j=0; j<nb; j++){
            matrix[i*nb+j]=a[i]*b[j];
        }
    }

    return matrix;
}

int main(){

    int a[]={1,2,3};
    int b[]={10,20,30,40};
    int *c=x_array(a,3,b,4);

    for(int i=0; i<3; i++){
        for(int j=0; j<4; j++){
            printf("%d ", c[i*4+j]);
        }
    }
}
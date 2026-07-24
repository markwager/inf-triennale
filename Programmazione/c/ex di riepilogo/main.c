/*
Scrivere una funzione in C che, date tre varibili intere a, b e c, scambia gli interi contenuti in queste variabile in modo che a <= b <= c.
Esempio:

Input: int a = 5; int b = 7; int c = 2;
dopo l'esecuzione della funzione, si deve ottenere che
Output: a = 2; b = 5; c = 7;
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivere una funzione in C che, dato un array di interi a e la sua dimensione n, restituisce l'indirizzo del più piccolo elemento contenuto in a.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivere una funzione in C che, dato un'array a di float di lunghezza n, crea un'array che è l'inverso di a, ossia, il nuovo array memorizza gli elementi di a al
contrario.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivere una funzione in C che, dati due array a e b di int di lunghezza rispettivamente n e m, crea un'array che è la concatenazione di a e b, ossia, il nuovo array
memorizza prima gli elementi di a e, a seguire, gli elementi di b.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivere una funzione in C che, dato un'intero n, crea un'array di interi tale che nella posizione 0 <= i <= n è contenuta il valore di i!, ovvero il fattoriale di i.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivere una funzione in C che, dato in input un array di elementi b di lunghezza n, crea e restituisce in output una lista contenente gli elementi di b.
*/
#include<stdio.h>
#include <stdlib.h>
#include <string.h>

void ordina(int*, int*, int*);
int *piccoloinarray(int[],int);
float *inversearray(float[],int);
int *concatenazione(int[], int, int[], int);
int *arrayfatt(int);


int *arrayfatt(int n){

    int *array=malloc((n+1)*sizeof(int));
    *array=1;
    int i=1;
    for(i;i<n+1;i++){
        array[i]=array[i-1]*i;
    }

    return array;

}

int *concatenazione(int a[], int n1, int b[], int n2){

    int *new_a=malloc((n1+n2)*sizeof(int));
    int i=0;
    int j=0;
    for(i; i<n1; i++){
        new_a[i]=a[i];
    }

    for(j; j<n2;j++){
        new_a[n1 + j] = b[j];
    }

    return new_a;
}

float *inversearray(float a[],int n){

    float *new_a=malloc(n*sizeof(float));
    int i=0;
    for(i; i<n; i++){
        new_a[i]=a[n-1-i];
    }

    return new_a;
}



int *piccoloinarray(int a[], int n){

    if(n<=0){
        return NULL;
    }

    int *min=&a[0];

    int i=0;
    for(i; i<n; i++){
        if(a[i]<*min){
            min=&a[i];
        }
    }

    return min;

}

void ordina(int *a, int *b, int *c) {
    int temp;
    if (*a > *b) {
        temp = *a;
        *a = *b;
        *b = temp;
    }
    if (*a > *c) {
        temp = *a;
        *a = *c;
        *c = temp;
    }
    if (*b > *c) {
        temp = *b;
        *b = *c;
        *c = temp;
    }
}

int main(){

    int a = 16;
    int b = 18;
    int c = 7;
    ordina(&a,&b,&c);
    printf("%d, %d, %d\n",a,b,c);

    int L[5]={1,2,4,5,7};
    int n=sizeof(L)/sizeof(L[0]);

    int *minimo = piccoloinarray(L, n);
    printf("Il valore minimo è %d e si trova all'indirizzo %p\n", *minimo, minimo);

    float L1[]={2.3, 5.5, 6.8, 2.4};
    int n1=sizeof(L1)/sizeof(float);
    float *p = inversearray(L1, n1);

    for(int i = 0; i < n1-1; i++) {
        printf("%f\n", p[i]);
    }
    printf("%f\n", p[n1-1]);

    int x[] = {1, 2, 3};
    int y[] = {4, 5, 6};
    int n11 = sizeof(x) / sizeof(int);
    int n22 = sizeof(y) / sizeof(int);

    // Chiamata alla funzione concatenazione
    int* result = concatenazione(x, n11, y, n22);

    if (result != NULL) {
        printf("Array concatenato: ");
        for (int i = 0; i < n11 + n22; i++) {
            printf("%d ", result[i]);
        }
        printf("\n");
    }

    int num=5;
    int *arrayfattoriale = arrayfatt(num);
    for (int i = 0; i < num; i++) {
            printf("%d ", arrayfattoriale[i]);
        }

        printf("%d", arrayfattoriale[num] );

}
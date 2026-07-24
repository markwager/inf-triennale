#include <stdio.h>

float potenza(float x, int e);
int scambia(int *, int *, int *);
int* indirizzo_minimo(int *, int );
int* somma_array(int* , int , int );
int inv_array(int, int);

float potenza(float x, int e){
    int i=1;
    int pt=0;
    if (e>0){

        while(i<e){

            x*=x;
            i++;
    }

    }

    else if(e==0){
        return 1;
    }

    else{

        pt=-e;

        while(i<pt){

            x*=x;
            i++;
    }

        return 1/x;

    }

    return x;

}



//esercizio sulla potenza


int scambia(int *a, int *b, int *c){
    int tmp=0;

    if(*a > *b){
        tmp=*b;
        *b=*a;
        *a=tmp;
    }

    if(*b>*c){
        tmp=*c;
        *c=*b;
        *b=tmp;
    }

      if(*a > *b){
        tmp=*b;
        *b=*a;
        *a=tmp;
    }

    return 1;
}

int* indirizzo_minimo(int *a, int n){

    int* indirizzo_minimo=&a[0];

    for(int i=1; i<n; i++){

        if(a[i]<*indirizzo_minimo){
            indirizzo_minimo=&a[i];
        }

    }

    return indirizzo_minimo;
}

int* somma_array(int* a, int m, int n){

    int* p=malloc((n+m)*sizeof(int));
    if(p==NULL){
        return NULL;
    }

    int somma=0;
    p[m]=somma;

    for(int i=0; i<m; i++){

        p[i]=a[i];
        somma+=a[i];

    }

    for(int i=m+1; i<n+m; i++){

        p[i]=a[i-1]*2;
    }

    return p;
}

int inv_array(int array, int n){

    float copy[n];

    int j=0;

    for(int i=n; i>j; i-=1){
        copy[i]=i;
    }

    return copy;

}


int main0()
{
    printf("%f\n", potenza(3,-1));
    int a=5;
    int b=7;
    int c=2;
    scambia(&a, &b, &c);
    printf("%d, %d, %d\n", a, b, c);
    int d[]={21,5,6,1};
    int n=sizeof(d)/sizeof(int); //ritorna la dimensione in byte
    int *p=indirizzo_minimo(d,n);
    printf("indirizzo del minimo: %p\n", p);
    printf("Minimo: %d\n", *p);
    int e[]={1,2,3,};
    int m= sizeof(a)/sizeof(int);
    int *k=somma_array(e,m,6);
    for(int i=0; i<m+6; i++){

        printf("%d\n",k[i]);
    }

    //Scrivere una funzione in C che, dato un'array a di float di lunghezza n, crea un'array che è l'inverso di a,
    //ossia, il nuovo array memorizza gli elementi di a al contrario.
}


int main(){

int n=3;
int array[n]={0,1,2,3};
printf("%d\n", inv_array(array, n));

}

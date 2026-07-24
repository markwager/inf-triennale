#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//inserimento generico e eliminazione generica?

typedef struct  {
    char tipo; /* 'i' intero; 'f' float; 's' stringa */
    void *dato;
} elemento;

struct lista {
    elemento *a;
    int c;  /* capacita'  */
    int n;  /* dimensione, numero di elementi */
};
typedef struct lista lista;

lista init();
lista init_array(elemento *, int);
lista append(lista, elemento);
void mostra(lista);

elemento intero(int);
elemento fpoint(float);
elemento stringa(char*);

int main(){

    elemento a[]={intero(10), stringa("ciao"), fpoint(3.14)};
    int n=sizeof(a)/sizeof(elemento);
    lista L=init_array(a, n);
    mostra(L);
    L=append(L, fpoint(2.71));
    mostra(L);


}


lista init(){
    lista lista_vuota = {NULL, 0, 0};
    return lista_vuota;
}

lista init_array(elemento *b, int n){

    lista L=init();
    L.n=n;
    L.c=2*(n+1);
    L.a=malloc(L.c*sizeof(elemento));
    for(int i=0;i<n;i++){
        L.a[i]=b[i];
    }
    return L;
}

lista append(lista L, elemento e){
    if (L.n == L.c) {
        L.c = 2*(L.c+1);
        L.a = realloc( L.a, L.c*sizeof(elemento) );
    }

    L.a[L.n] = e;
    L.n++;

    return L;
}

void mostra(lista L){
    int i;

    printf("==================================\n");

    for(i = 0; i < L.n; i++){
        /* stampa L.a[i] */
        /*
         * if( L.a[i].tipo == 'i' )
            printf("%d\n", *((int*)L.a[i].dato) );
        */
        switch  (L.a[i].tipo) {
            case 'i':
                printf("%d\n", *((int*)L.a[i].dato) );
                break;
            case 'f':
                printf("%f\n", *((float*)L.a[i].dato) );
                break;
            case 's':
                printf("%s\n", (char*)L.a[i].dato );
                break;
            //default:
                /* se non vero i precedenti*/
        }
    }

    printf("dimensione %d, capacita' %d\n", L.n, L.c);
}

elemento intero(int d){
    elemento e = {'i', NULL};

    e.dato = malloc(sizeof(int));
    *((int*)e.dato) = d;

    return e;
}

elemento fpoint(float d){
    elemento e = {'f', NULL};

    e.dato = malloc(sizeof(float));
    *((float*)e.dato) = d;

    return e;
}

elemento stringa(char *d){
    elemento e = {'s', NULL};

    e.dato = d;

    return e;
}

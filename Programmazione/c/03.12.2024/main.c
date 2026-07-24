#include <stdio.h>
#include <stdlib.h>

//l'elemento di un array occupa un certo tipo di spazio per via dell'indicizzazione che deve essere facile ed efficiente da implementare
//e poi un elemento ha un certo spazio per via dell'elemento
//l'indirizzo di a[i] è a+d*i, dove d è il peso dell'elemento (indicizzazione in tempo costante)
//per mantenere questa formula valida e consentire la presenza di elementi di tipo diverso si introduce una lista indipendente dal tipo
//per ottenere una lista indipendente dal tipo: ogni elemento contiene 2 informazioni
//un tipo e un puntatore al dato vero e proprio (il tipo del dato è dentro l'elemento della lista)
//posso fare il free solo in caso di memoria allocata con malloc

typedef struct  {
    char tipo; /* 'i' intero; 'f' float; 's' stringa */
    void *dato; //metto void perchè non posso scrivere int, float o char. è un tipo di dato jolly che si utilizza anche nelle funzioni pee indicare che la funzione non ha un return
} elemento;
//questa è una struttura per l'elemento dell'array

struct lista {
    elemento *a;
    int c;  /* capacita'  */
    int n;  /* dimensione, numero di elementi */
};
typedef struct lista lista;

//ricorda: i due typedef definiti sono uguali

lista init();
lista append(lista, elemento);
void mostra(lista); //tipo void perchè non ritorna  niente
lista pop(lista); //operazione di cancellazione in tempo costante a partire dall'ultimo elemento

elemento intero(int);
elemento fpoint(float);
elemento stringa(char*);

int main(){
    lista L = init();

    L = append(L, intero(10) );
    L = append(L, fpoint(3.14) );
    L = append(L, stringa("programma") );
    L = append(L, fpoint(2.71) );
    L = append(L, stringa("lista") );
    L = append(L, intero(7) );
    L = append(L, intero(10) );
    L = append(L, fpoint(3.14) );
    L = append(L, stringa("programma") );
    L = append(L, fpoint(2.71) );
    L = append(L, stringa("lista") );
    L = append(L, intero(7) );
    L = append(L, intero(10) );
    L = append(L, fpoint(3.14) );
    L = append(L, stringa("programma") );
    L = append(L, fpoint(2.71) );
    L = append(L, stringa("lista") );
    L = append(L, intero(7) );
    L = append(L, intero(10) );
    L = append(L, fpoint(3.14) );
    L = append(L, stringa("programma") );
    L = append(L, fpoint(2.71) );
    L = append(L, stringa("lista") );
    L = append(L, intero(7) );

    mostra(L);

    while(L.n > 0){
        L = pop(L);
        mostra(L);
    }

}

lista init(){
    lista lista_vuota = {NULL, 0, 0}; //a=0, c=0, n=0
    return lista_vuota;
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
                printf("%d\n", *((int*)L.a[i].dato) ); //devo fare una conversione di tipo dato che dato è un puntatore a void
                break;
            case 'f':
                printf("%f\n", *((float*)L.a[i].dato) );
                break;
            case 's':
                printf("%s\n", (char*)L.a[i].dato ); //il campo dato, in questo caso, contiene il puntatore che fa riferimento alla stringa. Non si mette l'asterisco perchè la stringa è già un array
                break;
            //default:
                /*se non vero i precedenti*/
        }
    }

    printf("dimensione %d, capacita' %d\n", L.n, L.c);
}

lista pop(lista L){
    if(L.n > 0){
        L.n--;
        if (L.n < L.c/4){
            L.c = L.c/2;
            L.a = realloc(L.a, (L.c)*sizeof(elemento));
        }
        if (L.a[L.n].tipo !='s')
            free(L.a[L.n].dato);
    }
    return L;
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

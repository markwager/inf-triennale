#include <stdio.h>
#include <stdlib.h>

struct lista_f{
    //un campo è un dato che si definisce come una variabile

    float *a;
    int c; //capacità
    int n; //dimensione (numero di elementi)
    //come si gestisce tale struttura?


}; //somiglia alla lista python

typedef struct lista_f lista_f; //ci consente di assegnare un nuovo nome a un tipo già esistente

lista_f append(lista_f, float);
lista_f init();
lista_f inverti_lista(lista_f);


int main()
{
    int i;
    float *a;
    lista_f L1;
    L1=init();
    for(i=0;i<20;i++){
        L1=append(L1, i*10);
        printf("%d, %d\n", L1.n, L1.c);
    }

    for(i=0;i<20;i++){
        printf("%f\n", L1.a[i]);
    }

    //questa funzione fa un append normale di una lista

    printf("\n");

    // Inversione della lista
    L1 = inverti_lista(L1);

    // Stampa della lista invertita
    printf("\nLista invertita:\n");
    for (i = 0; i < L1.n; i++) {
        printf("%f ", L1.a[i]);
    }
    printf("\n");



}

lista_f init(){

    lista_f lista_vuota={NULL, 0, 0}; //NULL valore del primo, 0 valore del secondo campo...
    return lista_vuota;

}

lista_f append(lista_f L, float e){

    if(L.n==L.c){
        L.c=2*(L.c+1);
        L.a=realloc(L.a, L.c*sizeof(float));
    }

        L.a[L.n]=e;
        L.n++;

    return L;
}

lista_f inverti_lista(lista_f L) {
    for (int i = 0; i < L.n/2; i++) {
        float temp = L.a[i];
        L.a[i] = L.a[L.n - 1 - i];
        L.a[L.n - 1 - i] = temp;
        //le ultime due stringhe invertono il posto nel nuovo array
    }
    return L; // Restituisce la lista invertita
}

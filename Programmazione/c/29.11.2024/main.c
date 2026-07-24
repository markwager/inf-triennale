#include <stdio.h>
#include <stdlib.h>

float *copia_array_di_float(float *, int);

//la struct o struttura è un contenitore che contiene dati

struct lista_f{
    //un campo è un dato che si definisce come una variabile

    float *a;
    int c; //capacità
    int n; //dimensione, numero di elementi
    //come si gestisce tale struttura?


}; //somiglia alla lista python

typedef struct lista_f lista_f; //ci consente di assegnare un nuovo nome a un tipo già esistente

lista_f append(lista_f, float);
lista_f init();


int main(){

    struct lista_f L; //L contiene i tre campi
    lista_f L1;
    int i;
    L.c=10; //contiene al massimo 10 elementi
    L.n=0;
    L.a=malloc(L.c*sizeof(float));

    L.a[0]=3.14;
    L.a[1]=2.71;
    L.n ++;

    for(int i=0; i<L.n; i++){
        printf("%f\n", L.a[i]);
    }

    L1=init();
    for(i=0;i<20;i++){
        L1=append(L1, i*10);
        printf("%d, %d\n", L1.n, L1.c);
    }

    for(i=0;i<20;i++){
        printf("%f\n", L1.a[i]);
    }

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

//costo temporale nel caso peggiore è o(n) per via della realloc

int main1(){
    int i, n=10;
    float *a=malloc(n*sizeof(float)); //array dinamico di 10 float. Ha costo O(1) (operazione malloc)
    //possiamo iniializzare l'array con il for
    for(i=0; i<n; i++){

        a[i]=10+i;

    }

    n++;

    //voglio che l'array diventi grande 11

    //possiamo chiedere al sistema operativo se c'è spazio

    a=realloc(a, (n+1)*sizeof(float)); //nel caso di successo ritorna il nuovo indirizzo alla nuova memoria allocata
    //la realloc non ritorna per forza l'indirizzo della locazione all'inizio
    //altrimenti va a cercare spazio da qualche altra parte e tutto il contenuto viene copiato nel nuovo spazio e lo spazio di prima viene liberato
    //nel terzo caso non c'è proprio spazio in memoria e si ritorna null
    //il costo nel peggiore dei casi è O(n), in tutti gli altri casi O(1)

    a[n-1]=0;

    for(i=0; i<n; i++){

        printf("%f\n", a[i]);

    }

    free(a);

    int m=100;

    n=1;

    a=malloc(1*sizeof(float));

    for(i=0; i<m; i++){
        n++;
        a=realloc(a,n*sizeof(float));
        a[n-1]=n;

        //si aggiunge in fondo all'array dinamico l'elemento
    }

    //questo for, nel caso peggiore, ha costo O(n*m) cioè quadratico
    //il costo di n append in python è O(n)
    //dobbiamo escludere che la realloc abbiamo un costo lineare, si deve comportare "male" nel caso peggiore ogni tanto: si alloca un po' più di spazio di modo da avere un costo costante
    //l'array ha un tipo e una dimensione
    //introduciamo quindi la capacità dell'array: quanti elementi posso inserire dentro l'array
    //se n(=numero di elementi nell'array)<c usiamo la posizione n[a] e aggiorniamo n, se n=c dobbiamo fare un realloc, e dobbiamo fare un append--> si raddoppia la capacità dell'array
    //il costo medio di un append è O(1), nel caso peggiore o(n)

    for(i=0; i<n; i++){

        printf("%f", a[i]);

    }

    printf("\n");

}




int main0()
{

    //un array allocato staticamente ha una memoria fissa in compile time
    //in allocazione dinamica possiamo decidere quanto allocare per una singola struttura dati
    float v[20]={0,1,2};
    int i,n=sizeof(v)/sizeof(float);
    float *w=copia_array_di_float(v, n); //sizeof restituisce la dimensione in byte di v. Ma si divide per sizeof(float) ottenendo il numero di elementi di v
    for(i=0; i<n; i++){
        printf("%f\n", w[i]);
    }

}


float *copia_array_di_float(float *a, int n){
    float *b=malloc(n*sizeof(float));

    printf("%d\n", sizeof(a)/sizeof(float)); //la sizeof di un puntatore è 8 in questo caso, quindi non compare 20, bensi 2 (8/4)

    if(b==NULL){
        return NULL;
    }

    for(int i=0; i<n; i++){
        b[i]=a[i];
    }

    return b;

}

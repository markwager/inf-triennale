#include <stdio.h>
//non può essere modificata la locazione statica dell'array durante il programma. Questa memoria è di dimensione limitata
//si possono però avere locazioni dinamiche durante il runtime del programma. Se ne occupa il sistema operativo tramite chiamate di sistema
//si fa attraverso una libreria dove ci sono funzioni che ritornano il primo byte allocato. Ci serve una variabile che possa catturare questi output di tipo indirizzo: il puntatore
#include <stdlib.h>

float *crea_array_di_float(int , float);
float *copia_array_di_float(float*, int); //oppure float *copia_array_di_float(float[], int);

int main()
{
    float *p; //p conterrà indirizzi di memoria che a loro volta contengono float
    //i puntatori non si usano solo per gli array

    float f=3.14; //f è un nome di una porzione di memoria
    //possiamo assegnare a p l'indirizzo di f

    p=&f;//indirizzo in cui è memorizzata f

    *p=0; //sto modificando f perchè punta all'indirizzo di f

    printf("%f, %f\n", f, *p); //se p è un puntatore tira fuori il valore dell'oggetto puntato da p

    p=malloc(sizeof(float));//restituisce un puntatore con input un intero. Questo è il primo array allocato dinamicamente. Restituisce l'indirizzo di un'altra locazione
    printf("sizeof(float): %d\n", sizeof(float));//restituisce il byte
    printf("valore di p: %p\n", p);//restituisce l'esadecimale
    *p=2.71;
    printf("%f, %f\n", f, *p);

    free(p); //riprenditi la zona allocata per p

    p=malloc(2*sizeof(float)); //occupami lo spazio per due float

    if(p==NULL){     //allocazione effettuata
        return -1;
    }

    *p=0.1; //scrivo sul primo float
    *(p+1)=0.2; //p+1 è l'indirizzo del float successivo a quello puntato da p. Quindi scrivo su quello.
    //il suo valore dipende da sizeof(float)
    float f0=*p, f1=*(p+1);
    printf("%f, %f\n", f0,f1);
    printf("%f\n", *(p+2)); //valore che si trova in p+2
    //c'è un erroe logico perchè si legge una posizione di memoria non scitta da noi. Però può essere occupata da un altro processo. Quindi possibile segmentation fault, memoria non allocata
    printf("%f\n", p[1]); //è equivalente a *(p+1)
    printf("%f\n", p[0]); //è equivalente a *p

    free(p);

    p=crea_array_di_float(10,2.71); //inserisci nella funzione la capienza e il valore

    for(int i=0; i<10; i++){
        printf("%f\n", p[i]);
    }

    //con il secondo malloc, si perde il puntatore verso la prima locazione del primo malloc. SI risolve con free(p) per liberare la locazione

    free(p);

    float b[10]={0}; //tutti quanti 0
    p=copia_array_di_float(b,10);//indirizzo dell'array e sua dimensione: ecco il suo prototipo (p è sempre un puntatore)

    for(int i=0; i<10; i++){
        printf("%f\n", p[i]);
    }

}

/*
float *crea_array_di_float(int n , float v){

    float a[n]; //a e un indirizzo. Somiglianza tra a e *p
    for(int i=0; i<n;i++){
        a[i]=v;

    }

    return a; //ritorno l'indirizzo di un float


}

VERSIONE ERRATA: viene restituito l'indirizzo di una variabile locale

*/

float *crea_array_di_float(int n , float v){

    float *a=malloc(n*sizeof(float));//a e un indirizzo. Somiglianza tra a e *p
    if(a==NULL){
        return NULL;
    }
    for(int i=0; i<n;i++){
        a[i]=v;

    }

    return a; //ritorno l'indirizzo di un float
}


float *copia_array_di_float(float *a, int n){
    float *b=malloc(n*sizeof(float));

    if(b==NULL){
        return NULL;
    }

    for(int i=0; i<n; i++){
        b[i]=a[i];
    }

    return b;

}

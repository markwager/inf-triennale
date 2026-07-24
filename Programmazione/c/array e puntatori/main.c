#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//in generale, ogni variabile viene prima definita (dichiarata) e poi inizializzata (le si assegna un valore)
//l'array e una sequenza ordinata di elementi di uno stesso tipo. Possiamo solo leggere l'array e modificare i suoi elementi tramite indici. Non è possibile eliminare
//o inserie e nuovi elementi nell'array (a meno di utilizzare dei trucchetti).

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

    int numeri[]={10,24,21,45,8};
    int len=sizeof(numeri)/sizeof(numeri[0]); //per determinare la lunghezza dell'array
    printf("%d,%d\n", sizeof(numeri), len); //sizeof mi restituisce il peso dell'array in bytes (4*5 numeri, 4 bytes per un intero/float)

    //meglio usare questo for per leggere un array dal momento che possiamo utilizzare sizeof per sapere il numero di elementi
    for(i=0; i<len; i++){
        printf("%d\n",numeri[i]);
    }

    char ringrazia[]="Hello world"; //questa è una stringa, ricordati che stringa non è un tipo di variabile: esiste solo il char
    printf("%s\n", ringrazia); //si usa s per le stringhe

    printf("%c\n", ringrazia[0]); //per leggere un carattere

    ringrazia[0]='o';
    printf("%s\n", ringrazia);


    char alfabeeb[]="ABCDEFGHILMNOPQRSTUVZ";
    printf("%d\n", strlen(alfabeeb)); //strlen ritorna la lunghezza della stringa
    printf("%d\n", sizeof(alfabeeb)/sizeof(alfabeeb[0]));

    //la differenza tra questa e la sizeof, è che quest'ultima conta anche il carattere speciale \0 (quindi +1)

    char str1[20]="Hello sos";
    char str2[20];
    strcpy(str2, str1); //copia str1 in str2
    printf("%s\n", str2);

    printf("%d\n", strcmp(str1, str2)); //ritorna 0 se le stringhe sono uguali, altrimenti un altro valore

    /*--------------------------------------------------------------------------------------------------------------------------------------------------------------*/

    int età=20;

    //quando si crea una variabile, un indirizzo di memoria è assegnato alla variabile                                        
    //quando assegnamo un valore alla variabile, questo è inside l'indirizzo

    /*
        --------------
        | età | 20  |
        --------------   */




    printf("%p", &età); //&variabile ritorna l'indirizzo della variabile in esadecimale
    //inoltre &variabile è un puntatore: un puntatore è una variabile che contiene l'indirizzo di memoria come suo valore

    int* ptr=&età;

    printf("%p\n", ptr); //stampa indirizzo di valore di età
    printf("%d\n", *ptr); //stampa il valore di età

    //posso usare i puntatori per accedere agli array
    //in particolare, il nome di un array è praticamente un puntatore al primo elemento dell'array
    printf("%p\n", numeri); //stampa indirizzo di array
    printf("%p\n", &numeri[0]); //stampa indirizzo di primo elemento di array
    printf("%d\n", *numeri); //stampa il primo valore dell'array, STESSO di numeri[0]
    //per accedere agli altri elementi
    printf("%d\n", *(numeri+1));

    *numeri=77; //modifica il primo elemento dell'array
    *(numeri+1)=90; //modifica il secondo elemento dell'array

    }
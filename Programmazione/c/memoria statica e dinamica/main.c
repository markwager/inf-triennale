#include <stdio.h>
#include <stdlib.h>

int main()
{
    //il c ha due tipi di memoria: statica e dinamica
    //la prima è riservata per le variabili prima dell'esecuzione del programma.
    //c alloca la memoria per ogni variabile quando il programma è compilato
    //tuttavia se hai un array con capacità di 20 elementi e ne usi solo 12, gli altri 8 sprecano spazio e non puoi cambiare la dimensione dell'array
    //per gestire meglio la memoria puoi utilizzare quella dinamica
    //questa permette di riservare spazio per le variabili dopo l'esecuzione del programma
    //ci si può accedere solo tramite puntatori: per allocare usi malloc che ritorna un puntatore alla sua memoria e prende come argomento i byte che servono per allocare memoria
    //se non trova spazio, malloc restituisce NULL

    //per allocare memoria si utilizza sizeof
    int *ptr1;

    ptr1=malloc(sizeof(*ptr1));

    //ATTENZIONE: sizeof(*ptr1) ritorna il numero di byte delle informazioni all'indirizzo. Se dimentichi *, misurerà la grandezza del puntatore stesso
    //ecco come accedere alla memoria

    //alloca la memoria
    int *punt;
    ptr1=malloc(sizeof(*punt)*4); //alloca la memoria per 4 interi

    //scrivi nella memoria
    punt[0]=2; //oppure scrivi *punt=2 per il primo elemento
    punt[1]=4; //oppure scrivi *(punt+1)=4
    punt[2]=6;

    //leggi dalla memoria
    printf("%d\n", punt[0]);
    printf("%d\n", punt[1]);
    printf("%d\n", punt[2]);
    printf("%d\n", punt[3]); //stampa 0 perchè non ci abbiamo scritto sopra

    //se la memoria allocata non è abbastanza, allora puoi riallocarla
    int *ptr2, ptr3, size;

    //alloca la memoria per 4 interi
    size=4*sizeof(*ptr2);
    ptr2=malloc(size);

    //voglio estendere a 6 interi
    size=6*sizeof(*ptr2);
    ptr3=realloc(ptr1, size); //sposta il contenuto di ptr1 in ptr2 con una nuova size
    //realloc ritorna NULL se non può allocare più memoria

    //se non hai più bisogno di un blocco di memoria, liberalo

    free(ptr1);
    ptr1=NULL; //se lo metti a NULL non lo utilizzi più

    //accedere a un elemento sia in lettura che in scrittura su un array comporta un costo temporale costante. Abbiamo già detto che un array normalmente può essere solo
    //letto oppure modificato: non ci è permesso (a meno di utilizzo di trucchetti) cancellare o inserire nuovi elementi nell'array. Ciò non si presenta in Python.
    //Per ovviare a ciò si utilizza la memoria dinamica, quindi array dinamici.
    //Finora si ha utilizzato un array dinamico non troppo genrale costituito da tipo e dimensione. Per questo si introduce anche la capacità e, di conseguenza, una
    //struttura dati chiamata struct (in realtà il prof ha introdotto la sctruct con la capacità per avere un'ottimizzazione della funzione append).

}



//lettura, scrittura, cancellazione, inserimento e ricerca nelle liste (o array dinamici)
//ricerca pef posizione: O(1)
//pop e append: O(n) per n operazioni, una operazione O(1) in media perchè in qualche operazione ci può essere un pop
//inserimento e cancellazione: O(n) nel caso peggiore, nel caso medio bisogna fare una somma dei costa di c*(n-p)=c*(n*(n+1))/2 quindi è O(n)
//ricerca di una chiave: O(n) (stessa cosa nel caso medio)

//nei dizionari:
//ricerca pef posizione: // (gli elementi non occupano una posizione)
//pop e append: // ....
//inserimento e cancellazione: O(1) nel caso medio
//ricerca di una chiave: O(1) nel caso medio

//i dizionari sono strutture che contengono delle coppie composta da chiave e valore
//caratteristiche: le chiavi sono univoche
//un dizionario è una mappa che associa le chiavi ai valori
//operazioni: aggiornamento del valore assoiato alla chiave, altrimenti nulla, appartenenza della chiave al dizionario (operazione di ricerca), cancellazione (rimuovi k da dizionario, altrimenti nulla)
//assunzioni: le chiavi sono stringhe e i valori sono interi e che le chiavi siano composte da 10 byte
//creo una relazione tra la stringa e un indice di un array per implementare il dizionario: a una chiave si associa in maniera univoca una posizione e viceversa
//si può creare quindi un array di una certa dimensione in cui alla posizione p dell'array corrisponde una ed una sola chiave (e viceversa)
//in tempo O(1) posso fare la ricerca (verifica il valore d[p])
//il numero di possibili chiavi è 2^80 (80 bit) 2^80=m
//si deve eliminare la corrispondenza 1 a 1 perchè altrimenti è troppo grande la struttura per via di m
//quindi su un indice potranno ricadere più chiavi (chiamati conflitti: più chiavi stanno sullo stesso indice)
//come gestire conflitti: in una pos dell'array abilitiamo la possibilità di poter inserire più elementi del dizionario, quindi d[p] contiene un insieme di elementi del dizionario
//esiste una chiave dentro il dizionario per cercarla? si deve ottenere in tempo costante la posizione. Bisognerebbe vedere se nell'insieme di elementi del diionario c'è la nostra chiave
//biosgna quindi fare una ricerca lineare dentro quell'insieme, nel numero di elemeni del dizionario dentro d[p], se insieme piccolo allora è costante
//sia m la dim. dell'array, n il num di elementi (chiavi), le chiavi saranno distribuite in maniera uniforme tra tutti gli elementi dell'array
//cioè in una pos generica d[p] ricadono in media n/m chiavi. La ricerca di k ha costo costante oer ottenere p + il costo di n/m per trovare k nell'insieme delle chiavi che ricadono in d[p]
// n/m è costante se n=c*m, c è costante
//da garantire: dato k (potenziale chiave), la funzione che da k calcola la pos. p in cui deve trovarsi k deve avere costo costante (O(1)). Ci serve la funzione h(k,m) che tira fuori p (hash)

//se devo fare una ricerca di chiave nel dizionario, lo faccio all'interno dell'insieme. Deve essere una ricerca veloce, lo si fa grazie a un insieme piccolo (in media costante) (è un riassunto)
//gli array dinamici possono avere come memoria supplementare 4 volte (nel caso peggiore), non usiamo gli array dinamici quindi
//si considera una lista concatenata: abbandoniamo la necessità di avere una ricerca per posizione in tempo costante (viene garantito negli array per via dell'unico blocco di memoria con elementi della stessa posizione)
//ora questa cosa cambia nella lista concatenata: non si necessità di un'unico blocco di memoria con celle consecutive, si spargono quindi in memoria. Sono comunque messi in ordine, però sono fisicamnete messi in zone diverse della memoria
//come si aggregano? si utilizza un puntatore che punta al primo elemento, il quale punterà all'elemento che segue. Il nodo contiene quindi due info (struct): dato, e una variabile di tipo puntatore

#include <stdio.h>
#include <stdlib.h>

//definiamo la struct del nodo

typedef struct nodo{
    float dato;
    struct nodo *succ; //puntatore al successivo nodo

}nodo;

//L è una lista che è un puntatore a nodo
typedef nodo *clista; //lista concatenata

clista clista_vuota(); // funzione per creare una lista vuota
void clista_mostra(clista); // funzione per stampare la lista
nodo *clista_in0(clista, float); // funzione per inserire un nodo in testa alla lista
nodo *clista_cerca(clista, float); // funzione per cercare un nodo nella lista

nodo *clista_cerca(clista a, float k){ //i parametri sono la lista e la chiave

    nodo *p=a; //p punta al primo nodo perchè si parte dalla testa, cioè la lista punta al primo nodo di default

    while(p!=NULL && p->dato!=k){ // fintanto che il puntatore è diverso da NULL, quindi non è l'ultimo, e il dato non corrisponde alla chiave, vado avanti

        p=p->succ; //il puntatore punta al nodo successivo

    }

    return p; // ritorno il puntatore
}

nodo *clista_in0(clista a, float v){

    nodo *p=malloc(sizeof(nodo));
    p->dato=v; // nel nodo p, il campo dato punta alla variabile v
    p->succ=a; //nel nodo p, il campo succ punta alla variabile a
    a=p; //ora a punta al nuovo nodo
    return a;

    //quello che sta succedendo: si crea un puntatore p che il cui campo dato sarà pari al valore v
    //successivamente il campo succ di p sarà pari all'indirizzo a cui punta a (cioè il nodo prima della creazione del nuovo nodo)
    //infine ad a assegno l'indirizzo di p
}


clista clista_vuota(){
    return NULL;
}

void clista_mostra(clista a){

    nodo *p;
    p=a;
    printf("Contenuto della lista-->");
    while(p!=NULL){//che non raggiungo il fine lista, quindi vado avanti fintanto che p!=null

        printf("%f,", (*p).dato); //se p è un punatore, posso accedere ai campi della struct con *p
        p=(*p).succ; //equivalente a p=p->succ;
    }

    printf("\n");

}

int main(){

    clista L0=clista_vuota();
    clista L;

    nodo q={3.14, NULL};

    L0=&q;
    //la nostra lista contiene un nodo in testa alla lista

    nodo p={0.0, NULL};
    p.succ=&q; //per avere p in testa alla lista, si aggiorna il campo null di p. altrimenti scrivo similm. p.succ=L
    L0=&p;//ed L si aggiorna
    clista_mostra(L0);

    /*pochi interessante la parte sopra perchè è un'osservazione preliminare di come funziona la clista----------------------------------------------*/

    L=clista_vuota();

    for(int i=0; i<10; i++){

        L=clista_in0(L,i);
    }
    clista_mostra(L);

    nodo *point=clista_cerca(L, 6);
    if(point!=NULL){
        printf("%f\n", point->dato);
    }
    else{

        printf("Non trovato\n");
    }
}

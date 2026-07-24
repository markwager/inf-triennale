//come concludere l'implementazione dela struttura dati in c
//ho unn insieme di elementi composti da coppie: chiave univoca+valore (di tipo intero)=coppia in dizionario, le chiavi sono strighe di lunghezza arbitraria.
//ricerca, aggiornamento e cancellazione devono essere implementate su C come su Python
//bisogna vedere le chiavi k come indice di un array, così si fa un accesso in tempo costante perchè l'indicizzazione sugli array ha tempo costante
//non possiamo però garantire che per ogni chiave ci sia un diverso indice del mio array
//si utilizza perciò una funzione h(k) (hash) data una chiave mi ritorna un indice dell'array dove memorizzare la chiave col suo valore (quindi l'elemento, se v è il valore associato alla chiave k)
//è quindi una funzione calcolabile in tempo costante quindi ed è deterministica (mi da sempre lo stesso risultato). Quindi h(k) mi da la posizione in cui inserire l'elemento.
//ci possono essere delle collisioni (cioè le coppie h(k1)=h(k2 quindi portano alla stessa posizione) però che si gestiscono attraverso l'inserimento dei due elementi nella stessa lista (di trabocco) nella pos p di d (array di liste)
//tutto è efficiente quando la dimesnione delle liste di trabocco è più piccola rispetto alla dimensione del dizionario. Da garantire: dimensione media di una lista sia costante. In questo modo quando facco ricerca, se la lista, è piccola l'operazione è efficiente
//la ricerca è composta da due passi: 1) calcolo l'indice con h(k) 2) cerco la chiave in pos p del dizionario
//quindi il dizionario sarà un array d di dimensione m. Se n è il numero di elementi del dizionario (dim dizionario) e m è il numero di liste di trabocco-->n/m (quando m cresce aumento n) deve essere costante e poi deve essere
//anche vero che gli n elementi sono distribuiti in maniera uniforme tra le m liste. La funzione h deve sparpagliare bene gli elementi.
//la distribuzione omogenea dipenderà dalla funzione h
//la funzione h deve essere deterministica, calcolabile in tempo costante e che mi dia la garanzia che gli elementi siano distribuiti uniformemente.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct ditem{

    char *k; //stringa (chiave)
    int *v; //valore

}ditem; //item del dizionario, coppia chiave-valore, quindi l'elemento

typedef struct nodo{
    ditem dato;
    struct nodo *succ, *prec; //puntatore a nodo precedente

}nodo;

//L è una lista che è un puntatore a nodo
typedef nodo *clista; //lista concatenata

typedef struct dict{

    clista *a; //array di clista
    int m; //dimensione

}dict; //dizionario con m liste di trabocco

int h(char *k, dict d){ // funzione hash che dipende da chiave e da dizionario

    return 0; // mi ritorna sempre 0 per fare i primi esperimenti: abbiamo un'unica lista di trabocco

}

/*dizionario*/
dict dict_init();
int dict_cerca(dict, char*); 
dict dict_add_item(dict, char*, int);
void dict_mostra(dict);
int dict_get(dict, char*);
dict dict_del(dict, char*);

/* lista concatenata */
clista clista_vuota();
nodo *clista_cerca(clista, char*);
nodo *clista_in0(clista, ditem);
void clista_mostra(clista);
nodo *clista_out(clista, char*);
nodo *clista_out0(clista);
clista clista_vuota(){
    return NULL;
}

int dict_cerca(dict d, char *k){ //ritorna 1 se la chiave k appartiene al dizionario
    int i = h(k, d);
    nodo *p = clista_cerca(d.a[i], k);
    
    if (p == NULL)
        return 0;
    else
        return 1;
}

nodo *clista_in0(clista a, ditem v){

    nodo *p=malloc(sizeof(nodo));
    p->dato=v;
    p->succ=a;
    p->prec=NULL;
    if(a!=NULL)
        a->prec=p;
    a=p;
    return a;

}

dict dict_init(){

    dict d={NULL,7}; //campo clista e il campo m
    d.a=malloc(d.m*sizeof(clista)); //alloco memoria per array dinamico
    for(int i=0; i<d.m;i++){

        d.a[i]=clista_vuota();

    }
    return d;

}

int dict_get(dict d, char *k){ //ritorna il valore associato alla chiave
    /*
     * verificare prima che  dict_cerca(d, k) != 0
     * 
     * */
    
    int i = h(k, d);
    nodo *p = clista_cerca(d.a[i], k);
    
    return p->dato.v;
}

dict dict_add_item(dict d, char *k, int v){

    int i=h(k,d); //indice del dizionario che contiene la lista in cui devo andare a cercare
    nodo *p=clista_cerca(d.a[i], k); //devo avviare una ricerca su una clista per cercare la chiave. Mi ritorna la posizioneche ci ha ritornato la funzione
    if(p!=NULL){ //k è una chiave del dizionario, aggiorno il valore. Cioè chiave è già presente nel dizionario
        p->dato.v=v;
    }

    else{ //se non esiste creiamo un nuovo item in testa

        ditem itm={NULL,v};  //si mette NULL per garantitre per ora l'immutabolità della chiave
        //poi ci inserirò un puntatore a una copia di k
        itm.k=malloc(sizeof(char)*strlen(k)+1);
        strcpy(itm.k,k); //strcpy non pensa all'allocazione di memoria
        d.a[i]=clista_in0(d.a[i], itm);
    }

    return d;

}

nodo *clista_cerca(clista a, char *k){

    nodo *p=a; 

    while(p!=NULL && strcmp(p->dato.k, k)!=0){

        p=p->succ;

    }

    return p;

}

void dict_mostra(dict d){

    int i;
    for(i=0; i<d.m;i++){
        printf("d[%d]",i);
        clista_mostra(d.a[i]);
    }
}

void clista_mostra(clista a){
    nodo *p;
    
    p = a;
    
    while( p != NULL ){ 
        printf("(%s, %d), ", p->dato.k, p->dato.v); 
        p = p->succ; 
    }
    
    printf("\n");
}

clista clista_out(clista a, char *k){
    nodo *p = clista_cerca(a, k);
    if (p == NULL)
        return a;
    
    nodo *q = p->prec;
    
    if ( q == NULL){ // p e' il primo nodo della lista ovvero p == a
        return clista_out0(p);
    }
    
    q->succ = clista_out0(q->succ);
    if (q->succ != NULL)
        q->succ->prec = q;
    
    return a;
        
}

clista clista_out0(clista a){
    clista p = a;
    if( a == NULL)
        return NULL;
    a = a->succ;
    if (a != NULL)
        a->prec = NULL;
    free(p->dato.k); //dealloca memoria per la chiave perchè si ha una memoria dinamica
    free(p);//e poi per il nodo
    return a;
}

dict dict_del(dict d, char *k) {
    int i = h(k, d);
    
    d.a[i] = clista_out(d.a[i], k);
        
    return d;
}


int main(){

    dict d = dict_init(); //crea un dizionario vuoto
    
    d = dict_add_item(d, "chiave0", 0);
    d = dict_add_item(d, "chiave1", 1);
    d = dict_add_item(d, "chiave0", 10);
    d = dict_add_item(d, "chiave2", 2);
    d = dict_add_item(d, "chiave1", 11);
    
    dict_mostra(d);
    
    if ( dict_cerca(d, "chiave2") )
        printf("%d\n", dict_get(d, "chiave2"));
        
    d = dict_del(d, "chiave0");
    dict_mostra(d);
    
}

/*----------------------------------RIASSUNTO--------------------------------*/
//Proprietà funzione h:
//output in 0,....,d.m-1
//funzione deterministica e facile da calcolare (costo O(1) non dipendente da d.m, efficiente)
//può dipendere dalla dimensione della chiave (soltanto)
//su n stringhe (chiavi) distinte il numero di volte in cui h(k,d) è i deve essere circa n/d.m (la probabilità che il valore risultante sia i è n/d.m) (questa sarà la dim media delle liste di trabocco)
/*----------------------------------IMPLEMENTAZIONE FUNZIONE H--------------------------------*/
//creo una funzione a parte, hsomma, il cui parametro è una stringa. La funzione ha un intero inizializzato a 0 e con un while sommo ad h k, incrementiamo poi il puntatore che punta all'elemento successivo
//si ritorna poi il resto di hsomma
//creiamo un dizionario più complesso creando un array, il quale, sarà composto da stringhe. Dopodichè aggiungiamo con un for per il dizionario il dataset (cioè l'array)
//funzione djb2 (acronimo del tizio che ha inventato la funzione) parte da un valore h che ha un valore "strano" (5381), lo aggiorna poi facendo 33*valore strano+tutti i caratteri
//si ritorna poi h. 5381 è un numero dispari
//questa funzione viene utilizzata e ci da la possibilità di introdurre gli operatori bit a bit: posso eseguire l'operazione del cambio di valore in modo diverso
//in c è possibile spostere i bit prendendo il valore strano (<< 5). Lo spostamento bit a bit è più veloce, ecco perchè si usa.
//I diversi operatori sono or, and e xor

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct ditem {
        char *k;  // chiave
        int v; // valore
    } ditem;  // item del dizionario, coppia chiave-valore

typedef struct nodo {
    ditem dato;
    struct nodo *succ, *prec;
} nodo;

typedef nodo *clista; // lista concatenata

typedef struct dict {
    clista *a;
    int m;
    } dict;  // dizionario con m liste di trabocco
    

int h(char*,dict);

/* dizionario*/
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

int main(){
    dict d = dict_init();
    
    //array di stringhe, se togliamo * diventa array di caratteri
    char *dataset[] = {"davide","valerio", "dannis", "elisa", "vanessa", "francesca", "sergio", "jacopo", "massimo", "ludovico", "anastasia", "edoardo", "pierre", "valerio", "ginevra", "domenico", "whendy", "mateo", "tommaso", "simone", "mario", "antonio"};
    
    int n = sizeof(dataset)/sizeof(char*); //dimesione dell'array
    
    for(int i = 0; i < n; i++){
        d = dict_add_item(d, dataset[i], i);
    }
    
    dict_mostra(d);
    
}


int hsomma(char *k){
    int h = 0;
    
    while ( *k != '\0' ){
        h += *k;
        k++;
    }
    
    return h;
}

int djb2(char *k){
    int h = 5381;
    
    while ( *k != '\0' ){
        //h = 33*h + *k;  = 32*h + h + *k = h*(2**5) + h + *k
        h = (h << 5) + h + *k; /* altri operatori bit a bit >>, | or, & and, ^ xor */
        // è un'operazione equivalente perchè spostare a sinistra dei bit equivale all'operazione del moltiplicare per 2^5
        //cioè: (h << 5) + h == h*(2**5) + h == 32*h + h
        
        
        /* 10011 equivale 1+(2**0) + 1+(2**1) + 0*(2**2) + 0*(2**3) + 1*(2**4) = 19
         * 
         * 
         * 10011<<2 ......    1001100 = 19*4
         * 10011>>2 ......    100
         * 10011|     OR
         *   101
         * ------
         * 10111
         * 
         * 10011&    AND
         *   101
         * ------
         * 00001
         * 
         * 10011^     XOR
         *   101
         * ------
         * 10110
         * 
         * */
        
        k++;
    }
    
    return h;
}

int h(char *k, dict d){
    /*
     * Proprieta'
     * 
     * - output in 0,...,d.m-1
     * - funzione deterministica ed efficiente, costo O(1) non dipendente da d.m
     * - su n stringhe distinte il numero di volte in cui h(k, d) e' i deve essere
     *      circa n/d.m (questa sara' la dimensione media delle liste di trabocco)
     * 
     * */
    
    
     
    //return hsomma(k) % d.m;
    return djb2(k) % d.m; //funzione meglio
}


dict dict_del(dict d, char *k) {
    int i = h(k, d);
    
    d.a[i] = clista_out(d.a[i], k);
        
    return d;
}

int dict_get(dict d, char *k){
    /*
     * verificare prima che  dict_cerca(d, k) != 0
     * 
     * */
    
    int i = h(k, d);
    nodo *p = clista_cerca(d.a[i], k);
    
    return p->dato.v;
}

int dict_cerca(dict d, char *k){
    int i = h(k, d);
    nodo *p = clista_cerca(d.a[i], k);
    
    if (p == NULL)
        return 0;
    else
        return 1;
}

void dict_mostra(dict d){
    int i;
    
    for(i = 0; i < d.m; i++){
        printf("d[%d] = ", i);
        clista_mostra(d.a[i]);
    }
}

dict dict_add_item(dict d, char *k, int v){
    int i = h(k, d);
    nodo *p = clista_cerca(d.a[i], k);
    
    if( p!=NULL ){ // k e' una chiave del dizionario, aggiorno il valore 
        p->dato.v = v;
    } else {
        ditem itm = {NULL, v};
        itm.k = malloc(sizeof(char)*(strlen(k)+1));
        strcpy(itm.k, k);
        d.a[i] = clista_in0(d.a[i], itm);
    }
    
    return d;
}

dict dict_init(){
    dict d = {NULL, 7};
    
    d.a = malloc(d.m*sizeof(clista));
    
    for(int i=0; i < d.m; i++)
        d.a[i] = clista_vuota();
    
    return d;
}

clista clista_out0(clista a){
    clista p = a;
    if( a == NULL)
        return NULL;
    a = a->succ;
    if (a != NULL)
        a->prec = NULL;
    free(p->dato.k);
    free(p);
    return a;
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

void clista_mostra(clista a){
    nodo *p;
    
    p = a;
    
    while( p != NULL ){ 
        printf("(%s, %d), ", p->dato.k, p->dato.v  ); 
        p = p->succ; 
    }
    
    printf("\n");
}

nodo *clista_in0(clista a, ditem v){
    nodo *p = malloc(sizeof(nodo));
    p->dato = v;
    p->succ = a;
    p->prec = NULL;
    if (a != NULL)
        a->prec = p;
    a = p;
    return a;
}

nodo *clista_cerca(clista a, char *k){
    nodo *p = a;
    
    while( p != NULL && strcmp(p->dato.k, k)!=0 ){
        p = p->succ;
    }
    
    return p;
}


clista clista_vuota(){
    return NULL;
}
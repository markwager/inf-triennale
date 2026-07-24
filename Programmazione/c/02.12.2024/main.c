#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int str_cmp(char*, char*);


int str_len(char *a){
    int c=0;

    while(a[c]!='\0'){

        c++;

    }

    return c;
    //complessità temporale = O(n)
}

int main()
{
    //una stringa è una sequenza di caratteri che termina con un carattere speciale: fine stringa (\0)
    //è memorizzata in un array di caratteri

    //come posso definire una stringa

    char a[]="una stringa"; //array composto dai caratteri mostrati + carattere \0
    char b0[1000];
    char *b1;
    //b si può definire come statico o dinamico

    char stringa_vuota[]=""; //l'array contiene \0 in pos 0

    printf("%d\n", sizeof(a));

    printf("%s\n", a);

    a[3]='\0'; //definisce la stringa  "una"

    printf("%s\n", a, str_len(a));

    printf("str_len(\"%s\")=%d\n", a, strlen(a));

    //copia di una stringa come si fa?

    strcpy(b0, a); //stringa destinazione e stringa da copiare


    printf("str_len(\"%s\")=%d\n", b0, strlen(b0));

    b1=malloc(sizeof(char)*(strlen(a)+1)); //strlen ritorna il numero di caratteri veri (non il fine stringa)

    strcpy(b1, a); //costo lineare

    printf("str_len(\"%s\")=%d\n", b1, strlen(b1));

    //ex: scrivere una funzione col seguente prototipo:
    //clona(char *a) //data un stringa ritorna la stessa stringa
    //questa funzione copia a in una nuova stringa allocata dinamicamente e ne ritorna
    //l'indirizzo
    //ritorna NULL se l'operazione non è possibile

    //come faccio a testare se una stringa è uguale a un'altra struttura
    //voglio testare se a e b0 sono uguali
    //uguali come stringhe, ma non come array

    //a==b0?? no! stiamo verificando se i due indirizzi sono uguali

    char c[]="programmazione";
    char d[]="programma";
    char e[]="prolog";
    char f[]="prolog";

    printf("%d\n", str_cmp(c,d));
    printf("%d\n", str_cmp(d,e));
    printf("%d\n", str_cmp(e,f));

}

    int str_cmp(char *a, char *b){


        //a e b sono due stringhe. Ritorna -1 se a precede b nell'ordinamento lessicografico
        //ovvero se i è la prima posizione in cui a e b divergono, allora a[i]<b[i]

        //ritorna +1 quando b precede a
        //ritorna 0 quando a e b sono uguali

        int i=0;

        while(i<strlen(a) && i<strlen(b) && a[i]==b[i]){

            i++;
        }

        //costo quadratico il while: non efficiente
        //ciò e dovuto alle strlen all'interno del while

        //cme riparare?

        //int na= strlen(a), nb=strlen(b)

        //e usare na e nb dove serve

        if(i==strlen(a)){

            if(i<strlen(b)){

                return -1;

            }

            else{

                return 0;

            }

        }

        if(i==strlen(b)){

            return +1;
        }

        if(a[i]<b[i]){
            return -1;
        }
        else{
            return +1;

        }


    }

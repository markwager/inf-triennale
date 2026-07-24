#include <stdio.h> //questo è un file e serve nella precompilazione: prende il file e lo inserisce nella prima riga
//ci sono i prototipi delle fuznioni di quella libreria

//possiamo dare in pasto al compliatore die prototipi per non essere oppressi dall'ordine delle funzioni
float my_sqrt(float, int);
float my_abs(float a);
char maiuscola_to_minuscola(char);
//il nome delle variabili è facoltativo
//cosi il compilatore si risparmia di fare delle ipotesi se le due funzioni dovessero invertirsi (per esempio si risparmia la collisione)

float my_abs(float a){
    if (a<0){
    return -a;
    }

    else{
    return a;
    }
}
//sto ritornando un float


float my_sqrt(float x, int max_iter)
{
    float g=x/2;
    int c=0;
    while (my_abs(g*g-x)>0.00001 && c<max_iter){
        g=(g+x/g)/2;
        c++;
    }

    return g;
}

char maiuscola_to_minuscola(char c){
    if (c>='A' && c<='Z'){  //codifica di A che e un intero in realtà

        int d=c-'A';//quanti caratteri ci sono tra c e A
        return 'a'+d;
    }

    return -1;


}



//se scambiassimo l'ordine delle due funzioni soprastanti, allora ci sarebbe un errore di conflitto per via del protoripo pensato dal compilatore

int main()
{
    //non abbiamo la potenza in c tra le operazioni aritmetiche

    int a=3, b=2;
    float c=a/b; // a/b e un intero per via di a e b
    float d=(1.0*a)/b;
    float e=(a/b)*1.0; //fa 1
    float f=(float)a/b; //casting esplicito: conversione da int in un float
    // a/b è un casting implicito
    printf("%f, %f,%f,%f\n",c,d,e,f);
    //dovrebbe stampare 1.5 ma non è cosi perchè a/b è un intero
    //divisione tra float e int è un float
    char ch='h';
    printf("%c, %c, %d, %d\n",ch,ch+1,ch,ch+1);
    printf("%c\n", maiuscola_to_minuscola('G'));

    printf("Radice quadrata di 2: %f\n", my_sqrt(2,2)); //printf e una funzione, fa parte di una libreria esterna, non fa parte del linguaggio (assume di default che il tipo sia int)
    printf("Radice quadrata di 2: %f", my_sqrt(2,200));

    //le operazioni relazionali sono le solite
    //le operazioni logiche

}

//in c non esiste il tipo string, bensi il tipo char (carattere)
//il tipo char è un intero
//i char della tastiera hanno una codifica numerica: ASCII

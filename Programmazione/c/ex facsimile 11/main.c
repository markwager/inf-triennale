/*
Scrivi un programma che legga le coordinate di un punto 2D da input usando scanf e calcoli la sua distanza dall'origine (0,0).
------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivi un programma che legga un numero intero dall'utente usando scanf. Verifica se il numero è pari o dispari.
------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivi un programma che legga una stringa nel formato x=5 y=10 z=15 e usi sscanf per estrarre i valori di x, y e z. Stampa i valori letti.
------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivi un programma che legga tre numeri interi dall'utente usando scanf, calcoli la loro somma e la loro media e stampi i risultati.
------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivi un programma che legga una stringa dall'utente usando scanf e conti quante parole contiene. Considera che le parole sono separate da spazi.
------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivi un programma che legga un numero intero n che rappresenta la dimensione di un vettore, quindi legga n numeri interi. Alla fine, stampa i numeri inseriti.
------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivi un programma che chieda all'utente di inserire un numero reale e controlli se l'input è nel formato corretto usando sscanf. Se l'input non è valido, chiedi all'utente di
riprovare.
------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivi un programma che legga due stringhe dall'utente usando scanf e confronti se sono uguali.
*/

#include <stdlib.h> // Necessario per malloc e free
#include <stdio.h> 
#include <string.h>

float my_abs(float );
float potenza(float, int);
float radice_quadrata(float);

float my_abs(float a){
    if (a < 0) {
        return -a;
    } else
        return a;
}

float radice_quadrata(float x){
    float g;  /* Dichiarazione */
    
    g = 5; // inizializzazione

    while ( my_abs( g*g - x ) > 0.00001 ) {
        g = ( g + x/g )/2;
    }

    return g;
}

float potenza(float x, int e){
    int pe;
    float pow = 1;
    
    if (e < 0)
        pe = -e;
    else
        pe = e;
        
    while (pe > 0){
        pow *= x;
        pe--;
    }
    
    if ( e < 0 )
        pow = (1.0)/pow;
        
    return pow;
}


int main0(){

    float x,y;
    printf("Inserisci le coordinate del punto: ");
    scanf("%f %f",&x,&y);
    float somma=potenza(x,2)+potenza(y,2);
    float distanza=radice_quadrata(somma);
    printf("La distanza dal punto (0,0) e': %f",distanza);
    printf("\n");

    int numero;
    printf("Inserisci un numero: ");
    scanf("%d",&numero);
    if (numero%2==0)
        printf("Il numero e' pari");
    else
        printf("Il numero e' dispari");
    printf("\n");

    char stringa[100];
    printf("Inserisci la stringa nel formato x=%%d y=%%d z=%%d: ");
    int a,b,c;
    if(sscanf(stringa, "x=%d y=%d z=%d", &a, &b, &c) == 3) {
        printf("x=%d y=%d z=%d\n", a, b, c);
    }

    else {
        printf("Errore nel formato della stringa.\n");
    }

    int p,q,r;
    printf("Inserisci tre numeri interi: ");
    scanf("%d %d %d", &p, &q, &r);
    float somma1=p+q+r;
    float media=somma1/3;
    printf("La somma dei tre numeri e': %f",somma1);
    printf("\n");
    printf("La media dei tre numeri e': %f",media);
    printf("\n");

    int numero1;
    printf("Inserisci un numero: ");
    scanf("%d",&numero1);
    int *array=malloc(numero1*sizeof(int));
    for(int i=0;i<numero1;i++){
        printf("Inserisci i numeri %d: ",i+1);
        scanf("%d",&numero1);
        array[i]=numero1;
    }

    for(int j=0;j<numero1;j++){
        printf("%d ",array[j]);
    }

    printf("Inserisci una stringa: ");
    char stringa1[100];
    scanf("%s",stringa1);
    int parole=0;
    for(int i=0;i<strlen(stringa1);i++){
        if(stringa1[i]==' '){
            parole++;
        }
    }
    parole++;
    printf("La stringa contiene %d parole",parole);

}

int main1(){
    char stringa[100];
    float g;
    int valid = 0; // Flag per verificare l'input valido
    while (valid==0){
        printf("Inserisci un numero reale: ");
        scanf("%s", stringa);
        int t=sscanf(stringa, "%f", &g);
        if (t==1){ 
            valid = 1;
        }

        else {
            printf("Input non valido. Riprova.\n");
        }
    }
}

int main(){
    printf("Inserisci due stringhe: ");
    char stringa[100];
    scanf("%s %s", stringa, stringa);
    if (strcmp(stringa, stringa) == 0)
        printf("Le stringhe sono uguali");
    else
        printf("Le stringhe sono diverse");
}






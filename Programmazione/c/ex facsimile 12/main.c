/*
Scrivere una funzione in C che, data una stringa a, rimuove da a tutti i caratteri che non sono in ordine lessicografico con i precedenti a partire dal primo simbolo.
Dopo l'operazione a risulterà ordinata lessicograficamente.
--------------------------------------------------------------------------------------------------------------------------------
Scrivere una funzione in C che, date in input due stringhe a e b, crea una nuova stringa che è la concatenazione delle due stringhe.
In particolare, se a precede o è uguale a b, allora la concatenazione deve avere prima la stringa a e poi b; viceversa, se b precede a,
allora la concatenazione deve avere prima la stringa b e poi a.
----------------------------------------------------------------------------------------------------------------------------------
Scrivere una funzione in C che, data in input una stringa a, la sua lunghezza n e due interi i, j con i <= j, crea una nuova stringa che è la sottostringa di a compresa
tra gli indici i e j. La funzione ritorna l'indirizzo in cui è memorizzata la stringa appena creata in questo modo.
----------------------------------------------------------------------------------------------------------------------------------
*/

#include <stdlib.h> // Necessario per malloc e free
#include <stdio.h> // Necessario per printf
#include <string.h>

void prefix(char*);

char *newstring(char*, char*);

char *substring(char*, int, int, int);

char *substring(char *s, int i, int j, int n){

    char *substringa=malloc(n*sizeof(char));
    int k=0;

    if(i>j){
        return NULL;
    }

    for(int l=i;l<j;l++){
        substringa[k]=s[l];
        k++;
    }
    return substringa;
}

char *newstring(char *a, char *b){
    int n0=strlen(a);
    int n1=strlen(b);
    int n=n0+n1;
    char *newstringa=malloc(n*sizeof(char));
    if(strcmp(a,b)<=0){
        for(int i=0;i<n0;i++){
            newstringa[i]=a[i];
        }

        for(int i=0;i<n1;i++){
            newstringa[n0+i]=b[i];
        }
        
    }

    else{
        for(int i=0;i<n0;i++){
            newstringa[i]=a[i];
        }

        for(int i=0;i<n1;i++){
            newstringa[n0+i]=b[i];
        }
    }

    return newstringa;

}

void prefix(char *s){
    char massimo=s[0]; 
    int i=0;
    while (s[i]!='\0'){
        
        if(s[i]<massimo){ //se il carattere è minore del massimo, lo rimuovo
            for(int j=i;j<strlen(s);j++){
                s[j]=s[j+1];
                
            }
        
        }

        else if(s[i]>=massimo){ //se il carattere è maggiore o uguale al massimo, lo sostituisco

            massimo=s[i];
            i++;
            
        }
    }
}

/*
Oppure si può usare questo per avere una maggiore efficienza:

#include <stdio.h>
#include <string.h>

void rimuovi_non_ordinati(char *a) {
    if (a == NULL || a[0] == '\0') return; // Se la stringa è vuota, non fare nulla
    
    int j = 1; // Indice per la posizione corretta nella stringa modificata
    for (int i = 1; a[i] != '\0'; i++) {
        if (a[i] >= a[j - 1]) { // Mantieni solo i caratteri in ordine
            a[j] = a[i];
            j++;
        }
    }
    a[j] = '\0'; // Termina la stringa
}

int main() {
    char str[] = "cbadefgz"; // Esempio di input
    printf("Stringa originale: %s\n", str);
    
    rimuovi_non_ordinati(str);
    
    printf("Stringa filtrata: %s\n", str);
    return 0;
}

*/

int main(){
    char a[] = "ddabeceffgfh";
    prefix(a);
    printf("%s", a);
    printf("\n");

    char x[] = "abc";
    char y[] = "def";
    char *z=newstring(x,y);
    printf("%s", z);
    printf("\n");

    char c[] = "caccapipi";
    int n=strlen(c);
    //senza sarebbe sizeof(c)/sizeof(char) meno 1;
    char *d=substring(c,2,5,n);
    printf("%s", d);
}
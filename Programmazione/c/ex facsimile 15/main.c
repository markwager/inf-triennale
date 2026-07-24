#include<stdlib.h>
#include<stdio.h>
#include<string.h>

struct array_int{
    int *a;
    int n;
};
typedef struct array_int array_int;

array_int posizione_vocali(char*);

array_int posizione_vocali(char *a){
    array_int p;
    p.a=malloc((strlen(a)+1)*sizeof(int));
    p.n=0;
    for(int i=0;i<strlen(a);i++){
        if(a[i]=='a' || a[i]=='e' || a[i]=='i' || a[i]=='o' || a[i]=='u' || a[i]=='A' || a[i]=='E' || a[i]=='I' || a[i]=='O' || a[i]=='U'){
            p.a[p.n]=i;
            p.n++;
        }
    }
    
    return p;
}

int main(){
    char c[]="ciao";
    array_int p=posizione_vocali(c);
    printf("Posizioni delle vocali: ");
    for (int i = 0; i < p.n; i++) {
        printf("%d ", p.a[i]);
    }
    printf("\nNumero di vocali: %d\n", p.n);
    
}
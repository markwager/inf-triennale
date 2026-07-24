#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char *prefix(char *a, int n){
    char *stringa=malloc(n*sizeof(char));

    if(n>=strlen(a)){
        for(int i=0; i<strlen(a)+1; i++){
            stringa[i]=a[i];
        }
    }

    else{
        for(int i=0; i<n; i++){
            stringa[i]=a[i];
        }
    }

    return stringa;
}

int main(){
    char a[]="ciao";
    char *b=prefix(a,9);
    printf("%s",b);
}
#include <stdio.h>
#include <stdlib.h>



float *inserisci_media(float *a, int n){

    float media=0;
    for(int i=0;i<n;i++){
        media+=a[i];
    }
    media=media/n;
    a[n]=media;
    return a;

}


int main(){

    int n=4;
    float *a=malloc(sizeof(float)*n);
    for(int i=0;i<n;i++){
        a[i]=i;
    }

    float *res=inserisci_media(a,n);

    for(int j=0;j<n+1;j++){
        printf("%f ", res[j]);
    }

}
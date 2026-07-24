#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
scrivere una fuinzione sort_by_vocals che prende in input una stringa e restituisce la stringa ordinata per vocali. Il prototipo è questo: void sort_by_vocals (char *a)
si deve rispettare l'ordinamento lessico grafico anche per tutti gli altri caratteri
*/

void sort_by_vocals(char *a){
    
    char voc[100];
    char caratt[100];
    int index0=0;
    int index1=0;
    
    int len=strlen(a);
    for(int i=0; i<len;i++){
        if (a[i]=='A' || a[i]=='E' || a[i]=='I' || a[i]=='O' || a[i]=='U' || a[i]=='a' || a[i]=='e' || a[i]=='i' || a[i]=='o' || a[i]=='u'){
            
            voc[index0]=a[i];
            index0++;
        }
        else{
            caratt[index1]=a[i];
            index1++;
        }
    }
    
    for (int i = 0; i < index0 - 1; i++) {
        for (int j = 0; j < index0 - i - 1; j++) {
            if (voc[j] > voc[j + 1]) {
                // Scambia gli elementi
                char temp = voc[j];
                voc[j] = voc[j + 1];
                voc[j + 1] = temp;
            }
        }
    }
    
    for (int i = 0; i < index1 - 1; i++) {
        for (int j = 0; j < index1 - i - 1; j++) {
            if (caratt[j] > caratt[j + 1]) {
                // Scambia gli elementi
                char temp1 = caratt[j];
                caratt[j] = caratt[j + 1];
                caratt[j + 1] = temp1;
            }
        }
    }
    
    for(int i=0; i<index0; i++){
        a[i]=voc[i];
    }
    
    for(int j=0; j<index1; j++){
        a[j+index0]=caratt[j];
    }
    
    a[index0 + index1] = '\0';
    
    printf("%s",a);
    
}

int main() {
    
    char a[]=".pr0grAmMaz1onE-C*";
    sort_by_vocals(a);
}
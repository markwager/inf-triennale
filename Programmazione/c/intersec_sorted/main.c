#include <stdio.h>
#include <stdlib.h>

int *intersec(int *a, int *b, int len1, int len2){
    
   int i = 0, j = 0, pos = 0;
    int *array = malloc((len1 + len2) * sizeof(int));

    while (i < len1 && j < len2) {
        if (a[i] == b[j]) {
            if (pos == 0 || array[pos - 1] != a[i])
                array[pos++] = a[i];
            i++;
            j++;

        }

        else if (a[i] < b[j]) {

            i++;
        }

        else {

            j++;
        }
    
    
}

return array;

}

int main(){
    
    int a[] = {2, 5, 6, 8, 8, 8, 8, 10, 12, 13};
    int b[] = {0, 0, 0, 1, 2, 3, 4, 5, 6, 13};
    int len1=sizeof(a)/sizeof(int);
    int len2=sizeof(b)/sizeof(int);
    int *array=intersec(a,b, len1, len2);
    int n=sizeof(array)/sizeof(int);
    
    int len_intersec = 0;
    for (int i = 0; i < (len1 + len2); i++) {
        if (array[i] != 0) {  // Identifichiamo l'elemento finale valido
            len_intersec++;
        }
    }

    // Stampa l'array risultante
    for (int x = 0; x < len_intersec; x++) {
        printf("%d ", array[x]);
    }
}
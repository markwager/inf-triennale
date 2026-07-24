#include <stdio.h>
#include <stdlib.h>


int *copia_array_di_int_conc(int *, int, int *, int);

int *copia_array_di_int_conc(int *a, int size0, int *b, int size1){
    int *c=malloc((size0+size1)*sizeof(int));

    if(c==NULL){
        return NULL;
    }

    for(int i=0; i<size0; i++){
        c[i]=a[i];
    }

    for(int j=0; j<size1; j++){
        c[size0+j]=b[j];
    }

    return c;

}

int main()
{
    int a[]={1,2,3,4,5};
    int b[]={6,7,8,9};
    int size0=sizeof(a)/sizeof(int);
    int size1=sizeof(b)/sizeof(int);
    int *w=copia_array_di_int_conc(a, size0, b, size1);
    for(int i=0; i<size0+size1; i++){
        printf("%d\n", w[i]);
    }
}


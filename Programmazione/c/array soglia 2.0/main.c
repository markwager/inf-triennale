#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
  int *a;
  int n; //dim array
} array_int;

array_int applica_vocali(char *, int);
array_int applica_vocali(char *a_int, int n) {
  array_int x = {NULL, 0};
  int i, j = 0;

  for (i = 0; i < n; i++) {
    if (a_int[i] == 'a' || a_int[i] == 'e' || a_int[i] == 'i' || a_int[i] == 'o' || a_int[i] == 'u'|| a_int[i] == 'A' || a_int[i] == 'E' || a_int[i] == 'I' || a_int[i] == 'O' || a_int[i] == 'U')
      x.n += 1;
  }

  // alloco un array di dimensione pari al numero di interi <= di soglia
  x.a = malloc(sizeof(char) * x.n);

  // copio gli indici degli interi < di soglia all'interno dell'array appena allocato
  for (i = 0; i < n; i++) {
    if (a_int[i] == 'a' || a_int[i] == 'e' || a_int[i] == 'i' || a_int[i] == 'o' || a_int[i] == 'u'|| a_int[i] == 'A' || a_int[i] == 'E' || a_int[i] == 'I' || a_int[i] == 'O' || a_int[i] == 'U') {
      x.a[j] = i;
      j++;
    }
  }

  return x;
}

/*
 * Numero di operazioni: lineare (scansiono tutta la stringa due volte, quindi
 * 2n operazioni).
 * la memoria supplementare utilizzata è costante.
 * */

int main() {
  char b[] = "Algoritmi";
  int n = strlen(b)+1;

  array_int x = applica_vocali(b, n);

  for (int i = 0; i < x.n; i++)
    printf("%d\n", x.a[i]);
}


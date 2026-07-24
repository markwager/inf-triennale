#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct {
  char tipo; // 'i' intero; 'f' float; 's' stringa
  void *dato;
} elemento;

typedef struct {
  elemento *a;
  int c;
  int n;
} lista;

lista init();
lista append(lista, elemento); // aggiunge un elemento alla lista 
void stampa(lista); // stampa la lista 
lista pop(lista); // elimina l'ultimo elemento della lista e lo restituisce
lista delete(lista, int); // elimina l'elemento in posizione p e lo restituisce

elemento intero(int); // restituisce un elemento intero
elemento fpoint(float); // restituisce un elemento float
elemento stringa(char *); // restituisce un elemento stringa

lista delete(lista L, int p) { //i parametri sono la lista e la posizione da eliminare

  if (p < 0) // se la posizione e' negativa, la posizione sara' 0
    p = 0;
  if (p > L.n) // se la posizione e' maggiore della dimensione della lista, la posizione sara' l'ultima posizione della lista (numeri di elementi della lista)
    p = L.n;

  elemento e = L.a[p]; // salvo l'elemento da eliminare

  for (int i = p + 1; i < L.n; i++) { // sposto tutti gli elementi a destra della posizione da eliminare
    L.a[i - 1] = L.a[i];
    L.a[i] = e;
  }

  L = pop(L); // elimino l'elemento da eliminare alla fine della lista

  return L;
}

/**************************************************
****** funzioni ausiliarie per le liste ***********
**************************************************/

lista init() {
  lista lista_vuota = {NULL, 0, 0};
  return lista_vuota;
}

lista append(lista L, elemento e) {
  if (L.n == L.c) {
    L.c = 2 * (L.c + 1);
    L.a = realloc(L.a, L.c * sizeof(elemento));
  }
  L.a[L.n] = e;
  L.n++;
  return L;
}

lista pop(lista L) {
  if (L.n > 0) {
    L.n--;
    if (L.n < L.c / 4) {
      L.c = L.c / 2;
      L.a = realloc(L.a, (L.c) * sizeof(elemento)); // riduco la dimensione della lista 
    }
    if (L.a[L.n].tipo != 's')
      free(L.a[L.n].dato);
  }
  return L;
}

void stampa(lista L){
  for (int i = 0; i < L.n; i++) {
    switch (L.a[i].tipo) {
    case 'i':
      printf("%d: %d\n", i, *((int *)L.a[i].dato));
      break;
    case 'f':
      printf("%d: %f\n", i, *((float *)L.a[i].dato));
      break;
    case 's':
      printf("%d: %s\n", i, (char *)L.a[i].dato);
      break;
    }
  }
}

elemento intero(int d) {
  elemento e = {'i', NULL};

  e.dato = malloc(sizeof(int));
  *(int *)(e.dato) = d;

  return e;
}

elemento fpoint(float d) {
  elemento e = {'f', NULL};

  e.dato = malloc(sizeof(float));
  *(float *)(e.dato) = d;

  return e;
}

elemento stringa(char *c) {
  elemento e = {'s', NULL};

  e.dato = c;

  return e;
}

int main(){
    lista L = init();
    L = append(L, intero(1));
    L = append(L, intero(2));
    L = append(L, intero(3));
    L = append(L, intero(4));
    L = append(L, intero(5));
    L = append(L, intero(6));
    L = append(L, intero(7));
    L = append(L, intero(8));
    L = append(L, intero(9));
    L = append(L, intero(10));
    L = append(L, intero(11));
    L = append(L, intero(12));
    L = append(L, intero(13));

    stampa(L);
    L = delete(L, 5);
    stampa(L);
}
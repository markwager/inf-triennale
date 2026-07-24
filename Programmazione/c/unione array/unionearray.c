#include <stdlib.h>
#include <stdio.h>
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
lista append(lista, elemento);
void stampa(lista);
lista insert(lista, elemento, int);
lista unione(int *, int, int *, int);

elemento intero(int);
elemento fpoint(float);
elemento stringa(char *);

lista append(lista L, elemento e) {
  if (L.n == L.c) {
    L.c = 2 * (L.c + 1);
    L.a = realloc(L.a, L.c * sizeof(elemento));
  }
  L.a[L.n] = e;
  L.n++;
  return L;
}

void stampa(lista L) {
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

lista unione(int *a, int n, int *b, int m) {
  lista L = init();
  int i = 0, j = 0;

  while (i < n && j < m) {
    if (a[i] <= b[j]) {
      if (L.n == 0 || (L.n > 0 && *(int *)L.a[L.n - 1].dato != a[i]))
        L = append(L, intero(a[i]));
      i += 1;
    } else {
      if (L.n == 0 || (L.n > 0 && *(int *)L.a[L.n - 1].dato != b[j]))
        L = append(L, intero(b[j]));
      j += 1;
    }
  }

  while (i < n) {
    if (L.n == 0 || (L.n > 0 && *(int *)L.a[L.n - 1].dato != a[i]))
      L = append(L, intero(a[i]));
    i += 1;
  }

  while (j < m) {
    if (L.n == 0 || (L.n > 0 && *(int *)L.a[L.n - 1].dato != b[j]))
      L = append(L, intero(b[j]));
    j += 1;
  }

  return L;
}

lista init() {
  lista lista_vuota = {NULL, 0, 0};
  return lista_vuota;
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

int main() {
  int a[] = {1, 3, 5, 7, 9};
  int b[] = {2, 4, 6, 8, 10};
  lista L = unione(a, 5, b, 5);
  stampa(L);
  
}
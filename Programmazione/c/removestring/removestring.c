#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int rimuovi_stringa(char *, char *);

int main() {
  char a[] = "azioneprogrammazione dei calcolatoriazione";
  char b[] = "azione";

  printf("%d\n", rimuovi_stringa(a, b));
  printf("%s\n", a);
}

int rimuovi_stringa(char *a, char *b) {
  int n = strlen(a); //prende la lunghezza di a
  int m = strlen(b); //prende la lunghezza di b
  int corr; 
  int i = 0;
  int res = 0;

  while (a[i] != '\0') { //ciclo per tutti gli elementi di a fintanto che non incontra il carattere nullo
    corr = 0;

    if (a[i] == b[0]) { //se il carattere di a è uguale al primo carattere di b, comincio a controllare tutti gli altri caratteri
      corr = 1;
      for (int j = 1; j < m && corr == 1; j++) {
        if (a[i + j] == b[j])
          corr = 1;
        else
          corr = 0;
      } //metti corr a 0 o a 1 in base alla condizione
    }

    if (corr == 1) { //se corr è uguale a 1, res=1 e metti a[k], dove k=i di i salvato precedentemente. Per i successivi, metti a[k]=a[k+m]
      res = 1;
      for (int k = i; k <= (n - m); k++)
        a[k] = a[k + m]; //cancella la stringa b dalla stringa a modificando i caratteri di a
    }
    
    else {
      i++;
    }
  }

  return res;
}
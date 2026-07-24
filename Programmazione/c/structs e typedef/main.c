#include <stdio.h>
#include <stdlib.h>

//si può usare typedef per avere un alias per un tipo di dato esistente: tipo di dato-nuovo nome
typedef int panzone;

//le structs sono un modo per raggruppare diverse varibili in un unico posto. Ogni variabile nella struct si chiama membro
//a differenza dell'array, la struttura può contenere diversi tipi di dati

//creazione di struct
struct struttura{

    int num;
    char lett;
    char stringa[30];
};

int main()
{

//accesso alla struct struttura
struct struttura str1;

//assegna i valori ai membri s1
str1.num=13;
str1.lett='C';

//stampa i valori
printf("Mio numero: %d\n", str1.num);
printf("Mia lettera: %c\n", str1.lett);

//per una stringa come si fa?
strcpy(str1.stringa, "cazzo");
printf("La mia stringa è: %s\n", str1.stringa);

//modifica un membro
str1.num=14;
printf("Mio numero: %d\n", str1.num);
printf("Mia lettera: %c\n", str1.lett);

//si può usare typedef per avere un alias per un tipo di dato esistente: tipo di dato-nuovo nome
panzone ciao=10;

printf("Il numero è: %d\n", ciao);




}

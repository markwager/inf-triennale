/*
La funzione deve aggiornare lo stipendio di un impiegato (employee) aumentandolo della percentuale specificata (positiva o negativa).
*/


#include <stdlib.h> // Necessario per malloc e free
#include <stdio.h> // Necessario per printf

struct employee {
    char name[50];
    int age;
    float salary;
};
typedef struct employee employee;

void update_salary(employee *emp, float percentage);

void update_salary(employee *emp, float percentage){
    emp->salary += percentage;
    printf("Stipendio aggiornato: %.2f\n", emp->salary);
}

int main(){
    employee emp;
    float percentage;

    printf("Inserisci il nome dell'impiegato: ");
    scanf("%s", emp.name);
    printf("Inserisci l'eta' dell'impiegato: ");
    scanf("%d", &emp.age);
    printf("Inserisci lo stipendio dell'impiegato: ");
    scanf("%f", &emp.salary);

    printf("Inserisci la percentuale di aumento: ");
    scanf("%f", &percentage);

    update_salary(&emp, percentage);

}
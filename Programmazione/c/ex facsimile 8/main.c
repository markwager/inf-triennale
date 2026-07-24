/*
La funzione deve creare una nuova scatola (box) con una base di dimensioni width x height e una profondità depth. La funzione deve restituire un puntatore al nuovo oggetto box.
*/


#include <stdlib.h> // Necessario per malloc e free
#include <stdio.h> // Necessario per printf

struct rectangle {
    float width, height;
};
typedef struct rectangle rectangle;

struct box {
    rectangle *base;
    float depth;
};
typedef struct box box;

box *create_box(float, float, float);

box *create_box(float width, float height, float depth){
    box *a=malloc(sizeof(box)); //assegni memoria al box
    a->base=malloc(sizeof(rectangle)); //assegni memoria alla base
    a->base->width=width; //gli assegno  larghezza
    a->base->height=height; //gli assegno altezza
    a->depth=depth; //assegno la profondità a parte
    return a;

}

int main() {
    box *b = create_box(10, 5, 3);
    printf("Larghezza: %f\n", b->base->width);
    printf("Altezza: %f\n", b->base->height);
    printf("Profondità: %f\n", b->depth);
}
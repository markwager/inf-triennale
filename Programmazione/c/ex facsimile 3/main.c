#include <stdlib.h> // Necessario per malloc e free
#include <stdio.h> // Necessario per printf


struct point{
    float x,y;
};
typedef struct point point;

struct segment{
    point *a;
    point *b;
};
typedef struct segment segment;

segment *new_segment(float, float, float, float);
void stampa(segment *);

void stampa (segment *s){
    printf("%f %f %f %f", s->a->x, s->a->y, s->b->x, s->b->y);
}

segment *new_segment(float ax, float ay, float bx, float by){

    segment *s=malloc(sizeof(segment)); //alloca memoria per il puntatore
    s->a=malloc(sizeof(point)); //alloca memoria per il puntatore point a
    s->b=malloc(sizeof(point)); //alloca memoria per il puntatore point b
    //ora abbiamo praticamente due point con due float ciascuno
    s->a->x=ax; //gli assegno valori
    s->a->y=ay; //gli assegno valori
    s->b->x=bx; //gli assegno valori
    s->b->y=by; //gli assegno valori
    return s;
    
}

int main(){
    segment *s=new_segment(1,2,3,4);
    stampa(s);
}

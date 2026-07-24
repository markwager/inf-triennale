
#include <stdlib.h> // Necessario per malloc e free
#include <stdio.h> // Necessario per printf

/*
La funzione deve creare una nuova linea (line) i cui estremi sono due punti 3D con coordinate (x1, y1, z1) e (x2, y2, z2). La funzione deve restituire un puntatore al nuovo oggetto line.
*/


struct point3d {
    float x, y, z;
};
typedef struct point3d point3d;

struct line {
    point3d *start;
    point3d *end;
};
typedef struct line line;

line *create_line(float, float, float, float, float, float);
line *create_line(float x1, float y1, float z1, float x2, float y2, float z2){
    line *a=malloc(sizeof(line));
    a->start=malloc(sizeof(point3d)); //perchè sono dei puntatori start ed end
    a->end=malloc(sizeof(point3d)); //quindi si usa malloc
    a->start->x=x1;
    a->start->y=y1;
    a->start->z=z1;
    a->end->x=x2;
    a->end->y=y2;
    a->end->z=z2;
    return a;
}



int main(){
    line *s=create_line(1.2, 2.3, 3.4, 4.5, 5.6, 6.7);
    printf("%f %f %f %f %f %f", s->start->x, s->start->y, s->start->z, s->end->x, s->end->y, s->end->z);
}
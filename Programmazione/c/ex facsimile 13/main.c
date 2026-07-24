/*
Scrivi una funzione che aggiunge un nuovo elemento in testa a una lista dinamica.
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivi una funzione che controlla se un valore è presente in una lista.
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivi una funzione che rimuove il primo nodo che contiene un valore specificato.
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivi una funzione che aggiunge un nuovo nodo alla fine della lista.
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivi una funzione che dealloca tutta la memoria occupata dalla lista.
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivi una funzione che inverte l'ordine degli elementi in una lista.
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivi una funzione che concatena due liste dinamiche.
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Scrivi una funzione che crea una lista dinamica leggendo un numero specificato di elementi dall'utente.
*/

#include <stdlib.h> // Necessario per malloc e free
#include <stdio.h>  // Necessario per printf

struct Node {
    int data;
    struct Node *next;
};
typedef struct Node Node;

Node* insert_at_head(Node *head, int value);
Node* insert_at_tail(Node *head, int value);
int search_in_list(Node *head, int value);
void stampa(Node *head);
Node* remove_from_list(Node *head, int value);
Node* reverse_list(Node *head);
Node* concatenate_lists(Node *list1, Node *list2);
Node* create_list_from_input(int n);
void free_list(Node *head);

// Funzione per inserire un nodo in testa
Node* insert_at_head(Node *head, int value){
    Node *new_node = malloc(sizeof(Node));
    if (new_node == NULL) {
        return NULL;  // Se l'allocazione fallisce, restituisce NULL
    }
    new_node->data = value;
    new_node->next = head;
    return new_node;
}

// Funzione per inserire un nodo in coda
Node* insert_at_tail(Node *head, int value) {
    Node *new_node = malloc(sizeof(Node));
    if (new_node == NULL) {
        return NULL;  // Se malloc fallisce, restituiamo NULL per segnalare l'errore
    }
    new_node->data = value;
    new_node->next = NULL;
    
    if (head == NULL) {
        return new_node;
    }
    
    Node *temp = head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = new_node;
    
    return head;
}

// Funzione per cercare un valore nella lista
int search_in_list(Node *head, int value) {
    while (head != NULL) {
        if (head->data == value) {
            return 1;
        }
        head = head->next;
    }
    return 0;
}

// Funzione per stampare la lista
void stampa(Node *head) {
    while (head != NULL) {
        printf("%d ", head->data);
        head = head->next;
    }
    printf("\n");
}

// Funzione per rimuovere un nodo dalla lista
Node* remove_from_list(Node *head, int value) {
    if (head == NULL) {
        return NULL;
    }

    // Caso: il valore è nella testa
    if (head->data == value) {
        Node *temp = head;
        head = head->next;
        free(temp);
        return head;
    }

    // Caso generale
    Node *prev = head;
    Node *curr = head->next;

    while (curr != NULL) {
        if (curr->data == value) {
            prev->next = curr->next;
            free(curr);
            return head;
        }
        prev = curr;
        curr = curr->next;
    }

    return head;
}

// Funzione per invertire la lista
Node* reverse_list(Node *head) {
    Node *prev = NULL;
    Node *current = head;
    Node *next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    return prev; // Nuova testa della lista
}

// Funzione per concatenare due liste
Node* concatenate_lists(Node *list1, Node *list2) {
    if (list1 == NULL) return list2;
    if (list2 == NULL) return list1;

    Node *tail = list1;
    while (tail->next != NULL) {
        tail = tail->next;
    }
    tail->next = list2;
    return list1;
}

// Funzione per creare una lista leggendo N valori dall'utente
Node* create_list_from_input(int n) {
    Node *head = NULL;
    for (int i = 0; i < n; i++) {
        printf("Inserisci un valore: ");
        int value;
        scanf("%d", &value);
        head = insert_at_tail(head, value);
    }
    return head;
}

// Funzione per liberare tutta la memoria della lista
void free_list(Node *head) {
    Node *temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}

int main() {
    Node *lista = NULL;
    lista = insert_at_head(lista, 1);
    lista = insert_at_head(lista, 2);
    lista = insert_at_head(lista, 3);
    lista = insert_at_head(lista, 4);
    lista = insert_at_head(lista, 5);
    lista = insert_at_head(lista, 6);
    lista = insert_at_head(lista, 7);
    lista = insert_at_head(lista, 8);
    lista = insert_at_head(lista, 9);
    lista = insert_at_head(lista, 10);

    printf("Lista iniziale:\n");
    stampa(lista);

    int trovato = search_in_list(lista, 5);
    printf("Valore 5 trovato? %s\n", trovato ? "Sì" : "No");

    lista = remove_from_list(lista, 5);
    printf("Lista dopo la rimozione di 5:\n");
    stampa(lista);

    Node *head2 = NULL;
    head2 = insert_at_tail(head2, 1);
    head2 = insert_at_tail(head2, 2);
    head2 = insert_at_tail(head2, 3);
    head2 = insert_at_tail(head2, 4);
    head2 = insert_at_tail(head2, 5);
    head2 = insert_at_tail(head2, 6);
    head2 = insert_at_tail(head2, 7);
    head2 = insert_at_tail(head2, 8);
    head2 = insert_at_tail(head2, 9);
    head2 = insert_at_tail(head2, 10);

    printf("Seconda lista:\n");
    stampa(head2);

    Node *head3 = reverse_list(head2);
    printf("Lista invertita:\n");
    stampa(head3);

    Node *head4 = concatenate_lists(head3, lista);
    printf("Liste concatenate:\n");
    stampa(head4);

    // Liberazione memoria
    free_list(head4);

    return 0;
}


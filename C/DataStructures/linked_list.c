// Author: Shaikh Aquib
// Singly Linked List in C

#include<stdio.h>

typedef struct node
{
    int n;
    struct node *ptr = NULL;
}
node;

int main() 
{
    int size = 0;
    int capacity = 0;

    node *list = NULL;
    
    while (1) {
        int val;
        scanf("%i", &val);

        if (size == capacity) {
            node *list = malloc(sizeof(int));
            capacity++;
        }
        
        list -> n = val;
        list -> ptr = NULL;
        size++;
    }
}



        

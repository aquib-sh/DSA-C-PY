#include<stdio.h>
#include<limits.h>
#include<stdlib.h>

int main() {
    int capacity = 0;
    int size = 0;

    int *arr = NULL;

    while (1) {
        int number;
        printf("Enter number: ");
        scanf("%i", &number);

        if (number == INT_MAX) { break; }

        if (size == capacity) {
            arr = realloc(arr, sizeof(int) * (size + 1));
            capacity++;
        }
        
        arr[size] = number;
        size++;
    }

    for (int i = 0; i < size; i++) {
        printf("You Entered: %i\n", arr[i]);
    }
    free(arr);
}

#include <stdio.h>

int main() {
    int capacity;
    printf("Enter the length: ");
    scanf("%i", &capacity);
    int size = 0;
    int arr [capacity];

    while (size < capacity) {
        scanf("%i", &arr[size]);
        size++;
    }
    
    printf("\n");

    for(int i = 0; i < size; i++) {
        printf("Your entered: %i\n", arr[i]);
    }
}


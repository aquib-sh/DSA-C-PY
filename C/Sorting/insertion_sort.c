#include <stdio.h>

void insertion_sort(int *arr, int len) {
    for(int i = 0; i < len; i++) {
        int pos = i;
        
        while((pos > 0) && (arr[pos] < arr[pos-1])) {
            int temp = arr[pos];
            arr[pos] = arr[pos-1];
            arr[pos-1] = temp;

            pos--;
        }
    }
}


int main() {
    int arr[] = {10,20,3,5,2,-1};
    int len = sizeof(arr)/sizeof(int);
    insertion_sort(arr, len);

    for(int i = 0; i < len; i++) {
        printf("%d\n", arr[i]);
    }
}


                


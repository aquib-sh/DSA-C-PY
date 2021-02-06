#include <stdio.h>

void insertion_sort(int *arr, int len) {
    for(int i=0; i<len; i++) {
        int min = i;
        for(int j=i; j<len; j++) {
            if(arr[j] < arr[i]) {
                min = j;
                
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int main() {
    int arr[] = {155,39,54,45,13,455};
    int len = (sizeof(arr)/sizeof(int));
    insertion_sort(arr, len);

    for(int i = 0; i < len; i++) {
        printf("%d\n",arr[i]);
    }
}


#include <stdio.h>

int get_max(int val, int val2) {
    int max = 0;
    if (val > val2) {
        max = val; 
    }
    else {
        max = val2;
    }
    return max;
}

int* merge(int arr[], int arr2[]) {
    int len_of_int = sizeof(int);
    int len_arr  = sizeof(arr) / len_of_int;
    int len_arr2 = sizeof(arr2) / len_of_int;

    int max = get_max(len_arr, len_arr2); 
    int new_arr[max];
    int i=0, j=0, k=0;

    while ((i+j) < (len_arr + len_arr2)) {
        if (i == len_arr-1) {
            new_arr[k] = arr2[j];
            j++;
        }
        else if (j == len_arr2-1) {
            new_arr[k] = arr[i];
            i++;
        }
        else if (arr[i] < arr2[j]) {
            new_arr[k] = arr[i];
            i++;
        }
        else if (arr2[j] < arr[i]) {
            new_arr[k] = arr2[j];
            j++;
        }
        else {
            new_arr[k] = arr[i];
            i++;
            j++;
        }
        k++;
    }
    return new_arr;
}  

int main() {
    int arr[] = {1,10,20,40};
    int arr2[] = {90,120,140,150,160};

    int merged_array = merge(arr, arr2);
    int merged_len = sizeof(merged_array) / sizeof(int);

    for (int i = 0; i < merged_len; i++) {
        printf("%d", merged_array[i]);
    }
}



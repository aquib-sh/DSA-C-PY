/*** Author: Shaikh Aquib
     Binary Search on a sorted array
     Time Complexity: O(log2n) 
*/

#include <stdio.h>

int search(int *arr, int elem, int start, int stop, int len)
{
        // Eliminate the possiblilty of element being lesser or greater
        // in the first step to avoid unnecessary computations further
        if (start == 0 && stop == (len-1)) {
                if (elem > arr[stop]) {
                       return -1;
                }
                else if(elem < arr[start]) {
                        return -1;
                }
        }

        int mid = (start + stop) / 2;
        
        if (elem == arr[mid]) {
                return mid;
        }
        else {
                if (elem < arr[mid]) {
                        search(arr, elem, start, (mid-1), len);
                }
                else if (elem > arr[mid]) {
                        search(arr, elem, (mid+1), stop, len);
                }
        }
}

int main() {
        int arr[] = {10,20,30,40,50,60,70,80};
        printf("Enter an element to search: ");
        int want;
        scanf("%d", &want);
        int len = sizeof(arr)/sizeof(int);  
        
        int got = search(arr, want, 0, len-1, len);
        
        if (got == -1) {
                printf("Unable to find the element");
        }
        else {
               printf("Found the element at %d", got);
        }
} 

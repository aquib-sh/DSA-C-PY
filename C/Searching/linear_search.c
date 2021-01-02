#include<stdio.h>

int ar_search(int *arr, int val) 
{
	int len = sizeof(arr)/sizeof(arr[0]);
	for(int i = 0; i < len; i++) {
		if(arr[i] == val) {
			return i;
		}
	}
	return -1; 
}

int main()
{
	
	int arr[] = {10, 20, 40, 65, 39, 44};
	printf("enter the value to search: ");
	int e;
	scanf("%d", &e);
	
	int got = ar_search(arr, e);
	if(got == -1) {
		printf("Unable to find the given element\n");
	}
	else {
		printf("Got the element at position %d", got); 
	}
}



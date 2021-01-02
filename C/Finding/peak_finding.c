/*** Author: Shaikh Aquib
	Peak Finding Algorithm using divide and conquer
	On 1D Array
	Time Complexity: O(log2n)
*/

#include<stdio.h>

int find(int *arr, int start, int end, int len)
{
	// Check for the peak at start and end when entered for 1st time
	if(start == 0 && end == (len-1)) {
		int len = sizeof(arr)/sizeof(arr[0]);
		if(arr[0] > arr[1]) {
			return start;
		}
		else if(arr[len-1] < arr[len-2]) {
			return len-1;
		}
	}

	// Get the mid and check whether its peak
	int mid = (start + end)/2;	

	// Enter only if the mid is between array range
	if(mid > 0 && mid < len) {
		if(arr[mid] <= arr[mid-1]) {
			find(arr, start, (mid-1), len);
		}
		else if(arr[mid] <= arr[mid+1]) {
			find(arr, (mid+1), end, len);
		}
		else {
			return mid;
		}
	}
	else {
		return -1;
	}
}

int main()
{
	int arr[] = {40,90,30,70,600,60,47,90,100};
	int len = sizeof(arr)/sizeof(arr[0]);

	int peak = find(arr, 0, (len-1), len);
	if(peak == -1) {
		printf("Unable to find the peak");
	}
	else {
		printf("peak is: %d \nfound at position: %d", 
               		arr[peak], peak);
	}
}	
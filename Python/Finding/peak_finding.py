# Author: Shaikh Aquib
# Peak Finding Algorithm using Recursive Approach
# Time Complexity: O(log2n)

def find(arr, start, end, n):
    if (start == 0 and end == (n-1)):
        if arr[start] > arr[start+1]:
            return start
        elif arr[end] > arr[end-1]:
            return end

    mid = (start + end)/2
    if not(mid > start) and not(mid < n):
        return -1

    if (arr[mid] <= arr[mid-1]):
        find(arr, start, (mid-1), n)
    elif (arr[mid] <= arr[mid+1]):
        find(arr, (mid+1), end, n)
    else:
        return mid

if __name__ == "__main__":
    arr = [40, 90, 30, 70, 600, 60, 47, 90, 100]
    n = len(arr)
    got = find(arr, 0, (n-1), n)
    if (got == -1):
        print("Unable to find peak")
    else:
        print("found peak at {}, \n peak was {}".format(got, arr[got]))

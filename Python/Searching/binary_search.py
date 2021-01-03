# Author: Shaikh Aquib
# Binary Search Algorithm
# Time Complexity: O(log2n)

def search(arr, elem, start, stop, length):
    # Eliminate the possibity of element being lesser or greater 
    # at the first step
    if start > stop:
        return -1
    elif (start == 0 and stop == (length-1)):
        if (elem < arr[start]) or (elem > arr[stop]):
            return -1
   
    mid = (start + stop) // 2
    
    if (elem == arr[mid]): 
        return mid
    else:
        if elem < arr[mid]:
            return search(arr, elem, start, (mid-1), length)
        elif elem > arr[mid]:
            return search(arr, elem, (mid+1), stop, length)

if __name__ == "__main__":
    arr = [10,20,30,40,50,60,70,99,101]
    want = int(input("Enter an element to search: "))
    length = len(arr)

    got = search(arr, want, 0, (length-1), length) 

    if got == -1:
        print("Unable to find the element")
    else:
        print("Found the element at position {}".format(got))

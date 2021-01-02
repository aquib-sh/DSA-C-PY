# Author: Shaikh Aquib
# Simple Linear Search Algorithm
# Time complexity is O(n)

def search(arr, to_search):
    for i in range(0, len(arr)):
        if arr[i] == to_search:
            return i
    return -1

if __name__ == "__main__":
    arr = [10,20,30,44,66,10]    
    to_search = int(input("Enter an element to search: "))
    got = search(arr, to_search)
    if got == -1:
        print("Unable to find the value: ")
    else:
        print("Got the element at position: {}".format(got))




def insertion_sort(arr):
    for i in range(len(arr)):
        pos = i

        while pos > 0 and arr[pos] < arr[pos-1]:
            (arr[pos], arr[pos-1]) = (arr[pos-1], arr[pos])      
            pos -= 1




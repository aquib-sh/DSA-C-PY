def partition(arr, start, end):
    pivot = start

    while end > start:
        while start < len(arr) and arr[start] <= arr[pivot]:
            start += 1
        while arr[end] > arr[pivot]:
            end -= 1

        print(arr)
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
            #start += 1
            #end -= 1

    arr[pivot], arr[end] = arr[end], arr[pivot]
    return end
    

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)

            
if __name__ == '__main__':
    arr = [11,9,29,7,2,15,28]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)




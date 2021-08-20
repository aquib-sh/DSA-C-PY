def merge(a, b):
    a_size = len(a)
    b_size = len(b)
    i = 0
    j = 0

    res = []

    while (i + j) < (a_size + b_size):
        if i >= a_size:
            res.append(b[j])
            j += 1

        elif j >= b_size:
            res.append(a[i])
            i += 1

        else: 
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1

            elif b[j] < a[i]:
                res.append(b[j])
                j += 1
    return res

def merge_sort(arr, left, right):
    if right - left <= 1:
        return arr[left:right]

    mid = (left + right) // 2
    LHS = merge_sort(arr, left, mid)
    RHS = merge_sort(arr, mid, right)

    return merge(LHS, RHS)


    



            
            

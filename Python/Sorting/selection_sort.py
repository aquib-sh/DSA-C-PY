def selection_sort(li):
    for i in range(0, len(li)):
        minpos = i
        for j in range(i, len(li)):
            if li[j] < li[i]:
               minpos = j

               (li[i], li[j]) = (li[j], li[i])





                

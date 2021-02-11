def remdup(li):
    length = len(li) 
    holder = []
    if length <= 1:
        return li
    for i in range(0, length):
        if i == length-1:
            holder.append(li[i])
        else:
            if not li[i] in li[(i+1):]:
                holder.append(li[i])
    return holder

def splitsum(l):
    pos = 0 
    neg = 0
   
    for i in range(0, len(l)):
        if l[i] < 0:
            neg += l[i]**3
        else:
            pos += l[i]**2

    return [pos, neg]

def matrixflip(m, d):
    nm = []
    if d == 'h':
        for elem in m:
            nm.append([elem[i] for i in range(len(elem)-1, -1, -1)])
            
    if d == 'v':
        for i in range(len(m)-1, -1, -1):
            nm.append(m[i]) 
    return nm
            




             
    
        
            

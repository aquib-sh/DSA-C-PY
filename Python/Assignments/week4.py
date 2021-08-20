def rainaverage(arr):
    arr.sort()
    ctys = {}
    ctys_cnt = {}

    prev = None

    for element in arr:
        if element[0] == prev:
            ctys[element[0]] += element[1]
            ctys_cnt[element[0]] += 1
        else:
            count = 1
            prev = element[0]
            ctys[element[0]] = element[1]
            ctys_cnt[element[0]] = 1

    raintup = [] 
    for city in ctys:
        avg = ctys[city] / ctys_cnt[city]
        raintup.append((city, avg))

    return raintup
   
def listtype(l):
    return(type(l) == type([]))

def flatten(elem):
    flat = []
    if listtype(elem):
        for e in elem:
            flat.extend(flatten(e))
        return flat
    else:
        return [elem]

        


    
    

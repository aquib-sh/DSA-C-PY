def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primepartition(n):
    p = 0
    q = n
    for i in range(0, n//2):
        p += 1
        q -= 1
        
        if (isprime(p) and isprime(q)) and (p + q == n):
            return True 
    return False

def matched(s):
    opener = 0
    closer = 0
    opener_appeared = False

    for i in range(0, len(s)):
        if s[i] == "(":
            opener += 1
            opener_appeared = True
        elif (s[i] == ")") and (opener_appeared or opener > 0) and (opener > closer):
            closer += 1
            opener_appeared = False

    if opener == closer:
        return True
    else:
        return False

def rotatelist(l, k):
    rlist = l[:]
    rdone = 0
    while rdone < k:
        first = rlist[0]
        for i in range(1, len(rlist)):
            rlist[i-1] = rlist[i]
        rlist[-1] = first
        rdone += 1
    return rlist
            


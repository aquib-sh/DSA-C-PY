# Author: Shaikh Aquib
# Euclid's Algorithm for GCD
# Complexity:

import sys

def gcd(x, y):
    if x < y:
        (x, y) = (y, x)
    if(x % y) == 0:
        return y
    else:
        diff = x-y
        return (gcd(max(y,diff), min(y, diff)))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please enter both x, y values as arguments")    
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    print(gcd(m, n))

# Author: Shaikh Aquib
# Algorithm for finding Greatest Common Divisor(GCD)
# Complexity: O(n)

import sys

def gcd(x, y):
    for i in range(min(x, y), 0, -1):
        if (x % i == 0) and (y % i == 0):
            return i

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("please x, y valeus as argument")    
    else:
        a = int(sys.argv[1]) 
        b = int(sys.argv[2])
        print(gcd(a, b))


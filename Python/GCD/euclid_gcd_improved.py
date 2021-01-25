# Author: Shaikh Aquib
# Euclid's GCD Algorithm
# Complexity: O(log n)

# if x and y are 2 numbers such that x > y then
# x = quotient * y + remainder


import sys

def gcd(x, y):
    if x < y:
        (x, y) = (y, x)
    
    if x % y == 0:
        return y 
    else:
        return(gcd(y, (x % y)))

if __name__ = "__main__":
    if len(sys.argv) != 3:
        print("please enter the arguments for x and y")
    print(gcd(x, y))


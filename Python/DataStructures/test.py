from math import sqrt

def sum3cubes(n):
    for i in range(1, int(sqrt(n))):
    	
        for j in range(1, int(sqrt(n))):
          
            for k in range(1, int(sqrt(n))):
     			
                if (n == i**3 + j**3 + k**3):
                    return True
                
    return False
           

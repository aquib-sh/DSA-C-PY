# lds() returns the length of the longest 
# dividing subsequence in arr[] of size n
def lds(arr, n):
	
	lds = [0 for i in range(n)]
	
	lds[0] = 1
	
	# Compute optimized lds values 
	# in bottom up manner
	for i in range(n):
		lds[i] = 1
		for j in range(i):
			if (lds[j] != 0 and
				arr[i] % arr[j] == 0):
				lds[i] = max(lds[i], lds[j] + 1)

	return max(lds)

# Driver Code
length = int(input())
inp = []

for i in range(0, length):
    e = int(input())
    inp.append(e)


print("Length of lds is", lds(inp, length))


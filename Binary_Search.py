# Python code to implement iterative Binary 
# Search. 

# It returns location of x in given array arr 
# if present, else returns -1 
def binarySearch(arr, x): 
	i=0
	l=len(arr)-1
	while i <= l: 

		mid = int((i + l)/2); 
		
		# Check if x is present at mid 
		if arr[mid] == x: 
			return mid 

		# If x is greater, ignore left half 
		elif arr[mid] < x: 
			i = mid + 1

		# If x is smaller, ignore right half 
		else: 
			l = mid - 1
	
	# If we reach here, then the element 
	# was not present 
	return -1


# Test array 
arr = [1,2,3,4,6,12,34,56,67,87,91,92,95,97] 
x = 56

# Function call 
result = binarySearch(arr, x) 

if result != -1: 
	print ("Element is present at index % d" % result)
else: 
	print ("Element is not present in array")


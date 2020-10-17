'''
Consider that the element to be searched is x, in the array arr.
The idea is to first find the smallest Fibonacci number that is greater than or equal to the length of given array n. 
Let the found Fibonacci number be k. 
We use (k-2)’th Fibonacci number as the index givn that it is a valid index. 
Let (k-2)’th Fibonacci Number be i, we compare arr[i] with x, if x is same, we return i. 
Else if x is greater, we recur for subarray after i, else we recur for subarray before i.
'''

def fibonaccianSearch(arr, x, n): 
    k2 = 0 
    k1 = 1 
    k = k2 + k1 
  
    while (k < n): 
        k2 = k1 
        k1 = k
        k = k2 + k1 

    offset = -1; 

    while (k > 1): 
        i = min(offset+k2, n-1) 
        if (arr[i] < x): 
            k = k1 
            k1 = k2 
            k2 = k - k1 
            offset = i 
        elif (arr[i] > x): 
            k = k2 
            k1 = k1 - k2 
            k2 = k - k1 
        else : 
            return i 
  
    if(k1 and arr[offset+1] == x): 
        return offset+1; 
   
    return -1
  
arr = [1,2,3,4,6,12,34,56,67,87,91,92,95,97] 
x = 56
n = len(arr)
print("Found at index:", fibonaccianSearch(arr, x, n)) 

#Python 3.x : Linear Search
#Complexity : O(n)

def linearSearch(arr,x):
    n = len(arr)
    for i in range(n):
        #If x in arr
        if arr[i] == x:
            return i
    #if x is not in arr, it returns -1
    return -1

def main():
    arr = [33,24,5,6,17,8,444,32,12,97]
    x = 8

    index = linearSearch(arr,x)
    print("Number {} is at index {}".format(x,index))

if __name__ == "__main__":
    main()
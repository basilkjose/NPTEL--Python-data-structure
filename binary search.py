# BINARY SEARCH USING RECURSIVE AND ITERATIVE METHODS


# 1.RECURSIVE METHOD

def binary_search_recursive(seq, left, right, ele):

    if right >= left:
 
        mid = (right + left) // 2
        if seq[mid] == ele:
            return mid
        elif seq[mid] > ele:
            return binary_search_recursive(seq, left, right - 1, ele)
        else:
            return binary_search_recursive(seq, mid + 1, right, ele)
    else:
         return -1
 
seq = [ 2, 3, 4, 10, 40 ]
ele = 40
 
result = binary_search_recursive(seq, 0, len(seq)-1, ele)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

#________________________________________________________________________________________    

# 2. Iterative Method

def binary_search_iterative(seq, ele):
    left = 0
    right = len(seq) - 1
    mid = 0
 
    while left <= right:
 
        mid = (left + right) // 2

        if seq[mid] < ele:
            left = mid + 1

        elif seq[mid] > ele:
            right = mid - 1

        else:
            return mid
 
    return -1
 

seq = [ 2, 3, 4, 10, 40 ]
ele = 10
result = binary_search_iterative(seq, ele)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")    

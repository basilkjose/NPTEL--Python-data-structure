# SELECTION SORT

def selectionsort(seq):
    for start in range(len(seq)):
        minpos=start
        for i in range(start,len(seq)):
            if seq[i] < seq[minpos]:
                minpos=i
        (seq[start],seq[minpos])=(seq[minpos],seq[start]) 
    
    return seq    
                
result=selectionsort([74,32,89,55,21,64])

print(result)
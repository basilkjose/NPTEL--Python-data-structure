#following are different way(optimized way) to calculate greatest common divisior

def gcd_with_list(m,n):
    
    """Function to calculate gcd using list"""
    cf=[] #common factor    
    for i in range(1,min(m,n)+1):
        if(m%i)==0 and(n%i)==0:
            cf.append(i)
    return(cf[-1]) 

    

def gcd_without_list(m,n):
    
    """Function to calculate gcd without using list"""  
    for i in range(1,min(m,n)+1):
        if(m%i)==0 and(n%i)==0:
            mrcf=i #most recent common factor
    return(mrcf)    

def gcd_without_list_and_for_loop(m,n):
    
    """Function to calculate gcd without using list and for loop"""  
    i=min(m,n)
    while i>0:
        if(m%i)==0 and(n%i)==0:
            mrcf=i #most recent common factor
            return(mrcf)  
        else:  
             i=i-1


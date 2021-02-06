# -*- coding: utf-8 -*-
"""
Write a function expanding(l) that takes as input a list of integer l and returns True 
if the absolute difference between each adjacent pair of elements strictly increase
"""
def expanding(l):
    c1=abs(l[1]-l[0]) # Difference of 1st 2 integers.
    for j in range(2,len(l)): 
        c2=abs(l[j]-l[j-1]) # Next difference = l[2]-l[1] 
        if c2 <= c1: # if next diff smaller/equal to prev diff 
            return(False) #return false
        else: # if next diff > prev diff
              c1=c2 # next diff be prev diff for next iteration.
    return(True)
# -*- coding: utf-8 -*-
"""
Write a function accordian(l) that takes as input a list of integer l and returns True 
if the absolute difference between each adjacent pair of elements alternates between
 increasing strictly and decreasing strictly.
"""
def accordian(l):
    list=[]
    c1=abs(l[1]-l[0]) # Difference of 1st 2 integers.
    for j in range(2,len(l)): 
        c2=abs(l[j]-l[j-1]) # Next difference = l[2]-l[1] 
        if c2>=c1:
            c1=c2
            list.append(1)
        else:
            c1=c2
            list.append(0)
    for i  in range(1,len(list)):
        if (((list[i]>list[i+1]) and (list[i]>list[i-1])) or ((list[i]  <list[i+1]) and (list[i]<list[i-1]))) :
            return True
        else:
            return False   
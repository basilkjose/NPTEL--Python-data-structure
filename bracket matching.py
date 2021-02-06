# -*- coding: utf-8 -*-
"""
Write a function matched(s) that takes as input a string s and checks 
if the brackets "(" and ")" in s are matched: that is, every "(" has a matching ")" after 
it and every ")" has a matching "(" before it. Your function should ignore all other 
symbols that appear in s. Your function should return True if s has matched
brackets and False if it does not.

"""

def matched(s):
  nested = 0
  for i in range(0,len(s)):
    if s[i] == "(":
       nested = nested+1
    elif s[i] == ")":
       nested = nested-1
       if nested < 0:
          return(False)    
  return(nested == 0)
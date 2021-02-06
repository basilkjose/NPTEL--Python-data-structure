"""Write a function intreverse(n) that takes as input a positive 
integer n and returns the integer obtained by reversing the digits in n."""

def intreverse(n):
  ans = 0
  while n > 0:
    (d,n) = (n%10,n//10)
    ans = 10*ans + d
  return(ans)
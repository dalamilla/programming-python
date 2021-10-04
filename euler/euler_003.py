"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def Euler003(n):
  """ Solution of third Euler problem. """
  pm = 2
  
  while n != 1:
    if  n % pm == 0:
      n = n / pm
    else:
      pm += 1
  
  return pm

# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(13))


#IMPORTS
import math
from math import sin, pi

syn_pi = math.sin(math.pi)
syn_pi1 = sin(pi)

print(syn_pi)
print(syn_pi1)

def factorial(n):
    if n<= 1:
        return 1
    else:
        return n * factorial(n-1)
        

def number_of_groups(n, k):
   a= factorial(n) / (factorial(n - k) * factorial(k))
   return int(factorial(n) / (factorial(n - k) * factorial(k)))
print(number_of_groups(50,7))
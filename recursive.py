def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(13))


#IMPORTS
import math
from math import sin, pi

syn_pi = math.sin(math.pi)
syn_pi1 = sin(pi)

print(syn_pi)
print(syn_pi1)
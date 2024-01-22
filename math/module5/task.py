from sympy import *
import numpy as np
import matplotlib.pyplot as plt


x = symbols('x')
x0=oo
x_n = np.arange(50,500,0.01)

func = ((4*(x_n**3)-2*(x_n**2) + x_n - 2) / (2 * (x_n**3) + 6 * (x_n**2) - 3*x_n))
l =limit(func, x_n, x0)
print (l)

fig, ax = plt.subplots()

ax.plot(x_n, func)
# ax.plot(x, y2)

ax.set(xlabel='x', ylabel= 'y', title='xy graph')
ax.grid()


plt.show()
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
x = symbols('x')
x0=-oo
func = (7*(x**2)+7*x-2)/(x**2-2*x+3)
l =limit(func, x, x0)
print (type(oo))

if(l==x0):
    print('limit is infinite')
elif(l==-oo):
    print('limit is minus infinite')
else:
    print('limit is limited')



x_n = np.arange(50,500,0.01)
y = (7*(x_n**2)+7*x_n-2)/(x_n**2-2*x_n+3)
y2 = 7 + x_n * 0

# fig, ax = plt.subplots()

# ax.plot(x_n, y)
# ax.plot(x_n, y2)

# ax.set(xlabel='x', ylabel= 'y', title='xy graph')
# ax.grid()

# fig.savefig('test.png')

# plt.show()
x_values = np.linspace(-10, 10, 400)
y_values1 = [func.subs(x, val) for val in x_values]

# Побудова графіку для першої особливої границі
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values1, label='(7*(x**2) + 7*x - 2) / (x**2 - 2*x + 3)')
plt.axvline(x=oo, color='r', linestyle='--', label='x = oo')
plt.title('Графік першої особливої границі')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
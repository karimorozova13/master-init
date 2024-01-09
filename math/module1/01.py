import numpy as np

a= np.array([1,2,3,4], dtype=float)
print(a)
print(np.shape(a))
print(a[0])
print(a[1:])
print(a[:2])

b= np.array([[1,2,3], [4,5,6]], dtype=int)
print(b)

i = np.identity(4, dtype=int)
print(i)

r = np.arange(5)
print(r)

r1 = np.arange(1,3,0.5)
print(r1)

l= np.linspace(1,5,num=5)
print(l)

l1 = np.linspace(1,3,num=3)
print(l1)

ran = np.random.random(3,)
print(ran)

ran1 = np.random.random((3,3))
print(ran1)

# index

c= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(c[1,1])
print(c[1:,1])
print(c[0,:2])

d= np.zeros((3,3), dtype='u4')
print(d)

e = np.array([u"\u2211", u"\u220F"], dtype="U")
print(e)

e = np.array([1, 2, 3])
f= np.array([4, 5, 6])
print(e + f)
print(e - f)
print(e * f)
print(e / f)

g = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
h = np.array([[2, 2, 2], [3, 3, 3], [4, 4, 4]])
print(g + h)
print(g - h)
print(g * h)
print(g / h)

# adregation
z = np.array([1, 2, 3, 4, 5])

print(z.min())

print(z.max())

print(z.sum())

print(z.mean()) #average

print(z.prod()) #mul all

matr =np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print(matr)

diag = np.diag(matr)
print(diag)

k=np.diag(diag)
print(k)

# identity

l =np.eye(4,k=-1,dtype=float)
print(l)
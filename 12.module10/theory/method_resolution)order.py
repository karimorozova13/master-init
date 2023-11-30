# MRO

class A:
    x = "I'm A class"
class B:
    x = x = "I'm B class"
    y = 'Just in B'
class C(A,B):
    z=   "Just in C"
    
c_class = C()
print(c_class.x)
print(c_class.y)
print(c_class.z)

import math

# ctrl + O - open file
a = 5
type(a)
b = 3
c = a / 3
type(c) # float

round(c,3)
help(round) # docs about the built-in functions

# 1 byte = 8 bit
bool(-3) # True
d = False
k = int(d) # 0

print('Hi')

# doc str => multiple lines
name = """    
fdghfh
hgghgg
hgfhgf
"""
print(id(name))# different place in memory

name = 'kari' # different place in memory
print(id(name))


# str => immutable
# garbage collector

# multiline comment
"""
fdsdddddddddddddddddddddddddg
gfdgfdg
gdsgfd
"""

# is None, is not None, for int better ==


# triangle square
# math.sqrt()  korin kvadratnij √
s1 = int(input('Enter: >>>>>'))
s2 = int(input('Enter: >>>>>'))
s3 = int(input('Enter: >>>>>'))
P = s1+s2+s3
p = P /2
S = math.sqrt(p * (p-s1) * (p-s2) * (p-s3))

print('Square is: ', S)
print('Square is: {}'.format(S))
print(f'Square is: {S}')


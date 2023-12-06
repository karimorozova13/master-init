def add(a,b):
    return a +b
def mul(a,b):
    return a * b
def ops(a,b,fn):
    return fn(a,b)

res = ops(2,3,add)
print(res)

res = ops(2,3,mul)
print(res)
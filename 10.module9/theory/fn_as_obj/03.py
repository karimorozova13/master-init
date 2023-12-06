def add(a,b):
    return a +b
def mul(a,b):
    return a * b
def ops(operator):
    if operator == '*':
        return mul
    elif operator == '+':
        return add
    else:
        raise ValueError('the oparator does not exist')
    
# functor
res = ops('+')
print(res(2,3))
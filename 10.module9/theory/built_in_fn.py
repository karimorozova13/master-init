from functools import reduce


names = ['fds', 'fret', 'wqerw']

# return generator
res = list(map(lambda x: x.title(), names))
print(res)

# your fn
def fn_title(x):
    return x.title()
res2 = list(map(fn_title, names))
print(res2)


# comprehension
res3 = [fn_title(x) for x in names]
print(res3)

# FILTER
payments = [100, -3,5,-8,9, 4]

res4 = filter(lambda x: x> 0, payments)
print(list(res4))


# REDUCE
numbers = [3,8,5]
chars = ['g', 'k', 'm']
res5 = reduce(lambda x, y : x +y, numbers, 200)
res6 = reduce(lambda x, y : x +y, chars, "Kari ")

print(res5)
print(res6)



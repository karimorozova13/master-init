def flatten(data):
    l=[]
    if len(data)==0:
        return []
    for el in data:
        if type(el) == list:
            l +=flatten(el)
        else:
            l.append(el)
    return l
print(flatten([1, 2, [3, 4, [5, 6]], 7]))

def make_request(keys, values):
    a ={}
    if not len(keys)==len(values):
        return {}
    for i in range(len(keys)):
        a.update({keys[i]:values[i]})
    return a
print(make_request(['name', 'age', 'lastname'], ['Kari', '18', "Mo"]))
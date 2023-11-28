def normal_name(list_name):
    new_l = []
    for el in map(lambda el: el.title(), list_name):
        new_l.append(el)
    return new_l

name = ["dan", "jane", "steve", "mike"]
print(normal_name(name))
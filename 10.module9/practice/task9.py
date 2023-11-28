def positive_values(list_payment):
    l=[]
    for el in filter(lambda el: el >=0, list_payment):
        l.append(el)

    return l
payment = [100, -3, 400, 35, -100]
print(positive_values(payment))
from functools import reduce


def amount_payment(payment):
    res =[]
    for el in filter(lambda el:el>0,payment):
        res.append(el)
    return reduce(lambda x,y: x+y,res)

print(amount_payment([1, -3, 4]))
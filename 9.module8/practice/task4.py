from random import randrange


def get_numbers_ticket(min, max, quantity):
    s =set()
    if min< 1:
        return []
    elif max > 1000:
        return []
    elif quantity < min or quantity > max:
        return []
    else:
        while len(s) < quantity:
            s.add(randrange(min,max))
        l = list(s)
        l.sort()
        return l
print(get_numbers_ticket(5, 99,13))
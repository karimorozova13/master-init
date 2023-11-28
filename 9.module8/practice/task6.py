from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    total = Decimal(0)
    for el in number_list:
        total += Decimal(el)
        
    return total / Decimal(len(number_list))
print(decimal_average([3, 5, 77, 23, 0.57], 6))
print(decimal_average([31, 55, 177, 2300, 1.57], 9))
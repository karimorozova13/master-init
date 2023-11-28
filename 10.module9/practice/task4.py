def discount_15(price):
    return price * (1 - 0.15)
def discount_25(price):
    return price * (1 - 0.25)
def discount_10(price):
    return price * (1 - 0.1)
def discount_5(price):
    return price * (1 - 0.05)
def discount_0(price):
    return price
DISCOUNTS ={
    15: discount_15,
    25: discount_25,
    10: discount_10,
    5: discount_5,
    0: discount_0
}

def discount_price(discount):
    return DISCOUNTS[discount*100]



DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    discount = customer.get('discount', None)
    return price * (1 - discount) if discount !=None else price * (1 - DEFAULT_DISCOUNT)
print(get_discount_price_customer(5,{"name": "Dima"}))
print(get_discount_price_customer(13,{"name": "Dima","discount": 0.15}))
print(get_discount_price_customer(10, {'name': 'Olga', 'discount': 0}))

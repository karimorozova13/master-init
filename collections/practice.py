from random import randint
import re

def amount_payment(payment):
    total =0
    for el in payment:
        if el >=0:
            total+=el
    return total
print(amount_payment([1,-3,4]))

def format_ingredients(items):
    print(items == [])
    if len(items) > 1:
        new_list = items[:len(items)-2]
        new_list.extend([f'{items[-2]} and {items[-1]}'])
        new_str = ', '.join(new_list)
        return new_str
    elif items == []:
        return ''
    else:
        return items[0]
print(format_ingredients([]))

def get_grade(key=''):
    grades = {"F":1, "FX":2, "E": 3, "D":3, "C": 4, "B":5, "A": 5}
    if key:
        return grades[key]
    else:
        return
print(get_grade("FX"))

def lookup_key(data, value):
    new_dict= []
    for key,val in data.items():
        if val == value:
            new_dict.insert(1,key)
    return new_dict
print(lookup_key({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}, 2))

def split_list(grade):
    if len(grade)==0:
        return([],[])
    average = 0
    for num in grade:
        average+=num
    average = int(average / len(grade))
    min = []
    max = []
    for num in grade:
        if num <= average:
            min.insert(1,num)
        else:
            max.insert(1,num)
    min.sort()
    max.sort()
    return (min,max)
print(split_list([1, 12, 3, 24, 5]))

points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}

def calculate_distance(coordinates):
    
    if len(coordinates) <= 1:
        return 0
    else:
        distance = 0
        first_coordinate = coordinates[0]
        coordinates.pop(0)
        for el in coordinates:
            if first_coordinate > el:
                distance+= points[(el,first_coordinate)]
            else:
                distance+= points[(first_coordinate,el)]
            first_coordinate=el


        return distance
print(calculate_distance([0, 1,3, 2, 0]))

def game(terra, power):
    new_power = power
    for items in terra:
        for item in items:
            if item <= new_power:
                new_power += item
            else:
                break
    return new_power
print(game([[1, 1, 5, 10], [10, 2], [1, 1, 1]],1))

def is_valid_pin_codes(pin_codes):
    if len(pin_codes) == 0:
        return False
    else:
        count_of_codes = 1
        for pin in pin_codes:
            count_of_codes = pin_codes.count(pin)
            if count_of_codes> 1 or type(pin) is not str or len(pin) != 4 or not pin.isdigit() :
                return False
            
    return True
print(is_valid_pin_codes(['1101', '9034', '0011','110a',]))

def get_random_password(password = ''):
    
    def get_random_digit():
        digit = randint(40,126)
        return chr(digit)
    if len(password) == 8:
        return password
    else:
        password += get_random_digit()
        return get_random_password(password)

    
print(get_random_password())

def is_valid_password(password):
    regex = ("^(?=.*[a-z])(?=." +
             "*[A-Z])(?=.*\\d)" )
     
    p = re.compile(regex)
    if len(password) <8 or not re.search(p, password):
        return False
    
    return True

    # BETTER SOLUTION
    # if len(password) != 8:
    #     return False

    # has_upper = False
    # has_lower = False
    # has_num = False

    # for ch in password:
    #     if ch.isupper():
    #         has_upper = True
    #     elif ch.islower():
    #         has_lower = True
    #     elif ch.isdigit():
    #         has_num = True

    # return has_upper and has_lower and has_num

print(is_valid_password('b8g^ro4^'))




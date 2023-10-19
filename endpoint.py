from helo import say_hello

say_hello("Kari")

def get_fullname(first_name,last_name, middle_name=None):
    if middle_name == None:
        return f'{first_name} {last_name}'
    return f'{first_name} {middle_name} {last_name}'

print(get_fullname('Kari', "mo", "Va"))
print(get_fullname('Kari', 'Mo'))

def format_string(string, length):
    if len(string) >= length:
        return string
 

    return " "*int((length - len(string))/2)+ string

print(format_string(length=15, string='abaa'))

def first(size, *numbers ):
    return size + len(numbers)
    
def second(size,**names ):
    return size + len(names)

first(5, "first", "second", "third")
first(1, "Alex", "Boris")
second(3, comment_one="first", comment_two="second", comment_third="third")
second(10, comment_one="Alex", comment_two="Boris")

def cost_delivery(quantity, discount=0):
    if discount == 0:
        if quantity ==1:
            return 5
        else:
            return 5 + ((quantity - 1)*2)
    else:
        if quantity ==1:
            return 5 - 5*discount
        else:
            return (5 + ((quantity - 1)*2)) - (5 + ((quantity - 1)*2))*discount





cost_delivery(2, 1, 2, 3) # 7
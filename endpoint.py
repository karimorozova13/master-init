from helo import say_hello

say_hello("Kari")

def get_fullname(first_name,last_name, middle_name=None):
    if middle_name == None:
        return f'{first_name} {last_name}'
    return f'{first_name} {middle_name} {last_name}'

print(get_fullname('Kari', "mo", "Va"))
print(get_fullname('Kari', 'Mo'))

def format_string(string, length):
    print(length -len(string), 'diference')
    if len(string) >= length:
        return string
    
    print(len(string+" "*(length - len(string))), 'newwwwwww')
    return " "*(length - len(string))+ string
print(format_string(length=15, string='abaa'))

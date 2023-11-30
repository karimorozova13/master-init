import string

def input_num():
    while True:
        try:
            num = input('Enter the number >>>>')
            return int(num)
        except:
            print("i need number")
            
print(input_num())

class NameTooShortError(Exception):
    pass
class FirstLetterIsNotUpperError(Exception):
    pass


def enter_name():
    name = input('Enter your name>>>>')
    if len(name) < 3:
        raise NameTooShortError
    if name[0] not in string.ascii_uppercase:
        raise FirstLetterIsNotUpperError
    
while True:
    try:
        name = enter_name()
        break
    except NameTooShortError:
        print('at least 3 symbols')
    except FirstLetterIsNotUpperError:
        print('first letter should be big')
value = 'b'

try:
    print(int(value))
except ValueError:
    print(f"value is {value}")
except NameError:
    print(f'is not defined')
else:
    print(value > 0)
finally:
    print("You'll see it for sure")

age = input('How old are you?')

try:
    age = int(age)
    if age >= 18:
        print('You are adult')
    else:
        print('You are too small')
except ValueError:
    print(f'{age} is not a number')

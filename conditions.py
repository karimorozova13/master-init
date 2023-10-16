age = input("Your age: ")
if int(age) >= 30:
    print("Adult")
elif int(age) == 20:
    print("good")
else:
    print("Too small")

# falsy values: None, empty container, empty string, 0(int, float, complex)

# several conditions

name = "kari"
experience = 3
has_license = True
if name and experience > 2 and has_license:
    print('Allow')

# compare operators and, or, not

if int(age) < 30 and int(age) > 20:
        print("and")
        
if name or has_license:
        print("or")

if not False:
        print("not")

# ternary operator if...else, short version - or
is_nice = True
msg = "nice" if is_nice else "not nice"

nth = None
result =  nth or 'not found' 

# quarter of square

x =int(input("X:"))
y =int(input("y:"))

if x >=0:
      if y>= 0:                    # x > 0, y > 0
            print('first')
      else:                         # x > 0, y < 0
            print('forth')  
else:
      if y >= 0:                    # x < 0, y > 0
            print('second')
      else:                         # x < 0, y < 0
            print('third')

def print_max(a,b):
    if a > b:
        print(a,'a')
    elif b> a:
        print(b,'b')
    else:
        print('equal')

x = 5
y = 7

print_max(x,y)
print_max(1,3)

def add(a,b):
    return a+b

print(add(3,7))

z = 5
print(z) 

# nonlocal, global
def change_global():
    global z
    z = 50
change_global()
print(z)

#KEY PARAMETERS
def func(a,b=5,c=7):
    print(f'a-{a}, b- {b}, c- {c}')
func(c=100,a=30)

def print_msg(msg, times=1):
    print(msg*times)

print_msg("Hi")
print_msg('Kari', 7)
print_msg(times=5,msg='Kari')




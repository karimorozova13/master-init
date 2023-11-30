class User:
    name= 'Kari'
    age= 13
    
    def say_hello(self):
        print(f'Hi! my name is {self.name}. I am {self.age} years old')
    def set_age(self, age):
        self.age = age
    
    
kari_user =User()
print(kari_user.name)
kari_user.set_age(17)
kari_user.say_hello()

platon_user = User()
platon_user.name = "Platon"
platon_user.age = 9
platon_user.set_age(3)
platon_user.say_hello()
print(platon_user.name)

class UserNew:
    name= ''
    age= 0
    
    def __init__(self, name, age): # constructor
        self.name = name
        self.age = age
    def say_hello(self):
        print(f'Hi! my name is {self.name}. I am {self.age} years old')
            

lewa = UserNew('Lewa', 40)
lewa.say_hello()


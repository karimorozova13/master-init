class Human:
    name=''
    def voice(self):
        print(f'Hi! My name is {self.name}')
        
class Developer(Human):
    des = 'My programming language'
    language=''
    def make_some_code(self):
        print(f'{self.des}: {self.val}')
        
class PythonDev(Developer):
    val ='Python'
    
class JSDev(Developer):
    val= 'JavaScript'
    
kari_dev = PythonDev()
kari_dev.name = 'Kari'
kari_dev.make_some_code()

new_dev = JSDev()
new_dev.name = 'Karine'
new_dev.make_some_code()
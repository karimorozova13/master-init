class Secret:
    public_key = "I'm public"
    _private_key="Avoid to use me"
    __secret_key="I'm hidden"
    
new = Secret()

print(new.public_key)
print(new._private_key)
print(new._Secret__secret_key)


class PositiveNumbers:
    def __init__(self):
        self.__value= None
        
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_val):
        if new_val > 0:
            self.__value = new_val
        else:
            'Val shoueld be > 0'
            
num = PositiveNumbers()
num.value = 13
print(num.value)
num.value = -3  # 'Val shoueld be > 0'

num._PositiveNumbers__value = -13
print(num.value)
# print(type(3))
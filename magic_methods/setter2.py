class Age:
    def __init__(self) -> None:
        self.__age = 0
        
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
    def del_age(self):
        del self.__age
    age = property(get_age,set_age,del_age)
    
a = Age()
a.set_age(13)
print(a.get_age())
# a.del_age()
print(a.get_age())


class AgePub:
    def __init__(self, age) -> None:
        self.age = age
        
age = AgePub(15)
print(age.age)
print(getattr(age, 'name', None))
print(hasattr(age, 'name'))
print(hasattr(age, 'age'))


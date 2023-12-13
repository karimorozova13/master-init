class Car:
    def __init__(self, year, car, model, color, age) -> None:
        self.__age = None
       
        self.year = year
        self.car = car
        self.model = model
        self.color = color
        self.oldness = age
        
    def set_price(self, val):
        self.__price = val
    def get_price(self):
        return self.__price
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age
    

    
mery = Car(2006, 'Mercedes', 'A150', 'light blue', 17)
poly = Car(2004, 'Wolskswagen', 'Polo', 'light blue', 19)

mery.set_price(3600)
print(mery.get_price())

# mery.age(33)
print(mery.oldness)



        
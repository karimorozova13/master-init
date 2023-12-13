class Car:
    def __init__(self, year, car, model, color, price) -> None:
        self.year = year
        self.car = car
        self.model = model
        self.color = color
        self.price = price
        
        # to show what you want when print or use just class object, for print, for users
    def __str__(self) -> str:
        return f'{self.car} {self.model} is {self.color} color and {self.year} year.'
    
    # to work from console or for internal documentation
    def __repr__(self) -> str:
        return f'{self.car} {self.model} is {self.color} color costs {self.price} euro.'
    
    def __eq__(self, __value: object) -> bool:
        return self.price == __value.price
    def __ne__(self, __value: object) -> bool:
        return self.price != __value.price
    def __lt__(self, __value: object) -> bool:
        return self.price < __value.price
    def __gt__(self, __value: object) -> bool:
        return self.price > __value.price
    def __le__(self, __value: object) -> bool:
        return self.price <= __value.price
    def __ge__(self, __value: object) -> bool:
        return self.price != __value.price
    
mery = Car(2006, 'Mercedes', 'A150', 'light blue', 3600)
poly = Car(2004, 'Wolskswagen', 'Polo', 'light blue', 1500)

print(mery == poly)
print(mery != poly)
print(mery < poly)
print(mery > poly)
print(mery <= poly)
print(mery >= poly)


        
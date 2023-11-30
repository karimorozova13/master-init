# duck typing
class Mammal:
    phrase =''
    def voice(self):
        return self.phrase
class Dog(Mammal):
    phrase= 'Bark'
class Cat(Mammal):
    phrase='Meow'
class Chupakabra:
    def voice(self):
        return 'Whoooo'
class Recoder:
    def record_phrase(self,animal):
        voice = animal.voice()
        print(f'Recorded {voice}')
        
r = Recoder()
c = Cat()
d = Dog()
chu = Chupakabra()
r.record_phrase(c)
r.record_phrase(d)
r.record_phrase(chu)
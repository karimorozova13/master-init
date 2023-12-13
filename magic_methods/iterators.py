from random import randint

class RandomIterator:
    def __init__(self,start, end, quantity) -> None:
        self.start = start
        self.end = end
        self.quantity = quantity
        self.count=0
        
    def __iter__(self):
        return self
    def __next__(self):
        self.count+=1
        if self.count > self.quantity:
            raise StopIteration
        else:
            return randint(self.start, self.end)

it = RandomIterator(13,44,5)
for i in it:
    print(i)



a = [1,5,3]
t = iter(a)
print(next(t))
print(next(t))
print(next(t))

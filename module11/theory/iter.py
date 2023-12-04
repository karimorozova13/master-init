class Iterable:
    MAX_VAl= 10
    def __init__(self):
        self.val= 0
    def __next__(self):
        if self.val < self.MAX_VAl:
            self.val +=1
            return self.val
        raise StopIteration
class CustomIterator:
    def __iter__(self):
        return Iterable()
c = CustomIterator()
for i in c:
    print(i)
# generator function

def simple_gen():
    print(1)
    yield 'First'
    print(2)
    yield 'Second'
    
for i in simple_gen():
    print(i)
    
ex= simple_gen()
print(next(ex))
print(next(ex))


import pickle

some_data = {
    (1,2,3): "tuple",
    2: [1,2,3],
    "a": {'key': 'val'}
}

bite_str = pickle.dumps(some_data)
print(bite_str)

unpacked = pickle.loads(bite_str)
print(unpacked)
print(unpacked == some_data)
print(unpacked is some_data)

path = 'pickle.bin'

with open(path, 'wb') as fh:
    pickle.dump(some_data, fh)
    
with open(path, 'rb') as fh:
    unpacked = pickle.load(fh)
    print(unpacked)
    print(unpacked == some_data)
    print(unpacked is some_data)
    
    
# dumps, loads - for byte-string;  dump, load - for files

class Human:
    def __init__(self,name) -> None:
        self.name = name
        
bob = Human('Kari')
bob_byte_str = pickle.dumps(bob)

unpacked_bob= pickle.loads(bob_byte_str)


# it works just if you have class Human here
print(unpacked_bob.name == bob.name)
import json

some_data = {
    'key': 'value',
    2: [1, 2, 3],
    'tuple': (5, 6), 
    'a': {'key': 'value'}
}

byte_str = json.dumps(some_data)

unpacked = json.loads(byte_str)
print(unpacked)
print(unpacked is some_data)
print(unpacked == some_data)

path = 'data.json'

with open(path, 'w') as fh:
    json.dump(some_data, fh)
    
with open(path, 'r') as fh:
    unpacked = json.load(fh)
    print(unpacked)
    print(unpacked is some_data)
    print(unpacked == some_data)
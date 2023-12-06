expenses = {
    "rent": 1600,
    "restaurants": 300,
    "toys":200
}

file_name ='expenses.txt'

# this is serialization
with open(file_name, 'w') as fh:
    for key, val in expenses.items():
        fh.write(f"{key} | {val}\n")
        
# deserialization
expenses2 ={}
with open(file_name, 'r') as fh:
    l = fh.readlines()
    for el in l:
        key, val = el.split('|')
        expenses2.update({key: int(val)})
        
print(expenses2)
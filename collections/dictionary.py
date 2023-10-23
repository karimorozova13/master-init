# return value of key and remove from dict
dict = {'a':1, 'b':2}
b_num = dict.pop('b')
print(dict)
print(b_num)

# concat 2 dictionaries
dict2 = {'c':3}
dict.update(dict2)
print(dict)

# clear all dict
# dict.clear()
print(dict)

# make a copy or dict
copy_dict = dict.copy()
print(copy_dict)
print(copy_dict == dict) #True

# return value of key, don't change the dict, if the key doesn't exist return None or default value
c_el = dict.get('z', 5)
print(c_el)
print(dict)

# iteration
numbers = {
    1: "one",
    2: "two",
    3: "three"
}
for key in numbers.keys(): #return keys, possible write without method
    print(key)
for value in numbers.values(): #return values, 
    print(value)
for key, value in numbers.items(): #return entries, key-value pair 
    print(value)
    print(key)






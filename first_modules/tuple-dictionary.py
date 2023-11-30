# tuples - kortej *numbers
#dictionary -  key-value pairs **phone_book

def total(a, *numbers, **phone_book):
    print(a, 'a')
    for item in numbers:
        print(item, 'item')
    for first, second in phone_book.items():
        print(first, second)
total(5, 6,7,8,9, 13,Kari=13, John=10,Doe=15)

#TUPLES

# empty tuples
new_tuple = tuple()
one_tuple =()

#not empty

not_empty = (1,2,3)
print(not_empty[2]) #print by index

#DICTIONARY

#empty dictionary
first_dict= {}
second_dict = dict()

#not empty
some_dict= {
    'key': 'value',
    1:'one'
}

new_dict = {'key':'value'}
new_dict['Kari'] = "Mo"
print(new_dict)

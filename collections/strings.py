# take =value by idx
string = 'Hello!'
last_char = string[-1]
first_char = string[0]
print(last_char)

# can't change
# str[0] = 'K' TypeError

# convert to upper case
string.upper()
print(string.upper())

# convert to lower case
string.lower()
print(string.lower())

# check if starts with substr
print(string.startswith('He'))

# check if ends with substr
print(string.endswith('!'))

# make first letter of word upper
name = "avril lavigne"
print(name.title())  

# remove spaces on the left
name1 = '               Kari'
print(name1.lstrip())

# remove space from both sides
name2 = '         kari       '
print(name2.strip())


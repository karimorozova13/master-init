# find char in str. if nth return -1, return idx, default - start, end find()
s = 'Hi there'
print(s.find('th',1,6))
print(s.find('q'))

# find from right side rfind()
print(s.rfind('h'))

# find the index. if not exist return ValueError
# print(s.index('q'))
print(s.index('Hi'))

# find from right side rindex()
print(s.rindex('h'))

# split str by sign
s1 = "I am learning strings in Python. Some new methods got now."
sentences = s1.split('. ')
print(sentences)

# join str by sign
s2 = '. '.join(sentences)
print(s2)

# delete spaces from both sides
s3 = s2.strip()
print(s3)

# delete spaces from left side
s4 = '       dfds  '.lstrip()
print(s4)

# delete spaces from right sides
s5 = '   fdggdf      '.rstrip()
print(s5)

# change substr inside the str
dogs = "All dogs bark like dogs."
cats = dogs.replace('dogs', 'cats')
print(cats)

# remove fixed substr from the start
s6 = "TestHook"
print(s6.removeprefix('Test'))
print(s6.removeprefix('Hook'))

# remove fixed substr from the end
print(s6.removesuffix('Test'))
print(s6.removesuffix('Hook'))

# collection of unick and immutable  data types
new_set = set()
print(new_set)

# filled set
not_empty = set('Karri')
print(not_empty)
not_empty2 = {1,2,3,1}
print(not_empty2)

# add el to the end
not_empty2.add(5)
print(not_empty2)

# remove el, call Exception if the el doesn't exist
not_empty2.remove(2)
print(not_empty2)

# remove el, don't call Exception if the el doesn't exist
not_empty2.discard(7)
print(not_empty2)

# math operations between 2 sets
a = set('hello')
b = set('hi there!')
print(a)
print(b)

common_els =a & b  #return common elements for both sets AND
print(common_els)

all_without_common =a ^ b  #return common elements for both sets OR
print(all_without_common)

all_elements =a | b  #return all unique elements for both sets OR
print(all_elements)



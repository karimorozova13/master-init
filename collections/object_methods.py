obj = ['a', 'b']
obj.append('c')
print(obj)

# obj.clear()
print(obj)

obj.remove('b') #will be an error if el doesn't exist
print(obj)

# remove by idx , by default remove the last one
chars = ['k', 'l', 'm']
middle_char = chars.pop(1)
print(chars)
print(middle_char)

# concat 2 lists
list1 = [1,2,3]
list2 = ['w', 'e',]
list1.extend(list2)
print(list1)

# add el on the idx position
list3 = [1,2,3]
list3.insert(1,13)
print(list3)

# find idx of el
idx_of_3 =list3.index(3)
print(idx_of_3)

#count the same elements
list4 = [1,2,3,1]
count_of_1 = list4.count(1)
print(count_of_1)

# sort hte list .sort(key=None, reverse=False)
list5 = ['k', 'a', 'z', 'b']
list5.sort()
print(list5)

# reverse the list
list5.reverse()
print(list5)

# copy of list
copy_list = list5.copy()
print(copy_list)

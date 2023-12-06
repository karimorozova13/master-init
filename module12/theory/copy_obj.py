import copy

my_l = [1,2,3]
copy_l = my_l
copy_l.append(4)
print(my_l)

# for lists and dict
l = [1,2,3]
copied = l[:]
copied.append(4)
print(l)

d= {1:'a'}
copy_d = {**d}
copy_d.update({2:'b'})
copy_d[3]= 'c'
print(d)
print(copy_d)


# copy.copy make unique first level, not deeper

my_list  = [1, 2, {1: 'a'}]
new_list = copy.copy(my_list)
new_list.append(4)

print(my_list)
print(new_list)

new_list[2][2] = 'b'

print(my_list)
print(new_list)

# copy.deepcopy make unique list

my_list  = [1, 2, {1: 'a'}]
new_list = copy.deepcopy(my_list)
new_list.append(4)

print(my_list)
print(new_list)

new_list[2][2] = 'b'

print(my_list)
print(new_list)

# copy object of user

class Expenses:
    def __init__(self) -> None:
        self.data = {}
        self.places =[]
    def spent(self, place, value):
        self.data[str(place)] = value
        self.places.append(place)
    def __copy__(self):
        copy_obj = Expenses()
        copy_obj.data = self.data
        copy_obj.places = self.places
        
        return copy_obj
    
    # mandadory parametr obj, where to save 
    def __deepcopy__(self,memo):
        copy_obj = Expenses()
        memo[id(self)] = copy_obj
        copy_obj.data = copy.deepcopy(self.data, memo)
        copy_obj.places = copy.deepcopy(self.places, memo)
        return copy_obj
    
expenses = Expenses()
expenses.spent('hotel', 240)
expenses.spent('swimming', 50)
print(expenses.places)
print(expenses.data)

e = copy.copy(expenses)
e.spent('bar', '400')
print(expenses.places)
print(e.places)

deep_e = copy.deepcopy(expenses)
print(deep_e is expenses)
deep_e.spent('kids', 1000)
print(expenses.places)
print(e.places)
print(deep_e.places)

#create an empty list
my_list = list()
empty_list = []

# completed list
completed_list = [1,3,'Kari']
my_name = completed_list[len(completed_list)-1]
print(my_name)

# order from the end
firtst_item = completed_list[-3]
last_item = completed_list[-1]

completed_list[0] = "Mo"

# slices (start idx, end idx - not included, step)
string = "My name is Kari"
new_str = string[3:8]
print(new_str)

numbers  = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = numbers[0:9:2]
even_numbers = numbers[1:9:2]
devided_by_three = numbers[2:9:3]
print(odd_numbers)
print(even_numbers)
print(devided_by_three)

# short version of slice
odd_numbers1 = numbers[::2]
even_numbers1 = numbers[1::2]
devided_by_three1 = numbers[2::3]
copy_numbers = numbers[:]
print(odd_numbers1)
print(even_numbers1)
print(devided_by_three1)
print(copy_numbers)



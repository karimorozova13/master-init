# check for an el in the collection
password = 'qwerty123'
if 'qwerty' in password or '123' in password:
    print("Your password is shit")

# sets
prime_nums = {1,3,5,7,9,13}
is_prime = 7 in prime_nums
print(is_prime)

# dictionary
user = {
    "name":"Kari",
    'age':13
}
if 'age' in user:
    print(f'{user["name"]} is {user["age"]} years old')

# length of colection
user_name = input('Your name: ')
if len(user_name)< 5:
    print('Very short')

# use loop
some_iterable = ["a", "b", "c"]
for i in some_iterable:
    print(i)

odd_nums = [1,3,5,7,9]
for num in odd_nums:
    print(num ** 2) #root square



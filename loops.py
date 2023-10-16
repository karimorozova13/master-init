# for loop

fruit = 'banana'
for char in fruit:
    print(char)

# while loop
a = 3
while a <= 5:
    # print(a)
    a = a +1

# break
b = 5
while True:
    # print(b)
    if b > 20:
        break
    b +=5

# infinite loop
while True:
    client_input = input()
    print(client_input)
    if client_input == "exit":
        break

# continue
x = 0
while x < 6:
    x += 1
    if not x % 2:
        continue
    print(x)



# break, continue terminates just one loop

# while True:
#     number = input("Number: ")
#     number = int(number) 
#     while True:
#         print(number)
#         number -=1
#         if number < 0:
#             break


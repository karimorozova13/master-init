first = 375
second = 575

gcd =first if first< second else second

while  first % gcd or  second % gcd:
    gcd -=1

sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    for i in range(num):
        if not (i+1) % 2:
            sum = sum +i+1
    print(sum)
        

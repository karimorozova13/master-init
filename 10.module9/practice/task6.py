def generator_numbers(string=""):
    arr = string.split(' ')
    new_a = []
    for word in arr:
        word = word.replace('$', '')
        word = word.replace('.', '')
        word = word.replace(',', '')
        if word.isdecimal():
            new_a.append(int(word))
    for num in new_a:
        yield int(num)
   
 

def sum_profit(string):
    total = 0
    for w in generator_numbers(string):
        total+= w

    return total

print(sum_profit("The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."))
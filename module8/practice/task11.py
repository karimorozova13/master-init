d ={
    '1':['.', ',', '?', '!', ':'],
    '2':['A', 'B', 'C'],
    '3':["D", 'E',"F"],
    '4':['G','H','I'],
    '5':['J','K','L'],
    '6':['M', 'N','O'],
    '7':['P','Q','R','S'],
    '8':['T', 'U', 'V'],
    '9':['W','X','Y', 'Z'],
    '0':[' ']
}

def sequence_buttons(string):
    new_s =''
    for ch in string.upper():
        for key,val in d.items():
            for i in range(len(val)):
                if ch ==val[i]:
                    new_s+= key*(i+1)
           
    return new_s
print(sequence_buttons("Hello, World!"))

# "4433555555666110966677755531111"
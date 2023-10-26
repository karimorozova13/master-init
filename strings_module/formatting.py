# decimal(10), hexadecimal(16), octal(8) and binary(2) representation
for i in range(16):
    s= 'int: {0:d}; hex: {0:x}: oct: {0:o}; bin: {0:b}'.format(i)
    print(s)

# display squares and cubes of numbers up 12
width = 5
for num in range(12):
    s= '{:^10} {:^10} {:^10}'.format(num,num**2, num**3)
    print(s)

# field name
s= '{name} {last_name}'.format(last_name='Mo', name="Kari")
print(s)

# conversion - convert el or display 'as is' !r !s
s1 ='{name!r} {last_name!s}'.format(last_name="Mo",name="Kari")
print(s1)

# specification :
    # whole numbers (decimal, octal, hexadecimal, etc.);
s2 = 'dec: {:d} hex: {:x} bin: {:b}'.format(15,15,15)
print(s2)

    # fractional numbers(round up)
s3='pi: {:0.3}'.format(3.1415)
print(s3)

    # how to display a number sign
s4 = '{} {:+} {:-} {: }'.format(1,2,3,4)
print(s4)

    # how to align the position of the element
s5 = '|{:<10} | {:*^10} | {:>10}'.format('left', 'center', 'right')
print(s5)

grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    count =0
    obj = []
    for name,grade in students.items():
        count+=1
        obj.append('{:>4}|{:<10}|{:^5}|{:^5}'.format(count, name,grade, grades[grade]))

    return obj
for el in formatted_grades({"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}):
    print(el)

def formatted_numbers():
    obj = ['|{:^10}|{:^10}|{:^10}|'.format('decimal', 'hex','binary' )]
    for i in range(16):
        obj.append('|{:<10}|{:^10}|{:>10}|'.format('{0:d}'.format(i),'{0:x}'.format(i),'{0:b}'.format(i)))

    return obj
for el in formatted_numbers():
    print(el)

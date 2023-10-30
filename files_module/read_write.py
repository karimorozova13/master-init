fh = open('new_gile.txt', 'w+')
fh.write('Kari')
fh.seek(0) # move cursor to position
first_symbols = fh.read(2) #you can read from position, for all file without arguments
print(first_symbols)
fh.close()

fh1 = open('new_gile.txt', 'r')
all_file = fh1.read()
print(all_file)
fh1.close()
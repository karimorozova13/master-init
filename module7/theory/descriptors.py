fh= open('test.txt', 'w+')

symbols = fh.write('first line\nsecond line\nthird line') #return len

print(fh.tell())
fh.seek(0) # move cursor
two_symbols = fh.readlines()

print(symbols,two_symbols)

fh.close()
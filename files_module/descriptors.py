# open file descriptor, open for reading
# fh= open('test_file.txt')

# in the end we should close the descriptor
# fh.close()

# 'r' - read file, default
#  'w' - write, rewrite. if nor exist create new one
#  'x' = write. if not exist, return exception
#  'a' - add to the end of file
# 'b' - open in binary mode
#  't' - open in text mode, default
#  '+' - open for read and write

fh1 = open('text_file', 'w')
symbols = fh1.write('Hi there') #return length
print(symbols)
fh1.close()
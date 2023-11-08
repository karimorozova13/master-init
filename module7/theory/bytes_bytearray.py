# with 1 byte we can write num  0...255

s = b'Hello!'
print(s[1]) # b'e'

byte_str= b'Hi there'
print(byte_str)

another_byte_str= 'Kari'.encode()
print(another_byte_str)

numbers = [0,128,255]
byte_nums= bytes(numbers)  #return str in hexadecimal format
print(byte_nums)

for num in numbers:
    print(hex(num))

# python use UTF-8 encode format
print(ord('a')) #return the number of symbol in UTF
print(chr(100)) #return the symbol 

str = "Kari"

utf8= str.encode()
print(utf8)

utf16 = str.encode('utf-16')
print(utf16)

s_from_utf16 = utf16.decode('utf-16')
print(s_from_utf16)

byte_arr= bytearray(b'Kill Bill')
byte_arr[0] = ord('B')
byte_arr[5] = ord('K')
print(byte_arr)
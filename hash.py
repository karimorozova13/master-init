message = "Hello world!"
# offset = int(input("Enter the offset: "))
# 'Hello my little friends!' -> 'Spwwz xj wteewp qctpyod!'
encoded_message = ""
for char in message:
   if char.isalpha() :
      is_upper = char.isupper()
      char = char.lower()
      shifted_char = chr((ord(char) - ord('a') + 37) % 26 + ord('a'))
      if is_upper:
         shifted_char = shifted_char.upper()
      encoded_message += shifted_char
   else:
      encoded_message += char
   print(encoded_message)

  
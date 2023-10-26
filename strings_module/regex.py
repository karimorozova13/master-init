import re

#  \d - any number, \d+ - one or more numbers
s= "my age is 17"
age = re.search('\d+', s) #return Match object or None, find just first match
print(age)

age1 = age.group() #return the matched val
print(age1)

s1 = "I bought 7 nuts for 6$ and 10 bolts for 3$."
numbers = re.findall('\d+', s1) #find all matches, return arr of them
print(numbers)

# to change all mathes with sub
s2 = re.sub(r'blue|white|red', 'colour', 'blue socks and red gloves')
print(s2)

# regex consists from blocks and modifies
# Blocks:

# \d - numbers or [0-9]
# \D - not number or [^0-9]
#  * - any caracter
# \s - any symbol: tab,space, line feed
# \w - any num or letter, underscore [a-zA-Z0-9_]
# \W - no num, no letter, no underscore

# Modifies quantity of matches

# ? - 0 or 1
#  + - 1 or more
#  * - 0 or more
# {n} - n times
#  {n,m} - from n to m times

def find_word(text, word):
    result=re.search(word, text)
    return {
        'result': True if result else False,
        'first_index': result.span()[0] if result else None,
        'last_index': result.span()[1] if result else None,
        'search_string': word,
        'string':text
    }
print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.","Kari"))
def find_all_words(text, word):
    words =re.findall(word, text, flags=re.IGNORECASE)
    return words
print(find_all_words("Guido van Rossum began working on PyThon in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.","Python"))

def is_spam_words(text, spam_words):
    new_text = text
    for word in spam_words:
      new_text=  re.sub(word, '*'*len(word), new_text, flags=re.IGNORECASE)
        
       
    return new_text
print(is_spam_words('Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', ['began' , 'Python']))
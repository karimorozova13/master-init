# string in several lines
s = """ First line
second
third"""
print(s)

# one line str, but better view in code
s1 = "Textual data in Python is handled with str objects, or strings."\
    "Strings are immutable sequences of Unicode code points."\
    "String literals are written in a variety of ways: single quotes, double quotes, triple quoted."
print(s1)

# if between stings are nothing, just space  - it's one string
s2 = ('hi ' 'there')
print(s2)

# carriage return \r
s3=("Hi\rthere")
print(s3)
print("Hi\rhello")
# \n new line
# \f new page
# \r carriage return
# \t horizontal tab
# \v vertical tab
print("vertical\vtab")
print("horizontal\ttab")
print("new\fpage")



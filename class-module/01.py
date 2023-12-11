import re

my_dict = {
    "name": "Kari",
    "age": 13
}


def fn(my_dict):
    next_fn(my_dict)
    
def next_fn(dict):
    print(dict)
    
fn(my_dict)


# module 5 14 task
def find_all_phones(text):
    pattern = r'\+\d{3}\(\d{2}\)\d{3}-\d{1}-\d{3}|\+\d{3}\(\d{2}\)\d{3}-\d{2}-\d{2}'
    result = re.findall(pattern, text)
    return result
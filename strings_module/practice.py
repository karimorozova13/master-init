def real_len(text):
    special_char=['\f', '\n', '\t', '\v', '\r']
    length = 0
    for chr in text:
        if chr not in  special_char:
            length +=1
    return length
real_len('Al\nKdfe23\t\v.\r')

articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    articles=[]
    for article in articles_dict:
        idx_title =article['title'].find(key) if letter_case  else article['title'].lower().find(key.lower())
        idx_author = article['author'].find(key) if letter_case  else article['author'].lower().find(key.lower())
        if idx_author >=0 or idx_title >= 0:
            articles.append(article)

    return articles
print(find_articles("Ocean", True))

def sanitize_phone_number(phone):
    new_ph = phone.strip().replace('+','').replace('(','').replace(')','').replace('-','').replace(' ', '')
    return new_ph
print(sanitize_phone_number("38050 111 22 11   "))

def is_check_name(fullname, first_name):
    return fullname.find(first_name) >=0
print(is_check_name('Kari Mo', "kari"))
def get_phone_numbers_for_countries(list_phones):
    phones ={
        "UA": [],
        "JP": [],
        "TW": [],
        "SG": []
    }
    for phone in list_phones:
        if sanitize_phone_number(phone).find('81',0,2) >= 0:
            phones["JP"].append(sanitize_phone_number(phone))
        
        elif sanitize_phone_number(phone).find('886',0,3) >= 0:
            phones["TW"].append(sanitize_phone_number(phone))
        elif sanitize_phone_number(phone).find('65',0,2) >= 0:
            phones["SG"].append(sanitize_phone_number(phone))
        else:
            phones["UA"].append(sanitize_phone_number(phone))
    return phones
print(get_phone_numbers_for_countries(['380998759405', '818765347', '8867658976', '657658976']))

def is_spam_words(text, spam_words, space_around=False):
    for word in spam_words:
        if text.lower().find(word.lower()) >= 0 and not space_around:
            return True
        elif space_around:
            if text.lower().find(f' {word.lower()} ') != -1 or text.lower().find(f' {word.lower()}.') != -1:
                return True
    return False
print(is_spam_words('Молох бог ужасен.', ['лох'], True))
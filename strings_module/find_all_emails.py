import re

def find_all_emails(text):
    result = re.findall(r'\b[A-Za-z0-9]{2,}[A-Za-z0-9._]*@[A-Za-z.]{2,}[A-Za-z]{2,}\b', text)
    new_result=[]
    for email in result:
        if email.split('@')[1].find('.') == -1:
            continue
        if email[0].isnumeric() and email[1].isnumeric():
           continue
        if len(email.split('@')[1].split('.')) > 2:
            a =email.split('@')[1].split('.')
            b= f'{a[0]}.{a[1]}'
            first = email.split('@')[0]
            new_result.append(f'{first}@{b}')
            continue
        if email[0].isnumeric() and isinstance(email[1], str):
           new_result.append(email.removeprefix(email[0]))
        else:
            new_result.append(email.removesuffix('.'))
  
    return new_result
print(find_all_emails('Simple email cool@api.io cool@api.i first.middle.last@iana.or a2@test.com a3@test.com.io 222111@test.com'))

def find_all_emails2(text):
    regex = r"[a-zA-Z]{1}[\w\.]+@[a-zA-z]+\.[a-zA-Z]{2,}"
    result = re.findall(regex,text)
    return result
print(find_all_emails2("Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net"))



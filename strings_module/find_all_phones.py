import re

def find_all_phones(text):
    pattern = r'\+\d{3}\(\d{2}\)\d{3}-\d{1,2}-\d{2,3}'
    result = re.findall(pattern, text)
    new_result= []
    for email in result:
        if len(email) > 17:
            new_result.append(email[:17])
            continue
        else:
            new_result.append(email)
    return new_result

print(find_all_phones('Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787'))
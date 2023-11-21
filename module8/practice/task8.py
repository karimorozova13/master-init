def token_parser(s):
    idx1 =s.find('+')
    idx2 =s.find('-')
    idx3 =s.find('/')
    idx4 =s.find('*')
    a =[]
    a.append(idx1)
    a.append(idx2)
    a.append(idx3)
    a.append(idx4)
    a.sort()
    b= []   
    
    for el in a:
        if el<=0:
            a.remove(el)
    
    b.append(s[:a[0]].strip())
    b.append(s[a[0]])
    b.append(s[a[0]+1:a[1]].strip())
    b.append(s[a[1]])
    b.append(s[a[1]+1:a[2]].strip())
    b.append(s[a[2]])
    b.append(s[a[2]+1::].strip())
  
    return b
print(token_parser("2+ 34-5 * 3"))


def tokenize_expression(expression):
    tokens = []
    current_token = ''

    for char in expression:
        if char.isdigit():
            # Додаємо цифру до поточної лексеми
            current_token += char
        elif char in ['+', '-', '*', '/']:
            # Додаємо поточну лексему та оператор до списку лексем
            if current_token:
                tokens.append(current_token)
                current_token = ''
            tokens.append(char)
        elif char == ' ':
            # Пропускаємо прогалини
            continue
        else:
            # Додаємо поточну лексему та дужку до списку лексем
            if current_token:
                tokens.append(current_token)
                current_token = ''
            tokens.append(char)

    # Додаємо останню лексему, якщо вона є
    if current_token:
        tokens.append(current_token)

    return tokens

# Приклад використання:
expression = "2+ 34-5 * 3"
result = tokenize_expression(expression)
print(result)

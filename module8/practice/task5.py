def capital_text(s):
    a = s.split()
    a[0]= a[0].title()
    idx = 0
    for el in a:
        if el.rfind('.') != -1 or el.rfind('?') != -1 or el.rfind('!') != -1:
            a[idx +1]=  a[idx +1].title()
        idx+=1

    # print(a)

    return (' '.join(a))
print(capital_text('hello world! awesome? yes'))
print(capital_text('alert. boss! oh'))

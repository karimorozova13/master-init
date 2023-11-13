data = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

def save_applicant_data(source, output):
    s =''
    for el in source:
        str =f"{el['name']},{el['specialty']},{el['math']},{el['lang']},{el['eng']}\n"
        s+=str
    with open(output, 'w') as fh:
        fh.write(s)

    return s
print(save_applicant_data(data, 'new_gile.txt'))
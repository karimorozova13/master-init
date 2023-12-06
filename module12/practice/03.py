import csv


l =   [ {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},{
    "name": "kari Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},{
    "name": "Brad Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},
       ]

def write_contacts_to_file(filename,contacts):
    with open(filename, 'w', newline='') as fh:
        name,email,phone,favorite = l[0].keys()
        writer = csv.DictWriter(fh, fieldnames=[name,email,phone,favorite])
        writer.writeheader()
        for el in contacts:
            writer.writerow({name:el[name], email:el[email],phone: el[phone],favorite:el[favorite]})
        
def read_contacts_from_file(filename):
    contacts = []
    with open(filename, newline='') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
           boolean_val =True if row['favorite']=='True' else False
           contacts.append({'name'.strip():row['name'], 'email':row['email'],'phone': row['phone'],'favorite':boolean_val})
    return contacts
        
write_contacts_to_file('new.csv', l)
print(read_contacts_from_file('new.csv'))
string_value = "False"
boolean_value = bool(string_value)

print(boolean_value)

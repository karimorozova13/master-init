import pickle
import json

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
    with open(filename, 'w') as fh:
        d = {"contacts": contacts}
        json.dump(d, fh)
def read_contacts_from_file(filename):
    with open(filename, 'r') as fh:
      contacts =  json.load(fh)['contacts']
      return contacts
        
write_contacts_to_file('new.json', l)
read_contacts_from_file('new.json')
        
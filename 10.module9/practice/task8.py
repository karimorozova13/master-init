def get_emails(list_contacts):
    l =[]
    for el in map(lambda el:el['email'], list_contacts):
        l.append(el)
    return l
contacts = [
    {
    "name": "Allen Raymond",
    "email": "kari.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},
{
    "name": "Allen Raymond",
    "email": "platon.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},
{
    "name": "Allen Raymond",
    "email": "lesha.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
]
print(get_emails(contacts))
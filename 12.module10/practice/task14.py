class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts
        

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append({
            "id":self.current_id,
            "name":name,
            "phone":phone,
            "email":email,
            "favorite":favorite
        })
        self.current_id +=1
    def get_contact_by_id(self, id):
        d= None
        for i in filter(lambda x: x["id"] ==id, self.contacts):
            d=i
        return d
    def remove_contacts(self, id):
        for i in range(len(self.contacts)):
            if self.contacts[i]['id'] == id:
                del self.contacts[i]
                break
        
con1 = Contacts()
con1.add_contacts('Wylie Pope', '(692) 802-2949','est@utquamvel.net', False)
con1.add_contacts( 'Cyrus Jackson','(501) 472-5218', 'nibh@semsempererat.com',False )
print(con1.list_contacts())
print(con1.get_contact_by_id(3))
con1.remove_contacts(1)
print(con1.list_contacts())

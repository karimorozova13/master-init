import pickle
import copy
class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite
    def __copy__(self):
        new = Person(self.name,self.email,self.phone,self.favorite)
        new.name = self.name
        new.email = self.email
        new.phone = self.phone
        new.favorite = self.favorite
        return new
    
class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0
        self.is_unpacking = False
        
    def save_to_file(self):
        with open(self.filename, 'wb') as fh:
            pickle.dump(self, fh)
        
    def read_from_file(self):
        with open(self.filename, 'rb') as fh:
            data = pickle.load(fh)
            return data
    def __getstate__(self) -> object:
        attributes = {**self.__dict__}
        attributes['count_save'] +=1
        return attributes
    def __setstate__(self,value):
        self.__dict__ = value
        self.is_unpacking =True
    def __copy__(self):
        new = Contacts(self.filename)
        new.filename = self.filename
        new.contacts = self.contacts
        new.is_unpacking =  self.is_unpacking 
        new.count_save =  self.count_save 
        return new

    def __deepcopy__(self, memo):
        new = Contacts(self.filename)
        memo[id(self)] = new
        new.filename = copy.deepcopy(self.filename, memo)
        new.contacts = copy.deepcopy(self.contacts, memo)
        new.is_unpacking =  copy.deepcopy(self.is_unpacking, memo )
        new.count_save =  copy.deepcopy(self.count_save, memo) 
        return new
    
    
    

def copy_class_contacts(contacts):
    new_obj= copy.deepcopy(contacts)
    return new_obj
        
    
contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons.is_unpacking)  # False
print(person_from_file.is_unpacking)  # True

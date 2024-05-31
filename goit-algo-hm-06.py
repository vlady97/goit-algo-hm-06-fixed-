from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
        pass

class Phone(Field):
    def __init__(self, value):
        if self.validate_phone(value):
             super().__init__(value)
        else: raise ValueError('Phone number should contain 10 digits.')
    
    @staticmethod
    def validate_phone(value):
         return value.isdigit() and len(value) == 10
             

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone):
         self.phones.append(Phone(phone))

    def remove_phone(self, phone):
         self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        try:
            Phone(new_phone)
        except ValueError as e:
            return str(e)
        
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return f'Phone number has changed from {old_phone} to {new_phone} for {self.name.value}'
        return f'Phone number {old_phone} not found for {self.name.value}'
    

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    
     def add_record(self, record):
          self.data[record.name.value] = record
     
     def find(self, name: str) -> Record:
            return self.data.get(name, None)
     
     def delete(self, name:str):
        if name in self.data:
            del self.data[name]


book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)


jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)


john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john) 


found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

book.delete("Jane")

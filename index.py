import os

def main():
    print("------------------------------------------")
    print("       Welcome in contact manager !       ")
    print("------------------------------------------")
    print("1. Add new contact\n2. Show all contact\n3. Delete a contact")
    print("------------------------------------------\n")

def creatContact():
    file = open("contact.txt", "w")
    file.close
    
def readContact():
    file = open("contact.txt", "r")
    contact = file.read()
    return contact

def addNewContact(name, phone, email):
    contact = name + " " + phone + " " + email
    file = open("contact.txt", "a")
    file.write(contact)

print("Hello Houssam !\n")
main()
select = input("Enter your chose : ")
print(select)
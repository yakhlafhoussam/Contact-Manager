import os

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

print("Hello Houssam !")

if os.path.exists("contact.txt"):
    print("The contact file is exist !")
    contact = readContact()
    print(contact)
else:
    print("The contact file not exist !")
    creatContact()
    print("The conatct file was created !")
    addNewContact("Houssam", "0615940605", "yakhlafhoussam@gmail.com")
    print("The New contact was created !")
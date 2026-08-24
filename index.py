import os

def main():
    print("------------------------------------------")
    print("       Welcome in contact manager !       ")
    print("------------------------------------------")
    print("1. Add new contact\n2. Show all contact\n3. Delete a contact\n4. Exit")
    print("------------------------------------------\n")
    selectGet()

def selectGet():
    select = int(input("Enter your chose : "))
    selectPost(select)

def selectPost(select):
    match select:
        case 1:
            print("Add new comming soon !")
        case 2:
            showAllContact()
        case 3:
            print("Add new comming soon !")
        case 4:
            print("Good bey !")
            quit()
        case _:
            print("Please select a suitable option from the list.")
            main()

def showAllContact():
    contact = readContact()
    print(contact)

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
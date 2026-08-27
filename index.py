import os
import platform

options = ["Add new contact", "Show all contact", "Delete a contact", "Exit"]

# Check file exist
def main():
    clear()
    if os.path.exists("contact.txt"):
        menu()
    else:
        creatContact()
        clear()
        successMsg("New contact file was created !")
        menu()

# Main Menu
def menu():
    print("------------------------------------------")
    print("     Welcome to HYK contact manager !     ")
    print("------------------------------------------")
    for index, option in enumerate(options):
        num = index + 1
        print(num, option)
    print("------------------------------------------\n")
    selectGet()

def selectGet():
    try:
        select = int(input("Enter your chose : "))
        selectPost(select)
    except ValueError:
        clear()
        errorMsg("Please enter a number.")
        menu()

def selectPost(select):
    match select:
        case 1:
            clear()
            addNewContact()
        case 2:
            clear()
            showAllContact()
            miniSelect()
        case 3:
            clear()
            deleteContact()
        case 4:
            exitApp()
        case _:
            clear()
            errorMsg("Please select a suitable option from the list.")
            menu()

# Messages
def errorMsg(msg):
    print(f"\033[31m{msg}\033[0m")

def askMsg(msg):
    print(f"\033[33m{msg}\033[0m")

def successMsg(msg):
    print(f"\033[32m{msg}\033[0m")

# Exit
def exitApp():
    clear()
    quit("\033[34mGood Bye !\033[0m")

# Clear Terminal
def clear():
    os_name = platform.system()
    os.system("clear" if os_name == "Linux" else "cls")

# Show All Contacts
def showAllContact():
    array = getAllContact()
    array = prepareContact(array)
    printContact(array)

def getAllContact():
    contact = readContact()
    array = contact.split("\n")
    return array

def prepareContact(array):
    finish = []
    for contact in array:
        if contact:
            finish.append(contact.split("|"))
    return finish

def printContact(contacts):
    print("---------------------------------------------------")
    print("                   All  Contacts                   ")
    print("---------------------------------------------------")
    for index, contact in enumerate(contacts):
        num = index + 1
        print(f"--------------------Contact N°{num}--------------------\n")
        print(f"Name  : {contact[0]}\nPhone : {contact[1]}\nEmail : {contact[2]}\n")
    print("---------------------------------------------------\n")

def miniSelect():
    print("\n1. Back to Menu\n2. Exit\n")
    getMiniSelect()

def getMiniSelect():
    try:
        select = int(input("Your choice : "))
        postMiniSelect(select)
    except ValueError:
        clear()
        errorMsg("Please enter a valide choices")
        miniSelect()

def postMiniSelect(select):
    match select:
        case 1:
            main()
        case 2:
            exitApp()
        case _:
            clear()
            errorMsg("Please chose from the choices")
            miniSelect()

# Build Contact File
def creatContact():
    file = open("contact.txt", "w")
    file.close

# Read Contact File
def readContact():
    file = open("contact.txt", "r")
    contact = file.read()
    return contact

# Add New Contact
def addNewContact():
    new = getNewContactInfo()
    createNewContact(new[0], new[1], new[2])
    clear()
    successMsg("The new contact was created")
    menu()

def getNewContactInfo():
    name = getName()
    while not name:
        clear()
        errorMsg("The name is required")
        name = getName()
    phone = getPhone()
    while not phone:
            clear()
            errorMsg("The phone is required")
            print(f"Name : {name}")
            phone = getPhone()
    email = getEmail()
    while not email:
            clear()
            errorMsg("The email is required")
            print(f"Name : {name}\nPhone : {phone}")
            email = getEmail()
    return (name, phone, email)

def getName():
    name = input("Name : ")
    return name

def getPhone():
    phone = input("Phone : ")
    return phone

def getEmail():
    email = input("Email : ")
    return email

def createNewContact(name, phone, email):
    contact = f"{name}|{phone}|{email}\n"
    file = open("contact.txt", "a")
    file.write(contact)
    file.close

# Delete a contact
def deleteContact():
    showAllContact()
    delete = getContactN()
    check = checkContact(delete)
    if not check:
        clear()
        errorMsg("This contact does't exist")
        menu()
    clear()
    printOneContact(delete)
    check = ValidateDelete()
    if check == "y":
        deleteContactN(delete - 1)
    else:
        clear()
        askMsg("The delete was cancled !")
        menu()

def getContactN():
    askMsg("Each contact you want to delete ?\n")
    while True:
        try:
            delete = int(input("Contact N° :"))
            return delete
        except ValueError:
            errorMsg("Please enter a valide choice")

def printOneContact(delete):
    contact = getAllContact()
    target = contact[delete -1]
    target = target.split("|")
    print(f"--------------------Contact N°{delete}--------------------\n")
    print(f"Name  : {target[0]}\nPhone : {target[1]}\nEmail : {target[2]}\n")
    print("---------------------------------------------------\n")

def checkContact(index):
    contacts = getAllContact()
    if index > len(contacts) or index <= 0 or not contacts[index -1]:
        return False
    else:
        return True

def ValidateDelete():
    askMsg("Are you sure ?")
    while True:
        try:
            delete = input("n/y : ")
            return delete
        except ValueError:
            errorMsg("Please enter a valide choice")

def deleteContactN(delete):
    contacts = getAllContact()
    del contacts[delete]
    rewriteContact(contacts)
    clear()
    successMsg("The contact was deleted !")
    menu()

def rewriteContact(contacts):
    creatContact()
    for contact in contacts:
        if contact:
            file = open("contact.txt", "a")
            file.write(f"{contact}\n")
            file.close

main()
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
        case 3:
            clear()
            print("Comming soon !")
            menu()
        case 4:
            exitApp()
        case _:
            clear()
            errorMsg("Please select a suitable option from the list.")
            menu()

# Messages
def errorMsg(msg):
    clear()
    print(f"\033[31m{msg}\033[0m")

def askMsg(msg):
    clear()
    print(f"\033[33m{msg}\033[0m")

def successMsg(msg):
    clear()
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
    miniSelect()

def getAllContact():
    contact = readContact()
    array = contact.split("\n")
    return array

def prepareContact(array):
    finish = []
    for contact in array:
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

# Create Contact File
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
    contact = f"\n{name}|{phone}|{email}"
    file = open("contact.txt", "a")
    file.write(contact)
    file.close

main()
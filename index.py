import os

options = ["Add new contact", "Show all contact", "Delete a contact", "Exit"]

def main():
    clear()
    if os.path.exists("contact.txt"):
        menu()
    else:
        creatContact()
        successMsg("New contact file was created !")
        menu()

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

def selectPost(select):
    match select:
        case 1:
            clear()
            print("Add new comming soon !")
            menu()
        case 2:
            clear()
            showAllContact()
        case 3:
            clear()
            print("Add new comming soon !")
            menu()
        case 4:
            clear()
            exitApp()
        case _:
            clear()
            errorMsg("Please select a suitable option from the list.")
            menu()

def errorMsg(msg):
    clear()
    print(f"\033[31m{msg}\033[0m")
    menu()

def askMsg(msg):
    clear()
    print(f"\033[33m{msg}\033[0m")

def successMsg(msg):
    clear()
    print(f"\033[32m{msg}\033[0m")

def exitApp():
    quit("""\033[35m
      ██████╗  ██████╗  ██████╗ ██████╗     ██████╗ ██╗   ██╗███████╗    ██╗
     ██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗    ██╔══██╗╚██╗ ██╔╝██╔════╝    ██║
     ██║  ███╗██║   ██║██║   ██║██║  ██║    ██████╔╝ ╚████╔╝ █████╗      ██║
     ██║   ██║██║   ██║██║   ██║██║  ██║    ██╔══██╗  ╚██╔╝  ██╔══╝      ╚═╝
     ╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝    ██████╔╝   ██║   ███████╗    ██╗
      ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝     ╚═════╝    ╚═╝   ╚══════╝    ╚═╝
    \033[0m""")

def clear():
    os.system("clear")

def showAllContact():
    array = getAllContact()
    array = prepareContact(array)
    print(array)

def getAllContact():
    contact = readContact()
    array = contact.split("\n")
    return array

def prepareContact(array):
    finish = []
    for contact in array:
        finish.append(contact.split("|"))
    return finish
    
def creatContact():
    file = open("contact.txt", "w")
    file.close
    
def readContact():
    file = open("contact.txt", "r")
    contact = file.read()
    return contact

def addNewContact(name, phone, email):
    contact = f"{name} {phone} {email}"
    file = open("contact.txt", "a")
    file.write(contact)

main()
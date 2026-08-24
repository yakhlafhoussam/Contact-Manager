import os

options = ["Add new contact", "Show all contact", "Delete a contact", "Exit"]

def main():
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
            main()
        case 2:
            clear()
            showAllContact()
        case 3:
            clear()
            print("Add new comming soon !")
            main()
        case 4:
            clear()
            print("Good bey !")
            quit()
        case _:
            clear()
            errorMsg("Please select a suitable option from the list.")
            main()

def errorMsg(msg):
    clear()
    print(f"\033[31m{msg}\033[0m")
    main()

def clear():
    os.system("clear")

def showAllContact():
    contact = readContact()
    print(contact)
    main()

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

main()
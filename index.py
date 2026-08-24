import os

print("Hello Houssam !")

if os.path.exists("contact.txt"):
    print("The contact file is exist !")
else:
    print("The contact file not exist !")
    file = open("contact.txt", "w")
    file.close
    print("The conatct file was created !")
contact = {"help":100}
def addContact(name,number):
    if name in contact:
        print("Name already exists!!")
    else:
        contact[name]=number
        print("Contact added successfully!!")

def searchContact(name):
    if name in contact:
        print("Your contact is",name,contact[name])
    else:
        print("No such contact are found ")

def deleteContact(name):
    if name in contact:
        del(contact[name])
        print("Contact deleted successfully!!")
    else:
        print("No such contact found!!")

def updateContact(name,number):
    if name in contact:
        contact[name]=number
        print("Contact updated successfully!!")
    else:
        print("!No such contact found!!")

def displayContact():
    print("Contacts are:")
    for k, v in contact.items():
        print(k, "-->", v)
    print("/n")

def favouriteContact(name):
    if name in contact:
        dict.get(name)
        print("Your favourite contact is",name,contact[name])
    else:
        print("No such contact are found ")

print("1-Add Contact\n2-Search Contact\n3-Delete Contact\n4-Update Conatct\n5-Display Contact\n6-Favourite Contact\n7-Exit")

#while True:
    #choice =int(input("Enter your choice(1/2/3/4/5/6/7))"))

    #if choice==1:
    #     name=input("Enter your name:")
    #     number=int(input("Enter your number:"))
    #     addContact(name, number)
    # elif choice==2:
    #     name=input("Enter your name:")
    #     searchContact(name)
    # elif choice==3:
    #     name=input("Enter your name:")
    #     deleteContact(name)
    # elif choice==4:
    #     name=input("Enter your name:")
    #     number=int(input("Enter your number:"))
    #     updateContact(name,number)
    # elif choice==5:
    #     displayContact()
    # elif choice==6:
    #     name=input("Enter your name:")
    #     number=int(input("Enter your number:"))
    #     favouriteContact(name, number)
    #     displayContact()
    # elif choice==7:
    #     print("Exit")
    #     break
    # else:
    #     print("Invalid input,please enter (1/2/3/4/5/6/7)")
    


    
    




    
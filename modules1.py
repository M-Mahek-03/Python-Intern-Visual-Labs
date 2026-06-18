import contact as ct 

choice =int(input("Enter your choice(1/2/3/4/5/6/7))"))
if choice==1:
    name=input("Enter your name:")
    number=int(input("Enter your number:"))
    ct.addContact(name, number)
elif choice==2:
    name=input("Enter your name:")
    ct.searchContact(name)
elif choice==3:
    name=input("Enter your name:")
    ct.deleteContact(name)
elif choice==4:
    name=input("Enter your name:")
    number=int(input("Enter your number:"))
    ct.updateContact(name,number)
elif choice==5:
    ct.displayContact()
elif choice==6:
    name=input("Enter your name:")
    number=int(input("Enter your number:"))
    ct.favouriteContact(name, number)
    ct.displayContact()
elif choice==7:
    print("Exit")
else:
    print("Invalid input,please enter (1/2/3/4/5/6/7)")
    

def passwordChecker(password):

    lengthRequired = 8
    upper = False
    lower = False
    digit = False
    symbol = False

    if len(password)>=lengthRequired:

        for i in password:
            if i.isupper():
                upper = True
            elif i.islower():
                lower = True
            elif i.isdigit():
                digit = True
            else:
                symbol = True
    else:
        print("Please enter 8 characters")

    if upper and lower and digit and symbol and len(password)>=lengthRequired:
        print("Strong Password!!")

    elif upper or lower and digit and len(password)>=lengthRequired:
        print("Moderate Password!!")

    else:
        print("weak Password!!")

pass1 = input("Enter password")
passwordChecker(pass1)

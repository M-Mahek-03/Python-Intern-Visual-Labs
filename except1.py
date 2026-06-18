try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    c = a / b
    print(c)

except ZeroDivisonError:
    print("Invalid number it is a integer error")

except ValueError:
    print("Ivalid Typing ")
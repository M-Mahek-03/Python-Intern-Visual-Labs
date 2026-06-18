n1 = int(input("Enter a value"))
operator = (input("Enter a operator"))
n2 = int(input("Enter a value"))

def calci(n1, operator, n2):
    if operator == "+":
        add = n1 + n2
        print("The sum of the two number is ",add)
    elif operator == "-":
        sub = n1 - n2
        print("The sum of the two number is ",sub)
    elif operator == "*":
        product = n1 * n2
        print("The sum of the two number is ",product)
    elif operator == "/":
        div = n1 / n2
        print("The sum of the two number is ",div)

calci(n1,operator,n2)
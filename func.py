#fn definition
def doSomething():
    print("Hello World")

def add(n1,n2):
    print(n1+n2)

def findsquare(n):
    return n*n

def findlargest(n1,n2):
    if(n1 > n2):
        return n1
    else:
        return n2

def swap(n1,n2):
    return n2, n1

#fn call

doSomething()
add(10, 20)
add("Mahek","Mukadam")
#add("T", 20)
print(findsquare(10))
print(findlargest(10, 20))
print(swap(10, 20))

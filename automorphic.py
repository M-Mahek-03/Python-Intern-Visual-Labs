#To Check a given number is Automorphic or Not
a = int(input("Enter the number: "))
b = a*a
print("Square of a number is: ",b)
if(a % 10 != b % 10):
    print(" a is not an automorphic")


else:
    print("is an automorphic")
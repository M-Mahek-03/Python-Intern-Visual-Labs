num = 10
def fibo(n1,n2):
    for i in range(0,num):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3)

print(fibo(0,1))
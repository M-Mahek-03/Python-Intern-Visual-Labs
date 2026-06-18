ls = [1,2,3,4,5]
sum=0 

def sum(ls):
    total=0
    i=0

    while i< len(ls):
        total = total + ls[i]
        i=i+1

    return total

print(sum(ls))
#print the sum of all elements in the list of 3 x 3

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
sum = 0
for outer in matrix:
    for inner in outer:
        print(inner)
        sum = sum + inner
print("sum of list is",sum)
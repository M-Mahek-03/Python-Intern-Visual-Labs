#Check how many elements of the list elements are armstrong number 
#(you can use a single list)

#example ls = [153, 270, 153, 103, 333]

ls = [153, 123, 783, 407, 313]
count = 0

for num in ls:
    
    temp = num
    rem = 0
    sum = 0

    while num > 0:
        rem = num % 10
        sum = sum + rem ** 3
        num = num//10


    if num == sum:
        print(temp,"is an Armstrong number") 
        count = count + 1

print("Total armstrong numbers are",count)
   
no = int(input("Enter the number: "))

sum = 0
copy_no = no

while (copy_no):
    last_digit = copy_no % 10
    sum = sum + last_digit
    copy_no //= 10

if no % sum == 0:
    print(f'{no} is a Niven number')
else:
    print(f'{no} is not a Niven number')

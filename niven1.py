n=int(input("enter n:"))

  sum = 0
  while n > 0:
    sum = sum + (n % 10)
    n //= 10
  return n % sum == 0


if no % sum == 0:
    print(f'{no} is a Niven number')
else:
    print(f'{no} is not a Niven number')
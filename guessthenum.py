import random as rd 
computer = rd.randint(1,27)
print("Please Enter your name:")
name = input()

print("OK", name, "Lets Start the game")

chances = 7

while chances >=1:
    choice=int(input("Enter your guess:"))

    if choice > computer:
        print("Your guess is High")

    elif choice < computer:
        print("Your guess is Low")

    elif choice == computer:
        break

    chances = chances-1
    print("You have",chances,"left")

if choice == computer:
    print("You won")
else:
    print("better luck next time")

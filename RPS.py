import random as rd

comp = 0
user = 0

chances = 5

while chances >=1 :
    computer = rd.choice(["R","P","S"])
    choice = input("Enter your choice (Enter R-Rock, P-Paper, S-Scissors): ")

    if choice == computer:
        print("Its a tie!!")

    elif choice == "R":
        if computer == "P":
            print("Its okay, Better luck next time",computer)
            comp = comp + 1
        else:
            print("Hureeey!!!",computer)
            user = user + 1
        
    elif choice == "P":
        if computer == "S":
            print("Its okay, Better luck next time",computer)
            comp = comp + 1
        else:
            print("Hureeey!!!",computer)
            user = user + 1
    
    elif choice == "S":
        if computer == "R":
            print("Its okay, Better luck next time",computer)
            comp = comp + 1
        else:
            print("Hureeey!!!",computer)
            user = user + 1

    else:
        print("please sahi seh enter ki jiya!!")

    chances = chances - 1

print("Computer->",comp)
print("User",user)

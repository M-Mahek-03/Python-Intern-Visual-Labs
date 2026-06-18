from random import randint

colors = ['red', 'blue', 'black', 'pink']
computer = randint(0,len(colors)-1)

print("Please Enter your name:")
name = input()

print("OK", name, "Lets Start the game")
guess = input('guess a color: ')

for color in colors[computer]:
    if guess != colors[computer]:
        print('wrong, try again')
        guess = input('guess a color: ')
    elif guess == colors[computer]:
        break


print('yay, color was: ' + colors[computer])
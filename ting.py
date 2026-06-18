no_of_words = 0
with open("test.txt","r") as f:
    lines = len(f.readlines())
    print(f"Numbers of lines are {lines}")
f = open("test.txt","r")
data = f.read()
no_of_chars = len(data)
print(f"No of characters are {no_of_chars}")
for letter in data:
    if letter == " " or letter == "\n":
        no_of_words = no_of_words + 1
no_of_words = no_of_words + 1
print(f"Number of words are {no_of_words}")
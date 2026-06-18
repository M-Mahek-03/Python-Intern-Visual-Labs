import turtle
colours = ["red", "purple", "blue", "green", "orange", "yellow"]
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(10)
for x in range(360):
    t.pencolor(colours[x % 6])
    t.width(x//100 + 2)
    t.forward(x)
    t.left(59)
# a program that draws dots randomly with colors. 

import turtle
import random

# list of colors
colors = ["red", "green", "blue", "yellow", "orange", "black", "purple"]

turtle.shape("turtle")
turtle.color("green")
turtle.speed(1)
turtle.penup()

for i in range(100):
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    
    # set a random turtle position
    turtle.setposition(x, y)
    # set a random color
    i = random.randint(0, len(colors) - 1)
    
    turtle.dot(colors[i])

turtle.done()

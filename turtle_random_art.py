# a program that draw line-dot randomly and print the random position of all the dots. 

import turtle
import random

for i in range(1, 21):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.setposition(x, y)
    if i == 1:
        print(i, "st point position:", turtle.position())
    elif i == 2:
        print(i, "nd point position:", turtle.position())
    elif i == 3:
        print(i, "rd point position:", turtle.position())
    else:
        print(i, "th point position:", turtle.position())
    turtle.dot()

turtle.done()

# drawing a wheel

import turtle
turtle.speed(5)
turtle.shape("turtle")
turtle.color("red")

counter = 0
while counter < 36:
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.right(10)
    counter += 1
turtle.exitonclick()

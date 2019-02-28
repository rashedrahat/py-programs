# drawing a wheel

import turtle
turtle.speed(5)
turtle.shape("turtle")
turtle.color("red")

c = 0
while c < 36:
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.right(10)
    c += 1
turtle.exitonclick()

# a program of method overriding.

import turtle

class AjobTurtle(turtle.Turtle):
    """AjobTurtle inherits Turtle class of the turtle module."""
    def forward(self, pixel):
        super().backward(pixel)
            
    def backward(self, pixel):
        super().forward(pixel)

    def left(self, angle):
        super().right(angle)

    def right(self, angle):
        print("I won't turn right! I'm a ajob turtle!")

if __name__ == "__main__":
    montu = AjobTurtle()
    montu.left(30)
    montu.forward(200)
    montu.left(45)
    montu.backward(100)
    montu.right(90)
    montu.forward(10)

    montu = turtle.Turtle()
    montu.shape("turtle")
    montu.left(30)
    montu.forward(10)
    montu.left(45)
    montu.backward(100)
    montu.right(90)
    montu.forward(10)
    montu.right(90)
    montu.forward(33)

    turtle.done()
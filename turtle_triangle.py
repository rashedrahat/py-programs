import turtle
turtle.shape("turtle")
turtle.color("blue")
turtle.speed(5)

def draw_triangle(side_length):
	for i in range(3):
		turtle.forward(side_length)
		turtle.left(120)

draw_triangle(100)

turtle.exitonclick()

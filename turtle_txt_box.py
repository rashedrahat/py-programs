# taking input by turtle text box and tell greeting based on name title.

import turtle
name = turtle.textinput("Name", "What's your name?")
name = name.lower()
if name.startswith("ms") or name.startswith("miss") or name.startswith("mrs") or name.startswith("mrs."):
	print("Hello mam, how are you?")
elif name.startswith("mr.") or name.startswith("mr"):
	print("Hello sir, how are you?")
else:
    name = name.capitalize()
    str = "Hi " + name + "! How are you?"
    print(str)

turtle.exitonclick()

# a program that handles the exceptions on two numbers' division.

def divide(a, b):
	try:
		return a / b
	except ZeroDivisionError as e1:
		print("Can't divide by 0")
	except TypeError as e2:
		print("Can't divide by string! Please enter an integer value.")

print(divide(5, 5))
print(divide(3, 0))
print(divide("8", 2))
print(divide(10, 5))
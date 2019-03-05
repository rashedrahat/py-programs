# arithmetic operation based on the user's choice.

terminate_program = False
while not terminate_program:
	num1 = input("Enter a number: ")
	num2 = input("Enter another number: ")
	num1 = int(num1)
	num2 = int(num2)

	while True:
		operation = input("What kind of claculation do you want? Write 'add'/'sub'/'mul'/'div' for showing calculation result or 'quit' to end.. ")

		if operation == "quit":
			terminate_program = True
			break
		if operation not in ["add", "sub", "mul", "div"]:
			print("Unknown operation!")
			continue
		if operation == "add":
			print("Sum result:", num1 + num2)
		if operation == "sub":
			print("Subtract result:", num1 - num2)
		if operation == "mul":
			print("Sum result:", num1 * num2)
		if operation == "div":
			print("Sum result:", num1 / num2)
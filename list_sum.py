# sum result of all the numbers in a list by a function

def add_numbers(numbers):
	if len(numbers) == 0:
		print("Empty list!")
	else:
		result = 0
		for number in numbers:
			result += number
		return result

sum_result1 = add_numbers([])
sum_result2 = add_numbers([1, 5, 7, 4, 8, 9])
print("Result-1:", sum_result1)
print("Result-2:", sum_result2)
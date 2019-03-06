# average result of all the numbers in a list by a function

def avg_numbers(numbers):
	result = 0
	n = len(numbers)
	for number in numbers:
		result += number
	result = result / n
	return result

result = avg_numbers([1, 5, 7, 4, 8, 9])
print("Average result:", result)
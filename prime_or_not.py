def is_prime(num):
	if num < 2:
		return False
	prime = True
	for x in range(2,num):
		if num % x == 0:
			print(num, "is divisible by", x)
			prime = False
	return prime

while True:
	number = input("Enter a number to check it's prime or not? (enter 0 to exit): ")
	number = int(number)
	if number == 0:
		break
	prime = is_prime(number)
	if prime is True:
		print(number, "is prime!")
	else:
		print(number, "isn't prime!")

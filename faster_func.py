# a program that will show the difference between functions. Which one is more faster?

import math

def is_prime1(num = 1013):
	if num < 2:
		return False
	if num == 2:
		return True
	if num % 2 == 0:
		return False
	prime = True
	for x in range(3,num,2):
		if num % x == 0:
			print(num, "is divisible by", x)
			prime = False
			return prime
	return prime

def is_prime2(num = 1013):
	if num < 2:
		return False
	if num == 2:
		return True
	if num % 2 == 0:
		return False
	m = math.sqrt(num)
	m = int(m) + 1
	prime = True
	for x in range(3,m,2):
		if num % x == 0:
			print(num, "is divisible by", x)
			prime = False
			return prime
	return prime

import timeit
t1 = timeit.timeit(is_prime1)
t2 = timeit.timeit(is_prime2)
print(t1, t2, "time diff:", t1 / t2, "X")

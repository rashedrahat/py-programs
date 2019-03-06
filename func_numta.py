# multiplication table by a function

def multiplication_tab(num = 1):
	m = 1
	while m <= 10:
		print(num, "X", m, "=", num * m)
		m += 1

multiplication_tab()
multiplication_tab(4)
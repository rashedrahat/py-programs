def swap_case(s):
	new_s = ""
	for x in s:
		if x in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]:
			low_case = x.lower()
			new_s = new_s + low_case
		elif x in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
			cap_case = x.upper()
			new_s = new_s + cap_case
		else:
			new_s = new_s + x
	return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
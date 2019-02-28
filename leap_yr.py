yr = input("Enter a year to check whether it's leap year or not: ")
yr = int(yr)

if yr % 4 == 0 and yr % 100 != 0:
	print(yr, "is leap year!")
elif yr % 100 == 0 and yr % 400 == 0:
	print(yr, "is leap year!")
else:
	print(yr, "isn't leap year!")
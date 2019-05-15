# reading data from a file in three different ways.

# step 1
with open("file.txt", "r") as f:
	content = f.read()
	print(content)
# step 2
with open("file.txt", "r") as f:
	lines = f.readlines()
	print(lines)
	for line in lines:
		print(line)
# step 3
with open("file.txt", "r") as f:
	print(f)
	for line in f:
		print(line)
# a program of printing a new list where each and every list is a square value of the previous list.

list = [1, 2, 10, 12, 15]
new_li = []
new_li = [x ** 2 for x in list]
print(new_li)

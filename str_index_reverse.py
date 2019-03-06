# a program of rerversing all the index pairs in a string.
str = input("Enter a string: ")
li = list(str)
ln = len(li)
newStr = ""
i = 0

if ln % 2 == 0:
    while i <= (ln - 1):
        a = li[i]
        b = li[i + 1]
        li[i] = b
        li[i + 1] = a
        newStr = newStr + b + a
        i = i + 2
else:
    while i < (ln - 1):
        a = li[i]
        b = li[i + 1]
        li[i] = b
        li[i + 1] = a
        newStr = newStr + b + a
        i = i + 2
    newStr = newStr + li[(ln - 1)]
        
print(newStr)


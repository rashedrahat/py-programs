# a program breaking the string into new four string. Where string formats are capital, lower, digit, and special char type string.

str = input("Enter a string: ")

cap = ""
low = ""
num = ""
spc_char = ""
    
for s in str:
    if s in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        cap = cap + s
    elif s in "abcdefghijklmnopqrstuvwxyz":
        low = low + s
    elif s in "0123456789":
        num = num + s
    else:
        spc_char = spc_char + s

print(cap)
print(low)
print(num)
print(spc_char)

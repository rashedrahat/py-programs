import turtle #importing the turtle module.

str = turtle.textinput("PALINDROME or not?", "Enter a string") #taking a string from user & storing into variable through turtle text box.
li = list(str) #converting the string into list & storing into variable.
ln = len(li) #storing the length of the list into a variable.
revStr = "" #defining a empty variable (which will be updated & will be final result to check palindrome).
i = ln - 1 #value of i will be used in loop.

while i >= 0: #here logic is to taking values from right to left from the list named "li". That means going from last to first index of the list.
    revStr = revStr + li[i] #concatenating & updating the "revStr" variable.
    i = i - 1 #decreasing the value of to reach from the last index to first index.
    
str = str.lower() #converting value into lowercase string.
revStr = revStr.lower() #converting the final output into lowercase string.

if str == revStr: #the two string is same or not?
    print(str, ", is PALINDROME!") #if same.
else:
    print(str, ", isn't PALINDROME!") #if not same.

turtle.exitonclick()
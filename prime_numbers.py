# a program that will print all the prime numbers between a given range

lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  

print("List of prime numbers:")  
for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:  
        	print(num)
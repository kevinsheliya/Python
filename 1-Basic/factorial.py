# Write a program that calculates the factorial of a number input by the user using a while loop.

n=int(input("enter the number :"))
fact=1

while n>=1:
    fact=fact*n
    n=n-1


print("factorial :",fact)    
    
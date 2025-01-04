# Write a program that calculates the sum of the digits of a number input by the user using a while loop.

n = int(input("enter the number"))
remainder = 0
sum = 0

while n!=0:
    remainder = n % 10
    sum = sum + remainder
    n = n/10

print("digit of sum = ",int(sum))    

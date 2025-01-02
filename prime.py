# Write a program that checks if a number input by the user is a prime number using a for loop.

num=int(input("please enter the number : "))

if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not prime")
            break
    else:
        print(num,"is prime")


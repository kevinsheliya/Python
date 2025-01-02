def fibonacci(num):
    if num<=2:
        return num
    else:
        return fibonacci(num-1) +fibonacci(num-2)


x=fibonacci(5)
print(x)


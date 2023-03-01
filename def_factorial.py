import math

def factorial(x):
    if x == 0:
        return 1
    else:
        return math.factorial(x)

num = 10
factorial(num)  # called num in place of x (def factorial(x))

print(f"Factorial of {num} is {factorial(num)}")





import math

#Welcome note
print("Welcome to the Factorial Calculator App\n")

#user input
num = int(input("What number would you like to compute the factorial of? "))

print(f"{num}! = ", end=" ")
for i in range(1,num):
    print(i, end='*')
print(num)
    
# math library
n = num*math.factorial(num-1)   # n! = n*(n-1)!


print("\nHere is the result from the math library: ")
print(f"The factorial of {num} is {math.factorial(num)}!")

# own algorithm
print("\nHere is the result from my own algorithm:")
print(f"The factorial of {num} is {n}!")

print(f"\nIt is shown twice that {num}! = {n} (with excitement)")


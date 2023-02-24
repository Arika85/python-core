
# Sol: 1

#Welcome note
print("Welcome to the Fibonacci Calculator App\n")

#user input of fibonacci count
count = int(input("How many digits of the Fibonacci Sequence would you like to compute: "))

print(f"\nThe first {count} numbers of the Fibonacci sequence are: ")

#Initialising fibonacci list
fib = [1,1]

#Computing fibonacci numbers
for i in range(count-2):
    result = fib[i] + fib[i+1]    #n = n1 + n2
    fib.append(result)

#Displaying fibonaci numbers
for j in fib:
    print(j)

#computing and displaying GOlden Ratio of Phi (Formula = # A, B = B/A or A+B/A)
print("\nThe corresponding Golden Ratio values are:")

for k in range(1, len(fib)):
    print(fib[k]/fib[k-1])  # A, B = B/A fib[k]   ..... k= 0 index, k-1 = previous index

print("\nThe ratio of consecutive Fibonacci terms approaches Phi: 1.618...")





# Sol:2

import math
# Welcome note
print("Welcome to Fibonacci Calculator App\n")

user_input = int(input("How many digits of the Fibonacci Sequence would you like to compute: "))

#compute values of fib
fib = [1,1]
for i in range(user_input-2):   # fib(n) = fib(n1)+fib(n2), where n1 = 1, n2 = 1 [i.e, fib =[1,1]]
    result = fib[i] + fib[i+1]
    fib.append(result)

#Display fib values
print(f"\nThe first {user_input} numbers of the Fibonacci sequence are:")
for num in fib:
    print(num)

#compute golden ratio
golden = []     # A, B then golden ration = B/A
for i in range(len(fib)-1):
    ratio = fib[i+1]/fib[i]
    golden.append(ratio)

#Display golden ratio values
print("\nThe corresponding Golden Ratio values are: ")
for j in golden:
    print(j)

print("The ratio of consecutive Fibonacci term approaches Phi: 1.618...")




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



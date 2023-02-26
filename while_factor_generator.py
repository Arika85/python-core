

# sol:1

import math
#Welcome note
print("Welcome to Factor Generator App\n")

flag = True

while True:
    #User input
    num = int(input("Enter a number to determine all factors of that number: "))

    #generating and displaying factors
    print(f"\nFactors of {num} are:")

    #while loop
    factors = []
    i = 1       # start the loop from 1
    while num >=i:
        if num%i == 0:
            print(i)
            factors.append(i)
        i +=1

            # or
    # for i in range(1,num+1):
    #     if num%i == 0:
    #         print(i)

    print("\nIn summary:")
    for i in range(int(len(factors)/2)):
        print(f"{factors[i]} * {factors[-i-1]} = {num}")
    
    choice = input('\nRun again(y/n): ').lower()
    if choice != 'y':
        flag = False
        print('Thank you for using program. Have a great day.')


    # for i, j in zip(factors, reversed(factors)):
    #         # l = len(factors)
    #         if i == j:
    #             break
    #         else:
    #             print(f'{i} * {j} = {i*j}')



print("\n*****************************************************************8")

# Sol 2:

# welcome screen
print('Welcome to the Factor Generator App')

flag = True
while flag:
    num = int(input('\nEnter a number to determine all factors of that number: '))
    # num=10
    # calculating factors
    factors=[]
    # for i in range(1,num+1):   ## using for loop
    #     if num%i==0:
    #         factors.append(i)
    i=1
    while num >= i:
        if num%i == 0:
            factors.append(i)
        i += 1

    # print
    print(f'\nFactors of {num} are: ')
    for i in factors:
        print(i)

    # summary
    print('\nIn summary: ')
    for i in range(int(len(factors)/2)):
        print(f'{factors[i]} * {factors[-i-1]} = {num}')
        
    
    choice = str(input('\nRun again(y/n): '))
    if choice != 'y':
        flag = False
        print('Thank you for using program. Have a great day.')








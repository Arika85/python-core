
def addition(num1,num2):
    """addition operation for user inputs"""
    add = num1 + num2
    return add

def subtraction(num1,num2):
    """subtraction operation for user inputs"""
    sub = num1 - num2
    return sub

def multiplication(num1,num2):
    """multiplication operation for user inputs"""
    mul = num1 * num2
    return mul

def division(num1,num2):
    """division operation for user inputs"""
    if num2 == 0:
        print("DIV ERROR")
    else:
        div = num1 / num2
        return div

def exponentiation(num1,num2):
    """exponentiation operation for user inputs"""
    exp = num1 ** num2
    return exp

def run():
    running = input("Would you like to run the program(y/n): ")
    return running

# Main program

#welcome note
print('Welcome to the Python Calculator App.')
print('Enter 2 numbers and an operation and the desired operation will be performed.')

result_dict = {}
# Main program
flag = True
while flag:
    first = float(input("\nEnter a number: "))
    last = float(input("Enter a number: "))
    choice = input("Enter an operation(addition, subtraction, multiplication, division or exponentiation): ").lower()
    if choice == 'addition' or choice == 'a':
        res_add = addition(first, last)
        result_dict['add'] = (f'{first} + {last} = {res_add}')
        print(f"The sum of {first} and {last} is {res_add}")
    elif choice == 'subtraction' or choice == 's':
        res_sub = subtraction(first,last)
        result_dict['sub'] = (f'{first} - {last} = {res_sub}')
        print(f"The difference of {first} and {last} is {res_sub}")
    elif choice == 'multiplication' or choice == 'm':
        res_mul = multiplication(first,last)
        result_dict['mul'] = (f'{first} * {last} = {res_mul}')
        print(f"The product of {first} and {last} is {res_mul}")
    elif choice == 'division' or choice == 'd':
        res_div = division(first,last)
        result_dict['div'] = (f'{first} / {last} = {res_div}')
        print(f"The division of {first} and {last} is {res_div}")
    elif choice == 'exponentiation' or choice == 'e':
        res_exp = exponentiation(first,last)
        result_dict['exp'] = (f'{first} ** {last} = {res_exp}')
        print(f"The exponent of {first} and {last} is {res_exp}")
    else:
        print("That is not a valid option.  Try again")
    
    res_run = run()
    if res_run != 'y':
        flag = False
        print("Calculation Summary:")
        for i in result_dict.values():
            print(i)
        print("\nThank you for using the Python Calculator App.  Goodbye")

print("\n***********************************************************")


sol 2:

# welcome msg
print('Welcome to the Python Calculator App.')
print('Enter 2 numbers and an operation and the desired operation will be performed.')

# funcs
def addition(a, b):
    c = a + b
    return c

def subs(a, b):
    c = a - b
    return c

def div(a, b):
    if b == 0:
        print('You cannot divide by zero')
    else:
        c = a/b
        return c

def expo(a, b):
    c = a**b
    return c

result_diction = {}
flag = True
while flag:
    # user in
    num_1 = float(input('\nEnter a number: '))
    num_2 = float(input('Enter a number: '))
    operation = str(input('Enter an operation (addition, subtraction, division or exponentiation): ')).lower().strip()

    # result_diction = {}
    # conditions
    if operation == 'addition' or operation == 'a':
        result = addition(num_1, num_2)
        result_diction['add'] = (f'{num_1} + {num_2} = {result}')
        print(f'The sum of {num_1} and {num_2} is {result}')
    elif operation == 'subtraction' or operation == 's':
        result = subs(num_1, num_2)
        result_diction['sub'] = (f'{num_1} - {num_2} = {result}')
        print(f'The difference of {num_1} and {num_2} is {result}')
    elif operation == 'division' or operation == 'd':
        result = div(num_1, num_2)
        result_diction['div'] = (f'{num_1} / {num_2} = {result}')
        print(f'The div of {num_1} and {num_2} is {result}')
    elif operation == 'exponentiation' or operation == 'e':
        result = expo(num_1, num_2)
        result_diction['exp'] = (f'{num_1} ** {num_2} = {result}')
        print(f'The expo of {num_1} and {num_2} is {result}')
    else:
        print('That is not a valid operation')

    choice = str(input('\nWould you like to run the program again(y/n): ')).lower()
    if choice != 'y':
        flag = False
        print('\nCalculation Summary: ')
        for i in result_diction.values():
            print(i)
        print('Okay Goodby')


# def arithmetic(num1, num2):
#     add = num1 + num2
#     sub = num1 - num2
#     multiply = num1 * num2
#     division = num1 / num2
#     # return four values
#     return add, sub, mul, div, exp

# # read four return values in four variables
# a, b, c, d = arithmetic(10, 2)

# print("Addition: ", a)
# print("Subtraction: ", b)
# print("Multiplication: ", c)
# print("Division: ", d)


    
    




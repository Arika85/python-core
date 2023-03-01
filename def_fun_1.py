# 1. Write a program to create function to accept name and age and print their value.

# #Sol :1
# def func1(name, age):
#     print(name)
#     print(age)

# func1("arika", 33)

# #Sol:2

# def hello(name, age):
#     print(f'hello {name} {age}')

# hello("shubha", 21)

# print("**********************************************")

#2. Write a program to create function func1() to accept a variable length of arguments and print their value.

# Sol:1

# def func2(*args):
#     for i in args:
#         print(i)
# print("Printing Values")

# # Sol:2
# def func2(*args):
#     a= list(args)
#     for i in args:
#         print(i)
# print("Printing Values")

# func2(20, 30, 40)
# func2(80,100)

# print("**********************************************")

#3. Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call

# sol:1

# def calculation(a, b):
#     add = a + b
#     sub = a - b
#     return add, sub

# res = calculation(40, 10)
# print(res)

#Sol:2

# def calculation(a, b):
#     return a + b, a - b
#         # get result in tuple format
#         # unpack tuple
# add, sub = calculation(40, 10)
# print(add, sub)

# print("**********************************************")

#4. Write a program to create a function show_employee() using the following conditions.
        # It should accept the employee’s name and salary and display both.
        # If the salary is missing in the function call then assign default value 9000 to salary

# def showEmployee(name, salary=9000):
#     print(f"Name: {name} Salary: {salary}")

# showEmployee("Ben", 12000)
# showEmployee("Jessa")

# print("**********************************************")

#5: Create an inner function to calculate the addition in the following way
    # Create an outer function that will accept two parameters, a and b
    # Create an inner function inside an outer function that will calculate the addition of a and b
    # At last, an outer function will add 5 into addition and return it

# Sol:1
# def outer(a,b):
#     a,b
#     def inner(a,b):
#         return a+b
#     return inner(a,b) +5

# res = outer(3,4)
# print(res)

# Sol:2
#Outer function
# def outer_fun(a, b):
#     square = a ** 2

#     # inner function
#     def addition(a, b):
#         return a + b

#     # call inner function from outer function
#     add = addition(a, b)
#     # add 5 to the result
#     return add + 5

# result = outer_fun(5, 10)
# print(result)

# print("**********************************************")
# Exercise 6: Create a recursive function
        # Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
        # A recursive function is a function that calls itself again and again.

# Sol:1
# def recur(a):
#     res = sum(range(0,a+1))
#     return res

# sol = recur(10)
# print(sol)

# Sol:2 (recursive function)
# def addition(num):
#     if num:
#         # call same function by reducing number by 1
#         return num + addition(num-1)
#     else:
#         return 0

# res = addition(15)
# print(res)

# print("**********************************************")

# Exercise 7: Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.

# # sol:1
# def display_student(name, age):
#     print(name, age)

# # call using original name
# display_student("Emma", 26)

# # assign new name
# showStudent = display_student
# # call using new name
# showStudent("Emma", 26)

# # call using new name
# abc = showStudent("Rithvik", 9)
# abc

# print("**********************************************")

# Exercise 8: Generate a Python list of all the even numbers between 4 to 30

# def even(a,b):
#     sum = []
#     for i in range(a,b):
#         if i%2 ==0:
#             sum.append(i)       
#     print(sum)

# even(4,30)

# Sol:2 (using list)
# print(list(range(4, 30, 2)))

# print("**********************************************")

# Exercise 9: Find the largest item from a given list

# sol:1
# x = [4, 6, 8, 24, 12, 2]
# print(max(x))

# Sol:2
# def high(x):
#     return (max(x))

# a = [4, 6, 8, 24, 12, 2]

# res = high(a)
# print(res)










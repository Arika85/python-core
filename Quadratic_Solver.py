
# Sol: 1

import cmath

# Welcome Note
print("Welcome to the Quadratic Solver App.")

print("\nA quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.\n")

equation = int(input("How many equations would you like to solve today: "))

print("\nSolving equation #1")
print("-----------------------------------------------------------------")

a = int(input("Please enter your value of a (coefficient of x^2): "))
b = int(input("Please enter your value of a (coefficient of x): "))
c = int(input("Please enter your value of a (coefficient): "))

print(f"\nThe solutions to {float(a)}x^2 + {float(b)}x + {float(c)} are:")

d = (b**2) - (4*a*c)

x1 = (-b-cmath.sqrt(d))/(2*a)  
x2 = (-b+cmath.sqrt(d))/(2*a)

print(f"\tx1 = {x1}")
print(f"\tx2 = {x2}")

# Equation 2
print("\nSolving equation #2")
print("-----------------------------------------------------------------")

x = int(input("Please enter your value of a (coefficient of x^2): "))
y = int(input("Please enter your value of a (coefficient of x): "))
z = float(input("Please enter your value of a (coefficient): "))

print(f"\nThe solutions to {a}x^2 + {b}x + {c} are:")

k = (y**2) - (4*x*z)

p1 = (-y-cmath.sqrt(k))/(2*x)  
p2 = (-y+cmath.sqrt(k))/(2*x)

print(f"\tx1 = {p1}")
print(f"\tx2 = {p2}")

print("Thank you for using Quadratic Solver App.  Goodbye.")
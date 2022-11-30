
# Sol:1 
import math
print("Welcome to the Right Triangle Solver App\n")

first = int(input("What is the first leg of the triangle: "))
second = float((input("What is the second leg of the triangle: ")))

hypotenuse = math.sqrt(first**2+ second**2)
area = 0.5 * first * second
print(f"\nFor a traingle with legs of {first} and {second} the hypotenuse is {round(hypotenuse, 3)}")
print(f"For a traingle with legs of {first} and {second} the area is {round(area, 1)}")

# Sol: 2
# Import math Library
import math
# welcome message
print("Welcome to the Right Triangle solver App.\n")
# getting first side
first_leg = float(input("What is the First leg of the Triangle: "))
# getting second side
second_leg = float(input("What is the Second leg of the Triangle: "))
# calculating hypotenuse
hyp = math.hypot(first_leg, second_leg)
# calculating area
area = 0.5 * first_leg * second_leg
print(f"\nFor Triangle with legs of {first_leg} and {second_leg} the hypotenuse is {round(hyp, 3)}")
print(f"For Triangle with legs of {first_leg} and {second_leg} the area is {round(area, 1)}")

#Sol: 3
from math import sqrt
print('Welcome to the Right Triangle Solver\n')

first_leg = float(input('What is the first leg of the triangle:'))
second_leg = float(input('What is the second leg of the triangle:'))
c = sqrt(first_leg*2 + second_leg*2)
 
s = (first_leg+second_leg+c)/2

Area = (s*(s-first_leg)(s-second_leg)(s-c)) ** 0.5

print("For a triangle with",first_leg,'and',second_leg,'the hypotheneus is',round(c,3))
print('For a triangle with leg',first_leg,'and',second_leg,'the area is ',round(Area,3))



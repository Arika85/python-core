#Q1: Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
    
# v = Vehicle(100, 20)
# print(v.max_speed, v.mileage)

# print("***********************************************************")
# OOP Exercise 2: Create a Vehicle class without any variables and methods

# class Vehicle:
#     pass

# # print("***********************************************************")
# # OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle 

# # 1st method
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name.title()
#         self.max_speed = max_speed
#         self.mileage = mileage
    
# class Bus(Vehicle):
#     def __init__(self, name, max_speed, mileage):
#         super().__init__(name, max_speed, mileage)
#         print(f"Vehicle Name: {self.name} Speed: {self.max_speed} Mileage: {self.mileage}")

# bus1 = Bus("school volvo", 180, 12)

# # 2nd method
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 180, 12)
# print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

# # print("***********************************************************")
# OOP Exercise 4: Class Inheritance
# Given:

# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return (f"The seating capacity of a {self.name} is {capacity} passengers")
    
# class Bus(Vehicle):
#     pass

#     def seating_capacity(self, capacity=50):
#         return (f"The seating capacity of a {self.name} is {capacity} passengers")

# a = Bus('bus', 180, 12)
# print(a.seating_capacity())

# # 2nd method
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"

# class Bus(Vehicle):
#     # assign default value to capacity
#     def seating_capacity(self, capacity=50):
#         return super().seating_capacity(capacity=50)

# School_bus = Bus("School Volvo", 180, 12)
# print(School_bus.seating_capacity())

# # print("***********************************************************")

# OOP Exercise 5: Define a property that must have the same value for every class instance (object)
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

# Use the following code for this exercise.

# 1st method
# class Vehicle:
#     def __init__(self, name, max_speed, mileage, color='white'):
#         self.name = name.title()
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.color = color.title()

# class Bus(Vehicle):
#     pass

# class Car(Vehicle):
#     pass

# bus = Bus('school volvo', 180, 12)
# print(f"Color {bus.color}, Vehicle name: {bus.name}, Speed: {bus.max_speed}, Mileage: {bus.mileage}")

# car = Car('audi q5', 240, 18)
# print(f"Color {car.color}, Vehicle name: {car.name}, Speed: {car.max_speed}, Mileage: {car.mileage}")

# 2nd method
# class Vehicle:
#     def __init__(self, name, max_speed, mileage, color='White'):
#         self.name = name.title()
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.color = color.title()

# class Bus(Vehicle):
#     def __init__(self, name, max_speed, mileage, color='White'):
#         super()._init_(name, max_speed,mileage, color)
#         print(f'Color: {self.color}, Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {mileage}')

# class Car(Vehicle):
#     def __init__(self, name, max_speed, mileage, color='White'):
#         super().__init__(name, max_speed,mileage, color)
#         print(f'Color: {self.color}, Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {mileage}')

# bus = Bus('volvo', 180, 12)
# car = Car('audi q5', 240, 18)

# # 3rd and easy method
# class Vehicle:
#     # Class attribute
#     color = "White"

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     pass

# class Car(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 180, 12)
# print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

# car = Car("Audi Q5", 240, 18)
# print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)

# # print("***********************************************************")
# OOP Exercise 6: Class Inheritance
# Given:

# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
# Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class in Bus class.

# Use the following code for your parent Vehicle class. We need to access the parent class from inside a method of a child class.

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

#     def fare(self):
#         return self.capacity * 100

# class Bus(Vehicle):

#     def fare(self):
#         return (self.capacity * 100) + (self.capacity * 100 * 10/100)

# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare())

# # 2nd method
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

#     def fare(self):
#         return self.capacity * 100

# class Bus(Vehicle):
#     def fare(self):
#         amount = super().fare()
#         amount += amount * 10 / 100
#         return amount

# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare())

# # print("***********************************************************")

# OOP Exercise 7: Check type of an object
# Write a program to determine which class a given Bus object belongs to.

# Given:

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 12, 50)

# print(type(School_bus))
# print(issubclass(Bus, Vehicle))

# # print("***********************************************************")

# OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 12, 50)
# print(isinstance(School_bus, Vehicle))

# # print("***********************************************************")

# Exercise 5: Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# import random
# import string

# length = 5
# res = ''.join(random.choices(string.hexdigits, k = length))
# print(res)

# 2nd method
# import random
# import string

# def randomString(stringLength):
#     """Generate a random string of 5 charcters"""
#     letters = string.ascii_letters
#     return ''.join(random.choice(letters) for i in range(stringLength))

# print ("Random String is ", randomString(5) )

# # print("***********************************************************")
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i, num in enumerate(numbers):
#     if num % 3 == 0:
#         numbers[i] = "fizz"
#     if num % 5 == 0:
#         numbers[i] = "buzz"
#     if num % 5 == 0 and num % 3 == 0:
#         numbers[i] = "fizzbuzz"
    
# print(numbers)

# # print("***********************************************************")
# Exercise 6: Generate a random Password which meets the following conditions

# Password length must be 10 characters long.
# It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

# import random
# import string

# length = 10
# res = ''.join(random.choices((string.ascii_uppercase) + (string.digits) + (string.punctuation), k = length))
# print(res)

# # print("***********************************************************")

# import random
# import string
# from datetime import date
# import datetime

# class Dog():
#     def __init__(self, Name, size, Breed = 'Unknown', dob = 'Unknown'):
#         self.Name = Name.title()
#         self.size = size
#         self.Breed = Breed
#         self.dob = dob

#     def Bark(self):
#         print('woof!')
        
#     def get_name(self):
#         print(f'{self.Name}')
        
#     # def set_name(self, length):
#     #     new_name = ''.join(random.choices(string.ascii_letters, k = length))
#     #     new_name.title()
#     #     print(f'{new_name}')
    
#     def set_name(self, new_name):
#         self.Name = new_name
#         print(new_name.title())
      
#     # def calculateAge(dob):
#     #     today = date.today()
#     #     age = today.year - dob.year -((today.month, today.day) <
#     #         (dob.month, dob.day))
#     #     return age * 7

#     # method to see dog years
#     def new_age(self):
#         Year_of_birth = int(self.Date_of_Birth[6:])
#         current_year = datetime.datetime.now().year
#         Current_age = current_year - Year_of_birth
#         print("Your current age is ", (Current_age))

# dog1 = Dog('sporty', 6, 'pug', '20/5/2021')
# print(dog1.Name)

# dog1.Bark()
# # dog1.dog_years()
# dog1.set_name('benzie')

# dog1.dog_years()


# shuffling of list items and displaying result through indexing
# import random

# mylist = ["apple", "banana", "cherry"]
# random.shuffle(mylist)
# print(mylist[0])






        




    






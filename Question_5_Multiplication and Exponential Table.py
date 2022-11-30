# # Sol: 1
print("Welcome to Multiplication/Exponent Table App")

name = input("\nHello, what is your name:\t" )
num = float(input("What number would you like to work with: "))
print(f"\nMultiplication Table for {num}\n")

for count in range(1, 10):      
   print (count, '*', num, '=', round(num * count,2))

print(f"\nExponent Table For {num}\n")
for count in range(1, 10):      
   print (num, '**', count, '=', round(num ** count,4))

print(name.capitalize() + " " + "Math is cool!")
print(f"\t{name} Math is cool!")
print(f"\t\t{name.capitalize()} Math is cool!")
print(f"\t\t\t{name.upper()} MATH IS COOL!")


# # Sol: 2
# Welcome message
print("Welcome to Multiplication/Exponent App")

# user name
name = str(input("What is your name: "))

# number input
num = float(input("What number you want to work with: "))

# calculations multi
print(f"\nMultiplication table for {num}")

for i in range(1, 10):
    print(f"\t {i} x {num} = {round(num * i, 2)}")

# exponent
print(f"\nExponent table for {num}")
for i in range(1, 10):
    print(f"\t {i} x {num} = {round(num ** i, 2)}")

# strings
print(f"{name.capitalize()} math is cool")
print(f"\t{name.lower()} math is cool")
print(f"\t\t{name.capitalize()} Math is cool")
print(f"\t\t\t{name.upper()} Math is cool")

# # Sol:3
# #Multiplication table 
print('Welcome to the Multiplication/Exponent Table App\n')
name = input('Hello, what is your name:')
num = float(input('What number would you like to work:'))
print('Multiplication table for',{num})
for i in range(1,10):
    print(i,'x',num, '=',round(num*i,2))
#Exponential table
print('Multiplication',{num})
for i in range(1,10):
    print(num,'x',i, '=',round(num**i,2))
print('Exponential table for',{num})

print("Welcome to the Multiplication/Exponent Table App\n")
name = input("Hello, what is your name:\t").title().strip()
num = float(input("What number would you like to work with: "))
print(f"\nMultiplication Table for {num}\n")

for i in range(1, 10):
    print(f"\t {i} * {num} = {round(num*i, 2)}")

print(f"\nExponent Table For {num}\n")
for i in range(1, 10):
    print(f"\t{num} ** {i} = {round(num**i,4)}")

message = name + " " + "Math is cool!"
print("\n" + message)
print("\t" + message.lower())
print("\t\t" + message.capitalize())
print("\t\t\t" + message.upper())

# Sol: 4

print("Welcome to the Multiplication/Exponent Table App\n")
name = input("Hello, what is your name:\t").title().strip()
num = float(input("What number would you like to work with: "))

print(f"\nMultiplication Table for {num}\n")
print("\t 1.0 * " + str(num) + ' = ' + str(round(num*1,2)))
print("\t 2.0 * " + str(num) + ' = ' + str(round(num*2,2)))
print("\t 3.0 * " + str(num) + ' = ' + str(round(num*3,2)))
print("\t 4.0 * " + str(num) + ' = ' + str(round(num*4,2)))
print("\t 5.0 * " + str(num) + ' = ' + str(round(num*5,2)))
print("\t 6.0 * " + str(num) + ' = ' + str(round(num*6,2)))
print("\t 7.0 * " + str(num) + ' = ' + str(round(num*7,2)))
print("\t 8.0 * " + str(num) + ' = ' + str(round(num*8,2)))
print("\t 9.0 * " + str(num) + ' = ' + str(round(num*9,2)))

print(f"\nExponent Table For {num}\n")
print("\t" + str(num) + ' ** ' + ' 1 ' + ' = ' + str(round(num*1, 4)))
print("\t" + str(num) + ' ** ' + ' 2 ' + ' = ' + str(round(num*2, 4)))
print("\t" + str(num) + ' ** ' + ' 3 ' + ' = ' + str(round(num**3, 4)))
print("\t" + str(num) + ' ** ' + ' 4 ' + ' = ' + str(round(num**4, 4)))
print("\t" + str(num) + ' ** ' + ' 5 ' + ' = ' + str(round(num**5, 4)))
print("\t" + str(num) + ' ** ' + ' 6 ' + ' = ' + str(round(num**6, 4)))
print("\t" + str(num) + ' ** ' + ' 7 ' + ' = ' + str(round(num**7, 4)))
print("\t" + str(num) + ' ** ' + ' 8 ' + ' = ' + str(round(num**8, 4)))
print("\t" + str(num) + ' ** ' + ' 9 ' + ' = ' + str(round(num**9, 4)))

message = name + " " + "Math is cool!"
print("\n" + message)
print("\t" + message.lower())
print("\t\t" + message.title())
print("\t\t\t" + message.upper())














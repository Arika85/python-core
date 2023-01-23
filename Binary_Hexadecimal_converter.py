# Sol:1 

# Welcome note
print("Welcome to the Binary/Hexadecimal Converter App\n")

#user input values
values = int(input("Compute binary and hexadecimal values up to the following decimal number: "))
print("Generating lists....complete!")

print("\nUsing slices, we will now show a portion of each list.")
decimal_start = int(input("What decimal number would you like to start at: "))
decimal_stop = int(input("What decimal number would you like to stop at: "))

# displaying decimal values
print(f"\nDecimal values from {decimal_start} to {decimal_stop}:")
for start in range(decimal_start, decimal_stop+1):
    print(start)

# displaying binary values
print(f"\nBinary values from {decimal_start} to {decimal_stop}:")
for start in range(decimal_start, decimal_stop+1):
    print(bin(start))

# displaying hexadecial values
print(f"\nHexadecimal values from {decimal_start} to {decimal_stop}:")
for start in range(decimal_start, decimal_stop+1):
    print(hex(start))

print(f"\nPress Enter to see all values from 1 to {values}")
print("Decimal----Binary----Hexadecimal")
print("--------------------------------------------------------")

for i in range(1,values+1):
    print(i, end = '----')
    print(bin(i),end = '----')
    print(hex(i))
    

# sol: 2
print("Welcome to Binary/Hexadecimal Converter App.")

# taking user input
val_1 = int(input("\nCompute binary and hexadecimal values up to the following decimal number: "))

# generating list
numers_list = list(range(1, val_1 + 1))
print("Generating list................Commplete!")

# portion of list
print("\nWe will now portion of each list.")
start_dec = int(input("What decimal number would you like to start: "))
stop_dec = int(input("What decimal number would you like to start: "))

# decimal
print(f"\nDecimal values from {start_dec} to {stop_dec}")
for dec in range(start_dec, stop_dec + 1):
    print(dec)

# binary
print(f"\nBinary values from {start_dec} to {stop_dec}")
for dec in range(start_dec, stop_dec + 1):
    print(bin(dec))

# binary
print(f"\nHexadecimal values from {start_dec} to {stop_dec}")
for dec in range(start_dec, stop_dec + 1):
    print(hex(dec))

# pass
enter = input(f"\nPress enter to see all the results from 1 to {val_1}.")

# looping all
print("\nDecimal----Binary----Hexadecimal")
print("-------------------------------------------------")

for i in range(1, val_1 + 1):
    print(f"{i} ---- {bin(i)} ---- {hex(i)}")








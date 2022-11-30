# # Question: 3
# Type : 1
print("Welcome to the Temperature Conversion Program\n")
df = float(input("What is the given temperature in degrees Fahrenheit:  "))

cel = (df-32)*5/9
kel = (df-32)*5/9+273.15

print(f"\nDegrees Fahrenheit: \t{round(df,2)}")
print(f"Degrees Celsius: \t{round(cel,4)}")
print(f"Degrees Kelvin: \t{round(kel,4)}")

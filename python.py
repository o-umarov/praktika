# Issue 14.1
print("Omaddiyor Umarov Abdurakhim Ugli")
print("I am 26 years old now")
print(" I am studying in Korrea now")

# Issue 14.2
name = input("What is your name: ")
print(f"Let's do some math, {name}")
x = int(input("First Number: "))
y = int(input("Second Number"))
print(f"Addition: {x+y}")
print(f"Subtraction: {x-y}")
print(f"Multiplication: {x*y}")
print(f"Division: {x/y:.2f}")
print(f"Remainder: {x % y}")  # qoldiq qismini topish
print(f"Integer Part: {x//y}")  # butun qismini topish
print(f"Exponent: {x**y}")  # darajasini topish


# Issue 14.3
print("Input in SECONDS: ")
total_seconds = int(input("Total Seconds: "))
hours = total_seconds//3600
minutes = total_seconds % 3600//60
remaining_seconds = (total_seconds % 3600) % 60
print(
    f"time in standard fractions: {hours} HOUR : {minutes} MIN : {remaining_seconds} SEC")

# Issue 14.4
fahrenheit = float(input("Input in fahrenheit: "))
celsius = (fahrenheit - 32)/1.8
print(f"in Celsius: {celsius:.2f}")
print("------------------------------------")
kilometer = float(input("Input in kilometer: "))
mile = kilometer*0.621371
print(f"in Miles: {mile:.2f}")
print("------------------------------------")
kilos = float(input("Input in kilos: "))
pound = kilos*2.20462
print(f"in Pounds: {pound:.2f}")

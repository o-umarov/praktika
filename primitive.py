import math

# # Issue 16.1

int_type = 18
print(f"Int Type: {type(int_type)}")
float_type = 19.45
print(f"Float Type: {type(float_type)}")
string_type = "Jason"
print(f"String Type: {type(string_type)}")
boolean_type = 10 < 9
print(f"Boolean Type: {type(boolean_type)}")
none_type = None
print(f"None Type: {type(none_type)}")

print("------------------------")
# Issue 16.2
radius = float(input("Input of circle radius: "))
square = (math.pi*radius**2)
length = (2*math.pi*radius)
print(
    f"Circle Square: {square:.2f} && Circle Length: {length:.2f}")

print("------------------------")
# Issue 16.3

print(type(7/2))  # float
print(type(7//2))  # int
print(type(-7/2))  # float
print(type(0.1+0.2 == 0.3))  # bool
print(type(int('12') + float(3.5)))  # float
print(type(bool("")))
print(type(bool("0")))
print(type("5"*3))
print(True + False)


print("------------------------")

# Issue 16.4
name = input("Your name: ")
print(
    f"Name: {name.strip().title()}. Character in the name: {len(name)}. The first char: {name[0]} and the last char: {name[-1]} and the reverse version: {(name[::-1]).title()}")

# 1. Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
# Input = 2024
# Output = LEAP YEAR

year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")


# 2. Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 = side 3

side1 = float(input("Enter the side 1 :"))
side2 = float(input("Enter the side 2 :"))
side3 = float(input("Enter the side 3 :"))

if side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
    print("The given side lengths do not form a valid triangle.")
else:
    # Check the type of triangle
    if side1 == side2 == side3:
        print("The triangle is equilateral (Eq)")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("The triangle is isosceles (Iso)")
    else:
        print("The triangle is scalene")


# 3. Task - Fibonacci series and Factorial
# Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24

factorial = int(input("Enter the Number:\n"))
num = 1
for i in range(1, factorial + 1):
    num = num * i
print(f" The Factorial of {factorial} is {num} ")




# 4. Fibonaci series
#  0,0+1, 0+1+1,
#  n = 7
#  0, 1, 2, 3, 5, 8, 13

number=int(input("Enter the Fibonacci Number:\n"))
x = 0
y = 1
print(x)
print(y)
for i in range(2,number):
    z = x+y
    x=y
    y=z
    print(z)
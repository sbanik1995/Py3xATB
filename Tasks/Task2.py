# 1. Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
def calculate_square_and_cube(number):

    square = number ** 2

    cube = number ** 3

    return square, cube



number = float(input("Enter a number: "))

square, cube = calculate_square_and_cube(number)

print(f"The square of {number} is {square}")

print(f"The cube of {number} is {cube}")



# 2. Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number

def compare_numbers(num1, num2):

    if num1 > num2:

        return "The first number is greater than the second number."

    elif num1 < num2:

        return "The first number is less than the second number."

    else:

        return "The first number is equal to the second number."

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(num1 if num1 > num2 else num2)

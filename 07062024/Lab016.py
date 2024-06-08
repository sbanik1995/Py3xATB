# Take the 2 int numbers from the user and we want to add them
# We need to use the input() function

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
result = num1 + num2
print(result)

# type conversion :- str -> int -> ? = int()

result = int(num1) + int(num2)
print(result)

# + -> int -> sum operation
# + -> str -> concat operation
# int to str -> str()
# str to int -> int()

print(type(int(num1)))
print(type(int(num2)))

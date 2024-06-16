# Conditions
# age>18 -> You are allowed to go the club
# age<18 -> You are not allowed to go the club

# sourav -> goa -> father permission
# sourav -> no goa> no father permission

# If, ELSE
# Syntax
# if condition:
#       code to be executed
# else:
#       code to be executed when condition is false

# Write a program to take a user age and let him know if he can go to the club or not
#  Take a user input

age = int(input("Enter your age: "))
if age >= 18:
    print("You are allowed to go the club")
else:
    print("You are not allowed to go the club")

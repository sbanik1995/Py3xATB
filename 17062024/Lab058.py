# Functions -> Block of code which can be executed or reused
# Define the function
# Call the function
from os import name

# Built in Functions -> Which are created by Python Contributors

result = max(2, 3)


# User defined functions
# They can return something
# # They can't return -> Non return
# # They have parameters
# # They don't have parameters / arguments
#
def say_hello():
    print("Hello")


say_hello()
result = say_hello()
print(result)


def say_hello_arg(name):
    print("Hello", name)


say_hello_arg("Sourav")
say_hello_arg("Amit")

result = say_hello_arg("Sourav")
print(result)

# No return type with default arguments



def say_hello_arg_default(name=" Sumit "):
    print("Hello", name)

say_hello_arg_default()
say_hello_arg_default("Amit")
say_hello_arg_default(name="Sangita")






def sum_number_argument_ret(a,b):
    return a+b


result1 = sum_number_argument_ret(3,4)
print(result1)

result2 = sum_number_argument_ret(a=20, b=30)
print(result2)

result3 = sum_number_argument_ret(50, 60)
print(result3)

result4 = sum_number_argument_ret(b=70, a=80)
print(result4)
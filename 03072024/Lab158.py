# try, except and finally

try:
    num1 = int(input("Enter the first number:\n "))
    num2 = int(input("Enter the second number:\n: "))
    result = num1/num2

except ValueError as ve:
    print(ve)
except ZeroDivisionError as zde:
    print(zde)
else:
    print(f'Result is {result}')

finally:
    print(" I will be executed anyhow!! ")


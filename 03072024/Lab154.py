print("-- Start of the Program -- ")

try:
    a = int(input("\nEnter the num1"))
    b = int(input("\nEnter the num2"))
    c = a/b
    print("Result Div is", c)

except Exception as e:
    print(e)
    print("Please enter integer!")



print("--End of the Program--")

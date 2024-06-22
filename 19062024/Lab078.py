# Lambda arguments : Expressions


def find_odd_even(num):
    if num%2 == 0:
        print("Even")
    else:
        print("Odd")

find_odd_even(6)



# Using Lambda
check_even_odd = lambda num: "Even" if num%2 == 0 else "Odd"
print(check_even_odd(10))

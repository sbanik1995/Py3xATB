# Recursion -> It is a programming technique where a function calls itself in order to solve a problem

# Key concepts -> Base case, Recursive case

# Base case -> A condition that stops the recursion (Termination condition)

# Recursive case -> A call to the same function with a different input (Recursive step)


# Factorial
def factorial(n):
    # Base case:
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n-1)

print(factorial(5))

# Program -> Calculate the area of circle
# input -> radius
# outout -> area

import math

# datatypes
# input -> int or float -> float
# output -> float

# core logic -> pi*r*r = 3.14

radius = float(input("Enter the radius\n"))
print(math.pi)
area = math.pi * (radius ** 2)
area2 = math.pi * (math.pow(radius, 2))
print(area)
print(area2)

# args -> Any number of arguments

print("Sourav", "Amit", "SB")



def sum3(a,b,c):
    return a+b+c


result = sum3(2,3,4)
print(result)



def sum_three(a=1, b=1, c=1):
    return a+b+c

result1 = sum_three()
result2 = sum_three(1,2)
result3 = sum_three(1,2,3)
result4 = sum_three(a=10, b=60, c=50)
result5 = sum_three(b=60, a=10, c=50)
print(result1, result2, result3, result4,result5)




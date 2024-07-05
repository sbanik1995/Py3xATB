#   print("dads")   #Indentation Error

# result = 5 + "5"  #Type Error

# int("pramod")     #Value Error

# print(undefined_variable)     #Name Error

# my_list =[1,2,3]
# print(my_list[3])  #Index Error

# my_dict = {"a":1 , "b":2}
# print(my_dict["c"])  #Key Error

# result = 10/0     # Zero Division Error

# import non_existent_module    #Module Not Found Error

# import math
# math.exp(1000)    #Overflow Error


try:
    import math
    math.exp(1000)
except Exception as e:
    print(e)

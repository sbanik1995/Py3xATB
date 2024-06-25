# map -> pick one item and apply the function and give same number

numbers = [1,2,3,4,5,6,7,8,9,10]

def double_me(num):
    return num*2

new_list_double = map(double_me,numbers)
print(list(new_list_double))




# Filters -> pick item, if true then keep it, if false then remove it
# it can give less number of items as compared to actual list


def even_giver(num):
    return num % 2 == 0

new_filtered_list = list(filter(even_giver, numbers))
print(new_filtered_list)

# lambda
new_filtered_list1 = list(filter(lambda num: num % 2 == 0, numbers))
print(new_filtered_list1)

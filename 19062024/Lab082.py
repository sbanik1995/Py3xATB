# Double list elements

list = [1,2,3,4,5]

temp_list = []

for i in list:
    temp = i*2
    temp_list.append(temp)


print(temp_list)


# Map()
# 1. Takes each item from the list
# 2. Execute the function on it
# 3. Return same number of elements(list)

my_list = [2,3,4,5,6]
def double_item(num):
    return num*2

double_my_list = list(map(double_item,my_list))
print(double_my_list)






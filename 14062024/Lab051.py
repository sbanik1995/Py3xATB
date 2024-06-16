# Break -> Based on the condition it will kick you out of the loop




# Pass -> ? -> pass do nothing -> it skips the code -> Not out of the loop

for i in range(10):
    if i == 5:
        pass
    else:
        print(i)


for i in range(20):
    if i == 8 or i == 12:
        pass
    else:
        print(i)


set1 = set([" TheTestingAcademy", " For", " TheTestingAcademy."])
print(len(set1))


for i in set1:
    print(i)


set2 = set([1,2,3,4,5,6,7,8,9,10,11,12])
print(set2)
print(len(set2))


set2.remove(5)
print(set2)
print(len(set2))


set2.add(100)
print(set2)


set2.pop()
print(set2)

class Parent:
    gold = "2kg"

    def BHK2(self):
        print("2 BHK flat")


class Child(Parent):

    def BHK3(self):
        print("3 BHK flat")

child_object = Child()
child_object.BHK2()
child_object.BHK3()
print(child_object.gold)

father_object_ref = Parent()
# father_object_ref.BHK2()
# father_object_ref.gold()

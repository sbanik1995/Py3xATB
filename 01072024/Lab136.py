# Hierarchical Inheritance -> Father - Multiple Children

class Father:
    def BHK1(self):
        print("This is BHK1")

class Pramod(Father):
    def BHK2(self):
        print("This is BHK2")

class Sourav(Father):
    def BHK3(self):
        print("This is BHK3")

class Amit(Father):
    def no_house(self):
        print("No house")


pramod = Pramod()
pramod.BHK1()
pramod.BHK2()

sourav = Sourav()
sourav.BHK1()
sourav.BHK3()

amit = Amit()
amit.BHK1()
amit.no_house()

# Multiple Inheritance

class Father:
    def father_money(self):
        return "5"

        def home(self):
            return "This is from Father"


class Mother:
    def mother_money(self):
        return "10"

    def home(self):
        return "This is from Mother"


class Child(Mother, Father):
    def home(self):
        return "This is from Child"


child = Child()
child.father_money()
child.mother_money()
print(child.home())
